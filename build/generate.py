#!/usr/bin/env python3
"""Generates every static HTML page for Maria Aziz's portfolio from shared
head/nav/footer templates plus per-page content blocks defined below.
Re-run this script any time a page's content or the shared chrome changes."""

import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

NAV_ITEMS = [
    ("Home", "/"),
    ("About", "/about/"),
    ("Work", "/work/"),
    ("Solutions", "/solutions/"),
    ("Research", "/research/"),
    ("Writing", "/writing/"),
    ("Recognition", "/recognition/"),
    ("Now", "/now/"),
]

def nav_html(current_path):
    links = []
    for label, href in NAV_ITEMS:
        current = ' aria-current="page"' if href == current_path else ''
        links.append(f'<a href="{href}"{current}>{label}</a>')
    return "\n                ".join(links)

def head(title, description, path, extra=""):
    # NOTE: no live domain is confirmed for this site yet, so canonical/og:url
    # are deliberately omitted rather than pointing at a guessed domain. Once
    # this site has a real hosting domain, add a SITE_URL constant here and
    # reinstate `<link rel="canonical">` / `og:url` using it.
    return f"""<!doctype html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <meta name="description" content="{description}">
    <meta property="og:type" content="website">
    <meta property="og:title" content="{title}">
    <meta property="og:description" content="{description}">
    <meta name="twitter:card" content="summary">
    <link rel="icon" href="/assets/favicon.svg" type="image/svg+xml">
    <link rel="stylesheet" href="/assets/site.css">
{extra}</head>
"""

def page(title, description, path, body, extra_head="", extra_scripts=""):
    return head(title, description, path, extra_head) + f"""
<body>

    <header class="nav">
        <div class="wrap navin">
            <a class="brand" href="/">
                <span class="mono">MA</span>
                Maria Aziz
            </a>
            <nav class="navlinks">
                {nav_html(path)}
            </nav>
            <div class="navcta">
                <a class="btn primary" href="/contact/">Contact</a>
                <button class="menu" id="menuToggle" aria-label="Open menu">☰</button>
            </div>
        </div>
    </header>

    <main id="top">
{body}
    </main>

    <footer class="wrap foot">
        <span>© <span id="year"></span> Maria Aziz</span>
        <span><a href="https://www.linkedin.com/in/maria-aziz-ai/" target="_blank" rel="noopener">LinkedIn</a> ·
            <a href="https://imadi-technologies.com" target="_blank" rel="noopener">Imadi Technologies</a> ·
            <a href="/contact/">Contact</a></span>
    </footer>
    <script src="/assets/site.js"></script>
{extra_scripts}</body>

</html>
"""

def write(path, content):
    full = os.path.join(ROOT, path.lstrip("/"))
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "w", encoding="utf-8") as f:
        f.write(content)
    print("wrote", path)
