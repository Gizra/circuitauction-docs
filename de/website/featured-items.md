<!-- i18n source=website/featured-items.md sha=8f85fc2372ba -->
# Hervorgehobene Lose

**Selektor:** `#ca-featured-items` &nbsp;•&nbsp; *einmal pro Seite*

## Funktion

Zeigt ein automatisch ablaufendes Karussell der Lose, die für eine Auktion als **Featured** markiert sind. Optional kann es über dem Karussell das Auktionsbild oder die vollständige Auktionsinformation anzeigen. Es eignet sich ideal für einen Highlight-Streifen auf der Startseite oder den oberen Bereich einer Auktions-Landingpage.

Das Karussell wechselt alle 8 Sekunden, pausiert beim Überfahren mit der Maus und bietet Schaltflächen für Wiedergabe/Pause und Zurück/Weiter sowie Tastaturbedienung (links/rechts zum Blättern, Leertaste zum Pausieren). Hat eine Auktion keine Highlight-Lose, stellt der Block nichts dar.

## So fügen Sie es hinzu

```html
<div id="ca-featured-items" class="circuit-user-ui" data-sale-nid="123"></div>
```

## Optionen

| Attribut | Erforderlich | Standard | Werte | Wirkung |
|-----------|----------|---------|--------|--------|
| `data-sale-nid` | **Ja** | — | Auktions-NID | Von welcher Auktion die Highlight-Lose angezeigt werden. |
| `data-display-mode` | Nein | *(keiner)* | `sale-image`, `sale-info` | Was über dem Karussell angezeigt wird. Ohne Angabe nur das Karussell; `sale-image` fügt das anklickbare Auktionslogo hinzu; `sale-info` fügt Logo, Titel, Datum/Ort, Link zum Online-Katalog und PDF-Links hinzu. |
| `data-item-display` | Nein | *(keiner)* | `lot-number` | Wie jede Losekachel aussieht. Ohne Angabe vollständige Kacheln (Bild, Titel, Preise). `lot-number` zeigt nur das Bild mit einem Link „LOT # – Sale #“ darunter und blendet die Punktindikatoren aus. |

## Beispiele

```html
<!-- Carousel only -->
<div id="ca-featured-items" class="circuit-user-ui" data-sale-nid="123"></div>

<!-- Homepage highlight: full sale info + minimal item tiles -->
<div id="ca-featured-items" class="circuit-user-ui"
     data-sale-nid="123"
     data-display-mode="sale-info"
     data-item-display="lot-number"></div>

<!-- Just the sale image above the carousel -->
<div id="ca-featured-items" class="circuit-user-ui"
     data-sale-nid="123"
     data-display-mode="sale-image"></div>
```

> **Tipp:** Der Block [Auktionsseite](website/sale-page.md) kann dieses Karussell mit `data-show-featured="true"` automatisch einbetten, und der Block [Auktionsliste](website/sales-list.md) kann mit `data-show-featured-items="true"` pro Auktion eines anzeigen.
