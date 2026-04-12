# Item All Bids Popup

This popup shows all bids for a selected item, along with other bid-relevant information. Open it by clicking the **plus sign** on any row in the [Bids Item Table](bids-item-table.md).

## Page Header

- Item number
- Next/Previous buttons (to navigate between items)
- Item prices (start, opening, current, minimum)
- Item status

## Top Blocks

1. **Enter bids form** — Lot number is pre-filled for the current item.
2. **Change opening price and reknock down:**
   - Adjust the opening price as you would in a live auction.
   - The current price is calculated based on this opening price.
   - The opening price can be set higher or lower than the starting price to achieve the desired final sale price.
   - Use the **Reknock** button to recalculate the current price and update all related invoices.
3. **Links** — Link to the consignor page and invoice.

## Bids Table

### Bid Information

| Column | Description |
|---|---|
| Status | Current state of the bid |
| Type | Category or classification of the bid |
| Amount | Monetary value of the bid |
| Created | Timestamp of bid creation |
| Bidder | Name of the bidder (linked to client profile) |
| Bidder Number | Unique identifier associated with the bid |
| Authored by | Entity who entered the bid (client, staff, or affiliate) |
| Group Name | Category for grouping related bids |
| Approval Date | When the bid was validated by staff |
| Approval Author | Staff member who validated the bid |
| Note | Additional comments or information about the bid |

{% hint style="info" %}
**Group bids** are automatically managed during auctions. Only one item per group can be won by a client — winning any item in a group cancels the remaining group bids.
{% endhint %}

### Actions and Controls

1. **Under Extension** — Checkbox to indicate the bid was placed during an extension period. Visual indicator changes from gray to red when checked. Auto-submitted.
2. **Approve/Unapprove Bid** — Checkbox to mark bid approval status. Visual indicator changes from yellow to green when approved. Auto-submitted.
3. **Save** — Stores the group name and notes. Also updates the bidder number and amount if the bid was edited.
4. **Delete/Undelete Bid** — Red trash icon to delete a bid; blue undo button to restore a deleted bid.
5. **Edit** — Allows staff to modify existing bids (amount and bidder number). Requires clicking **Save** to confirm changes.

![Item all bids popup table](https://circuitdemo.s3.eu-central-1.amazonaws.com/help-text-images/popup-table.png)
