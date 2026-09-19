# PEPEPOW Site

Official source repository for the next-generation PEPEPOW community website at `pepepow.net`.

## Status

Migration and rebuild are in progress.

The new site replaces the legacy WordPress presentation with a maintainable static-first architecture while preserving useful PEPEPOW content, public URLs, media, documents, and historical announcements.

## Direction

- **Source of truth:** this repository (`edisontw/pepepow-site`, branch `main`)
- **Framework:** Astro
- **Content:** Markdown / MDX and structured data
- **Production serving:** Nginx serving the generated `dist/`
- **Dynamic data:** small read-only public APIs only where needed
- **Primary focus:** PEPEPOW information, tools, network visibility, mining, masternodes, wallets, community and education
- **Secondary focus:** small, curated cryptocurrency news and reference information

## Read first

Before substantial website work, read:

1. `CHATGPT_PROJECT_CONTEXT.md`
2. `docs/WEBSITE_PLAN.md`
3. `docs/MIGRATION_REPORT.md` when working on restored WordPress content/media

## Local site development

Current Astro requires Node.js 22.12 or newer. The repository includes `.nvmrc` for Node 22.

```bash
npm install
npm run dev
```

Production-style static build:

```bash
npm run build
```

Output is written to `dist/`.

## WordPress migration inventory

Raw WXR exports are migration inputs and must remain outside Git.

Run the privacy-conscious inventory tool against one or more local exports:

```bash
python3 scripts/migration/wxr_inventory.py \
  /path/to/pepepowcommunityorganization.WordPress.2026-09-18.xml \
  /path/to/pepepowcommunityorganization.WordPress.2026-09-19.xml
```

Local outputs are written to `migration/work/` and ignored by Git.

See `docs/MIGRATION_REPORT.md` for the currently validated inventory.

## Migration sources

Migration sources are evidence/input only and are not future website authority:

1. WordPress WXR exports supplied outside the repository
2. legacy static mirror under `edisontw/web/portal/pepepow-org/`
3. the existing PEPEPOW explorer / monitor project
4. public PEPEPOW repositories and services

Do not copy WordPress/Elementor generated HTML as the long-term content architecture.

## Security

Do not commit:

- SSH keys
- wallet/node credentials
- RPC credentials
- private keys or masternode secrets
- `.env` files
- raw WordPress exports containing author/account metadata
- local migration inventories generated from private inputs

The website must never require direct browser access to wallet/node RPC.

## Deployment

Production deployment will be introduced after migration and staging validation.

Target flow:

```text
edit
→ commit/push main
→ server pull
→ Astro build
→ Nginx serve dist/
```

Production website changes must not stop, reconfigure, or otherwise interfere with the PEPEPOW wallet/node running on the host.
