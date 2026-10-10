<!-- i18n source=data-migration/README.md sha=de75ff796cf9 -->
---
description: Massenimport-Handler für Lose, Kunden, Einlieferungen, Gebote und verwandte Daten.
---

# Datenmigration

Das Backoffice enthält eine Reihe von Migrations-Handlern, mit denen sich Daten in großen Mengen aus einem Google Sheet (CSV) oder in einigen Fällen aus einer entfernten API importieren lassen. Jeder Handler ist für eine bestimmte Entität zuständig (Lose, Kunden, Adressen, Gebote usw.) und stellt seine eigenen Quellspalten bereit.

Alle Handler folgen demselben allgemeinen Ablauf:

1. Bereiten Sie eine Quelldatei (in der Regel ein Google Sheet) mit den erwarteten Spaltenüberschriften vor.
2. Fügen Sie die **CSV-Export-URL** des Sheets in das entsprechende Formular im Backoffice ein.
3. Starten Sie die Warteschlange, um die Zeilen zu verarbeiten.
4. Prüfen Sie die Ergebnistabelle und stellen Sie fehlgeschlagene Zeilen bei Bedarf erneut in die Warteschlange.

{% hint style="info" %}
Bei Google Sheets muss die URL die CSV-Exportform sein, nicht der normale `edit`-Link. Das Muster lautet:

```
https://docs.google.com/spreadsheets/d/<SPREADSHEET_ID>/export?format=csv&gid=<SHEET_GID>
```
{% endhint %}

## Verfügbare Handler

### Lose

| Handler | Zweck |
|---|---|
| [Items (Self-Service)](items.md) | Neue Lose in großen Mengen importieren; Einlieferung und Einlieferer werden bei Bedarf automatisch angelegt. |
| [Items Update](items-update.md) | Bestehende Lose anhand von `nid`, `_internal_id` oder Losnummer aktualisieren. Legt keine neuen Lose an. |
| [Items Sold Result](items-sold-result.md) | Verkaufspreise und Höchstbietende importieren; erzeugt Einträge im Losverlauf. |
| [Item Catalogs](items-catalogs.md) | Katalogverweise (Multifield) an bestehende Lose anhängen. |
| [Item Dimensions](items-dimensions.md) | Dimensions- und Verpackungsangaben (Multifield) an bestehende Lose anhängen. |

### Kunden & Adressen

| Handler | Zweck |
|---|---|
| [Clients](clients.md) | Kundenknoten importieren (Käufer & Einlieferer). |
| [Clients Update](clients-update.md) | Bestehende Kunden aktualisieren, zugeordnet über die E-Mail-Adresse. |
| [Clients Password](clients-password.md) | Passwort-Hashes auf bestehende Kunden übertragen. |
| [Addresses](addresses.md) | Adressknoten importieren und an bestehende Kunden anhängen. |
| [External IDs](external-ids.md) | Externe System-IDs (Multifield) an Kunden anhängen. |
| [Clients Bank Accounts](clients-bank-accounts.md) | Bankverbindungen (Multifield) an bestehende Kunden anhängen. |

### Kategorien, Auktionen & Einlieferungen

| Handler | Zweck |
|---|---|
| [Categories](categories.md) | Die Taxonomie `categories` mit Hierarchie und Übersetzungen importieren. |
| [Sales](sales.md) | Auktionsknoten importieren. |
| [Consignments](consignments.md) | Einlieferungsknoten importieren (inkl. Typ der Provisionsstufen und Standardprovision). |
| [Consignment Commission Steps](consignment-commission-steps.md) | Provisionsstufen-Multifields an Einlieferungen anhängen. |
| [Consignment Finder Fees](consignment-finder-fees.md) | Vermittlungsprovisions-Multifields an Einlieferungen anhängen. |
| [Transactions](transactions.md) | Transaktionsknoten für Bestellungen importieren. |

### Gebote

| Handler | Zweck |
|---|---|
| [Bids](bids.md) | Generischer CSV-/SQL-Gebotsimport. |
| [Philasearch Bids](bids-philasearch.md) | Gebote aus der Philasearch-API abrufen und importieren. |
| [Delcampe Bids](bids-delcampe.md) | Gebote aus einem Delcampe-Export importieren. |
| [Auction Mobility Bids](bids-mobility.md) | Von Auction Mobility exportierte Gebote importieren. |
| [SAN Bids](bids-san.md) | Gebote aus einem SAN-Export importieren. |

## Importreihenfolge & Abhängigkeiten

Die Drive-Handler (CSV) lösen die Abhängigkeiten zwischen den Migrationen auf, sodass **Sie die Reihenfolge der Durchläufe selbst bestimmen**. Die empfohlene Reihenfolge lautet:

```
categories
  → clients
    → addresses · bank accounts · external ids · bidder numbers · client commission steps
  → sales
  → consignments  (+ consignment commission steps · finder fees)
  → items
  → orders
  → buyer transactions
  → consignor statements / payouts
  → images (phase 2)
```

Wichtige Hinweise:

* **Einlieferungen müssen nicht vor den Losen kommen.** Der Handler [Items (Self-Service)](items.md) legt Einlieferung und Einlieferer automatisch aus der Loszeile an, wenn `_consignment` vor dem ersten Pipe-Zeichen eine E-Mail-Adresse / Kunden-ID / Einlieferungs-ID des Einlieferers enthält. Einlieferungen zuerst zu importieren wird dennoch empfohlen, wenn Sie umfangreiche Verkäuferdaten haben, denn so behalten Sie von Anfang an die Kontrolle über Provisionsstufen, Steuerart und Einlieferungs-IDs.
* **Bestellungen werden aus Verkaufsergebnissen automatisch angelegt** (eine Bestellung pro Auktion + Käufer) oder können explizit importiert werden.
* Eine **Abrechnung** der Einlieferung wird automatisch aus dem Ablauf für Lose / Verkaufsergebnisse erzeugt — für die automatisch abgeleiteten Positionen gibt es keinen separaten Abrechnungsimport.

## Schlüssel & Zuordnung

Die Migration stützt sich auf stabile Quell-IDs, sodass Beziehungen auch bei wiederholten Durchläufen erhalten bleiben:

* **Kunden** werden über `_customer_id` → `field_philaworksplace_id` identifiziert. Dies ist der Resolver, den fast jeder kundenbezogene Handler verwendet (Adressen, Bankverbindungen, externe IDs, Los → Einlieferer usw.); E-Mail-Adressen von Kunden müssen daher **nicht** global eindeutig sein. Die einzige Ausnahme ist die **Suche des Höchstbietenden bei Verkaufsergebnissen**, die den Höchstbietenden derzeit nur über die E-Mail-Adresse ermittelt.
* **Lose** werden über `_internal_id` → `field_internal_id` identifiziert und von Verkaufsergebnissen und Transaktionen wiedergefunden. Wird keine Auktion angegeben, gewinnt der erste Treffer; `_internal_id` sollte daher global eindeutig sein.
* **Auktionen** werden über `_sale_number` zugeordnet (die für Menschen lesbare Auktionsreferenz). Es ist ein Freitextfeld, muss aber eindeutig sein — der erste Treffer gewinnt.
* **Kategorien** werden über `_hk_id` → `field_hk_cat_id` zugeordnet.
* **Dasselbe physische Kunstwerk in mehreren Auktionen:** Bilden Sie jedes Auftreten als eigenes Los ab und tragen Sie die gemeinsame Kunstwerk-ID in `_search_tag` (`field_search_tags`) ein, um alle Auftritte zu gruppieren. Eine eigene Entität „übergeordnetes Kunstwerk“ gibt es nicht.

## Allgemeine Konventionen

* **Eindeutige Kennung:** Jede Zeile muss eine Spalte `_unique_id` (oder eine gleichwertige) enthalten. Die Migrationszuordnung nutzt sie, um nachzuverfolgen, welche Zeilen bereits importiert wurden, und um Duplikate zu vermeiden.
* **Unbekannte Spalten werden ignoriert.** Drive-Handler lesen die Kopfzeile und überspringen jede Quellspalte ohne Feldzuordnung; zusätzliche Spalten (z. B. `gap_*`) sind daher wirkungslos — nützlich, um Daten mitzuführen, die in Circuit noch keinen Platz haben und später geprüft werden sollen.
* **Sprachen:** Handler lesen Spalten der Form `_<field>_<langcode>` und füllen eine zweite Sprache nur, wenn die entsprechende Variable `*_second_language` gesetzt ist. Rein englische Daten (`_..._en` befüllen, die übrigen leer lassen) werden vollständig unterstützt.
* **Formate:** Liefern Sie Datumsangaben im ISO-Format `YYYY-MM-DD` (geparst über `strtotime()`), Beträge als reine Zahlen ohne Währungssymbol und Dateien in UTF-8. Preisspalten entfernen ein vorangestelltes Währungssymbol automatisch; vermeiden Sie jedoch Tausendertrennzeichen in Betragsspalten, die keine Preise sind — nicht jeder Handler entfernt Kommas.
* **Eine Zeile überspringen:** Verweist eine Zeile auf eine fehlende Entität (Kunde, Los, Einlieferung), protokolliert der Handler den Grund und überspringt die Zeile — die Spalte **Info** der Ergebnistabelle zeigt, warum.
* **Einen Import erneut ausführen:**
  * **Importelemente in die Warteschlange stellen** verarbeitet nur Zeilen, die noch nie importiert wurden.
  * **Queue failed import items** wiederholt nur die Zeilen, die zuvor fehlgeschlagen sind.
  * **Queue update All items data** importiert jede Zeile erneut und **überschreibt manuelle Änderungen im Backoffice** — mit Vorsicht verwenden.
* **Testmodus:** In Nicht-Live-Umgebungen wird an ausgehende E-Mails `.test` angehängt, um zu verhindern, dass echte Kunden kontaktiert werden.
