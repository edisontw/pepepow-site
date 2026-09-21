#!/usr/bin/env python3
"""Fetch a small, high-signal PEPEPOW Lens feed using only the Python standard library."""

from __future__ import annotations

import argparse
import html
import json
import re
import sys
from datetime import datetime, timedelta, timezone
from email.utils import parsedate_to_datetime
from pathlib import Path
from urllib.parse import parse_qsl, urlencode, urlsplit, urlunsplit
from urllib.request import Request, urlopen
import xml.etree.ElementTree as ET

DEFAULT_SOURCES = Path("src/data/lens-sources.json")
DEFAULT_OUTPUT = Path("src/data/generated/pepepow-lens.json")

MAX_AGE_DAYS = 21
MAX_ITEMS = 6
MAX_PER_SOURCE = 2
MAX_ENTRIES_PER_FEED = 20
TIMEOUT_SECONDS = 12

CRYPTO_TERMS = (
    "bitcoin", "ethereum", "crypto", "cryptocurrency", "blockchain", "digital asset",
    "stablecoin", "tokenized", "tokenisation", "tokenization", "defi", "proof of work",
    "proof-of-work", "mining", "miner", "wallet", "lightning", "layer 2", "layer-2",
    "onchain", "on-chain", "consensus", "smart contract", "zero knowledge", "zero-knowledge",
)
SEC_STRICT_TERMS = (
    "crypto", "digital asset", "bitcoin", "ethereum", "stablecoin", "tokenized",
    "tokenisation", "tokenization", "blockchain", "onchain", "on-chain",
)
TECH_TERMS = (
    "protocol", "upgrade", "release", "testnet", "mainnet", "fork", "client", "node",
    "consensus", "cryptography", "zero knowledge", "zero-knowledge", "wallet", "lightning",
    "utxo", "bip", "eip", "layer 2", "layer-2", "scaling", "privacy", "open source",
    "open-source", "security", "vulnerability", "mining", "miner", "difficulty",
)
SECURITY_TERMS = (
    "hack", "hacked", "cyberattack", "exploit", "vulnerability", "breach", "malware",
    "phishing", "compromise", "stolen", "theft", "security incident", "ransomware",
)
POLICY_TERMS = (
    "regulation", "regulatory", "sec ", "cftc", "law", "legislation", "congress", "senate",
    "court", "policy", "government", "mica", "tax", "rules", "rulemaking", "exemption",
    "securities", "stablecoin",
)
MINING_TERMS = (
    "proof of work", "proof-of-work", "mining", "miner", "mining pool", "hashrate",
    "difficulty", "coinbase transaction", "stratum",
)
LOW_VALUE_TERMS = (
    "price prediction", "price analysis", "technical analysis", "presale", "airdrop",
    "best crypto", "top crypto", "buy now", "sponsored", "podcast", "video:",
)
TRACKING_QUERY_KEYS = {
    "utm_source", "utm_medium", "utm_campaign", "utm_term", "utm_content",
    "gclid", "fbclid", "mc_cid", "mc_eid",
}


def local_name(tag: str) -> str:
    return tag.rsplit("}", 1)[-1].lower()


def clean_text(value: str | None) -> str:
    if not value:
        return ""
    value = re.sub(r"<[^>]+>", " ", value)
    return re.sub(r"\\s+", " ", html.unescape(value)).strip()


def first_child_text(parent: ET.Element, names: tuple[str, ...]) -> str:
    wanted = set(names)
    for child in list(parent):
        if local_name(child.tag) in wanted:
            return clean_text("".join(child.itertext()))
    return ""


def canonical_url(value: str) -> str:
    value = value.strip()
    split = urlsplit(value)
    if split.scheme not in {"http", "https"} or not split.netloc:
        return ""
    query = [
        (key, val)
        for key, val in parse_qsl(split.query, keep_blank_values=True)
        if key.lower() not in TRACKING_QUERY_KEYS
    ]
    return urlunsplit((split.scheme, split.netloc, split.path, urlencode(query), ""))


def entry_link(entry: ET.Element) -> str:
    for child in list(entry):
        if local_name(child.tag) != "link":
            continue
        href = child.attrib.get("href")
        rel = child.attrib.get("rel", "alternate")
        if href and rel in {"alternate", ""}:
            return canonical_url(href)
        if child.text:
            value = canonical_url(child.text)
            if value:
                return value
    return ""


def parse_date(value: str) -> datetime | None:
    value = value.strip()
    if not value:
        return None
    try:
        parsed = parsedate_to_datetime(value)
        if parsed:
            if parsed.tzinfo is None:
                parsed = parsed.replace(tzinfo=timezone.utc)
            return parsed.astimezone(timezone.utc)
    except (TypeError, ValueError, OverflowError):
        pass
    try:
        parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
        if parsed.tzinfo is None:
            parsed = parsed.replace(tzinfo=timezone.utc)
        return parsed.astimezone(timezone.utc)
    except ValueError:
        return None


def parse_feed(xml_bytes: bytes) -> list[dict[str, str]]:
    root = ET.fromstring(xml_bytes)
    entries: list[dict[str, str]] = []
    wanted = "item" if local_name(root.tag) in {"rss", "rdf"} else "entry"
    candidates = [element for element in root.iter() if local_name(element.tag) == wanted]

    for entry in candidates[:MAX_ENTRIES_PER_FEED]:
        title = first_child_text(entry, ("title",))
        link = entry_link(entry)
        published = first_child_text(entry, ("pubdate", "published", "updated", "date"))
        summary = first_child_text(entry, ("description", "summary", "content", "encoded"))
        if title and link:
            entries.append(
                {"title": title, "url": link, "published_raw": published, "summary": summary}
            )
    return entries


def fetch_source(source: dict[str, object]) -> list[dict[str, str]]:
    request = Request(
        str(source["feed"]),
        headers={
            "User-Agent": "PEPEPOW-Lens/1.0 (+https://pepepow.net/)",
            "Accept": "application/rss+xml, application/atom+xml, application/xml, text/xml;q=0.9, */*;q=0.1",
        },
    )
    with urlopen(request, timeout=TIMEOUT_SECONDS) as response:
        return parse_feed(response.read())


def contains_any(text: str, terms: tuple[str, ...]) -> bool:
    return any(term in text for term in terms)


def classify(text: str) -> str:
    if contains_any(text, SECURITY_TERMS):
        return "Security"
    if contains_any(text, POLICY_TERMS):
        return "Policy"
    if contains_any(text, MINING_TERMS):
        return "Mining / PoW"
    if contains_any(text, TECH_TERMS):
        return "Technology"
    return "Major"


def is_relevant(text: str, mode: str) -> bool:
    if contains_any(text, LOW_VALUE_TERMS):
        return False
    if mode == "strict":
        return contains_any(text, SEC_STRICT_TERMS)
    if mode == "technical":
        return contains_any(text, CRYPTO_TERMS) and contains_any(text, TECH_TERMS)
    return contains_any(text, CRYPTO_TERMS)


def normalized_title(title: str) -> str:
    return re.sub(r"[^a-z0-9]+", " ", title.lower()).strip()


def score_item(item: dict[str, object], now: datetime, priorities: dict[str, int]) -> int:
    published = parse_date(str(item["published"])) or now - timedelta(days=MAX_AGE_DAYS)
    age_days = max(0, (now - published).days)
    recency = max(0, 6 - min(age_days, 6))
    category_bonus = {
        "Security": 6,
        "Policy": 5,
        "Mining / PoW": 5,
        "Technology": 4,
        "Major": 2,
    }.get(str(item["category"]), 0)
    return priorities.get(str(item["source"]), 0) + recency + category_bonus


def load_existing(path: Path) -> list[dict[str, str]]:
    if not path.is_file():
        return []
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return []
    items = data.get("items", [])
    return items if isinstance(items, list) else []


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--sources", type=Path, default=DEFAULT_SOURCES)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()

    sources = json.loads(args.sources.read_text(encoding="utf-8"))
    if not isinstance(sources, list) or not sources:
        raise SystemExit("No Lens sources configured")

    now = datetime.now(timezone.utc)
    cutoff = now - timedelta(days=MAX_AGE_DAYS)
    priorities = {str(source["name"]): int(source.get("priority", 0)) for source in sources}
    fresh: list[dict[str, object]] = []
    failed_sources: set[str] = set()
    successful_sources: set[str] = set()

    for source in sources:
        name = str(source["name"])
        try:
            entries = fetch_source(source)
            successful_sources.add(name)
        except Exception as exc:
            failed_sources.add(name)
            print(f"WARN {name}: {exc}", file=sys.stderr)
            continue

        for entry in entries:
            published = parse_date(entry["published_raw"])
            if published is None or published < cutoff or published > now + timedelta(days=1):
                continue
            text = f'{entry["title"]} {entry["summary"]}'.lower()
            if not is_relevant(text, str(source.get("mode", "crypto"))):
                continue
            fresh.append(
                {
                    "title": entry["title"],
                    "url": entry["url"],
                    "source": name,
                    "published": published.isoformat().replace("+00:00", "Z"),
                    "category": classify(text),
                }
            )

    if not successful_sources:
        print("All Lens feeds failed; preserving last-known-good data.")
        return 0

    existing = load_existing(args.output)
    retained = []
    for item in existing:
        if str(item.get("source", "")) not in failed_sources:
            continue
        published = parse_date(str(item.get("published", "")))
        if published and published >= cutoff:
            retained.append(item)

    candidates = fresh + retained
    seen_urls: set[str] = set()
    seen_titles: set[str] = set()
    unique: list[dict[str, object]] = []
    for item in candidates:
        url = canonical_url(str(item["url"]))
        title_key = normalized_title(str(item["title"]))
        if not url or url in seen_urls or not title_key or title_key in seen_titles:
            continue
        item["url"] = url
        seen_urls.add(url)
        seen_titles.add(title_key)
        unique.append(item)

    unique.sort(
        key=lambda item: (
            score_item(item, now, priorities),
            parse_date(str(item["published"])) or cutoff,
        ),
        reverse=True,
    )

    selected: list[dict[str, object]] = []
    source_counts: dict[str, int] = {}
    for item in unique:
        source = str(item["source"])
        if source_counts.get(source, 0) >= MAX_PER_SOURCE:
            continue
        selected.append(item)
        source_counts[source] = source_counts.get(source, 0) + 1
        if len(selected) >= MAX_ITEMS:
            break

    if selected == existing:
        print(f"Lens unchanged: {len(selected)} items.")
        return 0

    args.output.parent.mkdir(parents=True, exist_ok=True)
    payload = {
        "generated_at": now.replace(microsecond=0).isoformat().replace("+00:00", "Z"),
        "items": selected,
    }
    args.output.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\\n", encoding="utf-8")
    print(
        f"Lens updated: {len(selected)} items | "
        f"sources ok: {len(successful_sources)} | sources failed: {len(failed_sources)}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
