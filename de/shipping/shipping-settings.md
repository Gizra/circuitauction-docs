<!-- i18n source=shipping/shipping-settings.md sha=f9b3e6d591bb -->
# Versandeinstellungen

*Für Administratoren.* Der Versand wird im Drupal-Admin unter **Server settings → Shipping** (`admin/circuit-backoffice/server-settings`) eingerichtet.

![Der Bereich Shipping der Seite Server settings](../../assets/screenshots/shipping-settings.png)

## Anbieter

**Shipping provider API** legt fest, woher Preise und Etiketten kommen:

* **ShipStation**: aktuelle Tarife und Etiketten der Versanddienstleister. Tragen Sie für Testseiten den **ShipStation Sandbox API key** und für die Live-Seite den **ShipStation Production API key** ein.
* **ShipStation V2**: die neuere ShipStation-API. Sie hat keine Sandbox, jeder Schlüssel kauft also echte Etiketten; lassen Sie den Nicht-Live-Schlüssel auf Testseiten leer.
* **Manual**: Die Preise kommen aus Ihren eigenen Tariftabellen nach Gebiet und Gewicht; keine Etiketten.
* **Easyship**.

Die **Sender address** (Firmenname, Absenderadresse und Kontakt) ist die Absenderadresse auf den Etiketten. **Tax identifier type** und **Tax entity type** werden bei internationalen Sendungen übermittelt.

Für Tracking-Meldungen legen Sie ein **Webhook secret** fest und tragen die auf der Seite angezeigte **Webhook URL** im ShipStation-Dashboard ein (Webhooks → Ereignis TRACK).

## Was dem Käufer berechnet wird

| Einstellung | Wirkung |
| :--- | :--- |
| **Insured package value is based on** | Nur der Zuschlagspreis, oder Zuschlag plus Aufgeld. |
| **Insurance charge (%)** | Prozentsatz des versicherten Werts, der als Versicherung berechnet wird. 0 = keine Versicherung. |
| **Value cap** | Höchster Paketwert, auf den der Prozentsatz angewendet wird. 0 = keine Obergrenze. |
| **Fee cap** | Höchste Versicherungsgebühr pro Sendung. 0 = keine Obergrenze. |
| **Packing and handling markup (%)** | Wird auf die Kosten des Versanddienstleisters aufgeschlagen: 50 berechnet dem Käufer 150 % der Versandkosten. |

Die Obergrenzen gelten pro Sendung. Versicherung und Aufschlag werden dem Käufer nicht getrennt ausgewiesen: Sie sind Teil der **Versand**-Gebühr. Einen Wert beim Versanddienstleister zu deklarieren (damit dieser das Paket versichert), ist ein eigenes Kontrollkästchen und ändert nicht, was der Käufer zahlt.

## Weitere Einstellungen

* **Send one package per packed box to the carrier**: standardmäßig an; schalten Sie es für Versanddienstleister ab, die keine Sendungen mit mehreren Paketen annehmen.
* **Overdue shipment alerts**: Eine tägliche Prüfung legt für jede Sendung, die ihr voraussichtliches Lieferdatum überschritten hat, eine Aufgabe an. Das voraussichtliche Datum ist die Schätzung des Versanddienstleisters oder das Abholdatum plus **Delivery SLA (days after pickup)**. Lassen Sie **Task assignee UID** beim ersten Einschalten leer, prüfen Sie die angelegten Aufgaben und tragen Sie es dann ein.
* **Payment Approval**: Rechnungen über dem Schwellenwert (Nicht-VIP-Kunden) brauchen eine Zahlungsfreigabe, bevor sie verschickt werden können.

## Kundenvorgaben

Auf der Kundenseite begrenzen **Bevorzugte Versandmethode** und **Bevorzugter Versandservice** des Käufers die angebotenen Tarife auf diesen Versanddienstleister und Service. **Kostenloser Versand** macht neue Sendungen für diesen Kunden standardmäßig kostenlos, und **Automatische Auswahl des Versanddienstleisters deaktivieren** verhindert, dass das System für ihn einen Versanddienstleister wählt.
