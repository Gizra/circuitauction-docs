<!-- i18n source=consignment/how-consignment-statement-are-created.md sha=4c86495fcc4e -->
# So werden Einlieferungsabrechnungen erstellt

Einlieferungsabrechnungen werden während einer Live-Auktion automatisch erstellt und enthalten eine Liste aller Lose des Einlieferers in dieser Auktion. Sie führt jedes Detail eines Loses auf, etwa den Ausruf, ob es verkauft wurde oder nicht, den Zuschlagspreis und alle zusätzlichen Kosten.

Eine Einlieferungsabrechnung hat 5 verschiedene Status:

**Neu** - Eine Einlieferungsabrechnung wurde erstellt.

**In Bearbeitung** - Mitarbeiter bearbeiten die Einlieferungsabrechnung.

**Fertig** - Die Einlieferungsabrechnung nimmt keine weiteren Änderungen mehr entgegen. Wenn Sie die Schaltfläche Print for Accounting verwenden, wechselt die Abrechnung automatisch in diesen Status.

**gesperrt** - Entspricht „Fertig“, bedeutet aber zusätzlich, dass die Abrechnung in ein Microsoft-Dynamics-Buchhaltungssystem exportiert wurde. Dies ist ein optionaler Service. Bitte wenden Sie sich für weitere Details an Ihren Ansprechpartner.

**Storniert** - Ein Mitarbeiter hat die Einlieferungsabrechnung storniert.

**Zweite Einlieferungsabrechnung -** Solange eine Einlieferungsabrechnung offen ist \(d. h. **Neu** oder **In Bearbeitung**\), wird jede Änderung an einem Los oder an den zusätzlichen Kosten in dieser Einlieferungsabrechnung aktualisiert. Sobald die Abrechnung abgeschlossen ist \(d. h. **Fertig** oder **gesperrt**\), erzeugen Änderungen an einem Los eine zweite Einlieferungsabrechnung.

**Was löst einen neuen Einlieferungseintrag aus?**

1. Ein unverkauftes Los wurde verkauft.
2. Eine Gutschrift wurde ausgestellt.
3. Der Einlieferung wurden neue zusätzliche Kosten hinzugefügt. 
4. Bei einem Los, das als „nicht an den Einlieferer auszahlen“ markiert war, wurde die Markierung entfernt.
