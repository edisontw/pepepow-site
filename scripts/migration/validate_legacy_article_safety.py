#!/usr/bin/env python3
"""Require explicit safety warnings before high-risk commands in legacy articles."""

from __future__ import annotations

import re
from pathlib import Path

ARTICLES_ROOT = Path("src/content/articles")
WARNING = "> **Legacy safety warning:**"
RISK_PATTERNS = (
    ("private-key export/import", re.compile(r"\b(?:dumpprivkey|importprivkey)\b", re.IGNORECASE)),
    ("recovery phrase in config", re.compile(r"(?:\bmnemonic\s*=|12-word recovery phrase)", re.IGNORECASE)),
    ("destructive wallet-directory cleanup", re.compile(r"delete all files in the wallet directory", re.IGNORECASE)),
    ("destructive filesystem command", re.compile(r"\brm\s+-rf\b", re.IGNORECASE)),
    ("chain-state override", re.compile(r"\b(?:invalidateblock|reconsiderblock)\b", re.IGNORECASE)),
    ("remote script piped to shell", re.compile(r"curl[^\n|]*\|\s*(?:sh|bash)\b", re.IGNORECASE)),
    ("masternode private key config", re.compile(r"\bmasternodeprivkey\b", re.IGNORECASE)),
    ("hard-coded peer recovery", re.compile(r"\baddnode\s+(?:\d{1,3}\.){3}\d{1,3}(?::\d+)?", re.IGNORECASE)),
)


def markdown_body(text: str) -> str:
    if not text.startswith("---\n"):
        return text
    end = text.find("\n---\n", 4)
    return text[end + 5 :] if end >= 0 else text


def main() -> int:
    issues: list[tuple[str, str]] = []
    checked = 0
    risky = 0

    for path in sorted(ARTICLES_ROOT.glob("*.md")):
        if path.name.startswith("_"):
            continue
        checked += 1
        body = markdown_body(path.read_text(encoding="utf-8"))
        matches: list[tuple[int, str]] = []
        for label, pattern in RISK_PATTERNS:
            match = pattern.search(body)
            if match:
                matches.append((match.start(), label))

        if not matches:
            continue

        risky += 1
        first_risk = min(position for position, _ in matches)
        warning_pos = body.find(WARNING)
        if warning_pos < 0 or warning_pos > first_risk:
            labels = ", ".join(sorted({label for _, label in matches}))
            issues.append((path.as_posix(), labels))

    print(
        f"Legacy articles: {checked} | high-risk articles: {risky} | "
        f"missing/late safety warnings: {len(issues)}"
    )
    for path, labels in issues:
        print(f"  SAFETY {path}: {labels}")

    return 2 if issues else 0


if __name__ == "__main__":
    raise SystemExit(main())
