# WordPress Plugin

**Plugin:** CircuitAuction · v2.0.25 · GPL-2.0 · [github.com/Gizra/circuit-wordpress](https://github.com/Gizra/circuit-wordpress)
**Requires:** PHP 8.0+ · WordPress 6.4+

## What it does

Bridges WordPress with the CircuitAuction back-office. The plugin loads the CDN React app, auto-creates the standard bidder pages with the right block divs (login, my-account, sales archive, prices realized, …), registers Gutenberg blocks for catalog and sales widgets, and routes dynamic `/sale/...`, `/item/...`, `/prices-realized/...` URLs to a React template — no WordPress page object required.

If you are running on WordPress this plugin is the easiest way to wire the embeddable blocks documented in the rest of this section.

## Installation

- Download from the plugin update channel (CDN) or clone the repo into `wp-content/plugins/circuitauction/`.
- Activate from **Plugins**. On activation the plugin flushes rewrite rules and creates the standard pages (see below).
- Auto-update is driven by `https://cdn.circuitauction.com/latest/wordpress/plugins/plugin.json`.

## Configuration — Settings → CircuitAuction

| Option | Label | Description |
|---|---|---|
| `ca_bo_base_url` | Hostname | Back-office API base URL (e.g. `https://backoffice.example.com`). Can be bare (no scheme) for Polylang multi-language setups. |
| `ca_site_short_name` | Site short name | Install identifier on the bid server (e.g. `backoffice-hk-eu`). |
| `ca_circuit_debug` | Debug mode | Adds debug output and console logs. |
| `ca_local_serverless` | Local serverless | Use a dev local serverless endpoint instead of prod. |
| `ca_log_api_requests` | Log API requests | Logs sale-search requests to the PHP error log. |
| `ca_add_user_block_to_header` | Add user block to header | Auto-inject the user-menu div when the theme does not include it. |
| `ca_add_circuit_settings_div` | Add circuit settings div | Inject the `<meta id="circuit-setup">` setup tag — see the [Overview](README.md). |
| `ca_use_latest_cdn` | Use latest CDN | Load the unstable CDN build instead of the stable one. |

## Auto-created pages

On activation/upgrade the plugin creates the following pages (only if they don't already exist), each with the right block div embedded. The block-level behaviour is documented in the linked pages.

| Page | Slug | Embedded selector | Doc |
|---|---|---|---|
| Login | `login` | `#login` | [Login](login.md) |
| Register | `register` | `#register` | [Register](register.md) |
| Forgot password | `forgot-password` | `#forgotpassword` | [Forgot Password](forgot-password.md) |
| My account | `my-account` | `#my-account` | [My Account](my-account.md) |
| My bids | `my-bids` | `#my-bids` | [My Bids](my-bids.md) |
| My favorites | `my-favorites` | `#my-favorites` | [My Favorites](my-favorites.md) |
| My interests | `my-interests` | `#my-interests` | [My Interests](my-interests.md) |
| Sales archive | `sales-archive` | `#ca-sales-list` | [Sales List](sales-list.md) |
| Prices realized | `prices-realized` | `#ca-prices-realized` | [Prices Realized](prices-realized.md) |
| Sale detail | dynamic | `#ca-sale-page` | [Sale Page](sale-page.md) |
| Item detail | dynamic | `#ca-item-page` | [Item Page](item-page.md) |
| Billing history | `billing-history` | `#billing-history` | [Billing & Payments](billing.md) |
| Subscription magazine | `subscription-magazine` | `#subscription-magazine` | [Magazine Subscription](subscription-magazine.md) |

## Dynamic URL routing

| URL pattern | Template | Notes |
|---|---|---|
| `/sale/<id>` or `/sale/<id>/<slug>/` | `ca-react-page.php` | Renders the Sale Page block div. |
| `/item/<id>` or `/item/<id>/<slug>/` | `ca-react-page.php` | Renders the Item Page block div. |
| `/prices-realized/<sale_id>` | `ca-react-page.php` | Renders the Prices Realized block div. |
| `/live` | `live.php` | Standalone live auction (no theme). |
| `/testlive` | `testlive.php` | Test build of the live auction. |

These routes do not need a WordPress page object — they go through a rewrite rule and a `ca_page` query var. Polylang language prefixes (e.g. `/de/sale/123`) are honoured.

## Gutenberg blocks

The plugin registers six blocks under the **Circuit Auction** block category. Each block renders the matching `class="circuit-user-ui"` mount div with attributes passed through as `data-*` properties.

| Block | Editor name | Attributes | Related doc |
|---|---|---|---|
| User block | `circuit-auction/user-block` | — | [User Menu](user-block.md) |
| Featured items | `circuit-auction/featured-items` | `sale_nid`, `display_mode` | [Featured Items](featured-items.md) |
| Sale catalog parts | `circuit-auction/sale-catalog-part` | `sale_id`, `catalog_part` | — |
| Sale sessions | `circuit-auction/sale-sessions` | `sale_nid` | [Sale Info](sale-info.md) |
| Sales archive | `circuit-auction/sales-archive` | `first_year`, `display_mode`, `remove_filters`, `search`, `year`, `department`, `status`, `show_featured_items`, `item_display` | [Sales List](sales-list.md) |
| Prices realized | `circuit-auction/prices-realized` | `sale_nid`, `items_per_page`, `columns`, `show_filters`, `show_lot_filter`, `show_status_filter`, `show_items_per_page`, `show_pagination`, `title` | [Prices Realized](prices-realized.md) |

## SEO & meta tags

For dynamic sale / item pages the plugin fetches the title and description from the back-office API and overrides the WordPress / AIOSEO meta tags.

- Successful fetch is cached in a transient for 12 hours.
- Failed fetch is cached for 5 minutes to avoid hammering the back-office.

## Multilingual (Polylang)

When Polylang is active:

- The hostname can be left bare (no scheme) so the language-prefixed URL is built per language.
- Language-prefixed URLs like `/de/sale/123` work out of the box.
- The CDN app is initialised with the active language so the block divs render translated content.

## Error monitoring

The plugin integrates with GlitchTip / Sentry. The DSN is read from the `ca_glitchtip_dsn` option and defaults to the circuit.auction GlitchTip instance. A client-side banner is shown if the CDN app-loader fails to load.

## Dependencies

- PHP 8.0+
- WordPress 6.4+
- Composer: `yahnis-elsts/plugin-update-checker` (^5.3), `kint-php/kint` (^5.0)
- Optional: AIOSEO (richer meta overrides), Polylang (multilingual URLs)

## See also

- [Overview](README.md) — the block-div embedding model (what the plugin sets up under the hood).
- Individual block pages linked in the tables above.
