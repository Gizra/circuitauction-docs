# Sales List

**Selector:** `#ca-sales-list` &nbsp;•&nbsp; *one per page*

## What it does

Displays a filterable, paginated list of your sales. Visitors can switch between grid, list and minimal layouts, filter by year, department and status, and optionally see a featured‑items carousel under each sale. It is the typical "Auctions" / "Sales" landing page.

Pagination is server‑side at 20 sales per page, and the current page is reflected in the URL (`?page=2`).

## How to add it

```html
<div id="ca-sales-list" class="circuit-user-ui"></div>
```

That alone shows all sales in grid view with the full filter bar. Add the options below to pre‑filter or change the layout.

## Options

| Attribute | Default | Values | Effect |
|-----------|---------|--------|--------|
| `data-display-mode` | `grid` | `grid`, `list`, `minimal` | Layout of the list. `grid` = responsive cards (3 columns), `list` = full‑width detailed rows, `minimal` = centered image + title + "Sale # – date". |
| `data-status` | `both` | `published_on_site`, `finished`, `both` | Filter by sale status: active/live, closed, or all. |
| `data-department` | — | ID, name or slug | Show only sales in one department. Accepts the department ID, its name (e.g. `memorabilia`) or its machine‑name slug. |
| `data-year` | — | `YYYY` | Show only sales from a given year. |
| `data-first-year` | — | `YYYY` | Turns on a **year filter** spanning from this year up to the current year. Shown as a dropdown normally, or as year buttons when filters are removed. |
| `data-search` | — | text | Pre‑filter by a search term and **hide** the search box (visitors can't change it). |
| `data-remove-filters` | `false` | `true` / `1` | Hide the entire filter bar (search, year, department, status). If combined with `data-first-year`, year selection buttons are shown instead. |
| `data-show-featured-items` | `false` | `true` / `1` | Render a featured‑items carousel beneath each sale that has featured items. |
| `data-item-display` | — | `lot-number` | Only with featured items: `lot-number` shows minimal "LOT # – Sale #" tiles instead of full item cards. |

### Layout details

- **Grid** — image, title, subtitle, formatted date and PDF links (catalogue, e‑book, results). View‑toggle buttons are shown unless `data-display-mode` is forced. The chosen view is remembered in the browser.
- **List** — same as grid plus department labels and the full sale description.
- **Minimal** — centered image, title and "Sale # – date" only. No view toggle.

> **Hidden filters always win.** Any filter you set via an attribute is applied and cannot be changed by the visitor; only the remaining filters appear in the UI.

## Examples

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
</content>
