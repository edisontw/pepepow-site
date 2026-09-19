# ChatGPT / Agent Project Context

## Repository authority

- Repository: `edisontw/pepepow-site`
- Primary branch: `main`
- Target site: `pepepow.net`
- GitHub `main` in this repository is the sole authority for the new website once files exist here.

Do not treat conversation cache, the old WordPress site, or the legacy static mirror as newer than this repository.

## Project goal

Rebuild and upgrade the PEPEPOW website as a lightweight, open, maintainable community site.

Long-term direction:

```text
WordPress → retired after migration validation
GitHub → source of truth
Astro → site architecture
Markdown / MDX → announcements and normal content
generated JSON → low-frequency automated data
Apache → static production serving
```

The site is primarily about PEPEPOW. General cryptocurrency information is secondary and should support miners, masternode operators, holders/traders, ordinary users, and people learning about PEPEPOW or cryptocurrency.

Core themes:

- transparent
- decentralized
- community-driven
- open source
- practical
- verifiable

## Migration sources

Use these only as migration/reference sources:

1. WordPress WXR exports supplied through the ChatGPT project
2. legacy mirror at `edisontw/web/portal/pepepow-org/`
3. old `pepepow.org` public URLs
4. existing public PEPEPOW services and repositories

Preserve useful:

- pages
- announcements/posts
- images
- PDFs
- slugs and important historical URLs
- dates, categories and useful metadata

Do not migrate:

- WordPress core
- Elementor as the future layout system
- plugins
- cache
- irrelevant generated metadata
- raw backups that are not needed by the public site

Raw WordPress exports may contain personal/account metadata and must not be committed to the public repository.

## Network monitoring

Reuse and improve the existing monitor where practical:

- repository: `edisontw/pepepow-explorer`
- current monitor location: `monitor/`

Prefer a small read-only public summary endpoint for the main website rather than duplicating wallet/node RPC logic in this repository.

The browser must never directly call wallet/node RPC.

## Architecture constraints

Prefer:

- static generation
- small client-side islands only where needed
- cached read-only APIs
- build-time data generation
- scheduled GitHub Actions for low-frequency external data
- no database unless a future requirement clearly justifies one

Avoid introducing for ordinary site requirements:

- Docker
- a database
- a long-running Node.js website service
- a second blockchain collector
- unnecessary backend infrastructure

## Verified production baseline

Verified on 2026-09-19:

- production host role/name: `edison2`
- web server: Apache 2.4.52 (Ubuntu), not Nginx
- Node.js: v22.23.2
- npm: 10.9.8
- Git: 2.34.1
- repository already exists at `~/pepepow-site`; routine deployment is pull + build, not clone
- Astro production root: `/var/www/pepepow.net/current`
- Apache vhost: `/etc/apache2/sites-available/pepepow.net.conf`
- HTTP redirects to HTTPS; TLS uses the existing Let's Encrypt certificate
- old local `game.pepepow.net` Apache vhosts are disabled because that hostname is served elsewhere
- previous WordPress tree at `/var/www/html/wordpress` is retained for rollback/reference
- `rsync` is not assumed installed; `cp -a` is an acceptable release copy path
- PEPEPOWd TCP 8833 and loopback RPC 8834 are outside website deployment scope and must not be changed

Read `docs/DEPLOYMENT.md` before production deployment or Apache changes.

## Production safety

Website work must not interfere with the PEPEPOW wallet/node.

Never:

- stop or reconfigure the wallet/node for a site update
- touch `wallet.dat`
- modify blockchain data
- expose RPC credentials
- expose masternode/private keys
- reboot the host just for a website deployment

Before production Apache changes:

1. back up the current configuration
2. validate the new configuration
3. use an atomic/static deployment path where practical

Do not commit SSH keys, credentials, tokens, secrets, raw `.env` files, or private server configuration.

## Maintenance flow

Preferred website workflow:

```text
edit
→ validate
→ commit/push GitHub main
→ production server pull
→ Astro build
→ publish static release under /var/www/pepepow.net
→ Apache serve /var/www/pepepow.net/current
```

Use coherent commits. Keep migration scripts reproducible.

## Priorities

Use this priority order:

```text
content recovery/completeness
→ URL preservation
→ maintainability
→ production safety/stability
→ responsive/accessibility
→ useful PEPEPOW tools
→ visual improvement
→ optional new features
```

## Current planning authority

Read `docs/WEBSITE_PLAN.md` before broad implementation work and update it when architecture or scope decisions materially change.
