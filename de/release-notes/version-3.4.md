<!-- i18n source=release-notes/version-3.4.md sha=f92768f8bcef -->
# Version 3.4

Veröffentlicht im März 2026. Die Live-Bietengine wurde auf Geschwindigkeit neu aufgebaut, und das Backoffice erhielt ein Formular Quick Add Item, PDF- und Video-Dateien, Sammlertypen, Buy It Now, Mindestgebote, ein Besichtigungsmodul, einen Saldoverlauf, Zahlungen über Authorize.net und mehr.

## Live-Bietengine

### Live-Bieten ist bis zu fünfmal schneller

Die Live-Bietetechnologie wurde auf Redis und Go neu aufgebaut und ersetzt den bisherigen Node.js-Stack. Die Verarbeitung eines Gebots dauert jetzt nur noch zweistellige Millisekunden, mit Antwortzeiten unter 100 ms in Web-, Mobil- und Podium-Apps. Alle Live-Funktionen profitieren von dieser Änderung.

## Lose & Katalogisierung

### Quick Add Item

Ein schlankes Formular für die schnelle Losaufnahme, erreichbar über das Hauptmenü und direkt aus einer Einlieferung.

- Es werden nur die Felder angezeigt, die Sie benötigen. Die Liste der Felder ist in den Einstellungen konfigurierbar.
- Das Formular wird nach jedem Speichern zurückgesetzt, sodass Sie direkt weitere Lose erfassen können.
- Jede Einlieferung hat einen **QR-Code**. Scannen Sie ihn mit einem Smartphone oder Tablet, um Lose beim Gang durch den Raum zu erfassen. Auf dem Mobilgerät können Sie Fotos mit der Kamera aufnehmen oder aus der Galerie auswählen.

### PDF- und Video-Dateien

Hängen Sie MP4-Videos und PDF-Dateien an Lose an. Sie werden in der Los-Galerie auf der Website angezeigt, was für Zustandsberichte, Zertifikate und Rundgänge nützlich ist.

### Sammlertyp

Typspezifische Datenfelder: Münzen erhalten Felder für den Erhaltungsgrad, Kunstwerke Medium und Abmessungen und so weiter.

### Mehrfach-Bild-Upload per Drag & Drop

Laden Sie mehrere Bilder gleichzeitig hoch, indem Sie sie auf das Los ziehen, siehe [Massen-Upload von Losbildern](../sale/how-to-mass-upload-items-images.md).

### Formatierung entfernen

Entfernen Sie unerwünschte Formatierungen aus eingefügtem Text mit einem Klick in Textfeldern.

### Vermittlungsgebühr pro Los

Vermittlungsgebühren können jetzt pro Los festgelegt werden, das Importformat finden Sie unter [Vermittlungsgebühren für Einlieferungen](../data-migration/consignment-finder-fees.md).

## Gebote & Auktionen

### Buy It Now

Legen Sie einen festen Kaufpreis fest, damit Kunden ein Los sofort kaufen können, ohne die Auktion abzuwarten.

### Mindestgebote

Vollständige Unterstützung für Mindestgebote. Auktionatoren können während einer Live-Auktion vom Podium aus einen Mindestpreis entfernen.

### Zugangsart der Auktion

Steuern Sie, wer in jeder Auktion bieten darf. Legen Sie Standard-Bietschritte fest und beschränken Sie den Zugang über Kunden-Tags, zum Beispiel für eine reine VIP-Auktion.

### Alle Lose abschließen

Schlagen Sie alle Lose einer Vorab-Auktion mit einer Aktion von der Auktionsseite aus erneut zu. Nützlich beim Abschluss von Auktionen mit schriftlichen Geboten.

### Auction-Mobility-Integration

Exportieren Sie den Katalog nach Auction Mobility und importieren Sie Gebote von dort, zusätzlich zu den bestehenden Integrationen von StampCircuit, SAN, PhilaSearch und Delcampe, siehe [Auction-Mobility-Gebote](../data-migration/bids-mobility.md).

## Kunden & Finanzverwaltung

### Besichtigungsmodul

Verfolgen Sie Besichtigungen vor der Auktion: wer welche Lose besichtigt hat und wann Lose entnommen und zurückgegeben wurden. Für Besichtigungen per Post erstellen Sie eine Besichtigungsrechnung, die die versendeten Lose und Kosten auflistet.

### Saldoverlauf

Ein vollständiges Hauptbuch der finanziellen Aktivitäten jedes Kunden: Rechnungen, Zahlungen, Gutschriften und Anpassungen, statt nur einer Momentaufnahme des Saldos.

### Bieteralias

Weisen Sie einem Kunden einen Anzeige-Alias zu, der bei Live-Auktionen verwendet wird.

### Auswahl der Rechnungsadresse

Beim Bearbeiten einer Rechnung wählen Sie eine der gespeicherten Adressen des Kunden aus, statt eine eigene einzutippen.

### Opt-in für Printmaterial

Kunden können sich auf ihrer Kontoseite auf der Website für gedruckte Kataloge und Zusendungen an- oder abmelden.

## Versand & Verpackung

### Nachverfolgung der Versandkartons

Markieren Sie, in welchen Karton jedes Paket kommt. Mit dem QR-Scanner scannen Sie Lose beim Verpacken, ohne etwas eintippen zu müssen.

## Zahlungen & Abonnements

### Authorize.net-Integration

Kunden können Rechnungen per Kreditkarte über Authorize.net bezahlen, siehe [Abrechnung & Zahlungen](../website/billing.md).

### Magazinabonnements

Verkaufen Sie Magazinabonnements direkt über Circuit Auction. Kunden schließen das Abonnement auf Ihrer Website ab und bezahlen dort, siehe [Abonnement kaufen](../website/subscription-purchase.md).

## System & Oberfläche

### Überarbeitung der React-App

Das React-Frontend ist schneller und hängt nicht mehr von der WordPress-Synchronisierung ab, wodurch sich jede Website leichter anbinden lässt, siehe [Website (einbettbare Blöcke)](../website/README.md).

### Neugestaltung der Auktionsseite

Ein übersichtlicheres Layout mit strukturiertem Ablauf und weniger Schaltflächen, siehe [So erstellen Sie eine Auktion](../sale/how-to-create-a-sale.md).

### Aufteilung der Aktivitätsseiten

Aktivitäten verteilen sich jetzt auf zwei Seiten: eine für die Ereignisprotokollierung mit besserer Filterung und eine für E-Mails und Dokumente.

### Flood-Benachrichtigungen

Mitarbeiter erhalten eine E-Mail-Warnung, wenn eine Login-Flut erkannt wird, und können die Sperre für verifizierte Benutzer aufheben.

### Aufgaben-Benachrichtigungen

E-Mail-Benachrichtigungen werden versendet, wenn im Backoffice Aufgaben erstellt werden, siehe [Aufgaben](../tasks.md).

## Premium-Dienste

Mit diesem Release wurden zwei kostenpflichtige Dienste eingeführt. Kontaktieren Sie Circuit Auction für Details und ein Angebot.

- **Elite-Website-Paket mit WebDrop**: eine Website auf Basis von Astro, gehostet auf Cloudflare Workers, mit Optimierung für Suchmaschinen und KI-Suche, erstellt und betreut von WebDrop und koordiniert von Circuit Auction.
- **Eigene Vektordatenbank für Katalog-KI**: Binden Sie Ihre eigenen Referenzdatenbanken (Briefmarkenkataloge, Münzreferenzen, Provenienz von Kunstwerken) an die KI-Katalogisierung an, sodass Beschreibungen auf Ihren maßgeblichen Quellen beruhen. Die Datenbank kann aus vorhandenen Datendateien oder PDFs aufgebaut werden.
