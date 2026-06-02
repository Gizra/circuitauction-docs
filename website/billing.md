# Billing & Payments

**Selector:** `#billing-history` (also `#payment-method`) &nbsp;•&nbsp; *one per page* &nbsp;•&nbsp; **login required**

## What it does

The bidder's billing centre, with two tabs:

- **Billing History** — a list of invoices with a status filter (all / pending / overdue / paid), per‑invoice details and PDF links, transaction history, pagination, and a checkout flow to pay selected invoices.
- **Payment Methods** — saved cards (with brand logos), add‑card form (cardholder, number, expiry, CVV, billing address) and edit/delete actions. This tab is hidden when your site uses phone‑only payment.

The page supports deep links: the URL hash `#payment-methods` opens the Payment Methods tab, while `#billing` (or no hash) opens Billing History.

## How to add it

```html
<div id="billing-history" class="circuit-user-ui"></div>
```

Mounting on `#payment-method` instead renders the same billing centre — useful if you want the URL/anchor to read "payment-method".

## Options

None.

## See also

- [Balance Button](website/balance.md) — a compact "amount due" indicator that links here
</content>
