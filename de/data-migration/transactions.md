<!-- i18n source=data-migration/transactions.md sha=bf412c4b8200 -->

# Vorgänge

Handler: `ServerTransactionsDriveMigrate`.

Erstellt `transaction`-Knoten und hängt sie an die Bestellung eines bestehenden Loses an.

Konfiguriert über die Drupal-Variable `migrate_transaction_csv`.

## Quelldatei

Tragen Sie die **CSV-Export-URL** Ihres Google Sheets in der Variable `migrate_transaction_csv` ein. Die URL muss die CSV-Form sein, nicht der normale `edit`-Link:

```
https://docs.google.com/spreadsheets/d/<SPREADSHEET_ID>/export?format=csv&gid=<SHEET_GID>
```

Die zugehörige Bearbeiten-URL (Ursprung) sieht so aus:

```
https://docs.google.com/spreadsheets/d/<SPREADSHEET_ID>/edit?gid=<SHEET_GID>#gid=<SHEET_GID>
```

## Übersprungene Zeilen

* Zeilen mit `_status == 'Declined'` werden ohne weitere Prüfung übersprungen.
* Zeilen, bei denen das zugehörige Los, der Losverlauf oder die Bestellung nicht ermittelt werden kann, werden mit einer Meldung übersprungen.

## Ermittlung des Loses

Der Handler ermittelt das Los in dieser Reihenfolge:

1. Über `_id` (direkt).
2. Über `_item_ref` — eine Zeichenfolge in freier Form. Die erste Zahl nach `AW` wird extrahiert (`AW1234` → `1234`); andernfalls wird die erste Ziffernfolge verwendet.

Vom ermittelten Los aus geht der Handler zum letzten veröffentlichten `item_history`, liest daraus `field_order` und verwendet den Eigentümer der Bestellung als Kunden.

## Spaltenzuordnung

| Spalte | Ziel |
|---|---|
| `_internal_id` / `_item_ref` | Suche des Loses (siehe oben) |
| `_status` | Filter — `Declined` überspringt die Zeile |
| `_bank_account` | `field_bank_account` (legt den Term des Bankkontos automatisch an) |
| `_info` | `field_info` |
| `_amount` | `field_amount` |
| `_date` | `field_transaction_date` **und** der Zeitstempel `created` des Knotens (geparst über `strtotime()`) |
| `_order` (ermittelt) | `field_order` |
| `_client` (aus dem Eigentümer der Bestellung ermittelt) | `field_client` |

{% hint style="info" %}
Eine Käuferrechnung über viele Lose entspricht einer einzigen **Bestellung** (eine Bestellung pro Auktion + Käufer). Eine Zahlung ist eine Transaktionszeile, die auf die `_internal_id` eines beliebigen Loses verweist — sie wird der gemeinsamen Bestellung zugeordnet, sodass die Abrechnung auf Bestellebene abgeglichen wird. Senden Sie pro Zahlung eine Transaktionszeile; für Genauigkeit auf Positionsebene senden Sie mehrere Zeilen, die alle in dieselbe Bestellung einfließen.
{% endhint %}

{% hint style="warning" %}
**Geplant (Auszahlungen an Einlieferer):** `field_order` akzeptiert bereits eine Referenz auf `consignment_statement` ebenso wie auf `order`. Eine geplante Änderung ergänzt dieses Sheet um eine Spalte für die Einlieferungs-ID, damit eine Zeile eine Abrechnung der Einlieferung ermitteln (über `server_consignment_statement_get_or_create()`) und `field_order` darauf zeigen lassen kann — analog dazu, wie Käuferzahlungen heute `_internal_id` → Bestellung auflösen. So können Zahlungen an Einlieferer (`StatementPayment`) über denselben Transaktionsimport laufen; ein separater Handler für Auszahlungen ist nicht nötig.
{% endhint %}
