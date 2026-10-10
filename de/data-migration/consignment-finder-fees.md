<!-- i18n source=data-migration/consignment-finder-fees.md sha=4c8d6c78f803 -->
---
description: Vermittlungsprovisions-Multifields an bestehende Einlieferungen anhängen.
---

# Vermittlungsprovisionen der Einlieferungen

Handler: `ServerConsignmentFinderFeesDriveMigrate`.

Importiert Zeilen in das **Multifield** `field_finder_fees` der Einlieferungsknoten. Jede Zeile erfasst einen Vermittler, einen Provisionssatz und das zugehörige Los.

Konfiguriert über die Drupal-Variable `migrate_items_csv` (gemeinsam mit dem Lose-Import genutzt).

## Quelldatei

Tragen Sie die **CSV-Export-URL** Ihres Google Sheets in der Variable `migrate_items_csv` ein (gemeinsam mit dem Handler [Lose (Self-Service)](items.md) genutzt). Die URL muss die CSV-Form sein, nicht der normale `edit`-Link:

```
https://docs.google.com/spreadsheets/d/<SPREADSHEET_ID>/export?format=csv&gid=<SHEET_GID>
```

Die zugehörige Bearbeiten-URL (Ursprung) sieht so aus:

```
https://docs.google.com/spreadsheets/d/<SPREADSHEET_ID>/edit?gid=<SHEET_GID>#gid=<SHEET_GID>
```

## Spalten

| Spalte | Verwendet als |
|---|---|
| `_unique_id` | ID zur Zeilenverfolgung (erforderlich) |
| `_finders_rate` | Erforderlich. Wird als Prozentwert in `field_commission` gespeichert — die Quelle muss eine Dezimalzahl sein (z. B. `0.05`), die beim Import mit 100 multipliziert wird. Zeilen mit leerem Wert werden übersprungen. |
| `_finders_fullname` | Erforderlich. Wird am ersten Leerzeichen aufgeteilt; der Handler sucht einen Kunden anhand von Vor- und Nachname. Zeilen, die auf mehr als einen Kunden (oder auf keinen) passen, werden übersprungen. |
| `_sale_number` | Wird verwendet, um die Auktion zu ermitteln (`server_sale_get_by_sale_number()`). |
| `_consignment_id` | Wird zusammen mit der ermittelten Auktion verwendet, um die Einlieferung zu finden (`server_consignment_get_by_consignment_id()`). Erforderlich. |
| `_internal_id` | Wird verwendet, um das zugehörige Los über `server_item_get_internal_id()` zu ermitteln. |

## Zuordnung zum Ziel

| Quelle | Ziel |
|---|---|
| `_host` (ermittelte NID der Einlieferung) | `host` |
| `_commission` (× 100 aus `_finders_rate`) | `field_commission` |
| `_finder` (ermittelte NID des Kunden) | `field_finder` |
| `_item` (ermittelte NID des Loses) | `field_item` |
