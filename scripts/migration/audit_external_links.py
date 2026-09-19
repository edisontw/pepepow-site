#!/usr/bin/env python3
"""Inventory and optionally probe external links used by current PEPEPOW pages.

This is a migration/review aid. HTTP failures are classified conservatively:
401/403/429 and network errors are not treated as proof that a service is dead.
The script writes its JSON report under migration/work/ by default.
"""

from __future__ import annotations

import argparse
import concurrent.futures
import json
import re
import urllib.error
import urllib.request
from collections import defaultdict
from pathlib import Path
from typing import Any
from urllib.parse import quote, urlsplit, urlunsplit

DEFAULT_PATHS = (
    Path("src/content/pages/home.md"),
    Path("src/content/pages/about.md"),
    Path("src/content/pages/mining.md"),
    Path("src/content/pages/masternode.md"),
    Path("src/content/pages/wallet.md"),
    Path("src/content/pages/market.md"),
)
URL_RE = re.compile(r"https?://[^\s<>()\[\]\"']+", re.IGNORECASE)
USER_AGENT = "pepepow-site-link-audit/1.0 (+https://pepepow.net)"
BLOCKED_STATUSES = {401, 403, 429}
MISSING_STATUSES = {404, 410}


def markdown_body(text: str) -> str:
    if not text.startswith("---\n"):
        return text
    end = text.find("\n---\n", 4)
    return text[end + 5 :] if end >= 0 else text


def clean_url(value: str) -> str:
    return value.rstrip(chr(96) + ".,;:!?")


def requestable_url(url: str) -> str:
    parts = urlsplit(url)
    try:
        netloc = parts.netloc.encode("idna").decode("ascii")
    except UnicodeError:
        netloc = parts.netloc
    path = quote(parts.path, safe="/%:@+~!$&()*;,=")
    query = quote(parts.query, safe="=&%:@/?+~!$()*;,")
    fragment = quote(parts.fragment, safe="%:@/?+~!$&()*;,=")
    return urlunsplit((parts.scheme, netloc, path, query, fragment))


def request_once(url: str, method: str, timeout: float) -> dict[str, Any]:
    headers = {"User-Agent": USER_AGENT}
    if method == "GET":
        headers["Range"] = "bytes=0-0"
    request = urllib.request.Request(
        requestable_url(url),
        headers=headers,
        method=method,
    )
    with urllib.request.urlopen(request, timeout=timeout) as response:
        return {
            "status": response.status,
            "method": method,
            "final_url": response.geturl(),
            "content_type": response.headers.get("Content-Type", ""),
            "error": "",
        }


def classify(status: int | None, error: str) -> str:
    if status is not None and 200 <= status < 400:
        return "available"
    if status in BLOCKED_STATUSES:
        return "blocked"
    if status in MISSING_STATUSES:
        return "missing"
    if error:
        return "unresolved"
    return "http_error"


def probe(url: str, timeout: float) -> dict[str, Any]:
    for method in ("HEAD", "GET"):
        try:
            result = request_once(url, method, timeout)
            return {
                "url": url,
                **result,
                "classification": classify(result["status"], ""),
            }
        except urllib.error.HTTPError as exc:
            status = exc.code
            if method == "HEAD" and status in {403, 405, 501}:
                continue
            error = f"HTTPError: {exc}"
            return {
                "url": url,
                "status": status,
                "method": method,
                "final_url": exc.geturl() or url,
                "content_type": (
                    exc.headers.get("Content-Type", "") if exc.headers else ""
                ),
                "error": error,
                "classification": classify(status, error),
            }
        except Exception as exc:
            if method == "HEAD":
                continue
            error = f"{type(exc).__name__}: {exc}"
            return {
                "url": url,
                "status": None,
                "method": method,
                "final_url": url,
                "content_type": "",
                "error": error,
                "classification": "unresolved",
            }

    return {
        "url": url,
        "status": None,
        "method": "",
        "final_url": url,
        "content_type": "",
        "error": "No request completed",
        "classification": "unresolved",
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "paths",
        nargs="*",
        type=Path,
        help="Markdown/MDX files to audit; defaults to the six current public pages.",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=Path("migration/work/external-link-audit.json"),
    )
    parser.add_argument("--timeout", type=float, default=12.0)
    parser.add_argument("--workers", type=int, default=8)
    parser.add_argument(
        "--inventory-only",
        action="store_true",
        help="Extract URLs without making network requests.",
    )
    parser.add_argument(
        "--strict-missing",
        action="store_true",
        help="Exit non-zero only for confirmed HTTP 404/410 results.",
    )
    args = parser.parse_args()

    paths = args.paths or list(DEFAULT_PATHS)
    if args.workers < 1:
        parser.error("--workers must be at least 1")
    if args.timeout <= 0:
        parser.error("--timeout must be positive")

    sources: dict[str, set[str]] = defaultdict(set)
    missing_files: list[str] = []
    for path in paths:
        if not path.is_file():
            missing_files.append(path.as_posix())
            continue
        body = markdown_body(path.read_text(encoding="utf-8"))
        for match in URL_RE.finditer(body):
            url = clean_url(match.group(0))
            if url:
                sources[url].add(path.as_posix())

    if missing_files:
        parser.error("Input file(s) not found: " + ", ".join(missing_files))

    urls = sorted(sources)
    if args.inventory_only:
        results = [
            {
                "url": url,
                "sources": sorted(sources[url]),
                "classification": "not_probed",
            }
            for url in urls
        ]
    else:
        with concurrent.futures.ThreadPoolExecutor(max_workers=args.workers) as pool:
            probed = list(pool.map(lambda url: probe(url, args.timeout), urls))
        results = [
            {**item, "sources": sorted(sources[item["url"]])}
            for item in probed
        ]

    counts: dict[str, int] = defaultdict(int)
    for item in results:
        counts[str(item["classification"])] += 1

    payload = {
        "paths": [path.as_posix() for path in paths],
        "unique_external_urls": len(urls),
        "counts": dict(sorted(counts.items())),
        "results": results,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        json.dumps(payload, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )

    print(f"External URLs: {len(urls)}")
    print(" | ".join(f"{key}: {value}" for key, value in sorted(counts.items())))
    print(f"Wrote: {args.output}")

    if args.strict_missing and counts.get("missing", 0):
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
