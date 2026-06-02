---
description: Attach catalog references (multifield) to existing items.
---

# Item Catalogs

Handler: `ServerItemDriveCatalogsMigrate`.

Imports rows into the `field_catalog` **multifield** on item nodes. Each row creates one catalog entry (catalog ref, catalog number, sort text) on the targeted item.

The catalog file is read from the same Drupal variable as the items import (`migrate_items_csv`).

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

| Column | Destination |
|---|---|
| `_unique_id` | Row tracking ID (required) |
| `_item` | Target item — NID. When empty, the item NID is resolved from the items migration map (`migrate_map_serveritemsdrivemigrate`) using `_unique_id` |
| `_catalog_name` | Catalog name — resolved to a `catalogs` taxonomy term (auto-created), stored in `field_catalog_ref` |
| `_catalog_number` | `field_catalog_number` |
| `_ordering_sort` | `field_sort_text` |

{% hint style="info" %}
The catalog taxonomy term is cached during the migration run, so a single catalog name is only resolved / created once.
{% endhint %}
