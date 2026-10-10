<!-- i18n source=website/balance.md sha=62fdbba28aff -->
# Saldo-Button

**Selektor:** `#balance-btn` &nbsp;•&nbsp; *einmal pro Seite*

## Funktion

Ein kompakter Button, der den Kontosaldo bzw. den fälligen Betrag des angemeldeten Bieters anzeigt — praktisch für den Seitenkopf Ihrer Website. Er behandelt mehrere Zustände automatisch:

- **Nicht angemeldet** — zeigt die Aufforderung „Anmelden, um den Saldo zu sehen“.
- **Laden / Fehler** — während des Abrufs oder wenn die Abfrage fehlschlägt.
- **Offener Betrag** — bei negativem Saldo führt er weiter zur Abrechnung.
- **Alles beglichen** — wenn nichts offen ist.

## So fügen Sie es hinzu

```html
<div id="balance-btn" class="circuit-user-ui"></div>
```

## Optionen

Keine.

## Siehe auch

- [Abrechnung & Zahlungen](/de/website/billing.md) — wohin der Zustand „Offener Betrag“ verlinkt
