---
description: Import consignment nodes.
---

# Consignments

Handler: `ServerConsignmentsDriveMigrate` — extends `ServerConsignmentsMigrate`.

Thin CSV wrapper around the base `ServerConsignmentsMigrate` handler. It only changes the source to a CSV file and removes the dependencies for standalone use; the column mapping and prepare logic come from the parent class.

Configured via the `migrate_consignments_csv` Drupal variable.

## Source File

Set the **CSV export URL** of your Google Sheet in the `migrate_consignments_csv` variable. The URL must be the CSV form, not the regular `edit` link:

```
https://docs.google.com/spreadsheets/d/<SPREADSHEET_ID>/export?format=csv&gid=<SHEET_GID>
```

The corresponding edit URL (origin) looks like:

```
https://docs.google.com/spreadsheets/d/<SPREADSHEET_ID>/edit?gid=<SHEET_GID>#gid=<SHEET_GID>
```

{% hint style="info" %}
In most cases consignments don't need to be migrated separately — the [Items (Self-Service)](items.md) handler will auto-create the consignment from the `_consignment` field of the items sheet. Use this handler only when you want to import consignments ahead of (or independently from) the items.
{% endhint %}

## Related

* [Consignment Finder Fees](consignment-finder-fees.md) — attach finder fees to existing consignments.
