<!-- i18n source=website/sales-list.md sha=03675199f4ba -->
# Auktionsliste

**Selektor:** `#ca-sales-list` &nbsp;•&nbsp; *einmal pro Seite*

## Funktion

Zeigt eine filterbare Liste Ihrer Auktionen mit Seitennavigation. Besucher können zwischen Raster-, Listen- und Minimal-Layout wechseln, nach Jahr, Abteilung und Status filtern und optional unter jeder Auktion ein Karussell der Highlight-Lose sehen. Es ist die typische Landingpage „Auktionen“.

Die Seitennavigation erfolgt serverseitig mit 20 Auktionen pro Seite; die aktuelle Seite wird in der URL abgebildet (`?page=2`).

## So fügen Sie es hinzu

```html
<div id="ca-sales-list" class="circuit-user-ui"></div>
```

Damit werden bereits alle Auktionen in der Rasteransicht mit der vollständigen Filterleiste angezeigt. Mit den folgenden Optionen filtern Sie vor oder ändern das Layout.

## Optionen

| Attribut | Standard | Werte | Wirkung |
|-----------|---------|--------|--------|
| `data-display-mode` | `grid` | `grid`, `list`, `minimal` | Layout der Liste. `grid` = responsive Karten (3 Spalten), `list` = detaillierte Zeilen in voller Breite, `minimal` = zentriertes Bild + Titel + „Sale # – Datum“. |
| `data-status` | `both` | `published_on_site`, `finished`, `both` | Nach Auktionsstatus filtern: aktiv/live, beendet oder alle. |
| `data-department` | — | ID, Name oder Slug | Nur Auktionen einer Abteilung anzeigen. Akzeptiert die Abteilungs-ID, ihren Namen (z. B. `memorabilia`) oder ihren maschinenlesbaren Slug. |
| `data-year` | — | `YYYY` | Nur Auktionen eines bestimmten Jahres anzeigen. |
| `data-first-year` | — | `YYYY` | Aktiviert einen **Jahresfilter**, der von diesem Jahr bis zum aktuellen Jahr reicht. Wird normalerweise als Dropdown angezeigt, bei entfernten Filtern als Jahres-Buttons. |
| `data-search` | — | Text | Filtert nach einem Suchbegriff vor und **blendet** das Suchfeld **aus** (Besucher können ihn nicht ändern). |
| `data-remove-filters` | `false` | `true` / `1` | Blendet die gesamte Filterleiste aus (Suche, Jahr, Abteilung, Status). In Kombination mit `data-first-year` werden stattdessen Buttons zur Jahresauswahl angezeigt. |
| `data-show-featured-items` | `false` | `true` / `1` | Stellt unter jeder Auktion mit Highlight-Losen ein Karussell der Highlight-Lose dar. |
| `data-item-display` | — | `lot-number` | Nur mit Highlight-Losen: `lot-number` zeigt minimale Kacheln „LOT # – Sale #“ statt vollständiger Loskarten. |

### Details zum Layout

- **Grid** — Bild, Titel, Untertitel, formatiertes Datum und PDF-Links (Katalog, E-Book, Ergebnisse). Die Buttons zum Umschalten der Ansicht werden angezeigt, sofern `data-display-mode` nicht fest vorgegeben ist. Die gewählte Ansicht wird im Browser gespeichert.
- **List** — wie Grid, zusätzlich mit Abteilungsbezeichnungen und der vollständigen Auktionsbeschreibung.
- **Minimal** — nur zentriertes Bild, Titel und „Sale # – Datum“. Kein Umschalter für die Ansicht.

> **Ausgeblendete Filter haben immer Vorrang.** Jeder Filter, den Sie über ein Attribut setzen, wird angewendet und kann vom Besucher nicht geändert werden; nur die übrigen Filter erscheinen in der Oberfläche.

## Beispiele

```html
<!-- Active sales for one department, with featured carousels -->
<div id="ca-sales-list" class="circuit-user-ui"
     data-status="published_on_site"
     data-department="memorabilia"
     data-show-featured-items="true"
     data-item-display="lot-number"></div>

<!-- Minimal "upcoming sales" strip, no filters -->
<div id="ca-sales-list" class="circuit-user-ui"
     data-display-mode="minimal"
     data-status="published_on_site"
     data-remove-filters="true"></div>

<!-- Year archive with year buttons -->
<div id="ca-sales-list" class="circuit-user-ui"
     data-first-year="2020"
     data-remove-filters="true"></div>
```
