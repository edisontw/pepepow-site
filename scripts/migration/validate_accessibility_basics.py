#!/usr/bin/env python3
"""Validate basic accessibility invariants in generated static HTML."""

from __future__ import annotations

import argparse
from html.parser import HTMLParser
from pathlib import Path


class A11yParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.html_lang = ""
        self.main_ids: list[str] = []
        self.skip_link = False
        self.primary_nav = False
        self.images_without_alt = 0

    def handle_starttag(
        self,
        tag: str,
        attrs: list[tuple[str, str | None]],
    ) -> None:
        values = {key: value for key, value in attrs}

        if tag == "html":
            self.html_lang = (values.get("lang") or "").strip()

        if tag == "main":
            self.main_ids.append((values.get("id") or "").strip())

        if tag == "a":
            classes = set((values.get("class") or "").split())
            if "skip-link" in classes and values.get("href") == "#main-content":
                self.skip_link = True

        if tag == "nav" and (values.get("aria-label") or "").strip() == "Primary":
            self.primary_nav = True

        if tag == "img" and "alt" not in values:
            self.images_without_alt += 1


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dist-root", type=Path, default=Path("dist"))
    args = parser.parse_args()

    if not args.dist_root.is_dir():
        parser.error(f"Build output not found: {args.dist_root}")

    html_files = sorted(args.dist_root.rglob("*.html"))
    issues: list[tuple[str, str]] = []

    for path in html_files:
        audit = A11yParser()
        audit.feed(path.read_text(encoding="utf-8", errors="replace"))
        relative = path.relative_to(args.dist_root).as_posix()

        if not audit.html_lang:
            issues.append((relative, "missing html lang"))
        if audit.main_ids != ["main-content"]:
            issues.append(
                (relative, f"expected one main#main-content, found {audit.main_ids}")
            )
        if not audit.skip_link:
            issues.append((relative, "missing skip link to #main-content"))
        if not audit.primary_nav:
            issues.append((relative, "missing nav[aria-label='Primary']"))
        if audit.images_without_alt:
            issues.append(
                (relative, f"{audit.images_without_alt} image(s) missing alt attribute")
            )

    print(
        f"HTML files: {len(html_files)} | accessibility-basic issues: {len(issues)}"
    )
    for path, message in issues:
        print(f"  A11Y {path}: {message}")

    return 2 if issues else 0


if __name__ == "__main__":
    raise SystemExit(main())
