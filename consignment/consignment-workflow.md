---
description: >-
  Consignment workflow allow to track milestones within the consignment
  workflow.
---

# Consignment Workflow

Consignment workflow is customisable,  but the system comes with  a default workflow in place.

**Default workflow:**\
****1. Contract signed -> This task is considered done when an activity of type 'Contract sent' exists.\
2\. Consignment confirmation sent (before Lot numbering) -> This task is considered done if the report was sent.\
3\. Consignment confirmation sent (after Lot numbering) -> This task is considered done if the report was sent.\
4\. Price realised sent -> This task is considered done if the report was sent.\
5\. Unsold items returned report sent -> This task is considered done if the report was sent.

**UI**

In consignment table the column _Workflow_ displays a visual indicator showing the status of each task:\


![](<../.gitbook/assets/image (33).png>)

:

\
\
Each square represent the task as numbered in the workflow, _Grey_ task are due, _Green tasks are completed._

![Indicator](<../.gitbook/assets/image (37) (3) (3) (1).png>)

&#x20;**API Info**

See following callback to override defaults.

```
server_consignment_workflow_inventory();
```

 
