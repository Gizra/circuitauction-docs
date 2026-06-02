---
description: Fetch and import bids from the Philasearch API.
---

# Philasearch Bids

Handler: `ServerPhilasearchBidMigrate` — extends `ServerBidMigrateBase`.

Unlike the other bid handlers, Philasearch is **API-based**: the migration source is a JSON endpoint, not a CSV — there is **no Google Sheet to configure**. The handler is only invoked through an AQ task.

## Required Variables

| Variable | Purpose |
|---|---|
| `server_bid_philasearch_api_key` | Required — used to authenticate the API request. Throws if missing. |
| `server_bid_philasearch_api_last_fetch` | UNIX timestamp of the last successful fetch. Used as the `from` cursor. |
| `server_bid_philasearch_menu_secret` | Shared secret used to compute the one-time URL token. |
| `server_bid_import_philasearch_username` | Author for the imported bids (defaults to `Philasearch`). Auto-created with Clerk permission if missing. |

The handler constructs a one-time URL of the form:

```
/admin/philasearch-bids/{sale_nid}/{api_key}/{last_timestamp}/{one_time_token}
```

…and reads bids from `MigrateSourceJSON`.

## Source JSON Format

Each bid carries at minimum:

| Field | Description |
|---|---|
| `bidId` | Source unique ID (used as the migration key) |
| `custNo` | Philasearch customer number |
| `orderTime` | Bid timestamp |
| `saleNo`, `lotNo`, `supNo`, `posNo`, `orderNo` | Sale / lot information |
| `bidType`, `bidAmount` | Bid value |
| `email` | Bidder email |
| `info.comment` | Optional bidder comment — logged and marks the map row with `STATUS_OK_WITH_INFO` |
| `client.internalInfo`, `client.shippingAddress` | Extra info attached to the bidder; logged and triggers the same flag |
| `client.*` | Full client payload used to seed the back-office missing-bidder UI when the client can't be matched. |

## Destination Mapping

| Source | Destination |
|---|---|
| `lotNo` | `lot` |
| `bidAmount` | `amount` |
| `sale_uuid` | `sale_uuid` |
| `email` | `email` |

When the bid server reports `BID_CLIENT_MISSING`, the row is stored with `STATUS_MISSING_CLIENT` and the full `client_data` JSON is kept on the map row, including the `platform: 'Philasearch'` tag and `custNo` as `external_id`.

## Notes

* The handler overrides `import()` to merge `STATUS_OK_WITH_INFO` and other map states properly per row.
* Errors thrown by the source (e.g. an API timeout) abort the whole run — they are logged as `WATCHDOG_ERROR` against `server_migrate`.
