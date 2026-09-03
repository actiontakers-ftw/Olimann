#!/usr/bin/env python3
"""Build olimann.com into ./dist (static HTML + assets). Run: python3 build.py"""
import math, os, shutil, sys, time
from pathlib import Path
from jinja2 import Environment, FileSystemLoader

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import content as C  # noqa: E402

DIST = HERE.parent / "dist"
BUILD = time.strftime("%Y%m%d%H%M")

# ---------------------------------------------------------------- ring (the mark)
N, R, RAD = 10, 66, 36

def _pos(i, radius=R):
    a = math.radians(-90 + i * 360 / N)
    return radius * math.cos(a), radius * math.sin(a), a

def _disc(x, y, uid, dim):
    """One disc: face gradient, mesh texture, rim. dim=True renders the resting (navy) state."""
    if dim:
        return (f'<circle cx="{x:.2f}" cy="{y:.2f}" r="{RAD}" fill="url(#dim-{uid})"/>'
                f'<circle cx="{x:.2f}" cy="{y:.2f}" r="{RAD-1}" fill="none" stroke="rgba(250,246,232,.28)" stroke-width="1.6"/>')
    return (f'<circle cx="{x:.2f}" cy="{y:.2f}" r="{RAD}" fill="url(#cu-{uid})"/>'
            f'<circle cx="{x:.2f}" cy="{y:.2f}" r="{RAD}" fill="url(#mesh-{uid})"/>'
            f'<circle cx="{x:.2f}" cy="{y:.2f}" r="{RAD-1.3}" fill="none" stroke="url(#rim-{uid})" stroke-width="2.4"/>')

def ring(kind="hero", labels=None, cls=""):
    uid = kind
    diagram = kind == "diagram"
    vb = 172 if diagram else 106
    x9, y9, _ = _pos(N - 1)
    out = [f'<svg class="ring {cls}" viewBox="{-vb} {-vb} {2*vb} {2*vb}" xmlns="http://www.w3.org/2000/svg" aria-hidden="true" focusable="false">',
           '<defs>',
           f'<radialGradient id="cu-{uid}" cx="36%" cy="30%" r="82%"><stop offset="0" stop-color="#E4AE7C"/><stop offset=".5" stop-color="#A45F30"/><stop offset="1" stop-color="#4A2712"/></radialGradient>',
           f'<linearGradient id="rim-{uid}" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#F6D6B0"/><stop offset=".55" stop-color="#B8763F"/><stop offset="1" stop-color="#4E2A14"/></linearGradient>',
           f'<radialGradient id="dim-{uid}" cx="36%" cy="30%" r="82%"><stop offset="0" stop-color="#1B4B8C"/><stop offset="1" stop-color="#0A2750"/></radialGradient>',
           f'<pattern id="mesh-{uid}" width="3" height="3" patternUnits="userSpaceOnUse"><circle cx="1.5" cy="1.5" r=".72" fill="#2A1507" fill-opacity=".42"/></pattern>',
           f'<clipPath id="last-{uid}"><circle cx="{x9:.2f}" cy="{y9:.2f}" r="{RAD}"/></clipPath>',
           '</defs>']
    if not diagram:
        out.append('<g class="spin"><g class="spin-scroll">')
    def seg(i, clip=False, with_label=True):
        x, y, a = _pos(i)
        side = C.SIDES[i]
        attrs = f' clip-path="url(#last-{uid})"' if clip else ''
        if diagram:
            s = [f'<g class="seg {side}" data-i="{i}"{attrs}>',
                 f'<g class="dim">{_disc(x, y, uid, True)}</g>',
                 f'<g class="lit">{_disc(x, y, uid, False)}</g>']
            if with_label and labels:
                lx, ly, _ = _pos(i, R + RAD + 16)
                c = math.cos(a)
                anchor = 'start' if c > 0.35 else ('end' if c < -0.35 else 'middle')
                s.append(f'<text x="{lx:.1f}" y="{ly:.1f}" text-anchor="{anchor}" dominant-baseline="middle">{labels[i]}</text>')
            s.append('</g>')
            return ''.join(s)
        return f'<g{attrs}>{_disc(x, y, uid, False)}</g>'
    for i in range(N):
        out.append(seg(i))
    out.append(seg(0, clip=True, with_label=False))  # seamless overlap: disc 0 over disc 9
    if not diagram:
        out.append('</g></g>')
    out.append('</svg>')
    return ''.join(out)

# ---------------------------------------------------------------- pages
def path_for(key, lang):
    for k, l, p in C.PAGES:
        if k == key and l == lang:
            return p
    return None

def main():
    if DIST.exists():
        shutil.rmtree(DIST)
    shutil.copytree(HERE / "static", DIST, dirs_exist_ok=True)
    (DIST / "assets" / "img" / "favicon.svg").write_text(ring("icon").replace('class="ring "', ''), encoding="utf-8")
    (DIST / "assets" / "img" / "mark.svg").write_text(ring("icon").replace('class="ring "', ''), encoding="utf-8")

    env = Environment(loader=FileSystemLoader(str(HERE / "templates")), autoescape=False, trim_blocks=True, lstrip_blocks=True)
    env.globals.update(ring=ring, site=C.SITE, build=BUILD)
    tpl_for = {"home": "home.html", "method": "method.html", "departments": "departments.html", "who": "who.html",
               "about": "about.html", "audit": "audit.html", "thanks": "simple.html", "imprint": "legal.html", "privacy": "legal.html"}

    written = []
    for key, lang, path in C.PAGES:
        t = C.T[lang]
        alt_lang = "de" if lang == "en" else "en"
        nav = {k: path_for(k, lang) for k in ["home", "method", "departments", "who", "about", "audit", "imprint", "privacy"]}
        ctx = dict(key=key, lang=lang, path=path, t=t, ui=t["ui"], meta=t["meta"][key], nav=nav,
                   alt_lang=alt_lang, alt_path=path_for(key, alt_lang),
                   alternates=[("en", path_for(key, "en")), ("de", path_for(key, "de"))], xdefault=path_for(key, "en"),
                   noindex=key in C.NOINDEX, ring_labels=C.RING[lang])
        html = env.get_template(tpl_for[key]).render(**ctx)
        out = DIST / path.strip("/") / "index.html" if path != "/" else DIST / "index.html"
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(html, encoding="utf-8")
        written.append((path, len(html)))

    # 404 (single file, EN with DE link)
    t = C.T["en"]
    nav = {k: path_for(k, "en") for k in ["home", "method", "departments", "who", "about", "audit", "imprint", "privacy"]}
    html = env.get_template("404.html").render(key="notfound", lang="en", path="/404.html", t=t, ui=t["ui"], meta=("Page not found — Olimann", ""),
                                               nav=nav, alt_lang="de", alt_path="/de/", alternates=[], xdefault="/", noindex=True, ring_labels=C.RING["en"])
    (DIST / "404.html").write_text(html, encoding="utf-8")

    # sitemap
    urls = []
    for key, lang, path in C.PAGES:
        if key in C.SITEMAP_EXCLUDE:
            continue
        alts = ''.join(f'<xhtml:link rel="alternate" hreflang="{l}" href="{C.SITE["domain"]}{path_for(key, l)}"/>' for l in ("en", "de"))
        alts += f'<xhtml:link rel="alternate" hreflang="x-default" href="{C.SITE["domain"]}{path_for(key, "en")}"/>'
        urls.append(f'<url><loc>{C.SITE["domain"]}{path}</loc>{alts}<changefreq>monthly</changefreq><priority>{"1.0" if key == "home" else "0.7"}</priority></url>')
    (DIST / "sitemap.xml").write_text('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">\n' + "\n".join(urls) + "\n</urlset>\n", encoding="utf-8")

    for p, n in written:
        print(f"  {p:38s} {n:>7d} bytes")
    print(f"built {len(written)} pages + 404 + sitemap into {DIST}")

if __name__ == "__main__":
    main()
