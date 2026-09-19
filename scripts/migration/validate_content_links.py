#!/usr/bin/env python3
"""Validate migrated content hygiene and generated internal links."""

from __future__ import annotations

import argparse
import re
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urljoin, urlsplit

LEGACY_HOST_RE = re.compile(
    r"https?://(?:www\.)?pepepow\.org(?:/|\b)",
    re.IGNORECASE,
)
SOURCE_ARTIFACTS = (
    ("legacy-site URL", LEGACY_HOST_RE),
    (
        "WordPress render marker",
        re.compile(r"^\s*skip render:", re.MULTILINE | re.IGNORECASE),
    ),
    (
        "WordPress emoji CDN",
        re.compile(r"https://s\.w\.org/images/core/emoji/", re.IGNORECASE),
    ),
)
SKIP_SCHEMES = {"mailto", "tel", "javascript", "data"}


def markdown_body(text: str) -> str:
    """Return Markdown body while intentionally ignoring provenance frontmatter."""
    if not text.startswith("---\n"):
        return text
    end = text.find("\n---\n", 4)
    if end < 0:
        return text
    return text[end + 5 :]


class ReferenceParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.references: list[tuple[str, str]] = []

    def handle_starttag(
        self,
        tag: str,
        attrs: list[tuple[str, str | None]],
    ) -> None:
        wanted = (
            "href"
            if tag == "a"
            else "src"
            if tag in {"img", "script", "source"}
            else None
        )
        if wanted is None:
            return
        for key, value in attrs:
            if key == wanted and value:
                self.references.append((tag, value))


def route_for_html(dist_root: Path, html_path: Path) -> str:
    relative = html_path.relative_to(dist_root)
    if relative == Path("index.html"):
        return "/"
    if relative.name == "index.html":
        return "/" + relative.parent.as_posix().strip("/") + "/"
    return "/" + relative.as_posix()


def internal_target_candidates(dist_root: Path, path: str) -> list[Path]:
    clean = unquote(path).lstrip("/")
    if not clean:
        return [dist_root / "index.html"]

    target = dist_root / clean
    if path.endswith("/"):
        return [target / "index.html"]

    candidates = [target]
    if not Path(clean).suffix:
        candidates.append(target / "index.html")
    return candidates


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--content-root", type=Path, default=Path("src/content"))
    parser.add_argument("--dist-root", type=Path, default=Path("dist"))
    args = parser.parse_args()

    if not args.content_root.is_dir():
        parser.error(f"Content root not found: {args.content_root}")
    if not args.dist_root.is_dir():
        parser.error(f"Build output not found: {args.dist_root}")

    source_issues: list[tuple[str, str, str]] = []
    content_files = sorted(
        path
        for pattern in ("*.md", "*.mdx")
        for path in args.content_root.rglob(pattern)
    )
    for path in content_files:
        body = markdown_body(path.read_text(encoding="utf-8"))
        for label, pattern in SOURCE_ARTIFACTS:
            match = pattern.search(body)
            if match:
                source_issues.append((path.as_posix(), label, match.group(0)))

        fence_count = len(re.findall(r"^\\s*\x60\x60\x60", body, re.MULTILINE))
        if fence_count % 2:
            source_issues.append(
                (path.as_posix(), "unbalanced fenced code block", str(fence_count))
            )

    generated_issues: set[tuple[str, str, str]] = set()
    references_checked = 0
    html_files = sorted(args.dist_root.rglob("*.html"))

    for html_path in html_files:
        html_text = html_path.read_text(encoding="utf-8", errors="replace")
        if "Migration candidate generated from the legacy WordPress export" in html_text:
            generated_issues.add(
                (
                    html_path.as_posix(),
                    "rendered internal migration banner",
                    "Migration candidate generated from the legacy WordPress export",
                )
            )

        parser_instance = ReferenceParser()
        parser_instance.feed(html_text)
        route = route_for_html(args.dist_root, html_path)
        base_url = f"https://site.invalid{route}"

        for tag, raw_value in parser_instance.references:
            value = raw_value.strip()
            if not value or value.startswith("#"):
                continue

            split = urlsplit(value)
            if split.scheme.lower() in SKIP_SCHEMES:
                continue

            if split.scheme in {"http", "https"} or split.netloc:
                host = split.hostname.lower() if split.hostname else ""
                if host in {"pepepow.org", "www.pepepow.org"}:
                    generated_issues.add(
                        (html_path.as_posix(), "legacy-site URL", value)
                    )
                continue

            resolved = urlsplit(urljoin(base_url, value))
            if resolved.hostname != "site.invalid":
                continue

            references_checked += 1
            candidates = internal_target_candidates(args.dist_root, resolved.path)
            if not any(candidate.is_file() for candidate in candidates):
                generated_issues.add(
                    (html_path.as_posix(), f"missing internal {tag}", value)
                )

    print(
        f"Content files: {len(content_files)} | HTML files: {len(html_files)} | "
        f"internal refs checked: {references_checked} | "
        f"source issues: {len(source_issues)} | "
        f"generated link issues: {len(generated_issues)}"
    )

    for path, label, value in source_issues:
        print(f"  SOURCE {path}: {label}: {value}")
    for path, label, value in sorted(generated_issues):
        print(f"  GENERATED {path}: {label}: {value}")

    if source_issues or generated_issues:
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
