#!/usr/bin/env python3
"""
Write a redirect page for every page of a site that moved to another organisation.

GitHub does not redirect a Pages address after a repository transfer. The 404
page of this site sends visitors on, but a search engine only sees the 404.
A real page with an instant meta refresh is read as a permanent redirect, so
each old address gets one.

    python generate_redirects.py

Run it again when a moved site gets new pages. The list of pages comes from
the sitemap of the new site.
"""

import re
import urllib.request
from html import escape
from pathlib import Path

ROOT = Path(__file__).resolve().parent

# Old directory on minbzk.github.io -> new address, and where its pages are listed.
MOVED_SITES = {
    "NeRDS": {
        "target": "https://nerds.digitaledienst.overheid.nl",
        "sitemap": "https://nerds.digitaledienst.overheid.nl/sitemap.xml",
    },
    # Storybook addresses a story in the query string, so two pages cover it.
    "storybook": {
        "target": "https://nederlandsedigitaledienst.github.io/design-system",
        "pages": ["", "iframe.html"],
    },
    # The old RegelRecht landing page had two pages; the site now has its own domain.
    "regelrecht": {
        "target": "https://regelrecht.rijks.app",
        "pages": ["", "aanmelden/"],
    },
}

PAGE = """<!DOCTYPE html>
<html lang="nl">
<head>
    <meta charset="UTF-8">
    <title>Deze pagina is verhuisd</title>
    <link rel="canonical" href="{url}">
    <script>
        // Takes the query string and the anchor along; the meta refresh below cannot.
        window.location.replace("{url}" + window.location.search + window.location.hash);
    </script>
    <meta http-equiv="refresh" content="0; url={url}">
</head>
<body>
    <p>Deze pagina is verhuisd naar <a href="{url}">{url}</a>.</p>
</body>
</html>
"""


def pages_from_sitemap(sitemap_url: str, target: str) -> list[str]:
    with urllib.request.urlopen(sitemap_url, timeout=30) as response:
        sitemap = response.read().decode("utf-8")
    locations = re.findall(r"<loc>([^<]+)</loc>", sitemap)
    return sorted(location.removeprefix(target).lstrip("/") for location in locations if location.startswith(target))


def write_site(directory: str, site: dict) -> int:
    pages = site.get("pages") or pages_from_sitemap(site["sitemap"], site["target"])
    for page in pages:
        url = f"{site['target']}/{page}"
        relative = page if page.endswith(".html") else f"{page}index.html"
        output = ROOT / directory / relative
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text(PAGE.format(url=escape(url, quote=True)), encoding="utf-8")
    return len(pages)


def main() -> None:
    for directory, site in MOVED_SITES.items():
        print(f"{directory}: {write_site(directory, site)} pages")


if __name__ == "__main__":
    main()
