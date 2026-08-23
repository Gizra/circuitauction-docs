---
description: Attach package / dimension info (multifield) to existing items.
---

# Item Dimensions

Handler: `ServerItemDriveDimensionsMigrate`.

Imports rows into the `field_dimensions` **multifield** on item nodes. Each row records a package type, a number on the box and a weight.

## Running from the Backoffice

Open the sale and go to **Item Import → Dimensions**. The tab works like the [Items (Self-Service)](items.md) import:

1. Paste the Google Sheet URL in the **Google drive file URL** textbox — the regular `edit` link is fine, it is converted to the CSV export form automatically — or upload a CSV file instead.
2. Click **Queue import items**. The import runs in the background; rows are matched to the items of the **current sale** by `_internal_id` (unless the sheet carries an explicit `_item` NID).
3. Click **Load Results** to see the per-row status and error messages, and **Queue failed import items** to retry only the failed rows.

## Source File

When no URL / file is given in the tab, the file is read from the `migrate_items_csv` variable (shared with the [Items (Self-Service)](items.md) handler — the legacy site-wide flow). A stored URL must be the CSV form, not the regular `edit` link:

```
https://docs.google.com/spreadsheets/d/<SPREADSHEET_ID>/export?format=csv&gid=<SHEET_GID>
```

The corresponding edit URL (origin) looks like:

```
https://docs.google.com/spreadsheets/d/<SPREADSHEET_ID>/edit?gid=<SHEET_GID>#gid=<SHEET_GID>
```

## Columns

| Column | Destination |
|---|---|
| `_unique_id` | Row tracking ID (required) |
| `_item` | Target item — NID. When empty, the item NID is resolved from `_internal_id` via `server_item_get_internal_id()` |
| `_internal_id` | Internal item ID, used to find the item if `_item` is empty |
| `_box_type` | Required — auto-creates a `package_types` taxonomy term and writes it to `field_package` |
| `_box_number` | `field_number_on_box` |
| `_weight` | `field_weight` |

{% hint style="warning" %}
Rows with an empty `_box_type` are skipped (with a watchdog warning), so make sure every dimension row carries one.
{% endhint %}
