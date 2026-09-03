# olimann.com

Static, bilingual (EN default, DE under `/de/`) marketing site for Olimann. No framework, no build tooling needed on the server: plain HTML, CSS, one small JS file, self-hosted fonts, and one PHP file for the audit form.

```
brand/           logo colourways (copper is the website mark), source PNGs
site/content.py  every sentence of the site, EN and DE — edit copy here
site/templates/  Jinja2 templates (base, home, method, departments, who, about, audit, legal, 404)
site/static/     CSS, JS, fonts, images, .htaccess, robots.txt, api/send.php — copied into dist as-is
site/build.py    renders content + templates into dist/
dist/            the finished website — this is what goes to the server
olimann-site.zip dist/ zipped for upload
```

## Rebuild after editing copy or templates

```bash
pip install jinja2        # once
cd site && python3 build.py
cd ../dist && zip -r ../olimann-site.zip .   # includes .htaccess
```

## Deploy to Hostinger (shared hosting)

1. hPanel → Websites → olimann.com → **File Manager** → open `public_html`.
2. Delete whatever is in `public_html` (default placeholder files), upload `olimann-site.zip`, right-click → **Extract** into `public_html`, then delete the zip.
   The result must be `public_html/index.html`, `public_html/de/`, `public_html/assets/`, `public_html/.htaccess`, etc. — not `public_html/dist/...`.
3. hPanel → **SSL**: make sure the free certificate is active and "Force HTTPS" is on (the `.htaccess` also redirects to https and drops `www.`).
4. **Form email (Google Workspace).** The mailbox info@olimann.com is on Google Workspace, so the form sends through
   Google's SMTP server, authenticated with an *App Password*:
   - Sign in to Google as info@olimann.com → Manage your Google Account → Security → make sure **2-Step Verification** is on
     (an App Password cannot be created without it; a Workspace admin can enable it for the account).
   - Security → **App passwords** → name it "Olimann website" → Google shows a 16-character password once. Copy it.
   - In Hostinger's File Manager open `public_html/api/config.sample.php`, paste the app password in place of the placeholder,
     and save it as `public_html/api/config.php`. That file is not part of the bundle, so later re-uploads never overwrite it.
   - Submit a test on `/constraint-audit/`. If it fails, hPanel → Advanced → PHP Configuration → error log names the SMTP reason.
   Do **not** create an info@ mailbox in Hostinger's own email service; the domain's mail must keep going to Google.
5. Check `https://olimann.com/`, `/de/`, `/constraint-audit/`, `/imprint/` on a phone and a laptop.

### DNS: keep email on Google when the domain moves to Hostinger

When olimann.com is pointed at Hostinger hosting, check the DNS zone (hPanel → Domains → olimann.com → DNS / Nameservers)
**before and after**: the MX records must still be Google's (`ASPMX.L.GOOGLE.COM` and the `ALT…` entries) and the SPF TXT record
must still contain `include:_spf.google.com`. Hostinger's setup wizard sometimes replaces MX records with its own mail servers,
which would silently stop incoming mail to info@olimann.com. If that happened, restore Google's MX records in the zone editor.

### Before sending the link to anyone

- Fill in the legal facts in `site/content.py` (`imprint` and `privacy` for both languages) — every `[bracketed]` placeholder is marked in copper on the live page. Rebuild and re-upload. A German-facing site with an incomplete Impressum is an Abmahnung risk.
- Confirm the data-centre location Hostinger assigned (hPanel → Hosting → Details) and put it in the privacy policy.

### olimann.de

The old receptionist site should redirect. In the `.htaccess` of the olimann.de hosting:

```
RewriteEngine On
RewriteRule ^ https://olimann.com/de/ [R=301,L]
```

## Notes

- No cookies, no analytics, no third-party requests: no consent banner needed. If analytics are wanted later, Plausible or Umami (cookieless) keep it that way.
- Fonts are served from `/assets/fonts/` (variable Cormorant Garamond, Inter, JetBrains Mono) to avoid the Google-Fonts IP-transfer issue in Germany.
- The mark is rebuilt as inline SVG (`build.py: ring()`), turning slowly in the hero and lighting segments in the flywheel section. The PNG render is used for the social image and touch icon.
