<!-- i18n source=data-migration/consignment-commission-steps.md sha=8b53245ecc2c -->

# Provisionsschritte der Einlieferungen

Handler: `ServerConsignmentCommissionStepsMigrate`.

Importiert Zeilen in das **Multifield** `field_commission_steps` der Einlieferungsknoten. Jede Zeile erfasst eine Provisionsstufe — einen Provisionssatz des Einlieferers, der ab einem bestimmten Betrag gilt. Verwenden Sie diesen Handler, wenn eine Einlieferung **mehr als eine** Stufe benötigt (gestaffelte Provision) oder wenn Sie explizite Stufen statt der [Standard-Ersatzstufe](/de/data-migration/consignments.md#standard-provisionsstufe-ersatz) wünschen.

Hängt von [Einlieferungen](/de/data-migration/consignments.md) (`ServerConsignmentsMigrate`) ab — die Einlieferungsknoten müssen zuerst importiert werden, damit die Stufen an sie angehängt werden können.

## Quelle

Die Stufen werden aus der Tabelle `_raw_consignment_commission_steps` gelesen. Ist die Variable `server_migrate_item_sale_number_to_import` gesetzt, werden nur Stufen für Einlieferungen dieser Auktion verarbeitet.

## Spalten

| Spalte | Verwendet als |
|---|---|
| `_unique_id` | ID zur Zeilenverfolgung (erforderlich). |
| `_consignment` | Die Einlieferung, zu der die Stufe gehört, ermittelt über die Zuordnung von `ServerConsignmentsMigrate`. |
| `_commission` | Der Provisionssatz des Einlieferers für diese Stufe (gespeichert in `field_consignor_commission`). |
| `_from_amount` | Der Betrag, ab dem der Satz dieser Stufe gilt (gespeichert in `field_step_from`). Verwenden Sie `0` für die erste bzw. Basisstufe. |

## Zuordnung zum Ziel

| Quelle | Ziel |
|---|---|
| `_consignment` (ermittelte NID der Einlieferung) | `host` |
| `_commission` | `field_consignor_commission` |
| `_from_amount` | `field_step_from` |

## Beispiel

Zwei Stufen derselben Einlieferung — 10 % ab 0, danach ein höherer Satz ab 1.000:

| Unique Id | Consignment | Commission | From amount |
|---|---|---|---|
| `consignment_commission_step_1` | `consignment1` | `10` | `0` |
| `consignment_commission_step_2` | `consignment1` | `500` | `1000` |

## Verwandt

* [Einlieferungen](/de/data-migration/consignments.md) — importieren Sie die Einlieferungsknoten, an die diese Stufen angehängt werden (und das Standardverhalten mit einer einzelnen Stufe).
