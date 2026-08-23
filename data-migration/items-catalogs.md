---
description: Attach catalog references (multifield) to existing items.
---

# Item Catalogs

Handler: `ServerItemDriveCatalogsMigrate`.

Imports rows into the `field_catalog` **multifield** on item nodes. Each row creates one catalog entry (catalog ref, catalog number, sort text) on the targeted item.

## Running from the Backoffice

Open the sale and go to **Item Import → Catalogs**. The tab works like the [Items (Self-Service)](items.md) import:

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
| `_item` | Target item — NID. When empty, the item is resolved from `_internal_id` (scoped to the sale in the per-sale flow), falling back to the items migration map (`migrate_map_serveritemsdrivemigrate`) using `_unique_id` |
| `_internal_id` | Internal item ID, used to find the item if `_item` is empty |
| `_catalog_name` | Catalog name — required (empty rows are skipped) — resolved to a `catalogs` taxonomy term (auto-created), stored in `field_catalog_ref` |
| `_catalog_number` | `field_catalog_number` |
| `_ordering_sort` | `field_sort_text` |

{% hint style="info" %}
The catalog taxonomy term is cached during the migration run, so a single catalog name is only resolved / created once.
{% endhint %}
