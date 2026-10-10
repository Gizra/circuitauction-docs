"""Create untranslated copies of English pages under <lang>/ for an agent to translate.

Usage:
  python3 tools/i18n/scaffold.py --lang de --sidebar          # de/_sidebar.md
  python3 tools/i18n/scaffold.py --lang de client/README.md    # one page
  python3 tools/i18n/scaffold.py --lang de --all               # every missing page
Existing files are never overwritten.
"""
from __future__ import annotations

import argparse
from pathlib import Path

from common import (ROOT, make_header, rewrite_asset_links, rewrite_sidebar_links,
                    sha_of, source_pages)


def scaffold_page(root: Path, lang: str, page: str) -> Path | None:
    src, dst = root / page, root / lang / page
    if dst.exists():
        return None
    dst.parent.mkdir(parents=True, exist_ok=True)
    body = rewrite_asset_links(src.read_text(encoding="utf-8"))
    dst.write_text(make_header(page, sha_of(src)) + "\n" + body, encoding="utf-8")
    return dst


def scaffold_sidebar(root: Path, lang: str) -> Path | None:
    dst = root / lang / "_sidebar.md"
    if dst.exists():
        return None
    dst.parent.mkdir(parents=True, exist_ok=True)
    src = (root / "_sidebar.md").read_text(encoding="utf-8")
    dst.write_text(rewrite_sidebar_links(src, lang), encoding="utf-8")
    return dst


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--lang", required=True)
    ap.add_argument("--all", action="store_true", help="scaffold every source page that is missing")
    ap.add_argument("--sidebar", action="store_true", help="scaffold <lang>/_sidebar.md")
    ap.add_argument("pages", nargs="*", help="source pages, e.g. client/README.md")
    a = ap.parse_args(argv)
    created = []
    if a.sidebar:
        created.append(scaffold_sidebar(ROOT, a.lang))
    for page in (source_pages(ROOT) if a.all else a.pages):
        if not (ROOT / page).exists():
            ap.error(f"no such source page: {page}")
        created.append(scaffold_page(ROOT, a.lang, page))
    for p in created:
        print("created" if p else "exists ", p or "")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
