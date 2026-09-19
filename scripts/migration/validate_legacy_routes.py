#!/usr/bin/env python3
"""Validate that every published legacy route has a generated Astro HTML file."""

from __future__ import annotations

import argparse
import json
from pathlib import Path


def output_file(dist_root: Path, target_path: str) -> Path:
    if target_path == "/":
        return dist_root / "index.html"
    relative = target_path.strip("/")
    return dist_root / relative / "index.html"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--manifest",
        type=Path,
        default=Path("migration/public/legacy-routes.json"),
    )
    parser.add_argument("--dist-root", type=Path, default=Path("dist"))
    args = parser.parse_args()

    if not args.manifest.is_file():
        parser.error(f"Manifest not found: {args.manifest}")
    if not args.dist_root.is_dir():
        parser.error(f"Build output not found: {args.dist_root}")

    payload = json.loads(args.manifest.read_text(encoding="utf-8"))
    routes = payload.get("routes", [])

    missing: list[tuple[str, str]] = []
    seen: set[str] = set()

    for route in routes:
        target = str(route.get("target_path") or route.get("planned_path") or "")
        if not target:
            missing.append(("<empty target>", str(route.get("legacy_path", ""))))
            continue
        if target in seen:
            missing.append((target, "duplicate target path"))
            continue
        seen.add(target)

        generated = output_file(args.dist_root, target)
        if not generated.is_file():
            missing.append((target, str(generated)))

    print(
        f"Legacy routes: {len(routes)} | unique targets: {len(seen)} | "
        f"generated: {len(routes) - len(missing)} | missing/errors: {len(missing)}"
    )

    if missing:
        for target, detail in missing:
            print(f"  {target}: {detail}")
        return 2

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
