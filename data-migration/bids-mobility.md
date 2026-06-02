---
description: Import bids exported by Auction Mobility.
---

# Auction Mobility Bids

Handler: `ServerMobilityBidMigrate` — extends `ServerBidMigrateBase`.

Imports bids from an Auction Mobility export. Runs as an AQ task — provide either an `fid` (uploaded CSV) or a `drive_url` (Google Sheet, comma-delimited).

When a CSV is uploaded directly, the handler defaults to a **semicolon** delimiter (Mobility's default).

## Source File

This handler runs as an AQ task. Pass either:

* `fid` — a Drupal file id pointing to the raw Auction Mobility CSV (semicolon-delimited), or
* `drive_url` — the **CSV export URL** of a Google Sheet (comma-delimited):

```
https://docs.google.com/spreadsheets/d/<SPREADSHEET_ID>/export?format=csv&gid=<SHEET_GID>
```

The corresponding edit URL (origin) looks like:

```
https://docs.google.com/spreadsheets/d/<SPREADSHEET_ID>/edit?gid=<SHEET_GID>#gid=<SHEET_GID>
```

Author defaults to the `Mobility` user; if missing it is created automatically with Clerk permission (`server_bid_import_mobility_username` variable).

## Expected Columns

| Column | Used as |
|---|---|
| `rowId` | Source unique ID — used as the migration key |
| `lotNumber`, `lotNumberExtension` | Lot — mapped to `lot` |
| `soldPrice` | Amount — mapped to `amount` |
| `status` | Informational |
| `winnerEmail` | Bidder email — required. Rows without an email are skipped. |
| `winnerIsClerk`, `winnerPaddle`, `winnerNote`, `winnerName` | Used to derive bidder info |
| `winnerShippingAddress*`, `winnerPhoneNumber`, `winnerCreditCard*` | Used to seed the missing-client payload |
| `type` | Optional. Mapped to bidder type — `mail`, `phone`, `floor`, otherwise `website`. |

## Missing Client Payload

When the bid server cannot match the bidder, the row is saved with `STATUS_MISSING_CLIENT`. The `client_data` JSON includes name, email, shipping address, phone, and `"platform": "mobility"` so the back-office can create the client on demand.

## Bidder Type Mapping

| `type` value | `bidderType` |
|---|---|
| `mail` | `mail` |
| `phone` | `phone` |
| `floor` | `floor` |
| anything else / empty | `website` |
