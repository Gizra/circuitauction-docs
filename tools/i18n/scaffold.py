"""Create untranslated copies of English pages under <lang>/ for an agent to translate.

Usage:
  python3 tools/i18n/scaffold.py --lang de --sidebar          # de/_sidebar.md
  python3 tools/i18n/scaffold.py --lang de client/README.md    # one page
  python3 tools/i18n/scaffold.py --lang de --all               # every missing page
  python3 tools/i18n/scaffold.py --lang de --restamp client/README.md   # refresh header sha only
Existing files are never overwritten.
"""
from __future__ import annotations

import argparse
from pathlib import Path

from common import (LANG_RE, ROOT, HEADER_RE, parse_header, make_header, rewrite_asset_links, rewrite_page_links,
                    rewrite_sidebar_links, sha_of, source_pages)


def scaffold_page(root: Path, lang: str, page: str) -> Path | None:
    src, dst = root / page, root / lang / page
    if dst.exists():
        return None
    dst.parent.mkdir(parents=True, exist_ok=True)
    body = rewrite_page_links(rewrite_asset_links(src.read_text(encoding="utf-8"), page), page, lang, root)
    dst.write_text(make_header(page, sha_of(src)) + "\n" + body, encoding="utf-8")
    return dst


def validate(root: Path, lang: str, pages: list[str]) -> None:
    if not LANG_RE.match(lang):
        raise ValueError(f"invalid --lang {lang!r} (expected e.g. de, zh-hans)")
    known = set(source_pages(root))
    for page in pages:
        if page not in known:
            raise ValueError(f"not a translatable source page: {page}")


def restamp_page(root: Path, lang: str, page: str) -> Path:
    """Rewrite only the provenance header of <lang>/<page> with the current source sha."""
    dst = root / lang / page
    if not dst.exists():
        raise ValueError(f"{lang}/{page} does not exist")
    text = dst.read_text(encoding="utf-8")
    if not parse_header(text):
        raise ValueError(f"{lang}/{page} has no i18n header")
    new = make_header(page, sha_of(root / page))
    dst.write_text(HEADER_RE.sub(lambda m: new, text, count=1), encoding="utf-8")
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
    ap.add_argument("--restamp", action="store_true",
                    help="only refresh the header sha of existing <lang>/<page> files")
    ap.add_argument("pages", nargs="*", help="source pages, e.g. client/README.md")
    a = ap.parse_args(argv)
    pages = source_pages(ROOT) if a.all else a.pages
    try:
        validate(ROOT, a.lang, pages)
        if a.restamp:
            for page in pages:
                print("restamped", restamp_page(ROOT, a.lang, page))
            return 0
    except ValueError as e:
        ap.error(str(e))
    created = []
    if a.sidebar:
        created.append(scaffold_sidebar(ROOT, a.lang))
    for page in pages:
        created.append(scaffold_page(ROOT, a.lang, page))
    for p in created:
        print("created" if p else "exists ", p or "")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
