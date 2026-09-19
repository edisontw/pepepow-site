# PEPEPOW Migration Report

Status: **Initial WXR inventory validated**  
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
- [ ] convert the seven pages to normalized site content
- [ ] convert representative posts
- [ ] validate old internal links
- [ ] build final redirect map
- [ ] batch migrate remaining posts

## Next migration slice

1. Extract the seven published pages and a representative group of recent/older posts.
2. Normalize WordPress/Elementor body markup into clean content.
3. Create a media manifest and test automatic recovery from current public attachment URLs.
4. Cross-check unresolved media against `edisontw/web/portal/pepepow-org/`.
5. Produce a missing-media list; only then request `wp-content/uploads/` from the old host if needed.
6. Validate route preservation before batch migration.
