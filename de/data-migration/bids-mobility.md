<!-- i18n source=data-migration/bids-mobility.md sha=25287bf1c69a -->

# Auction-Mobility-Gebote

Handler: `ServerMobilityBidMigrate` — erweitert `ServerBidMigrateBase`.

Importiert Gebote aus einem Auction-Mobility-Export. Läuft als AQ-Aufgabe — übergeben Sie entweder eine `fid` (hochgeladene CSV) oder eine `drive_url` (Google Sheet, durch Komma getrennt).

Wird eine CSV direkt hochgeladen, verwendet der Handler standardmäßig ein **Semikolon** als Trennzeichen (Standard von Mobility).

## Quelldatei

Dieser Handler läuft als AQ-Aufgabe. Übergeben Sie entweder:

* `fid` — eine Drupal-Datei-ID, die auf die rohe Auction-Mobility-CSV verweist (durch Semikolon getrennt), oder
* `drive_url` — die **CSV-Export-URL** eines Google Sheets (durch Komma getrennt):

```
https://docs.google.com/spreadsheets/d/<SPREADSHEET_ID>/export?format=csv&gid=<SHEET_GID>
```

Die zugehörige Bearbeiten-URL (Ursprung) sieht so aus:

```
https://docs.google.com/spreadsheets/d/<SPREADSHEET_ID>/edit?gid=<SHEET_GID>#gid=<SHEET_GID>
```

Als Autor wird standardmäßig der Benutzer `Mobility` verwendet; fehlt er, wird er automatisch mit der Berechtigung Clerk angelegt (Variable `server_bid_import_mobility_username`).

## Erwartete Spalten

| Spalte | Verwendet als |
|---|---|
| `rowId` | Eindeutige ID der Quelle — wird als Migrationsschlüssel verwendet |
| `lotNumber`, `lotNumberExtension` | Los — zugeordnet zu `lot` |
| `soldPrice` | Betrag — zugeordnet zu `amount` |
| `status` | Zur Information |
| `winnerEmail` | E-Mail-Adresse des Bieters — erforderlich. Zeilen ohne E-Mail-Adresse werden übersprungen. |
| `winnerIsClerk`, `winnerPaddle`, `winnerNote`, `winnerName` | Werden verwendet, um Bieterinformationen abzuleiten |
| `winnerShippingAddress*`, `winnerPhoneNumber`, `winnerCreditCard*` | Werden verwendet, um die Daten eines fehlenden Kunden vorzubelegen |
| `type` | Optional. Wird dem Bietertyp zugeordnet — `mail`, `phone`, `floor`, sonst `website`. |

## Daten eines fehlenden Kunden

Kann der Gebotsserver den Bieter nicht zuordnen, wird die Zeile mit `STATUS_MISSING_CLIENT` gespeichert. Das JSON in `client_data` enthält Name, E-Mail-Adresse, Lieferadresse, Telefon und `"platform": "mobility"`, damit das Backoffice den Kunden bei Bedarf anlegen kann.

## Zuordnung des Bietertyps

| Wert von `type` | `bidderType` |
|---|---|
| `mail` | `mail` |
| `phone` | `phone` |
| `floor` | `floor` |
| alles andere / leer | `website` |
