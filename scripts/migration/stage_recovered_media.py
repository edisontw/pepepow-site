#!/usr/bin/env python3
"""Stage recovered legacy media into the Astro public tree.

The source recovery directory is never modified. Canonical WordPress attachment
files are copied to stable public paths, a checksum-backed media map is written,
and Markdown/MDX content can optionally have legacy upload URLs rewritten.

PDFs go to /docs/legacy/YYYY/MM/... and other media go to
/media/legacy/YYYY/MM/....
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import shutil
from pathlib import Path, PurePosixPath
from urllib.parse import unquote, urlsplit

UPLOAD_URL_RE = re.compile(
    r"https?://(?:www\.)?pepepow\.org/wp-content/uploads/"
    r"(?P<path>[^\s\"'<>\)\]]+)",
    re.IGNORECASE,
)
THUMBNAIL_SUFFIX_RE = re.compile(r"-(\d{2,5})x(\d{2,5})(?=\.[^.]+$)")


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def safe_upload_path(value: str) -> PurePosixPath:
    path = PurePosixPath(value)
    if not value or path.is_absolute() or ".." in path.parts:
        raise ValueError(f"unsafe upload path: {value!r}")
    return path


def public_path_for(upload_path: PurePosixPath) -> str:
    prefix = "docs/legacy" if upload_path.suffix.lower() == ".pdf" else "media/legacy"
    return "/" + str(PurePosixPath(prefix) / upload_path)


def content_files(content_root: Path) -> list[Path]:
    result: list[Path] = []
    for suffix in ("*.md", "*.mdx"):
        result.extend(content_root.rglob(suffix))
    return sorted(path for path in result if not path.name.startswith("_"))


def resolve_upload_reference(
    raw_path: str,
    by_upload_path: dict[str, str],
) -> str | None:
    path = unquote(raw_path.split("?", 1)[0].split("#", 1)[0]).lstrip("/")
    if path in by_upload_path:
        return by_upload_path[path]

    candidate = THUMBNAIL_SUFFIX_RE.sub("", path)
    if candidate in by_upload_path:
        return by_upload_path[candidate]

    return None


def rewrite_content(
    root: Path,
    by_upload_path: dict[str, str],
    *,
    apply: bool,
) -> dict[str, object]:
    changed_files: list[str] = []
    unresolved: set[str] = set()
    replacements = 0

    for path in content_files(root):
        original = path.read_text(encoding="utf-8")

        def replace(match: re.Match[str]) -> str:
            nonlocal replacements
            resolved = resolve_upload_reference(match.group("path"), by_upload_path)
            if not resolved:
                unresolved.add(match.group(0))
                return match.group(0)
            replacements += 1
            return resolved

        updated = UPLOAD_URL_RE.sub(replace, original)
        if updated != original:
            changed_files.append(str(path))
            if apply:
                path.write_text(updated, encoding="utf-8")

    return {
        "apply": apply,
        "replacement_count": replacements,
        "changed_file_count": len(changed_files),
        "changed_files": changed_files,
        "unresolved_url_count": len(unresolved),
        "unresolved_urls": sorted(unresolved),
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--recovered-root",
        type=Path,
        default=Path("migration/work/recovered-uploads"),
    )
    parser.add_argument(
        "--manifest",
        type=Path,
        default=Path("migration/public/media-manifest.json"),
    )
    parser.add_argument(
        "--public-root",
        type=Path,
        default=Path("public"),
    )
    parser.add_argument(
        "--map-output",
        type=Path,
        default=Path("migration/public/media-map.json"),
    )
    parser.add_argument(
        "--content-root",
        type=Path,
        default=Path("src/content"),
    )
    parser.add_argument(
        "--audit-only",
        action="store_true",
        help="Validate and report recovered files without copying them.",
    )
    parser.add_argument(
        "--rewrite-content",
        action="store_true",
        help="Rewrite resolvable legacy upload URLs in Markdown/MDX.",
    )
    parser.add_argument(
        "--overwrite",
        action="store_true",
        help="Overwrite existing staged public files.",
    )
    args = parser.parse_args()

    if not args.manifest.is_file():
        parser.error(f"Manifest not found: {args.manifest}")
    if not args.recovered_root.is_dir():
        parser.error(f"Recovered media directory not found: {args.recovered_root}")

    payload = json.loads(args.manifest.read_text(encoding="utf-8"))
    attachments = payload.get("attachments", [])

    records: list[dict[str, object]] = []
    missing: list[str] = []
    invalid: list[str] = []
    external: list[dict[str, str]] = []
    by_upload_path: dict[str, str] = {}
    total_bytes = 0

    for attachment in attachments:
        upload_value = str(attachment.get("upload_path", "")).strip()
        attachment_url = str(attachment.get("attachment_url", "")).strip()

        if not upload_value:
            external.append(
                {
                    "wordpress_id": str(attachment.get("wordpress_id", "")),
                    "attachment_url": attachment_url,
                }
            )
            continue

        try:
            upload_path = safe_upload_path(upload_value)
        except ValueError:
            invalid.append(upload_value)
            continue

        source = args.recovered_root.joinpath(*upload_path.parts)
        if not source.is_file():
            missing.append(upload_value)
            continue

        public_url = public_path_for(upload_path)
        destination = args.public_root / public_url.lstrip("/")
        size_bytes = source.stat().st_size
        total_bytes += size_bytes

        record = {
            "wordpress_id": str(attachment.get("wordpress_id", "")),
            "title": str(attachment.get("title", "")),
            "upload_path": upload_value,
            "legacy_url": attachment_url,
            "public_url": public_url,
            "size_bytes": size_bytes,
            "sha256": sha256_file(source),
        }
        records.append(record)
        by_upload_path[upload_value] = public_url

        if not args.audit_only:
            destination.parent.mkdir(parents=True, exist_ok=True)
            if args.overwrite or not destination.exists():
                shutil.copy2(source, destination)

    rewrite_report = rewrite_content(
        args.content_root,
        by_upload_path,
        apply=args.rewrite_content and not args.audit_only,
    )

    output = {
        "source_manifest": str(args.manifest),
        "recovered_root": str(args.recovered_root),
        "audit_only": args.audit_only,
        "canonical_file_count": len(records),
        "external_attachment_count": len(external),
        "missing_count": len(missing),
        "invalid_count": len(invalid),
        "total_bytes": total_bytes,
        "files": records,
        "external_attachments": external,
        "missing": missing,
        "invalid": invalid,
        "content_rewrite": rewrite_report,
    }

    if not args.audit_only:
        args.map_output.parent.mkdir(parents=True, exist_ok=True)
        args.map_output.write_text(
            json.dumps(output, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )

    print(
        f"Canonical files: {len(records)} | external: {len(external)} | "
        f"missing: {len(missing)} | invalid: {len(invalid)}"
    )
    print(f"Total bytes: {total_bytes}")
    print(
        "Content URLs: "
        f"{rewrite_report['replacement_count']} resolvable | "
        f"{rewrite_report['unresolved_url_count']} unresolved"
    )
    if args.audit_only:
        print("Audit only: no files were copied and no content was modified.")
    else:
        print(f"Media map: {args.map_output}")

    return 2 if missing or invalid else 0


if __name__ == "__main__":
    raise SystemExit(main())
