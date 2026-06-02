# Place Bid

**Selector:** `.place-bid` (class) &nbsp;•&nbsp; *multiple per page allowed*

## What it does

An inline bidding widget for pre‑auction mail and agent bids. It can be dropped next to any item — for example one widget per row in a custom item list — because it is matched by **class**, not ID, so a page can contain many independent instances.

The widget shows the current/starting bid with smart increment controls, validates against minimums and the user's available credit, and updates live via WebSocket as bids come in. It adapts to the item's state (not started, in progress, ended, sold, passed) and lets the bidder place, update or delete their mail and agent bids.

**Bidding requires login.** Anonymous visitors see a sign‑in prompt; accounts pending approval and accounts without enough credit are shown the relevant message.

## How to add it

```html
<div class="place-bid circuit-user-ui"
     data-sale-uuid="live-68f657cdd8e3a5-18178142"
     data-item-uuid="live-68f793c6759514-56806752"></div>
```

## Options

| Attribute | Required | Default | Values | Effect |
|-----------|----------|---------|--------|--------|
| `data-sale-uuid` | **Yes** | — | sale UUID | The sale the item belongs to. |
| `data-item-uuid` | **Yes** | — | item UUID | The item being bid on. |
| `hide-sold-unsold` | No | `false` | `true` | Hide the widget entirely when the item is already sold or unsold (show only for biddable items). |
| `data-debug` | No | `false` | `true` | Enable developer console logging. |

## Examples

```html
<!-- One widget per item in a custom list -->
<div class="item-card">
  <h3>Lot 101 — Vintage Watch</h3>
  <div class="place-bid circuit-user-ui"
       data-sale-uuid="live-68f657cdd8e3a5-18178142"
       data-item-uuid="live-68f793c6759514-56806752"></div>
</div>

<div class="item-card">
  <h3>Lot 102 — Antique Clock</h3>
  <div class="place-bid circuit-user-ui"
       data-sale-uuid="live-68f657cdd8e3a5-18178142"
       data-item-uuid="live-68f793c6759514-56806753"></div>
</div>

<!-- Only render while the lot is still biddable -->
<div class="place-bid circuit-user-ui"
     data-sale-uuid="live-68f657cdd8e3a5-18178142"
     data-item-uuid="live-68f793c6759514-56806752"
     hide-sold-unsold="true"></div>
```
</content>
