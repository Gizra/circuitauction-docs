<!-- i18n source=data-migration/clients-update.md sha=2eaab550486b -->
---
description: Bestehende Kunden aktualisieren, zugeordnet über die E-Mail-Adresse.
---

# Kunden aktualisieren

Handler: `ServerClientsUpdateDriveMigrate` — erweitert `ServerClientsMigrate`.

Aktualisiert **bestehende** Kundenknoten aus einer CSV-Datei. Die Zuordnung erfolgt über `_email`; Zeilen, deren E-Mail-Adresse keinem bestehenden Kunden entspricht, werden mit einem Watchdog-Fehler übersprungen.

Konfiguriert über die Drupal-Variable `migrate_clients_update_csv`.

## Quelldatei

Tragen Sie die **CSV-Export-URL** Ihres Google Sheets in der Variable `migrate_clients_update_csv` ein. Die URL muss die CSV-Form sein, nicht der normale `edit`-Link:

```
https://docs.google.com/spreadsheets/d/<SPREADSHEET_ID>/export?format=csv&gid=<SHEET_GID>
```

Die zugehörige Bearbeiten-URL (Ursprung) sieht so aus:

```
https://docs.google.com/spreadsheets/d/<SPREADSHEET_ID>/edit?gid=<SHEET_GID>#gid=<SHEET_GID>
```

Intern wird `Migration::DESTINATION` als führendes System verwendet, sodass nur die von diesem Handler zugeordneten Spalten bestehende Werte überschreiben.

## Spalten

Der Handler ordnet zu:

| Spalte | Ziel |
|---|---|
| `_email` | Wird verwendet, um den bestehenden Kunden zu finden; die Zeile wird übersprungen, wenn es keinen Treffer gibt. |
| `_nid` | Wird intern aus dem gefundenen Kunden ermittelt und in das Ziel zurückgeschrieben. |
| Alle übrigen von `ServerClientsMigrate` geerbten Spalten | Die Felder, die die Basiszuordnung definiert (Telefon, Adressfelder, Anrede usw.). |

## Vollständigen Namen aufteilen

Wie beim Handler [Kunden](clients.md): Ist `_first_name` leer und `server_migrate_split_lastname_column` aktiviert, wird `_last_name` am ersten Leerzeichen aufgeteilt.
