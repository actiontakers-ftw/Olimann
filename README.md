# olimann.com

Static, bilingual (EN default, DE under `/de/`) marketing site for Olimann. No framework, no build tooling needed on the server: plain HTML, CSS, one small JS file, self-hosted fonts, and one PHP file for the audit form.

```
brand/           logo colourways (copper is the website mark), source PNGs
site/content.py  every sentence of the site, EN and DE — edit copy here
site/templates/  Jinja2 templates (base, home, method, departments, who, about, audit, legal, 404)
site/static/     CSS, JS, fonts, images, .htaccess, robots.txt, api/ (form handler + storage), inbox/ — copied into dist as-is
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
2. Delete the default placeholder files, upload `olimann-site.zip`, right-click → **Extract** into `public_html`, then delete the zip.
   The result must be `public_html/index.html`, `public_html/de/`, `public_html/assets/`, `public_html/.htaccess`, etc. — not `public_html/dist/...`.
3. hPanel → **SSL**: make sure the free certificate is active (the `.htaccess` redirects to https and drops `www.`).
4. Open `https://olimann.com/`, `/de/` and `/constraint-audit/` on a phone and a laptop.
5. After every re-upload: hPanel → Websites → Manage → **Cache Manager → Purge All**, then hard-refresh the browser.

## Reading audit requests

Every form submission is saved on the server and shown at **https://olimann.com/inbox/** (password-protected; the initial
password was handed over separately — change it inside the inbox under "Change the inbox password"). The inbox lists requests
newest first and has a **Download CSV** button for Excel or Google Sheets.

- Data lives in the folder `olimann-data` *next to* `public_html` (outside the web root), so re-uploading the site never touches it.
  If that location is not writable, `public_html/api/data/` is used instead and is blocked from web access.
- The inbox locks an address out for 15 minutes after 8 wrong passwords.

### Optional: email notifications

The form also tries to email each request to info@olimann.com. Because that mailbox is on Google Workspace, PHP's plain
`mail()` will often be junked or dropped. For reliable emails, once: create a Google **App Password** for info@olimann.com
(Google Account → Security → 2-Step Verification on → App passwords), open `public_html/api/config.sample.php` in File Manager,
paste it in, and save as `public_html/api/config.php`. Not required — the inbox always has every request.

### Before sending the link to anyone

- Fill in the legal facts in `site/content.py` (`imprint` and `privacy` for both languages) — every `[bracketed]` placeholder is marked in copper on the live page. Rebuild and re-upload. A German-facing site with an incomplete Impressum is an Abmahnung risk.
- Confirm the data-centre location Hostinger assigned (hPanel → Hosting → Details) and put it in the privacy policy.

### DNS: keep email on Google when the domain moves to Hostinger

When olimann.com is pointed at Hostinger hosting, check the DNS zone (hPanel → Domains → olimann.com → DNS / Nameservers)
**before and after**: the MX records must still be Google's (`ASPMX.L.GOOGLE.COM` and the `ALT…` entries) and the SPF TXT record
must still contain `include:_spf.google.com`. Hostinger's setup wizard sometimes replaces MX records with its own mail servers,
which would silently stop incoming mail to info@olimann.com. If that happened, restore Google's MX records in the zone editor.

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
