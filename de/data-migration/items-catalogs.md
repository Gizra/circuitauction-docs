<!-- i18n source=data-migration/items-catalogs.md sha=052495bd55c0 -->
---
description: Katalogverweise (Multifield) an bestehende Lose anhängen.
---

# Item Catalogs

Handler: `ServerItemDriveCatalogsMigrate`.

Importiert Zeilen in das **Multifield** `field_catalog` der Losknoten. Jede Zeile legt einen Katalogeintrag (Katalogverweis, Katalognummer, Sortiertext) am Ziellos an.

## Ausführung über das Backoffice

Öffnen Sie die Auktion und gehen Sie zu **Item Import → Kataloge**. Der Reiter funktioniert wie der Import [Items (Self-Service)](items.md):

1. Fügen Sie die Google-Sheet-URL in das Textfeld **Google drive file URL** ein — der normale `edit`-Link genügt, er wird automatisch in die CSV-Exportform umgewandelt — oder laden Sie stattdessen eine CSV-Datei hoch.
2. Klicken Sie auf **Importelemente in die Warteschlange stellen**. Der Import läuft im Hintergrund; die Zeilen werden den Losen der **aktuellen Auktion** über `_internal_id` zugeordnet (es sei denn, das Sheet enthält eine explizite `_item`-NID).
3. Klicken Sie auf **Load Results**, um den Status je Zeile und Fehlermeldungen zu sehen, und auf **Queue failed import items**, um nur die fehlgeschlagenen Zeilen zu wiederholen.

## Quelldatei

Wird im Reiter keine URL / Datei angegeben, wird die Datei aus der Variable `migrate_items_csv` gelesen (gemeinsam mit dem Handler [Items (Self-Service)](items.md) genutzt — der ältere Ablauf für die gesamte Website). Eine gespeicherte URL muss die CSV-Form sein, nicht der normale `edit`-Link:

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
| `_item` | Ziellos — NID. Ist sie leer, wird das Los aus `_internal_id` ermittelt (im Ablauf pro Auktion auf die Auktion begrenzt) und ersatzweise über die Zuordnung der Lose-Migration (`migrate_map_serveritemsdrivemigrate`) anhand von `_unique_id` |
| `_internal_id` | Interne Los-ID, wird zum Auffinden des Loses verwendet, wenn `_item` leer ist |
| `_catalog_name` | Katalogname — erforderlich (leere Zeilen werden übersprungen) — wird einem Term der Taxonomie `catalogs` zugeordnet (automatisch angelegt) und in `field_catalog_ref` gespeichert |
| `_catalog_number` | `field_catalog_number` |
| `_ordering_sort` | `field_sort_text` |

{% hint style="info" %}
Der Katalog-Term der Taxonomie wird während des Migrationslaufs zwischengespeichert, sodass ein einzelner Katalogname nur einmal ermittelt / angelegt wird.
{% endhint %}
