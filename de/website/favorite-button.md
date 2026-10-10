<!-- i18n source=website/favorite-button.md sha=7567066da266 -->
# Favoriten-Button

**Selektor:** `.favorite-btn` (Klasse) &nbsp;•&nbsp; *mehrfach pro Seite erlaubt*

## Funktion

Ein kleiner Herz-Button, mit dem ein angemeldeter Bieter ein Los zu seinen Favoriten hinzufügen oder daraus entfernen kann. Wie Place Bid wird er über die **Klasse** gefunden, sodass Sie ihn neben jedem Los in einer eigenen Liste oder einem Raster platzieren können. Favorisierte Lose erscheinen im Block [Meine Favoriten](/de/website/my-favorites.md) des Bieters.

Klickt ein nicht angemeldeter Besucher darauf, wird er zur Anmeldung aufgefordert.

## So fügen Sie es hinzu

```html
<div class="favorite-btn circuit-user-ui" data-item-id="123456"></div>
```

## Optionen

| Attribut | Erforderlich | Standard | Werte | Wirkung |
|-----------|----------|---------|--------|--------|
| `data-item-id` | **Ja** | — | Los-NID/UUID | Das Los, das als Favorit markiert wird. |
| `data-display-mode` | Nein | `grid` | `grid`, `full` | Visueller Stil des Buttons. `grid` eignet sich für kompakte Kacheln; `full` ist die größere Variante mit Beschriftung. |

## Beispiel

```html
<div class="item-card">
  <img src="lot-101.jpg" alt="Lot 101">
  <div class="favorite-btn circuit-user-ui"
       data-item-id="1902261"
       data-display-mode="grid"></div>
</div>
```
