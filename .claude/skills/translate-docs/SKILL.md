---
name: translate-docs
description: Translate a CircuitAuction docs page (docsify markdown) into a language folder such as de/, following the glossary and the i18n provenance rules. Use when asked to translate, update or review a translated docs page.
---

# Translate a docs page

## Workflow (all commands run from the repo root)
1. `python3 tools/i18n/status.py --lang <lang>` – pick pages that are `missing`, `untranslated` or `outdated`.
2. Missing page: `python3 tools/i18n/scaffold.py --lang <lang> <page>`; it creates `<lang>/<page>` with the
   provenance header and the English text (asset links already depth-correct).
3. Outdated page: read the English source, diff against what the translation describes, update the
   translation, then refresh the header with
   `python3 tools/i18n/scaffold.py --lang <lang> --restamp <page>`.
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
- The glossary is generated from UI strings; a few rows built from long or odd UI texts are unreliable (e.g. punctuation-only rows). Use it for labels and nouns, and ignore rows that are obviously not a term.
- German: formal "Sie". Nouns per the glossary (Kunde, Los (Plural: Lose), Einlieferung, Auktion, Gebot, Aufgabe,
  Rechnung, Zuschlag). Keep English words that the glossary keeps. Where this list and the glossary disagree, the glossary wins.
- Links: links to other pages are absolute: `/<lang>/<path>.md` when the German page exists, `/<path>.md` for
  pages that stay English. The scaffold writes them that way and `status.py` reports anything else as
  `broken-links` (docsify resolves body links from the site root, so relative targets leave the language).
  When the target heading is translated, the anchor is the slug of the translated heading (lower-case,
  spaces to `-`, punctuation removed).
- Images: keep the depth-correct relative form the scaffold produces (`../assets/…` for a root page,
  `../../assets/…` one folder down, …); `status.py` flags anything else as broken-assets. Keep the same image path as the English page; on language routes `index.html` swaps in `assets/screenshots/<lang>/<name>` automatically when that file exists. Translate alt texts.
- Release notes: keep version numbers, dates and `<video class="release-video" …>` lines. Use the `-<lang>`
  video URL (`…/release-3.5-<name>-<lang>/final.mp4`) only when that render exists in S3 (check with
  `curl -sI <url> | head -1` → `200`); otherwise keep the English URL.
- Never leave English paragraphs behind except the untranslatable items above; `status.py` cannot
  detect a half-translated page.
