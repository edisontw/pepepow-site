# PEPEPOW Website

Official source repository for the PEPEPOW (PEPEW) community website.

**Live site:** https://pepepow.net

<p align="center">
  <img src="public/media/legacy/2025logo.webp" alt="PEPEPOW logo" width="120" />
</p>

## Overview

The site is built with Astro and generated as a static website. GitHub `main` is the source of truth for the current site.

The project replaces the former WordPress presentation with a maintainable static-first architecture while preserving useful PEPEPOW pages, historical announcements, public URLs, media, and documents.

Primary areas include:

- PEPEPOW network information and status
- wallets
- mining
- masternodes
- market links
- community channels
- announcements and historical records
- learning material and practical tools

## Architecture

- **Framework:** Astro
- **Content:** Markdown / MDX and structured data
- **Production:** static Astro build served by Apache
- **Dynamic data:** small read-only public APIs where required
- **Repository authority:** `edisontw/pepepow-site`, branch `main`

The browser must never connect directly to PEPEPOW wallet/node RPC.

## Local development

Node.js 22.12 or newer is required. The repository includes `.nvmrc` for Node 22.

For a reproducible install:

```bash
npm ci
npm run dev
```

Production-style build:

```bash
npm run build
```

The generated static site is written to `dist/`.

## Repository structure

Key paths:

```text
src/pages/                  Astro routes
src/content/                Markdown content
src/components/             Shared Astro components
src/data/                   Verified structured links/data
public/                     Public media and documents
scripts/migration/          Migration and validation tooling
migration/public/           Sanitized migration metadata
docs/                       Project, migration and deployment documentation
server/admin/               Announcement publisher source
server/deploy/              Restricted deployment helper
```

For substantial work, read:

1. `CHATGPT_PROJECT_CONTEXT.md`
2. `docs/WEBSITE_PLAN.md`
3. `docs/MIGRATION_REPORT.md` for restored WordPress content/media
4. `docs/DEPLOYMENT.md` for production/deployment work

## Contributing

Issues and pull requests are welcome for corrections, documentation, accessibility, site UX, PEPEPOW information, and practical tools.

When contributing:

- keep changes focused and reviewable
- preserve important historical/public URLs
- prefer static generation over unnecessary backend services
- keep operational information verifiable and current
- do not introduce browser access to wallet/node RPC
- do not commit credentials, private keys, tokens, or private server configuration

Site validation runs automatically for pushes and pull requests.

## WordPress migration

The former WordPress site is a migration/reference source only and is not the authority for the current website.

Raw WordPress WXR exports must remain outside Git because they can contain account or author metadata.

Privacy-conscious migration tools are available under `scripts/migration/`. Sanitized public migration metadata is stored under `migration/public/`.

Do not copy WordPress/Elementor-generated HTML as the long-term site architecture.

## Security

Never commit:

- SSH private keys
- GitHub or OAuth tokens/secrets
- wallet/node credentials
- RPC credentials
- wallet private keys or masternode secrets
- `.env` files
- production admin configuration
- raw WordPress exports containing private/account metadata

Example configuration files contain placeholders only. Production secrets are stored outside the repository.

If reporting a security problem, do not include live credentials, private keys, seed phrases, tokens, or other sensitive values in a public issue.

## Deployment

Production deployment is automated from `main` using the restricted deployment workflow documented in `docs/DEPLOYMENT.md`.

The website deployment path is intentionally isolated from PEPEPOW wallet/node operation. Site deployment must not stop, reconfigure, or modify PEPEPOWd, wallet data, blockchain data, or RPC credentials.

## License

Source code authored for this repository is licensed under the **MIT License**. See `LICENSE`.

Original written content created specifically for the current pepepow.net website is generally licensed under **CC BY 4.0** unless otherwise noted. See `CONTENT_LICENSE.md`.

Historical, migrated, and third-party media/documents are excluded from these blanket grants unless their own licensing terms say otherwise. See `NOTICE.md` for provenance and exclusions.
