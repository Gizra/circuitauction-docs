# Balance Button

**Selector:** `#balance-btn` &nbsp;•&nbsp; *one per page*

## What it does

A compact button that shows the signed‑in bidder's account balance or amount due — handy for a site header. It handles several states automatically:

- **Not logged in** — shows a "log in to see balance" prompt.
- **Loading / error** — while fetching, or if the lookup fails.
- **Amount owed** — when the balance is negative, it links through to billing.
- **All clear** — when nothing is owed.

## How to add it

```html
<div id="balance-btn" class="circuit-user-ui"></div>
```

## Options

None.

## See also

- [Billing & Payments](website/billing.md) — where the "amount owed" state links to
</content>
