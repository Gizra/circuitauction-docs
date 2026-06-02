# Favorite Button

**Selector:** `.favorite-btn` (class) &nbsp;•&nbsp; *multiple per page allowed*

## What it does

A small heart button that lets a logged‑in bidder add or remove an item from their favorites. Like Place Bid, it is matched by **class**, so you can put one next to every item in a custom list or grid. Favorited items appear in the bidder's [My Favorites](website/my-favorites.md) block.

If a visitor who is not logged in clicks it, they are prompted to sign in.

## How to add it

```html
<div class="favorite-btn circuit-user-ui" data-item-id="123456"></div>
```

## Options

| Attribute | Required | Default | Values | Effect |
|-----------|----------|---------|--------|--------|
| `data-item-id` | **Yes** | — | item NID/UUID | The item to favorite. |
| `data-display-mode` | No | `grid` | `grid`, `full` | Visual style of the button. `grid` suits compact tiles; `full` is the larger, labelled variant. |

## Example

```html
<div class="item-card">
  <img src="lot-101.jpg" alt="Lot 101">
  <div class="favorite-btn circuit-user-ui"
       data-item-id="1902261"
       data-display-mode="grid"></div>
</div>
```
</content>
