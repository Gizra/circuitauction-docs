---
description: Import sale nodes.
---

# Sales

Handler: `ServerSalesDriveMigrate` — extends `ServerSalesMigrate`.

Thin CSV wrapper around the base `ServerSalesMigrate` handler. It only changes the source to a CSV file and removes the migration dependencies; the actual column mapping and processing logic come from the parent class.

Configured via the `migrate_sales_csv` Drupal variable.

## Source File

Set the **CSV export URL** of your Google Sheet in the `migrate_sales_csv` variable. The URL must be the CSV form, not the regular `edit` link:

```
https://docs.google.com/spreadsheets/d/<SPREADSHEET_ID>/export?format=csv&gid=<SHEET_GID>
```

The corresponding edit URL (origin) looks like:

```
https://docs.google.com/spreadsheets/d/<SPREADSHEET_ID>/edit?gid=<SHEET_GID>#gid=<SHEET_GID>
```

{% hint style="info" %}
Sales are usually created manually from the back-office. This handler is mostly useful when bootstrapping a new installation from an external system — e.g. importing a back-catalogue of historical sales.
{% endhint %}

## Columns

| Column | Destination |
|---|---|
| `_unique_id` | Row tracking ID (required). Also stored as `field_item_images_dir` — the per-sale image folder name used when syncing item images. |
| `_title_en` (+ `_title_{language}`) | Sale `title` / translated `title_field`. The English value sets the node title; other languages are only applied when a second language is configured. |
| `_body_en` (+ `_body_{language}`) | `body` |
| `_subtitle_en` (+ `_subtitle_{language}`) | `field_subtitle` |
| `_sale_number` | `field_sale_number` — the human auction reference (e.g. `Aug13`). Must be unique; downstream item / sold-result / transaction imports resolve the sale by exact match on this value (first match wins). |
| `_sale_status` | `field_sale_status`. Defaults to **FINISHED** when omitted — ideal for historical sales. |
| `_live_start_date` | `field_live_sale_date` (parsed via `strtotime()`). |
| `_mail_date_from` | `field_mail_sale_date` (start of the mail-sale window). |
| `_mail_date_to` | `field_mail_sale_date:to` (end of the mail-sale window). |
| `_sale_logo` | `field_sale_logo` — a filename resolved against the migrate covers directory, or `public://sale_images/<name>` if present there. |

{% hint style="warning" %}
**Mail-date columns:** the date-to-timestamp conversion in `prepareRow()` currently runs against the column names `_mail_start_date` / `_mail_end_date`, while the field mapping reads `_mail_date_from` / `_mail_date_to`. Lock the exact mail-date header names with the dev team before populating them, or the mail dates may not be converted. `_live_start_date` is mapped and converted consistently.
{% endhint %}
