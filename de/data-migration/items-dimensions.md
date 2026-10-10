<!-- i18n source=data-migration/items-dimensions.md sha=9927389f5687 -->

# Los-Dimensionen

Handler: `ServerItemDriveDimensionsMigrate`.

Importiert Zeilen in das **Multifield** `field_dimensions` der Losknoten. Jede Zeile erfasst eine Verpackungsart, eine Nummer auf dem Karton und ein Gewicht.

## Ausführung über das Backoffice

Öffnen Sie die Auktion und gehen Sie zu **Item Import → Dimensionen**. Der Reiter funktioniert wie der Import [Lose (Self-Service)](/de/data-migration/items.md):

1. Fügen Sie die Google-Sheet-URL in das Textfeld **Google drive file URL** ein — der normale `edit`-Link genügt, er wird automatisch in die CSV-Exportform umgewandelt — oder laden Sie stattdessen eine CSV-Datei hoch.
2. Klicken Sie auf **Importelemente in die Warteschlange stellen**. Der Import läuft im Hintergrund; die Zeilen werden den Losen der **aktuellen Auktion** über `_internal_id` zugeordnet (es sei denn, das Sheet enthält eine explizite `_item`-NID).
3. Klicken Sie auf **Load Results**, um den Status je Zeile und Fehlermeldungen zu sehen, und auf **Queue failed import items**, um nur die fehlgeschlagenen Zeilen zu wiederholen.

## Quelldatei

Wird im Reiter keine URL / Datei angegeben, wird die Datei aus der Variable `migrate_items_csv` gelesen (gemeinsam mit dem Handler [Lose (Self-Service)](/de/data-migration/items.md) genutzt — der ältere Ablauf für die gesamte Website). Eine gespeicherte URL muss die CSV-Form sein, nicht der normale `edit`-Link:

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
| `_item` | Ziellos — NID. Ist sie leer, wird die NID des Loses über `server_item_get_internal_id()` aus `_internal_id` ermittelt |
| `_internal_id` | Interne Los-ID, wird zum Auffinden des Loses verwendet, wenn `_item` leer ist |
| `_box_type` | Erforderlich — legt automatisch einen Term der Taxonomie `package_types` an und schreibt ihn in `field_package` |
| `_box_number` | `field_number_on_box` |
| `_weight` | `field_weight` |

{% hint style="warning" %}
Zeilen mit leerem `_box_type` werden übersprungen (mit einer Watchdog-Warnung). Stellen Sie daher sicher, dass jede Dimensionszeile einen Wert enthält.
{% endhint %}
