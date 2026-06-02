---
description: Attach external system IDs (multifield) to existing clients.
---

# External IDs

Handler: `ServerExternalIdsDriveMigrate`.

Imports rows into the `field_external_ids` **multifield** on client nodes. Each row records one `(system, id)` pair, allowing clients to be cross-referenced with external platforms (Philasearch, Delcampe, SAN, etc.).

Configured via the `migrate_clients_external_ids_csv` Drupal variable.

## Source File

Set the **CSV export URL** of your Google Sheet in the `migrate_clients_external_ids_csv` variable. The URL must be the CSV form, not the regular `edit` link:

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
| `_customer_id` | Used to look up the host client via `server_client_get_client_nid_by_customer_id()`. Rows with no match are skipped. |
| `_external_id` | `field_id` |
| `_external_system` | Auto-creates an `external_systems` taxonomy term and assigns it to `field_system` |

The handler depends on `ServerClientsMigrate` having already run.
