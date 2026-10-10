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
