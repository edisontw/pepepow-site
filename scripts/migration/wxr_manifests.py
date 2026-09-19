#!/usr/bin/env python3
"""Generate route and media manifests from a WordPress WXR export.

Raw WXR files and generated working manifests stay outside Git. This tool emits
only migration metadata needed for URL preservation and media recovery; it does
not export author login/email data or post body content.
"""

from __future__ import annotations

import argparse
import json
import re
import xml.etree.ElementTree as ET
from pathlib import Path
from urllib.parse import urlparse

NS = {
    "content": "http://purl.org/rss/1.0/modules/content/",
    "wp": "http://wordpress.org/export/1.2/",
}
PDF_RE = re.compile(
    r"https?://[^\\s\\\"'<>]+\\.pdf(?:\\?[^\\s\\\"'<>]*)?",
    re.IGNORECASE,
)


def text(node: ET.Element, path: str) -> str:
    value = node.findtext(path, default="", namespaces=NS)
    return (value or "").strip()


def clean_urls(values: list[str]) -> list[str]:
    return sorted({value.rstrip(".,;)") for value in values if value})


def legacy_path(url: str) -> str:
    if not url:
        return ""
    return urlparse(url).path or "/"


def categories_and_tags(node: ET.Element) -> tuple[list[str], list[str]]:
    categories: list[str] = []
    tags: list[str] = []
    for category in node.findall("category"):
        label = (category.text or "").strip()
        domain = (category.attrib.get("domain") or "").strip()
        if not label:
            continue
        if domain == "category":
            categories.append(label)
        elif domain == "post_tag":
            tags.append(label)
    return sorted(set(categories)), sorted(set(tags))


def attached_file(node: ET.Element) -> str:
    for meta in node.findall("wp:postmeta", NS):
        key = text(meta, "wp:meta_key")
        if key == "_wp_attached_file":
            return text(meta, "wp:meta_value")
    return ""


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("wxr", type=Path, help="Canonical WordPress WXR export")
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=Path("migration/work"),
        help="Ignored local working directory.",
    )
    parser.add_argument(
        "--recovered-slug",
        action="append",
        default=[],
        help="Published page/post slug already recovered in Git. May be repeated.",
    )
    args = parser.parse_args()

    if not args.wxr.is_file():
        parser.error(f"WXR file not found: {args.wxr}")

    root = ET.parse(args.wxr).getroot()
    channel = root.find("channel")
    if channel is None:
        raise RuntimeError(f"No RSS channel found in {args.wxr}")

    recovered = set(args.recovered_slug)
    routes: list[dict[str, object]] = []
    attachments: list[dict[str, str]] = []
    pdf_urls: list[str] = []

    for node in channel.findall("item"):
        post_type = text(node, "wp:post_type")
        status = text(node, "wp:status")
        slug = text(node, "wp:post_name")
        link = text(node, "link")
        content = text(node, "content:encoded")
        categories, tags = categories_and_tags(node)

        pdf_urls.extend(PDF_RE.findall(content))

        if post_type in {"page", "post"} and status == "publish":
            path = legacy_path(link)
            planned_path = "/" if post_type == "page" and slug == "home-new" else path
            routes.append(
                {
                    "wordpress_id": text(node, "wp:post_id"),
                    "post_type": post_type,
                    "title": text(node, "title"),
                    "slug": slug,
                    "published": text(node, "wp:post_date_gmt")
                    or text(node, "wp:post_date"),
                    "modified": text(node, "wp:post_modified_gmt")
                    or text(node, "wp:post_modified"),
                    "legacy_url": link,
                    "legacy_path": path,
                    "planned_path": planned_path,
                    "categories": categories,
                    "tags": tags,
                    "recovery_state": (
                        "recovered_draft" if slug in recovered else "pending_recovery"
                    ),
                }
            )

        if post_type == "attachment":
            attachment_url = text(node, "wp:attachment_url")
            if attachment_url.lower().split("?", 1)[0].endswith(".pdf"):
                pdf_urls.append(attachment_url)
            attachments.append(
                {
                    "wordpress_id": text(node, "wp:post_id"),
                    "title": text(node, "title"),
                    "published": text(node, "wp:post_date_gmt")
                    or text(node, "wp:post_date"),
                    "parent_id": text(node, "wp:post_parent"),
                    "attachment_url": attachment_url,
                    "upload_path": attached_file(node),
                }
            )

    routes.sort(key=lambda item: (str(item["post_type"]), str(item["legacy_path"])))
    attachments.sort(key=lambda item: int(item["wordpress_id"] or 0))
    pdf_urls = clean_urls(pdf_urls)

    args.output_dir.mkdir(parents=True, exist_ok=True)
    (args.output_dir / "legacy-routes.json").write_text(
        json.dumps(
            {
                "source": args.wxr.name,
                "published_route_count": len(routes),
                "routes": routes,
            },
            ensure_ascii=False,
            indent=2,
        )
        + "\n",
        encoding="utf-8",
    )
    (args.output_dir / "media-manifest.json").write_text(
        json.dumps(
            {
                "source": args.wxr.name,
                "attachment_count": len(attachments),
                "attachments": attachments,
                "referenced_pdf_count": len(pdf_urls),
                "referenced_pdf_urls": pdf_urls,
            },
            ensure_ascii=False,
            indent=2,
        )
        + "\n",
        encoding="utf-8",
    )

    page_count = sum(item["post_type"] == "page" for item in routes)
    post_count = sum(item["post_type"] == "post" for item in routes)
    print(
        f"Published routes: {len(routes)} "
        f"({page_count} pages, {post_count} posts)"
    )
    print(f"Attachments: {len(attachments)}")
    print(f"Referenced PDFs: {len(pdf_urls)}")
    print(f"Wrote working manifests to: {args.output_dir}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
