"""Report translation state of a language folder against the English sources.

  python3 tools/i18n/status.py --lang de            # counts + lists
  python3 tools/i18n/status.py --lang de --json
  python3 tools/i18n/status.py --lang de --fail-on orphan,broken-assets   # exit 1 if any

Categories (a page is in exactly one of the first five):
  current      translated and its source is unchanged since
  outdated     source changed since translation (or the header is missing)
  untranslated scaffold copy that nobody translated yet
  missing      no file under <lang>/ (docsify falls back to English)
  orphan       file under <lang>/ whose source no longer exists
  broken-assets (extra flag) page has an asset link whose ../ prefix is not depth-correct
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

from common import (ROOT, has_misresolved_asset_links, parse_header, rewrite_asset_links,
                    sha_of, source_pages)

CATEGORIES = ["current", "outdated", "untranslated", "missing", "orphan", "broken-assets"]


def status(root: Path, lang: str) -> dict[str, list[str]]:
    res: dict[str, list[str]] = {c: [] for c in CATEGORIES}
    sources = source_pages(root, exclude=(lang,))
    for page in sources:
        src, dst = root / page, root / lang / page
        if not dst.exists():
            res["missing"].append(page)
            continue
        text = dst.read_text(encoding="utf-8")
        if has_misresolved_asset_links(text, page):
            res["broken-assets"].append(page)
        header = parse_header(text)
        if header is None or header[1] != sha_of(src):
            res["outdated"].append(page)
            continue
        body = text.split("\n", 1)[1] if "\n" in text else ""
        if body == rewrite_asset_links(src.read_text(encoding="utf-8"), page):
            res["untranslated"].append(page)
        else:
            res["current"].append(page)
    known = {page for page in sources}
    for p in sorted((root / lang).rglob("*.md")):
        rel = p.relative_to(root / lang).as_posix()
        if rel.startswith("_") or rel in known:
            continue
        res["orphan"].append(f"{lang}/{rel}")
    return res


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--lang", required=True)
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--fail-on", default="", help="comma-separated categories that make the exit code 1")
    a = ap.parse_args(argv)
    res = status(ROOT, a.lang)
    if a.json:
        print(json.dumps(res, indent=2))
    else:
        total = len(source_pages(ROOT, exclude=(a.lang,)))
        print(f"{a.lang}: {len(res['current'])}/{total} current, {len(res['outdated'])} outdated, "
              f"{len(res['untranslated'])} untranslated, {len(res['missing'])} missing, "
              f"{len(res['orphan'])} orphan, {len(res['broken-assets'])} broken-assets")
        for cat in CATEGORIES[1:]:
            for page in res[cat]:
                print(f"  {cat:13} {page}")
    bad = [c for c in a.fail_on.split(",") if c and res.get(c)]
    return 1 if bad else 0


if __name__ == "__main__":
    raise SystemExit(main())
