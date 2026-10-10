<!-- i18n source=data-migration/bids-philasearch.md sha=87f23a5d2720 -->
---
description: Gebote aus der Philasearch-API abrufen und importieren.
---

# Philasearch-Gebote

Handler: `ServerPhilasearchBidMigrate` — erweitert `ServerBidMigrateBase`.

Anders als die übrigen Gebots-Handler ist Philasearch **API-basiert**: Die Migrationsquelle ist ein JSON-Endpunkt, keine CSV — es gibt **kein Google Sheet zu konfigurieren**. Der Handler wird ausschließlich über eine AQ-Aufgabe aufgerufen.

## Erforderliche Variablen

| Variable | Zweck |
|---|---|
| `server_bid_philasearch_api_key` | Erforderlich — dient der Authentifizierung der API-Anfrage. Löst einen Fehler aus, wenn sie fehlt. |
| `server_bid_philasearch_api_last_fetch` | UNIX-Zeitstempel des letzten erfolgreichen Abrufs. Wird als Cursor `from` verwendet. |
| `server_bid_philasearch_menu_secret` | Gemeinsames Geheimnis, aus dem das Token der Einmal-URL berechnet wird. |
| `server_bid_import_philasearch_username` | Autor der importierten Gebote (Standard ist `Philasearch`). Wird bei Fehlen automatisch mit der Berechtigung Clerk angelegt. |

Der Handler erzeugt eine Einmal-URL der Form:

```
/admin/philasearch-bids/{sale_nid}/{api_key}/{last_timestamp}/{one_time_token}
```

…und liest die Gebote aus `MigrateSourceJSON`.

## Quell-JSON-Format

Jedes Gebot enthält mindestens:

| Feld | Beschreibung |
|---|---|
| `bidId` | Eindeutige ID der Quelle (wird als Migrationsschlüssel verwendet) |
| `custNo` | Philasearch-Kundennummer |
| `orderTime` | Zeitstempel des Gebots |
| `saleNo`, `lotNo`, `supNo`, `posNo`, `orderNo` | Angaben zu Auktion / Los |
| `bidType`, `bidAmount` | Gebotswert |
| `email` | E-Mail-Adresse des Bieters |
| `info.comment` | Optionaler Kommentar des Bieters — wird protokolliert und markiert die Zuordnungszeile mit `STATUS_OK_WITH_INFO` |
| `client.internalInfo`, `client.shippingAddress` | Zusätzliche Informationen zum Bieter; werden protokolliert und lösen dieselbe Markierung aus |
| `client.*` | Vollständige Kundendaten, mit denen die Oberfläche für fehlende Bieter im Backoffice vorbelegt wird, wenn der Kunde nicht zugeordnet werden kann. |

## Zuordnung zum Ziel

| Quelle | Ziel |
|---|---|
| `lotNo` | `lot` |
| `bidAmount` | `amount` |
| `sale_uuid` | `sale_uuid` |
| `email` | `email` |

Meldet der Gebotsserver `BID_CLIENT_MISSING`, wird die Zeile mit `STATUS_MISSING_CLIENT` gespeichert, und das vollständige JSON `client_data` bleibt an der Zuordnungszeile erhalten, einschließlich des Tags `platform: 'Philasearch'` und `custNo` als `external_id`.

## Hinweise

* Der Handler überschreibt `import()`, um `STATUS_OK_WITH_INFO` und andere Zuordnungszustände pro Zeile korrekt zusammenzuführen.
* Von der Quelle ausgelöste Fehler (z. B. ein API-Timeout) brechen den gesamten Lauf ab — sie werden als `WATCHDOG_ERROR` gegen `server_migrate` protokolliert.
