<!-- i18n source=data-migration/bids-delcampe.md sha=ba85d09745bb -->

# Delcampe-Gebote

Handler: `ServerDelcampeBidMigrate` — erweitert `ServerBidMigrateBase`.

Importiert Gebote aus einem Delcampe-Export. Läuft als AQ-Aufgabe — übergeben Sie entweder eine `fid` (hochgeladene CSV) oder eine `drive_url` (Google Sheet).

Die CSV verwendet **Semikolons** als Trennzeichen (Standard von Delcampe). Beim Import aus einem Google Sheet (über `drive_url`) werden Kommas verwendet.

## Quelldatei

Dieser Handler läuft als AQ-Aufgabe. Übergeben Sie entweder:

* `fid` — eine Drupal-Datei-ID, die auf die rohe Delcampe-CSV verweist (durch Semikolon getrennt), oder
* `drive_url` — die **CSV-Export-URL** eines Google Sheets (durch Komma getrennt):

```
https://docs.google.com/spreadsheets/d/<SPREADSHEET_ID>/export?format=csv&gid=<SHEET_GID>
```

Die zugehörige Bearbeiten-URL (Ursprung) sieht so aus:

```
https://docs.google.com/spreadsheets/d/<SPREADSHEET_ID>/edit?gid=<SHEET_GID>#gid=<SHEET_GID>
```

Als Autor wird standardmäßig der Benutzer `Delcampe` verwendet; fehlt er, wird er automatisch mit der Berechtigung Clerk angelegt (Variable `server_bid_import_delcampe_username`).

## Erwartete Spalten

| Spalte | Verwendet als |
|---|---|
| `Catalogus`, `Ttitel`, `Datum`, `Munteenheid`, `Koper` | Zur Information |
| `Referentie` | Los — zugeordnet zu `lot` |
| `Bedrag` | Betrag — zugeordnet zu `amount` |
| `E-mail` | E-Mail-Adresse des Bieters — zugeordnet zu `email` |
| `Naam` | Wird verwendet, um Vor- und Nachnamen für die Daten eines fehlenden Kunden abzuleiten |
| `Adres`, `Postcode`, `Stad`, `Regio`, `Land`, `Telefoon` | Werden verwendet, um die Daten eines fehlenden Kunden vorzubelegen |

Der eindeutige Schlüssel pro Zeile lautet `<Referentie>-<E-mail>-<Bedrag>`.

## Daten eines fehlenden Kunden

Kann der Gebotsserver den Bieter nicht zuordnen, wird die Zeile mit `STATUS_MISSING_CLIENT` und folgendem JSON in `client_data` gespeichert:

```json
{
  "firstname": "...",
  "lastname": "...",
  "email": "...",
  "zip": "...",
  "address": "...",
  "city": "...",
  "state": "...",
  "country": "...",
  "phone": "...",
  "platform": "delcampe"
}
```

Diese Daten verwendet die Oberfläche für fehlende Bieter im Backoffice, um den Kunden bei Bedarf anzulegen.
