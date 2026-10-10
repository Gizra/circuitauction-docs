<!-- i18n source=release-notes/version-3.3.md sha=0ff614abc6f1 -->
# Version 3.3

Veröffentlicht im Mai 2026. Diese Version bringt eine Neugestaltung aller Live-Auktionsbildschirme, eine umfassende Überarbeitung des Versands mit ShipStation-Integration und schnelleres Laden von Bildern.

## Live-Auktionserlebnis

### Neues Anzeigedesign auf allen Live-Bildschirmen

Das gesamte Live-Auktionserlebnis wurde neu gestaltet. Die Bildschirme für Auktionator, Clerk, Bieter und Saal haben übersichtlichere, großzügigere Layouts, die mehr Informationen auf einen Blick zeigen, siehe [Live-Auktion](../auction/README.md).

### Heller und dunkler Anzeigemodus

Die Seiten der Live-App haben einen Umschalter für den Anzeigemodus. Wechseln Sie zwischen hellem und dunklem Modus, passend zum Saal und zur Beleuchtung.

Bieterbildschirm:

![Bieterbildschirm, heller Modus](/assets/screenshots/release-3.3-bidder-light.png)

![Bieterbildschirm, dunkler Modus](/assets/screenshots/release-3.3-bidder-dark.png)

### Ergonomischer Clerk-Bildschirm: die Auktion ohne Maus durchführen

Der Clerk-Bildschirm wurde für die Bedienung per Tastatur neu entwickelt. Die gesamte Auktion lässt sich über die Tastatur durchführen:

| Taste | Aktion |
|-----|--------|
| Leertaste | Nächstes Gebot abgeben |
| Pfeil links / rechts | Durch die Losstatus wechseln (verkauft, zurückgezogen, ...) |
| Pfeil nach unten | Auf Saalgebot setzen |
| Pfeil nach oben | Eingabefeld für den Gebotsbetrag öffnen |

![Clerk-Bildschirm, heller Modus](/assets/screenshots/release-3.3-clerk-light.png)

![Clerk-Bildschirm, dunkler Modus](/assets/screenshots/release-3.3-clerk-dark.png)

Die vollständige Beschreibung finden Sie unter [Der Clerk-Bildschirm](../auction/clerk-screen/README.md).

### Live-Statistiken zum Einlieferer auf dem Auktionatorbildschirm

Ein stets sichtbares Panel auf dem Auktionatorbildschirm zeigt Echtzeit-Statistiken zum Einlieferer des aktuellen Loses: Startpreise, Schätzpreise und laufende Summen verkaufter und unverkaufter Lose nach Betrag und Anzahl. Es aktualisiert sich nach jedem Los automatisch.

### Verbesserungen beim verdeckten Mindestpreis

- Ein Farbindikator zeigt Auktionatoren und Clerks den Status des Mindestpreises: rot, bis der Mindestpreis erreicht ist, grün, sobald er erreicht ist. Bieter sehen ihn nie.
- Auktionatoren können den Mindestpreis während der Auktion mit einem einzigen Klick freigeben.
- Lose, die unter einem nicht freigegebenen Mindestpreis zugeschlagen werden, werden automatisch als nicht verkauft / zurückgezogen markiert.

### Verbundene Benutzer nach oben verschoben

Der Block mit den verbundenen Online-Bietern befindet sich jetzt oben auf dem Auktionatorbildschirm und ist damit während der gesamten Auktion besser sichtbar.

![Auktionatorbildschirm, heller Modus](/assets/screenshots/release-3.3-auctioneer-light.png)

![Auktionatorbildschirm, dunkler Modus](/assets/screenshots/release-3.3-auctioneer-dark.png)

### Bildergalerie auf Bieter- und Saalbildschirmen

Lose mit mehreren Bildern zeigen eine automatische Galerie mit bis zu drei Bildern. Jedes Bild wird acht Sekunden lang mit einer Überblendung angezeigt. Bewegen Sie den Mauszeiger über die Galerie, um sie anzuhalten.

![Saalbildschirm, heller Modus](/assets/screenshots/release-3.3-room-light.png)

![Saalbildschirm, dunkler Modus](/assets/screenshots/release-3.3-room-dark.png)

## Versand

Eine umfassende Überarbeitung des gesamten Versandablaufs.

### ShipStation-Integration

ShipStation steht zusätzlich zu den vorhandenen Versandoptionen zur Verfügung. Sendungsnummern und Etiketten werden direkt in Circuit übernommen.

### Neu gestaltete Versandbildschirme

Aufgefrischte Oberfläche für das Dashboard der Versandbestellungen, die Seite für Etiketten und Lieferscheine sowie die Versandeinstellungen.

### Intelligentere Tarifberechnung

Die Tariflogik unterstützt Volumengewicht, Zonen, Bestellungen mit mehreren Paketen, eigene Tarifregeln und Staffelungen sowie Versicherungs- und Bearbeitungsgebühren.

### Verbesserter Statusablauf

Neue Versandstatus (gepackt, bereit, versendet, zugestellt), automatische Statusaktualisierungen von den Versanddienstleistern und Massenaktualisierungen des Status für Betriebe mit hohem Volumen.

### Packinventar

Verfolgen Sie genau, welche Lose in welchem Karton oder Paket verpackt sind.

### Scannen & Packen

Scannen Sie die Barcodes von Losen, um sie Paketen zuzuordnen, für schnelleres und fehlerfreies Packen.

## Leistung

### Schnelleres Laden von Bildern

Vorschaubilder werden in den Formaten WebP und AVIF und in weniger Größen erzeugt, was zu schnelleren Seitenaufrufen und geringeren Speicherkosten führt. Das gilt für neue Uploads.
