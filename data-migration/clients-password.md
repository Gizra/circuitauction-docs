---
description: Migrate password hashes (and optional default payment type) onto existing clients.
---

# Clients Password

Handler: `ServerClientsPasswordDriveMigrate`.

Updates the password hash on an existing client node. Used when migrating clients from a legacy system that stores hashes compatible with Drupal's `$HK...$salt` format.

Configured via the `migrate_client_password_csv` Drupal variable. Uses `Migration::DESTINATION` as the system of record.

## Source File

Set the **CSV export URL** of your Google Sheet in the `migrate_client_password_csv` variable. The URL must be the CSV form, not the regular `edit` link:

```
https://docs.google.com/spreadsheets/d/<SPREADSHEET_ID>/export?format=csv&gid=<SHEET_GID>
```

The corresponding edit URL (origin) looks like:

```
https://docs.google.com/spreadsheets/d/<SPREADSHEET_ID>/edit?gid=<SHEET_GID>#gid=<SHEET_GID>
```

## Columns

| Column | Behavior |
|---|---|
| `_unique_id` | Source identifier — used to resolve the client by customer ID when `_nid` is empty (`server_client_get_client_nid_by_customer_id`). |
| `_nid` | Client node ID. Resolved from `_unique_id` if missing; if still empty the row is skipped. |
| `field_password` | Password hash. Stored as `$HK<value>$<salt>`. Rows with `<empty>` are skipped. |
| `salt` | Salt used to compose the stored hash. |
| `_default_payment_method` | Optional. Auto-creates a `payment_types` term and assigns it to `field_default_payment_type`. |

{% hint style="warning" %}
This handler does **not** hash the password — it stores the value verbatim with the `$HK…$<salt>` envelope. Only use it with hashes that are already in the expected format.
{% endhint %}
