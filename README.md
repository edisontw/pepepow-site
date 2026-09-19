# PEPEPOW Site

Official source repository for the next-generation PEPEPOW community website at `pepepow.net`.

## Status

Planning and migration are in progress.

The new site will replace the legacy WordPress presentation with a maintainable static-first architecture while preserving useful PEPEPOW content, public URLs, media, documents, and historical announcements.

## Direction

- **Source of truth:** this repository (`edisontw/pepepow-site`, branch `main`)
- **Framework:** Astro
- **Content:** Markdown / MDX and structured data
- **Production serving:** Nginx serving the generated `dist/`
- **Dynamic data:** small read-only public APIs only where needed
- **Primary focus:** PEPEPOW information, tools, network visibility, mining, masternodes, wallets, community and education
- **Secondary focus:** small, curated cryptocurrency news and reference information

## Migration sources

Migration sources are evidence/input only and are not future website authority:

1. WordPress WXR exports supplied outside the repository
2. legacy static mirror under `edisontw/web/portal/pepepow-org/`
3. the existing PEPEPOW explorer / monitor project
4. public PEPEPOW repositories and services

Do not copy WordPress/Elementor generated HTML as the long-term content architecture.

## Read first

Before substantial website work, read:

1. `CHATGPT_PROJECT_CONTEXT.md`
2. `docs/WEBSITE_PLAN.md`

## Security

Do not commit:

- SSH keys
- wallet/node credentials
- RPC credentials
- private keys or masternode secrets
- `.env` files
- raw WordPress exports containing author/account metadata

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
