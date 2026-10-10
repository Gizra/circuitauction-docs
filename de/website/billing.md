<!-- i18n source=website/billing.md sha=acbd18ed1273 -->
# Abrechnung & Zahlungen

**Selektor:** `#billing-history` (auch `#payment-method`) &nbsp;•&nbsp; *einmal pro Seite* &nbsp;•&nbsp; **Anmeldung erforderlich**

## Funktion

Das Abrechnungscenter des Bieters mit zwei Reitern:

- **Billing History** — eine Liste der Rechnungen mit Statusfilter (alle / ausstehend / überfällig / bezahlt), Details und PDF-Links pro Rechnung, Transaktionsverlauf, Seitennavigation und einem Bezahlvorgang, um ausgewählte Rechnungen zu begleichen.
- **Payment Methods** — gespeicherte Karten (mit Markenlogos), Formular zum Hinzufügen einer Karte (Karteninhaber, Nummer, Ablaufdatum, CVV, Rechnungsadresse) sowie Aktionen zum Bearbeiten/Löschen. Dieser Reiter ist ausgeblendet, wenn Ihre Website ausschließlich telefonische Zahlung nutzt.

Die Seite unterstützt Deep Links: Der URL-Hash `#payment-methods` öffnet den Reiter Payment Methods, während `#billing` (oder kein Hash) die Billing History öffnet.

## So fügen Sie es hinzu

```html
<div id="billing-history" class="circuit-user-ui"></div>
```

Wenn Sie stattdessen `#payment-method` einbinden, wird dasselbe Abrechnungscenter dargestellt — nützlich, wenn die URL bzw. der Anker „payment-method“ lauten soll.

## Optionen

Keine.

## Siehe auch

- [Saldo-Button](/de/website/balance.md) — ein kompakter Indikator für den fälligen Betrag, der hierher verlinkt
