---
description: Bulk import handlers for items, clients, consignments, bids and related data.
---

# Data Migration

The back-office ships with a set of migration handlers used to import data in bulk from a Google Sheet (CSV) or, in some cases, a remote API. Each handler is responsible for a specific entity (items, clients, addresses, bids, etc.) and exposes its own set of source columns.

All handlers share the same general workflow:

1. Prepare a source file (usually a Google Sheet) with the expected column headers.
2. Paste the **CSV export URL** of the sheet in the corresponding form on the back-office.
3. Trigger the queue to process the rows.
4. Review the results table and re-queue failed rows if needed.

{% hint style="info" %}
For Google Sheets the URL must be the CSV export form, not the regular `edit` link. The pattern is:

```
https://docs.google.com/spreadsheets/d/<SPREADSHEET_ID>/export?format=csv&gid=<SHEET_GID>
```
{% endhint %}

## Available Handlers

### Items

| Handler | Purpose |
|---|---|
| [Items (Self-Service)](items.md) | Import new items in bulk, auto-create consignment and consignor when needed. |
| [Items Update](items-update.md) | Update existing items by `nid`, `_internal_id` or by lot. Will not create new items. |
| [Items Sold Result](items-sold-result.md) | Import sold prices and winning bidders, creates item history records. |
| [Item Catalogs](items-catalogs.md) | Attach catalog references (multifield) to existing items. |
| [Item Dimensions](items-dimensions.md) | Attach dimension / package info (multifield) to existing items. |

### Clients & Addresses

| Handler | Purpose |
|---|---|
| [Clients](clients.md) | Import client nodes (buyers & consignors). |
| [Clients Update](clients-update.md) | Update existing clients matched by email. |
| [Clients Password](clients-password.md) | Migrate password hashes onto existing clients. |
| [Addresses](addresses.md) | Import and attach address nodes to existing clients. |
| [External IDs](external-ids.md) | Attach external system IDs (multifield) to clients. |
| [Clients Bank Accounts](clients-bank-accounts.md) | Attach bank account details (multifield) to existing clients. |

### Categories, Sales & Consignments

| Handler | Purpose |
|---|---|
| [Categories](categories.md) | Import the `categories` taxonomy with hierarchy and translations. |
| [Sales](sales.md) | Import sale nodes. |
| [Consignments](consignments.md) | Import consignment nodes. |
| [Consignment Finder Fees](consignment-finder-fees.md) | Attach finder fee multifields to consignments. |
| [Transactions](transactions.md) | Import transaction nodes for orders. |

### Bids

| Handler | Purpose |
|---|---|
| [Bids](bids.md) | Generic CSV/SQL bid import. |
| [Philasearch Bids](bids-philasearch.md) | Fetch and import bids from the Philasearch API. |
| [Delcampe Bids](bids-delcampe.md) | Import bids from a Delcampe export. |
| [Auction Mobility Bids](bids-mobility.md) | Import bids exported by Auction Mobility. |
| [SAN Bids](bids-san.md) | Import bids from a SAN export. |

## Common Conventions

* **Unique identifier:** Each row must carry a `_unique_id` (or equivalent) column. The migration map uses it to track which rows have already been imported and to avoid duplicates.
* **Skipping a row:** When a row references a missing entity (client, item, consignment) the handler logs the reason and skips the row — the **Info** column of the results table shows why.
* **Re-running an import:**
  * **Queue import items** only processes rows that have never been imported.
  * **Queue failed import items** retries only the rows that previously failed.
  * **Queue update All items data** re-imports every row and **overwrites manual back-office changes** — use with caution.
* **Test mode:** In non-live environments, `.test` is appended to outgoing emails to prevent contacting real clients.
