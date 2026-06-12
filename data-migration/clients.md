---
description: Import client nodes (buyers and consignors) from a Google Sheet.
---

# Clients

Handler: `ServerClientsDriveMigrate` — extends `ServerClientsMigrate`.

Imports `client` nodes from a CSV. The column mapping lives on the parent `ServerClientsMigrate` (documented below); the drive variant only adds the CSV source plus a small `prepareRow()` hook.

Configured via the `migrate_clients_csv` Drupal variable.

## Source File

Set the **CSV export URL** of your Google Sheet in the `migrate_clients_csv` variable. The URL must be the CSV form, not the regular `edit` link:

```
https://docs.google.com/spreadsheets/d/<SPREADSHEET_ID>/export?format=csv&gid=<SHEET_GID>
```

The corresponding edit URL (origin) looks like:

```
https://docs.google.com/spreadsheets/d/<SPREADSHEET_ID>/edit?gid=<SHEET_GID>#gid=<SHEET_GID>
```

## Required Fields

| Column | Used as |
|---|---|
| `_id` | Row tracking key. |

## Identity

| Column | Destination | Notes |
|---|---|---|
| `_first_name` | `field_first_name` | Auto-extracted from `_last_name` when empty if `server_migrate_split_lastname_column` is enabled. |
| `_last_name` | `field_last_name` | First space-separated token can be moved to `_first_name`, see above. |
| `_username` | `field_username` | |
| `_email` | `field_email` | Used as a lookup key; also drives duplicate handling. |
| `_secondary_email` | `field_secondary_email` | |
| `_salutation` | `field_salutation` | Taxonomy term, auto-created. |
| `_letter_salutation` | `field_letter_salutation` | Free text. |
| `_company` | `field_company` | |
| `_birthdate` | `field_birthdate` | Empty / `0` is unset. Otherwise reduced by 6 hours and stored as `Y-m-d` (timezone workaround). |
| `_customer_id` | `field_philaworksplace_id` | External / legacy customer id. Used to find existing clients in update mode. |

## Contact Info

| Column | Destination |
|---|---|
| `_phone` | `field_phone` |
| `_mobile` | `field_mobile` |
| `_fax` | `field_fax` |
| `_office_phone` | `field_office_phone` |
| `_website` | `field_client_website` — lowercased automatically in update mode |

## Preferences & Categorisation

| Column | Destination | Notes |
|---|---|---|
| `_interests` | `field_area_of_interests` | Pipe-separated taxonomy terms, auto-created. Each segment trimmed to 255 chars. |
| `_tags` | `field_client_tags` | Pipe-separated taxonomy terms, auto-created. Each segment trimmed to 255 chars. |
| `_source` | `field_client_source` | Pipe-separated taxonomy terms, auto-created. |
| `_default_payment_method` | `field_default_payment_type` | Resolved via the `ServerPaymentTypeMigrate` map; auto-created if missing. Each segment trimmed to 255 chars. |
| `_agent` | `field_agent` | Defaults to `FALSE`. |
| `_language` | `field_website_language` | Defaults to the site language; lowercased. |

## Tax & Billing

| Column | Destination | Notes |
|---|---|---|
| `_tax_type` | `field_tax_type` | Taxonomy term, auto-created. Each segment trimmed to 255 chars. |
| `_tax_id` | `field_tax_id` | |
| `_shipping_instructions` | `field_shipping_instructions` | |
| `_billing_instructions` | `field_billing_instructions` | |
| `_buyer_premium` | `field_bidder_commission` | Buyer's premium / bidder commission percentage. |
| `_country` | (used by downstream addresses logic) | Defaults to the value of `backoffice_order_default_country_for_tax` (`DE` if unset) when empty. |

## Status

| Column | Destination | Notes |
|---|---|---|
| `_status` | `field_user_status` | Defaults to `approved`. Only mapped when **not** in update-existing mode. |
| `_is_deleted` | `field_user_status` | When truthy on the row, status is forced to `deleted` (overrides `_status`). |
| `_warning` | `field_warning` | Free-form warning displayed in the back-office. |
| `_created` | `created` | Node creation timestamp. |
| `_cancellation_date` | `field_cancellation_date` | |

## Consignor Commission Steps (Multifield)

The handler builds a stepped consignor commission multifield (`field_consignor_commissions`) from numbered columns on the row:

| Column pair | Stored as |
|---|---|
| `_consignor_commission_1` + `_step_from_1` | First step (commission + threshold) |
| `_consignor_commission_2` + `_step_from_2` | Second step |
| `_consignor_commission_N` + `_step_from_N` | …and so on, scanned until a missing column is hit |

For each step:

* `_consignor_commission_N` is normalised to a percentage — if the value does not already contain `%`, it is cast to an int and a `%` is appended (e.g. `7` → `7%`).
* `_step_from_N` defaults to `0` when empty.
* Empty commission values skip the step.

The collected steps are written to `field_consignor_commissions` via the entity wrapper.

## Notes (Multi-column)

The handler creates `note` nodes attached to the client from up to four pipe-separated columns:

* `_notes`, `_notes2`, `_notes3`, `_notes4`

Each pipe segment becomes one note. Note titles are deterministic (`Migrate imported note <_unique_id> - <field><index>`) so a re-import does **not** create duplicates.

When `server_migrate_update_existing_notes` is on, existing notes with the same title are overwritten.

{% hint style="info" %}
For the `hr` installation, `_notes3` and `_notes4` numeric values are automatically prefixed with `Total Purchase - ` and `Credit Limit - ` respectively.
{% endhint %}

## Client References (SQL Only)

When the `_raw_client_references` SQL table exists, the `complete()` step populates `field_node_references` (a multifield) on each freshly imported client. Each reference row carries `_source_client`, `_destination_client` (NIDs resolved via `migrate_map_serverclientsmigrate`) and `_reference_type` (auto-created `relation_types` term).

References are imported only when **not** in update-existing mode, because the back-office relies on `hook_node_update` to mirror the relationship and that hook does not fire on an existing-node update path.

## Bypass Duplicates

When the `server_migrate_bypass_duplicates` variable is enabled, the drive variant skips any row whose `_email` already matches an existing client. Useful when re-importing a bids sheet that also carries client info — existing clients are left untouched.

## Update Existing

When `server_migrate_update_existing` is enabled, the handler switches into update mode:

* `systemOfRecord` becomes `DESTINATION` — only the mapped columns overwrite existing values.
* `_nid` becomes a mapped column.
* The matching strategy is controlled by `server_migrate_update_existing_find_by_key`:
  * `nid` *(default)* — lookup by `_philaworksplace_id` (customer id).
  * `emailphone` — lookup by `_email`.
* When no match is found, the handler falls back to a **phone-similarity search** on `field_phone`, then `field_mobile`, then `field_fax`. Multiple matches → row skipped with a watchdog warning.
* Final fallback: lookup in `migrate_map_serverclientsdrivemigrate` by `_unique_id`, then create an empty client when nothing matches.

## Duplicate Email Cleanup

When `server_migrate_update_existing_set_duplicate_to_delete` is on (default), every other client with the **same email** is set to `deleted` after the import. Useful when consolidating duplicate accounts during a migration.

## Splitting Full Name

When `_first_name` is empty and `server_migrate_split_lastname_column` is enabled, the handler splits `_last_name` on the first space and uses the leftmost token as `_first_name`. Useful when the source system stores the full name in a single column.

## Term Truncation

Every term name in `_interests`, `_default_payment_method`, `_tags`, `_salutation` and `_tax_type` is truncated to 255 characters per pipe segment. Truncations are logged to `server_migrate` watchdog.

## Related

* [Addresses](addresses.md) — attach address nodes to clients.
* [External IDs](external-ids.md) — attach external system IDs to clients.
* [Clients Update](clients-update.md) — update existing clients matched by email.
* [Clients Password](clients-password.md) — migrate password hashes.
