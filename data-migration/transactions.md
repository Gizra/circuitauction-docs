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

1. By `_id` (direct).
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

{% hint style="info" %}
A buyer invoice that spans many lots maps to a single **order** (one order per sale + buyer). A payment is one transaction row referencing any one lot's `_internal_id` — it resolves to the shared order, so billing reconciles at the order level. Send one transaction row per payment; for per-line fidelity send several rows and they all roll up to the same order.
{% endhint %}

{% hint style="warning" %}
**Planned (consignor payouts):** `field_order` already accepts a `consignment_statement` reference as well as an `order`. A planned change adds a consignment-id column to this sheet so a row can resolve a consignment statement (via `server_consignment_statement_get_or_create()`) and point `field_order` at it — mirroring how buyer payments resolve `_internal_id` → order today. This lets consignor payments (`StatementPayment`) ride the same Transactions import; no separate payout handler is needed.
{% endhint %}
