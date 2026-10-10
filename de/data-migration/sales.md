<!-- i18n source=data-migration/sales.md sha=f56499e36f04 -->
---
description: Auktionsknoten importieren.
---

# Auktionen

Handler: `ServerSalesDriveMigrate` — erweitert `ServerSalesMigrate`.

Dünner CSV-Wrapper um den Basis-Handler `ServerSalesMigrate`. Er ändert lediglich die Quelle auf eine CSV-Datei und entfernt die Migrationsabhängigkeiten; die eigentliche Spaltenzuordnung und Verarbeitungslogik stammen aus der Elternklasse.

Konfiguriert über die Drupal-Variable `migrate_sales_csv`.

## Quelldatei

Tragen Sie die **CSV-Export-URL** Ihres Google Sheets in der Variable `migrate_sales_csv` ein. Die URL muss die CSV-Form sein, nicht der normale `edit`-Link:

```
https://docs.google.com/spreadsheets/d/<SPREADSHEET_ID>/export?format=csv&gid=<SHEET_GID>
```

Die zugehörige Bearbeiten-URL (Ursprung) sieht so aus:

```
https://docs.google.com/spreadsheets/d/<SPREADSHEET_ID>/edit?gid=<SHEET_GID>#gid=<SHEET_GID>
```

{% hint style="info" %}
Auktionen werden in der Regel manuell im Backoffice angelegt. Dieser Handler ist vor allem nützlich, wenn eine neue Installation aus einem externen System aufgebaut wird — z. B. beim Import eines Altbestands historischer Auktionen.
{% endhint %}

## Spalten

| Spalte | Ziel |
|---|---|
| `_id` | ID zur Zeilenverfolgung (erforderlich). Wird auch als `field_item_images_dir` gespeichert — der Name des Bilderordners pro Auktion, der beim Synchronisieren der Losbilder verwendet wird. |
| `_title_en` (+ `_title_{language}`) | `title` der Auktion / übersetztes `title_field`. Der englische Wert setzt den Titel des Knotens; andere Sprachen werden nur angewendet, wenn eine zweite Sprache konfiguriert ist. |
| `_body_en` (+ `_body_{language}`) | `body` |
| `_subtitle_en` (+ `_subtitle_{language}`) | `field_subtitle` |
| `_sale_number` | `field_sale_number` — die für Menschen lesbare Auktionsreferenz (z. B. `254`). Muss eindeutig sein; nachgelagerte Importe von Losen / Verkaufsergebnissen / Transaktionen ermitteln die Auktion über exakte Übereinstimmung mit diesem Wert (der erste Treffer gewinnt). |
| `_sale` | `field_sale_number` — die Migrations-Referenz-ID aus der CSV der Auktionsmigration |
| `_sale_status` | `field_sale_status`. Standard ist **FINISHED**, wenn weggelassen — ideal für historische Auktionen. |
| `_live_start_date` | `field_live_sale_date` (geparst über `strtotime()`). |
| `_mail_date_from` | `field_mail_sale_date` (Beginn des Zeitfensters der schriftlichen Auktion). |
| `_mail_date_to` | `field_mail_sale_date:to` (Ende des Zeitfensters der schriftlichen Auktion). |
| `_sale_logo` | `field_sale_logo` — ein Dateiname, der im Verzeichnis der Migrations-Cover aufgelöst wird, oder `public://sale_images/<name>`, falls dort vorhanden. |

{% hint style="warning" %}
**Spalten für das Mail-Datum:** Die Umwandlung von Datum in Zeitstempel in `prepareRow()` arbeitet derzeit mit den Spaltennamen `_mail_start_date` / `_mail_end_date`, während die Feldzuordnung `_mail_date_from` / `_mail_date_to` liest. Klären Sie die genauen Kopfzeilennamen für das Mail-Datum mit dem Entwicklungsteam, bevor Sie sie befüllen, sonst werden die Mail-Daten möglicherweise nicht umgewandelt. `_live_start_date` wird durchgängig zugeordnet und umgewandelt.
{% endhint %}
