# How consignment statement are created?

Consignment statement are created automatically during a live auction and contains list of all the items belong to the consignor on that sale. for every item you can find its details like the starting price, if it sold or not, the sold price and the additional charges.

Consignment statement has 5 different statuses:

**New** - consignment statement has been created.

**In process** - staff working on the consignment statement.

**Finished** - the consignment statement is not accepting anymore changes. When using print for accounting button, the statement will move automatically to this status.

**Locked** - same as finished, but also means that the statement was export to MS dynamics accounting system.

**Canceled** - staff canceled the consignment statement.

**Second consignment -** As long as the a consignment statement is open \(i.e **New** or **In process**\), every change made on an item, or on the additional charges, will be updated on this consignment statement. As soon as the consignment statement is close \(i.e **Finished** or **Locked**\), change made on an item will create 2nd consignment statement.

**What will trigger a new consignment?**

1. An unsold item has been sold.
2. A credit note was issued.
3. A new additional charge was added to the consignment. 
4. An item that marked as don't pay consignor, was uncheck.

