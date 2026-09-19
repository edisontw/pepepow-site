#!/usr/bin/env python3
"""Create a privacy-conscious inventory from one or more WordPress WXR exports.

The raw WXR files are migration inputs and should remain outside Git. This script
extracts only fields needed for migration planning and URL/media recovery. It
intentionally omits author login/email metadata and post body content.
"""

from __future__ import annotations

import argparse
import csv
import json
import re
import sys
import xml.etree.ElementTree as ET
from collections import Counter
from dataclasses import asdict, dataclass
from pathlib import Path
from urllib.parse import urlparse

NS = {
    "content": "http://purl.org/rss/1.0/modules/content/",
    "dc": "http://purl.org/dc/elements/1.1/",
    "wp": "http://wordpress.org/export/1.2/",
}

UPLOAD_RE = re.compile(
    r"https?://[^\\s\\\"'<>]+/wp-content/uploads/[^\\s\\\"'<>]+",
    re.IGNORECASE,
)
PDF_RE = re.compile(
    r"https?://[^\\s\\\"'<>]+\\.pdf(?:\\?[^\\s\\\"'<>]*)?",
    re.IGNORECASE,
)


@dataclass
class Item:
    source: str
    wp_id: str
    post_type: str
    status: str
    title: str
    slug: str
    published: str
    modified: str
    legacy_url: str
    legacy_path: str
    categories: list[str]
    tags: list[str]
    attachment_url: str
    parent_id: str
    media_urls: list[str]
    pdf_urls: list[str]


def text(node: ET.Element, path: str) -> str:
    value = node.findtext(path, default="", namespaces=NS)
    return (value or "").strip()


def unique_sorted(values: list[str]) -> list[str]:
    return sorted({value.rstrip(".,;)") for value in values if value})


def path_from_url(url: str) -> str:
    if not url:
        return ""
    parsed = urlparse(url)
    return parsed.path or "/"


def parse_wxr(path: Path) -> list[Item]:
    try:
        tree = ET.parse(path)
    except ET.ParseError as exc:
        raise RuntimeError(f"Invalid XML in {path}: {exc}") from exc

    channel = tree.getroot().find("channel")
    if channel is None:
        raise RuntimeError(f"No RSS channel found in {path}")

    items: list[Item] = []

    for node in channel.findall("item"):
        content = text(node, "content:encoded")
        link = text(node, "link")
        attachment = text(node, "wp:attachment_url")

        categories: list[str] = []
        tags: list[str] = []

        for category in node.findall("category"):
            domain = (category.attrib.get("domain") or "").strip()
            label = (category.text or "").strip()
            if not label:
                continue
            if domain == "category":
                categories.append(label)
            elif domain == "post_tag":
                tags.append(label)

        media_urls = UPLOAD_RE.findall(content)
        if attachment and "/wp-content/uploads/" in attachment:
            media_urls.append(attachment)

        pdf_urls = PDF_RE.findall(content)
        if attachment.lower().split("?", 1)[0].endswith(".pdf"):
            pdf_urls.append(attachment)

        items.append(
            Item(
                source=path.name,
                wp_id=text(node, "wp:post_id"),
                post_type=text(node, "wp:post_type"),
                status=text(node, "wp:status"),
                title=text(node, "title"),
                slug=text(node, "wp:post_name"),
                published=text(node, "wp:post_date_gmt") or text(node, "wp:post_date"),
                modified=text(node, "wp:post_modified_gmt") or text(node, "wp:post_modified"),
                legacy_url=link,
                legacy_path=path_from_url(link),
                categories=unique_sorted(categories),
                tags=unique_sorted(tags),
                attachment_url=attachment,
                parent_id=text(node, "wp:post_parent"),
                media_urls=unique_sorted(media_urls),
                pdf_urls=unique_sorted(pdf_urls),
            )
        )

    return items


def summarize(items_by_source: dict[str, list[Item]]) -> dict:
    summary: dict[str, object] = {"sources": {}}
    attachment_maps: dict[str, dict[str, str]] = {}

    for source, items in items_by_source.items():
        type_status = Counter((item.post_type, item.status) for item in items)
        published_pages = [
            {"title": item.title, "slug": item.slug, "path": item.legacy_path}
            for item in items
            if item.post_type == "page" and item.status == "publish"
        ]
        published_posts = [
            item for item in items
            if item.post_type == "post" and item.status == "publish"
        ]
        category_counts = Counter(
            category
            for item in published_posts
            for category in item.categories
        )
        attachment_urls = {
            item.wp_id: item.attachment_url
            for item in items
            if item.post_type == "attachment" and item.attachment_url
        }
        attachment_maps[source] = attachment_urls

        summary["sources"][source] = {
            "total_items": len(items),
            "type_status_counts": [
                {"post_type": key[0], "status": key[1], "count": value}
                for key, value in sorted(type_status.items())
            ],
            "published_posts": len(published_posts),
            "published_pages": len(published_pages),
            "attachments": sum(
                1 for item in items if item.post_type == "attachment"
            ),
            "published_page_routes": published_pages,
            "published_post_categories": dict(sorted(category_counts.items())),
            "unique_media_urls_referenced": len(
                {url for item in items for url in item.media_urls}
            ),
            "unique_pdf_urls_referenced": len(
                {url for item in items for url in item.pdf_urls}
            ),
        }

    if len(attachment_maps) > 1:
        source_names = sorted(attachment_maps)
        base = source_names[0]
        base_map = attachment_maps[base]
        comparisons = []

        for other in source_names[1:]:
            other_map = attachment_maps[other]
            shared_ids = set(base_map) & set(other_map)
            comparisons.append(
                {
                    "base": base,
                    "other": other,
                    "base_attachment_count": len(base_map),
                    "other_attachment_count": len(other_map),
                    "shared_attachment_ids": len(shared_ids),
                    "same_url_for_shared_ids": sum(
                        base_map[item_id] == other_map[item_id]
                        for item_id in shared_ids
                    ),
                    "only_in_base_ids": sorted(
                        set(base_map) - set(other_map),
                        key=lambda value: int(value or 0),
                    ),
                    "only_in_other_ids": sorted(
                        set(other_map) - set(base_map),
                        key=lambda value: int(value or 0),
                    ),
                }
            )

        summary["attachment_comparisons"] = comparisons

    return summary


def write_csv(path: Path, items: list[Item]) -> None:
    fields = [
        "source",
        "wp_id",
        "post_type",
        "status",
        "title",
        "slug",
        "published",
        "modified",
        "legacy_url",
        "legacy_path",
        "categories",
        "tags",
        "attachment_url",
        "parent_id",
        "media_urls",
        "pdf_urls",
    ]

    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()

        for item in items:
            row = asdict(item)
            for key in ("categories", "tags", "media_urls", "pdf_urls"):
                row[key] = " | ".join(row[key])
            writer.writerow(row)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "wxr",
        nargs="+",
        type=Path,
        help="WordPress WXR XML export(s)",
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=Path("migration/work"),
        help="Local working output. Keep this directory out of Git.",
    )
    args = parser.parse_args()

    for path in args.wxr:
        if not path.is_file():
            parser.error(f"WXR file not found: {path}")

    args.output_dir.mkdir(parents=True, exist_ok=True)

    items_by_source = {
        path.name: parse_wxr(path)
        for path in args.wxr
    }
    all_items = [
        item
        for items in items_by_source.values()
        for item in items
    ]
    summary = summarize(items_by_source)

    (args.output_dir / "inventory.json").write_text(
        json.dumps(
            [asdict(item) for item in all_items],
            indent=2,
            ensure_ascii=False,
        )
        + "\n",
        encoding="utf-8",
    )
    write_csv(args.output_dir / "inventory.csv", all_items)
    (args.output_dir / "summary.json").write_text(
        json.dumps(summary, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )

    print(json.dumps(summary, indent=2, ensure_ascii=False))
    print(
        f"\nWrote privacy-conscious working inventory to: {args.output_dir}",
        file=sys.stderr,
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
