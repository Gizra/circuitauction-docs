<!-- i18n source=data-migration/items-sold-result.md sha=33b2345793b4 -->
---
description: Verkaufspreise importieren und Losverlaufsknoten für Zuschläge erstellen.
---

# Items Sold Result

Handler: `ServerItemsSoldResultDriveMigrate`.

Erstellt `item_history`-Knoten, die den Zuschlag für jedes Los festhalten — wird üblicherweise nach der Auktion ausgeführt, um Ergebnisse aus einem externen System zu importieren.

## Ausführung über das Backoffice

Öffnen Sie die Auktion und gehen Sie zu **Item Import → Verkaufsergebnisse**. Der Reiter funktioniert wie der Import [Items (Self-Service)](items.md):

1. Fügen Sie die Google-Sheet-URL in das Textfeld **Google drive file URL** ein — der normale `edit`-Link genügt, er wird automatisch in die CSV-Exportform umgewandelt — oder laden Sie stattdessen eine CSV-Datei hoch.
2. Klicken Sie auf **Importelemente in die Warteschlange stellen**. Der Import läuft im Hintergrund und ist auf die **aktuelle Auktion** begrenzt (Zeilen anderer Auktionen werden übersprungen).
3. Klicken Sie auf **Load Results**, um den Status je Zeile und Fehlermeldungen zu sehen, und auf **Queue failed import items**, um nur die fehlgeschlagenen Zeilen zu wiederholen.

## Quelldatei

Wird im Reiter keine URL / Datei angegeben, wird die Datei aus der Variable `migrate_items_sold_result_csv` gelesen (der ältere Ablauf für die gesamte Website). Eine gespeicherte URL muss die CSV-Form sein, nicht der normale `edit`-Link:

```
https://docs.google.com/spreadsheets/d/<SPREADSHEET_ID>/export?format=csv&gid=<SHEET_GID>
```

Die zugehörige Bearbeiten-URL (Ursprung) sieht so aus:

```
https://docs.google.com/spreadsheets/d/<SPREADSHEET_ID>/edit?gid=<SHEET_GID>#gid=<SHEET_GID>
```

## Erforderliche Spalten

| Spalte | Beschreibung |
|---|---|
| `_unique_id` | ID zur Zeilenverfolgung (erforderlich) |
| `_internal_id` | Interne Los-ID — wird verwendet, um das Los innerhalb der Auktion zu finden |
| `_sale` | NID der Auktion (oder ersatzweise `_sale_number`) |
| `_sale_number` | Auktionsnummer — wird in eine Auktions-NID aufgelöst, wenn `_sale` nicht angegeben ist |
| `_sold_for` | Zuschlagspreis. Leer / 0 → das Los wird als UNSOLD markiert. Negativ → erzeugt eine Bestellung als Gutschrift. |
| `_wining_bidder_email` | E-Mail-Adresse des Höchstbietenden (muss bereits als Kunde existieren) |
| `_bidder_alias` | Optionaler Alias, der festgehalten wird |
| `_withdrawn` | Wird auf `FALSE` erzwungen |
| `_under_extension_status` | Standard ist `NOT_REQUESTED` |

## Verarbeitungslogik

Für jede Zeile geht der Handler wie folgt vor:

1. Er sucht das Los über `_internal_id` innerhalb der ermittelten Auktion. Zeilen ohne Treffer werden übersprungen.
2. Er ermittelt die Abrechnung der Einlieferung über `server_consignment_statement_get_or_create()` für die Einlieferung des Loses.
3. Ist `_sold_for` gesetzt:
   * Er sucht den Höchstbietenden über die E-Mail-Adresse. Fehlt er, wird die Zeile übersprungen.
   * Er legt den passenden `order`-Knoten an (oder ruft ihn ab) — Typ `bidder`, bzw. `credit_note`, wenn `_sold_for` negativ ist.
   * Er setzt `field_sold_status` auf `SOLD`.
4. Andernfalls setzt er `field_sold_status` auf `UNSOLD`.

Der neu erstellte Losverlaufseintrag wird als der **hervorgehobene** (promoted) gesetzt, und der bisher hervorgehobene Losverlauf desselben Loses wird zurückgestuft.

## Zuordnung der Zielfelder

| Quellspalte | Zielfeld |
|---|---|
| `_item` (intern ermittelt) | `field_item` |
| `_order` (intern ermittelt) | `field_order` |
| `_cs` (intern ermittelt) | `field_consignment_statement` |
| `_wining_bidder` (intern ermittelt) | `field_winner_bidder` |
| `_bidder_id` | `field_sold_to_bidder_id` |
| `_bidder_alias` | `field_bidder_alias` |
| `_withdrawn` | `field_withdrawn` — Hinweis: `prepareRow()` erzwingt derzeit `FALSE`, sodass der CSV-Wert ignoriert wird und dieser Handler einen Auftritt nicht als zurückgezogen markieren kann. |
| `_under_extension_status` | `field_under_extension_status` |
| `_sold_for` | `field_sold_for_amount` |
| `_sold_status` | `field_sold_status` (Standard `SOLD`) |

{% hint style="info" %}
`ServerItemsUpdateDriveMigrate` und `ServerItemsSelfServiceMigrate` stellen beide ebenfalls eine Aufgabe für den Losverlauf in die Warteschlange, wenn `_sold_for` in einer Zeile gesetzt ist — dieser Handler ist das Äquivalent, das aus einer dedizierten CSV läuft.
{% endhint %}

{% hint style="warning" %}
**Geplant:** Die Suche des Höchstbietenden erfolgt derzeit **nur über die E-Mail-Adresse** (`_wining_bidder_email`) und überspringt die Zeile, wenn es keinen Treffer gibt. Eine geplante Änderung ergänzt einen Ersatz über `_customer_id` (über `server_client_get_client_nid_by_customer_id()`, denselben Resolver, den jeder andere kundenbezogene Handler verwendet), sodass Gewinner über die Kunden-ID zugeordnet werden können, wenn eine E-Mail-Adresse fehlt oder nicht passt. Bis dahin braucht jede verkaufte Zeile eine auflösbare E-Mail-Adresse des Gewinners.
{% endhint %}
