#!/usr/bin/env python3
"""Probe legacy media URLs from a generated migration media manifest.

This tool checks availability and response metadata only. It does not download
or commit legacy media. Run it locally after wxr_manifests.py has produced
migration/work/media-manifest.json.
"""

from __future__ import annotations

import argparse
import concurrent.futures
import json
import urllib.error
import urllib.request
from pathlib import Path
from typing import Any

USER_AGENT = "pepepow-site-migration/1.0 (+https://pepepow.net)"


def request_once(url: str, method: str, timeout: float) -> dict[str, Any]:
    headers = {"User-Agent": USER_AGENT}
    if method == "GET":
        headers["Range"] = "bytes=0-0"
    request = urllib.request.Request(url, headers=headers, method=method)
    with urllib.request.urlopen(request, timeout=timeout) as response:
        return {
            "ok": 200 <= response.status < 400,
            "status": response.status,
            "method": method,
            "final_url": response.geturl(),
            "content_type": response.headers.get("Content-Type", ""),
            "content_length": response.headers.get("Content-Length", ""),
            "error": "",
        }


def probe(url: str, timeout: float) -> dict[str, Any]:
    try:
        return {"url": url, **request_once(url, "HEAD", timeout)}
    except urllib.error.HTTPError as exc:
        if exc.code not in {403, 405, 501}:
            return {
                "url": url,
                "ok": False,
                "status": exc.code,
                "method": "HEAD",
                "final_url": exc.geturl() or url,
                "content_type": exc.headers.get("Content-Type", "") if exc.headers else "",
                "content_length": exc.headers.get("Content-Length", "") if exc.headers else "",
                "error": f"HTTP {exc.code}",
            }
    except (urllib.error.URLError, TimeoutError, OSError):
        pass

    try:
        return {"url": url, **request_once(url, "GET", timeout)}
    except urllib.error.HTTPError as exc:
        return {
            "url": url,
            "ok": False,
            "status": exc.code,
            "method": "GET",
            "final_url": exc.geturl() or url,
            "content_type": exc.headers.get("Content-Type", "") if exc.headers else "",
            "content_length": exc.headers.get("Content-Length", "") if exc.headers else "",
            "error": f"HTTP {exc.code}",
        }
    except (urllib.error.URLError, TimeoutError, OSError) as exc:
        return {
            "url": url,
            "ok": False,
            "status": None,
            "method": "GET",
            "final_url": url,
            "content_type": "",
            "content_length": "",
            "error": str(exc),
        }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "manifest",
        type=Path,
        nargs="?",
        default=Path("migration/work/media-manifest.json"),
        help="Manifest produced by wxr_manifests.py.",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=Path("migration/work/media-probe.json"),
        help="Ignored JSON result path.",
    )
    parser.add_argument("--timeout", type=float, default=12.0)
    parser.add_argument("--workers", type=int, default=8)
    parser.add_argument(
        "--strict",
        action="store_true",
        help="Exit non-zero when one or more URLs remain unresolved.",
    )
    parser.add_argument(
        "--limit",
        type=int,
        default=0,
        help="Probe only the first N attachment URLs; 0 means all.",
    )
    args = parser.parse_args()

    if not args.manifest.is_file():
        parser.error(f"Manifest not found: {args.manifest}")
    if args.workers < 1:
        parser.error("--workers must be at least 1")
    if args.timeout <= 0:
        parser.error("--timeout must be positive")

    payload = json.loads(args.manifest.read_text(encoding="utf-8"))
    attachments = payload.get("attachments", [])
    urls = []
    seen = set()
    for attachment in attachments:
        url = str(attachment.get("attachment_url", "")).strip()
        if url and url not in seen:
            seen.add(url)
            urls.append(url)

    if args.limit > 0:
        urls = urls[: args.limit]

    with concurrent.futures.ThreadPoolExecutor(max_workers=args.workers) as pool:
        results = list(pool.map(lambda url: probe(url, args.timeout), urls))

    available = sum(bool(item["ok"]) for item in results)
    missing = len(results) - available
    output = {
        "source_manifest": str(args.manifest),
        "probed": len(results),
        "available": available,
        "unresolved": missing,
        "results": results,
    }

    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        json.dumps(output, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    print(
        f"Probed: {len(results)} | available: {available} | unresolved: {missing}"
    )
    print(f"Wrote: {args.output}")
    return 2 if args.strict and missing else 0


if __name__ == "__main__":
    raise SystemExit(main())
