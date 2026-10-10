<!-- i18n source=data-migration/bids.md sha=c468dfc3f41c -->

# Gebote

Handler: `ServerBidMigrate` — erweitert `ServerBidMigrateBase`.

Der generische Handler für den Gebotsimport. Er kann lesen aus:

* einer **CSV-Datei** (hochgeladen über `fid`) oder einem **Google Sheet** (über `drive_url`), oder
* einer **älteren SQL-Tabelle** (`_raw_bids`, verknüpft mit `_raw_bidpos` und `_raw_catalogpos`).

Der Autor der importierten Gebote muss ein bestehender Benutzer sein — der Benutzername wird aus der Variable `server_bid_import_bid_import_username` gelesen (Standard `admin`) und muss die Berechtigung **Clerk** besitzen. Fehlt der Benutzer, bricht die Migration ab.

## Allgemeine Variablen

| Variable | Zweck |
|---|---|
| `server_bid_import_sale_nid` | NID der Zielauktion — erforderlich. |
| `server_bid_import_bid_import_username` | Autor der importierten Gebote. Standard ist `admin`. |
| `server_bid_import_bid_import_table` | SQL-Quelltabelle, wenn keine CSV verwendet wird. Standard ist `_raw_bids`. |
| `server_bid_import_source_sale_id` | Filtert die ältere Tabelle nach Auktions-ID (Standard `1433`). |

## Quelldatei

Dieser Handler läuft als AQ-Aufgabe. Übergeben Sie entweder:

* `fid` — eine Drupal-Datei-ID (die Datei wird über eine vorsignierte S3-URL geladen und heruntergeladen), oder
* `drive_url` — die **CSV-Export-URL** eines Google Sheets:

```
https://docs.google.com/spreadsheets/d/<SPREADSHEET_ID>/export?format=csv&gid=<SHEET_GID>
```

Die zugehörige Bearbeiten-URL (Ursprung) sieht so aus:

```
https://docs.google.com/spreadsheets/d/<SPREADSHEET_ID>/edit?gid=<SHEET_GID>#gid=<SHEET_GID>
```

Die CSV ist durch Kommas getrennt. Wird weder `fid` noch `drive_url` angegeben, greift der Handler auf die ältere SQL-Quelle (`_raw_bids`) zurück.

## Zuordnung zum Ziel

| Quellspalte | Ziel |
|---|---|
| `lotNo` | `lot` |
| `totalBid` | `amount` |
| `roomBidNo` | `bidder_id` |
| `bidType` | `type` (zugeordnet zu `mail`, `floor`, `internet`) |
| `bidTime` | `created` |
| `contactNo` | `customer_number` |

## Zuordnung des Gebotstyps

| `bidType` der Quelle | Ergebnis |
|---|---|
| `0` | Gebot vom Typ `mail` |
| `5` | Gebot vom Typ `floor` — wird zu `internet` hochgestuft, wenn die Bieternummer `≥ 4000` ist |
| `3`, `10`, `999` | Übersprungen (null / doppelt / live gelöscht) |
| alles andere | Löst eine Ausnahme aus (unbekannter Typ) |

## Bietertyp nach Nummernbereich

Der Bereich von `bidder_id` bestimmt den Bietertyp:

| Bereich | Bietertyp |
|---|---|
| `< 300` | `floor_by_agent` |
| `< 400` | `phone` |
| `< 1000` | `floor` |
| `< 4000` | `mail` |
| `≥ 4000` | `website` |

## Kundenzuordnung

Für jede Zeile ermittelt der Handler den Kunden (`server_client_get_client_nid_by_customer_id`) und ruft auf dem Gebotsserver `server_bid_get_bidder_info()` auf. Kann der Kunde nicht zugeordnet werden, wird die Zeile mit `STATUS_MISSING_CLIENT` in der Zuordnungstabelle gespeichert, einschließlich Los, Betrag, Paddle und E-Mail-Adresse, damit die Oberfläche für fehlende Bieter sie später erneut verarbeiten kann.
