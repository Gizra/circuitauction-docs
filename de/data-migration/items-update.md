<!-- i18n source=data-migration/items-update.md sha=2e966dea1a3c -->

# Lose aktualisieren

Handler: `ServerItemsUpdateDriveMigrate`.

Dieser Handler aktualisiert **bestehende** Losknoten aus einer CSV. Anders als die reguläre Lose-Migration legt er keine neuen Lose an — findet er für eine Zeile kein passendes Los, wird die Zeile mit einer Meldung in der Ergebnistabelle übersprungen.

Konfiguriert über `migrate_items_update_csv` (Drupal-Variable). Ist `migrate_sale_reference_nid` gesetzt, liest der Handler stattdessen aus der SQL-Tabelle `_raw_item`, gefiltert nach Auktion.

## Quelldatei

Tragen Sie die **CSV-Export-URL** Ihres Google Sheets in der Variable `migrate_items_update_csv` ein. Die URL muss die CSV-Form sein, nicht der normale `edit`-Link:

```
https://docs.google.com/spreadsheets/d/<SPREADSHEET_ID>/export?format=csv&gid=<SHEET_GID>
```

Die zugehörige Bearbeiten-URL (Ursprung) sieht so aus:

```
https://docs.google.com/spreadsheets/d/<SPREADSHEET_ID>/edit?gid=<SHEET_GID>#gid=<SHEET_GID>
```

{% hint style="info" %}
Intern wird `Migration::DESTINATION` als führendes System verwendet: Es werden nur die von diesem Handler zugeordneten Spalten geschrieben; alle anderen Felder behalten ihren aktuellen Wert.
{% endhint %}

## Zuordnungsstrategie

Der Handler versucht in dieser Reihenfolge, ein bestehendes Los zuzuordnen:

1. **`_nid`** - direkte Knoten-ID
2. **`_lot_number` + `_lot_letter` + `_sale`** - Suche über die Losnummer innerhalb einer Auktion
3. **`_internal_id` (+ `_sale`)** - Suche über die interne Los-ID
4. **`_consignment` + `_position_of_consignment`** - bildet eine interne ID wie `consignment_id` + mit Nullen aufgefüllte Position

Wird über keinen dieser Wege ein bestehendes Los gefunden, wird die Zeile mit der Meldung „No item found“ verworfen.

## Aktualisierbare Felder

| Spalte | Aktualisiertes Feld |
|---|---|
| `_language` | Sprache des Loses (Standard ist die Standardsprache der Website) |
| `_internal_id` | `field_internal_id` |
| `_position_of_consignment` | `field_position_of_consignment` |
| `_title_{lang}` | `title` / `title_field` |
| `_body_{lang}` | `body` (filtered_html) |
| `_opening_price` | `field_opening_price` |
| `_minimum_price` | `field_minimum_price` |
| `_estimation_high` | `field_estimate_high` |
| `_estimation_low` | `field_estimate_low` |
| `_main_category` | `field_category` (durch Pipe getrennt oder über die Kategorien-Migration, wenn `server_migrate_map_categories_from_migrate` aktiviert ist) |
| `_main_category_id` | `field_category` über die Suche nach der Philaworksplace-ID |
| `_symbol_ids` | `field_symbols` (durch Pipe getrennt, zugeordnet über `ServerSymbolsMigrate`) |
| `_sub_symbol_id` | `field_sub_symbol` (zugeordnet über `ServerSubSymbolsMigrate`) |
| `_search_tag` | `field_search_tags` |
| `_item_type` | `field_item_type` (Standard `single`) |
| `_thematics` | `field_thematics` |
| `_sold_for` | `field_sold_for_amount` — löst außerdem die Erstellung einer Aufgabe für den Losverlauf aus (siehe [Zuschlagsergebnisse der Lose](/de/data-migration/items-sold-result.md)) |
| `_responsible_clerk` | Legt den zuständigen Clerk fest |
| `_catalog_part` | Legt den Term `field_catalogue_part` an / setzt ihn |
| `_lot_number` | Überschreibt `field_lot_number` |
| `_title_{secondary_lang}` | Übersetzter Titel für die konfigurierte zweite Sprache |
| `_body_{secondary_lang}` | Übersetzter Text für die konfigurierte zweite Sprache |

{% hint style="info" %}
Standardmäßig bricht der Handler nach der Aktualisierung der „oberen“ Felder (Losnummer, Titel, Text, Kategorien) vorzeitig ab. Um die vollständige Zuordnung zu verarbeiten, deaktivieren Sie die Variable `server_migrate_update_item_early_return`.
{% endhint %}

## Verhalten bei mehreren Sprachen

Die konfigurierte zweite Sprache wird aus der Variable `migrate_items_csv_second_language` gelesen. Sind die entsprechenden Spalten `_title_{lang}` / `_body_{lang}` in der CSV vorhanden, schreibt der Handler sie in die übersetzten Wrapper.

Für Kategorien gilt: Ist `server_migrate_force_category_translation_update` aktiviert, werden bestehende Terme mit dem übersetzten Namen aus der CSV aktualisiert.
