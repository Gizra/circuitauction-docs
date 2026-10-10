<!-- i18n source=website/place-bid.md sha=50c3c2265cba -->
# Gebot abgeben

**Selektor:** `.place-bid` (Klasse) &nbsp;•&nbsp; *mehrfach pro Seite erlaubt*

## Funktion

Ein Inline-Gebots-Widget für schriftliche Gebote und Kommissionsgebote vor der Auktion. Es kann neben jedem Los platziert werden — zum Beispiel ein Widget pro Zeile in einer eigenen Losliste —, da es über die **Klasse** und nicht über die ID gefunden wird; eine Seite kann also viele unabhängige Instanzen enthalten.

Das Widget zeigt das aktuelle bzw. Ausrufgebot mit intelligenten Steigerungsschaltflächen, prüft Mindestgebote und das verfügbare Guthaben des Benutzers und aktualisiert sich live per WebSocket, sobald Gebote eingehen. Es passt sich dem Zustand des Loses an (nicht gestartet, laufend, beendet, verkauft, zurückgegangen) und lässt den Bieter seine schriftlichen Gebote und Kommissionsgebote abgeben, ändern oder löschen.

**Zum Bieten ist eine Anmeldung erforderlich.** Anonyme Besucher sehen eine Anmeldeaufforderung; Konten, die noch auf Freigabe warten, sowie Konten mit unzureichendem Guthaben erhalten die jeweilige Meldung.

## So fügen Sie es hinzu

```html
<div class="place-bid circuit-user-ui"
     data-sale-uuid="live-68f657cdd8e3a5-18178142"
     data-item-uuid="live-68f793c6759514-56806752"></div>
```

## Optionen

| Attribut | Erforderlich | Standard | Werte | Wirkung |
|-----------|----------|---------|--------|--------|
| `data-sale-uuid` | **Ja** | — | Auktions-UUID | Die Auktion, zu der das Los gehört. |
| `data-item-uuid` | **Ja** | — | Los-UUID | Das Los, auf das geboten wird. |
| `hide-sold-unsold` | Nein | `false` | `true` | Blendet das Widget vollständig aus, wenn das Los bereits verkauft oder unverkauft ist (nur für bietbare Lose anzeigen). |
| `data-debug` | Nein | `false` | `true` | Aktiviert die Protokollierung in der Entwicklerkonsole. |

## Beispiele

```html
<!-- One widget per item in a custom list -->
<div class="item-card">
  <h3>Lot 101 — Vintage Watch</h3>
  <div class="place-bid circuit-user-ui"
       data-sale-uuid="live-68f657cdd8e3a5-18178142"
       data-item-uuid="live-68f793c6759514-56806752"></div>
</div>

<div class="item-card">
  <h3>Lot 102 — Antique Clock</h3>
  <div class="place-bid circuit-user-ui"
       data-sale-uuid="live-68f657cdd8e3a5-18178142"
       data-item-uuid="live-68f793c6759514-56806753"></div>
</div>

<!-- Only render while the lot is still biddable -->
<div class="place-bid circuit-user-ui"
     data-sale-uuid="live-68f657cdd8e3a5-18178142"
     data-item-uuid="live-68f793c6759514-56806752"
     hide-sold-unsold="true"></div>
```
