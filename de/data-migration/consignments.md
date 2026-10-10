<!-- i18n source=data-migration/consignments.md sha=376d82a6c2ec -->
---
description: Einlieferungsknoten importieren.
---

# Consignments

Handler: `ServerConsignmentsDriveMigrate` — erweitert `ServerConsignmentsMigrate`.

Dünner CSV-Wrapper um den Basis-Handler `ServerConsignmentsMigrate`. Er ändert lediglich die Quelle auf eine CSV-Datei und entfernt die Abhängigkeiten für die eigenständige Nutzung; die Spaltenzuordnung und die Vorbereitungslogik stammen aus der Elternklasse.

Konfiguriert über die Drupal-Variable `migrate_consignments_csv`.

## Quelldatei

Tragen Sie die **CSV-Export-URL** Ihres Google Sheets in der Variable `migrate_consignments_csv` ein. Die URL muss die CSV-Form sein, nicht der normale `edit`-Link:

```
https://docs.google.com/spreadsheets/d/<SPREADSHEET_ID>/export?format=csv&gid=<SHEET_GID>
```

Die zugehörige Bearbeiten-URL (Ursprung) sieht so aus:

```
https://docs.google.com/spreadsheets/d/<SPREADSHEET_ID>/edit?gid=<SHEET_GID>#gid=<SHEET_GID>
```

{% hint style="info" %}
In den meisten Fällen müssen Einlieferungen nicht separat migriert werden — der Handler [Items (Self-Service)](items.md) legt die Einlieferung automatisch aus dem Feld `_consignment` des Lose-Sheets an. Verwenden Sie diesen Handler nur, wenn Sie Einlieferungen vor den Losen (oder unabhängig von ihnen) importieren möchten.
{% endhint %}

## Provisionsstufen

Die Einlieferer-Provision einer Einlieferung wird als eine oder mehrere **Provisionsstufen** im Multifield `field_commission_steps` gespeichert; jede Stufe ist ein Provisionssatz, der ab einem bestimmten Betrag (`field_step_from`) aufwärts gilt. Die Migration richtet diese auf drei Arten ein:

### Typ der Provisionsstufen

Die Spalte `_commission_steps_type` wird `field_commission_step_type` zugeordnet, was steuert, wie die Stufen interpretiert werden:

| Wert | Bedeutung |
|---|---|
| `single_lots` | Die Provision wird pro Los berechnet. |
| `entire_collection` | Die Provision wird über die gesamte Einlieferung / Sammlung berechnet. |

### Standard-Provisionsstufe (Ersatz)

Wird eine Einlieferung **ohne** Provisionsstufen importiert — d. h. es gibt in der Quelle für [Consignment Commission Steps](consignment-commission-steps.md) keine Zeile dafür und das Feld ist leer —, wendet der Handler automatisch eine einzelne Standardstufe an:

* **Satz:** aus der websiteweiten Drupal-Variable `backoffice_consignor_commission_for_migrate` übernommen (Standard `10%`).
* **Ab Betrag:** `0`.

Das stellt sicher, dass jede migrierte Einlieferung eine gültige Provision hat, damit die Abrechnung der Einlieferung erzeugt werden kann. Hat eine Einlieferung *dagegen* explizite Stufen aus der Multifield-Migration, wird der Standard **nicht** angewendet und die Validierung übersprungen, damit die Stufen anschließend angehängt werden können.

### Explizite Provisionen / mehrere Stufen

Um mehr als eine Stufe zu importieren (z. B. 10 % ab 0, dann 5 % ab 10.000), verwenden Sie die dedizierte Multifield-Migration [Consignment Commission Steps](consignment-commission-steps.md), die Stufen an bereits bestehende Einlieferungen anhängt.

Legt der Handler [Items (Self-Service)](items.md) automatisch eine Einlieferung an, setzt er eine einzelne Stufe aus dem Wert `_commission` des Lose-Sheets (Dezimalwerte unter 1 werden in einen Prozentwert umgerechnet) mit dem Stufentyp `single_lots`.

## Verwandt

* [Consignment Commission Steps](consignment-commission-steps.md) — mehrere Provisionsstufen an bestehende Einlieferungen anhängen.
* [Consignment Finder Fees](consignment-finder-fees.md) — Vermittlungsprovisionen an bestehende Einlieferungen anhängen.
