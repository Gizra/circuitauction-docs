<!-- i18n source=data-migration/clients-bank-accounts.md sha=2d813a76fc69 -->
---
description: Bankverbindungen (Multifield) an bestehende Kunden anhängen.
---

# Clients Bank Accounts

Handler: `ServerClientBankAccountDriveMigrate` — erweitert `ServerClientBankAccountMigrate`.

Importiert Zeilen in das **Multifield** `field_bank_details` der Kundenknoten. Jede Zeile erfasst eine Bankverbindung (Bankname, Bankleitzahl, Kontonummer, IBAN, BIC).

Konfiguriert über die Drupal-Variable `migrate_clients_bank_accounts_csv`.

## Quelldatei

Tragen Sie die **CSV-Export-URL** Ihres Google Sheets in der Variable `migrate_clients_bank_accounts_csv` ein. Die URL muss die CSV-Form sein, nicht der normale `edit`-Link:

```
https://docs.google.com/spreadsheets/d/<SPREADSHEET_ID>/export?format=csv&gid=<SHEET_GID>
```

Die zugehörige Bearbeiten-URL (Ursprung) sieht so aus:

```
https://docs.google.com/spreadsheets/d/<SPREADSHEET_ID>/edit?gid=<SHEET_GID>#gid=<SHEET_GID>
```

## Kundensuche

Die Drive-Variante ermittelt den zugehörigen Kunden direkt aus `_customer_id` über `server_client_get_client_nid_by_customer_id()`. Zeilen, deren Kunden-ID keinem bestehenden Kunden entspricht, werden mit einer Watchdog-Warnung übersprungen (`Bank account row without client: <_unique_id> for customer: <_customer_id>`).

{% hint style="info" %}
Das übergeordnete `ServerClientBankAccountMigrate` (SQL-Variante) ermittelt den zugehörigen Kunden dagegen über die Zuordnung von `ServerClientsMigrate`. Die Drive-Variante entfernt diese Zuordnung bewusst zugunsten der direkten Suche über die Kunden-ID.
{% endhint %}

## Spalten

| Spalte | Ziel |
|---|---|
| `_unique_id` | ID zur Zeilenverfolgung (erforderlich) |
| `_customer_id` | Wird verwendet, um den zugehörigen Kunden zu ermitteln. Zeilen ohne Treffer werden übersprungen. |
| `_bank` | `field_bank_name` |
| `_bank_code` | `field_bank_code` |
| `_account_number` | `field_bank_account_number` **und** `field_bank_account_owner` (beide werden aus derselben Spalte befüllt — siehe den Hinweis unten) |
| `_iban` | `field_iban` |
| `_bic` | `field_bic` |

{% hint style="warning" %}
**Geplant (Modelländerung):** Derzeit liegen die Bankdaten im Multifield `field_bank_details` pro Kunde, wobei `_account_number` fälschlicherweise sowohl der Kontonummer **als auch** dem Kontoinhaber zugeordnet wird. Eine geplante Änderung verschiebt umfangreichere Bankattribute (Kontoinhaber, Zahlungsempfänger bei Schecks, Bankadresse, Währung, …) stattdessen in die **Taxonomie** `bank_accounts` — neue Felder am Term des Vokabulars, importiert über die Taxonomie-Migration für Bankkonten (`ServerBankAccountsMigrate`). Liefern Sie diese Attribute als Spalten, dann werden sie dem Vokabular hinzugefügt und dort zugeordnet, statt das Multifield pro Kunde zu überladen.
{% endhint %}
