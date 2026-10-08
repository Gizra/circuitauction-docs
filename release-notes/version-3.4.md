# Version 3.4

Released March 2026. The live bidding engine was rebuilt for speed, and the backoffice gained a Quick Add Item form, PDF and video assets, collectible types, Buy It Now, reserve bids, a viewing module, balance history, Authorize.net payments and more.

## Live Bidding Engine

### Live bidding is up to five times faster

The live bidding technology was rebuilt on Redis and Go, replacing the previous Node.js stack. Bid processing now takes double-digit milliseconds, with response times under 100 ms on web, mobile and podium apps. Every live feature benefits from the change.

## Items & Cataloging

### Quick Add Item

A streamlined form for rapid item entry, available from the main menu and directly from a consignment.

- Only the fields you need are shown. The field list is configurable in the settings.
- The form resets after each save so you can keep entering items.
- Each consignment has a **QR code**. Scan it with a phone or tablet to add items while walking the room. On mobile you can take photos with the camera or pick them from the gallery.

### PDF and video assets

Attach MP4 videos and PDF files to items. They are shown in the item gallery on the website, which is useful for condition reports, certificates and walkthroughs.

### Collectible type

Type-specific data fields: coins get grading fields, art gets medium and dimensions, and so on.

### Drag & drop multi-image upload

Upload several images at once by dragging them onto the item, see [How to Mass Upload Items Images](../sale/how-to-mass-upload-items-images.md).

### Clear formatting

Strip unwanted formatting from pasted text with one click in text areas.

### Finders fee by item

Finders fees can now be set per item, see [Consignment Finder Fees](../data-migration/consignment-finder-fees.md) for the import format.

## Bidding & Sales

### Buy It Now

Set a fixed purchase price so clients can buy an item immediately without waiting for the auction.

### Reserve bids

Full reserve bid support. Auctioneers can remove a reserve from the podium during a live auction.

### Sale access type

Control who can bid in each sale. Set default bid steps and restrict access by client tags, for example a VIP-only sale.

### Close all items

Re-knock down all items of a pre-sale auction in one action from the sale page. Useful when finalising mail bid sales.

### Auction Mobility integration

Export the catalog to, and import bids from, Auction Mobility, alongside the existing StampCircuit, SAN, PhilaSearch and Delcampe integrations, see [Auction Mobility Bids](../data-migration/bids-mobility.md).

## Clients & Financial Management

### Viewing module

Track pre-auction viewings: who viewed which items, and when items were taken out and returned. For mail viewings, generate a viewing invoice listing the shipped items and costs.

### Balance history

A complete ledger of each client's financial activity: invoices, payments, credits and adjustments, instead of a single balance snapshot.

### Bidder alias

Assign a display alias to a client for use during live auctions.

### Invoice address selection

When editing an invoice, choose one of the client's stored addresses instead of typing a custom one.

### Opt-in for printed materials

Clients can opt in or out of printed catalogs and mailings from their account page on the website.

## Shipping & Packing

### Shipment box tracking

Mark which box each package goes into. Use the QR scanner to scan items as you pack them, with no typing needed.

## Payments & Subscriptions

### Authorize.net integration

Clients can pay invoices by credit card through Authorize.net, see [Billing & Payments](../website/billing.md).

### Magazine subscriptions

Sell magazine subscriptions directly through Circuit Auction. Clients subscribe and pay on your website, see [Purchase Subscription](../website/subscription-purchase.md).

## System & Interface

### React app overhaul

The React front end is faster and no longer depends on the WordPress sync, which makes it easier to connect any website, see [Website (Embeddable Blocks)](../website/README.md).

### Sale page redesign

A cleaner layout with a structured workflow and fewer buttons, see [How to Create a Sale](../sale/how-to-create-a-sale.md).

### Activity pages split

Activities are now two pages: one for event logging with better filtering, and one for emails and documents.

### Flood notifications

Staff receive an email alert when a login flood is detected, and can reset the block for verified users.

### Task notifications

Email notifications are sent when tasks are created in the backoffice, see [Tasks](../tasks.md).

## Premium Services

Two paid services were introduced with this release. Contact Circuit Auction for details and a quote.

- **Elite website package with WebDrop**: a website built on Astro and hosted on Cloudflare Workers, with search engine and AI search optimisation, built and managed by WebDrop and coordinated by Circuit Auction.
- **Custom vector database for catalog AI**: connect your own reference databases (stamp catalogs, coin references, art provenance) to the AI cataloging feature so descriptions are based on your authoritative sources. The database can be built from existing data files or PDFs.
