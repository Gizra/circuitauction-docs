# Item Page

**Selector:** `#ca-item-page` &nbsp;•&nbsp; *one per page*

## What it does

Displays a single auction item: image gallery with lightbox, title and subtitle, lot and item numbers, full description, estimate and current/starting bid, buyer's premium, breadcrumbs, favorite and share buttons, an "Ask a Question" form, related items, and the bidding interface. Several display modes let the same block act as a full detail page or a compact card.

## How to add it

```html
<div id="ca-item-page" class="circuit-user-ui" data-item-id="123456"></div>
```

## Options

| Attribute | Required | Default | Values | Effect |
|-----------|----------|---------|--------|--------|
| `data-item-id` | **Yes** | — | NID or UUID | Which item to display. Accepts either the numeric node ID or the UUID. |
| `data-display-mode` | No | `full` | `full`, `teaser`, `grid`, `featured`, `live-auction` | How the item is rendered (see below). |

### Display modes

| Mode | Best for | Shows |
|------|----------|-------|
| `full` | A dedicated item page | Everything: breadcrumbs, full gallery + lightbox, full description, pricing, bidding, favorite/share, ask‑a‑question, related items. |
| `teaser` | List rows | Horizontal card: image, title, lot number, estimate, current/starting bid, favorite, sold status. |
| `grid` | Grid layouts | Vertical card: image, truncated title, lot number, estimate or current bid, favorite, sold indicator. |
| `featured` | Carousels | Large image focus, title, estimate, current bid and integrated bidding. |
| `live-auction` | Live bidding views | Real‑time current bid, increment buttons, bid history, time remaining and sold overlay. |

## Examples

```html
<!-- Full detail page -->
<div id="ca-item-page" class="circuit-user-ui"
     data-item-id="1902261" data-display-mode="full"></div>

<!-- Compact card in a custom grid -->
<div id="ca-item-page" class="circuit-user-ui"
     data-item-id="1902261" data-display-mode="grid"></div>
```
</content>
