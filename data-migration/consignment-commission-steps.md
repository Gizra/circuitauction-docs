---
description: Attach commission step multifields to existing consignments.
---

# Consignment Commission Steps

Handler: `ServerConsignmentCommissionStepsMigrate`.

Imports rows into the `field_commission_steps` **multifield** on consignment nodes. Each row records one commission step — a consignor commission rate that applies from a given amount upward. Use this handler when a consignment needs **more than one** step (tiered commission) or when you want explicit steps instead of the [default fallback step](consignments.md#default-commission-step-fallback).

Depends on [Consignments](consignments.md) (`ServerConsignmentsMigrate`) — the consignment nodes must be imported first so the steps can be attached to them.

## Source

The steps are read from the `_raw_consignment_commission_steps` table. When the `server_migrate_item_sale_number_to_import` variable is set, only steps for consignments of that sale are processed.

## Columns

| Column | Used as |
|---|---|
| `_unique_id` | Row tracking ID (required). |
| `_consignment` | The consignment the step belongs to, resolved through the `ServerConsignmentsMigrate` map. |
| `_commission` | The consignor commission rate for this step (stored in `field_consignor_commission`). |
| `_from_amount` | The amount from which this step's rate applies (stored in `field_step_from`). Use `0` for the first/base step. |

## Destination Mapping

| Source | Destination |
|---|---|
| `_consignment` (resolved consignment NID) | `host` |
| `_commission` | `field_consignor_commission` |
| `_from_amount` | `field_step_from` |

## Example

Two steps on the same consignment — 10% from 0, then a higher rate from 1,000:

| Unique Id | Consignment | Commission | From amount |
|---|---|---|---|
| `consignment_commission_step_1` | `consignment1` | `10` | `0` |
| `consignment_commission_step_2` | `consignment1` | `500` | `1000` |

## Related

* [Consignments](consignments.md) — import the consignment nodes these steps attach to (and the default single-step behavior).
