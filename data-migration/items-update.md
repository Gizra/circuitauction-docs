---
description: Update existing item nodes from a CSV. Will not create new items.
---

# Items Update

Handler: `ServerItemsUpdateDriveMigrate`.

This handler updates **existing** item nodes from a CSV. Unlike the regular items migration, it does not create new items — if it cannot find a matching item for a row, the row is skipped with a message in the result table.

Configured via `migrate_items_update_csv` (Drupal variable). When `migrate_sale_reference_nid` is set, the handler reads from the `_raw_item` SQL table instead, filtered by sale.

## Source File

Set the **CSV export URL** of your Google Sheet in the `migrate_items_update_csv` variable. The URL must be the CSV form, not the regular `edit` link:

```
https://docs.google.com/spreadsheets/d/<SPREADSHEET_ID>/export?format=csv&gid=<SHEET_GID>
```

The corresponding edit URL (origin) looks like:

```
https://docs.google.com/spreadsheets/d/<SPREADSHEET_ID>/edit?gid=<SHEET_GID>#gid=<SHEET_GID>
```

{% hint style="info" %}
Internally this uses `Migration::DESTINATION` as the system of record: only the columns mapped by this handler are written; all other fields keep their current value.
{% endhint %}

## Matching Strategy

The handler tries to match an existing item, in this order:

1. **`_nid`** - direct node ID
2. **`_lot_number` + `_lot_letter` + `_sale`** - lookup by lot inside a sale
3. **`_internal_id` (+ `_sale`)** - lookup by internal item id
4. **`_consignment` + `_position_of_consignment`** - constructs an internal id like `consignment_id` + zero-padded position

If none of these resolves an existing item, the row is dropped with a "No item found" message.

## Updatable Fields

| Column | Field updated |
|---|---|
| `_language` | Item language (defaults to site default) |
| `_internal_id` | `field_internal_id` |
| `_position_of_consignment` | `field_position_of_consignment` |
| `_title_{lang}` | `title` / `title_field` |
| `_body_{lang}` | `body` (filtered_html) |
| `_opening_price` | `field_opening_price` |
| `_minimum_price` | `field_minimum_price` |
| `_estimation_high` | `field_estimate_high` |
| `_estimation_low` | `field_estimate_low` |
| `_main_category` | `field_category` (pipe-separated, or via the categories migration when `server_migrate_map_categories_from_migrate` is enabled) |
| `_main_category_id` | `field_category` via Philaworksplace ID lookup |
| `_symbol_ids` | `field_symbols` (pipe-separated, mapped via `ServerSymbolsMigrate`) |
| `_sub_symbol_id` | `field_sub_symbol` (mapped via `ServerSubSymbolsMigrate`) |
| `_search_tag` | `field_search_tags` |
| `_item_type` | `field_item_type` (default `single`) |
| `_thematics` | `field_thematics` |
| `_sold_for` | `field_sold_for_amount` — also triggers creation of an item history task (see [Items Sold Result](items-sold-result.md)) |
| `_responsible_clerk` | Sets the responsible clerk |
| `_catalog_part` | Creates / sets `field_catalogue_part` term |
| `_lot_number` | Overrides `field_lot_number` |
| `_title_{secondary_lang}` | Translated title for the configured second language |
| `_body_{secondary_lang}` | Translated body for the configured second language |

{% hint style="info" %}
By default the handler returns early after updating "above" fields (lot number, titles, body, categories). To process the full mapping, disable the `server_migrate_update_item_early_return` variable.
{% endhint %}

## Multi-language Behavior

The configured secondary language is read from the `migrate_items_csv_second_language` variable. When the relevant `_title_{lang}` / `_body_{lang}` columns are present in the CSV, the handler writes them to the translated wrappers.

For categories, when `server_migrate_force_category_translation_update` is on, existing terms are updated with the translated name from the CSV.
