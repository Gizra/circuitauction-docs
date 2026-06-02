# Sale Info

**Selector:** `#ca-sale-info` &nbsp;•&nbsp; *one per page*

## What it does

A standalone information block for a single sale. It shows the sale logo, title, subtitle, formatted date range, location, department labels, an "About This Sale" expandable description, and download links (PDF catalogue, e‑book, sale results) when available. The logo and title link through to the sale page.

Use it as a header on a custom sale landing page, a sidebar widget, or a department preview — anywhere you want sale details without the full item listing.

## How to add it

```html
<div id="ca-sale-info" class="circuit-user-ui" data-sale-nid="123"></div>
```

## Options

| Attribute | Required | Effect |
|-----------|----------|--------|
| `data-sale-nid` | **Yes** | The NID of the sale to display. |

This block has no other options.

### Date formatting

Dates are formatted intelligently:

- Single day → `January 11, 2026`
- Same month → `January 13–16, 2026`
- Different months → `January 28 – February 3, 2026`
- Different years → `December 30, 2025 – January 2, 2026`

## Examples

```html
<!-- Sale header, then a featured carousel below it -->
<div id="ca-sale-info"      class="circuit-user-ui" data-sale-nid="123"></div>
<div id="ca-featured-items" class="circuit-user-ui" data-sale-nid="123"
     data-item-display="lot-number"></div>
```

> To list several sales at once, use the [Sales List](website/sales-list.md) block instead — Sale Info renders a single sale.
</content>
