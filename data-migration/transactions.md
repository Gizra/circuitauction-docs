---
description: Import transaction nodes attached to existing orders.
---

# Transactions

Handler: `ServerTransactionsDriveMigrate`.

Creates `transaction` nodes and attaches them to the order of an existing item.

Configured via the `migrate_transaction_csv` Drupal variable.

## Source File

Set the **CSV export URL** of your Google Sheet in the `migrate_transaction_csv` variable. The URL must be the CSV form, not the regular `edit` link:

```
https://docs.google.com/spreadsheets/d/<SPREADSHEET_ID>/export?format=csv&gid=<SHEET_GID>
```

The corresponding edit URL (origin) looks like:

```
https://docs.google.com/spreadsheets/d/<SPREADSHEET_ID>/edit?gid=<SHEET_GID>#gid=<SHEET_GID>
```

## Skipped Rows

* Rows with `_status == 'Declined'` are skipped outright.
* Rows that cannot resolve the related item, item-history or order are skipped with a message.

## Item Resolution

The handler resolves the item in this order:

1. By `_internal_id` (direct).
2. By `_item_ref` — a free-form string. The first number after `AW` is extracted (`AW1234` → `1234`); otherwise the first numeric sequence is used.

From the resolved item the handler walks to the last promoted `item_history`, reads the `field_order` from it, and uses the order owner as the client.

## Column Mapping

| Column | Destination |
|---|---|
| `_internal_id` / `_item_ref` | Item lookup (see above) |
| `_status` | Filter — `Declined` skips the row |
| `_bank_account` | `field_bank_account` (auto-creates the bank account term) |
| `_info` | `field_info` |
| `_amount` | `field_amount` |
| `_date` | `field_transaction_date` **and** the node's `created` timestamp (parsed via `strtotime()`) |
| `_order` (resolved) | `field_order` |
| `_client` (resolved from order owner) | `field_client` |
