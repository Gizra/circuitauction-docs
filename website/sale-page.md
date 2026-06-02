# Sale Page

**Selector:** `#ca-sale-page` &nbsp;•&nbsp; *one per page*

## What it does

Shows the full item listing for a single sale: a searchable, filterable, paginated catalog with faceted search. This is the main "browse this auction" page. It includes the sale header (via the Sale Info block), an "About This Sale" section, and the item results with grid/list views.

Visitors can search by lot number or text, filter by sold status, favorites, price range and lot‑number range, use taxonomy facets (category, material, period, etc.), and sort by lot or price. Items per page can be 25, 50, 100 or 200. The current page and lot‑number range are kept in the URL for deep linking (`?page=2`, `?lotNumberRange=100-200`).

## How to add it

```html
<div id="ca-sale-page" class="circuit-user-ui" data-sale-nid="8"></div>
```

## Options

| Attribute | Required | Default | Values | Effect |
|-----------|----------|---------|--------|--------|
| `data-sale-nid` | **Yes** | — | sale NID | Which sale's items to show. |
| `data-show-featured` | No | `false` | `true` | Render a featured‑items carousel above the sale body (before "About This Sale"). Uses the lot‑number tile style; hides itself if the sale has no featured items. |
| `data-debug` | No | `false` | `true` | Enables developer console logging. |

## Examples

```html
<!-- Basic sale page -->
<div id="ca-sale-page" class="circuit-user-ui" data-sale-nid="8"></div>

<!-- With a featured-items carousel at the top -->
<div id="ca-sale-page" class="circuit-user-ui"
     data-sale-nid="8"
     data-show-featured="true"></div>
```

## See also

- [Featured Items](website/featured-items.md) — the carousel this page can embed
- [Sale Info](website/sale-info.md) — the sale header shown on this page
- [Prices Realized](website/prices-realized.md) — results table for a closed sale
</content>
