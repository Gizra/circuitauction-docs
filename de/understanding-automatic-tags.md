<!-- i18n source=understanding-automatic-tags.md sha=30d308d98c1e -->
# Automatische Tags und Begriffe verstehen
*Circuit Auction — Leitfaden für Backoffice-Mitarbeiter*

## Worum es in diesem Leitfaden geht

Bei der Arbeit im Backoffice sehen Sie Tags und Bezeichnungen an Kunden, Losen, Bestellungen und Rechnungen, die niemand von Hand eingegeben hat. Das System fügt sie automatisch hinzu, wenn bestimmte Dinge geschehen — ein Kunde ändert seine eigenen Daten, der Verkauft-Status eines Loses stimmt nicht überein, ein Saldo wird negativ und so weiter.

Dieser Leitfaden erklärt für jeden Tag, dem Sie begegnen können: **was er bedeutet**, **warum er erschienen ist** und **was er beeinflusst**. Die meisten Entitätstabellen (die Kundenliste, die Lose-Liste usw.) lassen sich außerdem nach diesen Tags filtern, um alle Datensätze zu finden, die einen Tag tragen.

**Wie Tags entstehen.** Im Hintergrund sind Tags in Gruppen organisiert (zum Beispiel „Kunden-Tags“, „Los-Tags“, „Aufgabenarten“). Das System verwendet einen vorhandenen Tag wieder, falls es ihn schon gibt, und legt einen neuen Tag nur an, wenn er zum ersten Mal gebraucht wird. Deshalb kann ein brandneuer Tag in einer Filterliste auftauchen, wenn eine Situation zum ersten Mal eintritt — das ist kein Fehler.

---

## Tags bei Kunden
*Sichtbar auf der Kundenseite; filterbar in der Kundenliste.*

### Open Balance
- **Bedeutung:** Der Kunde schuldet derzeit Geld (sein Saldo ist negativ).
- **Warum er erscheint:** Wird automatisch hinzugefügt, wenn der Saldo des Kunden neu berechnet wird (bei der Verarbeitung von Bestellungen/Einlieferungen) und negativ ausfällt. Er **entfernt sich auch automatisch**, sobald der Saldo wieder null oder positiv ist und der Datensatz erneut verarbeitet wird.
- **Auswirkung:** Ein **Hinweis nur zu Ihrer Information** — er hilft Ihnen, Kunden mit offenen Beträgen zu erkennen und zu filtern. Er blockiert **weder** das Bieten noch den Checkout noch irgendetwas anderes. Verstehen Sie ihn als Anstoß zum Nachfassen, nicht als Garantie, dass das System etwas gestoppt hat.

### Duplicate Email
- **Bedeutung:** Dieser Kunde teilt sich eine Haupt-E-Mail-Adresse mit einem anderen vorhandenen Kunden.
- **Warum er erscheint:** Erscheint bei Kunden, die über **Import oder externe Synchronisierung** übernommen wurden (nicht bei normalen Bearbeitungen am Bildschirm). Wenn Sie versuchen, eine doppelte E-Mail-Adresse **selbst am Bildschirm** zu speichern, blockiert das System das Speichern und zeigt Ihnen das kollidierende Konto — diesen Tag legen Sie also in der Regel nicht von Hand an.
- **Auswirkung:** Ein Prüfhinweis, damit Sie doppelte Konten finden und zusammenführen oder korrigieren können.
- **⚠️ Wichtig:** Dieser Tag wird **nicht** von selbst entfernt. Auch nachdem Sie das Duplikat bereinigt haben, bleibt der Tag bestehen, bis ihn jemand manuell entfernt. Gehen Sie nicht davon aus, dass ein Kunde noch einen Konflikt hat, nur weil der Tag vorhanden ist — prüfen, beheben, dann den Tag entfernen.

### Warning
- **Bedeutung:** Zu diesem Kunden ist eine Warnnotiz erfasst.
- **Warum er erscheint:** Der Tag spiegelt einfach das **Feld Warning** des Kunden wider. Steht in diesem Feld Text, wird der Tag beim nächsten Speichern hinzugefügt; wird das Feld geleert, wird der Tag beim nächsten Speichern entfernt.
- **Auswirkung:** Damit können Sie Kunden markieren und filtern, die besondere Sorgfalt brauchen. Zum Ändern bearbeiten Sie das Feld Warning beim Kunden — versuchen Sie nicht, den Tag direkt hinzuzufügen oder zu entfernen, da er sich einfach wieder mit dem Feld abgleicht.

### No Address
- **Bedeutung:** Zum Kunden ist keine verwendbare Adresse hinterlegt.
- **Warum er erscheint:** Wird bei jedem Speichern des Kunden automatisch verwaltet: entfernt, sobald der Kunde eine Standardadresse hat (oder automatisch eine zugewiesen werden kann), hinzugefügt, wenn er keine hat.
- **Auswirkung:** Hilft Ihnen, Datensätze zu finden, an die nicht korrekt versendet oder berechnet werden kann. Erledigt sich von selbst, sobald eine gültige Adresse hinzugefügt wird.

### Sync Error
- **Bedeutung:** Der Versuch, diesen Kunden mit einem externen System zu synchronisieren, ist fehlgeschlagen.
- **Warum er erscheint:** Wird hinzugefügt, wenn die externe Kundensynchronisierung läuft und für diesen Datensatz einen Fehler meldet.
- **Auswirkung:** Markiert Datensätze, die das verbundene System nicht erreicht haben, damit sie erneut versucht oder untersucht werden können.

### VIP
- **Bedeutung:** Ein als VIP markierter Kunde.
- **Auswirkung:** Beeinflusst die Behandlung zugehöriger Aufgaben und ermöglicht es, Ihre VIPs zu filtern.

### Active / Passive
- **Bedeutung:** Der Aktivitätsstatus des Kunden. (Je nachdem, wo sie eingerichtet wurden, sehen Sie möglicherweise auch die deutschen Entsprechungen **Aktiv / Passiv** sowie die englischen **Active / Passive**.)
- **Auswirkung:** Dient dazu, aktive Kunden von inaktiven zu trennen, für Filter und die Katalogsteuerung.

### Expert
- **Bedeutung:** Ein als Experte gekennzeichneter Kunde. Ein Standard-Tag, der mit dem System eingerichtet wird.

---

## Tags bei Losen
*Sichtbar auf der Losseite; filterbar in der Lose-Liste.*

### Sold Status Sync Error
- **Bedeutung:** Der Verkauft-Status des Loses im Backoffice stimmt nicht mit dem Bid-Server überein (zum Beispiel zeigt das Backoffice „verkauft“, die Bieterseite aber „unverkauft“).
- **Warum er erscheint:** Wird bei einer Statusprüfung automatisch hinzugefügt, wenn die beiden Systeme voneinander abweichen.
- **Auswirkung:** Markiert Lose, deren Verkauft-Status vor der Rechnungsstellung oder Auszahlung abgeglichen werden muss.

> **⚠️ Zum Tag „Sold Status Sync Fixed“ — bitte lesen.**
> Gelegentlich sehen Sie einen Tag namens **Sold Status Sync Fixed**. Behandeln Sie ihn **nicht** als verlässliches Signal dafür, dass etwas behoben wurde. In der Praxis entfernt das System, wenn ein echter Synchronisierungsfehler behoben wird, den Tag **Error**, und das Los hat danach in der Regel **gar keinen Tag mehr** — keinen „Fixed“-Tag. Am sichersten lesen Sie es daher so: Ein Los mit **Sold Status Sync Error** braucht weiterhin Aufmerksamkeit; ein Los mit **keinem** der beiden Tags ist in Ordnung. Verlassen Sie sich nicht auf „Fixed“, um eine Lösung zu bestätigen. Wenn dieser Tag in der Lose-Liste für Verwirrung sorgt, melden Sie das dem Entwicklungsteam.

### Featured item
- **Bedeutung:** Ein Los, das als hervorgehoben markiert ist.
- **Auswirkung:** Wird für Werbung und zum Filtern hervorgehobener Lose verwendet.

---

## Tags bei Bestellungen und Rechnungen
*Sichtbar auf der Bestell-/Rechnungsseite.*

### Bestell-Tags (beim Drucken und Packen hinzugefügt)
- **Bedeutung:** Bestellungen erhalten und verlieren Tags automatisch, während sie den Druck-/Packablauf durchlaufen.
- **Auswirkung:** Damit können Sie verfolgen, wo sich eine Bestellung im Packprozess befindet, und die Bestellliste entsprechend filtern.

**Gebührenpositionen, die Ihnen auf Rechnungen auffallen können.** Manche Gebühren werden automatisch als benannte Arten erstellt — am häufigsten eine **Kreditkartengebühr**. Sie erscheinen als Gebührenzeilen auf der Bestellung/Rechnung und nicht als Tags. Das System erzeugt sie, wenn die jeweilige Gebühr anfällt.

---

## Die Aufgabenwarteschlange
*Dies sind keine Tags auf einer Seite — jeder Eintrag ist eine **Aufgabenart**, die in der Aufgabenwarteschlange landet und von jemandem bearbeitet werden muss.*

### Client edited alert
- **Bedeutung:** Ein Kunde hat seine eigenen Daten auf der Kundenseite geändert (Self-Service), und Mitarbeiter sollten die Änderung prüfen.
- **Warum er erscheint:** Wird nur ausgelöst, wenn der **Kunde selbst** ein überwachtes Feld bearbeitet — Name, Anrede, E-Mail, Mobiltelefon, Telefon, Firma, Website, Geburtsdatum, Sprache, Versandhinweise oder wichtige Adressfelder. Änderungen durch Mitarbeiter lösen ihn nicht aus.
- **Auswirkung:** Erstellt eine Aufgabe (der Standard-Sekretärin zugewiesen, fällig am nächsten Tag) mit einer Vorher-/Nachher-Tabelle der genauen Änderungen. Sie ist dem Kunden zugeordnet. **Sie befindet sich in der Aufgabenwarteschlange — es ist kein Banner auf der Kundenseite.**

### Payment approval required
- **Bedeutung:** Eine Bestellung oder Zahlung braucht eine manuelle Freigabe, bevor sie fortgesetzt werden kann.
- **Auswirkung:** Erscheint in der Warteschlange, damit ein Mitarbeiter sie freigibt.

### Buy Now Order
- **Bedeutung:** Ein Buy-Now-Kauf muss bearbeitet werden.

### Mutate Order
- **Bedeutung:** Eine Bestellung braucht eine Änderung/Korrektur.

### Under Extension Request / Under Extension - Not Genuine
- **Bedeutung:** Aufgaben zu Verlängerungen der Bietzeit — eine für eine berechtigte Anfrage, eine als nicht berechtigt markiert.

### Received export confirmation
- **Bedeutung:** Es ist eine Bestätigung eingegangen, dass ein Export in ein externes System (z. B. Buchhaltung/Dynamics) erfolgreich war.

### Publish an event
- **Bedeutung:** Eine öffentliche Aufgabe zum Veröffentlichen einer Veranstaltung.
- **Hinweis:** Der Name ist im System falsch geschrieben („Pushlish/Puplish“). Das ist vorerst Absicht, damit das System ihn weiterhin erkennt — versuchen Sie nicht, ihn über die Oberfläche zu „korrigieren“.

---

## Einträge im Aktivitätsprotokoll
*Sie erscheinen im Aktivitätsverlauf eines Kunden oder einer Einlieferung — sie halten fest, dass etwas geschehen ist.*

- **Condition Report** — ein Zustandsbericht wurde erstellt.
- **Contract sent** / **Contract Signed** — der Einlieferungsvertrag wurde versendet / unterzeichnet.
- **Statement of account** — ein Kontoauszug wurde ausgestellt.
- **Catalog sent** — ein Katalog wurde an den Kunden gesendet.
- **Letter to client** — ein Brief wurde protokolliert.
- **Google Drive Document** — ein Drive-Dokument wurde verknüpft.
- **Subscription ended** — das Abonnement eines Kunden ist beendet.
- **Unsold Returned** — unverkaufte Lose wurden an den Einlieferer zurückgegeben.

---

## Begriffe im Hintergrund (in der Regel können Sie sie ignorieren)

Manche Begriffe dienen hauptsächlich der internen Buchführung des Systems und erfordern selten die Aufmerksamkeit von Mitarbeitern. Einige davon können Ihnen gelegentlich begegnen:

- **Externe Systemkennungen** (z. B. **Authorize.net**, **PayPal**, **Reserved Bidder number**) — verknüpfen einen Datensatz mit dem externen System, dem seine Referenznummer gehört.
- **Self** — wird bei der Synchronisierung von Losen zwischen verbundenen Backoffices verwendet; es bedeutet einfach „dieses Backoffice“.
- **Katalogteile** — Unterabschnitte des Katalogs einer Auktion. Derselbe Teilname kann für jede Auktion separat existieren, es ist also normal, denselben Namen über verschiedene Auktionen hinweg mehrfach zu sehen.
- **Beziehungsdatensätze** (z. B. **Merge**, **Source order**) — halten fest, dass zwei Kunden zusammengeführt wurden, oder verknüpfen eine Gutschrift mit ihrer ursprünglichen Bestellung.
- Verschiedene Einrichtungs-, Import- und Kategoriebegriffe (Verpackungsarten, Zahlungsarten, Namenspräfixe, Druckoptionen usw.) werden bei Datenimporten und der Ersteinrichtung angelegt. Sie erscheinen in Filterlisten, sind aber keine Handlungsaufforderungen.

---

## Wenn etwas nicht stimmt

Diese Tags werden durch automatische Regeln erzeugt. Wenn ein Tag erscheint, obwohl Sie ihn nicht erwarten, nach der Behebung des zugrunde liegenden Problems bestehen bleibt (denken Sie daran: **Duplicate Email** und die Sync-Tags verschwinden nicht immer von selbst) oder dem widerspricht, was Sie im Datensatz sehen, wenden Sie sich an das Entwicklungsteam, statt anzunehmen, dass die Daten falsch sind — der Tag und das zugrunde liegende Feld können gelegentlich nicht im Gleichklang sein.
