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

The mechanical recovery/link-routing gate is complete. The next work should not repeat media recovery,
route wiring, or exact legacy-host link cleanup.

Priority now:

1. Resolve the remaining current-consensus DevFee/funding description directly from PEPEPOW Core code.
2. Audit external links inside historical announcements separately, preserving historical context.
3. Review the recovered Announcements page and historical posts for readability/formatting artifacts that require
   human judgment, without changing historical claims merely to match today's state.
4. Keep content `status: draft` and `migration_review: true` until the remaining review gates are complete.
5. After content review, proceed to staging visual/responsive/accessibility work. Production Nginx remains out of scope
   until staging acceptance.


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
- The About page's exact current DevFee allocation remains deliberately unresolved. Historical
  documents and release notes describe different funding eras; the draft now says this should be
  documented directly from current consensus code before publishing a fixed present-day allocation.

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
  PDF. It now points to the recovered canonical
  `/docs/legacy/2025/01/PEPEPOW-Whitepaper_v2.0.pdf`.
- Homepage White Paper v2.0/v2.1 links now use the recovered local PDFs, reducing dependence on
  editable external Google Docs for canonical website reading.
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

