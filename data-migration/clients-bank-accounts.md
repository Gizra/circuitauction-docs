---
description: Attach bank account details (multifield) to existing clients.
---

# Clients Bank Accounts

Handler: `ServerClientBankAccountDriveMigrate` — extends `ServerClientBankAccountMigrate`.

Imports rows into the `field_bank_details` **multifield** on client nodes. Each row records one bank account (bank name, code, account number, IBAN, BIC).

Configured via the `migrate_clients_bank_accounts_csv` Drupal variable.

## Source File

Set the **CSV export URL** of your Google Sheet in the `migrate_clients_bank_accounts_csv` variable. The URL must be the CSV form, not the regular `edit` link:

```
https://docs.google.com/spreadsheets/d/<SPREADSHEET_ID>/export?format=csv&gid=<SHEET_GID>
```

The corresponding edit URL (origin) looks like:

```
https://docs.google.com/spreadsheets/d/<SPREADSHEET_ID>/edit?gid=<SHEET_GID>#gid=<SHEET_GID>
```

## Client Lookup

The drive variant resolves the host client directly from `_customer_id` via `server_client_get_client_nid_by_customer_id()`. Rows whose customer id does not match any existing client are skipped with a watchdog warning (`Bank account row without client: <_unique_id> for customer: <_customer_id>`).

{% hint style="info" %}
The parent `ServerClientBankAccountMigrate` (SQL variant) instead resolves the host client through the `ServerClientsMigrate` map. The drive variant deliberately removes that mapping in favour of the direct customer-id lookup.
{% endhint %}

## Columns

| Column | Destination |
|---|---|
| `_unique_id` | Row tracking ID (required) |
| `_customer_id` | Used to resolve the host client. Rows with no match are skipped. |
| `_bank` | `field_bank_name` |
| `_bank_code` | `field_bank_code` |
| `_account_number` | `field_bank_account_number` **and** `field_bank_account_owner` (both populated from the same column) |
| `_iban` | `field_iban` |
| `_bic` | `field_bic` |
