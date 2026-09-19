# PEPEPOW Migration Report

Status: **Phase 1 content recovery in progress**  
Date: **2026-09-19**

This report records reproducible migration findings only. Raw WordPress WXR files remain outside Git because they can contain account/author metadata that is not needed by the public site.

## Sources checked

- `pepepowcommunityorganization.WordPress.2026-09-18.xml`
- `pepepowcommunityorganization.WordPress.2026-09-19.xml`

The inventory was produced with:

`scripts/migration/wxr_inventory.py`

Local machine-readable output is written to `migration/work/`, which is intentionally ignored by Git.

## Primary WXR decision

Use the **2026-09-18 export as the canonical WordPress content migration source**.

Use the **2026-09-19 export only as an attachment cross-check**.

Reason:

- the 2026-09-18 export contains content plus attachments
- the 2026-09-19 export contains attachments only
- all 296 attachment IDs are shared between the two exports
- all 296 shared attachment IDs have the same attachment URL in both exports
- there are no attachment IDs unique to either export

## 2026-09-18 inventory

Total WordPress items: **458**

| Post type | Status | Count |
|---|---|---:|
| attachment | inherit | 296 |
| post | publish | 99 |
| page | publish | 7 |
| page | draft | 5 |
| elementor_library | publish | 17 |
| nav_menu_item | publish | 16 |
| wp_navigation | publish | 7 |
| wp_global_styles | publish | 4 |
| e-landing-page | publish | 2 |
| e-landing-page | draft | 1 |
| wp_template | publish | 2 |
| wp_template_part | publish | 1 |
| custom_css | publish | 1 |

### Published pages

| Title | WordPress slug | Legacy path |
|---|---|---|
| Home | `home-new` | `/` |
| About | `about` | `/about/` |
| Announcements | `announcements` | `/announcements/` |
| Market | `market` | `/market/` |
| Mining | `mining` | `/mining/` |
| Masternode | `masternode` | `/masternode/` |
| Wallet | `wallet` | `/wallet/` |

### Published post categories

The 99 published posts can belong to more than one category, so the counts below intentionally overlap.

| Category | Tagged published posts |
|---|---:|
| Announcements | 69 |
| Masternode | 28 |
| Wallet | 27 |
| Articles | 26 |
| Mining | 23 |
| Update | 19 |
| Campaigns | 9 |

### Media references

The inventory detected:

- **296 attachment records**
- **562 unique `wp-content/uploads` URLs referenced across item content and attachment records**
- **9 unique PDF URLs referenced**

The 562 URL count is a URL-reference inventory, not a claim that there are 562 canonical original media files. WordPress content can reference resized variants or duplicate representations of the same underlying asset.

## 2026-09-19 inventory

Total WordPress items: **296**

All are:

- post type: `attachment`
- status: `inherit`

There are:

- 0 posts
- 0 pages
- 296 attachment records

Attachment comparison against 2026-09-18:

| Check | Result |
|---|---:|
| Shared attachment IDs | 296 |
| Same URL for shared IDs | 296 |
| Only in 2026-09-18 | 0 |
| Only in 2026-09-19 | 0 |

## Migration classification

### Migrate as public site content

- 7 published pages
- 99 published posts, subject to content cleanup and historical-status review
- useful original media
- useful PDFs/documents
- categories/tags only where they remain useful for navigation/search
- legacy paths and redirects

### Reference only / do not directly migrate as site architecture

- Elementor library records
- WordPress navigation internals
- WordPress templates/template parts
- global styles
- custom CSS
- WordPress implementation metadata

These can be consulted during comparison but must not become the new maintenance model.

## Privacy rule

The migration inventory tool intentionally does **not** export:

- WordPress author email addresses
- WordPress author login names
- raw post body content into the machine-readable inventory

Raw WXR files remain outside Git.

## Staging conversion validation

The reviewed-content staging converter is now available at:

`scripts/migration/wxr_extract.py`

It was tested against the 2026-09-18 WXR and successfully staged:

- all **7 published pages**
- the **5 most recent published posts** as representative samples

The generated candidates are intentionally written under `migration/work/staged/`, which is ignored by Git.

The test confirmed that the conversion can remove most WordPress/Elementor presentation code while preserving useful headings, paragraphs, links, images, lists and code blocks. It also confirmed that staged content must not be auto-published: current page bodies still contain historical software versions, download URLs, operational commands and other statements that require review before becoming authoritative new-site content.

## Current validation status

Completed:

- [x] WXR files parse successfully
- [x] primary content export identified
- [x] attachment-only export identified
- [x] attachment IDs compared
- [x] attachment URLs compared
- [x] published pages counted and routed
- [x] published posts counted
- [x] category counts recorded
- [x] initial media/PDF URL inventory produced locally

Not yet completed:

- [ ] download/check live attachment URLs
- [ ] compare attachment URLs with the legacy static mirror
- [ ] identify canonical original images vs WordPress resized variants
- [ ] classify missing media
- [x] convert the seven pages to normalized review-only site content
- [x] convert representative posts (5 most recent published announcements recovered as review-only drafts)
- [x] validate old internal links
- [x] build sanitized legacy route preservation map
- [x] batch migrate remaining posts as review-only drafts

## Next migration slice

The mechanical recovery, current-sensitive public-page review, historical-link/readability cleanup,
and legacy technical-article safety gates are complete.

Priority now:

1. continue staging responsive/accessibility/visual refinement
2. replace the recovered legacy homepage presentation with the concise information hierarchy defined
   in `docs/WEBSITE_PLAN.md`, while keeping the recovered source page for provenance
3. add current release/network summary surfaces only through static/build-time data or isolated
   cached read-only APIs
4. perform staging review before changing any production Nginx configuration
5. keep production deployment out of scope until staging acceptance


## Phase 1 recovery slice — 2026-09-19

The first repository-backed content recovery slice now preserves the five most recent published WordPress posts as normalized Markdown under `src/content/announcements/`.

All five recovered entries remain:

- `status: draft`
- `migration_review: true`

This is intentional. Recovery establishes provenance and URL continuity first; it does not assert that historical service status, software versions, download links, or operational statements are still current.

A dedicated `pages` content collection is defined, and all seven published legacy pages are now recovered under `src/content/pages/` as review-only drafts without prematurely exposing stale operational guidance.

The migration tooling now includes `scripts/migration/wxr_manifests.py`, which reproducibly writes working manifests under the ignored `migration/work/` directory for:

- all published legacy page/post routes
- attachment/media records
- referenced PDF documents

Validation against the canonical 2026-09-18 WXR yields:

- 106 published legacy routes = 7 pages + 99 posts
- 296 attachment records
- 9 referenced PDF URLs

The recovered page set is:

- Home (legacy `/`, WordPress slug `home-new`)
- About (`/about/`)
- Announcements (`/announcements/`)
- Market (`/market/`)
- Mining (`/mining/`)
- Masternode (`/masternode/`)
- Wallet (`/wallet/`)

Every recovered page remains `status: draft` and `migration_review: true`. Historical operational claims and commands have not been promoted to current guidance.

The raw WXR and generated working manifests remain outside Git.


## Legacy static mirror cross-check

The migration fallback at `edisontw/web/portal/pepepow-org/` was inspected after the repository-backed page recovery.

Its archived README records a crawl performed on 2026-05-29 UTC / 2026-05-30 GMT+8. The mirror is useful for comparing rendered HTML, old routes, and the subset of assets that were actually captured, but it is not a complete media authority.

Current findings from the mirror on `edisontw/web/main`:

- `assets/img/` contains only the localized 2025 site logo.
- `original/raw-assets/` is dominated by WordPress/Elementor CSS, JavaScript, fonts, and the same site logo.
- `original/crawl-log/asset_mapping.json` maps the captured WordPress resources and confirms the limited image coverage.
- The archived README records `/mining/`, `/wallet/`, `/announcements/`, and several other routes as unavailable during that crawl.
- The README mentions three downloaded PDFs, but an `assets/docs/` directory is not present on the current mirror branch; therefore those files must not be assumed recovered without a separate check.

Media recovery precedence is therefore:

1. canonical WXR attachment/reference URL
2. matching file already present in the static mirror/raw-assets mapping
3. unresolved-media report
4. only then obtain missing `wp-content/uploads/` material from the legacy host or another verified source

This keeps the static archive as a recovery aid without treating its incomplete crawl as authoritative site content.


## Full published-post recovery

All **99 published WordPress posts** from the canonical 2026-09-18 WXR are now represented in GitHub `main` as review-only Markdown content.

Repository classification:

- **73 announcement/update/campaign/mining posts** in `src/content/announcements/`
- **26 posts carrying the WordPress `Articles` category** in `src/content/articles/`

The underscore-prefixed collection README files are not counted as content entries.

All recovered posts retain:

- original title
- publish and modified dates
- original slug
- categories and tags
- `legacy_url`
- `source_url`
- `status: draft`
- `migration_review: true`

No recovered historical post has been promoted to current authoritative guidance.

The staging converter now supports `--all-posts` so the 99-post conversion can be reproduced locally from the canonical WXR.

## Committed public migration manifests

Sanitized migration metadata is now committed under `migration/public/`:

- `legacy-routes.json` — **106 published legacy routes** (7 pages + 99 posts)
- `media-manifest.json` — **296 WordPress attachment records** plus **9 referenced PDF URLs**

The route map currently uses a same-path preservation strategy for every published legacy page/post. This records the intended URL contract; Astro runtime route wiring and link validation still remain to be completed.

The manifests contain no WordPress author login/email fields and no raw post bodies.

The media probe now exits successfully by default while recording unresolved URLs; `--strict` can be used when a non-zero exit is desired for validation gates.


## Media availability probe — 2026-09-19

The committed 296-attachment manifest was probed from GitHub Actions after URL/IRI normalization was added to the probe tool.

Result:

- **296** attachment URLs probed
- **1** directly available
- **295** blocked with HTTP 403 from `pepepow.org/wp-content/uploads/`
- the one directly available item is an external WordPress Video MP4 at `videos.files.wordpress.com`

The 295 HTTP 403 responses are classified as **blocked/unresolved**, not missing. A 403 response does not prove that the file no longer exists.

The legacy static mirror was also enumerated recursively:

- 559 files under `portal/pepepow-org/`
- 2 image files, representing the same localized site logo in clean/raw copies
- 0 PDF files
- no exact attachment-basename matches against the 296 WXR attachment records

Therefore the GitHub mirror cannot materially replace the missing WordPress uploads archive.

### Targeted uploads recovery

The WXR contains **295 unique canonical `_wp_attached_file` paths**. The remaining attachment is the externally hosted WordPress Video item.

A precise recovery list is committed at:

`migration/public/uploads-required.txt`

A read-only helper is committed at:

`scripts/migration/collect_uploads.py`

This helper can be run against an existing WordPress `wp-content/uploads/` directory or mounted backup. It copies only the 295 required canonical files into a separate working directory and never modifies the WordPress source tree.

Example dry run:

`python3 scripts/migration/collect_uploads.py --uploads-root /path/to/wp-content/uploads --dry-run`

This targeted approach avoids requesting or copying an entire WordPress backup when only the canonical attachment files are needed.


## Edison2 legacy uploads recovery check — 2026-09-19

The older WordPress installation currently present on `edison2` was checked against the 296-attachment migration manifest using:

`/var/www/html/wordpress/wp-content/uploads`

Dry-run result:

- attachment records: **296**
- canonical WordPress upload files found locally: **233**
- canonical upload files missing locally: **62**
- external attachment: **1**
- invalid paths: **0**

All 62 locally missing canonical uploads fall in **2025–2026**, consistent with the WordPress installation on `edison2` being an older backup rather than the final legacy-site media set.

Missing canonical uploads by month:

| Month | Missing |
|---|---:|
| 2025/01 | 7 |
| 2025/02 | 6 |
| 2025/03 | 1 |
| 2025/04 | 2 |
| 2025/05 | 3 |
| 2025/06 | 3 |
| 2025/07 | 5 |
| 2025/08 | 1 |
| 2025/09 | 1 |
| 2025/11 | 8 |
| 2025/12 | 1 |
| 2026/01 | 3 |
| 2026/02 | 3 |
| 2026/03 | 4 |
| 2026/04 | 4 |
| 2026/05 | 5 |
| 2026/06 | 1 |
| 2026/07 | 3 |
| 2026/08 | 1 |

Recovery scope is therefore narrowed to these **62 exact canonical paths** from a newer legacy WordPress filesystem or verified backup. The existing 233 files on `edison2` do not need to be re-downloaded from the old site.


### Cloudflare challenge confirmation

A direct request from `edison2` to a known missing canonical upload was tested with a normal desktop browser user-agent and a `pepepow.org` referer:

`/wp-content/uploads/2025/01/2025logo.png`

The origin path returned **HTTP 403** with:

- `server: cloudflare`
- `cf-mitigated: challenge`

This confirms that the public-URL probe cannot distinguish file existence for the 295 legacy-host attachments because Cloudflare is challenging non-browser requests. These records remain **blocked/unresolved**, not missing.

Do not add bypass logic to the migration scripts. Recovery should use an authorized browser/WordPress-admin path, Cloudflare configuration if the account owner has access, or a verified filesystem backup.


Browser verification of the challenged sample URL was also performed. After completing Cloudflare's browser security check, the requested image was displayed successfully. This confirms that at least the tested 2025 canonical upload still exists behind the Cloudflare challenge. The remaining 62 edison2-local misses should therefore be treated as **blocked but potentially recoverable**, not presumed deleted.


## Canonical media recovery completed — 2026-09-19

The WordPress Media Library export was obtained through the authorized legacy WordPress administration interface and compared with the 62 files that were absent from the older `edison2` WordPress backup.

Recovery result:

- previously recovered from `edison2`: **233**
- requested from Media Library export: **62**
- recovered from Media Library export: **62**
- unresolved: **0**
- ambiguous filename matches: **0**
- total local canonical WordPress upload files recovered: **295 / 295**
- external attachment records: **1**

The previously missing `2025/01/PEPEPOW-Whitepaper_v2.0.pdf` was also verified locally after recovery.

The canonical WordPress media-recovery gate is therefore complete. The next step is to audit total repository payload size, stage PDFs under `public/docs/legacy/`, stage other canonical media under `public/media/legacy/`, generate a checksum-backed URL map, and rewrite resolvable legacy upload URLs in recovered Markdown.


### Repository payload decision

The complete recovered canonical media set on `edison2` is approximately **169 MiB** (176,017,230 bytes). The largest files include historical wallet ZIP archives of approximately 20 MiB and 13 MiB plus several multi-megabyte legacy artwork/source images.

The full 295-file recovery set is therefore treated as a **migration archive/source**, not an automatic Git repository payload.

Repository staging policy:

1. keep the complete 295-file recovered set under ignored `migration/work/recovered-uploads/`
2. identify canonical files actually referenced by recovered Markdown/MDX
3. commit only the files needed by the static website plus deliberately retained documents/assets
4. keep historical installers/ZIPs and unreferenced source artwork out of the website repository unless there is a specific public-site requirement

`scripts/migration/stage_recovered_media.py --audit-only --referenced-only` reports the exact referenced-file count and byte size before any copy occurs. It also prints unresolved legacy upload URLs for follow-up.


### Referenced media audit

A referenced-only audit against the recovered Markdown/MDX found:

- canonical attachment files selected: **55**
- selected canonical payload: **22,914,070 bytes** (about 21.9 MiB)
- resolvable legacy upload URL occurrences: **63**
- unresolved legacy upload URLs: **3**

The three unresolved paths are:

- `2024/02/thumb-1.jpg`
- `2024/02/thumb-2.jpg`
- `2024/02/thumb-3.jpg`

These are referenced by the legacy Masternode page but are not present as canonical attachment records in the WXR manifest. They are therefore treated as **supplemental content-referenced media**, not silently promoted to WXR attachments.

The staging tool now recognizes such supplemental files when they are placed at their original relative path under `migration/work/recovered-uploads/`. It reports them separately and can stage/rewrite them together with the 55 canonical referenced files.


### Masternode decorative thumbnail disposition

The three content-referenced but non-WXR paths `2024/02/thumb-1.jpg`, `thumb-2.jpg`, and `thumb-3.jpg` were checked against both the older `edison2` WordPress uploads tree and the authorized 2026-09-19 WordPress Media Library export. None was present.

These files were used only as decorative images in the legacy Masternode “Benefits” section. The remaining canonical sibling image `service-thumb-2.jpg` served the same decorative role. To avoid preserving an incomplete/inconsistent legacy decoration set, all four Benefits thumbnails were deliberately removed from the migration draft while retaining the substantive text.

The future Astro presentation may render these benefits as consistent accessible cards/icons rather than reproducing the old WordPress thumbnails.

## Legacy internal-link and WordPress-artifact cleanup — 2026-09-19

The recovered content body was audited separately from provenance frontmatter. The original
`legacy_url` and `source_url` fields remain unchanged so migration provenance is preserved.

Cleanup completed in this slice:

- same-site links that still targeted the exact legacy host `pepepow.org` were converted to
  root-relative Astro paths where the corresponding preserved route exists
- legacy WordPress category navigation and `wp-admin/admin-ajax.php` pagination chrome were
  removed from the recovered Announcements page
- the WordPress-generated related-post/archive block appended to the Masternode page was removed;
  the substantive Masternode setup content was retained
- residual `skip render:` migration markers were removed
- a legacy WordPress emoji-CDN image reference was converted to its Unicode emoji
- the recovered About page had one unmatched Markdown code fence that caused its remaining roadmap/FAQ content to render as code; the fence was removed and one hidden malformed `h/media/...` image path was corrected
- `scripts/migration/wxr_extract.py` now performs the reproducible portions of the same cleanup
  so a future WXR restage does not silently reintroduce those artifacts

A new read-only validation gate is committed at
`scripts/migration/validate_content_links.py`. It intentionally ignores provenance frontmatter,
then checks migrated content bodies for exact legacy-site URLs and known WordPress artifacts. After
Astro builds, it parses generated HTML and verifies that rendered internal `href`/`src` targets
resolve to files in `dist/`, while leaving external services and PEPEPOW subdomains external.

Validated in GitHub Actions on PR #1:

- Astro build: **106 pages**
- legacy route validation: **106 routes / 106 unique targets / 106 generated / 0 errors**
- content/link validation: **112 content files / 106 HTML files / 804 internal references checked**
- content/link validation result: **0 source issues / 0 generated-link issues**
- migration-script compile check: **PASS**
- Markdown fence-balance validation: **PASS** after the About-page repair

Recovered historical and current-sensitive material remains `status: draft` and
`migration_review: true`; this cleanup does not promote it to current authoritative guidance.

No production deployment or Nginx change was made in this slice.

## Current-sensitive public-page verification — 2026-09-19

An initial current-state verification pass was completed for the six operational public pages:
`home`, `about`, `mining`, `masternode`, `wallet`, and `market`.

Authoritative/current sources used for this pass included the PEPEPOW Core repository/releases,
the PEPEPOW Explorer, the HTN Miner download/release page, PEPEW Light, the Android wallet
repository, the Foztor community pool, and current PEPEPOW announcements.

Verified findings and resulting changes:

- PEPEPOW currently uses **HooHash V110**; stale homepage/FAQ references that presented
  XelisV2-pepew as the current algorithm were corrected.
- PEPEPOW Core **v2.9.0.5** is the latest release reviewed in this pass. The wallet page now
  uses v2.9.0.5 consistently and no longer mixes v2.9.0.4 download commands into the current guide.
- The old wallet page had Linux x86_64/AARCH64 download examples crossed between architectures;
  the current guide now uses the correct v2.9.0.5 artifacts.
- Dated blockchain-bootstrap ZIP links were removed from the default wallet path because those
  archives age quickly and should not be presented as the normal current download.
- Wallet recovery guidance no longer recommends broadly deleting the data directory while retaining
  only `wallet.dat`; the page now requires a clean shutdown and separate wallet backup before any
  destructive recovery step.
- PEPEW Light Wallet is documented as the recommended browser entry and remains described as
  **public beta** / non-custodial.
- The Android wallet is now documented as a released **v1.0.0** non-custodial wallet rather than
  "under development".
- The current HTN download page lists **v1.4.22**. Since HTN v1.4.19, a valid PEPEPOW address can
  be auto-detected, so the old site's claim that `--pepepow` is mandatory was removed.
- The mining guide no longer hard-codes older Mining4People/Zpool Stratum settings as confirmed
  current configuration. The verified Foztor pool and PEPEPOW Lab Pool are linked, and users are
  directed to each pool's live connection instructions.
- Tiered masternode collateral is documented as **10M / 25M / 50M / 100M PEPEW** rather than
  treating 10M as the only collateral level.
- Fixed "first reward in around 24 hours" wording was removed; masternode reward timing is now
  described as dependent on tier, active-node count, queue position, and network conditions.
- The PEPEPOW Explorer currently exposes market data for **NonKYC** and **NestEx**. Exbitron could
  not be independently confirmed during this check and is therefore no longer presented as a
  confirmed active venue.
- The About page's exact current reward/funding split was initially left unresolved because historical
  documents and release notes describe different funding eras. It was subsequently resolved in the
  dedicated consensus-code verification below.

All six pages remain `status: draft` and `migration_review: true`. This pass corrects
high-confidence current operational errors but does not yet assert that every external link,
historical governance statement, or third-party service is current.

Next content gate:

1. run a systematic external-link/service health audit for the six public pages and important
   announcement links
2. resolve the remaining current-consensus DevFee/funding description from Core code
3. perform a rendered readability/editing pass on the recovered pages and historical posts
4. only after those gates consider promoting reviewed current pages out of migration-review state

No production deployment or Nginx change was made in this slice.

## External-link and service-health audit — 2026-09-19

A focused external-link audit was performed after the first current-sensitive content review. The
audit covered the six operational public pages rather than treating every historical post link as a
current service endorsement.

The review uses conservative status rules:

- a successful fetch/search can support keeping a current link
- HTTP 401/403/429, anti-bot behavior, or a crawler failure does **not** prove a service is dead
- a legacy link is removed from a current entry point only when its purpose is clearly obsolete,
  misleading, or no longer appropriate
- historical links may remain in historical content when they are part of the record

Findings and changes:

- HTN Miner, PEPEPOW Community Pool, PEPEPOW Lab Pool, the main Explorer, MiningPoolStats,
  Mining4People's PEPEW pool, and NestEx all had current public pages that could be identified.
- The current Mining4People PEPEW page still presents HooHash pool information, so Mining4People
  is now linked directly from the Mining page rather than treated only as an old endpoint.
- The PEPEPOW Discord invite `sJgDVRkBcq` is still repeated by current/recent PEPEPOW and
  Mining4People public references and remains the community link.
- NonKYC direct pages were not reliably fetchable by the crawler, but current PEPEPOW Explorer and
  independent market-reference data still report active NonKYC PEPEW markets. The link therefore
  remains, rather than being incorrectly classified as dead from an anti-bot/fetch failure.
- The legacy WhatToMine URL identifies itself as **PepePow-old** and still uses the old Memehash
  context. It was removed from the current homepage.
- Dex-Trade is already treated as a historical delisted venue and was removed from the current
  homepage resource set.
- MiningPower's public overview was reachable but showed no currently listed projects in the
  audited view. It is no longer presented as a current PEPEPOW homepage resource.
- NodeHub's public explorer still lists PEPEPOW, but that does not by itself prove current paid
  hosting terms. The Masternode page now tells users to verify service terms before use.
- Pecunia remains a legacy service reference, but its current PEPEPOW product page could not be
  independently verified in this audit. It is explicitly labeled for re-verification before use.
- The old WordPress homepage's large mixed logo wall was replaced with a concise set of current
  PEPEPOW resources. Specialized market/mining/masternode references now live on their relevant
  pages rather than implying homepage endorsement.
- The About page's **White Paper v2.0** link was found to point incorrectly to the local v1.0.1
  PDF. The canonical v2.0 file is present in the recovered migration archive/media map but was not
  included in the earlier referenced-only public staging set. Until that PDF is deliberately
  staged into `public/docs/legacy/2025/01/`, the page uses the correct v2.0 Google Doc rather
  than pretending the missing local target exists.
- Homepage White Paper v2.1 now uses the recovered local PDF. White Paper v2.0 remains external
  for the same unstaged-file reason above.
- The Market page now uses the PEPEPOW Explorer as the preferred PEPEPOW-specific market reference
  and keeps a smaller secondary tracker set: CoinCodex, LiveCoinWatch, CoinPaprika, Blockspot, and
  CoinCarp. Third-party tracker metadata is explicitly non-authoritative because some trackers lag
  protocol or exchange changes.

A reproducible external-link audit helper is now available at:

`scripts/migration/audit_external_links.py`

By default it inventories/probes links from `home`, `about`, `mining`, `masternode`,
`wallet`, and `market`, writes the detailed result to the ignored
`migration/work/external-link-audit.json`, and classifies results as available, blocked, missing,
or unresolved. Only confirmed HTTP 404/410 results are eligible for the optional
`--strict-missing` failure mode; blocked/network failures remain review items.

CI runs the tool in `--inventory-only` mode so extraction remains regression-tested without
making the normal site build depend on flaky third-party network availability.

Remaining external-link work is intentionally narrower:

1. re-verify Pecunia's current PEPEPOW service status before presenting it as active
2. periodically re-run live probes manually or in a future non-blocking scheduled workflow
3. audit external links inside historical announcements separately, preserving historical context
4. do not interpret a market-data aggregator's exchange list as authoritative service status

No production deployment or Nginx change was made in this slice.

## Current consensus reward/funding verification — 2026-09-19

The remaining DevFee/foundation ambiguity was resolved by reading the current `MattF42/PePe-core`
`master` implementation rather than relying on historical announcements or stale comments.

Current executable reward path:

- `src/validation.cpp::GetFoundationPayment()` returns **250 PEPEW** on mainnet after height
  1,065,649 for a normal block.
- The same function scales that foundation payment with PEPEPOW's special-block pattern:
  **2×** when the relevant height matches the 100-block bonus condition and **5×** on the
  corresponding 1000-block bonus condition.
- `src/masternode-payments.cpp::FillBloc()` creates the foundation coinbase output and subtracts
  that amount from the miner output before the rest of the payment construction completes.
- `src/validation.cpp::GetMasternodePayment()` calculates the masternode payment as
  **35% of (block reward − foundation payment)**.
- `src/masternode-payments.cpp::FillBlockPayee()` assigns the miner the remainder:
  **block reward − masternode payment − foundation payment**, and appends the selected masternode
  output.
- `src/spork.h` retains `SPORK_15_REQUIRE_FOUNDATION_FEE` with its historical 1 Feb 2024
  activation default.

This means the old public shorthand **65% miner / 35% masternode** is not an exact description of
the current coinbase distribution. The current coinbase has three economic outputs in normal
operation: miner, selected masternode, and foundation/development payment. The masternode's 35%
is calculated after the foundation amount is removed; the miner receives the remainder.

The source tree also contains older constants/comments such as a legacy `FOUNDATION` constant and
older percentage wording. Those comments are not used as the website authority when they conflict
with the currently executed `GetFoundationPayment()` / `GetMasternodePayment()` /
`FillBloc()` / `FillBlockPayee()` path.

Resulting content changes:

- About no longer displays a `65% / 35%` metric as current consensus.
- About explains the current three-output coinbase logic and the 250-PEPEW normal-block foundation
  amount.
- Homepage "Dual reward system" wording was replaced by current block-reward distribution wording.
- Historical references to "DevFee" remain valid as historical terminology, while current
  consensus-facing text uses **foundation/development payment** and explains the code-defined split.

This closes the current-consensus funding/reward review gate. Historical posts are not rewritten
solely because they describe older reward eras.

No production deployment or Nginx change was made in this slice.

## Generated announcements archive — 2026-09-19

The recovered WordPress `/announcements/` page was only a small archive snapshot containing four
older post cards and should not be treated as the long-term news index now that all published posts
have been recovered.

The route has therefore been converted to a build-time Astro archive:

- `src/pages/announcements/index.astro` reads the `announcements` content collection
- announcements are sorted newest-first and grouped by publication year
- each item links to its preserved same-path legacy route
- the archive is generated statically; no database or client-side JavaScript is required
- a visible historical-archive notice warns that older software, exchange, pool, service, and
  network-status statements may no longer be current
- the recovered `src/content/pages/announcements.md` remains in the repository as migration
  provenance, but the public `/announcements/` route no longer renders that four-item WordPress
  snapshot
- `src/pages/[...legacy].astro` excludes only the recovered Announcements page entry so the
  explicit generated archive owns `/announcements/` without changing any of the 99 post routes

This change improves completeness and maintainability without rewriting historical announcement
content. Historical individual posts remain `status: draft` / `migration_review: true` and keep
their original dates, titles, categories, and legacy paths.

No production deployment or Nginx change was made in this slice.

## Historical post hygiene and link inventory — 2026-09-19

The next migration-review gate focused on historical announcements/articles as archived records rather
than trying to rewrite old posts into current operational documentation.

Key decisions:

- Historical external links are preserved when they are part of the original record. A 2024/2025
  Dex-Trade, Xeggex, XelisV2, Memehash, miner, or pool link is not silently replaced with a 2026
  service simply because the old service is now inactive.
- Direct readers still need protection from mistaking an archived post for current instructions.
  `LegacyContent.astro` now renders a visible **Historical content** notice for migrated
  announcements/articles and points readers to the current Wallet, Mining, Masternode, Market, and
  Explorer entry points.
- The generated `/announcements/` archive already carries the same historical-context principle;
  this pass extends it to every individual migrated announcement/article route.

### Internal migration-review text

A migration-only blockquote had been inserted into many recovered Markdown files:

`Migration candidate generated from the legacy WordPress export...`

That text is useful to the migration process but should never be public website content.

The migration pipeline now handles this at the source/validation level:

1. `scripts/migration/wxr_extract.py` no longer writes the migration-review blockquote into newly
   staged Markdown; review state remains in frontmatter as `migration_review: true`.
2. all 106 recovered legacy Markdown documents were normalized so the internal blockquote is absent
   from the committed source
3. `scripts/migration/validate_content_links.py` rejects that banner if it reappears in source
   content

An attempted remark-plugin approach was deliberately discarded because the current Astro Markdown
processor would have required an unnecessary additional dependency. The final implementation keeps
the default Astro Markdown stack unchanged.

The source tree was then normalized in batch. **106 recovered legacy Markdown files** that still contained
the internal migration-review blockquote had that blockquote removed without changing their
frontmatter, historical body text, dates, links, commands, or media references. This covers the full set of **7 recovered pages + 99 recovered posts**. The six non-legacy content files did not contain this marker.

The migration-review state remains explicit in frontmatter as `migration_review: true`, and
`wxr_extract.py` no longer emits the public-facing blockquote on future restaging.

### Historical external-link inventory

The existing external-link audit tool is now also run against every file under
`src/content/announcements/*.md` in CI using `--inventory-only`.

This historical inventory is intentionally separate from the current public-page inventory:

- current operational pages are candidates for link replacement/removal after verification
- historical posts preserve original destinations unless a migration/rendering problem makes the
  link unusable as historical evidence
- anti-bot responses or an inactive service today do not invalidate the historical statement that
  the service existed when the post was published

The historical inventory is written to the ignored
`migration/work/announcement-external-link-audit.json` during CI/local validation. Live network
probing remains non-blocking and should be used as a review aid rather than as a reason to
automatically delete historical links.

This closes the first historical-announcement hygiene gate without altering historical claims.

Remaining content-review work:

1. review the smaller `articles` collection for security-sensitive legacy wallet/node commands
2. after content hygiene, move to staging responsive/accessibility/visual review
3. keep production Nginx/deployment out of scope until staging acceptance

No production deployment or Nginx change was made in this slice.

## Historical Markdown readability cleanup — 2026-09-19

A focused readability pass was added after historical-content context and link inventory were in place.

The pass deliberately distinguishes between **formatting artifacts** and **historical meaning**:

- formatting artifacts may be normalized when the intended Markdown structure is unambiguous
- missing emoji are not guessed; stray replacement `?` characters are removed only where the
  surrounding sentence remains complete without them
- historical software versions, pool/exchange destinations, governance outcomes, commands, and
  claims are not modernized merely because they are now obsolete

Recurring migration artifacts now handled reproducibly by `wxr_extract.py`:

- escaped bold markers such as `\*\*text\*\*` → `**text**`
- escaped line-leading bullets such as `\* item` → Markdown list items
- malformed double-bracket links produced during conversion, including
  `[[label](url)]` and `[[label]](url)`

`validate_content_links.py` now rejects those three artifact classes in source content so a future
restage cannot silently reintroduce them.

The first manual cleanup batch also fixed high-confidence one-off artifacts such as:

- broken emoji placeholders around headings and sentence endings
- duplicate punctuation from conversion
- redundant WordPress-generated Markdown link titles
- malformed double-bracket Google Docs / Discord / miner links
- escaped bold/list syntax in several historical announcements
- a duplicated comma in the August 2024 recovery announcement

No historical facts were intentionally altered by this pass.

The validator remains the final authority for whether recurring artifact patterns still exist; any
remaining files identified by CI should be normalized rather than weakening the validation rule.

No production deployment or Nginx change was made in this slice.

## Legacy technical article safety review — 2026-09-19

The recovered `articles` collection contains **26 historical articles**. Several are operational
wallet, masternode, mining, or incident-recovery guides with commands that were valid only for a
specific software/network state.

The site now distinguishes these documents from current operational guides in two layers:

- every migrated historical article receives an additional **Legacy technical guide** notice in
  `LegacyContent.astro`
- articles containing especially sensitive or destructive procedures must also contain a visible
  `> **Legacy safety warning:**` before the first risky command

The technical notice tells readers that old software versions, block heights, peer IPs, download
URLs, paths, and third-party services may be obsolete. It also directs users to stop the wallet
cleanly, keep a separate `wallet.dat` backup before file/blockchain changes, never share private
keys or recovery phrases, and inspect remote install scripts before execution.

A new validator at:

`scripts/migration/validate_legacy_article_safety.py`

scans all legacy articles and requires the inline warning before any of these high-risk patterns:

- `dumpprivkey` / `importprivkey`
- mnemonic/recovery-phrase configuration
- deleting the wallet data directory or `rm -rf`
- `invalidateblock` / `reconsiderblock`
- remote `curl ... | sh/bash` installation
- `masternodeprivkey` configuration
- hard-coded peer IP recovery via `addnode`

The historical commands themselves are preserved as archival evidence. This gate prevents them from
being presented without explicit context; it does not silently rewrite incident-specific block
hashes, old peer addresses, private-key workflow history, or obsolete miner installers into current
instructions.

CI runs this validation together with the existing route, content-link, external-link, and migration
script checks.

Final CI result for this pass:

- legacy articles scanned: **26**
- articles matching high-risk patterns: **10**
- high-risk articles missing or placing the safety warning after the risky command: **0**
- legacy routes: **106 / 106**
- content source issues: **0**
- generated internal-link issues: **0**

No production deployment or Nginx change was made in this slice.

## Staging responsive/accessibility baseline — 2026-09-19

With the major content-migration gates complete, the first staging presentation pass now establishes
a stronger site-wide responsive and accessibility baseline without changing production deployment.

Global layout improvements:

- a keyboard-visible **Skip to content** link targets `main#main-content`
- the brand and primary navigation expose `aria-current="page"` for the current section
- the primary navigation has an explicit accessible label and larger touch targets
- mobile navigation switches to a compact grid at narrow widths rather than relying only on wrapped
  inline links
- all interactive elements receive a clear `:focus-visible` outline
- long links, code blocks, and legacy content can wrap/scroll without forcing horizontal page overflow
- wide legacy tables and code blocks retain local horizontal scrolling on touch devices
- historical technical safety notices receive distinct visual emphasis
- animation/transition duration is minimized for users requesting reduced motion

A new generated-HTML validator is committed at:

`scripts/migration/validate_accessibility_basics.py`

It checks every built HTML file for:

- a non-empty `html[lang]`
- exactly one `main#main-content`
- a skip link targeting `#main-content`
- a primary navigation landmark with `aria-label="Primary"`
- an `alt` attribute on every image (empty alt remains valid for intentionally decorative images)

The validator is part of the normal Site validation workflow. This is intentionally a basic,
deterministic static gate rather than a substitute for later browser-based keyboard, responsive,
screen-reader, and visual staging review.

No production deployment or Nginx change was made in this slice.

## Custom staging homepage — 2026-09-19

The root route no longer renders the recovered WordPress `home.md` body as the site homepage.
That source file remains committed in `src/content/pages/home.md` for migration provenance and
historical comparison.

`src/pages/index.astro` now implements the concise homepage hierarchy defined in
`docs/WEBSITE_PLAN.md`:

- a short PEPEPOW / PEPEW hero with Wallet and Explorer entry points
- a **Network at a glance** card using verified static facts and authoritative links rather than
  introducing a new live-data collector
- **Start here** cards for Wallets, Mining, Masternode, and Market
- the three most recent recovered announcements selected automatically at build time
- a visible archive-context note so announcement history is not mistaken for current operational
  guidance
- a compact set of verified PEPEPOW entry links for Explorer, Core releases, PEPEW Light, HTN
  Miner, community/lab pools, and Discord

The page remains fully static and requires no client-side JavaScript.

The legacy catch-all route now excludes both `home-new` and `announcements`, because those two
paths are owned by explicit Astro pages while their recovered Markdown remains available as
migration provenance.

The staging homepage intentionally does **not** invent live network metrics. A future Network Pulse
should consume the isolated cached read-only monitor summary described in `docs/WEBSITE_PLAN.md`
rather than querying wallet/node RPC or creating a duplicate collector.

No production deployment or Nginx change was made in this slice.



## Phase 2 current-page and Network UX — 2026-09-19

The first Phase 2 core-page refinement replaces the raw migrated-page presentation with a reusable
current-information shell while keeping the recovered Markdown as the maintainable content source.

Current operational page treatment:

- `/about/`, `/wallet/`, `/mining/`, `/masternode/`, and `/market/` now render through
  `src/components/CurrentPage.astro`
- each page receives a consistent current-page header, concise orientation text, high-value action
  links, a visible last-reviewed date, and an automatically generated H2 section navigator
- the five source documents retain their substantive content; only redundant WordPress-era top-level
  headings were normalized so the generated pages have a clearer heading hierarchy
- code blocks, tables, images, long URLs, and page navigation receive responsive styling without
  adding a client-side framework or JavaScript dependency
- historical announcements/articles continue to use `LegacyContent.astro` and keep their historical
  and technical-safety notices

A new static `/network/` page is now part of the primary information architecture:

- the page explains the current PEPEPOW network visibility path and links directly to the live Explorer
- HooHash V110 is presented as a static current protocol fact; changing block height, hashrate,
  masternode count, price, and other live values are deliberately not fabricated or copied into the
  static build
- common network metrics are explained for users without implying a live reading
- the future Network Pulse integration is explicitly constrained to the existing centralized monitor
  plus a minimal cached read-only summary endpoint
- the browser is not connected to wallet/node RPC and no second blockchain collector was introduced

Navigation now includes Network, and the homepage Explore Network action leads to the local
`/network/` orientation page while the Explorer remains the live-data destination.

No production deployment, Nginx change, WordPress retirement, wallet/node configuration change, or
RPC access was performed in this slice.


## Production Astro cutover — 2026-09-19

The static Astro site was deployed on the existing `edison2` production host after the Phase 2 core-page work.

Verified environment:

- Apache 2.4.52 (Ubuntu) is the production web server; Nginx is not installed or required
- Node.js v22.23.2, npm 10.9.8, Git 2.34.1
- repository is already cloned at `~/pepepow-site`
- Apache serves the Astro release through `/var/www/pepepow.net/current`
- HTTP for `pepepow.net` / `www.pepepow.net` redirects to HTTPS
- HTTPS uses the existing Let's Encrypt certificate
- the previous WordPress tree at `/var/www/html/wordpress` remains in place for rollback/reference
- the old local `game.pepepow.net` Apache vhosts were disabled because that hostname is now served by another host
- the deployment does not depend on `rsync`; static releases can be copied with `cp -a`

Local production verification returned HTTP 200 for at least:

- `/about/`
- `/network/`
- `/announcements/`
- `/wallet/`

The website cutover did not stop or reconfigure PEPEPOWd. The observed PEPEPOWd P2P service on TCP 8833 and loopback RPC on TCP 8834 remain outside the website deployment path.

The previously planned Nginx production assumption is superseded by the verified Apache deployment. Operational details are documented in `docs/DEPLOYMENT.md`.
