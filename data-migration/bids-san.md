---
description: Import bids from a SAN export.
---

# SAN Bids

Handler: `ServerSANBidMigrate` — extends `ServerBidMigrateBase`.

Imports bids from a SAN export. Runs as an AQ task — provide either an `fid` (uploaded CSV) or a `drive_url` (Google Sheet). The CSV is comma-delimited.

## Source File

This handler runs as an AQ task. Pass either:

* `fid` — a Drupal file id pointing to the raw SAN CSV (comma-delimited), or
* `drive_url` — the **CSV export URL** of a Google Sheet:

```
https://docs.google.com/spreadsheets/d/<SPREADSHEET_ID>/export?format=csv&gid=<SHEET_GID>
```

The corresponding edit URL (origin) looks like:

```
https://docs.google.com/spreadsheets/d/<SPREADSHEET_ID>/edit?gid=<SHEET_GID>#gid=<SHEET_GID>
```

Author defaults to the `SAN` user; if missing it is created automatically with Clerk permission (`server_bid_import_san_username` variable).

## Expected Columns

| Column | Used as |
|---|---|
| `CustNo` | Source customer number — stored as `external_id` on the missing-client payload |
| `lName`, `fName` | Name |
| `Handle`, `Paddle` | Optional paddle data |
| `Email`, `EMAIL2` | Bidder email |
| `SaleNo` | Informational |
| `LotNo` | Lot — mapped to `lot` |
| `Amount` | Amount — mapped to `amount` |
| `BidUpTo`, `DateRcvd`, `Misc`, `Or_Ind` | Informational |
| `ADDR1`, `ADDR2`, `ADDR3`, `CITY`, `STATE`, `ZIP`, `COUNTRY` | Used to seed the missing-client payload |
| `WPHONE`, `HPHONE`, `FPHONE`, `OPHONE` | Used to seed the missing-client payload |

The migration key is `<LotNo>-<Email>-<Amount>`.

## Missing Client Payload

When the bid server cannot match the bidder, the row is saved with `STATUS_MISSING_CLIENT` and the `client_data` JSON includes:

* `firstname`, `lastname`, `email`, `secondary_email`
* `zip`, `address`, `address2`, `address3`, `city`, `state`, `country` (country normalized via `server_address_get_country_code()`)
* `office_phone`, `phone`, `fax`, `mobile`
* `external_id` (from `CustNo`)
* `platform: "SAN"`

The back-office uses this payload to create the client on demand.
