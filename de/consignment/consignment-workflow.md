<!-- i18n source=consignment/consignment-workflow.md sha=558488230d0b -->

# Einlieferungs-Workflow

Der Einlieferungs-Workflow ist anpassbar, das System bringt jedoch einen Standard-Workflow mit.

**Standard-Workflow:**\
****1. Vertrag unterzeichnet -> Diese Aufgabe gilt als erledigt, wenn eine Aktivität vom Typ 'Contract sent' existiert.\
2\. Einlieferungsbestätigung gesendet (vor der Losnummerierung) -> Diese Aufgabe gilt als erledigt, wenn der Bericht gesendet wurde.\
3\. Einlieferungsbestätigung gesendet (nach der Losnummerierung) -> Diese Aufgabe gilt als erledigt, wenn der Bericht gesendet wurde.\
4\. Zuschlagspreise gesendet -> Diese Aufgabe gilt als erledigt, wenn der Bericht gesendet wurde.\
5\. Bericht über zurückgesendete unverkaufte Lose gesendet -> Diese Aufgabe gilt als erledigt, wenn der Bericht gesendet wurde.

**Benutzeroberfläche**

In der Einlieferungstabelle zeigt die Spalte _Workflow_ eine visuelle Anzeige des Status jeder Aufgabe:\


![](</.gitbook/assets/image (33).png>)

:

\
\
Jedes Quadrat steht für die Aufgabe mit der entsprechenden Nummer im Workflow. _Graue_ Aufgaben sind fällig, _grüne Aufgaben sind erledigt._

![Anzeige](</.gitbook/assets/image (37) (3) (3) (1).png>)

&#x20;**API-Informationen**

Siehe den folgenden Callback, um die Standardwerte zu überschreiben.

```
server_consignment_workflow_inventory();
```

 
