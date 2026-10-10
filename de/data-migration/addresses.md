<!-- i18n source=data-migration/addresses.md sha=233aecbec71c -->
---
description: Adressknoten importieren und an bestehende Kunden anhängen.
---

# Addresses

Handler: `ServerAddressesDriveMigrate`.

Erstellt `address`-Knoten und hängt sie an bestehende Kunden an. Die erste importierte Adresse pro Kunde wird als Standardadresse des Kunden gesetzt.

Konfiguriert über die Drupal-Variable `migrate_clients_address_csv`.

## Quelldatei

Tragen Sie die **CSV-Export-URL** Ihres Google Sheets in der Variable `migrate_clients_address_csv` ein. Die URL muss die CSV-Form sein, nicht der normale `edit`-Link:

```
https://docs.google.com/spreadsheets/d/<SPREADSHEET_ID>/export?format=csv&gid=<SHEET_GID>
```

Die zugehörige Bearbeiten-URL (Ursprung) sieht so aus:

```
https://docs.google.com/spreadsheets/d/<SPREADSHEET_ID>/edit?gid=<SHEET_GID>#gid=<SHEET_GID>
```

## Kundensuche

Der Handler ermittelt den Zielkunden in dieser Reihenfolge:

1. Über `_customer_id` (via `getClientRef()`).
2. Über `_email` (via `server_client_get_by_email()`).

Wird auf keinem der Wege ein Kunde gefunden, wird die Zeile mit einem Watchdog-Fehler übersprungen.

## Spalten

| Spalte | Verwendet als |
|---|---|
| `_unique_id` | ID zur Zeilenverfolgung (erforderlich) |
| `_customer_id` | Primäre Kundensuche |
| `_email` | Ersatz-Kundensuche |
| `salutation` | Wird in der Anrede des Kunden gespeichert (ein einzelner Bindestrich `-` gilt als leer) |
| `_attention` | Feld `care_of`. Ein vorangestelltes `c/o `-Präfix wird entfernt. |
| `_address1` | `thoroughfare` |
| `_address2`, `_address3` | Werden zu `premise` zusammengefügt (durch Leerzeichen getrennt) |
| `_city` | `locality` |
| `_state`, `_county` | `administrative_area` (Bundesstaat bevorzugt, Ersatz ist County) |
| `_county` | `county` |
| `_postal_code` | `postal_code` |
| `_country` | Normalisiert über `server_address_get_country_code()` |

## Verhalten der Standardadresse

Ist `field_default_address` beim Kunden leer (oder auf einen anderen Knoten gesetzt), wird die importierte Adresse als Standard zugewiesen. Validierungen und Prüfungen auf doppelte E-Mail-Adressen beim Kunden werden beim Speichern umgangen, damit die Aktualisierung möglich ist.

{% hint style="info" %}
Die grundlegenden Prüfungen des Adresstyps (`server_address_node_presave`) werden während der Migration über `noAddressTypeChecks` am Knoten ausdrücklich deaktiviert.
{% endhint %}
