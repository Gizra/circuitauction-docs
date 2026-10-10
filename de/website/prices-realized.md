<!-- i18n source=website/prices-realized.md sha=6c1ee604be3b -->
# Erzielte Preise

**Selektor:** `#ca-prices-realized` &nbsp;•&nbsp; *einmal pro Seite*

## Funktion

Zeigt ein filterbares Raster mit Seitennavigation für die Ergebnisse einer **abgeschlossenen** Auktion — Losnummer, Vorschaubild des Loses, Ausrufpreis, endgültiger Zuschlagspreis und Verkaufsstatus. Ideal für eine Ergebnis- bzw. Archivseite „Prices Realized“ nach der Auktion. Jedes Los verlinkt zu seinen Details. Die Seitennavigation erfolgt serverseitig und wird in der URL abgebildet (`?page=2`).

## So fügen Sie es hinzu

```html
<div id="ca-prices-realized" class="circuit-user-ui"
     data-sale-uuid="backoffice-cls-live-67c87614a7c055-24010246"></div>
```

Die Auktion kann auch über den URL-Pfad angegeben werden — z. B. `/Prices-Realized/<uuid>`. Eine im Pfad gefundene UUID hat Vorrang vor `data-sale-uuid`.

## Optionen

| Attribut | Erforderlich | Standard | Werte | Wirkung |
|-----------|----------|---------|--------|--------|
| `data-sale-uuid` | **Ja** *(oder in der URL)* | — | Auktions-UUID | Von welcher Auktion die Ergebnisse angezeigt werden. |
| `data-items-per-page` | Nein | `40` | Zahl | Anzahl der Lose pro Seite. |
| `data-columns` | Nein | `4` | `1`–`6` | Anzahl der Rasterspalten. |
| `data-title` | Nein | `Prices Realized` | Text | Überschrift über dem Raster. |
| `data-show-filters` | Nein | `true` | `true` / `false` | Den gesamten Filterbereich ein- oder ausblenden. |
| `data-show-lot-filter` | Nein | `true` | `true` / `false` | Das Eingabefeld für den Losnummernfilter ein- oder ausblenden. |
| `data-show-status-filter` | Nein | `true` | `true` / `false` | Das Dropdown für den Status verkauft/unverkauft ein- oder ausblenden. |
| `data-show-items-per-page` | Nein | `true` | `true` / `false` | Die Auswahl der Lose pro Seite ein- oder ausblenden. |
| `data-show-pagination` | Nein | `true` | `true` / `false` | Die Seitennavigation ein- oder ausblenden. |

## Beispiele

```html
<!-- Standard results page -->
<div id="ca-prices-realized" class="circuit-user-ui"
     data-sale-uuid="backoffice-cls-live-67c87614a7c055-24010246"
     data-items-per-page="40"
     data-columns="4"
     data-title="Auction Results"></div>

<!-- Compact embed: no filters, dense grid -->
<div id="ca-prices-realized" class="circuit-user-ui"
     data-sale-uuid="backoffice-cls-live-67c87614a7c055-24010246"
     data-show-filters="false"
     data-columns="6"
     data-items-per-page="100"></div>
```
