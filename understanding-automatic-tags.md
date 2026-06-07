# Understanding Automatic Tags & Terms
*Circuit Auction — Backoffice Staff Guide*

## What this guide is

As you work in the backoffice, you'll notice tags and labels appearing on clients, items, orders and invoices that nobody typed in by hand. The system adds these automatically when certain things happen — a client edits their own details, an item's sold status doesn't match, a balance goes negative, and so on.

This guide explains, for each tag you're likely to see: **what it means**, **why it appeared**, and **what it affects**. You can also filter most entity tables (the client list, item list, etc.) by these tags to find every record that carries one.

**How tags are created.** Behind the scenes, tags are organised into groups (for example "client tags", "item tags", "task types"). The system reuses an existing tag if one already exists, and only creates a new one the first time it's needed. That's why a brand-new tag can appear in a filter list the first time a situation occurs — it isn't a mistake.

---

## Tags on Clients
*Seen on the client page; filterable in the client list.*

### Open Balance
- **Means:** The client currently owes money (their balance is negative).
- **Why here:** Added automatically whenever the client's balance is recalculated (during order/consignment processing) and comes out negative. It also **removes itself automatically** once the balance is back to zero or positive and the record is processed again.
- **Affects:** A **flag for your awareness only** — it helps you spot and filter clients who owe money. It does **not** block bidding, checkout, or anything else on its own. Use it as a prompt to follow up, not as a guarantee that the system has stopped anything.

### Duplicate Email
- **Means:** This client shares a main email address with another existing client.
- **Why here:** Appears on clients brought in through **import or external sync** (not normal screen edits). When you try to save a duplicate email **from the screen yourself**, the system instead blocks the save and shows you the conflicting account — so you generally won't create this tag by hand.
- **Affects:** A review flag so you can find and merge or correct duplicate accounts.
- **⚠️ Important:** This tag does **not** clear itself. Even after you've resolved the duplicate, the tag stays until someone removes it manually. Don't assume a client still has a conflict just because the tag is there — check, fix, then clear the tag.

### Warning
- **Means:** This client has a warning note recorded against them.
- **Why here:** The tag simply mirrors the client's **Warning field**. If that field has text in it, the tag is added on the next save; if the field is emptied, the tag is removed on the next save.
- **Affects:** Lets you flag and filter clients who need extra care. To change it, edit the Warning field on the client — don't try to add or remove the tag directly, as it will just re-sync to the field.

### No Address
- **Means:** The client has no usable address on file.
- **Why here:** Managed automatically on every client save: removed once the client has a default address (or one can be assigned automatically), added when they have none.
- **Affects:** Helps you find records that can't be shipped to or invoiced properly. Resolves itself once a valid address is added.

### Sync Error
- **Means:** An attempt to sync this client to an external system failed.
- **Why here:** Added when the external client sync runs and errors out for this record.
- **Affects:** Marks records that didn't make it to the connected system, so they can be retried or investigated.

### VIP
- **Means:** A client marked as VIP.
- **Affects:** Influences how related tasks are handled, and lets you filter your VIPs.

### Active / Passive
- **Means:** The client's activity status. (You may also see the German equivalents **Aktiv / Passiv**, and English **Active / Passive**, depending on where they were set up.)
- **Affects:** Used to separate engaged clients from dormant ones for filtering and catalogue logic.

### Expert
- **Means:** A client identified as an expert. A standard tag set up with the system.

---

## Tags on Items
*Seen on the item page; filterable in the item list.*

### Sold Status Sync Error
- **Means:** The item's sold status in the backoffice doesn't match the bidding server (for example, the backoffice shows sold but the bidding side shows unsold).
- **Why here:** Added automatically during a status check when the two systems disagree.
- **Affects:** Flags items whose sold status needs to be reconciled before invoicing or payout.

> **⚠️ About the "Sold Status Sync Fixed" tag — please read.**
> You may occasionally see a tag called **Sold Status Sync Fixed**. Do **not** treat it as a reliable "this was resolved" signal. In practice, when a real sync error is actually corrected, the system removes the **Error** tag and the item is usually left with **no tag at all** — not a "Fixed" tag. Because of this, the safest reading is: an item with **Sold Status Sync Error** still needs attention; an item with **neither** tag is fine. Don't rely on "Fixed" to confirm a resolution. If this tag is causing confusion in the item list, flag it to the dev team.

### Featured item
- **Means:** An item marked to be featured/highlighted.
- **Affects:** Used for promotion and for filtering featured lots.

---

## Tags on Orders & Invoices
*Seen on the order/invoice page.*

### Order tags (added during printing & packing)
- **Means:** Orders pick up and drop tags automatically as they move through the print/packing workflow.
- **Affects:** Lets you track where an order is in the packing process and filter the order list accordingly.

**Charge line-items you may notice on invoices.** Some charges are created automatically as named types — most commonly a **credit-card fee**. These appear as charge lines on the order/invoice rather than as tags. They're generated by the system when the relevant fee applies.

---

## The Task Queue
*These aren't tags on a page — each is a **type of task** that lands in the task queue for someone to action.*

### Client edited alert
- **Means:** A client changed their own details from the customer side (self-service) and staff should review.
- **Why here:** Triggered only when the **client themselves** edits a watched field — name, salutation, email, mobile, phone, company, website, birthdate, language, shipping instructions, or key address fields. Staff edits do not trigger it.
- **Affects:** Creates a task (assigned to the default secretary, due the next day) containing a before/after table of exactly what changed. It is attached to the client. **It lives in the task queue — it is not a banner on the client page.**

### Payment approval required
- **Means:** An order or payment needs manual approval before it can proceed.
- **Affects:** Appears in the queue for a staff member to approve.

### Buy Now Order
- **Means:** A Buy-Now purchase needs processing.

### Mutate Order
- **Means:** An order needs a change/correction.

### Under Extension Request / Under Extension - Not Genuine
- **Means:** Tasks relating to bidding-time extensions — one for a genuine request, one flagged as not genuine.

### Received export confirmation
- **Means:** Confirmation came back that an export to an external system (e.g. accounting/Dynamics) succeeded.

### Publish an event
- **Means:** A public task to publish an event.
- **Note:** The name is misspelled in the system ("Pushlish/Puplish"). That's intentional for now so the system keeps matching it — don't try to "fix" it from the UI.

---

## Activity Log Entries
*These appear in a client's or consignment's activity history — they record that something happened.*

- **Condition Report** — a condition report was produced.
- **Contract sent** / **Contract Signed** — consignment contract was sent / signed.
- **Statement of account** — a statement was issued.
- **Catalog sent** — a catalogue was sent to the client.
- **Letter to client** — a letter was logged.
- **Google Drive Document** — a Drive document was linked.
- **Subscription ended** — a client's subscription ended.
- **Unsold Returned** — unsold items were returned to the consignor.

---

## Behind-the-Scenes Terms (you can usually ignore these)

Some terms exist mainly for the system's own bookkeeping and rarely need staff attention. A few you might occasionally spot:

- **External system identifiers** (e.g. **Authorize.net**, **PayPal**, **Reserved Bidder number**) — used to link a record to the outside system that owns its reference number.
- **Self** — used when syncing items between connected backoffices; it just means "this backoffice."
- **Catalogue parts** — sub-sections of a sale's catalogue. The same part name can exist separately for each sale, so seeing the "same" name more than once across different sales is normal.
- **Relationship records** (e.g. **Merge**, **Source order**) — note that two clients were merged, or link a credit note back to its original order.
- Various setup, import and category terms (package types, payment types, name prefixes, print options, etc.) are created during data imports and initial setup. They appear in filter lists but aren't action items.

---

## If something doesn't look right

These tags are generated by automatic rules. If a tag appears when you don't expect it, lingers after you've resolved the underlying issue (remember: **Duplicate Email** and the sync tags don't always clear themselves), or seems to contradict what you see on the record, raise it with the dev team rather than assuming the data is wrong — the tag and the underlying field can sometimes be out of step.
