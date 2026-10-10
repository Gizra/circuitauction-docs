<!-- i18n source=data-migration/clients.md sha=3ee42ee021b0 -->
---
description: Kundenknoten (Käufer und Einlieferer) aus einem Google Sheet importieren.
---

# Kunden

Handler: `ServerClientsDriveMigrate` — erweitert `ServerClientsMigrate`.

Importiert `client`-Knoten aus einer CSV. Die Spaltenzuordnung liegt im übergeordneten `ServerClientsMigrate` (unten dokumentiert); die Drive-Variante ergänzt nur die CSV-Quelle sowie einen kleinen Hook `prepareRow()`.

Konfiguriert über die Drupal-Variable `migrate_clients_csv`.

## Quelldatei

Tragen Sie die **CSV-Export-URL** Ihres Google Sheets in der Variable `migrate_clients_csv` ein. Die URL muss die CSV-Form sein, nicht der normale `edit`-Link:

```
https://docs.google.com/spreadsheets/d/<SPREADSHEET_ID>/export?format=csv&gid=<SHEET_GID>
```

Die zugehörige Bearbeiten-URL (Ursprung) sieht so aus:

```
https://docs.google.com/spreadsheets/d/<SPREADSHEET_ID>/edit?gid=<SHEET_GID>#gid=<SHEET_GID>
```

## Pflichtfelder

| Spalte | Verwendet als |
|---|---|
| `_id` | Schlüssel zur Zeilenverfolgung. |

## Identität

| Spalte | Ziel | Hinweise |
|---|---|---|
| `_first_name` | `field_first_name` | Wird automatisch aus `_last_name` extrahiert, wenn leer und `server_migrate_split_lastname_column` aktiviert ist. |
| `_last_name` | `field_last_name` | Das erste durch Leerzeichen getrennte Token kann nach `_first_name` verschoben werden, siehe oben. |
| `_username` | `field_username` | |
| `_email` | `field_email` | Wird als Suchschlüssel verwendet; steuert auch den Umgang mit Duplikaten. |
| `_secondary_email` | `field_secondary_email` | |
| `_salutation` | `field_salutation` | Taxonomie-Term, wird automatisch angelegt. |
| `_letter_salutation` | `field_letter_salutation` | Freitext. |
| `_company` | `field_company` | |
| `_birthdate` | `field_birthdate` | Leer / `0` gilt als nicht gesetzt. Andernfalls um 6 Stunden verringert und als `Y-m-d` gespeichert (Workaround für Zeitzonen). |
| `_customer_id` | `field_philaworksplace_id` | Externe / ältere Kunden-ID. Wird im Aktualisierungsmodus verwendet, um bestehende Kunden zu finden. |

## Kontaktdaten

| Spalte | Ziel |
|---|---|
| `_phone` | `field_phone` |
| `_mobile` | `field_mobile` |
| `_fax` | `field_fax` |
| `_office_phone` | `field_office_phone` |
| `_website` | `field_client_website` — wird im Aktualisierungsmodus automatisch in Kleinbuchstaben umgewandelt |

## Einstellungen & Kategorisierung

| Spalte | Ziel | Hinweise |
|---|---|---|
| `_interests` | `field_area_of_interests` | Durch Pipe getrennte Taxonomie-Terme, werden automatisch angelegt. Jedes Segment wird auf 255 Zeichen gekürzt. |
| `_tags` | `field_client_tags` | Durch Pipe getrennte Taxonomie-Terme, werden automatisch angelegt. Jedes Segment wird auf 255 Zeichen gekürzt. |
| `_source` | `field_client_source` | Durch Pipe getrennte Taxonomie-Terme, werden automatisch angelegt. |
| `_default_payment_method` | `field_default_payment_type` | Wird über die Zuordnung von `ServerPaymentTypeMigrate` ermittelt; wird bei Fehlen automatisch angelegt. Jedes Segment wird auf 255 Zeichen gekürzt. |
| `_agent` | `field_agent` | Standard ist `FALSE`. |
| `_language` | `field_website_language` | Standard ist die Sprache der Website; in Kleinbuchstaben. |

## Steuern & Abrechnung

| Spalte | Ziel | Hinweise |
|---|---|---|
| `_tax_type` | `field_tax_type` | Taxonomie-Term, wird automatisch angelegt. Jedes Segment wird auf 255 Zeichen gekürzt. |
| `_tax_id` | `field_tax_id` | |
| `_shipping_instructions` | `field_shipping_instructions` | |
| `_billing_instructions` | `field_billing_instructions` | |
| `_buyer_premium` | `field_bidder_commission` | Aufgeld des Käufers / Provisionssatz des Bieters in Prozent. |
| `_country` | (wird von der nachgelagerten Adresslogik verwendet) | Ist sie leer, gilt der Wert von `backoffice_order_default_country_for_tax` (`DE`, wenn nicht gesetzt). |

## Status

| Spalte | Ziel | Hinweise |
|---|---|---|
| `_status` | `field_user_status` | Standard ist `approved`. Wird nur zugeordnet, wenn **nicht** im Modus „Bestehende aktualisieren“. |
| `_is_deleted` | `field_user_status` | Ist der Wert in der Zeile wahr, wird der Status auf `deleted` erzwungen (überschreibt `_status`). |
| `_warning` | `field_warning` | Freitext-Warnung, die im Backoffice angezeigt wird. |
| `_created` | `created` | Zeitstempel der Knotenerstellung. |
| `_cancellation_date` | `field_cancellation_date` | |

## Provisionsstufen des Einlieferers (Multifield)

Der Handler baut aus nummerierten Spalten der Zeile ein gestaffeltes Multifield für die Einlieferer-Provision auf (`field_consignor_commissions`):

| Spaltenpaar | Gespeichert als |
|---|---|
| `_consignor_commission_1` + `_step_from_1` | Erste Stufe (Provision + Schwellenwert) |
| `_consignor_commission_2` + `_step_from_2` | Zweite Stufe |
| `_consignor_commission_N` + `_step_from_N` | …und so weiter, bis eine fehlende Spalte erreicht wird |

Für jede Stufe gilt:

* `_consignor_commission_N` wird in einen Prozentwert normalisiert — enthält der Wert noch kein `%`, wird er in eine Ganzzahl umgewandelt und ein `%` angehängt (z. B. `7` → `7%`).
* `_step_from_N` ist standardmäßig `0`, wenn leer.
* Leere Provisionswerte überspringen die Stufe.

Die gesammelten Stufen werden über den Entity-Wrapper nach `field_consignor_commissions` geschrieben.

## Notizen (mehrere Spalten)

Der Handler erstellt `note`-Knoten, die dem Kunden zugeordnet sind, aus bis zu vier durch Pipe getrennten Spalten:

* `_notes`, `_notes2`, `_notes3`, `_notes4`

Jedes Pipe-Segment wird zu einer Notiz. Die Titel der Notizen sind deterministisch (`Migrate imported note <_unique_id> - <field><index>`), sodass ein erneuter Import **keine** Duplikate erzeugt.

Ist `server_migrate_update_existing_notes` aktiviert, werden bestehende Notizen mit demselben Titel überschrieben.

{% hint style="info" %}
Bei der Installation `hr` wird numerischen Werten in `_notes3` und `_notes4` automatisch `Total Purchase - ` bzw. `Credit Limit - ` vorangestellt.
{% endhint %}

## Kundenreferenzen (nur SQL)

Existiert die SQL-Tabelle `_raw_client_references`, befüllt der Schritt `complete()` das Feld `field_node_references` (ein Multifield) bei jedem frisch importierten Kunden. Jede Referenzzeile enthält `_source_client`, `_destination_client` (NIDs, ermittelt über `migrate_map_serverclientsmigrate`) und `_reference_type` (automatisch angelegter Term von `relation_types`).

Referenzen werden nur importiert, wenn **nicht** im Modus „Bestehende aktualisieren“, weil das Backoffice darauf angewiesen ist, dass `hook_node_update` die Beziehung spiegelt, und dieser Hook beim Aktualisieren eines bestehenden Knotens nicht ausgelöst wird.

## Duplikate umgehen

Ist die Variable `server_migrate_bypass_duplicates` aktiviert, überspringt die Drive-Variante jede Zeile, deren `_email` bereits zu einem bestehenden Kunden passt. Nützlich beim erneuten Import eines Gebote-Sheets, das auch Kundendaten enthält — bestehende Kunden bleiben unverändert.

## Bestehende aktualisieren

Ist `server_migrate_update_existing` aktiviert, wechselt der Handler in den Aktualisierungsmodus:

* `systemOfRecord` wird zu `DESTINATION` — nur die zugeordneten Spalten überschreiben bestehende Werte.
* `_nid` wird zu einer zugeordneten Spalte.
* Die Zuordnungsstrategie wird über `server_migrate_update_existing_find_by_key` gesteuert:
  * `nid` *(Standard)* — Suche über `_philaworksplace_id` (Kunden-ID).
  * `emailphone` — Suche über `_email`.
* Wird kein Treffer gefunden, greift der Handler auf eine **Suche nach ähnlichen Telefonnummern** in `field_phone`, dann `field_mobile`, dann `field_fax` zurück. Mehrere Treffer → die Zeile wird mit einer Watchdog-Warnung übersprungen.
* Letzter Ersatz: Suche in `migrate_map_serverclientsdrivemigrate` über `_unique_id`, danach wird ein leerer Kunde angelegt, wenn nichts passt.

## Bereinigung doppelter E-Mail-Adressen

Ist `server_migrate_update_existing_set_duplicate_to_delete` aktiviert (Standard), wird nach dem Import jeder andere Kunde mit **derselben E-Mail-Adresse** auf `deleted` gesetzt. Nützlich, um bei einer Migration doppelte Konten zusammenzuführen.

## Vollständigen Namen aufteilen

Ist `_first_name` leer und `server_migrate_split_lastname_column` aktiviert, teilt der Handler `_last_name` am ersten Leerzeichen und verwendet das linke Token als `_first_name`. Nützlich, wenn das Quellsystem den vollständigen Namen in einer einzigen Spalte speichert.

## Kürzung von Termen

Jeder Termname in `_interests`, `_default_payment_method`, `_tags`, `_salutation` und `_tax_type` wird pro Pipe-Segment auf 255 Zeichen gekürzt. Kürzungen werden im Watchdog `server_migrate` protokolliert.

## Verwandt

* [Adressen](addresses.md) — Adressknoten an Kunden anhängen.
* [Externe IDs](external-ids.md) — externe System-IDs an Kunden anhängen.
* [Kunden aktualisieren](clients-update.md) — bestehende Kunden aktualisieren, zugeordnet über die E-Mail-Adresse.
* [Kundenpasswörter](clients-password.md) — Passwort-Hashes migrieren.
