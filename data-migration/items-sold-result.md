---
description: Import sold prices and create item history nodes for winning bids.
---

# Items Sold Result

Handler: `ServerItemsSoldResultDriveMigrate`.

Creates `item_history` nodes that record the winning bid for each item — typically run after the sale to import results from an external system.

Configured via the `migrate_items_sold_result_csv` Drupal variable.

## Source File

Set the **CSV export URL** of your Google Sheet in the `migrate_items_sold_result_csv` variable. The URL must be the CSV form, not the regular `edit` link:

```
https://docs.google.com/spreadsheets/d/<SPREADSHEET_ID>/export?format=csv&gid=<SHEET_GID>
```

The corresponding edit URL (origin) looks like:

```
https://docs.google.com/spreadsheets/d/<SPREADSHEET_ID>/edit?gid=<SHEET_GID>#gid=<SHEET_GID>
```

## Required Columns

| Column | Description |
|---|---|
| `_unique_id` | Row tracking ID (required) |
| `_internal_id` | Internal item ID — used to find the item inside the sale |
| `_sale` | Sale NID (or `_sale_number` as a fallback) |
| `_sale_number` | Sale number — resolved to a sale NID if `_sale` is not provided |
| `_sold_for` | Winning price. Empty / 0 → item is marked UNSOLD. Negative → creates a credit note order. |
| `_wining_bidder_email` | Email of the winning bidder (must already exist as a client) |
| `_bidder_alias` | Optional alias to record |
| `_withdrawn` | Forced to `FALSE` |
| `_under_extension_status` | Defaults to `NOT_REQUESTED` |

## Processing Logic

For each row the handler:

1. Looks up the item by `_internal_id` within the resolved sale. Rows with no match are skipped.
2. Resolves the consignment statement via `server_consignment_statement_get_or_create()` for the item's consignment.
3. If `_sold_for` is set:
   * Looks up the winning bidder by email. If missing, the row is skipped.
   * Creates (or fetches) the matching `order` node — type `bidder`, or `credit_note` when `_sold_for` is negative.
   * Sets `field_sold_status` to `SOLD`.
4. Otherwise sets `field_sold_status` to `UNSOLD`.

The newly created item history record is set as the **promoted** one, and the previously promoted item history for the same item is demoted.

## Destination Field Mapping

| Source column | Destination field |
|---|---|
| `_item` (resolved internally) | `field_item` |
| `_order` (resolved internally) | `field_order` |
| `_cs` (resolved internally) | `field_consignment_statement` |
| `_wining_bidder` (resolved internally) | `field_winner_bidder` |
| `_bidder_id` | `field_sold_to_bidder_id` |
| `_bidder_alias` | `field_bidder_alias` |
| `_withdrawn` | `field_withdrawn` — note: `prepareRow()` currently forces this to `FALSE`, so the CSV value is ignored and this handler cannot mark an appearance as withdrawn. |
| `_under_extension_status` | `field_under_extension_status` |
| `_sold_for` | `field_sold_for_amount` |
| `_sold_status` | `field_sold_status` (default `SOLD`) |

{% hint style="info" %}
`ServerItemsUpdateDriveMigrate` and `ServerItemsSelfServiceMigrate` both also queue an item history task when `_sold_for` is set on a row — this handler is the equivalent that runs from a dedicated CSV.
{% endhint %}

{% hint style="warning" %}
**Planned:** the winning-bidder lookup currently resolves **by email only** (`_wining_bidder_email`) and skips the row on no match. A planned change adds a `_customer_id` fallback (via `server_client_get_client_nid_by_customer_id()`, the same resolver used by every other client-side handler) so winners can be matched by customer id when an email is missing or unmatched. Until this ships, every sold row needs a resolvable winner email.
{% endhint %}
