---
description: Import address nodes and attach them to existing clients.
---

# Addresses

Handler: `ServerAddressesDriveMigrate`.

Creates `address` nodes and attaches them to existing clients. The first imported address per client is set as the client's default address.

Configured via the `migrate_clients_address_csv` Drupal variable.

## Source File

Set the **CSV export URL** of your Google Sheet in the `migrate_clients_address_csv` variable. The URL must be the CSV form, not the regular `edit` link:

```
https://docs.google.com/spreadsheets/d/<SPREADSHEET_ID>/export?format=csv&gid=<SHEET_GID>
```

The corresponding edit URL (origin) looks like:

```
https://docs.google.com/spreadsheets/d/<SPREADSHEET_ID>/edit?gid=<SHEET_GID>#gid=<SHEET_GID>
```

## Client Lookup

The handler resolves the target client in this order:

1. By `_customer_id` (via `getClientRef()`).
2. By `_email` (via `server_client_get_by_email()`).

If neither resolves a client the row is skipped with a watchdog error.

## Columns

| Column | Used as |
|---|---|
| `_unique_id` | Row tracking ID (required) |
| `_customer_id` | Primary client lookup |
| `_email` | Fallback client lookup |
| `salutation` | Stored in client salutation (a single dash `-` is treated as empty) |
| `_attention` | `care_of` field. A leading `c/o ` prefix is stripped. |
| `_address1` | `thoroughfare` |
| `_address2`, `_address3` | Concatenated into `premise` (space-separated) |
| `_city` | `locality` |
| `_state`, `_county` | `administrative_area` (state preferred, county fallback) |
| `_county` | `county` |
| `_postal_code` | `postal_code` |
| `_country` | Normalized via `server_address_get_country_code()` |

## Default Address Behavior

When `field_default_address` is empty on the client (or set to a different node), the imported address is assigned as the default. Validations and duplicate-email checks on the client are bypassed during the save to allow the update.

{% hint style="info" %}
The base address-type checks (`server_address_node_presave`) are explicitly disabled via `noAddressTypeChecks` on the node during migration.
{% endhint %}
