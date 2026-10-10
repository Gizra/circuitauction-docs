"""Shared helpers for the docs translation tooling (Python 3 stdlib only).

Layout: English pages at the repo root, one mirror folder per language
(`de/client/x.md` <-> `client/x.md`). A translated page starts with
`<!-- i18n source=<path> sha=<12 hex> -->` so we can tell when its source changed.
"""
from __future__ import annotations

import hashlib
import re
from pathlib import Path
from typing import Iterable

ROOT = Path(__file__).resolve().parents[2]
LANG_RE = re.compile(r"^[a-z]{2}(-[a-z]{2,4})?$")
SKIP_DIRS = {"node_modules", ".git", ".remember", ".claude", "docs", "tools", "assets"}
NON_CONTENT = {"_sidebar.md", "_coverpage.md", "_navbar.md", "SUMMARY.md",
               "MAINTAINING_DOCS.md", "TRANSLATING_DOCS.md"}
HEADER_RE = re.compile(r"<!--\s*i18n\s+source=(?P<source>\S+)\s+sha=(?P<sha>[0-9a-f]{12})\s*-->")
ASSET_LINK_RE = re.compile(r"\]\((?:\.\./)*assets/")
ASSET_SRC_RE = re.compile(r"(src=[\"'])(?:\.\./)*assets/")
RELATIVE_ASSET_RE = re.compile(r"\]\((?:\.\./)*assets/|src=[\"'](?:\.\./)*assets/")
SIDEBAR_LINK_RE = re.compile(r"\]\((?!https?://|/|#)([^)]+\.md)\)")


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


def rewrite_asset_links(text: str) -> str:
    """`](../assets/x)` / `src="../assets/x"` -> `/assets/x` so links work from any language folder."""
    text = ASSET_LINK_RE.sub("](/assets/", text)
    return ASSET_SRC_RE.sub(r"\1/assets/", text)


def has_relative_asset_links(text: str) -> bool:
    return bool(RELATIVE_ASSET_RE.search(text))


def rewrite_sidebar_links(text: str, lang: str) -> str:
    """Make every relative `.md` link in a sidebar absolute under /<lang>/."""
    return SIDEBAR_LINK_RE.sub(lambda m: f"](/{lang}/{m.group(1)})", text)
