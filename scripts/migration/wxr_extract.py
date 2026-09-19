#!/usr/bin/env python3
"""Stage published WordPress WXR content as cleaned Markdown candidates.

This is a migration aid, not a publisher. Output belongs in migration/work/ and
must be reviewed before copying into src/content/. It strips WordPress/Elementor
presentation code but does not fact-check historical text, software versions,
links, commands, or security-sensitive instructions.
"""

from __future__ import annotations

import argparse
import re
import xml.etree.ElementTree as ET
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path

from bs4 import BeautifulSoup, Comment
from markdownify import markdownify as to_markdown

NS = {
    "content": "http://purl.org/rss/1.0/modules/content/",
    "wp": "http://wordpress.org/export/1.2/",
}

DROP_TAGS = {
    "style",
    "script",
    "link",
    "noscript",
    "iframe",
    "form",
    "input",
    "button",
    "svg",
}
ALLOWED_ATTRS = {"a": {"href", "title"}, "img": {"src", "alt", "title"}}
WHITESPACE_LINES = re.compile(r"\n{3,}")
LEGACY_HOST_RE = re.compile(
    r"https?://(?:www\.)?pepepow\.org(?P<path>/[^\s<>\)\"']*)?",
    re.IGNORECASE,
)
WORDPRESS_EMOJI_RE = re.compile(
    r"!\[[^\]]*\]\("
    r"https://s\.w\.org/images/core/emoji/[^)]+/svg/"
    r"(?P<codepoints>[0-9a-fA-F-]+)\.svg"
    r"\)"
)
OBSOLETE_WORDPRESS_PATHS = (
    "/wp-admin/",
    "/wp-includes/",
    "/wp-json/",
    "/category/",
    "/tag/",
    "/author/",
)


@dataclass
class Entry:
    title: str
    slug: str
    post_type: str
    status: str
    published: str
    modified: str
    legacy_url: str
    categories: list[str]
    tags: list[str]
    html: str


def text(node: ET.Element, path: str) -> str:
    value = node.findtext(path, default="", namespaces=NS)
    return (value or "").strip()


def parse_entries(path: Path) -> list[Entry]:
    root = ET.parse(path).getroot()
    channel = root.find("channel")
    if channel is None:
        raise RuntimeError(f"No RSS channel found in {path}")

    entries: list[Entry] = []
    for node in channel.findall("item"):
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

        entries.append(
            Entry(
                title=text(node, "title"),
                slug=text(node, "wp:post_name"),
                post_type=text(node, "wp:post_type"),
                status=text(node, "wp:status"),
                published=text(node, "wp:post_date_gmt") or text(node, "wp:post_date"),
                modified=text(node, "wp:post_modified_gmt") or text(node, "wp:post_modified"),
                legacy_url=text(node, "link"),
                categories=sorted(set(categories)),
                tags=sorted(set(tags)),
                html=text(node, "content:encoded"),
            )
        )
    return entries


def clean_html(html: str) -> str:
    soup = BeautifulSoup(html, "html.parser")

    for comment in soup.find_all(string=lambda value: isinstance(value, Comment)):
        comment.extract()

    for tag_name in DROP_TAGS:
        for tag in soup.find_all(tag_name):
            tag.decompose()

    for tag in soup.find_all(True):
        keep = ALLOWED_ATTRS.get(tag.name, set())
        tag.attrs = {
            key: value
            for key, value in tag.attrs.items()
            if key in keep
        }

    return str(soup)


def _wordpress_emoji(match: re.Match[str]) -> str:
    try:
        return "".join(
            chr(int(codepoint, 16))
            for codepoint in match.group("codepoints").split("-")
        )
    except (ValueError, OverflowError):
        return ""


def _localize_legacy_url(match: re.Match[str]) -> str:
    path = match.group("path") or "/"
    if path.startswith("/wp-content/") or path.startswith(OBSOLETE_WORDPRESS_PATHS):
        return match.group(0)
    return path


def sanitize_migration_markdown(markdown: str) -> str:
    """Remove reproducible WordPress chrome and localize same-site public links."""
    markdown = markdown.replace("\xa0", " ")
    markdown = WORDPRESS_EMOJI_RE.sub(_wordpress_emoji, markdown)

    clean_lines: list[str] = []
    for line in markdown.splitlines():
        stripped = line.strip().lower()
        if stripped.startswith("skip render:"):
            continue
        lowered = line.lower()
        if any(
            f"pepepow.org{prefix}" in lowered
            for prefix in ("/wp-admin/", "/category/", "/tag/")
        ):
            continue
        clean_lines.append(line)

    markdown = "\n".join(clean_lines)
    markdown = LEGACY_HOST_RE.sub(_localize_legacy_url, markdown)
    markdown = WHITESPACE_LINES.sub("\n\n", markdown)
    return markdown.strip()


def markdown_from_html(html: str) -> str:
    cleaned = clean_html(html)
    markdown = to_markdown(
        cleaned,
        heading_style="ATX",
        bullets="-",
        strip=["span"],
    )
    return sanitize_migration_markdown(markdown)

def yaml_string(value: str) -> str:
    escaped = (
        value.replace("\\", "\\\\")
        .replace('"', '\\"')
        .replace("\n", " ")
    )
    return f'"{escaped}"'


def yaml_list(values: list[str]) -> str:
    if not values:
        return "[]"
    return "[" + ", ".join(yaml_string(value) for value in values) + "]"


def normalize_date(value: str) -> str:
    if not value or value.startswith("0000-00-00"):
        return ""
    try:
        return datetime.fromisoformat(value).isoformat(sep=" ")
    except ValueError:
        return value


def render_candidate(entry: Entry) -> str:
    frontmatter = [
        "---",
        f"title: {yaml_string(entry.title)}",
        'description: ""',
        f"date: {yaml_string(normalize_date(entry.published))}",
    ]

    if entry.modified:
        frontmatter.append(
            f"updated: {yaml_string(normalize_date(entry.modified))}"
        )

    frontmatter.extend(
        [
            f"slug: {yaml_string(entry.slug)}",
            f"categories: {yaml_list(entry.categories)}",
            f"tags: {yaml_list(entry.tags)}",
            f"legacy_url: {yaml_string(entry.legacy_url)}",
            f"source_url: {yaml_string(entry.legacy_url)}",
            'status: "draft"',
            "featured: false",
            "migration_review: true",
            "---",
            "",
            "> Migration candidate generated from the legacy WordPress export. "
            "Review facts, links, software versions, commands, and media before publishing.",
            "",
            markdown_from_html(entry.html),
            "",
        ]
    )

    return "\n".join(frontmatter)


def safe_filename(value: str) -> str:
    value = re.sub(r"[^a-zA-Z0-9._-]+", "-", value).strip("-.")
    return value or "untitled"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("wxr", type=Path, help="Primary WordPress WXR export")
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=Path("migration/work/staged"),
    )
    parser.add_argument(
        "--recent-posts",
        type=int,
        default=0,
        help="Also stage the N most recent published posts. Default: 0.",
    )
    parser.add_argument(
        "--all-posts",
        action="store_true",
        help="Stage all published posts.",
    )
    parser.add_argument(
        "--post-slug",
        action="append",
        default=[],
        help="Stage a specific published post slug. May be repeated.",
    )
    args = parser.parse_args()

    if not args.wxr.is_file():
        parser.error(f"WXR file not found: {args.wxr}")

    entries = parse_entries(args.wxr)
    pages = [
        entry
        for entry in entries
        if entry.post_type == "page" and entry.status == "publish"
    ]
    posts = [
        entry
        for entry in entries
        if entry.post_type == "post" and entry.status == "publish"
    ]
    posts.sort(key=lambda entry: entry.published, reverse=True)

    selected_posts: dict[str, Entry] = {}
    if args.all_posts:
        for entry in posts:
            selected_posts[entry.slug] = entry
    else:
        for entry in posts[: max(args.recent_posts, 0)]:
            selected_posts[entry.slug] = entry

    requested = set(args.post_slug)
    for entry in posts:
        if entry.slug in requested:
            selected_posts[entry.slug] = entry

    missing = requested - set(selected_posts)
    if missing:
        parser.error(
            "Published post slug(s) not found: " + ", ".join(sorted(missing))
        )

    page_dir = args.output_dir / "pages"
    post_dir = args.output_dir / "posts"
    page_dir.mkdir(parents=True, exist_ok=True)
    post_dir.mkdir(parents=True, exist_ok=True)

    for entry in pages:
        filename = "home" if entry.slug == "home-new" else safe_filename(entry.slug)
        (page_dir / f"{filename}.md").write_text(
            render_candidate(entry),
            encoding="utf-8",
        )

    for entry in selected_posts.values():
        date_prefix = entry.published[:10] if entry.published else "undated"
        filename = f"{date_prefix}-{safe_filename(entry.slug)}.md"
        (post_dir / filename).write_text(
            render_candidate(entry),
            encoding="utf-8",
        )

    print(f"Staged {len(pages)} published pages in {page_dir}")
    print(f"Staged {len(selected_posts)} published posts in {post_dir}")
    print("Review all staged files before moving any content into src/content/.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
