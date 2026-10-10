<!-- i18n source=tasks.md sha=a6d91c52b259 -->
# Aufgaben

Sie können verschiedene Arten von Aufgaben erstellen und unterschiedlichen Personen in Ihrer Organisation zuweisen. Aufgaben lassen sich für Kunden, Einlieferungen, Lose, Auktionen und Bestellungen erstellen.

1. Gehen Sie auf die gewünschte Seite \(Kunde, Einlieferung, Los, Auktion oder Bestellung\), für die Sie eine Aufgabe erstellen möchten.
2. Klicken Sie auf den Tab **Aufgaben**. Der Tab zeigt außerdem die Gesamtzahl der Aufgaben für diesen Datensatz an.

![Tab Aufgaben](/assets/screenshots/tasks-tab.png)

## Eine neue Aufgabe erstellen

1. Füllen Sie die Felder unter `Aufgabe hinzufügen` aus

   **Art** - wählen Sie die Aufgabenart aus der Liste.

   **Bearbeiter** - wählen Sie den Benutzer im System, dem die Aufgabe zugewiesen ist.

   **Status** - `kann starten` oder `Kann nicht starten` \(eine Aufgabe, die von einer anderen Aufgabe abhängt, kann noch nicht starten\).

   **Deadline** - geben Sie das Datum ein, bis zu dem die Aufgabe erledigt sein soll.

2. Klicken Sie auf die Schaltfläche `Erstellt`.

![Aufgabe hinzufügen](/assets/screenshots/tasks-add.png)

## Eine Aufgabe löschen

Klicken Sie in der Zeile der Aufgabe auf die Schaltfläche `Löschen`.

![Bild](/assets/screenshots/tasks-delete.png)

## Eine Aufgabe als erledigt markieren

Sobald eine Aufgabe abgeschlossen ist, ändern Sie ihren **Status** auf `fertiggestellt` und klicken Sie in der Zeile der Aufgabe auf `speichern`.

![Bild](/assets/screenshots/tasks-complete.png)

## Standardaufgaben / abhängige Aufgaben

Im Backend des Systems kann der Administrator **Standardaufgaben** festlegen, die automatisch erstellt werden. Zum Beispiel: Jedes Mal, wenn ein Los angelegt wird, werden Aufgaben wie „Los beschreiben“ und „Fotografieren“ erstellt und dem zuständigen Mitarbeiter zugewiesen. Der Administrator kann auch **abhängige Aufgaben** festlegen. Zum Beispiel: Eine Aufgabe „Korrekturlesen“ für ein Los kann erst starten, nachdem die Aufgabe „Los beschreiben“ erledigt ist.
