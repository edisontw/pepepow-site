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


## GitHub Actions production deployment

An opt-in workflow now exists at:

`.github/workflows/deploy-production.yml`

It is deliberately disabled until the repository variable below is set:

```text
PRODUCTION_DEPLOY_ENABLED=true
```

When enabled, every push to `main` triggers a dedicated SSH connection to `edison2`. The SSH key should be restricted to one forced deployment command rather than being usable as a normal shell key.

The server-side helper source is:

`server/deploy/pepepow-site-deploy`

Install it as a root-owned executable:

```bash
cd ~/pepepow-site
git pull --ff-only origin main

sudo install -m 0755 -o root -g root \
  server/deploy/pepepow-site-deploy \
  /usr/local/sbin/pepepow-site-deploy
```

The helper:

1. refuses deployment when tracked production-repository changes are present;
2. fetches and fast-forwards the existing `~/pepepow-site` checkout;
3. runs `npm ci` and `npm run build` as the `ubuntu` user;
4. checks required static routes, including `/admin/`;
5. copies `dist/` into a timestamped release directory;
6. atomically repoints `/var/www/pepepow.net/current`.

It does not restart Apache, reboot the host, or touch PEPEPOWd.

### Restricted deployment SSH key

Create a **separate** Ed25519 key for GitHub Actions. Do not reuse a personal SSH key.

Install its public key in `/home/ubuntu/.ssh/authorized_keys` with a forced command:

```text
restrict,command="sudo -n /usr/local/sbin/pepepow-site-deploy" ssh-ed25519 AAAA... pepepow-github-deploy
```

Allow only that deployment helper through sudo:

```bash
sudo visudo -f /etc/sudoers.d/pepepow-site-deploy
```

Add:

```text
ubuntu ALL=(root) NOPASSWD: /usr/local/sbin/pepepow-site-deploy
```

Validate sudoers:

```bash
sudo visudo -cf /etc/sudoers.d/pepepow-site-deploy
```

The forced-command key cannot request an interactive shell or substitute another SSH command.

### GitHub production settings

Create a GitHub environment named `production`, then configure:

Repository/environment secrets:

- `PRODUCTION_SSH_KEY` — the dedicated private key
- `PRODUCTION_KNOWN_HOSTS` — the verified SSH known-hosts line for edison2

Repository/environment variables:

- `PRODUCTION_SSH_HOST` — the public SSH host or address
- `PRODUCTION_SSH_USER` — `ubuntu`
- `PRODUCTION_DEPLOY_ENABLED` — set to `true` only after the restricted key and helper are tested

Do not obtain the host key blindly inside CI. Verify the edison2 SSH host key through an already trusted connection before storing `PRODUCTION_KNOWN_HOSTS`.

### Test before enabling push deployments

From edison2, test the helper directly:

```bash
sudo /usr/local/sbin/pepepow-site-deploy
```

Then use the GitHub `Deploy production` workflow with `workflow_dispatch` after setting the required secrets and variables.

Only after a successful controlled test should `PRODUCTION_DEPLOY_ENABLED` be set to `true`.

Once enabled, the announcement publisher flow becomes:

```text
/admin/ Publish
→ GitHub main
→ GitHub Actions
→ restricted SSH command on edison2
→ pull / build / static release
→ pepepow.net updated
```
