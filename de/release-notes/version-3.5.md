<!-- i18n source=release-notes/version-3.5.md sha=400917b2eb3d -->
# Version 3.5

Kommendes Release. Version 3.5 konzentriert sich auf Auswertungen, die Kommunikation mit Kunden und Werkzeuge, die die tägliche Verwaltung erleichtern. Zu den Highlights gehören eine neue Seite Auction Timeline, ein überarbeiteter Statistik-Tab für Kunden, ein integrierter Editor für E-Mail-Vorlagen, automatische Zahlungserinnerungen für Rechnungen, die Zwei-Faktor-Authentifizierung mit einer Authenticator-App und ein dunkler Modus für das gesamte Backoffice.

## Auswertungen & Statistiken

### Auction Timeline

<video class="release-video" controls preload="metadata" playsinline src="https://circuit-kubernetes.s3.eu-central-1.amazonaws.com/openmontage/tutorials/release-3.5-auction-timeline/final.mp4">Your browser does not support the video tag. <a href="https://circuit-kubernetes.s3.eu-central-1.amazonaws.com/openmontage/tutorials/release-3.5-auction-timeline/final.mp4">Download the video</a>.</video>

Eine neue Seite **Auction Timeline** (Seitenleiste, unter Auswertungen) bietet einen Rückblick auf eine abgeschlossene Live-Session, wie sie vom Bid-Server aufgezeichnet wurde.

- Filtern Sie nach **Session** und nach **Zeitraum**.
- Die wichtigsten Kennzahlen auf einen Blick: Anzahl verkaufter Lose, abgegebene Gebote und Dauer der Session.
- Eine interaktive Timeline mit **Session summary** mit Autoplay, Zoom und Schieberegler, die Los-Ereignisse, abgegebene Gebote sowie Start- und Endmarkierungen zeigt. Mit den Pfeiltasten oder per Klick springen Sie durch die Lose.
- Ein Bereich **Bids placed** mit dem Zeitpunkt der höchsten Bietaktivität und den erfolgreichsten Losen.
- Ein **Auction Waterfall**, der jedes Los der Reihe nach mit Phase, Verweildauer, Anzahl der Gebote, Zuschlagspreis und Höchstbietendem auflistet. Filtern Sie den Waterfall nach Verkauft, Unverkauft oder Sonstige.

### Neugestaltung der Kundenstatistik

<video class="release-video" controls preload="metadata" playsinline src="https://circuit-kubernetes.s3.eu-central-1.amazonaws.com/openmontage/tutorials/release-3.5-client-statistics/final.mp4">Your browser does not support the video tag. <a href="https://circuit-kubernetes.s3.eu-central-1.amazonaws.com/openmontage/tutorials/release-3.5-client-statistics/final.mp4">Download the video</a>.</video>

Der Tab **Statistiken** auf der Kundenseite wurde neu gestaltet.

- Übersichtskarten: Gesamtsumme der Zuschläge, Gesamtsumme der Gebote, Erfolgsquote und durchschnittlicher Wert eines gewonnenen Loses.
- Ein Diagramm **Bidding activity**, das zwischen Gewonnen und Gewonnen + Unterboten, pro Jahr oder pro Auktion sowie nach Betrag oder Anzahl der Lose umgeschaltet werden kann.
- Ein Diagramm **Collecting areas**, das den gewonnenen Betrag pro Hauptkategorie zeigt. Klicken Sie auf einen Balken, um die darunterliegenden Kategorien zu filtern.
- Eine Liste **Top categories** mit Betrag und Anzahl der Lose pro Kategorie.
- Eine Schaltfläche **Generate Client Data Sheet**, um die Statistik des Kunden zu exportieren.

### Neugestaltung der Gebotsberichte

<video class="release-video" controls preload="metadata" playsinline src="https://circuit-kubernetes.s3.eu-central-1.amazonaws.com/openmontage/tutorials/release-3.5-bids-reports/final.mp4">Your browser does not support the video tag. <a href="https://circuit-kubernetes.s3.eu-central-1.amazonaws.com/openmontage/tutorials/release-3.5-bids-reports/final.mp4">Download the video</a>.</video>

Die Seite **Bids reports** (Seitenleiste) wurde als Satz von Tabs neu aufgebaut, jeweils mit Spaltenfiltern, Sortierung und CSV-Export:

- Bids List (mit einer Option zum Anzeigen gelöschter Gebote)
- Winning bids list
- aktuelle Gebotslage (Hammer Price list)
- Bidder info
- Bidder info grouped
- Flagged items

### Neue Einlieferungsberichte

<video class="release-video" controls preload="metadata" playsinline src="https://circuit-kubernetes.s3.eu-central-1.amazonaws.com/openmontage/tutorials/release-3.5-consignment-reports/final.mp4">Your browser does not support the video tag. <a href="https://circuit-kubernetes.s3.eu-central-1.amazonaws.com/openmontage/tutorials/release-3.5-consignment-reports/final.mp4">Download the video</a>.</video>

Die Einlieferungsseite bietet neue Berichtsaktionen:

- **Einlieferer-Bericht erstellen** mit drei Optionen: **Phase** (zum Beispiel Nach der Auktion), **Detail** (zum Beispiel nur Losnummern) und **Umfang**: nur diese Einlieferung, alle Lose des Einlieferers zusammengefasst oder alle Lose des Einlieferers pro Einlieferung.
- **Generate unsold items list**, **Generate Master sheet Report** und **Generate Proof reading list**.
- Berichte können mit oder ohne Briefkopf erstellt werden, und die zugehörige E-Mail lässt sich vor dem Versand bearbeiten.

### Buchhaltungsexport als CSV und XLSX

<video class="release-video" controls preload="metadata" playsinline src="https://circuit-kubernetes.s3.eu-central-1.amazonaws.com/openmontage/tutorials/release-3.5-export-accounting/final.mp4">Your browser does not support the video tag. <a href="https://circuit-kubernetes.s3.eu-central-1.amazonaws.com/openmontage/tutorials/release-3.5-export-accounting/final.mp4">Download the video</a>.</video>

Auf der Seite **Export Accounting** gibt es im Block Export jetzt die Schaltflächen **CSV** und **XLSX**. Sie laden die aktuell gefilterte Liste der Rechnungen oder Einliefererabrechnungen als Tabelle herunter. Durch diesen Download werden die Einträge nicht als an die Buchhaltung exportiert markiert.

## Rechnungen & E-Mails

### Vorschau von E-Mail und PDF in den Sammelaktionen für Bestellungen

<video class="release-video" controls preload="metadata" playsinline src="https://circuit-kubernetes.s3.eu-central-1.amazonaws.com/openmontage/tutorials/release-3.5-orders-preview-email/final.mp4">Your browser does not support the video tag. <a href="https://circuit-kubernetes.s3.eu-central-1.amazonaws.com/openmontage/tutorials/release-3.5-orders-preview-email/final.mp4">Download the video</a>.</video>

Im Block **Batch actions** der Seite Rechnungen zeigt die neue Schaltfläche **Preview email & PDF** die tatsächliche E-Mail und das Rechnungs-PDF mit echten Daten an, bevor Sie auf Anwenden klicken, um sie an die ausgewählten Bestellungen zu senden.

### Liste gesendeter E-Mails auf der Rechnungsseite

<video class="release-video" controls preload="metadata" playsinline src="https://circuit-kubernetes.s3.eu-central-1.amazonaws.com/openmontage/tutorials/release-3.5-invoice-email-list/final.mp4">Your browser does not support the video tag. <a href="https://circuit-kubernetes.s3.eu-central-1.amazonaws.com/openmontage/tutorials/release-3.5-invoice-email-list/final.mp4">Download the video</a>.</video>

Jede Rechnungsseite endet jetzt mit einer Tabelle **Emails and Documents**, die jede für diese Rechnung erzeugte E-Mail und jedes Dokument auflistet: Erstellungs- oder Versanddatum, Titel, Art, Empfänger, Inhalt, angehängte Dokumente und Autor (einschließlich der automatisch vom System versendeten E-Mails).

### Editor für E-Mail-Vorlagen

<video class="release-video" controls preload="metadata" playsinline src="https://circuit-kubernetes.s3.eu-central-1.amazonaws.com/openmontage/tutorials/release-3.5-email-templates/final.mp4">Your browser does not support the video tag. <a href="https://circuit-kubernetes.s3.eu-central-1.amazonaws.com/openmontage/tutorials/release-3.5-email-templates/final.mp4">Download the video</a>.</video>

Auf der neuen Seite **Email Templates** (Seitenleiste) können Sie alle globalen E-Mail-Vorlagen für Rechnungen, Versand, Bieterbenachrichtigungen und andere Abläufe ansehen und bearbeiten.

- Die Vorlagen sind nach Bereichen gruppiert (Rechnungen / Bestellungen, Kunden / Bieterbenachrichtigungen, ...) und können pro Sprache bearbeitet werden.
- Jede Vorlage hat einen Betreff und einen Rich-Text-Inhalt. Im Inhalt ist HTML erlaubt.
- Klicken Sie auf einen **Token** (zum Beispiel `@client-name`, `@invoice-id`, `@checkout-url`, `!signature`), um ihn einzufügen. Token werden beim Versand der E-Mail durch aktuelle Werte ersetzt.
- Das Speichern einer Vorlage aktualisiert alle künftigen E-Mails, die sie verwenden.

### Automatische Zahlungserinnerungen für Rechnungen

<video class="release-video" controls preload="metadata" playsinline src="https://circuit-kubernetes.s3.eu-central-1.amazonaws.com/openmontage/tutorials/release-3.5-payment-reminders/final.mp4">Your browser does not support the video tag. <a href="https://circuit-kubernetes.s3.eu-central-1.amazonaws.com/openmontage/tutorials/release-3.5-payment-reminders/final.mp4">Download the video</a>.</video>

Unbezahlte Rechnungen können jetzt automatisch in drei Stufen angemahnt werden: ein **Payment reminder**, eine Mitteilung **Past due** und ein **Final reminder**.

- Die **standortweiten Standardwerte** legen für jede Stufe die Anzahl der Tage fest, nachdem eine Rechnung abgeschlossen und für den Kunden sichtbar ist (zum Beispiel 7, 14 und 21 Tage).
- Auf der **Auktionsseite** aktivieren Sie unter Auction Settings mit **Automatische Zahlungserinnerungen** die Erinnerungen für diese Auktion. Die drei Fristen können Sie pro Auktion überschreiben. Auf der Seite Rechnungen weist ein Hinweis auf den aktiven Zeitplan hin.
- Ausgeblendete Rechnungen werden übersprungen. Wenn Sie die Kundensichtbarkeit einer Rechnung in den Sammelaktionen auf ausgeblendet setzen, werden auch deren Erinnerungen angehalten.
- Die E-Mails verwenden die drei Vorlagen **Invoice payment reminder**, **Invoice past due** und **Invoice final payment reminder**, die Sie auf der Seite Email Templates anpassen können.

### Adressaufkleber auf A4-Bögen drucken

<video class="release-video" controls preload="metadata" playsinline src="https://circuit-kubernetes.s3.eu-central-1.amazonaws.com/openmontage/tutorials/release-3.5-address-sticker-sheet/final.mp4">Your browser does not support the video tag. <a href="https://circuit-kubernetes.s3.eu-central-1.amazonaws.com/openmontage/tutorials/release-3.5-address-sticker-sheet/final.mp4">Download the video</a>.</video>

In der Sammelaktion **Address sticker** auf der Seite Kunden bietet die Liste **Format** jetzt zusätzlich zum Einzeletikett den **Etikettenbogen (2 × 5)**, sodass die Standardadresse jedes ausgewählten Kunden auf handelsübliche A4-Etikettenbögen gedruckt werden kann.

## Aufgaben & Support

### Auf Aufgaben vom Typ "Ask about item" antworten

<video class="release-video" controls preload="metadata" playsinline src="https://circuit-kubernetes.s3.eu-central-1.amazonaws.com/openmontage/tutorials/release-3.5-task-reply/final.mp4">Your browser does not support the video tag. <a href="https://circuit-kubernetes.s3.eu-central-1.amazonaws.com/openmontage/tutorials/release-3.5-task-reply/final.mp4">Download the video</a>.</video>

Fragen, die Bieter zu einem Los senden, erscheinen unter [Aufgaben](../tasks.md) als Aufgaben vom Typ *Ask about item*. Eine neue Aktion **Beantwortet** öffnet einen E-Mail-Editor:

- Die Frage des Bieters und das Los werden oben angezeigt.
- Die Antwort wird aus der Vorlage *Your question about lot* vorausgefüllt; Token und Dateianhänge stehen zur Verfügung.
- Änderungen können nur für diese E-Mail gespeichert oder in die globale Vorlage zurückgeschrieben werden.
- Nach dem Senden wird die Aufgabe als erledigt markiert, und die Antwort wird in den E-Mails des Kunden protokolliert.

### Integrierte Support-Tickets

<video class="release-video" controls preload="metadata" playsinline src="https://circuit-kubernetes.s3.eu-central-1.amazonaws.com/openmontage/tutorials/release-3.5-support-tickets/final.mp4">Your browser does not support the video tag. <a href="https://circuit-kubernetes.s3.eu-central-1.amazonaws.com/openmontage/tutorials/release-3.5-support-tickets/final.mp4">Download the video</a>.</video>

Eine neue Seite **Support-Tickets** (Seitenleiste und ein Verknüpfungssymbol in der oberen Leiste) listet Ihre Supportanfragen an das CircuitAuction-Team mit ihrem Status auf: offen, in Bearbeitung, gelöst, live ausgeliefert und geschlossen. Tickets lassen sich nach Status und nach Tag filtern.

## Auktionen & Gebote

### Import von HiBid-Geboten

<video class="release-video" controls preload="metadata" playsinline src="https://circuit-kubernetes.s3.eu-central-1.amazonaws.com/openmontage/tutorials/release-3.5-hibid-import/final.mp4">Your browser does not support the video tag. <a href="https://circuit-kubernetes.s3.eu-central-1.amazonaws.com/openmontage/tutorials/release-3.5-hibid-import/final.mp4">Download the video</a>.</video>

Der Tab **Gebotsimport** der Auktionsseite bietet neben den vorhandenen Importen für [Philasearch](../data-migration/bids-philasearch.md), [Delcampe](../data-migration/bids-delcampe.md), [Auction Mobility](../data-migration/bids-mobility.md), [SAN](../data-migration/bids-san.md) und Invaluable einen neuen **HiBid Import**.

- Fügen Sie die Google-Drive-URL der Tabelle mit dem HiBid-Export der Auktionsergebnisse ein oder laden Sie die Datei direkt hoch.
- Erwartete Spalten: Lot, Winning Bidder (paddle), Name, Address, State, Zip Code, Email, Phone und der Verkaufspreis.
- Lose, deren Mindestpreis **Not Met** war, werden mit einer Notiz importiert.
- Mit **Gebote importieren** starten Sie den Import, mit **fehlgeschlagene Gebote importieren** wiederholen Sie die fehlgeschlagenen Zeilen.

### Auktion zurücksetzen und synchronisieren

<video class="release-video" controls preload="metadata" playsinline src="https://circuit-kubernetes.s3.eu-central-1.amazonaws.com/openmontage/tutorials/release-3.5-reset-sale-sync/final.mp4">Your browser does not support the video tag. <a href="https://circuit-kubernetes.s3.eu-central-1.amazonaws.com/openmontage/tutorials/release-3.5-reset-sale-sync/final.mp4">Download the video</a>.</video>

Die neue Schaltfläche **Sale zurücksetzen und synchronisieren** auf der Auktionsseite stellt alle Lose der Auktion erneut für die Suchindizierung in die Warteschlange, synchronisiert die Lose erneut mit dem Bid-Server, baut das Sale-JSON neu auf und sendet, sobald diese Warteschlangen abgearbeitet sind, einen Cache-Reset an die Website für Kunden. Der Fortschritt jedes Schritts wird neben der Schaltfläche angezeigt. Verwenden Sie sie, wenn die Website veraltete Daten zu einer Auktion anzeigt.

## System

### Zwei-Faktor-Authentifizierung mit einer Authenticator-App

<video class="release-video" controls preload="metadata" playsinline src="https://circuit-kubernetes.s3.eu-central-1.amazonaws.com/openmontage/tutorials/release-3.5-authenticator-setup/final.mp4">Your browser does not support the video tag. <a href="https://circuit-kubernetes.s3.eu-central-1.amazonaws.com/openmontage/tutorials/release-3.5-authenticator-setup/final.mp4">Download the video</a>.</video>

Für Mitarbeiter-Logins kann jetzt zusätzlich zum Passwort ein sechsstelliger Code aus einer Authenticator-App (Authy, Google Authenticator, Microsoft Authenticator) verlangt werden. Siehe [Anmelden mit einer Authenticator-App](../logging-in-with-an-authenticator-app.md).

- Aktivierung für die gesamte Installation in den Servereinstellungen (standardmäßig aus) oder pro Konto mit **Always require an authenticator app for this account**.
- Beim ersten Login nach der Aktivierung erscheint einmalig eine **Einrichtungsseite**: Scannen Sie den QR-Code (oder geben Sie den manuellen Schlüssel ein) in der App und geben Sie den ersten Code ein. Andere Seiten bleiben gesperrt, bis die Einrichtung abgeschlossen ist.
- Bei jedem weiteren Login wird unter dem Passwort der Code abgefragt. Bei der Anmeldung mit Google wird er abgefragt, nachdem Google das Konto bestätigt hat.
- Administratoren sehen in der Benutzerliste eine Spalte **Authenticator** und können im Benutzerformular die Authenticator-App zurücksetzen (**Reset authenticator app**), wenn jemand sein Telefon verliert.
- Die Servereinstellungen haben außerdem einen Tab **Sessions & tokens**, in dem Sie festlegen, wie lange API-Token und Browser-Sessions gültig bleiben.

### Dunkler Modus

<video class="release-video" controls preload="metadata" playsinline src="https://circuit-kubernetes.s3.eu-central-1.amazonaws.com/openmontage/tutorials/release-3.5-dark-mode/final.mp4">Your browser does not support the video tag. <a href="https://circuit-kubernetes.s3.eu-central-1.amazonaws.com/openmontage/tutorials/release-3.5-dark-mode/final.mp4">Download the video</a>.</video>

Ein Mond-Symbol in der oberen Leiste neben der Benachrichtigungsglocke schaltet das gesamte Backoffice auf ein dunkles Design um. Die Auswahl wird für Ihren Benutzer gespeichert.

### Gesundheitsmonitor des Bid-Servers

<video class="release-video" controls preload="metadata" playsinline src="https://circuit-kubernetes.s3.eu-central-1.amazonaws.com/openmontage/tutorials/release-3.5-health-monitor/final.mp4">Your browser does not support the video tag. <a href="https://circuit-kubernetes.s3.eu-central-1.amazonaws.com/openmontage/tutorials/release-3.5-health-monitor/final.mp4">Download the video</a>.</video>

Die Schaltfläche **Health** in der oberen Leiste öffnet einen Monitor für die Verbindung zum Bid-Server und seine Warteschlangen. Die Warteschlange startet sich bei einem Stillstand jetzt automatisch neu, sodass sich das Live-Bieten ohne manuelles Eingreifen erholt.
