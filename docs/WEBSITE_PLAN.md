# PEPEPOW Website Plan

Status: **Migration validation / staging preparation**  
Target: **https://pepepow.net**  
Repository authority: **edisontw/pepepow-site `main`**

---

## 1. Mission

Build a new PEPEPOW community website that restores the useful historical content from `pepepow.org` while substantially improving structure, usability, transparency, automation, monitoring and maintainability.

The site should serve:

- people discovering PEPEPOW
- wallet users
- miners
- masternode operators
- holders and traders
- developers/community contributors
- people learning about Proof of Work, self-custody and cryptocurrency through the PEPEPOW ecosystem

PEPEPOW remains the primary subject. General cryptocurrency news and educational material are supporting content, not the site's identity.

### Core positioning

PEPEPOW should be presented as:

- transparent
- decentralized
- community-driven
- open source
- practical and verifiable

The site should demonstrate these traits through source links, network data, incident history, release information and reproducible code rather than relying only on marketing language.

---

## 2. Implementation principles

Priority order:

```text
content recovery
→ preserve important public URLs
→ maintainability
→ deployment safety
→ responsive/accessibility
→ useful PEPEPOW information/tools
→ visual refinement
→ optional features
```

Technical direction:

```text
WordPress migration source
        ↓
normalized Markdown / structured data
        ↓
Astro static build
        ↓
dist/
        ↓
Nginx
        ↓
pepepow.net
```

Dynamic blockchain information should come from an isolated cached read-only service, not directly from the wallet/node and not from a new database-backed website application.

---

## 3. Current migration inventory

### 3.1 WordPress exports supplied to the project

Two WordPress WXR files are currently available outside the repository:

- `pepepowcommunityorganization.WordPress.2026-09-18.xml`
- `pepepowcommunityorganization.WordPress.2026-09-19.xml`

Preliminary inspection shows:

#### 2026-09-18 export

- 458 total WordPress items
- 99 published posts
- 7 published normal pages
- 296 media attachments
- additional WordPress/Elementor/navigation/template records that are not expected to become direct site content

Published page slugs:

- `/masternode/`
- `/wallet/`
- `/mining/`
- `/` (WordPress page slug `home-new`)
- `/market/`
- `/about/`
- `/announcements/`

Major post categories observed:

- Announcements
- Masternode
- Wallet
- Articles
- Mining
- Update
- Campaigns

The published content spans older historical material through 2026.

#### 2026-09-19 export

Preliminary inspection shows 296 attachment records only.

Therefore:

- use the **2026-09-18 export as the current canonical WXR content source**
- use the **2026-09-19 export as a media/attachment cross-check**
- do not assume the newer filename is a more complete content backup

This decision must be validated by the reproducible migration inventory script before final import.

### 3.2 Legacy static mirror

Reference source:

`edisontw/web/portal/pepepow-org/`

It contains a localized static crawl of the legacy site, including:

- homepage
- About
- Market
- Masternode
- historical announcements/articles
- category/tag pages
- local static resources
- several PDF documents
- original crawl material for comparison

Use it to recover missing media, compare rendered text, verify old URLs and confirm assets.

Do not use the old generated WordPress/Elementor HTML as the new site's maintainable source.

### 3.3 Existing PEPEPOW monitor

Reference implementation:

`edisontw/pepepow-explorer/monitor/`

The existing monitor already uses the desired pattern:

```text
upstream sources
→ centralized collector
→ normalized cached snapshot
→ cheap JSON API
→ dashboard
```

Existing information includes or can provide:

- block height
- block timing/freshness
- hashrate
- recent blocks
- peers
- masternodes
- fork/upgrade state
- mining pool checks
- service availability
- alerts/anomalies
- cached PEPEW price

Do not duplicate this collection layer in `pepepow-site`.

---

## 4. Information architecture

Proposed primary navigation:

### PEPEPOW

Purpose: identity and orientation.

Content:

- What is PEPEPOW?
- project principles
- Proof of Work / decentralization
- history / milestones
- whitepaper
- open-source repositories
- community model

### Network

Purpose: current network visibility.

Content:

- Network Pulse
- block height
- last block age
- average block time
- hashrate
- masternode count/status
- pool/service status
- recent anomalies
- recent blocks
- longer-term trends where useful
- full Explorer link

### Mining

Purpose: practical mining entry point.

Content:

- current algorithm
- supported miner information
- pool list
- quick-start guide
- troubleshooting
- network hashrate context
- links to authoritative releases/repos

### Masternode

Purpose: masternode operation and understanding.

Content:

- what a PEPEPOW masternode is
- setup/maintenance guides
- current network count
- current software/version information
- reward estimator
- troubleshooting
- safety/backup notes

### Wallets

Purpose: safe wallet onboarding.

Content:

- desktop wallet
- Android wallet
- Light Wallet / Light Service where current
- backup/recovery guidance
- UTXO/consolidation guidance
- official download/release links
- checksum verification guidance
- retired wallet notices where historically important

### Market

Purpose: factual PEPEW market reference, not speculation.

Content:

- PEPEW current price
- market source attribution
- known active trading venues
- liquidity/context where reliable
- links to third-party market pages
- risk notice

Avoid price predictions and promotional trading claims.

### News

Two clearly separated streams:

1. **PEPEPOW News**
   - official/community announcements
   - releases
   - network changes
   - service changes
   - mining/masternode notices

2. **PEPEPOW Lens**
   - small curated selection of broader cryptocurrency developments

PEPEPOW Lens categories:

- Major
- Policy
- Security
- Technology
- optionally Mining / Proof of Work when useful

### Learn

Teach cryptocurrency through practical PEPEPOW examples.

Candidate topics:

- What is Proof of Work?
- Blocks and confirmations
- Hashrate and difficulty
- Wallets and self-custody
- Private keys and backups
- UTXO and consolidation
- Mining pools
- Masternodes
- Hard forks
- Why open-source verification matters

### Tools

Candidate tools:

- Explorer search shortcut
- Network status
- mining links
- masternode reward estimator
- unit/coin amount helpers if useful
- release/checksum verification guide
- service status
- link directory

### Community

Content:

- GitHub
- Discord
- Telegram
- social channels
- community projects
- contribution guidance
- governance/history where relevant

---

## 5. Homepage design

Staging implementation status: **initial custom homepage implemented**. Live Network Pulse data remains a later monitor/API integration; the current staging homepage uses only verified static entry points and build-time announcement data.


The homepage must remain concise.

Recommended information hierarchy:

### Hero

```text
PEPEPOW
Community-powered Proof of Work

Transparent · Open Source · Community Driven

[Get Started] [Explore Network]
```

### Network Pulse

Show only a small summary:

- overall network status
- PEPEW price
- block height
- last block age / block time
- hashrate
- masternode count

Link to the full Network page.

### Latest from PEPEPOW

Maximum approximately 3 recent important posts.

### Start here

Simple role/action cards:

- Wallet
- Mining
- Masternode
- Market
- Learn

### PEPEPOW Lens

Only a few high-value external developments.

Do not turn the homepage into a general crypto news feed.

### Quick links

Compact list of commonly used verified PEPEPOW services.

---

## 6. Content model

Use Astro Content Collections or equivalent schema validation.

Suggested content areas:

```text
src/content/
├── announcements/
├── articles/
├── guides/
├── learn/
└── incidents/
```

Candidate frontmatter:

```yaml
title: ""
description: ""
date: 2026-01-01
updated: 2026-01-01
slug: ""
type: announcement
categories: []
tags: []
legacy_url: ""
source_url: ""
status: published
featured: false
```

Do not blindly reproduce all WordPress metadata.

Preserve only metadata that remains useful for:

- chronology
- routing
- categorization
- source provenance
- redirects
- search
- display

---

## 7. WordPress recovery process

The migration must be reproducible.

### Step A — inventory

Create a script that records:

- post ID
- post type
- status
- title
- slug
- publish date
- modified date
- categories
- tags
- author display name if useful
- legacy URL
- media references
- attachments
- referenced PDFs

Output a machine-readable inventory under a migration working directory.

### Step B — classify

Classify WordPress records into:

- migrate as page
- migrate as announcement/post
- preserve as historical content
- attachment/media
- redirect only
- ignore WordPress implementation record

Examples of implementation records normally excluded:

- Elementor library records
- global style records
- WordPress templates
- navigation internals
- plugin metadata
- cache/plugin-specific postmeta

### Step C — convert content

Convert selected content to Markdown/MDX.

Requirements:

- remove Elementor wrapper markup
- normalize headings
- preserve useful links
- preserve dates
- preserve lists/tables
- preserve meaningful image placement
- remove obsolete embedded widgets/scripts
- sanitize HTML that must remain

### Step D — recover media

Build a media manifest combining:

- WXR attachment URLs
- static mirror assets
- referenced media URLs
- documents/PDFs

Preferred destination:

```text
public/media/
public/docs/
```

Use stable, readable filenames where practical.

Do not download unrelated WordPress thumbnails/duplicates if the canonical source image is available.

### Step E — verify content references

For each migrated document:

- every local image exists
- every PDF exists or is intentionally external
- internal links resolve
- external links are preserved or deliberately replaced
- obsolete external embeds are removed

### Step F — build redirect map

Preserve old public URLs where practical.

Prefer serving the same path directly in Astro.

If a path must change, add an explicit redirect mapping.

Do not silently discard frequently linked historical URLs.

---

## 8. Network Pulse architecture

The main site should consume a minimal read-only endpoint.

Preferred future endpoint in the monitor project:

`/monitor/api/public-summary`

Candidate payload:

```json
{
  "network_status": "normal",
  "height": 0,
  "last_block_age_seconds": 0,
  "avg_block_time_seconds": 0,
  "hashrate": 0,
  "masternode_count": 0,
  "price_usdt": 0,
  "updated_at": 0
}
```

The endpoint should:

- read cached state
- expose only allowlisted fields
- perform no request-time wallet RPC
- contain no credentials
- contain no internal host details
- be rate-limit/cache friendly

### Browser behavior

Homepage:

- initial static shell
- fetch small summary endpoint after load
- show stale/unavailable state cleanly
- do not block page rendering if the monitor is offline

Suggested browser refresh:

- approximately 60–120 seconds for homepage summary

The full Network page can use slightly more detailed cached endpoints.

---

## 9. Price data

Use the existing explorer/monitor path as primary site data where reliable.

Current monitor already obtains cached price from the explorer and adds `price_usdt` to status output.

Design goals:

- one price collection path
- source attribution
- cache aggressively
- tolerate upstream failure
- optionally cross-check/fallback to a second source

Do not load third-party price widgets directly into the main site unless there is a strong reason.

---

## 10. Crypto news / PEPEPOW Lens

Goal:

**small, high-value, low-cost, low-token curation**

Do not build a high-volume aggregator.

### Source strategy

Prefer first-party/authoritative sources where possible:

- official regulator/policy feeds
- protocol/developer publications
- respected security advisories
- a small number of established crypto news RSS feeds

Maintain an allowlist in repository data/config.

### Pipeline

```text
RSS / official feeds
        ↓
metadata extraction
        ↓
deduplicate
        ↓
source + keyword rules
        ↓
category
        ↓
importance filter
        ↓
small JSON output
        ↓
Astro display
```

AI/LLM processing is optional and should happen only after deterministic filtering.

If AI is used:

- process only a small shortlist
- produce a short factual summary
- produce a short "Why it matters" explanation
- retain the original source/date/link
- never fabricate missing article content

### Frequency

Initial recommendation:

- fetch 2–4 times per day
- keep only a few items per category
- weekly digest can be generated separately if useful

---

## 11. Automated data

Prefer generated static JSON for data that does not need live polling.

Candidate generated files:

```text
src/data/generated/news.json
src/data/generated/releases.json
src/data/generated/link-health.json
src/data/generated/network-history.json
```

Suggested cadence:

| Data | Suggested cadence |
|---|---|
| live network summary | read from monitor cache |
| PEPEW price | monitor cache, roughly 10 min upstream cadence |
| crypto news | 2–4 times/day |
| GitHub releases | daily |
| external link health | weekly |
| long-term network snapshot | daily |
| PEPEPOW announcements | on commit |

GitHub Actions should not contain private wallet/node access.

---

## 12. Useful future features

Prioritize features with lasting utility.

### Network Heartbeat

Simple public health indicator.

### PEPEPOW Timeline

Important project milestones:

- major releases
- algorithm changes
- service launches/retirements
- governance/community events

### Incident History

Transparent record of meaningful incidents:

- chain/sync disruptions
- explorer/service outages
- mandatory upgrades
- exchange/service changes

Suggested structure:

```text
what happened
→ detected impact
→ response
→ resolution/status
→ relevant source/announcement
```

### Release Center

Show:

- current official release
- repository link
- published date
- platform
- checksum/signature information when available
- superseded/retired notices

### Link Health

Automatically validate important external links.

Do not automatically hide failed links without review; distinguish:

- healthy
- temporarily unavailable
- redirected
- retired
- unknown

### Search

Use a static/build-time search solution where possible.

Avoid adding a server/database solely for site search.

---

## 13. Visual direction

Desired presentation:

- modern but restrained
- dark/charcoal base is appropriate
- PEPEPOW green as an accent
- strong typography and spacing
- data/status UI should be clear before decorative
- responsive from the beginning
- accessible contrast
- minimal animation
- fast load

Avoid:

- exchange/casino visual language
- excessive tickers
- excessive glowing effects
- full-screen animation
- crowded dashboards on the homepage
- generic meme-coin landing-page patterns

The visual identity should communicate an open technical community rather than speculative hype.

---

## 14. Security model

### Mandatory separation

The public site must never need:

- wallet RPC credentials
- wallet private keys
- masternode keys
- SSH credentials
- direct filesystem access to blockchain data

### External content

RSS/news content must be treated as untrusted input.

Do not directly render arbitrary feed HTML.

Store/display only sanitized fields such as:

- title
- short plain-text summary
- source
- date
- canonical URL
- category

### Browser/API

- read-only public endpoints only
- explicit field allowlist
- timeouts
- cache headers
- rate limiting where appropriate
- safe unavailable/stale states

### HTTP/security headers

Production Nginx should eventually include suitable:

- HSTS after HTTPS is confirmed stable
- Content-Security-Policy
- X-Content-Type-Options
- Referrer-Policy
- frame restrictions

### Repository

Before making the repository public, audit history for:

- secrets
- emails/private metadata
- raw WXR files
- server addresses that need not be public
- private deployment configuration
- third-party copyrighted assets

---

## 15. Licensing and provenance

Code and content/media must be considered separately.

Before public release:

- choose a code license
- define site-content licensing where possible
- retain attribution for third-party media
- identify assets that cannot be freely redistributed
- document external data sources

Do not assume old WordPress media can automatically be redistributed under the repository's code license.

---

## 16. Deployment direction

Production deployment should remain static-first:

```text
GitHub main
   ↓
production pull
   ↓
npm ci
   ↓
Astro build
   ↓
new dist directory
   ↓
atomic/current symlink or equivalent
   ↓
Nginx
```

Deployment must not:

- restart the PEPEPOW wallet/node
- alter wallet/node systemd services
- touch blockchain data
- reboot the server

For production Nginx changes:

1. back up the current config
2. write/change only the website server block needed
3. validate configuration
4. reload Nginx only after successful validation

Consider low-priority build scheduling (`nice` / `ionice`) on resource-constrained production hosts.

---

## 17. Repository target structure

Initial target:

```text
pepepow-site/
├── README.md
├── CHATGPT_PROJECT_CONTEXT.md
├── astro.config.*
├── package.json
├── public/
│   ├── media/
│   └── docs/
├── src/
│   ├── components/
│   ├── layouts/
│   ├── pages/
│   ├── content/
│   │   ├── announcements/
│   │   ├── articles/
│   │   ├── guides/
│   │   ├── incidents/
│   │   └── learn/
│   └── data/
│       ├── sources.*
│       └── generated/
├── scripts/
│   ├── migration/
│   ├── fetch-news.*
│   ├── check-links.*
│   └── snapshot-network.*
├── docs/
│   ├── WEBSITE_PLAN.md
│   ├── MIGRATION_REPORT.md
│   ├── DATA_SOURCES.md
│   ├── CONTENT_POLICY.md
│   ├── SECURITY.md
│   └── DEPLOYMENT.md
└── .github/
    └── workflows/
```

Do not create all files merely to match this tree. Add them when the corresponding feature is implemented.

---

## 18. Delivery phases

### Phase 0 — Repository foundation

Deliver:

- project context
- website plan
- Astro skeleton
- basic lint/build validation
- safe ignore rules
- initial route/content conventions

Exit criteria:

- clean build
- no secrets/raw migration exports committed
- structure ready for migration

### Phase 1 — Content recovery

Deliver:

- reproducible WXR inventory script
- migration report
- recovered published pages
- recovered 99 published posts or documented exclusions
- media/PDF manifest
- URL/redirect inventory
- sanitized Markdown/MDX content

Exit criteria:

- all migrated content traceable to source
- important legacy URLs accounted for
- no broken required media references

### Phase 2 — Core site UX

Deliver:

- responsive global layout
- homepage
- About/PEPEPOW
- Announcements/News archive
- Wallets
- Mining
- Masternode
- Market
- Community
- basic search/navigation if ready

Exit criteria:

- normal visitor can understand PEPEPOW and reach key actions quickly
- mobile/desktop layout works
- historical posts are usable

### Phase 3 — Network integration

Deliver:

- minimal public monitor summary contract
- homepage Network Pulse
- full Network page
- price display
- stale/offline handling

Exit criteria:

- no direct wallet/node RPC from site/browser
- data path remains low-load
- site still works when live API is unavailable

### Phase 4 — Automation / PEPEPOW Lens

Deliver:

- curated feed allowlist
- deterministic fetch/dedupe/classification
- generated news data
- release checker
- link health checker
- daily network history if useful

Exit criteria:

- automation is reproducible
- failures do not break site builds
- news remains small and high signal

### Phase 5 — Transparency / education / polish

Deliver as justified:

- PEPEPOW Timeline
- Incident History
- Learn section
- Release Center
- reward estimator
- accessibility/SEO/performance refinement

### Phase 6 — Production migration

Before switching traffic:

- staging validation
- old/new URL comparison
- media verification
- HTTPS/Nginx validation
- backup current production config
- deployment rollback procedure
- confirm wallet/node isolation

Only after successful validation should legacy WordPress be retired.

---

## 19. Immediate next implementation slice

The next work should be deliberately narrow:

1. initialize Astro in this repository
2. add safe `.gitignore`
3. build the WXR inventory/import tooling
4. generate a migration report from the two supplied exports
5. establish content schemas
6. migrate the seven published pages and a small representative post set first
7. validate slugs/media conversion
8. then batch-migrate the remaining published posts

Do **not** start crypto-news automation or extensive visual polish before the migration path is proven.

---

## 20. Decision log

### Decided

- `edisontw/pepepow-site/main` is the new website authority.
- Astro/static-first is the default architecture.
- WordPress will not remain the long-term CMS.
- raw WordPress/Elementor HTML will not be the future content model.
- PEPEPOW is the site's primary subject.
- general crypto news will be curated and low-volume.
- existing monitor infrastructure should be reused rather than duplicated.
- production website work must remain isolated from the PEPEPOW wallet/node.
- important historical URLs should be preserved whenever practical.

### To decide later

- final code/content license
- exact visual design system
- final public-summary API schema
- exact news source allowlist
- exact analytics approach (prefer privacy-respecting or none)
- final production directory/rollback convention
- whether multilingual support is worth adding after English migration is stable
