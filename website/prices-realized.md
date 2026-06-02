# Prices Realized

**Selector:** `#ca-prices-realized` &nbsp;•&nbsp; *one per page*

## What it does

Displays a filterable, paginated grid of results for a **completed** sale — lot number, item thumbnail, opening price, final sold price and sold status. Ideal for a post‑sale "Prices Realized" / results archive page. Each lot links through to its item detail. Pagination is server‑side and reflected in the URL (`?page=2`).

## How to add it

```html
<div id="ca-prices-realized" class="circuit-user-ui"
     data-sale-uuid="backoffice-cls-live-67c87614a7c055-24010246"></div>
```

The sale can also be identified by the URL path — e.g. `/Prices-Realized/<uuid>`. A UUID found in the path takes precedence over `data-sale-uuid`.

## Options

| Attribute | Required | Default | Values | Effect |
|-----------|----------|---------|--------|--------|
| `data-sale-uuid` | **Yes** *(or in URL)* | — | sale UUID | Which sale's results to show. |
| `data-items-per-page` | No | `40` | number | Items shown per page. |
| `data-columns` | No | `4` | `1`–`6` | Number of grid columns. |
| `data-title` | No | `Prices Realized` | text | Heading shown above the grid. |
| `data-show-filters` | No | `true` | `true` / `false` | Show or hide the whole filter section. |
| `data-show-lot-filter` | No | `true` | `true` / `false` | Show or hide the lot‑number filter input. |
| `data-show-status-filter` | No | `true` | `true` / `false` | Show or hide the sold/unsold status dropdown. |
| `data-show-items-per-page` | No | `true` | `true` / `false` | Show or hide the items‑per‑page selector. |
| `data-show-pagination` | No | `true` | `true` / `false` | Show or hide the pagination controls. |

## Examples

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
</content>
