<!-- i18n source=data-migration/bids-san.md sha=1247eb7b3f5d -->

# SAN-Gebote

Handler: `ServerSANBidMigrate` — erweitert `ServerBidMigrateBase`.

Importiert Gebote aus einem SAN-Export. Läuft als AQ-Aufgabe — übergeben Sie entweder eine `fid` (hochgeladene CSV) oder eine `drive_url` (Google Sheet). Die CSV ist durch Kommas getrennt.

## Quelldatei

Dieser Handler läuft als AQ-Aufgabe. Übergeben Sie entweder:

* `fid` — eine Drupal-Datei-ID, die auf die rohe SAN-CSV verweist (durch Komma getrennt), oder
* `drive_url` — die **CSV-Export-URL** eines Google Sheets:

```
https://docs.google.com/spreadsheets/d/<SPREADSHEET_ID>/export?format=csv&gid=<SHEET_GID>
```

Die zugehörige Bearbeiten-URL (Ursprung) sieht so aus:

```
https://docs.google.com/spreadsheets/d/<SPREADSHEET_ID>/edit?gid=<SHEET_GID>#gid=<SHEET_GID>
```

Als Autor wird standardmäßig der Benutzer `SAN` verwendet; fehlt er, wird er automatisch mit der Berechtigung Clerk angelegt (Variable `server_bid_import_san_username`).

## Erwartete Spalten

| Spalte | Verwendet als |
|---|---|
| `CustNo` | Kundennummer der Quelle — wird als `external_id` in den Daten des fehlenden Kunden gespeichert |
| `lName`, `fName` | Name |
| `Handle`, `Paddle` | Optionale Paddle-Daten |
| `Email`, `EMAIL2` | E-Mail-Adresse des Bieters |
| `SaleNo` | Zur Information |
| `LotNo` | Los — zugeordnet zu `lot` |
| `Amount` | Betrag — zugeordnet zu `amount` |
| `BidUpTo`, `DateRcvd`, `Misc`, `Or_Ind` | Zur Information |
| `ADDR1`, `ADDR2`, `ADDR3`, `CITY`, `STATE`, `ZIP`, `COUNTRY` | Werden verwendet, um die Daten eines fehlenden Kunden vorzubelegen |
| `WPHONE`, `HPHONE`, `FPHONE`, `OPHONE` | Werden verwendet, um die Daten eines fehlenden Kunden vorzubelegen |

Der Migrationsschlüssel lautet `<LotNo>-<Email>-<Amount>`.

## Daten eines fehlenden Kunden

Kann der Gebotsserver den Bieter nicht zuordnen, wird die Zeile mit `STATUS_MISSING_CLIENT` gespeichert, und das JSON in `client_data` enthält:

* `firstname`, `lastname`, `email`, `secondary_email`
* `zip`, `address`, `address2`, `address3`, `city`, `state`, `country` (Land normalisiert über `server_address_get_country_code()`)
* `office_phone`, `phone`, `fax`, `mobile`
* `external_id` (aus `CustNo`)
* `platform: "SAN"`

Das Backoffice verwendet diese Daten, um den Kunden bei Bedarf anzulegen.
