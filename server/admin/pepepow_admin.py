#!/usr/bin/env python3
"""Minimal CGI backend for pepepow.net/admin/.

Security model:
- GitHub OAuth authenticates the human publisher.
- Only allowlisted GitHub usernames receive a signed short-lived session.
- The OAuth token is discarded after identity verification.
- A separate fine-grained GitHub token, stored only in /etc/pepepow-admin/config.json,
  is used to create announcement files in one repository.
- Publish requests are constrained to src/content/announcements/.
- No database or long-running application server is required.
"""

from __future__ import annotations

import base64
import hashlib
import hmac
import json
import os
import re
import secrets
import sys
import time
from datetime import datetime, timezone
from http.cookies import SimpleCookie
from urllib import error, parse, request

DEFAULT_CONFIG = "/etc/pepepow-admin/config.json"
COOKIE_SESSION = "pepepow_admin_session"
COOKIE_STATE = "pepepow_admin_oauth_state"
COOKIE_PKCE = "pepepow_admin_oauth_pkce"
MAX_BODY_BYTES = 200_000
ALLOWED_CATEGORIES = {
    "Update",
    "Wallet",
    "Mining",
    "Masternode",
    "Network",
    "Market",
    "Community",
    "Campaigns",
}


class ApiError(Exception):
    def __init__(self, status: int, message: str):
        super().__init__(message)
        self.status = status
        self.message = message


def load_config() -> dict:
    path = os.environ.get("PEPEPOW_ADMIN_CONFIG", DEFAULT_CONFIG)
    try:
        with open(path, "r", encoding="utf-8") as handle:
            cfg = json.load(handle)
    except Exception as exc:
        raise ApiError(503, f"Publisher configuration unavailable: {exc}") from exc

    required = [
        "github_client_id",
        "github_client_secret",
        "github_publish_token",
        "session_secret",
        "allowed_users",
    ]
    missing = [key for key in required if not cfg.get(key)]
    if missing:
        raise ApiError(503, "Publisher configuration is incomplete.")

    cfg.setdefault("repo", "edisontw/pepepow-site")
    cfg.setdefault("branch", "main")
    cfg.setdefault("site_origin", "https://pepepow.net")
    cfg.setdefault("session_hours", 8)
    cfg["allowed_users"] = {str(x).lower() for x in cfg["allowed_users"]}
    return cfg


def status_text(status: int) -> str:
    return {
        200: "OK",
        201: "Created",
        204: "No Content",
        302: "Found",
        400: "Bad Request",
        401: "Unauthorized",
        403: "Forbidden",
        404: "Not Found",
        405: "Method Not Allowed",
        409: "Conflict",
        413: "Payload Too Large",
        500: "Internal Server Error",
        502: "Bad Gateway",
        503: "Service Unavailable",
    }.get(status, "Error")


def output_headers(status: int, headers: list[tuple[str, str]] | None = None) -> None:
    print(f"Status: {status} {status_text(status)}")
    print("Cache-Control: no-store")
    print("X-Content-Type-Options: nosniff")
    print("Referrer-Policy: no-referrer")
    for key, value in headers or []:
        print(f"{key}: {value}")
    print()


def json_response(status: int, payload: dict, headers: list[tuple[str, str]] | None = None) -> None:
    body = json.dumps(payload, ensure_ascii=False, separators=(",", ":"))
    all_headers = [("Content-Type", "application/json; charset=utf-8")]
    all_headers.extend(headers or [])
    output_headers(status, all_headers)
    print(body)


def redirect(location: str, headers: list[tuple[str, str]] | None = None) -> None:
    all_headers = [("Location", location)]
    all_headers.extend(headers or [])
    output_headers(302, all_headers)


def b64url_encode(raw: bytes) -> str:
    return base64.urlsafe_b64encode(raw).rstrip(b"=").decode("ascii")


def b64url_decode(value: str) -> bytes:
    padding = "=" * ((4 - len(value) % 4) % 4)
    return base64.urlsafe_b64decode((value + padding).encode("ascii"))


def sign_value(value: str, secret: str) -> str:
    digest = hmac.new(secret.encode("utf-8"), value.encode("utf-8"), hashlib.sha256).digest()
    return b64url_encode(digest)


def make_session(login: str, cfg: dict) -> str:
    now = int(time.time())
    payload = {
        "login": login,
        "iat": now,
        "exp": now + int(cfg["session_hours"]) * 3600,
    }
    encoded = b64url_encode(json.dumps(payload, separators=(",", ":")).encode("utf-8"))
    return f"{encoded}.{sign_value(encoded, cfg['session_secret'])}"


def verify_session(token: str, cfg: dict) -> dict:
    try:
        encoded, signature = token.split(".", 1)
    except ValueError as exc:
        raise ApiError(401, "Invalid session.") from exc

    expected = sign_value(encoded, cfg["session_secret"])
    if not hmac.compare_digest(signature, expected):
        raise ApiError(401, "Invalid session.")

    try:
        payload = json.loads(b64url_decode(encoded))
    except Exception as exc:
        raise ApiError(401, "Invalid session.") from exc

    login = str(payload.get("login", "")).lower()
    if not login or int(payload.get("exp", 0)) < int(time.time()):
        raise ApiError(401, "Session expired.")
    if login not in cfg["allowed_users"]:
        raise ApiError(403, "This GitHub account is not allowed to publish.")
    return payload


def get_cookies() -> SimpleCookie:
    cookie = SimpleCookie()
    raw = os.environ.get("HTTP_COOKIE", "")
    if raw:
        cookie.load(raw)
    return cookie


def cookie_header(
    name: str,
    value: str,
    *,
    max_age: int | None = None,
    http_only: bool = True,
    same_site: str = "Lax",
) -> tuple[str, str]:
    parts = [f"{name}={value}", "Path=/", "Secure", f"SameSite={same_site}"]
    if http_only:
        parts.append("HttpOnly")
    if max_age is not None:
        parts.append(f"Max-Age={max_age}")
    return ("Set-Cookie", "; ".join(parts))


def clear_cookie(name: str) -> tuple[str, str]:
    return cookie_header(name, "", max_age=0)


def current_route() -> str:
    params = parse.parse_qs(os.environ.get("QUERY_STRING", ""), keep_blank_values=True)
    action = (params.get("action") or [""])[0].strip().lower()
    return "/" + action if action else "/"


def require_method(method: str) -> None:
    actual = os.environ.get("REQUEST_METHOD", "GET").upper()
    if actual != method:
        raise ApiError(405, f"Use {method} for this endpoint.")


def require_same_origin(cfg: dict) -> None:
    origin = os.environ.get("HTTP_ORIGIN", "")
    if origin != cfg["site_origin"]:
        raise ApiError(403, "Invalid request origin.")


def read_json_body() -> dict:
    raw_length = os.environ.get("CONTENT_LENGTH", "0") or "0"
    try:
        length = int(raw_length)
    except ValueError as exc:
        raise ApiError(400, "Invalid Content-Length.") from exc
    if length < 0 or length > MAX_BODY_BYTES:
        raise ApiError(413, "Request is too large.")
    raw = sys.stdin.buffer.read(length)
    try:
        value = json.loads(raw.decode("utf-8") if raw else "{}")
    except Exception as exc:
        raise ApiError(400, "Invalid JSON request.") from exc
    if not isinstance(value, dict):
        raise ApiError(400, "Request must be a JSON object.")
    return value


def github_request(
    method: str,
    url: str,
    *,
    token: str | None = None,
    data: dict | None = None,
    form: dict | None = None,
    accept: str = "application/vnd.github+json",
) -> tuple[int, dict]:
    headers = {
        "Accept": accept,
        "User-Agent": "pepepow.net-admin",
        "X-GitHub-Api-Version": "2022-11-28",
    }
    body = None

    if token:
        headers["Authorization"] = f"Bearer {token}"

    if data is not None:
        body = json.dumps(data, separators=(",", ":")).encode("utf-8")
        headers["Content-Type"] = "application/json"
    elif form is not None:
        body = parse.urlencode(form).encode("utf-8")
        headers["Content-Type"] = "application/x-www-form-urlencoded"

    req = request.Request(url, data=body, method=method, headers=headers)
    try:
        with request.urlopen(req, timeout=15) as response:
            raw = response.read()
            payload = json.loads(raw.decode("utf-8")) if raw else {}
            return response.status, payload
    except error.HTTPError as exc:
        raw = exc.read()
        try:
            payload = json.loads(raw.decode("utf-8")) if raw else {}
        except Exception:
            payload = {}
        message = payload.get("message") or f"GitHub request failed with HTTP {exc.code}."
        raise ApiError(exc.code if exc.code in {400, 401, 403, 404, 409} else 502, message) from exc
    except Exception as exc:
        raise ApiError(502, "GitHub could not be reached.") from exc


def authenticated_user(cfg: dict) -> dict:
    cookies = get_cookies()
    morsel = cookies.get(COOKIE_SESSION)
    if morsel is None:
        raise ApiError(401, "Sign in required.")
    return verify_session(morsel.value, cfg)


def oauth_login(cfg: dict) -> None:
    require_method("GET")
    state = secrets.token_urlsafe(32)
    code_verifier = secrets.token_urlsafe(64)
    code_challenge = b64url_encode(hashlib.sha256(code_verifier.encode("ascii")).digest())
    params = {
        "client_id": cfg["github_client_id"],
        "redirect_uri": f"{cfg['site_origin']}/admin-api?action=callback",
        "scope": "read:user",
        "state": state,
        "code_challenge": code_challenge,
        "code_challenge_method": "S256",
        "allow_signup": "false",
    }
    redirect(
        "https://github.com/login/oauth/authorize?" + parse.urlencode(params),
        [
            cookie_header(COOKIE_STATE, state, max_age=600),
            cookie_header(COOKIE_PKCE, code_verifier, max_age=600),
        ],
    )


def oauth_callback(cfg: dict) -> None:
    require_method("GET")
    params = parse.parse_qs(os.environ.get("QUERY_STRING", ""), keep_blank_values=True)
    code = (params.get("code") or [""])[0]
    state = (params.get("state") or [""])[0]

    cookies = get_cookies()
    state_cookie = cookies.get(COOKIE_STATE)
    pkce_cookie = cookies.get(COOKIE_PKCE)
    expected_state = state_cookie.value if state_cookie else ""
    code_verifier = pkce_cookie.value if pkce_cookie else ""

    if not code or not state or not expected_state or not hmac.compare_digest(state, expected_state):
        raise ApiError(400, "OAuth state validation failed.")
    if not code_verifier:
        raise ApiError(400, "OAuth PKCE validation data is missing.")

    _, token_payload = github_request(
        "POST",
        "https://github.com/login/oauth/access_token",
        form={
            "client_id": cfg["github_client_id"],
            "client_secret": cfg["github_client_secret"],
            "code": code,
            "redirect_uri": f"{cfg['site_origin']}/admin-api?action=callback",
            "code_verifier": code_verifier,
        },
        accept="application/json",
    )

    access_token = token_payload.get("access_token")
    if not access_token:
        raise ApiError(502, "GitHub did not return an access token.")

    _, user_payload = github_request(
        "GET",
        "https://api.github.com/user",
        token=access_token,
    )

    login = str(user_payload.get("login", "")).lower()
    if login not in cfg["allowed_users"]:
        raise ApiError(403, "This GitHub account is not allowed to publish.")

    session = make_session(login, cfg)
    redirect(
        f"{cfg['site_origin']}/admin/?signed_in=1",
        [
            cookie_header(COOKIE_SESSION, session, max_age=int(cfg["session_hours"]) * 3600),
            clear_cookie(COOKIE_STATE),
            clear_cookie(COOKIE_PKCE),
        ],
    )


def session_status(cfg: dict) -> None:
    require_method("GET")
    user = authenticated_user(cfg)
    json_response(200, {"authenticated": True, "login": user["login"]})


def logout(cfg: dict) -> None:
    require_method("POST")
    require_same_origin(cfg)
    json_response(200, {"ok": True}, [clear_cookie(COOKIE_SESSION)])


def slugify(value: str) -> str:
    value = value.strip().lower()
    value = re.sub(r"[^a-z0-9]+", "-", value)
    return value.strip("-")[:80]


def valid_tag(value: str) -> bool:
    return bool(value) and len(value) <= 50 and "\n" not in value and "\r" not in value


def make_markdown(payload: dict) -> tuple[str, str, str]:
    title = str(payload.get("title", "")).strip()
    description = str(payload.get("description", "")).strip()
    raw_date = str(payload.get("date", "")).strip()
    date_key = str(payload.get("date_key", "")).strip()
    requested_slug = str(payload.get("slug", "")).strip()
    body = str(payload.get("body", "")).strip()
    featured = bool(payload.get("featured", False))

    if not title or len(title) > 180 or "\n" in title or "\r" in title:
        raise ApiError(400, "Title is required and must be one line under 180 characters.")
    if len(description) > 300:
        raise ApiError(400, "Summary must be under 300 characters.")
    if not body or len(body) > 100_000:
        raise ApiError(400, "Announcement body is required and must be under 100,000 characters.")
    if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", date_key):
        raise ApiError(400, "Invalid publication date.")

    try:
        parsed_date = datetime.fromisoformat(raw_date.replace("Z", "+00:00"))
        if parsed_date.tzinfo is None:
            parsed_date = parsed_date.replace(tzinfo=timezone.utc)
        canonical_date = parsed_date.astimezone(timezone.utc).isoformat().replace("+00:00", "Z")
    except Exception as exc:
        raise ApiError(400, "Invalid publication timestamp.") from exc

    slug = slugify(requested_slug or title)
    if not slug:
        slug = "announcement-" + parsed_date.astimezone(timezone.utc).strftime("%Y%m%d-%H%M%S")
    if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", slug):
        raise ApiError(400, "Slug may contain only lowercase letters, numbers, and hyphens.")

    raw_categories = payload.get("categories") or []
    if not isinstance(raw_categories, list):
        raise ApiError(400, "Categories must be a list.")
    categories = []
    for value in raw_categories:
        category = str(value).strip()
        if category not in ALLOWED_CATEGORIES:
            raise ApiError(400, f"Unsupported category: {category}")
        if category not in categories:
            categories.append(category)
    categories = ["Announcements", *categories]

    raw_tags = payload.get("tags") or []
    if not isinstance(raw_tags, list) or len(raw_tags) > 10:
        raise ApiError(400, "Use at most 10 tags.")
    tags = []
    for value in raw_tags:
        tag = str(value).strip()
        if not valid_tag(tag):
            raise ApiError(400, "Each tag must be 1–50 characters and stay on one line.")
        if tag not in tags:
            tags.append(tag)

    yaml_string = lambda value: json.dumps(value, ensure_ascii=False)
    lines = [
        "---",
        f"title: {yaml_string(title)}",
        f"description: {yaml_string(description)}",
        f"date: {yaml_string(canonical_date)}",
        f"slug: {yaml_string(slug)}",
        f"categories: {json.dumps(categories, ensure_ascii=False)}",
        f"tags: {json.dumps(tags, ensure_ascii=False)}",
        'status: "published"',
        f"featured: {'true' if featured else 'false'}",
        "migration_review: false",
        "---",
        "",
        body,
        "",
    ]
    markdown = "\n".join(lines)
    path = f"src/content/announcements/{date_key}-{slug}.md"
    public_path = f"/{slug}/"
    return path, public_path, markdown


def publish(cfg: dict) -> None:
    require_method("POST")
    require_same_origin(cfg)
    user = authenticated_user(cfg)
    payload = read_json_body()
    path, public_path, markdown = make_markdown(payload)

    owner_repo = cfg["repo"]
    encoded_path = parse.quote(path, safe="/")
    contents_url = f"https://api.github.com/repos/{owner_repo}/contents/{encoded_path}"

    query_url = contents_url + "?" + parse.urlencode({"ref": cfg["branch"]})
    try:
        github_request("GET", query_url, token=cfg["github_publish_token"])
    except ApiError as exc:
        if exc.status != 404:
            raise
    else:
        raise ApiError(409, "An announcement with this date and slug already exists.")

    commit_message = f"content: publish announcement {path.rsplit('/', 1)[-1][:-3]}"
    _, created = github_request(
        "PUT",
        contents_url,
        token=cfg["github_publish_token"],
        data={
            "message": commit_message,
            "content": base64.b64encode(markdown.encode("utf-8")).decode("ascii"),
            "branch": cfg["branch"],
        },
    )

    commit = created.get("commit") or {}
    commit_url = commit.get("html_url") or f"https://github.com/{owner_repo}/commits/{commit.get('sha', '')}"

    json_response(
        201,
        {
            "ok": True,
            "published_by": user["login"],
            "path": path,
            "public_path": public_path,
            "commit_url": commit_url,
        },
    )


def main() -> None:
    try:
        cfg = load_config()
        route = current_route()

        if route == "/login":
            oauth_login(cfg)
        elif route == "/callback":
            oauth_callback(cfg)
        elif route == "/session":
            session_status(cfg)
        elif route == "/logout":
            logout(cfg)
        elif route == "/publish":
            publish(cfg)
        else:
            raise ApiError(404, "Unknown publisher endpoint.")
    except ApiError as exc:
        json_response(exc.status, {"error": exc.message})
    except Exception:
        json_response(500, {"error": "Publisher API failed unexpectedly."})


if __name__ == "__main__":
    main()
