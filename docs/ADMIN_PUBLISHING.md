# PEPEPOW Admin Publishing

Status: **source implemented; production setup required**

The site now includes a private publishing interface at:

`https://pepepow.net/admin/`

It is intentionally omitted from normal site navigation and marked `noindex`.

## Goal

The publishing flow is:

```text
pepepow.net/admin/
        ↓
Sign in with GitHub
        ↓
github.com authentication / 2FA
        ↓
GitHub redirects to pepepow.net/admin-api
        ↓
allowlisted GitHub identity receives a short-lived signed session
        ↓
announcement form
        ↓
server-side GitHub API write
        ↓
edisontw/pepepow-site main
        ↓
normal site build/deployment
```

The user never enters a GitHub password into pepepow.net.

## Security model

The publisher intentionally does **not** use a shared website password.

Authentication:

- GitHub handles account authentication and 2FA.
- OAuth requests only `read:user`.
- The OAuth access token is used once to read the GitHub login name and is then discarded.
- Only GitHub usernames listed in `allowed_users` receive a PEPEPOW publisher session.
- The publisher session is an HMAC-signed, short-lived, Secure + HttpOnly cookie.
- Publish POST requests require the exact `https://pepepow.net` browser origin.

Repository write access:

- The browser never receives a GitHub repository token.
- A separate **fine-grained personal access token** is stored only on `edison2`.
- Restrict that token to the single repository `edisontw/pepepow-site`.
- Give it repository **Contents: Read and write** only. Do not grant Actions, Administration, Secrets, or organization-wide access.
- The API only creates files under `src/content/announcements/`.
- Existing announcement paths are never silently overwritten.

No database and no long-running Node.js service are introduced.

## 1. Create the GitHub OAuth App

In the GitHub account that owns/manages the website integration, open:

`GitHub → Settings → Developer settings → OAuth Apps → New OAuth App`

Use:

- Application name: `PEPEPOW Publisher`
- Homepage URL: `https://pepepow.net/admin/`
- Authorization callback URL: `https://pepepow.net/admin-api?action=callback`

After creation, note:

- Client ID
- Client secret

Do not commit either secret.

## 2. Create the publishing token

Create a **fine-grained personal access token**.

Recommended restrictions:

- Resource owner: `edisontw`
- Repository access: **Only select repositories**
- Repository: `pepepow-site`
- Repository permissions:
  - Contents: **Read and write**
  - Metadata: automatic/read-only
- Everything else: no access
- Prefer an expiry date and rotate it periodically.

This token is used only by the server-side publisher API.

## 3. Install the CGI backend on edison2

The source file is:

`server/admin/pepepow_admin.py`

From the production repository:

```bash
cd ~/pepepow-site
git pull --ff-only origin main

sudo install -d -m 0755 /usr/local/lib/cgi-bin
sudo install -m 0755 server/admin/pepepow_admin.py /usr/local/lib/cgi-bin/pepepow-admin.cgi

sudo install -d -m 0750 -o root -g www-data /etc/pepepow-admin
sudo cp server/admin/config.example.json /etc/pepepow-admin/config.json
sudo chown root:www-data /etc/pepepow-admin/config.json
sudo chmod 0640 /etc/pepepow-admin/config.json
```

Edit the protected configuration:

```bash
sudo nano /etc/pepepow-admin/config.json
```

Set:

- `github_client_id`
- `github_client_secret`
- `github_publish_token`
- `session_secret`
- `allowed_users`

Generate a session secret locally on the server:

```bash
openssl rand -hex 32
```

Initially keep:

```json
"allowed_users": ["edisontw"]
```

Additional administrators can be added later without changing the public site.

## 4. Enable Apache CGI only for the admin endpoint

Back up the vhost before editing it:

```bash
sudo cp /etc/apache2/sites-available/pepepow.net.conf \
  /etc/apache2/sites-available/pepepow.net.conf.bak-$(date +%Y%m%d-%H%M%S)
```

Enable Ubuntu's CGI module:

```bash
sudo a2enmod cgid
```

Inside the HTTPS `pepepow.net` virtual host, add:

```apache
ScriptAlias /admin-api /usr/local/lib/cgi-bin/pepepow-admin.cgi

<Directory "/usr/local/lib/cgi-bin">
    Options +ExecCGI -Indexes
    Require all granted
</Directory>

<Location "/admin-api">
    LimitRequestBody 200000
</Location>
```

The public Astro document root remains unchanged.

Validate before reload:

```bash
sudo apache2ctl configtest
sudo apache2ctl -S
```

Only after `Syntax OK`:

```bash
sudo systemctl reload apache2
```

Do not reboot the host and do not modify PEPEPOWd.

## 5. Verify authentication

First verify the anonymous session endpoint:

```bash
curl -i 'https://pepepow.net/admin-api?action=session'
```

Expected before login:

```text
HTTP 401
{"error":"Sign in required."}
```

Then open:

`https://pepepow.net/admin/`

Select **Sign in with GitHub**.

Expected flow:

1. Browser leaves pepepow.net.
2. Authentication occurs on `github.com`.
3. GitHub returns to `https://pepepow.net/admin-api?action=callback`.
4. The API verifies the GitHub username against `allowed_users`.
5. Browser returns to `/admin/`.
6. The announcement editor becomes visible.

## 6. Announcement format

The form creates:

```text
src/content/announcements/YYYY-MM-DD-slug.md
```

New announcements use:

```yaml
status: published
migration_review: false
```

They do not receive the historical-content warning used by migrated WordPress posts.

New announcement routes are generated from the current slug when no historical `legacy_url` exists.

## 7. Publishing behavior

A successful publish:

1. validates title, timestamp, slug, categories, tags and body;
2. refuses to overwrite an existing announcement path;
3. creates one Markdown file on GitHub `main`;
4. returns the GitHub commit URL and expected public announcement URL.

At this stage, publication to GitHub and production deployment remain separate operations unless the production deployment workflow is enabled.

## Operational boundaries

The admin publisher must never:

- access PEPEPOWd RPC;
- read wallet files;
- expose wallet/node credentials;
- share the GitHub publishing token with browser JavaScript;
- store GitHub passwords;
- use a shared administrator password;
- write arbitrary repository paths;
- reboot the production host.

The protected config at `/etc/pepepow-admin/config.json` must never be committed.
