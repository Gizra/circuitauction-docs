# The Shipments Page

The **Shipments** page (main menu) lists the shipments of all invoices, with their carrier, label, tracking and delivery status.

## Filter

Filter the table by **Delivery status**, **Invoice status**, **Type**, order tags, weight range and **Pickup date** (with **Filter Today** and the arrows to move one day back or forward). The **Returns** filter shows only return labels, or excludes them. **Reset** clears the filters.

**Show orphan ShipStation shipments** lists shipments that exist in ShipStation but are not attached to any invoice, for example leftovers from tests.

A shipment past its expected delivery date that has not arrived is marked as overdue.

## Print

* **Print table (filtered)** prints the list as it is filtered.
* Select shipments and use **Bulk actions → Bulk print** to print their labels together.
* Each row links to its invoice and to its label PDF.

## Bulk shipping from the invoices list

On the bidder invoices list you can create shipments and labels for many invoices at once: select the invoices and use **Create/Update shipment + label (selected)**, or **Create/Update shipments + labels for all**. **Cancel shipments (selected)** cancels them, and **Print shipping labels** prints the labels. Large batches run in the background. Invoices with lots under extension are skipped and tagged.

See also [Labels and Tracking](labels-and-tracking.md).
