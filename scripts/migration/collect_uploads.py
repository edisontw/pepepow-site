#!/usr/bin/env python3
"""Collect canonical WordPress upload files needed by the PEPEPOW migration.

The script is read-only with respect to the WordPress uploads tree. It reads the
sanitized media manifest, copies only `_wp_attached_file` paths into a separate
working directory, and writes a machine-readable recovery report.
"""

from __future__ import annotations

import argparse
import json
import shutil
from pathlib import Path
from typing import Any


def safe_relative_path(value: str) -> Path:
    path = Path(value)
    if not value or path.is_absolute() or ".." in path.parts:
        raise ValueError(f"unsafe upload path: {value!r}")
    return path


def ensure_within(root: Path, candidate: Path) -> None:
    root_resolved = root.resolve()
    candidate_resolved = candidate.resolve(strict=False)
    try:
        candidate_resolved.relative_to(root_resolved)
    except ValueError as exc:
        raise ValueError(f"path escapes uploads root: {candidate}") from exc


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "manifest",
        type=Path,
        nargs="?",
        default=Path("migration/public/media-manifest.json"),
    )
    parser.add_argument(
        "--uploads-root",
        type=Path,
        required=True,
        help="Local WordPress wp-content/uploads directory.",
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=Path("migration/work/recovered-uploads"),
        help="Separate destination directory; source files are never modified.",
    )
    parser.add_argument(
        "--report",
        type=Path,
        default=Path("migration/work/uploads-collection.json"),
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Check availability without copying files.",
    )
    parser.add_argument(
        "--overwrite",
        action="store_true",
        help="Replace destination files that already exist.",
    )
    args = parser.parse_args()

    if not args.manifest.is_file():
        parser.error(f"Manifest not found: {args.manifest}")
    if not args.uploads_root.is_dir():
        parser.error(f"Uploads root not found: {args.uploads_root}")

    payload = json.loads(args.manifest.read_text(encoding="utf-8"))
    attachments = payload.get("attachments", [])

    found: list[dict[str, Any]] = []
    missing: list[dict[str, Any]] = []
    external: list[dict[str, Any]] = []
    invalid: list[dict[str, Any]] = []

    for attachment in attachments:
        upload_path = str(attachment.get("upload_path", "")).strip()
        item = {
            "wordpress_id": str(attachment.get("wordpress_id", "")),
            "title": str(attachment.get("title", "")),
            "attachment_url": str(attachment.get("attachment_url", "")),
            "upload_path": upload_path,
        }

        if not upload_path:
            external.append(item)
            continue

        try:
            relative = safe_relative_path(upload_path)
            source = args.uploads_root / relative
            ensure_within(args.uploads_root, source)
        except ValueError as exc:
            item["error"] = str(exc)
            invalid.append(item)
            continue

        if not source.is_file():
            missing.append(item)
            continue

        destination = args.output_dir / relative
        copied = False

        if not args.dry_run:
            destination.parent.mkdir(parents=True, exist_ok=True)
            if args.overwrite or not destination.exists():
                shutil.copy2(source, destination)
                copied = True

        item["source"] = str(source)
        item["destination"] = str(destination)
        item["copied"] = copied
        item["size_bytes"] = source.stat().st_size
        found.append(item)

    result = {
        "source_manifest": str(args.manifest),
        "uploads_root": str(args.uploads_root),
        "output_dir": str(args.output_dir),
        "dry_run": args.dry_run,
        "attachment_count": len(attachments),
        "found_count": len(found),
        "missing_count": len(missing),
        "external_count": len(external),
        "invalid_count": len(invalid),
        "found": found,
        "missing": missing,
        "external": external,
        "invalid": invalid,
    }

    args.report.parent.mkdir(parents=True, exist_ok=True)
    args.report.write_text(
        json.dumps(result, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )

    print(
        f"Attachments: {len(attachments)} | found: {len(found)} | "
        f"missing: {len(missing)} | external: {len(external)} | "
        f"invalid: {len(invalid)}"
    )
    print(f"Report: {args.report}")
    if not args.dry_run:
        print(f"Recovered files: {args.output_dir}")

    return 2 if invalid else 0


if __name__ == "__main__":
    raise SystemExit(main())
