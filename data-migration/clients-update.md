---
description: Update existing clients matched by email.
---

# Clients Update

Handler: `ServerClientsUpdateDriveMigrate` — extends `ServerClientsMigrate`.

Updates **existing** client nodes from a CSV. Rows are matched on `_email`; rows whose email does not correspond to an existing client are skipped with a watchdog error.

Configured via the `migrate_clients_update_csv` Drupal variable.

## Source File

Set the **CSV export URL** of your Google Sheet in the `migrate_clients_update_csv` variable. The URL must be the CSV form, not the regular `edit` link:

```
https://docs.google.com/spreadsheets/d/<SPREADSHEET_ID>/export?format=csv&gid=<SHEET_GID>
```

The corresponding edit URL (origin) looks like:

```
https://docs.google.com/spreadsheets/d/<SPREADSHEET_ID>/edit?gid=<SHEET_GID>#gid=<SHEET_GID>
```

Internally this uses `Migration::DESTINATION` as the system of record, so only the columns mapped by this handler overwrite existing values.

## Columns

The handler maps:

| Column | Destination |
|---|---|
| `_email` | Used to look up the existing client; the row is skipped if no match. |
| `_nid` | Resolved internally from the matched client and written back to the destination. |
| All other columns inherited from `ServerClientsMigrate` | Whatever fields the base mapping defines (phone, address fields, salutation, etc.). |

## Splitting Full Name

Same as the [Clients](clients.md) handler: when `_first_name` is empty and `server_migrate_split_lastname_column` is on, `_last_name` is split on the first space.
