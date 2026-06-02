---
description: Import bids from a Delcampe export.
---

# Delcampe Bids

Handler: `ServerDelcampeBidMigrate` — extends `ServerBidMigrateBase`.

Imports bids from a Delcampe export. Runs as an AQ task — provide either an `fid` (uploaded CSV) or a `drive_url` (Google Sheet).

The CSV uses **semicolons** as delimiter (Delcampe's default). When importing from a Google Sheet (via `drive_url`), commas are used.

## Source File

This handler runs as an AQ task. Pass either:

* `fid` — a Drupal file id pointing to the raw Delcampe CSV (semicolon-delimited), or
* `drive_url` — the **CSV export URL** of a Google Sheet (comma-delimited):

```
https://docs.google.com/spreadsheets/d/<SPREADSHEET_ID>/export?format=csv&gid=<SHEET_GID>
```

The corresponding edit URL (origin) looks like:

```
https://docs.google.com/spreadsheets/d/<SPREADSHEET_ID>/edit?gid=<SHEET_GID>#gid=<SHEET_GID>
```

Author defaults to the `Delcampe` user; if missing it is created automatically with Clerk permission (`server_bid_import_delcampe_username` variable).

## Expected Columns

| Column | Used as |
|---|---|
| `Catalogus`, `Ttitel`, `Datum`, `Munteenheid`, `Koper` | Informational |
| `Referentie` | Lot — mapped to `lot` |
| `Bedrag` | Amount — mapped to `amount` |
| `E-mail` | Bidder email — mapped to `email` |
| `Naam` | Used to derive first/last name for the missing-client payload |
| `Adres`, `Postcode`, `Stad`, `Regio`, `Land`, `Telefoon` | Used to seed the missing-client payload |

The unique key per row is `<Referentie>-<E-mail>-<Bedrag>`.

## Missing Client Payload

When the bid server cannot match the bidder, the row is saved with `STATUS_MISSING_CLIENT` and the following `client_data` JSON:

```json
{
  "firstname": "...",
  "lastname": "...",
  "email": "...",
  "zip": "...",
  "address": "...",
  "city": "...",
  "state": "...",
  "country": "...",
  "phone": "...",
  "platform": "delcampe"
}
```

This payload is used by the missing-bidder UI in the back-office to create the client on demand.
