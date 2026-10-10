<!-- i18n source=bids/item-all-bids-popup.md sha=007106eb4f44 -->
# Popup mit allen Geboten eines Loses

Dieses Popup zeigt alle Gebote für ein ausgewähltes Los zusammen mit weiteren gebotsrelevanten Informationen. Öffnen Sie es, indem Sie in einer beliebigen Zeile der [Los-Tabelle der Gebote](bids-item-table.md) auf das **Pluszeichen** klicken.

## Seitenkopf

- Losnummer
- Schaltflächen Weiter/Zurück (zum Wechseln zwischen Losen)
- Preise des Loses (Ausruf, Eröffnung, aktuell, Minimum)
- Losstatus

## Obere Blöcke

1. **Formular zum Eingeben von Geboten** — Die Losnummer ist für das aktuelle Los vorausgefüllt.
2. **Eröffnungspreis ändern und neu zuschlagen:**
   - Passen Sie den Eröffnungspreis an, wie Sie es in einer Live-Auktion tun würden.
   - Der aktuelle Preis wird auf Grundlage dieses Eröffnungspreises berechnet.
   - Der Eröffnungspreis kann höher oder niedriger als der Ausruf gesetzt werden, um den gewünschten Verkaufspreis zu erreichen.
   - Mit der Schaltfläche **Reknock** berechnen Sie den aktuellen Preis neu und aktualisieren alle zugehörigen Rechnungen.
3. **Links** — Link zur Einlieferer-Seite und zur Rechnung.

## Gebotstabelle

### Gebotsinformationen

| Spalte | Beschreibung |
|---|---|
| Status | Aktueller Zustand des Gebots |
| Art | Kategorie oder Klassifizierung des Gebots |
| Menge | Geldwert des Gebots |
| Erstellt | Zeitstempel der Gebotserstellung |
| Bieter | Name des Bieters (verlinkt auf das Kundenprofil) |
| Bieternummer | Eindeutige Kennung, die dem Gebot zugeordnet ist |
| Eingegeben von | Wer das Gebot eingegeben hat (Kunde, Mitarbeiter oder Partner) |
| Gruppenname | Kategorie zur Gruppierung zusammengehöriger Gebote |
| Genehmigungsdatum | Zeitpunkt, zu dem das Gebot von Mitarbeitern bestätigt wurde |
| Genehmigt von | Mitarbeiter, der das Gebot bestätigt hat |
| Hinweis | Zusätzliche Kommentare oder Informationen zum Gebot |

{% hint style="info" %}
**Gruppengebote** werden während der Auktionen automatisch verwaltet. Ein Kunde kann pro Gruppe nur ein Los gewinnen — der Zuschlag auf ein Los der Gruppe storniert die übrigen Gruppengebote.
{% endhint %}

### Aktionen und Steuerelemente

1. **uV Prüfung** — Kontrollkästchen, das anzeigt, dass das Gebot während einer Prüfungsfrist (Extension) abgegeben wurde. Die Anzeige wechselt beim Aktivieren von Grau zu Rot. Wird automatisch übermittelt.
2. **Gebot genehmigen/Genehmigung aufheben** — Kontrollkästchen zum Markieren des Genehmigungsstatus. Die Anzeige wechselt bei Genehmigung von Gelb zu Grün. Wird automatisch übermittelt.
3. **Speichern** — Speichert den Gruppennamen und die Notizen. Aktualisiert außerdem Bieternummer und Betrag, wenn das Gebot bearbeitet wurde.
4. **Gebot löschen/wiederherstellen** — Rotes Papierkorb-Symbol zum Löschen eines Gebots; blaue Schaltfläche „Rückgängig“ zum Wiederherstellen eines gelöschten Gebots.
5. **Bearbeiten** — Ermöglicht Mitarbeitern, bestehende Gebote zu ändern (Betrag und Bieternummer). Die Änderungen müssen mit einem Klick auf **Speichern** bestätigt werden.

![Tabelle im Popup mit allen Geboten eines Loses](../../assets/screenshots/popup-table.png)
