<!-- i18n source=website/sale-page.md sha=729523d3d54b -->
# Auktionsseite

**Selektor:** `#ca-sale-page` &nbsp;•&nbsp; *einmal pro Seite*

## Funktion

Zeigt die vollständige Losliste einer einzelnen Auktion: einen durchsuchbaren, filterbaren Katalog mit Seitennavigation und Facettensuche. Dies ist die zentrale Seite zum Stöbern in einer Auktion. Sie enthält den Auktionskopf (über den Block Auktionsinformation), einen Abschnitt „About This Sale“ und die Ergebnisse der Lose in Raster- und Listenansicht.

Besucher können nach Losnummer oder Text suchen, nach Verkaufsstatus, Favoriten, Preisbereich und Losnummernbereich filtern, Taxonomie-Facetten (Kategorie, Material, Epoche usw.) nutzen und nach Los oder Preis sortieren. Pro Seite können 25, 50, 100 oder 200 Lose angezeigt werden. Die aktuelle Seite und der Losnummernbereich werden für Deep Links in der URL gehalten (`?page=2`, `?lotNumberRange=100-200`).

## So fügen Sie es hinzu

```html
<div id="ca-sale-page" class="circuit-user-ui" data-sale-nid="8"></div>
```

## Optionen

| Attribut | Erforderlich | Standard | Werte | Wirkung |
|-----------|----------|---------|--------|--------|
| `data-sale-nid` | **Ja** | — | Auktions-NID | Von welcher Auktion die Lose angezeigt werden. |
| `data-show-featured` | Nein | `false` | `true` | Stellt über dem Hauptteil der Auktion (vor „About This Sale“) ein Karussell der Highlight-Lose dar. Verwendet den Kachelstil mit Losnummer; blendet sich aus, wenn die Auktion keine Highlight-Lose hat. |
| `data-debug` | Nein | `false` | `true` | Aktiviert die Protokollierung in der Entwicklerkonsole. |

## Beispiele

```html
<!-- Basic sale page -->
<div id="ca-sale-page" class="circuit-user-ui" data-sale-nid="8"></div>

<!-- With a featured-items carousel at the top -->
<div id="ca-sale-page" class="circuit-user-ui"
     data-sale-nid="8"
     data-show-featured="true"></div>
```

## Siehe auch

- [Hervorgehobene Lose](website/featured-items.md) — das Karussell, das diese Seite einbetten kann
- [Auktionsinfo](website/sale-info.md) — der Auktionskopf, der auf dieser Seite angezeigt wird
- [Erzielte Preise](website/prices-realized.md) — Ergebnistabelle einer abgeschlossenen Auktion
