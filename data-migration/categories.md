---
description: Import the categories taxonomy with hierarchy and translations.
---

# Categories

Handler: `ServerCategoriesDriveMigrate`.

Imports terms into the `categories` vocabulary. Designed to be re-runnable: existing terms are matched by their `field_hk_cat_id` value (set from `_hk_id` in the CSV), so a second run updates the same terms rather than creating duplicates.

Configured via the `migrate_categories_csv` Drupal variable. If unset, the handler falls back to the bundled `data/csv/taxonomy_term/categories_philately.csv` file shipped with the module.

**Default source:** [https://docs.google.com/spreadsheets/d/1I-TVXkBx3_wnVDEsCbxRu99rO0BFHnmCVtMVTKcOsYk/edit#gid=1962137688](https://docs.google.com/spreadsheets/d/1I-TVXkBx3_wnVDEsCbxRu99rO0BFHnmCVtMVTKcOsYk/edit#gid=1962137688)

## Source File

Set the **CSV export URL** of your Google Sheet in the `migrate_categories_csv` variable. The URL must be the CSV form, not the regular `edit` link:

```
https://docs.google.com/spreadsheets/d/<SPREADSHEET_ID>/export?format=csv&gid=<SHEET_GID>
```

The corresponding edit URL (origin) looks like:

```
https://docs.google.com/spreadsheets/d/<SPREADSHEET_ID>/edit?gid=<SHEET_GID>#gid=<SHEET_GID>
```

## Columns

| Column | Destination |
|---|---|
| `__id` | Row tracking ID (required) |
| `_hk_id` | `field_hk_cat_id` — primary key used to find existing terms |
| `_pwp_country` | `field_philasearch_id` |
| `_pwp_unterkat` | `field_phila_sub_id` |
| `_name_{language}` | Term name in the given language (`_name_en`, `_name_he`, …). The site's default language populates the term `name`. |
| `_label_for_catalog_{language}` | `field_label_for_catalogue` in the given language |
| `_weight` | Term weight |
| `_cantalogue_context` | `field_category_context` |
| `_heading_level_in_catalog` (configurable) | `field_heading_level_in_catalog`. The source column is read from `server_migrate_categories_heading_level_in_catalog_column`. |
| `parent_hk_id` (configurable) | Hierarchical parent lookup. The source column name is read from `server_migrate_categories_parent_id_column`. The handler resolves it to the parent term's `tid` via `field_hk_cat_id`. |

{% hint style="info" %}
Default matching (by term name) is disabled — terms are matched only by `field_hk_cat_id`. Two different HK IDs with the same name are intentionally allowed to coexist.
{% endhint %}

A term that references itself as its parent (`parent_hk_id` resolves to the same `tid`) is silently kept un-parented; a notice is queued for visibility.
