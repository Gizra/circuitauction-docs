<!-- i18n source=data-migration/external-ids.md sha=dc06bb1f2d2c -->
---
description: Externe System-IDs (Multifield) an bestehende Kunden anhängen.
---

# External IDs

Handler: `ServerExternalIdsDriveMigrate`.

Importiert Zeilen in das **Multifield** `field_external_ids` der Kundenknoten. Jede Zeile erfasst ein Paar `(system, id)`, wodurch Kunden mit externen Plattformen (Philasearch, Delcampe, SAN usw.) abgeglichen werden können.

Konfiguriert über die Drupal-Variable `migrate_clients_external_ids_csv`.

## Quelldatei

Tragen Sie die **CSV-Export-URL** Ihres Google Sheets in der Variable `migrate_clients_external_ids_csv` ein. Die URL muss die CSV-Form sein, nicht der normale `edit`-Link:

```
https://docs.google.com/spreadsheets/d/<SPREADSHEET_ID>/export?format=csv&gid=<SHEET_GID>
```

Die zugehörige Bearbeiten-URL (Ursprung) sieht so aus:

```
https://docs.google.com/spreadsheets/d/<SPREADSHEET_ID>/edit?gid=<SHEET_GID>#gid=<SHEET_GID>
```

## Spalten

| Spalte | Ziel |
|---|---|
| `_unique_id` | ID zur Zeilenverfolgung (erforderlich) |
| `_customer_id` | Wird verwendet, um den zugehörigen Kunden über `server_client_get_client_nid_by_customer_id()` zu finden. Zeilen ohne Treffer werden übersprungen. |
| `_external_id` | `field_id` |
| `_external_system` | Legt automatisch einen Term der Taxonomie `external_systems` an und weist ihn `field_system` zu |

Der Handler setzt voraus, dass `ServerClientsMigrate` bereits ausgeführt wurde.
