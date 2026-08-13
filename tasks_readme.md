# Tasks

You can create different types of tasks and assign them to different people in your organization. Tasks can be created for clients, consignments, items, sales, and orders.

1. Go to the entity page (client, consignment, item, sale, or order) you want to create a task for.
2. Click on the **Tasks** tab. The number on the tab represents the number of tasks for this record.

![tasks tab](assets/screenshots/tasks-tab.png)

### Creating a new task
1. Fill in the fields under `Add a task`   
**Type** - select the task type from the list.  
**Assignee** - select the user in the system that is assigned to do the task.  
**Status** - `Can start` or `Can't start` (a task that depends on another task can't start yet).  
**Due date** - enter the date on which the task is expected to be complete.  
2. Click on the `Created` button. 

![add a task](assets/screenshots/tasks-add.png)


### Deleting task
Click on the `Delete` button on the task's row. 

![image](assets/screenshots/tasks-delete.png)


### Marking task as complete
Once a task is done, change its **Status** to `Completed` and click `Save` on the task's row.

![image](assets/screenshots/tasks-complete.png)

### Default / Dependent tasks
In the backend of the system, Admin can define**default tasks** that will be created automatically. For example: every time an item is created, tasks such as “Describe item” and "Photograph" will be created and assigned to the right staff member.
Admin can also define **dependent tasks**. For example: a task to “proofread” an item can only start after the task to “Describe item” is complete.
