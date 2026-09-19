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
- [ ] validate old internal links
- [x] build sanitized legacy route preservation map
- [x] batch migrate remaining posts as review-only drafts

## Next migration slice

1. Extract the seven published pages and a representative group of recent/older posts.
2. Normalize WordPress/Elementor body markup into clean content.
3. Create a media manifest and test automatic recovery from current public attachment URLs.
4. Cross-check only unresolved media against `edisontw/web/portal/pepepow-org/` and its raw-asset mapping.
5. Produce a missing-media list; only then request `wp-content/uploads/` from the old host if needed.
6. Validate route preservation before batch migration.


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
