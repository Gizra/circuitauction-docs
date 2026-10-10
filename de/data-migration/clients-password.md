<!-- i18n source=data-migration/clients-password.md sha=f0e7d2d3670b -->

# Kundenpasswörter

Handler: `ServerClientsPasswordDriveMigrate`.

Aktualisiert den Passwort-Hash eines bestehenden Kundenknotens. Wird verwendet, wenn Kunden aus einem Altsystem migriert werden, das Hashes speichert, die mit dem Drupal-Format `$HK...$salt` kompatibel sind.

Konfiguriert über die Drupal-Variable `migrate_client_password_csv`. Verwendet `Migration::DESTINATION` als führendes System.

## Quelldatei

Tragen Sie die **CSV-Export-URL** Ihres Google Sheets in der Variable `migrate_client_password_csv` ein. Die URL muss die CSV-Form sein, nicht der normale `edit`-Link:

```
https://docs.google.com/spreadsheets/d/<SPREADSHEET_ID>/export?format=csv&gid=<SHEET_GID>
```

Die zugehörige Bearbeiten-URL (Ursprung) sieht so aus:

```
https://docs.google.com/spreadsheets/d/<SPREADSHEET_ID>/edit?gid=<SHEET_GID>#gid=<SHEET_GID>
```

## Spalten

| Spalte | Verhalten |
|---|---|
| `_unique_id` | Quellkennung — wird verwendet, um den Kunden über die Kunden-ID zu finden, wenn `_nid` leer ist (`server_client_get_client_nid_by_customer_id`). |
| `_nid` | Knoten-ID des Kunden. Wird aus `_unique_id` ermittelt, falls sie fehlt; ist sie dann immer noch leer, wird die Zeile übersprungen. |
| `field_password` | Passwort-Hash. Wird als `$HK<value>$<salt>` gespeichert. Zeilen mit `<empty>` werden übersprungen. |
| `salt` | Salt, mit dem der gespeicherte Hash zusammengesetzt wird. |
| `_default_payment_method` | Optional. Legt automatisch einen Term von `payment_types` an und weist ihn `field_default_payment_type` zu. |

{% hint style="warning" %}
Dieser Handler hasht das Passwort **nicht** — er speichert den Wert unverändert mit der Hülle `$HK…$<salt>`. Verwenden Sie ihn nur mit Hashes, die bereits im erwarteten Format vorliegen.
{% endhint %}
