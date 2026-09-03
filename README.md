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
4. hPanel → **Emails**: create the mailbox `info@olimann.com` (the form sends to it and from it).
   Then give the form the mailbox password so it can send by authenticated SMTP, which is the reliable way on Hostinger:
   in File Manager open `public_html/api/config.sample.php`, replace `PASTE-THE-MAILBOX-PASSWORD-HERE` with the mailbox password,
   and save it as `public_html/api/config.php`. That file is not part of the bundle, so later re-uploads never overwrite it.
   Without it the form falls back to PHP `mail()`, which Hostinger often refuses.
   Submit a test request on `/constraint-audit/`; if it fails, hPanel → Advanced → PHP Configuration → error log shows the SMTP reason.
5. Check `https://olimann.com/`, `/de/`, `/constraint-audit/`, `/imprint/` on a phone and a laptop.

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
