# Multilingual Docs (German first) Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Publish docs.circuitauction.com in German under `/#/de/…` (English fallback for anything not yet translated), with a language switcher, German search / pagination labels, German release-note videos, and tooling that turns "add French" into a repeat of the same steps.

**Architecture:** English stays at the root URLs (nothing moves, every existing link and the backoffice help links keep working). Each language is a mirror folder (`de/client/how-to-create-a-client.md` ↔ `client/how-to-create-a-client.md`) with its own `_sidebar.md` and `_coverpage.md`; docsify's `fallbackLanguages` serves the English page when a German one is missing. Every translated page starts with a hidden provenance comment (`<!-- i18n source=… sha=… -->`) so a small stdlib-Python toolset (`tools/i18n/`) can scaffold pages, report missing / outdated / untranslated pages, and build a UI-terminology glossary from the backoffice `locale-<lang>.json` files. Translation itself is done by Claude Code following a repo skill (`.claude/skills/translate-docs`) that encodes the rules and the glossary. Videos reuse OpenMontage's existing per-language flow (`<name>.i18n.de.json` → `timings.de.json` → `render_tutorial(lang="de")`).

**Tech Stack:** docsify 4 (CDN, no build), docsify search / pagination / copy-code plugins, Python 3 stdlib + `unittest`, Claude Code skill, OpenMontage circuit-video MCP, AngularJS backoffice (`angular-translate`, `localStorageService`), Cypress tutorial specs.

**Spec:** this plan is the spec. The request was "add German to the docs, and more languages in the future". Facts it argues from (verified 2026-10-10):

- Docs: 111 markdown pages, ~33,500 words, 102 screenshots in `assets/screenshots/` (English UI). Hosted on GitHub Pages at docs.circuitauction.com, deployed straight from `master` (no workflow, no build).
- The backoffice UI ships locale files for `de, fr, he, nl, ru, zh-hans` (`circuitauction-backoffice/client/app/i18n/locale-<lang>.json`), chosen in the UI via `SwitchLanguageCtrl` and stored by `localStorageService.set('language', code)`. `locale-de.json` is **not complete**: 1,559 of 2,810 strings are still identical to English (`checkTranslations.js` copies missing keys from `locale-en.json`).
- The backoffice embeds the docs in an iframe (`app/views/documentation/main.html`, `src="https://docs.circuitauction.com/#/README"`) and links four import help pages from `controllers/dashboard/sale.js:1726-1756`.
- The circuit-video MCP already supports translations: `get_tutorial_text(tutorial, lang)` → `save_tutorial_translation` → `author_tutorial(lang)` → `render_tutorial(lang)`; narration backend is ElevenLabs `eleven_multilingual_v2` with voices configured for `de,en` only. The Cypress bridge passes `tutorialLang` into `Cypress.env`.

## Global Constraints

- English pages stay where they are; language folders are ISO codes exactly as the backoffice uses them: `de`, `fr`, `he`, `nl`, `ru`, `zh-hans`.
- A translated page keeps the **same relative path and file name** as its source (only the folder prefix differs).
- A translated page's first line is `<!-- i18n source=<source path> sha=<12 hex> -->`; never hand-edit the sha, re-run the tooling.
- Asset links in translated pages are absolute: `](/assets/…)`. Relative `../assets/…` resolves to `/de/assets/…` and 404s.
- Never translate: code blocks, CSV/JSON column names and import field names (the Data Migration pages are file-format references), URLs, product names (Circuit Auction, ShipStation, HiBid, Pusher…), `{% hint %}` / `{% endhint %}` markers.
- German register: formal "Sie". UI labels in **bold** use the exact German string from the backoffice glossary when one exists, otherwise the English label as currently shown on screen.
- Tooling is stdlib-only Python 3 (`python3` on this machine has no pip), run from the repo root, tested with `unittest`.
- Commit after each task; nothing in this plan pushes.
- Out of scope (decisions to confirm with Brice): the IT section (`it-section/`, sysadmin audience) and `MAINTAINING_DOCS.md` / `running-docs-locally.md` stay English; German screenshots and German videos wait for the German UI translation to be completed in the backoffice (otherwise they would show a half-English UI).

## Review Focus

1. A translated page with a relative asset link (`../assets/screenshots/x.png`) shows a broken image under `/de/`. Pinned by `test_rewrite_asset_links` and the `broken-assets` check in `status.py` (Task 1).
2. A sidebar link in `de/_sidebar.md` that is relative resolves against the current sub-folder and 404s on nested pages. Pinned by `test_rewrite_sidebar_links` (Task 1): all links become `/de/…`.
3. A cross-page link with an anchor (`../sale/how-to-create-a-sale.md#bid-steps`) stops working once the target heading is translated, because docsify derives the id from the heading text. Pinned by the skill rule "re-slug anchors" (Task 3) and the manual check in Task 4 step 6.
4. A Data Migration page whose CSV column names got translated would make a customer's import fail. Pinned by the skill rule and the `grep` check in Task 7 step 4.
5. Switching language from a deep page via the navbar drops the reader to the language home. Pinned by the navbar plugin in Task 2 (links are rewritten to keep the current path) and its browser check (Task 2 step 7).

---

## File map

| File | Responsibility |
|------|----------------|
| `tools/i18n/common.py` | repo root, language-dir discovery, source-page listing, provenance header, link rewriting |
| `tools/i18n/scaffold.py` | create `<lang>/<page>` copies (with header, absolute asset links) and `<lang>/_sidebar.md` |
| `tools/i18n/status.py` | per-language report: current / outdated / untranslated / missing / orphan / broken-assets |
| `tools/i18n/glossary.py` | build `tools/i18n/glossary/<lang>.md` from the backoffice locale JSON |
| `tools/i18n/tests/test_*.py` | unit tests for the above |
| `.claude/skills/translate-docs/SKILL.md` | the translation rules an agent follows |
| `TRANSLATING_DOCS.md` | maintainer runbook: translate a page, refresh outdated pages, add a language (RTL / CJK / voices notes) |
| `index.html` | docsify config: `fallbackLanguages`, aliases, navbar, per-path labels, search namespaces, coverpages, `<html lang/dir>` plugin |
| `_navbar.md` | language switcher |
| `de/_sidebar.md`, `de/_coverpage.md`, `de/README.md`, `de/**/*.md` | German content |
| `assets/screenshots/de/*.png` | German UI captures (Task 9) |
| `circuitauction-backoffice/client/app/scripts/services/main.js` | `MainAppService.docsUrl(page)` |
| `circuitauction-backoffice/client/app/scripts/controllers/dashboard/documentation.js`, `app/views/documentation/main.html`, `controllers/dashboard/sale.js` | language-aware docs links |
| `circuitauction-backoffice/client/cypress/e2e-tutorials/release-3.5/_demo.js` | set the UI language from `tutorialLang` |

---

### Task 1: Translation tooling (`tools/i18n/`)

**Files:**
- Create: `tools/i18n/common.py`, `tools/i18n/scaffold.py`, `tools/i18n/status.py`, `tools/i18n/glossary.py`
- Create: `tools/i18n/tests/__init__.py` (empty, makes the tests importable as `tests.*`), `tools/i18n/tests/test_common.py`, `tools/i18n/tests/test_scaffold.py`, `tools/i18n/tests/test_status.py`, `tools/i18n/tests/test_glossary.py`

**Interfaces:**
- Consumes: nothing.
- Produces: `common.source_pages(root) -> list[str]`, `common.lang_dirs(root) -> list[str]`, `common.sha_of(path) -> str`, `common.make_header(source, sha) -> str`, `common.parse_header(text) -> tuple[str, str] | None`, `common.rewrite_asset_links(text) -> str`, `common.rewrite_sidebar_links(text, lang) -> str`, `scaffold.scaffold_page(root, lang, page) -> Path | None`, `scaffold.scaffold_sidebar(root, lang) -> Path | None`, `status.status(root, lang) -> dict[str, list[str]]`, `glossary.glossary_pairs(en, tr) -> list[tuple[str, str]]`. CLI: `python3 tools/i18n/scaffold.py --lang de [--all | --sidebar | page …]`, `python3 tools/i18n/status.py --lang de [--json] [--fail-on orphan,broken-assets]`, `python3 tools/i18n/glossary.py --lang de`.

- [ ] **Step 1: Write the failing tests for `common`**

Create the empty `tools/i18n/tests/__init__.py` (`: > tools/i18n/tests/__init__.py`), then `tools/i18n/tests/test_common.py`:

```python
import tempfile, unittest
from pathlib import Path

import common


def make_repo(tmp: Path):
    (tmp / "client").mkdir()
    (tmp / "README.md").write_text("# Intro\n")
    (tmp / "_sidebar.md").write_text("* [Intro](README.md)\n* [Clients](client/README.md)\n")
    (tmp / "client" / "README.md").write_text("![](../assets/screenshots/a.png)\n")
    (tmp / "de").mkdir()
    (tmp / "de" / "README.md").write_text("# Einleitung\n")
    (tmp / "node_modules").mkdir()
    (tmp / "node_modules" / "x.md").write_text("junk\n")
    (tmp / "assets").mkdir()
    (tmp / "assets" / "note.md").write_text("junk\n")


class CommonTests(unittest.TestCase):
    def setUp(self):
        self.tmp = Path(tempfile.mkdtemp())
        make_repo(self.tmp)

    def test_lang_dirs_finds_only_language_folders(self):
        self.assertEqual(common.lang_dirs(self.tmp), ["de"])

    def test_source_pages_skips_lang_dirs_non_content_and_vendor(self):
        self.assertEqual(common.source_pages(self.tmp), ["README.md", "client/README.md"])

    def test_header_roundtrip(self):
        h = common.make_header("client/README.md", "0123456789ab")
        self.assertEqual(common.parse_header(h + "\n# x"), ("client/README.md", "0123456789ab"))
        self.assertIsNone(common.parse_header("# no header"))

    def test_sha_is_12_hex(self):
        self.assertRegex(common.sha_of(self.tmp / "README.md"), r"^[0-9a-f]{12}$")

    def test_rewrite_asset_links(self):
        text = "![](../assets/a.png) ![](assets/b.png) ![](../../assets/c.png) [x](/assets/d.png)"
        self.assertEqual(
            common.rewrite_asset_links(text),
            "![](/assets/a.png) ![](/assets/b.png) ![](/assets/c.png) [x](/assets/d.png)",
        )

    def test_rewrite_sidebar_links(self):
        text = "* [Intro](README.md)\n* [Clients](client/README.md)\n* [Site](https://x.y/z.md)\n* [Abs](/de/x.md)"
        self.assertEqual(
            common.rewrite_sidebar_links(text, "de"),
            "* [Intro](/de/README.md)\n* [Clients](/de/client/README.md)\n* [Site](https://x.y/z.md)\n* [Abs](/de/x.md)",
        )


if __name__ == "__main__":
    unittest.main()
```

- [ ] **Step 2: Run the tests to verify they fail**

Run: `cd /media/bl/Disk2/htdocs/circuitauction-docs && python3 -m unittest discover -s tools/i18n/tests -t tools/i18n -v`
Expected: `ModuleNotFoundError: No module named 'common'`

- [ ] **Step 3: Implement `tools/i18n/common.py`**

```python
"""Shared helpers for the docs translation tooling (Python 3 stdlib only).

Layout: English pages at the repo root, one mirror folder per language
(`de/client/x.md` <-> `client/x.md`). A translated page starts with
`<!-- i18n source=<path> sha=<12 hex> -->` so we can tell when its source changed.
"""
from __future__ import annotations

import hashlib
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
LANG_RE = re.compile(r"^[a-z]{2}(-[a-z]+)?$")
SKIP_DIRS = {"node_modules", ".git", ".remember", ".claude", "docs", "tools", "assets"}
NON_CONTENT = {"_sidebar.md", "_coverpage.md", "_navbar.md", "SUMMARY.md",
               "MAINTAINING_DOCS.md", "TRANSLATING_DOCS.md"}
HEADER_RE = re.compile(r"<!--\s*i18n\s+source=(?P<source>\S+)\s+sha=(?P<sha>[0-9a-f]{12})\s*-->")
ASSET_LINK_RE = re.compile(r"\]\((?:\.\./)*assets/")
RELATIVE_ASSET_RE = re.compile(r"\]\((?:\.\./)*assets/|src=[\"'](?:\.\./)*assets/")
SIDEBAR_LINK_RE = re.compile(r"\]\((?!https?://|/|#)([^)]+\.md)\)")


def is_lang_dir(p: Path) -> bool:
    return p.is_dir() and bool(LANG_RE.match(p.name)) and (p / "README.md").exists()


def lang_dirs(root: Path = ROOT) -> list[str]:
    return sorted(p.name for p in root.iterdir() if is_lang_dir(p))


def source_pages(root: Path = ROOT) -> list[str]:
    """English content pages, as posix paths relative to the repo root."""
    langs = set(lang_dirs(root))
    pages = []
    for p in root.rglob("*.md"):
        rel = p.relative_to(root)
        if rel.parts[0] in SKIP_DIRS or rel.parts[0] in langs or rel.name in NON_CONTENT:
            continue
        pages.append(rel.as_posix())
    return sorted(pages)


def sha_of(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()[:12]


def make_header(source: str, sha: str) -> str:
    return f"<!-- i18n source={source} sha={sha} -->"


def parse_header(text: str) -> tuple[str, str] | None:
    m = HEADER_RE.search(text)
    return (m.group("source"), m.group("sha")) if m else None


def rewrite_asset_links(text: str) -> str:
    """`](../assets/x)` / `](assets/x)` -> `](/assets/x)` so links work from any language folder."""
    return ASSET_LINK_RE.sub("](/assets/", text)


def has_relative_asset_links(text: str) -> bool:
    return bool(RELATIVE_ASSET_RE.search(text))


def rewrite_sidebar_links(text: str, lang: str) -> str:
    """Make every relative `.md` link in a sidebar absolute under /<lang>/."""
    return SIDEBAR_LINK_RE.sub(lambda m: f"](/{lang}/{m.group(1)})", text)
```

- [ ] **Step 4: Run the `common` tests to verify they pass**

Run: `python3 -m unittest discover -s tools/i18n/tests -t tools/i18n -v`
Expected: 6 tests, `OK`

- [ ] **Step 5: Write the failing tests for `scaffold`**

`tools/i18n/tests/test_scaffold.py`:

```python
import tempfile, unittest
from pathlib import Path

import common, scaffold
from tests.test_common import make_repo


class ScaffoldTests(unittest.TestCase):
    def setUp(self):
        self.tmp = Path(tempfile.mkdtemp())
        make_repo(self.tmp)

    def test_scaffold_page_writes_header_and_absolute_assets(self):
        dst = scaffold.scaffold_page(self.tmp, "de", "client/README.md")
        self.assertEqual(dst, self.tmp / "de" / "client" / "README.md")
        text = dst.read_text()
        self.assertEqual(common.parse_header(text),
                         ("client/README.md", common.sha_of(self.tmp / "client" / "README.md")))
        self.assertIn("![](/assets/screenshots/a.png)", text)

    def test_scaffold_page_never_overwrites(self):
        scaffold.scaffold_page(self.tmp, "de", "client/README.md")
        (self.tmp / "de" / "client" / "README.md").write_text("translated")
        self.assertIsNone(scaffold.scaffold_page(self.tmp, "de", "client/README.md"))
        self.assertEqual((self.tmp / "de" / "client" / "README.md").read_text(), "translated")

    def test_scaffold_sidebar_rewrites_links(self):
        dst = scaffold.scaffold_sidebar(self.tmp, "de")
        self.assertEqual(dst.read_text(), "* [Intro](/de/README.md)\n* [Clients](/de/client/README.md)\n")
        self.assertIsNone(scaffold.scaffold_sidebar(self.tmp, "de"))


if __name__ == "__main__":
    unittest.main()
```

- [ ] **Step 6: Run to verify failure**

Run: `python3 -m unittest discover -s tools/i18n/tests -t tools/i18n -v`
Expected: `ModuleNotFoundError: No module named 'scaffold'`

- [ ] **Step 7: Implement `tools/i18n/scaffold.py`**

```python
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
```

- [ ] **Step 8: Run to verify pass**

Run: `python3 -m unittest discover -s tools/i18n/tests -t tools/i18n -v`
Expected: 9 tests, `OK`

- [ ] **Step 9: Write the failing tests for `status`**

`tools/i18n/tests/test_status.py`:

```python
import tempfile, unittest
from pathlib import Path

import scaffold, status
from tests.test_common import make_repo


class StatusTests(unittest.TestCase):
    def setUp(self):
        self.tmp = Path(tempfile.mkdtemp())
        make_repo(self.tmp)
        (self.tmp / "sale").mkdir()
        (self.tmp / "sale" / "x.md").write_text("# Sale\n")

    def test_categories(self):
        scaffold.scaffold_page(self.tmp, "de", "client/README.md")           # untranslated copy
        p = scaffold.scaffold_page(self.tmp, "de", "sale/x.md")
        p.write_text(p.read_text().replace("# Sale", "# Verkauf"))           # translated, current
        (self.tmp / "sale" / "x.md").write_text("# Sale (edited)\n")         # ... now outdated
        (self.tmp / "de" / "orphan.md").write_text("<!-- i18n source=gone.md sha=000000000000 -->\n")
        (self.tmp / "de" / "README.md").write_text("<!-- i18n source=README.md sha=000000000000 -->\n![](../assets/a.png)\n")
        r = status.status(self.tmp, "de")
        self.assertEqual(r["untranslated"], ["client/README.md"])
        self.assertEqual(r["outdated"], ["README.md", "sale/x.md"])
        self.assertEqual(r["missing"], [])
        self.assertEqual(r["orphan"], ["de/orphan.md"])
        self.assertEqual(r["broken-assets"], ["README.md"])
        self.assertEqual(r["current"], [])

    def test_missing_and_no_header_is_outdated(self):
        (self.tmp / "de" / "README.md").write_text("# Einleitung\n")
        r = status.status(self.tmp, "de")
        self.assertEqual(r["missing"], ["client/README.md", "sale/x.md"])
        self.assertEqual(r["outdated"], ["README.md"])


if __name__ == "__main__":
    unittest.main()
```

- [ ] **Step 10: Run to verify failure**

Run: `python3 -m unittest discover -s tools/i18n/tests -t tools/i18n -v`
Expected: `ModuleNotFoundError: No module named 'status'`

- [ ] **Step 11: Implement `tools/i18n/status.py`**

```python
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
  broken-assets (extra flag) page still has relative ../assets links
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

from common import (ROOT, has_relative_asset_links, parse_header, rewrite_asset_links,
                    sha_of, source_pages)

CATEGORIES = ["current", "outdated", "untranslated", "missing", "orphan", "broken-assets"]


def status(root: Path, lang: str) -> dict[str, list[str]]:
    res: dict[str, list[str]] = {c: [] for c in CATEGORIES}
    sources = source_pages(root)
    for page in sources:
        src, dst = root / page, root / lang / page
        if not dst.exists():
            res["missing"].append(page)
            continue
        text = dst.read_text(encoding="utf-8")
        if has_relative_asset_links(text):
            res["broken-assets"].append(page)
        header = parse_header(text)
        if header is None or header[1] != sha_of(src):
            res["outdated"].append(page)
            continue
        body = text.split("\n", 1)[1] if "\n" in text else ""
        if body == rewrite_asset_links(src.read_text(encoding="utf-8")):
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
        total = len(source_pages(ROOT))
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
```

- [ ] **Step 12: Run to verify pass**

Run: `python3 -m unittest discover -s tools/i18n/tests -t tools/i18n -v`
Expected: 11 tests, `OK`

- [ ] **Step 13: Write the failing tests for `glossary`**

`tools/i18n/tests/test_glossary.py`:

```python
import unittest

import glossary


class GlossaryTests(unittest.TestCase):
    def test_pairs_skip_identical_placeholders_and_long_strings(self):
        en = {"GENERAL": {"CLIENTS": "Clients", "SAVE": "Save", "HELLO": "Hello {{name}}",
                          "LONG": "x" * 61},
              "SALES": {"TITLE": "Sales", "CLIENTS": "Clients"}}
        de = {"GENERAL": {"CLIENTS": "Kunden", "SAVE": "Save", "HELLO": "Hallo {{name}}",
                          "LONG": "y" * 61},
              "SALES": {"TITLE": "Auktionen", "CLIENTS": "Klienten"}}
        self.assertEqual(glossary.glossary_pairs(en, de),
                         [("Clients", "Kunden"), ("Sales", "Auktionen")])

    def test_render_is_a_markdown_table(self):
        out = glossary.render([("Clients", "Kunden")], "de")
        self.assertIn("| English | de |", out)
        self.assertIn("| Clients | Kunden |", out)


if __name__ == "__main__":
    unittest.main()
```

- [ ] **Step 14: Run to verify failure**

Run: `python3 -m unittest discover -s tools/i18n/tests -t tools/i18n -v`
Expected: `ModuleNotFoundError: No module named 'glossary'`

- [ ] **Step 15: Implement `tools/i18n/glossary.py`**

```python
"""Build tools/i18n/glossary/<lang>.md (English UI label -> translated UI label) from the
backoffice locale files, so the docs use exactly the words the app shows.

  python3 tools/i18n/glossary.py --lang de
  python3 tools/i18n/glossary.py --lang de --locale-dir /path/to/client/app/i18n

Strings identical to English (= not translated yet in the app), strings with {{placeholders}}
and strings longer than 60 chars (sentences) are skipped. When the same English label has
several translations, the first key in locale-en.json order wins; the agent picks by context.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

from common import ROOT

DEFAULT_LOCALE_DIR = ROOT.parent / "circuitauction-backoffice" / "client" / "app" / "i18n"
MAX_LEN = 60


def flatten(obj: dict, prefix: str = "") -> dict[str, object]:
    out: dict[str, object] = {}
    for k, v in obj.items():
        if isinstance(v, dict):
            out.update(flatten(v, f"{prefix}{k}."))
        else:
            out[f"{prefix}{k}"] = v
    return out


def glossary_pairs(en: dict, tr: dict) -> list[tuple[str, str]]:
    fe, ft = flatten(en), flatten(tr)
    pairs: dict[str, str] = {}
    for key, src in fe.items():
        dst = ft.get(key)
        if not isinstance(src, str) or not isinstance(dst, str):
            continue
        src, dst = src.strip(), dst.strip()
        if not src or src == dst or "{{" in src or len(src) > MAX_LEN:
            continue
        pairs.setdefault(src, dst)
    return sorted(pairs.items(), key=lambda kv: kv[0].lower())


def render(pairs: list[tuple[str, str]], lang: str) -> str:
    lines = [f"# UI glossary ({lang})", "",
             "Generated by `python3 tools/i18n/glossary.py --lang " + lang + "` from the backoffice",
             "`locale-en.json` / `locale-" + lang + ".json`. Do not edit by hand.", "",
             f"| English | {lang} |", "|---|---|"]
    lines += [f"| {e.replace('|', '/')} | {t.replace('|', '/')} |" for e, t in pairs]
    return "\n".join(lines) + "\n"


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--lang", required=True)
    ap.add_argument("--locale-dir", type=Path, default=DEFAULT_LOCALE_DIR)
    ap.add_argument("--out", type=Path, default=None)
    a = ap.parse_args(argv)
    en = json.loads((a.locale_dir / "locale-en.json").read_text(encoding="utf-8"))
    tr = json.loads((a.locale_dir / f"locale-{a.lang}.json").read_text(encoding="utf-8"))
    pairs = glossary_pairs(en, tr)
    out = a.out or ROOT / "tools" / "i18n" / "glossary" / f"{a.lang}.md"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(render(pairs, a.lang), encoding="utf-8")
    print(f"wrote {out} ({len(pairs)} terms)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
```

- [ ] **Step 16: Run to verify pass**

Run: `python3 -m unittest discover -s tools/i18n/tests -t tools/i18n -v`
Expected: 13 tests, `OK`

- [ ] **Step 17: Smoke-run the CLIs against the real repo**

Run:
```bash
python3 tools/i18n/status.py --lang de
python3 tools/i18n/glossary.py --lang de && head -20 tools/i18n/glossary/de.md
```
Expected: status prints `de: 0/… current … missing` (no `de/` folder yet, so every page is missing); glossary writes several hundred terms, e.g. `| Clients | Kunden |`.

- [ ] **Step 18: Commit**

```bash
git add tools/i18n
git commit -m "Add docs translation tooling (scaffold, status, glossary)

Co-Authored-By: Claude Fable 5.1 <noreply@anthropic.com>"
```

---

### Task 2: Docsify multi-language scaffolding

**Files:**
- Modify: `index.html` (the `window.$docsify = {…}` block and the `plugins` array)
- Create: `_navbar.md`, `de/_sidebar.md`, `de/_coverpage.md`, `de/README.md`

**Interfaces:**
- Consumes: `python3 tools/i18n/scaffold.py` from Task 1.
- Produces: the `LANGS` list in `index.html` (`['de']`) that every later language extends, the `/de/` route with sidebar, cover page and fallback.

- [ ] **Step 1: Scaffold the German sidebar and home page**

Run:
```bash
python3 tools/i18n/scaffold.py --lang de --sidebar README.md
```
Expected: `created de/_sidebar.md`, `created de/README.md`.

- [ ] **Step 2: Translate the sidebar titles in `de/_sidebar.md`**

Only the link texts change; the targets stay `/de/…`. Use the glossary for section names (`Kunden`, `Objekte`, `Auktion`, …). Keep the `<!-- docs/_sidebar.md -->` comment. Example of the first block:

```markdown
* [Einführung](/de/README.md)
* [Anmeldung im System](/de/logging-into-the-system.md)
* [Anmeldung mit einer Authenticator-App](/de/logging-in-with-an-authenticator-app.md)
* [Zugang zu Ihrer Demo](/de/accessing-your-demo.md)
* [Empfohlener Arbeitsablauf](/de/workflow-best-practice.md)

* **Kunden**
  * [Übersicht](/de/client/README.md)
```

- [ ] **Step 3: Translate `de/README.md` and create `de/_coverpage.md`**

`de/README.md` keeps its provenance header line and gets the German text of `README.md` (links inside stay relative, e.g. `client/README.md`, which resolves to `/de/client/README.md`).

`de/_coverpage.md`:
```markdown
<!-- de/_coverpage.md -->

# CircuitAuction Dokumentation

> Hilfe-Dokumentation für das Backoffice

- Vollständiges Benutzerhandbuch für die Auktionsverwaltung
- Objekte, Kunden, Einlieferungen und Auktionen
- IT-Bereich mit technischer Dokumentation (Englisch)

[Los geht's](/de/README.md)
[GitHub](https://github.com/Gizra/circuitauction-docs/)

<!-- background color -->
![color](#f0f0f0)
```

- [ ] **Step 4: Create `_navbar.md`**

```markdown
<!-- _navbar.md : language switcher; the i18n plugin in index.html keeps the current page -->

* [English](/)
* [Deutsch](/de/)
```

- [ ] **Step 5: Update `index.html`**

Replace the `coverpage`, `alias`, `search`, `pagination` and `copyCode` entries and add the i18n keys so the config reads:

```js
    // Languages published besides English (folder name = ISO code used by the backoffice).
    var LANGS = ['de'];

    window.$docsify = {
      name: 'CircuitAuction Docs',
      nameLink: { '/de/': '#/de/', '/': '#/' },
      repo: 'https://github.com/Gizra/circuitauction-docs',
      loadSidebar: true,
      loadNavbar: true,
      coverpage: ['/', '/de/'],
      autoHeader: true,
      subMaxLevel: 3,
      maxLevel: 4,
      homepage: 'README.md',

      // Serve the English page when a translated one does not exist (yet).
      fallbackLanguages: LANGS,

      // Order matters: the language rule must come before the generic one,
      // otherwise /de/_sidebar.md is aliased to the English sidebar.
      alias: {
        '/de/(.*/)?_sidebar.md': '/de/_sidebar.md',
        '/.*/_sidebar.md': '/_sidebar.md',
        '/.*/_navbar.md': '/_navbar.md'
      },

      search: {
        maxAge: 86400000,
        paths: 'auto',
        pathNamespaces: LANGS.map(function (l) { return '/' + l; }),
        placeholder: { '/de/': 'Suchen...', '/': 'Search...' },
        noData: { '/de/': 'Keine Ergebnisse', '/': 'No Results!' },
        depth: 6,
        hideOtherSidebarContent: false
      },

      pagination: {
        previousText: { '/de/': 'Zurück', '/': 'Previous' },
        nextText: { '/de/': 'Weiter', '/': 'Next' },
        crossChapter: true,
        crossChapterText: true,
      },

      copyCode: {
        buttonText: { '/de/': 'Kopieren', '/': 'Copy' },
        errorText: { '/de/': 'Fehler', '/': 'Error' },
        successText: { '/de/': 'Kopiert', '/': 'Copied' }
      },
```

and append this plugin to the `plugins` array (after the hint plugin):

```js
        // i18n: <html lang/dir> follows the route, and the navbar language links
        // keep the current page instead of jumping to the language home.
        function (hook, vm) {
          var RTL = ['he'];
          function langOf(path) {
            var m = path.match(/^\/([a-z]{2}(?:-[a-z]+)?)(?:\/|$)/);
            return m && LANGS.indexOf(m[1]) !== -1 ? m[1] : '';
          }
          hook.doneEach(function () {
            var path = vm.route.path || '/';
            var cur = langOf(path);
            var rest = cur ? path.slice(cur.length + 1) || '/' : path;
            document.documentElement.lang = cur || 'en';
            document.documentElement.dir = RTL.indexOf(cur) !== -1 ? 'rtl' : 'ltr';
            document.querySelectorAll('.app-nav a').forEach(function (a) {
              var m = (a.getAttribute('href') || '').match(/^#\/([a-z]{2}(?:-[a-z]+)?)?\/?$/);
              if (!m) return;
              var target = m[1] || '';
              if (target && LANGS.indexOf(target) === -1) return;
              a.setAttribute('href', '#' + (target ? '/' + target : '') + rest);
            });
          });
        }
```

- [ ] **Step 6: Serve locally**

Run: `npx -y docsify-cli serve . -p 3005` (keep it running in the background).

- [ ] **Step 7: Verify in the browser (Claude-in-Chrome or manually)**

| URL | Expected |
|-----|----------|
| `http://localhost:3005/#/de/` | German cover page, German sidebar, German README |
| `http://localhost:3005/#/de/client/how-to-create-a-client` | **English** page body (fallback) with the **German** sidebar; the sidebar entry is highlighted |
| navbar "English" while on the page above | goes to `#/client/how-to-create-a-client` (same page, not the home) |
| navbar "Deutsch" from `#/sale/README` | goes to `#/de/sale/README` |
| search "Kunden" on `/#/de/` | results only from `/de/` pages; placeholder reads "Suchen..." |
| bottom of a German page | pagination labels "Zurück" / "Weiter" |
| `document.documentElement.lang` in the console on `/#/de/` | `"de"` |

- [ ] **Step 8: Commit**

```bash
git add index.html _navbar.md de/_sidebar.md de/_coverpage.md de/README.md
git commit -m "Add German (de) language scaffolding to the docs site

Co-Authored-By: Claude Fable 5.1 <noreply@anthropic.com>"
```

---

### Task 3: Translation skill and maintainer runbook

**Files:**
- Create: `.claude/skills/translate-docs/SKILL.md`
- Create: `TRANSLATING_DOCS.md`
- Create (generated): `tools/i18n/glossary/de.md`

**Interfaces:**
- Consumes: `tools/i18n/*.py` CLIs (Task 1), `LANGS` in `index.html` (Task 2).
- Produces: the rules every content task (4–7) follows; the "Adding a language" checklist used for fr/he/nl/ru/zh-hans.

- [ ] **Step 1: Generate the German glossary and skim it**

Run: `python3 tools/i18n/glossary.py --lang de && grep -c '^|' tools/i18n/glossary/de.md`
Expected: a few hundred rows. Spot-check `Clients`, `Items`, `Consignments`, `Sales`, `Bids`, `Tasks`, `Save`.

- [ ] **Step 2: Write `.claude/skills/translate-docs/SKILL.md`**

```markdown
---
name: translate-docs
description: Translate a CircuitAuction docs page (docsify markdown) into a language folder such as de/, following the glossary and the i18n provenance rules. Use when asked to translate, update or review a translated docs page.
---

# Translate a docs page

## Workflow
1. `python3 tools/i18n/status.py --lang <lang>` – pick pages that are `missing`, `untranslated` or `outdated`.
2. Missing page: `python3 tools/i18n/scaffold.py --lang <lang> <page>`; it creates `<lang>/<page>` with the
   provenance header and the English text (asset links already absolute).
3. Outdated page: read the English source, diff against what the translation describes, update the
   translation, then refresh the header: replace the `sha=` value with the output of
   `python3 -c "import sys; sys.path.insert(0,'tools/i18n'); import common, pathlib; print(common.sha_of(pathlib.Path('<page>')))"`.
4. Translate in place. Re-run `status.py` – the page must now be `current`.
5. Serve (`npx -y docsify-cli serve . -p 3005`) and open the page under `/#/<lang>/…` once.

## Rules
- Line 1 stays the `<!-- i18n source=… sha=… -->` comment. Never translate or move it.
- Keep the markdown structure exactly: heading levels, list nesting, tables, `{% hint style="…" %}` /
  `{% endhint %}` on their own lines, blank lines, image lines.
- Do not translate: fenced code blocks, inline code, URLs, file names, CSV/JSON column names and import
  field names (Data Migration pages describe file formats), product and company names
  (Circuit Auction, ShipStation, HiBid, Pusher, Authorize.net, WordPress, Delcampe, PhilaSearch, SAN,
  Auction Mobility, EasyPost), bidder-number formats and examples such as `#2001`.
- UI labels (text the reader must find on screen, usually **bold** or in `backticks` in the source):
  look the English label up in `tools/i18n/glossary/<lang>.md`. If it is there, use that translation
  verbatim. If it is not, the app still shows the English label: keep it in English.
- German: formal "Sie". Nouns per the glossary (Kunde, Objekt, Einlieferung, Auktion, Gebot, Aufgabe,
  Rechnung, Zuschlag). Keep English words that the glossary keeps.
- Links: keep relative targets unchanged (`../sale/how-to-create-a-sale.md` resolves inside the language
  folder; docsify falls back to English when the target is not translated). If a link has an anchor
  (`…md#bid-steps`) and the target page is already translated, replace the anchor with the slug of the
  translated heading (lower-case, spaces to `-`, punctuation removed).
- Images: `](/assets/…)` absolute. If a localized capture exists at `/assets/screenshots/<lang>/<name>.png`,
  use it; otherwise keep the English one. Translate alt texts.
- Release notes: keep version numbers, dates and `<video class="release-video" …>` lines. Use the `-<lang>`
  video URL (`…/release-3.5-<name>-<lang>/final.mp4`) only when that render exists in S3 (check with
  `curl -sI <url> | head -1` → `200`); otherwise keep the English URL.
- Never leave English paragraphs behind except the untranslatable items above; `status.py` cannot
  detect a half-translated page.
```

- [ ] **Step 3: Write `TRANSLATING_DOCS.md`**

```markdown
# Translating These Docs

Maintainer runbook, companion to `MAINTAINING_DOCS.md`. Not in the sidebar.

## How it works
- English lives at the repo root and keeps its URLs. Each language is a mirror folder (`de/…`).
- `index.html` lists the published languages in `LANGS` and tells docsify to fall back to English
  for pages that are not translated (`fallbackLanguages`), so a partial translation is always safe to ship.
- Every translated page starts with `<!-- i18n source=<path> sha=<12 hex> -->`. The sha is the English
  file's content hash at translation time; `tools/i18n/status.py` uses it to flag outdated pages.

## Daily use
| Need | Command |
|------|---------|
| What is left / outdated for German | `python3 tools/i18n/status.py --lang de` |
| Create the German copy of a page | `python3 tools/i18n/scaffold.py --lang de client/README.md` |
| Refresh the UI glossary after backoffice locale changes | `python3 tools/i18n/glossary.py --lang de` |
| Translate / refresh pages with Claude Code | `/translate-docs` (skill in `.claude/skills/translate-docs`) |
| Run the tooling tests | `python3 -m unittest discover -s tools/i18n/tests -t tools/i18n` |

After editing an English page, run `status.py` and refresh the pages it lists as `outdated` before
publishing, or leave them: readers still get the (older) translation.

## Adding a language (checklist)
1. The backoffice must have `locale-<lang>.json` (currently `de, fr, he, nl, ru, zh-hans`). Generate the
   glossary: `python3 tools/i18n/glossary.py --lang <lang>`.
2. `index.html`: add the code to `LANGS`; add `'/<lang>/(.*/)?_sidebar.md': '/<lang>/_sidebar.md'` to
   `alias` **above** the generic rule; add `'/<lang>/'` to `coverpage`; add `'/<lang>/'` entries to
   `search.placeholder`, `search.noData`, `pagination.previousText/nextText`, `copyCode.*`, `nameLink`.
3. `_navbar.md`: add `* [<Native name>](/<lang>/)`.
4. `python3 tools/i18n/scaffold.py --lang <lang> --sidebar README.md`, translate `<lang>/_sidebar.md`,
   `<lang>/README.md`, create `<lang>/_coverpage.md` (copy `de/_coverpage.md`).
5. Translate pages with the skill, in the same order as the German plan (home + release notes, then
   Clients / Items / Sale / Consignment, then Bids / Auction, then Website / Data Migration).
6. Videos: `get_tutorial_text` → `save_tutorial_translation` → `author_tutorial(lang)` →
   `render_tutorial(lang, project_id="release-3.5-<name>-<lang>")`. ElevenLabs needs a voice for the
   language in `ELEVENLABS_VOICE_IDS` (OpenMontage `.env`); today only `de,en` are configured.
7. Screenshots: see `MAINTAINING_DOCS.md` §5 and set `localStorage['ls.language']` to the code in the
   capture init script; save under `assets/screenshots/<lang>/` with the same file names.
8. Backoffice: add the code to `DOCS_LANGUAGES` in `MainAppService.docsUrl` so the embedded help opens
   in that language.

Language-specific notes:
- `he` (Hebrew, RTL): the i18n plugin already sets `<html dir="rtl">` for `he`; add CSS for
  `[dir=rtl] .sidebar`, `.content`, `.app-nav` margins (docsify's vue theme is LTR-only) before publishing.
- `zh-hans`: docsify's search tokenizes on characters, so searching works; keep headings short.
- `ru`, `fr`, `nl`: nothing special.
```

- [ ] **Step 4: Commit**

```bash
git add .claude/skills/translate-docs/SKILL.md TRANSLATING_DOCS.md tools/i18n/glossary/de.md
git commit -m "Add translate-docs skill, German glossary and translation runbook

Co-Authored-By: Claude Fable 5.1 <noreply@anthropic.com>"
```

---

### Task 4: Translate the entry pages and the release notes (≈7,000 words)

**Files:**
- Create: `de/logging-into-the-system.md`, `de/logging-in-with-an-authenticator-app.md`, `de/accessing-your-demo.md`, `de/workflow-best-practice.md`, `de/tasks.md`, `de/glossary.md`, `de/understanding-automatic-tags.md`, `de/import-migrate.md`, `de/release-notes/README.md`, `de/release-notes/version-3.5.md`, `de/release-notes/version-3.4.md`, `de/release-notes/version-3.3.md`, `de/release-notes/version-3.1.md`

**Interfaces:**
- Consumes: the `translate-docs` skill (Task 3).
- Produces: `current` status for the pages above.

- [ ] **Step 1: Scaffold**

Run:
```bash
python3 tools/i18n/scaffold.py --lang de logging-into-the-system.md logging-in-with-an-authenticator-app.md accessing-your-demo.md workflow-best-practice.md tasks.md glossary.md understanding-automatic-tags.md import-migrate.md release-notes/README.md release-notes/version-3.5.md release-notes/version-3.4.md release-notes/version-3.3.md release-notes/version-3.1.md
python3 tools/i18n/status.py --lang de | grep -c untranslated
```
Expected: `13` (plus `de/README.md` is already current from Task 2).

- [ ] **Step 2: Translate each file in place with the `translate-docs` skill**

Order: `release-notes/version-3.5.md` first (it is what customers get linked to), then the rest. The release notes keep the 16 `<video class="release-video" …>` lines with the **English** URLs for now (Task 8 switches them).

- [ ] **Step 3: Verify status**

Run: `python3 tools/i18n/status.py --lang de`
Expected: the 13 pages (and README.md) are no longer listed under `untranslated` / `outdated` / `broken-assets`; the count line shows `14/… current`.

- [ ] **Step 4: Verify no untranslated paragraph slipped through**

Run: `grep -nE '^(The|This|Click|Select|You can|When) ' de/*.md de/release-notes/*.md | grep -v '^de/[^:]*:1:' | head`
Expected: no output (sentences starting with these English words are the usual sign of a skipped paragraph).

- [ ] **Step 5: Verify the pages render**

With `npx -y docsify-cli serve . -p 3005` running, open `http://localhost:3005/#/de/release-notes/version-3.5` and `http://localhost:3005/#/de/glossary`: German text, videos play, hint boxes styled, screenshots visible.

- [ ] **Step 6: Verify anchors**

Run: `grep -noE '\]\([^)]*\.md#[^)]*\)' de/*.md de/release-notes/*.md`
For each hit, open the link in the browser and confirm it scrolls to the right heading; fix the slug if not.

- [ ] **Step 7: Commit**

```bash
git add de
git commit -m "German: entry pages and release notes

Co-Authored-By: Claude Fable 5.1 <noreply@anthropic.com>"
```

---

### Task 5: Translate Clients, Items, Sale and Consignment (≈4,900 words, 31 pages)

**Files:**
- Create: `de/client/*.md` (10), `de/items/*.md` (4), `de/sale/*.md` (7), `de/consignment/*.md` (10)

**Interfaces:**
- Consumes: the `translate-docs` skill (Task 3).
- Produces: `current` status for the four folders.

- [ ] **Step 1: Scaffold**

Run: `python3 tools/i18n/scaffold.py --lang de $(python3 tools/i18n/status.py --lang de --json | python3 -c "import json,sys; print(' '.join(p for p in json.load(sys.stdin)['missing'] if p.split('/')[0] in ('client','items','sale','consignment')))")`
Expected: 31 `created` lines.

- [ ] **Step 2: Translate each file with the `translate-docs` skill**

Work folder by folder, `README.md` of each folder first so its terminology sets the tone for the how-tos.

- [ ] **Step 3: Verify status**

Run: `python3 tools/i18n/status.py --lang de`
Expected: nothing from `client/`, `items/`, `sale/`, `consignment/` under `untranslated`, `outdated` or `broken-assets`.

- [ ] **Step 4: Verify no untranslated paragraph slipped through**

Run: `grep -rnE '^(The|This|Click|Select|You can|When) ' de/client de/items de/sale de/consignment | head`
Expected: no output.

- [ ] **Step 5: Verify in the browser**

Open `http://localhost:3005/#/de/client/understanding-client-page` and `http://localhost:3005/#/de/consignment/consignment-workflow`: German text, images load, the sidebar highlights the page, "Zurück"/"Weiter" link to the neighbouring German pages.

- [ ] **Step 6: Commit**

```bash
git add de/client de/items de/sale de/consignment
git commit -m "German: clients, items, sale and consignment sections

Co-Authored-By: Claude Fable 5.1 <noreply@anthropic.com>"
```

---

### Task 6: Translate Bids and Auction (≈2,000 words, 13 pages)

**Files:**
- Create: `de/bids/*.md` (6), `de/auction/*.md` and `de/auction/clerk-screen/*.md` (7)

**Interfaces:**
- Consumes: the `translate-docs` skill (Task 3).
- Produces: `current` status for both folders.

- [ ] **Step 1: Scaffold**

Run: `python3 tools/i18n/scaffold.py --lang de $(python3 tools/i18n/status.py --lang de --json | python3 -c "import json,sys; print(' '.join(p for p in json.load(sys.stdin)['missing'] if p.split('/')[0] in ('bids','auction')))")`
Expected: 13 `created` lines.

- [ ] **Step 2: Translate each file with the `translate-docs` skill**

The clerk-screen pages contain the keyboard table (Space / arrows); keep key names as in the English page, translate the action column.

- [ ] **Step 3: Verify status and leftovers**

Run:
```bash
python3 tools/i18n/status.py --lang de
grep -rnE '^(The|This|Click|Select|You can|When) ' de/bids de/auction | head
```
Expected: nothing from `bids/` or `auction/` in the status lists; no grep output.

- [ ] **Step 4: Verify in the browser**

Open `http://localhost:3005/#/de/auction/auction-flow`: the four-state screenshot matrix renders, German captions.

- [ ] **Step 5: Commit**

```bash
git add de/bids de/auction
git commit -m "German: bids and auction sections

Co-Authored-By: Claude Fable 5.1 <noreply@anthropic.com>"
```

---

### Task 7: Translate Website and Data Migration (≈15,600 words, 45 pages)

**Files:**
- Create: `de/website/**/*.md` (22), `de/data-migration/*.md` (23)

**Interfaces:**
- Consumes: the `translate-docs` skill (Task 3).
- Produces: `current` status for both folders; after this task only `it-section/`, `MAINTAINING_DOCS.md` and `running-docs-locally.md` remain `missing` (by decision).

- [ ] **Step 1: Scaffold**

Run: `python3 tools/i18n/scaffold.py --lang de $(python3 tools/i18n/status.py --lang de --json | python3 -c "import json,sys; print(' '.join(p for p in json.load(sys.stdin)['missing'] if p.split('/')[0] in ('website','data-migration')))")`
Expected: 45 `created` lines.

- [ ] **Step 2: Translate each file with the `translate-docs` skill**

Data Migration pages are column-by-column format references: translate the prose and the "Description" column of tables only. Column / field names, example values, file names and code blocks stay English.

- [ ] **Step 3: Verify status and leftovers**

Run:
```bash
python3 tools/i18n/status.py --lang de
grep -rnE '^(The|This|Click|Select|You can|When) ' de/website de/data-migration | head
```
Expected: only `it-section/README.md`, `MAINTAINING_DOCS.md`, `running-docs-locally.md` under `missing`; no grep output.

- [ ] **Step 4: Verify the import field names survived**

Run: `for f in data-migration/*.md; do diff <(grep -oE '`[A-Za-z_]+`' "$f" | sort -u) <(grep -oE '`[A-Za-z_]+`' "de/$f" | sort -u) >/dev/null || echo "FIELD MISMATCH $f"; done`
Expected: no output (every backticked field name in the English page exists in the German page).

- [ ] **Step 5: Verify in the browser**

Open `http://localhost:3005/#/de/data-migration/items` and `http://localhost:3005/#/de/website/wordpress-plugin`: tables intact, code blocks untouched, copy button reads "Kopieren".

- [ ] **Step 6: Commit**

```bash
git add de/website de/data-migration
git commit -m "German: website and data migration sections

Co-Authored-By: Claude Fable 5.1 <noreply@anthropic.com>"
```

---

### Task 8: German release-note videos

**Blocked on:** the backoffice German UI translation being complete (`locale-de.json` has 1,559 strings still in English). Narration text can be prepared now; render when the UI is ready. Decision to confirm with Brice: whether to render earlier with English UI + German narration.

**Files:**
- Modify: `circuitauction-backoffice/client/cypress/e2e-tutorials/release-3.5/_demo.js` (`loginDemo`)
- Create (by the MCP): `circuitauction-backoffice/client/cypress/e2e-tutorials/release-3.5/<name>.i18n.de.json` and `<name>.timings.de.json` for the 16 tutorials: auction-timeline, client-statistics, bids-reports, consignment-reports, export-accounting, orders-preview-email, invoice-email-list, email-templates, payment-reminders, address-sticker-sheet, task-reply, support-tickets, hibid-import, reset-sale-sync, dark-mode, health-monitor
- Modify: `de/release-notes/version-3.5.md` (video URLs)

**Interfaces:**
- Consumes: circuit-video MCP tools `get_tutorial_text`, `save_tutorial_translation`, `author_tutorial`, `render_tutorial`; `Cypress.env("tutorialLang")` set by `OpenMontage/tools/capture/cypress_bridge.py`.
- Produces: `s3://circuit-kubernetes/openmontage/tutorials/release-3.5-<name>-de/final.mp4` (public via the existing prefix policy).

- [ ] **Step 1: Confirm the UI language localStorage key**

Open `https://backoffice.ddev.site:9010/`, switch the interface language to Deutsch, then in the console run `Object.keys(localStorage).filter(k => /language/.test(k))`.
Expected: `["ls.language"]` (angular-local-storage default prefix `ls`). If the key differs, use that key in step 2.

- [ ] **Step 2: Make the capture follow `tutorialLang`**

In `_demo.js`, change `loginDemo()` to:

```js
/** Log in with the test token, point the sale context at the demo sale and
 *  switch the UI to the tutorial's language (render_tutorial --lang). */
export function loginDemo() {
  cy.loginWithToken();
  const lang = Cypress.env("tutorialLang") || "en";
  cy.window({ log: false }).then((win) => {
    win.localStorage.setItem("ls.language", lang);
    ["localStorage", "sessionStorage"].forEach((store) => {
      win[store].setItem("current_sale", DEMO.SALE_ID);
      win[store].setItem("current_sale_uuid", DEMO.SALE_UUID);
    });
  });
}
```

- [ ] **Step 3: Verify the English render is unchanged**

Run (MCP): `render_tutorial(tutorial="dark-mode", project_id="release-3.5-dark-mode", base_url="https://backoffice.ddev.site:9010", upload=false)`.
Expected: `succeeded`; a frame (`ffmpeg -ss 10 -i OpenMontage/projects/release-3.5-dark-mode/renders/final.mp4 -frames:v 1 /tmp/claude-1000/…/frame.png`) shows the English UI.

- [ ] **Step 4: Translate the narration of all 16 tutorials**

For each name: `get_tutorial_text(tutorial=<name>, lang="de")` → fill every `narration` and the `recipe` values (title "Circuit Auction Backoffice 3.5", intro "Neu in 3.5", outro "Vielen Dank fürs Zuschauen"; narration in formal German using glossary terms, same length as the English line ± 20 % so timings stay comparable) → `save_tutorial_translation(tutorial=<name>, lang="de", translation=<filled object>)`.
Expected per call: a path ending in `<name>.i18n.de.json` and `steps` equal to the English step count.

- [ ] **Step 5: Author timings (voice durations)**

For each name: `author_tutorial(tutorial=<name>, lang="de")`.
Expected: `<name>.timings.de.json` written, `lang=de`.

- [ ] **Step 6: Render and upload, one at a time (Cypress runs must not overlap)**

For each name: `render_tutorial(tutorial=<name>, lang="de", project_id="release-3.5-<name>-de", base_url="https://backoffice.ddev.site:9010", upload=true)`.
Expected: `succeeded`, S3 key `openmontage/tutorials/release-3.5-<name>-de/final.mp4`; `curl -sI https://circuit-kubernetes.s3.eu-central-1.amazonaws.com/openmontage/tutorials/release-3.5-<name>-de/final.mp4 | head -1` → `HTTP/1.1 200 OK`. Extract one frame per video and confirm German UI + German captions.

For `auction-timeline`, repeat the bid-server preparation in `MAINTAINING_DOCS.md` §3 and the memory note (uid 1 mail swap to `robot@no-reply.com.test`, token domain fix) and restore uid 1 afterwards.

- [ ] **Step 7: Point the German release page at the German videos**

Run: `sed -i -E 's#(openmontage/tutorials/release-3\.5-[a-z-]+)/final\.mp4#\1-de/final.mp4#g' de/release-notes/version-3.5.md && grep -c -- '-de/final.mp4' de/release-notes/version-3.5.md`
Expected: `16` (each player line has `src` and `href`, both rewritten; the count is lines).

Then, because the English source did not change, the page stays `current` in `status.py`.

- [ ] **Step 8: Verify in the browser**

Open `http://localhost:3005/#/de/release-notes/version-3.5`; play two videos; German narration and captions.

- [ ] **Step 9: Commit (two repos)**

```bash
cd /media/bl/Disk2/htdocs/circuitauction-backoffice/client && git add cypress/e2e-tutorials/release-3.5 && git commit -m "Tutorials: German narration sidecars and UI language from tutorialLang

Co-Authored-By: Claude Fable 5.1 <noreply@anthropic.com>"
cd /media/bl/Disk2/htdocs/circuitauction-docs && git add de/release-notes/version-3.5.md && git commit -m "German: use German release-3.5 videos

Co-Authored-By: Claude Fable 5.1 <noreply@anthropic.com>"
```

---

### Task 9: German screenshots

**Blocked on:** the same German UI completeness as Task 8.

**Files:**
- Create: `assets/screenshots/de/<same names as assets/screenshots/*.png>` (only for the screenshots referenced by translated pages)
- Modify: the `de/**/*.md` pages that reference them

**Interfaces:**
- Consumes: the Playwright capture harness in `MAINTAINING_DOCS.md` §5 (`Cap` class), demo fixtures from §1.
- Produces: localized images at `/assets/screenshots/de/<name>.png`.

- [ ] **Step 1: List the screenshots the German pages use**

Run: `grep -rhoE '/assets/screenshots/[^)"]+' de | sort -u > /tmp/claude-1000/-media-bl-Disk2-htdocs-circuitauction-docs/53784d85-aaa0-454c-bb8d-42e8dd4b02bd/scratchpad/de-shots.txt && wc -l < "$_"`
Expected: a number ≤ 102.

- [ ] **Step 2: Recreate `cap.py` from `MAINTAINING_DOCS.md` §5 with the language set in the init script**

In `Cap.__init__`, extend the `add_init_script` string with `"localStorage.setItem('ls.language', 'de');"` and set `OUT = ".../assets/screenshots/de"`.

- [ ] **Step 3: Re-run the capture scripts for the listed shots** (same selectors, viewports and clips as the English ones; the live-app shots need the bid-server steps of §3–4).

- [ ] **Step 4: Switch the German pages to the localized files**

Run: `for s in $(cat …/de-shots.txt); do n=${s#/assets/screenshots/}; [ -f "assets/screenshots/de/$n" ] && grep -rl "$s" de | xargs sed -i "s#$s#/assets/screenshots/de/$n#g"; done; python3 tools/i18n/status.py --lang de | head -1`
Expected: pages remain `current` (the English sources are untouched).

- [ ] **Step 5: Verify in the browser** that `http://localhost:3005/#/de/client/understanding-client-page` shows German UI captures.

- [ ] **Step 6: Commit**

```bash
git add assets/screenshots/de de
git commit -m "German: localized screenshots

Co-Authored-By: Claude Fable 5.1 <noreply@anthropic.com>"
```

---

### Task 10: Backoffice opens the help in the user's language

**Files (all in `/media/bl/Disk2/htdocs/circuitauction-backoffice/client`):**
- Modify: `app/scripts/services/main.js` (next to `this.getLanguage`, ~line 721)
- Modify: `app/scripts/controllers/dashboard/documentation.js` (`DocumentationPageCtrl`)
- Modify: `app/views/documentation/main.html`
- Modify: `app/scripts/controllers/dashboard/sale.js:1726,1736,1746,1756`
- Test: `cypress/e2e/documentation/documentation-page-smoke.cy.js`

**Interfaces:**
- Consumes: `MainAppService.getLanguage()` (existing).
- Produces: `MainAppService.docsUrl(page: string) -> string` returning `https://docs.circuitauction.com/#[/<lang>]/<page>`.

- [ ] **Step 1: Write the failing Cypress test**

Append to `documentation-page-smoke.cy.js`:

```js
  it('opens the German docs when the interface language is de', () => {
    cy.window().then((win) => win.localStorage.setItem('ls.language', 'de'));
    cy.visitState('dashboard/documentation', 'state-documentation');
    cy.get('[data-testid="documentation-iframe"]', { timeout: 20000 })
      .should('have.attr', 'src')
      .and('include', 'docs.circuitauction.com/#/de/README');
    cy.window().then((win) => win.localStorage.removeItem('ls.language'));
  });
```

- [ ] **Step 2: Run it to verify it fails**

Run: `cd /media/bl/Disk2/htdocs/circuitauction-backoffice/client && npx cypress run --browser chrome --spec cypress/e2e/documentation/documentation-page-smoke.cy.js`
Expected: the new test fails on `include 'docs.circuitauction.com/#/de/README'` (src is the English URL).

- [ ] **Step 3: Add `docsUrl` to `MainAppService`**

Insert after `this.setLanguage = function (languageCode) {…};` in `main.js`:

```js
    // Languages the help site (docs.circuitauction.com) is published in besides English.
    // Keep in sync with LANGS in circuitauction-docs/index.html.
    var DOCS_LANGUAGES = ['de'];
    var service = this;

    /**
     * URL of a help page in the current interface language (English when the
     * docs are not translated into that language).
     *
     * @param page  e.g. 'data-migration/items' (default 'README').
     */
    this.docsUrl = function (page) {
      var language = service.getLanguage();
      var prefix = DOCS_LANGUAGES.indexOf(language) !== -1 ? '/' + language : '';
      return 'https://docs.circuitauction.com/#' + prefix + '/' + (page || 'README');
    };
```

- [ ] **Step 4: Use it in the documentation page and the import help links**

`documentation.js`: inject `$sce, MainAppService` into `DocumentationPageCtrl` and add inside `init()`:

```js
      $scope.docsUrl = $sce.trustAsResourceUrl(MainAppService.docsUrl('README'));
```

`main.html`: replace `src="https://docs.circuitauction.com/#/README"` with `ng-src="{{docsUrl}}"`.

`sale.js`: replace the four literals, e.g. `help: 'https://docs.circuitauction.com/#/data-migration/items',` → `help: MainAppService.docsUrl('data-migration/items'),` (and `items-catalogs`, `items-dimensions`, `items-sold-result`). Confirm `MainAppService` is already injected into that controller (`grep -n "MainAppService" app/scripts/controllers/dashboard/sale.js | head -1`); inject it if not.

- [ ] **Step 5: Run the smoke spec to verify it passes**

Run: `npx cypress run --browser chrome --spec cypress/e2e/documentation/documentation-page-smoke.cy.js`
Expected: 3 passing (the two existing tests still pass with the English URL).

- [ ] **Step 6: Commit**

```bash
git add app/scripts/services/main.js app/scripts/controllers/dashboard/documentation.js app/views/documentation/main.html app/scripts/controllers/dashboard/sale.js cypress/e2e/documentation/documentation-page-smoke.cy.js
git commit -m "Open the help docs in the interface language when available

Co-Authored-By: Claude Fable 5.1 <noreply@anthropic.com>"
```

---

## Sequencing and effort

| Task | Depends on | Size |
|------|-----------|------|
| 1 Tooling | – | 1–2 h |
| 2 Docsify scaffolding | 1 | 1 h |
| 3 Skill + runbook | 1, 2 | 1 h |
| 4 Entry pages + release notes | 3 | ~7k words |
| 5 Clients/Items/Sale/Consignment | 3 | ~5k words |
| 6 Bids/Auction | 3 | ~2k words |
| 7 Website/Data Migration | 3 | ~15.6k words |
| 8 German videos | 3, backoffice German UI complete | 16 renders, sequential |
| 9 German screenshots | 7, backoffice German UI complete | ≤102 captures |
| 10 Backoffice links | 2 | 1 h |

Tasks 4–7 can run in parallel once Task 3 is done (they touch disjoint folders). Tasks 1–4 and 10 are enough for a first public German release; the site is safe to publish at any point after Task 2 because untranslated pages fall back to English.

**Native review:** every translated section should be read by a German-speaking Circuit Auction person before it is announced; the plan has no step for that because it is not something the executor can do. Keep the per-section commits so review can happen per section.

**Adding the next language** is `TRANSLATING_DOCS.md` → "Adding a language" (Task 3 step 3); it re-uses every task here with `de` replaced.
