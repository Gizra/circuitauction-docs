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

## Commission Steps

A consignment's consignor commission is stored as one or more **commission steps** in the `field_commission_steps` multifield, each step being a commission rate that applies from a given amount (`field_step_from`) upward. The migration sets these up in three ways:

### Commission step type

The `_commission_steps_type` column maps to `field_commission_step_type`, which controls how the steps are interpreted:

| Value | Meaning |
|---|---|
| `single_lots` | Commission is calculated per lot. |
| `entire_collection` | Commission is calculated across the entire consignment / collection. |

### Default commission step (fallback)

When a consignment is imported **without** any commission steps — i.e. there is no row for it in the [Consignment Commission Steps](consignment-commission-steps.md) source and the field is empty — the handler applies a single default step automatically:

* **Rate:** taken from the site-wide `backoffice_consignor_commission_for_migrate` Drupal variable (default `10%`).
* **From amount:** `0`.

This guarantees every migrated consignment has a valid commission, so the consignment statement can be generated. If a consignment *does* have explicit steps coming from the multifield migration, the default is **not** applied and validation is skipped so the steps can be attached afterward.

### Explicit / multi-step commissions

To import more than one step (e.g. 10% from 0, then 5% from 10,000) use the dedicated [Consignment Commission Steps](consignment-commission-steps.md) multifield migration, which attaches steps to consignments that already exist.

When the [Items (Self-Service)](items.md) handler auto-creates a consignment, it sets a single step from the item sheet's `_commission` value (decimals below 1 are converted to a percentage) with step type `single_lots`.

## Related

* [Consignment Commission Steps](consignment-commission-steps.md) — attach multiple commission steps to existing consignments.
* [Consignment Finder Fees](consignment-finder-fees.md) — attach finder fees to existing consignments.
