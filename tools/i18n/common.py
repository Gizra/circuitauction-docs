"""Shared helpers for the docs translation tooling (Python 3 stdlib only).

Layout: English pages at the repo root, one mirror folder per language
(`de/client/x.md` <-> `client/x.md`). A translated page starts with
`<!-- i18n source=<path> sha=<12 hex> -->` so we can tell when its source changed.
"""
from __future__ import annotations

import hashlib
import posixpath
import re
from pathlib import Path
from typing import Iterable

ROOT = Path(__file__).resolve().parents[2]
LANG_RE = re.compile(r"^[a-z]{2}(-[a-z]{2,4})?$")
SKIP_DIRS = {"node_modules", ".git", ".remember", ".claude", "docs", "tools", "assets", "it-section"}
NON_CONTENT = {"_sidebar.md", "_coverpage.md", "_navbar.md", "SUMMARY.md",
               "MAINTAINING_DOCS.md", "TRANSLATING_DOCS.md", "running-docs-locally.md",
               "GITHUB_PAGES_SETUP.md", "tasks_readme.md", "logging-the-system.md"}
HEADER_RE = re.compile(r"<!--\s*i18n\s+source=(?P<source>\S+)\s+sha=(?P<sha>[0-9a-f]{12})\s*-->")
# An asset reference: optional `<`, any run of `../` or `/`, optional `.gitbook/`, then `assets/`.
# docsify resolves image links against the page route (a leading `/` does not make them absolute),
# so the only form that works from `<lang>/<dirs>/x.md` is `../` * (1 + len(dirs)).
ASSET_LINK_RE = re.compile(r"\]\((<?)((?:\.\./|/)*)((?:\.gitbook/)?assets/)")
ASSET_SRC_RE = re.compile(r"(src=[\"'])((?:\.\./|/)*)((?:\.gitbook/)?assets/)")
SIDEBAR_LINK_RE = re.compile(r"\]\((?!https?://|/|#)([^)]+\.md)\)")
# A markdown (non-image) link to a .md page: `[text](target.md#anchor)` / `[text](<target.md>)`.
PAGE_LINK_RE = re.compile(r"(?<!!)(\[[^\]]*\]\()(<?)([^)>\s#]+\.md)(#[^)>\s]*)?(>?)\)")
ABS_PAGE_LINK_RE = re.compile(r"(?<!!)\[[^\]]*\]\(<?(/[^)>\s#]+\.md)(?:#[^)>\s]*)?>?\)")


def _is_relative_target(target: str) -> bool:
    return not (target.startswith("/") or re.match(r"[a-z][a-z0-9+.-]*:", target, re.I))


def is_lang_dir(p: Path) -> bool:
    return p.is_dir() and bool(LANG_RE.match(p.name)) and any(p.rglob("*.md"))


def lang_dirs(root: Path = ROOT) -> list[str]:
    return sorted(p.name for p in root.iterdir() if is_lang_dir(p))


def source_pages(root: Path = ROOT, exclude: Iterable[str] = ()) -> list[str]:
    """English content pages, as posix paths relative to the repo root."""
    langs = set(lang_dirs(root)) | set(exclude)
    pages = []
    for p in root.rglob("*.md"):
        rel = p.relative_to(root)
        if (rel.parts[0] in SKIP_DIRS or rel.parts[0].startswith(".")
                or rel.parts[0] in langs or rel.name in NON_CONTENT):
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


def asset_prefix(page: str) -> str:
    """`../` repeated for the page's depth inside <lang>/ (`tasks.md` -> `../`, `a/b.md` -> `../../`)."""
    return "../" * (len(Path(page).parts))


def rewrite_asset_links(text: str, page: str) -> str:
    """Normalise every asset link to the depth-correct relative form for `<lang>/<page>`."""
    prefix = asset_prefix(page)
    text = ASSET_LINK_RE.sub(lambda m: f"]({m.group(1)}{prefix}{m.group(3)}", text)
    return ASSET_SRC_RE.sub(lambda m: f"{m.group(1)}{prefix}{m.group(3)}", text)


def has_misresolved_asset_links(text: str, page: str) -> bool:
    """True if any asset link in `<lang>/<page>` does not use exactly the expected `../` prefix."""
    prefix = asset_prefix(page)
    return any(m.group(2) != prefix
               for rx in (ASSET_LINK_RE, ASSET_SRC_RE) for m in rx.finditer(text))


def rewrite_sidebar_links(text: str, lang: str) -> str:
    """Make every relative `.md` link in a sidebar absolute under /<lang>/."""
    return SIDEBAR_LINK_RE.sub(lambda m: f"](/{lang}/{m.group(1)})", text)


def rewrite_page_links(text: str, page: str, lang: str, root: Path) -> str:
    """Make relative `.md` page links absolute: `/<lang>/<path>.md` if translated, else `/<path>.md`.

    docsify resolves body links from the site root (no `relativePath`), so relative targets would
    leave the language. Targets are resolved against the English page's folder first, then the root.
    Links whose target exists in neither place are left unchanged.
    """
    def repl(m: re.Match) -> str:
        head, lt, target, anchor, gt = m.groups()
        if not _is_relative_target(target):
            return m.group(0)
        for cand in (posixpath.normpath(posixpath.dirname(page) + "/" + target), posixpath.normpath(target)):
            if not cand.startswith("..") and (root / cand).is_file():
                prefix = f"/{lang}/" if (root / lang / cand).is_file() else "/"
                return f"{head}{lt}{prefix}{cand}{anchor or ''}{gt})"
        return m.group(0)
    return PAGE_LINK_RE.sub(repl, text)


def has_relative_page_links(text: str) -> bool:
    return any(_is_relative_target(m.group(3)) for m in PAGE_LINK_RE.finditer(text))


def has_dead_absolute_page_links(text: str, root: Path) -> bool:
    return any(not (root / m.group(1).lstrip("/")).is_file() for m in ABS_PAGE_LINK_RE.finditer(text))
