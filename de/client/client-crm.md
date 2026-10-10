<!-- i18n source=client/client-crm.md sha=aa4e6ca9ce62 -->
# Kunden-CRM: Zeitleiste, Dokumente und Einlieferungs-Pipeline

Ab Version 3.5 funktioniert die Kundenseite wie ein kleines CRM. Alles, was mit einem Kunden geschehen ist, steht in einer **Zeitleiste**, die Unterlagen des Kunden liegen in einem Tab **Dokumente** mit Ablaufdaten, und Einlieferungsanfragen werden in der **Einlieferungs-Pipeline** vom ersten Kontakt bis zur angelegten Einlieferung verfolgt.

## Die Tabs der Kundenseite

Die Tabs der Kundenseite sind jetzt nach Zweck gruppiert:

| Gruppe | Tabs |
| --- | --- |
| Wer ist das | **Kunde**, **Adressen**, **Dokumente** |
| Was läuft gerade | **Zeitleiste**, **Aufgaben** |
| Als Käufer | **Gebotsinformationen**, **Besichtigungen**, **Gekaufte Lose**, **Auktionsfaktura** |
| Als Einlieferer | **Einlieferungs-Pipeline**, **Einlieferungen**, **Eingelieferte Lose** |
| Geld | **Vorgänge**, **Kontoauszug**, **Statistiken** |
| Protokolle | **E-Mails**, **Aktivitäten** |

Der Tab **History** heißt jetzt **Statistiken**, und **Emails and Documents** heißt jetzt **E-Mails**. Die Schaltfläche **Kundendatenblatt erzeugen** ist vom Tab E-Mails in den Tab Statistiken umgezogen.

## Zeitleiste

Der Tab **Zeitleiste** zeigt in einer nach Tagen gruppierten Übersicht alles, was für den Kunden erfasst wurde: **E-Mails**, **Notizen**, **Anrufe**, **Aufgaben**, **Besichtigungen**, **Aktivitäten** und **Meilensteine** (letztes Gebot, letzter Zuschlag, letzte Einlieferung, zuletzt auf der Website).

1. Öffnen Sie einen Kunden und klicken Sie auf **Zeitleiste**.
2. Klicken Sie oben auf eine Quelle, um sie aus- oder einzublenden. Fahren Sie mit der Maus über eine Quelle und klicken Sie auf **nur**, um ausschließlich diese Quelle zu sehen; **Alle** blendet wieder alles ein.
3. Wählen Sie einen Zeitraum: **30 Tage**, **90 Tage**, **Dieses Jahr**, **Gesamt**, oder legen Sie die Daten **Von** und **bis** fest.
4. Klicken Sie bei einem E-Mail-Eintrag auf **E-Mail anzeigen**, um die E-Mail zu lesen. Anhänge und besichtigte Lose sind in ihren Einträgen verlinkt.
5. Mit **Mehr laden** am unteren Rand laden Sie ältere Einträge einer Quelle.

## Dokumente

Der Tab **Dokumente** listet die Dokumente des Kunden mit **Art**, **Ablaufdatum**, den Dateien, dem Datum und der Person, die sie hinzugefügt hat. Die Dokumenttypen sind ID, Tax form, FFL, Consignment agreement, Bank details und Other.

So fügen Sie ein Dokument hinzu:

1. Klicken Sie auf **Dokument hinzufügen**.
2. Wählen Sie den **Dokumenttyp** und, wenn das Dokument abläuft, das **Ablaufdatum**.
3. Laden Sie die Dateien hoch, ergänzen Sie bei Bedarf einen Notiztext und klicken Sie auf **Notiz hinzufügen**.

Ein Ablaufdatum, das weniger als 30 Tage entfernt ist, wird rot mit der Anzahl der verbleibenden Tage angezeigt, und ein abgelaufenes Dokument ist mit **abgelaufen** gekennzeichnet.

## Notizen und Anrufe

Die Schaltflächen oben auf der Kundenseite heißen jetzt **+ Notizen / Dokumente** und **+ Anrufe**. Sie öffnen ein kurzes Formular, um eine Notiz, ein Dokument oder einen Anruf hinzuzufügen. Vorhandene Notizen, Dokumente und Anrufe werden in diesen Fenstern nicht mehr aufgelistet: Sie finden sie in den Tabs **Zeitleiste** und **Dokumente**.

## Einlieferungs-Pipeline

Eine Einlieferungsanfrage ist eine mögliche Einlieferung, die noch nicht als Einlieferung im System steht: Jemand hat angerufen, geschrieben oder ein Formular auf der Website ausgefüllt. Die Pipeline hält diese Anfragen sichtbar, bis sie zu einer Einlieferung werden oder abgelehnt sind.

Sie finden die Pipeline an zwei Stellen:

- **Einlieferungs-Pipeline** im Hauptmenü: alle Anfragen des Auktionshauses, mit Schnellfiltern für **Phase**, **Quelle** und **Zuständige(r) Mitarbeiter**.
- Der Tab **Einlieferungs-Pipeline** auf der Kundenseite: die Anfragen dieses Kunden.

### Eine Anfrage anlegen

1. Klicken Sie auf **Neue Anfrage**.
2. Wählen Sie den **Kunden** aus, oder geben Sie **Name**, **E-Mail** und **Telefon** ein, wenn die Person noch kein Kunde ist. Wenn Sie von der Kundenseite aus starten, sind diese Felder bereits ausgefüllt.
3. Füllen Sie **Kategorie**, **Geschätzter Wert**, **Quelle**, **Zuständige(r) Mitarbeiter**, **Deadline** und eine **Beschreibung** aus. Sie können bis zu 10 Dateien hochladen.
4. Klicken Sie auf **speichern**.

### Phasen

Eine Anfrage durchläuft diese Phasen: **Anfrage**, **Bewertung**, **Vertrag gesendet**, **Vertrag unterschrieben**, **Erhalten** und dann **Umgewandelt** oder **Abgelehnt**. Bearbeiten Sie die Anfrage und ändern Sie die **Phase**, sobald das Gespräch vorankommt. Jeder Phasenwechsel wird beim Kunden festgehalten und erscheint in der Zeitleiste.

### Eine Anfrage in eine Einlieferung umwandeln

1. Bearbeiten Sie die Anfrage und setzen Sie die **Phase** auf **Umgewandelt**.
2. Wählen Sie unter **In Einlieferung der Auktion umwandeln** die Auktion aus.
3. Klicken Sie auf **speichern**.

In dieser Auktion wird für den Kunden eine Einlieferung angelegt, mit der Provision des Kunden und den zuständigen Mitarbeitern der Anfrage. Die Anfrage zeigt danach einen Link zur Einlieferung. Die Anfrage muss mit einem Kunden verknüpft sein, bevor sie umgewandelt werden kann. Die hochgeladenen Dateien bleiben bei der Anfrage.

### Potenzielle Einlieferer

Der Tab **Potenzielle Einlieferer** der Seite Einlieferungs-Pipeline listet starke Käufer auf, die nie eingeliefert haben: Kandidaten, die Sie für Einlieferungen ansprechen können. Er zeigt ihre Gesamtumsätze als Käufer und Einlieferer, Status, Stufe, Interessen und zuständige Mitarbeiter. Klicken Sie auf einen Kunden, um die Kundenseite zu öffnen.

## Wen anrufen

Auf der Losseite listet der Kasten **Wen anrufen** bis zu 10 Kunden auf, die sich am wahrscheinlichsten für das Los interessieren, auf Grundlage ihrer Gebotshistorie in der Kategorie des Loses. Für jeden Kunden sehen Sie eine Punktzahl, die Signale dahinter (**beobachtet**, **Unterbieter bei ähnlichen Losen**, **bereits geboten**), Telefon, E-Mail und zuständige Mitarbeiter.

Kunden, die E-Mails gesperrt haben, werden ausgelassen, sofern Sie nicht **Kunden mit E-Mail-Sperre einbeziehen** ankreuzen. Es werden nur Kunden mit Gebotshistorie vorgeschlagen.

## Einlieferer-Performance

Die Einlieferungsseite zeigt über den Tabs eine Karte **Einlieferer-Performance**: Gesamtumsätze als Einlieferer und Käufer, Status und Stufe, die letzte Einlieferung, die **Verkaufsquote** und den **Offenen Saldo** des Einlieferers.

## Status, Stufe und automatische Aufgaben

Jede Nacht stuft das System jeden Kunden ein und speichert das Ergebnis als Kunden-Tags, die Sie überall dort verwenden können, wo sich nach Tags filtern lässt:

- **Status**: prospect, new, active, cooling, lapsed oder dormant, je nachdem, wie viele Auktionen vergangen sind, seit der Kunde zuletzt geboten, gekauft oder eingeliefert hat.
- **Stufe**: A, B oder C, nach dem Gesamtumsatz des Kunden als Käufer und Einlieferer. Stufe A sind die obersten 5 %, Stufe B die nächsten 20 %.

Außerdem legt es Folgeaufgaben an, höchstens eine offene Aufgabe jeder Art pro Kunde oder Los:

| Aufgabe | Wird angelegt, wenn |
| --- | --- |
| CRM: lapsing client | Ein Kunde der Stufe A oder B wird cooling oder lapsed. |
| CRM: lot matches | Ein Kunde der Stufe A oder B hat in einer kommenden Auktion mindestens 3 Lose, die zu seinen Interessen passen. |
| CRM: post-sale offer | Ein neues Nachverkaufsangebot für ein Los geht ein. |
| CRM: document expiring | Ein Kundendokument läuft innerhalb von 30 Tagen ab. |
| CRM: new enquiry | Eine Anfrage geht über die Website ein. |

Auf der Seite [Aufgaben](/de/tasks.md) hat der Tab Kunden zwei neue Filter: **Mir zugewiesen** und **Nur CRM-Aufgaben**.

## Zuletzt besucht

Das Verlaufssymbol oben auf der Seite, neben dem Logo, öffnet **Zuletzt besucht**: die Seiten, die Sie zuletzt aufgerufen haben. Es ersetzt die Liste der zuletzt besuchten Seiten, die bisher im Hauptmenü stand.

## FFL validation

Auktionshäuser, die Schusswaffen verkaufen, können die **FFL validation** einschalten. Eine FFL ist ein Kundendokument vom Typ FFL mit einem Ablaufdatum. Wenn die Einstellung eingeschaltet ist:

- Die Kundenliste und die Liste der Auktionsfakturen erhalten eine Spalte **FFL** mit Filter: **Gültig**, **Abgelaufen** oder **Fehlt**.
- Die Seite der Auktionsfaktura zeigt **FFL gültig** oder **FFL erforderlich**, mit einem Link zu den Dokumenten des Kunden.

Eine FFL ohne Ablaufdatum gilt als abgelaufen.

## Für Administratoren

- Das CRM wird mit dem Update eingeschaltet. Die Pipeline benötigt die Berechtigung **manage consignment enquiries**; Wen anrufen, Potenzielle Einlieferer und die Karte Einlieferer-Performance benötigen **view client stat**.
- Die Schwellenwerte für Status und Stufe, die Interessenpunkte und die Aufgabenregeln lassen sich auf der Einstellungsseite **Client CRM** ändern, und jede automatische Aufgabe lässt sich dort ausschalten (Berechtigung **administer client crm**).
- **Enable FFL validation** befindet sich in den Servereinstellungen, Abschnitt Shipping. Die Einstellung ist standardmäßig ausgeschaltet.
