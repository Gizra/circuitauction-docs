# Version 3.5

Upcoming release. Version 3.5 focuses on reporting, communication with clients, and tools that make day-to-day administration easier. Highlights include a new Auction Timeline page, a redesigned client statistics tab, a built-in email template editor, automatic invoice payment reminders, and a dark mode for the whole backoffice.

## Reports & Statistics

### Auction Timeline

A new **Auction Timeline** page (sidebar, under Reports) gives a retrospective view of a completed live session as recorded by the bid server.

- Filter by **session** and by **date range**.
- Key figures at a glance: total lots sold, bids placed, and session duration.
- An interactive **session summary** timeline with auto-play, zoom and a scrubber, showing item events, bids placed and start/end markers. Use the arrow keys or click to step through lots.
- A **bids placed** panel with the peak bidding time and the top performing lots.
- An **Auction Waterfall** listing each lot in order with its phase, dwell time, number of bids, hammer price and winning bidder. Filter the waterfall by Sold, Unsold or Other.

### Client statistics redesign

<video class="release-video" controls preload="metadata" playsinline src="https://circuit-kubernetes.s3.eu-central-1.amazonaws.com/openmontage/tutorials/release-3.5-client-statistics/final.mp4">Your browser does not support the video tag. <a href="https://circuit-kubernetes.s3.eu-central-1.amazonaws.com/openmontage/tutorials/release-3.5-client-statistics/final.mp4">Download the video</a>.</video>

The **Statistics** tab on the client page has been redesigned.

- Summary cards: total won, total bid, win rate and average lot won.
- A **bidding activity** chart that can be switched between won and won + underbid, per year or per sale, by amount or by number of lots.
- A **collecting areas** chart showing the amount won per top-level category. Click a bar to filter the categories below.
- A **top categories** list with the amount and number of lots per category.
- A **Generate Client Data Sheet** button to export the client's statistics.

### Bids reports redesign

<video class="release-video" controls preload="metadata" playsinline src="https://circuit-kubernetes.s3.eu-central-1.amazonaws.com/openmontage/tutorials/release-3.5-bids-reports/final.mp4">Your browser does not support the video tag. <a href="https://circuit-kubernetes.s3.eu-central-1.amazonaws.com/openmontage/tutorials/release-3.5-bids-reports/final.mp4">Download the video</a>.</video>

The **Bids reports** page (sidebar) has been rebuilt as a set of tabs, each with column filters, sorting and CSV export:

- Bids List (with an option to show deleted bids)
- Winning bids list
- Hammer Price list
- Bidder info
- Bidder info grouped
- Flagged items

### New consignment reports

<video class="release-video" controls preload="metadata" playsinline src="https://circuit-kubernetes.s3.eu-central-1.amazonaws.com/openmontage/tutorials/release-3.5-consignment-reports/final.mp4">Your browser does not support the video tag. <a href="https://circuit-kubernetes.s3.eu-central-1.amazonaws.com/openmontage/tutorials/release-3.5-consignment-reports/final.mp4">Download the video</a>.</video>

The consignment page gained new report actions:

- **Generate consignor report** with three options: **Phase** (for example Post-sale), **Detail** (for example lot numbers only) and **Scope**: this consignment only, all the consignor's lots combined, or all the consignor's lots per consignment.
- **Generate unsold items list**, **Generate Master sheet Report** and **Generate Proof reading list**.
- Reports can be generated with or without letterhead, and the accompanying email can be edited before it is sent.

### Export accounting in CSV and XLSX

<video class="release-video" controls preload="metadata" playsinline src="https://circuit-kubernetes.s3.eu-central-1.amazonaws.com/openmontage/tutorials/release-3.5-export-accounting/final.mp4">Your browser does not support the video tag. <a href="https://circuit-kubernetes.s3.eu-central-1.amazonaws.com/openmontage/tutorials/release-3.5-export-accounting/final.mp4">Download the video</a>.</video>

The **Export Accounting** page now has **CSV** and **XLSX** buttons in the Export block. They download the currently filtered list of invoices or consignment statements as a spreadsheet. This download does not mark the items as exported to accounting.

## Invoices & Emails

### Preview email and PDF in orders batch actions

<video class="release-video" controls preload="metadata" playsinline src="https://circuit-kubernetes.s3.eu-central-1.amazonaws.com/openmontage/tutorials/release-3.5-orders-preview-email/final.mp4">Your browser does not support the video tag. <a href="https://circuit-kubernetes.s3.eu-central-1.amazonaws.com/openmontage/tutorials/release-3.5-orders-preview-email/final.mp4">Download the video</a>.</video>

In the **Batch actions** block of the Invoices page, a new **Preview email & PDF** button shows the exact email and the invoice PDF, filled with real data, before you click Apply to send it to the selected orders.

### Sent email list on the invoice page

<video class="release-video" controls preload="metadata" playsinline src="https://circuit-kubernetes.s3.eu-central-1.amazonaws.com/openmontage/tutorials/release-3.5-invoice-email-list/final.mp4">Your browser does not support the video tag. <a href="https://circuit-kubernetes.s3.eu-central-1.amazonaws.com/openmontage/tutorials/release-3.5-invoice-email-list/final.mp4">Download the video</a>.</video>

Each invoice page now ends with an **Emails and Documents** table listing every email and document generated for that invoice: creation or sent date, title, type, recipient, content, attached documents and author (including emails sent automatically by the system).

### Email template editor

<video class="release-video" controls preload="metadata" playsinline src="https://circuit-kubernetes.s3.eu-central-1.amazonaws.com/openmontage/tutorials/release-3.5-email-templates/final.mp4">Your browser does not support the video tag. <a href="https://circuit-kubernetes.s3.eu-central-1.amazonaws.com/openmontage/tutorials/release-3.5-email-templates/final.mp4">Download the video</a>.</video>

A new **Email Templates** page (sidebar) lets you view and edit every global email template used for invoices, shipping, bidder notifications and other processes.

- Templates are grouped by area (Invoices / Orders, Clients / Bidder notifications, ...) and can be edited per language.
- Each template has a subject and a rich-text body. HTML is allowed in the body.
- Click a **token** (for example `@client-name`, `@invoice-id`, `@checkout-url`, `!signature`) to insert it. Tokens are replaced with live values when the email is sent.
- Saving a template updates all future emails that use it.

### Automatic invoice payment reminders

<video class="release-video" controls preload="metadata" playsinline src="https://circuit-kubernetes.s3.eu-central-1.amazonaws.com/openmontage/tutorials/release-3.5-payment-reminders/final.mp4">Your browser does not support the video tag. <a href="https://circuit-kubernetes.s3.eu-central-1.amazonaws.com/openmontage/tutorials/release-3.5-payment-reminders/final.mp4">Download the video</a>.</video>

Unpaid invoices can now be reminded automatically, in three steps: a **payment reminder**, a **past due** notice and a **final reminder**.

- **Site-wide defaults** define the number of days after an invoice is finished and visible to the customer for each step (for example 7, 14 and 21 days).
- On the **Sale page**, under Auction Settings, tick **Automatic payment reminders** to enable them for that sale. You can override the three delays per sale. The Invoices page shows a notice summarising the active schedule.
- Hidden invoices are skipped. Setting an invoice's customer visibility to hidden in batch actions also pauses its reminders.
- The emails use the three templates **Invoice payment reminder**, **Invoice past due** and **Invoice final payment reminder**, which can be customised in the Email Templates page.

### Print address stickers on A4 sheets

<video class="release-video" controls preload="metadata" playsinline src="https://circuit-kubernetes.s3.eu-central-1.amazonaws.com/openmontage/tutorials/release-3.5-address-sticker-sheet/final.mp4">Your browser does not support the video tag. <a href="https://circuit-kubernetes.s3.eu-central-1.amazonaws.com/openmontage/tutorials/release-3.5-address-sticker-sheet/final.mp4">Download the video</a>.</video>

In the **Address sticker** batch action on the Clients page, the **Format** list now offers **Sheet of labels (2 x 5)** in addition to the single label, so the default address of each selected client can be printed on standard A4 label sheets.

## Tasks & Support

### Reply to "Ask about item" tasks

<video class="release-video" controls preload="metadata" playsinline src="https://circuit-kubernetes.s3.eu-central-1.amazonaws.com/openmontage/tutorials/release-3.5-task-reply/final.mp4">Your browser does not support the video tag. <a href="https://circuit-kubernetes.s3.eu-central-1.amazonaws.com/openmontage/tutorials/release-3.5-task-reply/final.mp4">Download the video</a>.</video>

Questions sent by bidders about a lot appear in [Tasks](../tasks.md) as *Ask about item* tasks. A new **Replied** action opens an email composer:

- The bidder's question and the lot are shown at the top.
- The reply is pre-filled from the *Your question about lot* template, with tokens and file attachments available.
- Edits can be saved for this email only or written back to the global template.
- The task is marked as completed after sending, and the reply is logged in the client's emails.

### Integrated support tickets

<video class="release-video" controls preload="metadata" playsinline src="https://circuit-kubernetes.s3.eu-central-1.amazonaws.com/openmontage/tutorials/release-3.5-support-tickets/final.mp4">Your browser does not support the video tag. <a href="https://circuit-kubernetes.s3.eu-central-1.amazonaws.com/openmontage/tutorials/release-3.5-support-tickets/final.mp4">Download the video</a>.</video>

A new **Support Tickets** page (sidebar, and a shortcut icon in the top bar) lists your support requests to the CircuitAuction team with their status: open, in progress, resolved, deployed live and closed. Tickets can be filtered by status and by tag.

## Sales & Bids

### HiBid bids import

<video class="release-video" controls preload="metadata" playsinline src="https://circuit-kubernetes.s3.eu-central-1.amazonaws.com/openmontage/tutorials/release-3.5-hibid-import/final.mp4">Your browser does not support the video tag. <a href="https://circuit-kubernetes.s3.eu-central-1.amazonaws.com/openmontage/tutorials/release-3.5-hibid-import/final.mp4">Download the video</a>.</video>

The **Bids Import** tab of the sale page has a new **HiBid Import** next to the existing [Philasearch](../data-migration/bids-philasearch.md), [Delcampe](../data-migration/bids-delcampe.md), [Auction Mobility](../data-migration/bids-mobility.md), [SAN](../data-migration/bids-san.md) and Invaluable imports.

- Paste the Google Drive sheet URL of the HiBid auction results export, or upload the file directly.
- Expected columns: Lot, Winning Bidder (paddle), Name, Address, State, Zip Code, Email, Phone and the sale price.
- Lots whose reserve was **Not Met** are imported with a note.
- Use **Queue import bids** to start the import and **Queue failed import bids** to retry the rows that failed.

### Reset sale and sync

<video class="release-video" controls preload="metadata" playsinline src="https://circuit-kubernetes.s3.eu-central-1.amazonaws.com/openmontage/tutorials/release-3.5-reset-sale-sync/final.mp4">Your browser does not support the video tag. <a href="https://circuit-kubernetes.s3.eu-central-1.amazonaws.com/openmontage/tutorials/release-3.5-reset-sale-sync/final.mp4">Download the video</a>.</video>

A new **Reset sale and sync** button on the sale page re-queues every lot in the sale for search indexing, re-syncs the lots with the bid server, rebuilds the sale JSON and, once those queues have finished, broadcasts a cache reset to the user-facing website. The progress of each step is shown next to the button. Use it when the website shows stale data for a sale.

## System

### Dark mode

<video class="release-video" controls preload="metadata" playsinline src="https://circuit-kubernetes.s3.eu-central-1.amazonaws.com/openmontage/tutorials/release-3.5-dark-mode/final.mp4">Your browser does not support the video tag. <a href="https://circuit-kubernetes.s3.eu-central-1.amazonaws.com/openmontage/tutorials/release-3.5-dark-mode/final.mp4">Download the video</a>.</video>

A moon icon in the top bar, next to the notifications bell, switches the whole backoffice to a dark theme. The choice is remembered for your user.

### Bid server health monitor

<video class="release-video" controls preload="metadata" playsinline src="https://circuit-kubernetes.s3.eu-central-1.amazonaws.com/openmontage/tutorials/release-3.5-health-monitor/final.mp4">Your browser does not support the video tag. <a href="https://circuit-kubernetes.s3.eu-central-1.amazonaws.com/openmontage/tutorials/release-3.5-health-monitor/final.mp4">Download the video</a>.</video>

A **Health** button in the top bar opens a monitor of the bid server connection and its queues. The queue now restarts itself automatically when it stalls, so live bidding recovers without manual intervention.
