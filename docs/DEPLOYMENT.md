# Production Deployment Baseline

Verified on **2026-09-19** after the first Astro production cutover.

## Current production stack

- Host role/name: `edison2`
- OS family: Ubuntu
- Public site: `https://pepepow.net`
- Source authority: `edisontw/pepepow-site` branch `main`
- Site framework: Astro static output
- Web server: Apache HTTP Server **2.4.52 (Ubuntu)**
- Node.js: **v22.23.2**
- npm: **10.9.8**
- Git: **2.34.1**
- Production document root: `/var/www/pepepow.net/current`
- Previous WordPress tree retained for rollback/reference: `/var/www/html/wordpress`
- Apache vhost source: `/etc/apache2/sites-available/pepepow.net.conf`
- TLS: existing Let's Encrypt certificate for `pepepow.net`

Do not install or introduce Nginx merely for this site. Apache is the verified production web server.

## Apache behavior

The production vhost is expected to provide:

- port 80: `pepepow.net` and `www.pepepow.net`, redirecting to HTTPS
- port 443: static Astro files from `/var/www/pepepow.net/current`
- existing Let's Encrypt TLS for `pepepow.net`

The old local `game.pepepow.net` Apache vhosts were disabled on 2026-09-19 because that hostname is served from another host.

If the Apache vhost is edited again, remove or replace any stale WordPress-specific `<Directory /var/www/html/wordpress>` block with an appropriate static-site directory rule. Do not re-enable WordPress rewrite behavior for the Astro document root.

## Protected services and ports

Website deployment must remain isolated from PEPEPOW and database services.

Verified listening services on 2026-09-19 included:

- Apache: TCP 80 / 443
- PEPEPOWd P2P: TCP 8833
- PEPEPOWd RPC: TCP 8834 on loopback only
- MySQL: TCP 3306 / 33060 on loopback only
- SSH: TCP 22

Never stop, reconfigure, expose, or reuse the PEPEPOWd RPC/P2P ports for website deployment. Never make browser code connect directly to wallet/node RPC.

## Normal deployment flow

The repository is already cloned on the production host. Do not clone it again for routine updates.

```bash
cd ~/pepepow-site

git status
git pull --ff-only origin main

npm ci
npm run build
```

The Astro build output is `dist/`.

Use timestamped release directories and keep Apache pointed at the stable `current` path:

```bash
RELEASE="/var/www/pepepow.net/releases/$(date +%Y%m%d-%H%M%S)"

sudo mkdir -p "$RELEASE"
sudo cp -a dist/. "$RELEASE"/
sudo ln -sfn "$RELEASE" /var/www/pepepow.net/current
```

`rsync` is not assumed to be installed on this host.

Before reloading Apache:

```bash
sudo apache2ctl configtest
sudo apache2ctl -S
```

Only after `Syntax OK`:

```bash
sudo systemctl reload apache2
```

Use **reload**, not a host reboot. A normal static-site deployment must not stop or restart PEPEPOWd.

## Local verification

HTTP redirect:

```bash
curl -I -H 'Host: pepepow.net' http://127.0.0.1/
```

HTTPS static routes:

```bash
curl -kI --resolve pepepow.net:443:127.0.0.1 https://pepepow.net/
curl -kI --resolve pepepow.net:443:127.0.0.1 https://pepepow.net/about/
curl -kI --resolve pepepow.net:443:127.0.0.1 https://pepepow.net/network/
curl -kI --resolve pepepow.net:443:127.0.0.1 https://pepepow.net/announcements/
curl -kI --resolve pepepow.net:443:127.0.0.1 https://pepepow.net/wallet/
```

The 2026-09-19 cutover returned HTTP 200 for the tested Astro routes.

## Rollback principle

Keep the prior WordPress tree and prior Apache configuration until the Astro site is fully accepted.

Before significant Apache changes:

1. back up `/etc/apache2` or at minimum the affected vhost
2. preserve the previous `current` release target
3. run `apache2ctl configtest`
4. reload Apache only after validation

Never delete the previous release or WordPress tree as part of the same deployment step that changes the live document root.
