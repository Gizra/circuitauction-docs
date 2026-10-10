# Translating These Docs

Maintainer runbook, companion to `MAINTAINING_DOCS.md`. Not in the sidebar.

## How it works
- English lives at the repo root and keeps its URLs. Each language is a mirror folder (`de/…`).
- `index.html` lists the published languages in `LANGS` and tells docsify to fall back to English
  for pages that are not translated (`fallbackLanguages`). Untranslated pages show the English text with working
  images (the plugin in `index.html` rewrites asset links to the depth-correct relative form), but they are missing from that language's search
  (see Known limitations).
- On a language route, `index.html` rewrites app screenshots at render time to `assets/screenshots/<lang>/<name>`
  and falls back (`onerror`) to the English file when that capture does not exist.
- Every translated page starts with `<!-- i18n source=<path> sha=<12 hex> -->`. The sha is the English
  file's content hash at translation time; `tools/i18n/status.py` uses it to flag outdated pages.

## Daily use
| Need | Command |
|------|---------|
| What is left / outdated / has broken links for German | `python3 tools/i18n/status.py --lang de` |
| Create the German copy of a page | `python3 tools/i18n/scaffold.py --lang de client/README.md` |
| Refresh only the header sha of an already-updated page | `python3 tools/i18n/scaffold.py --lang de --restamp client/README.md` |
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
   `search.placeholder`, `search.noData`, `pagination.previousText/nextText`, `copyCode.*`, `nameLink`. docsify picks the first key where `path.indexOf(key) > -1`, so the new `'/<lang>/'` key must come
   **before** the `'/'` key in each of these maps.
3. `_navbar.md`: add `* [<Native name>](/<lang>/)`.
4. `python3 tools/i18n/scaffold.py --lang <lang> --sidebar README.md`, translate `<lang>/_sidebar.md`,
   `<lang>/README.md`, create `<lang>/_coverpage.md` (copy `de/_coverpage.md`).
5. Translate pages with the skill, in the same order as the German plan (home + release notes, then
   Clients / Items / Sale / Consignment, then Bids / Auction, then Website / Data Migration).
6. Videos: `get_tutorial_text` → `save_tutorial_translation` → `author_tutorial(lang)` →
   `render_tutorial(lang, project_id="release-3.5-<name>-<lang>")`. ElevenLabs needs a voice for the
   language in `ELEVENLABS_VOICE_IDS` (OpenMontage `.env`); today only `de,en` are configured.
7. Screenshots: see `MAINTAINING_DOCS.md` §5 and set both `localStorage['ls.language']` and
   `NG_TRANSLATE_LANG_KEY` to the code in the capture init script; save under `assets/screenshots/<lang>/` with the
   same file names. They are picked up by file name automatically; no page edits are needed.
8. Backoffice: add the code to `DOCS_LANGUAGES` in `MainAppService.docsUrl` so the embedded help opens
   in that language.

Language-specific notes:
- `he` (Hebrew, RTL): the i18n plugin already sets `<html dir="rtl">` for `he`; add CSS for
  `[dir=rtl] .sidebar`, `.content`, `.app-nav` margins (docsify's vue theme is LTR-only) before publishing.
- `zh-hans`: docsify's search tokenizes on characters, so searching works; keep headings short.
- `ru`, `fr`, `nl`: nothing special.

## Known limitations
- Search: on `/#/de/` the docsify search plugin only indexes pages that exist under `/de/`, and it requests
  the rest on each navigation, which produces background 404s until those pages are translated. German search
  therefore covers translated pages only.
