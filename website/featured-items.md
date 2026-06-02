# Featured Items

**Selector:** `#ca-featured-items` &nbsp;•&nbsp; *one per page*

## What it does

Displays an autoplaying carousel of the items tagged **Featured** for one sale. Optionally it can show the sale's image or full sale information above the carousel. It is ideal for a homepage highlight strip or the top of a sale landing page.

The carousel advances every 8 seconds, pauses on hover, and offers play/pause and previous/next controls plus keyboard navigation (left/right to move, space to pause). If a sale has no featured items, the block renders nothing.

## How to add it

```html
<div id="ca-featured-items" class="circuit-user-ui" data-sale-nid="123"></div>
```

## Options

| Attribute | Required | Default | Values | Effect |
|-----------|----------|---------|--------|--------|
| `data-sale-nid` | **Yes** | — | sale NID | Which sale's featured items to show. |
| `data-display-mode` | No | *(none)* | `sale-image`, `sale-info` | What to show above the carousel. Omit for carousel only; `sale-image` adds the clickable sale logo; `sale-info` adds logo, title, date/location, online‑catalog link and PDF links. |
| `data-item-display` | No | *(none)* | `lot-number` | How each item tile looks. Omit for full tiles (image, title, pricing). `lot-number` shows just the image with a "LOT # – Sale #" link below, and hides the dot indicators. |

## Examples

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

> **Tip:** The [Sale Page](website/sale-page.md) block can embed this carousel automatically with `data-show-featured="true"`, and the [Sales List](website/sales-list.md) block can show one per sale with `data-show-featured-items="true"`.
</content>
