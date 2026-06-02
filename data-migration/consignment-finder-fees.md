---
description: Attach finder fee multifields to existing consignments.
---

# Consignment Finder Fees

Handler: `ServerConsignmentFinderFeesDriveMigrate`.

Imports rows into the `field_finder_fees` **multifield** on consignment nodes. Each row records a finder, a commission rate, and the related item.

Configured via the `migrate_items_csv` Drupal variable (shared with the items import).

## Source File

Set the **CSV export URL** of your Google Sheet in the `migrate_items_csv` variable (shared with the [Items (Self-Service)](items.md) handler). The URL must be the CSV form, not the regular `edit` link:

```
https://docs.google.com/spreadsheets/d/<SPREADSHEET_ID>/export?format=csv&gid=<SHEET_GID>
```

The corresponding edit URL (origin) looks like:

```
https://docs.google.com/spreadsheets/d/<SPREADSHEET_ID>/edit?gid=<SHEET_GID>#gid=<SHEET_GID>
```

## Columns

| Column | Used as |
|---|---|
| `_unique_id` | Row tracking ID (required) |
| `_finders_rate` | Required. Stored as a percentage in `field_commission` — the source is expected to be a decimal (e.g. `0.05`), multiplied by 100 on import. Rows with an empty value are skipped. |
| `_finders_fullname` | Required. Split on the first space; the handler looks up a client by first/last name. Rows that match more than one client (or none) are skipped. |
| `_sale_number` | Used to resolve the sale (`server_sale_get_by_sale_number()`). |
| `_consignment_id` | Used together with the resolved sale to find the consignment (`server_consignment_get_by_consignment_id()`). Required. |
| `_internal_id` | Used to resolve the related item via `server_item_get_internal_id()`. |

## Destination Mapping

| Source | Destination |
|---|---|
| `_host` (resolved consignment NID) | `host` |
| `_commission` (× 100 from `_finders_rate`) | `field_commission` |
| `_finder` (resolved client NID) | `field_finder` |
| `_item` (resolved item NID) | `field_item` |
