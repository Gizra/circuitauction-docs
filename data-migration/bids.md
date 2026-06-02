---
description: Generic bid importer from a CSV or a legacy SQL table.
---

# Bids

Handler: `ServerBidMigrate` — extends `ServerBidMigrateBase`.

The generic bid import handler. It can read from either:

* a **CSV file** (uploaded via `fid`) or a **Google Sheet** (via `drive_url`), or
* a **legacy SQL table** (`_raw_bids` joined with `_raw_bidpos` and `_raw_catalogpos`).

The author of the imported bids must be an existing user — the username is read from the `server_bid_import_bid_import_username` variable (defaults to `admin`) and must hold the **Clerk** permission. If the user is missing, the migration aborts.

## Common Variables

| Variable | Purpose |
|---|---|
| `server_bid_import_sale_nid` | Target sale NID — required. |
| `server_bid_import_bid_import_username` | Author for the imported bids. Defaults to `admin`. |
| `server_bid_import_bid_import_table` | SQL source table when not using CSV. Defaults to `_raw_bids`. |
| `server_bid_import_source_sale_id` | Filters the legacy table by sale ID (defaults to `1433`). |

## Source File

This handler runs as an AQ task. Pass either:

* `fid` — a Drupal file id (the file is loaded and downloaded via a presigned S3 URL), or
* `drive_url` — the **CSV export URL** of a Google Sheet:

```
https://docs.google.com/spreadsheets/d/<SPREADSHEET_ID>/export?format=csv&gid=<SHEET_GID>
```

The corresponding edit URL (origin) looks like:

```
https://docs.google.com/spreadsheets/d/<SPREADSHEET_ID>/edit?gid=<SHEET_GID>#gid=<SHEET_GID>
```

The CSV is comma-delimited. When neither `fid` nor `drive_url` is provided, the handler falls back to the legacy SQL source (`_raw_bids`).

## Destination Mapping

| Source column | Destination |
|---|---|
| `lotNo` | `lot` |
| `totalBid` | `amount` |
| `roomBidNo` | `bidder_id` |
| `bidType` | `type` (mapped to `mail`, `floor`, `internet`) |
| `bidTime` | `created` |
| `contactNo` | `customer_number` |

## Bid Type Mapping

| Source `bidType` | Result |
|---|---|
| `0` | `mail` bid |
| `5` | `floor` bid — promoted to `internet` if the bidder number is `≥ 4000` |
| `3`, `10`, `999` | Skipped (zero / duplicate / live-deleted) |
| anything else | Throws an exception (unknown type) |

## Bidder Type by Number Range

The `bidder_id` range determines the bidder type:

| Range | Bidder type |
|---|---|
| `< 300` | `floor_by_agent` |
| `< 400` | `phone` |
| `< 1000` | `floor` |
| `< 4000` | `mail` |
| `≥ 4000` | `website` |

## Client Resolution

For each row the handler resolves the client (`server_client_get_client_nid_by_customer_id`) and calls `server_bid_get_bidder_info()` on the bid server. When the client cannot be matched the row is saved to the map table with `STATUS_MISSING_CLIENT`, including the lot, amount, paddle and email so the missing-bidder UI can re-process them later.
