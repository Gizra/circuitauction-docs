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
Sales are usually created manually from the back-office. This handler is mostly useful when bootstrapping a new installation from an external system.
{% endhint %}
