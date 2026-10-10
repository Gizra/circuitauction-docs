<!-- i18n source=website/wordpress-plugin.md sha=ec7c1e0a2394 -->
# WordPress-Plugin

**Plugin:** CircuitAuction · v2.0.25 · GPL-2.0 · [github.com/Gizra/circuit-wordpress](https://github.com/Gizra/circuit-wordpress)
**Voraussetzungen:** PHP 8.0+ · WordPress 6.4+

## Funktion

Verbindet WordPress mit dem CircuitAuction-Backoffice. Das Plugin lädt die React-App vom CDN, legt die Standardseiten für Bieter mit den passenden Block-Divs automatisch an (Login, My Account, Auktionsarchiv, Zuschlagspreise, …), registriert Gutenberg-Blöcke für Katalog- und Auktions-Widgets und leitet dynamische URLs wie `/sale/...`, `/item/...`, `/prices-realized/...` auf ein React-Template um — ohne WordPress-Seitenobjekt.

Wenn Sie WordPress verwenden, ist dieses Plugin der einfachste Weg, die in den übrigen Seiten dieses Abschnitts dokumentierten einbettbaren Blöcke einzurichten.

## Installation

- Laden Sie es über den Plugin-Update-Kanal (CDN) herunter oder klonen Sie das Repository nach `wp-content/plugins/circuitauction/`.
- Aktivieren Sie es unter **Plugins**. Bei der Aktivierung leert das Plugin die Rewrite-Regeln und legt die Standardseiten an (siehe unten).
- Automatische Updates laufen über `https://cdn.circuitauction.com/latest/wordpress/plugins/plugin.json`.

## Konfiguration — Settings → CircuitAuction

| Option | Label | Beschreibung |
|---|---|---|
| `ca_bo_base_url` | Hostname | Basis-URL der Backoffice-API (z. B. `https://backoffice.example.com`). Für mehrsprachige Polylang-Setups kann sie ohne Schema angegeben werden. |
| `ca_site_short_name` | Site short name | Installationskennung auf dem Bid-Server (z. B. `backoffice-hk-eu`). |
| `ca_circuit_debug` | Debug mode | Fügt Debug-Ausgaben und Konsolenprotokolle hinzu. |
| `ca_local_serverless` | Local serverless | Verwendet einen lokalen Serverless-Endpunkt der Entwicklung statt des Produktivsystems. |
| `ca_log_api_requests` | Log API requests | Protokolliert Auktionssuchanfragen im PHP-Fehlerlog. |
| `ca_add_user_block_to_header` | Add user block to header | Fügt das Div des Benutzermenüs automatisch ein, wenn das Theme es nicht enthält. |
| `ca_add_circuit_settings_div` | Add circuit settings div | Fügt das Setup-Tag `<meta id="circuit-setup">` ein — siehe die [Übersicht](README.md). |
| `ca_use_latest_cdn` | Use latest CDN | Lädt den instabilen CDN-Build statt des stabilen. |

## Automatisch angelegte Seiten

Bei Aktivierung/Upgrade legt das Plugin die folgenden Seiten an (nur wenn sie noch nicht existieren), jeweils mit dem passenden eingebetteten Block-Div. Das Verhalten der einzelnen Blöcke ist auf den verlinkten Seiten dokumentiert.

| Seite | Slug | Eingebetteter Selektor | Doku |
|---|---|---|---|
| Login | `login` | `#login` | [Anmeldung](login.md) |
| Register | `register` | `#register` | [Registrierung](register.md) |
| Forgot password | `forgot-password` | `#forgotpassword` | [Passwort vergessen](forgot-password.md) |
| My account | `my-account` | `#my-account` | [Mein Konto](my-account.md) |
| My bids | `my-bids` | `#my-bids` | [Meine Gebote](my-bids.md) |
| My favorites | `my-favorites` | `#my-favorites` | [Meine Favoriten](my-favorites.md) |
| My interests | `my-interests` | `#my-interests` | [Meine Interessen](my-interests.md) |
| Sales archive | `sales-archive` | `#ca-sales-list` | [Auktionsliste](sales-list.md) |
| Prices realized | `prices-realized` | `#ca-prices-realized` | [Erzielte Preise](prices-realized.md) |
| Sale detail | dynamisch | `#ca-sale-page` | [Auktionsseite](sale-page.md) |
| Item detail | dynamisch | `#ca-item-page` | [Losseite](item-page.md) |
| Billing history | `billing-history` | `#billing-history` | [Abrechnung & Zahlungen](billing.md) |
| Subscription magazine | `subscription-magazine` | `#subscription-magazine` | [Magazin-Abonnement](subscription-magazine.md) |

## Dynamisches URL-Routing

| URL-Muster | Template | Hinweise |
|---|---|---|
| `/sale/<id>` oder `/sale/<id>/<slug>/` | `ca-react-page.php` | Stellt das Block-Div der Auktionsseite dar. |
| `/item/<id>` oder `/item/<id>/<slug>/` | `ca-react-page.php` | Stellt das Block-Div der Losseite dar. |
| `/prices-realized/<sale_id>` | `ca-react-page.php` | Stellt das Block-Div der Zuschlagspreise dar. |
| `/live` | `live.php` | Eigenständige Live-Auktion (ohne Theme). |
| `/testlive` | `testlive.php` | Test-Build der Live-Auktion. |

Diese Routen benötigen kein WordPress-Seitenobjekt — sie laufen über eine Rewrite-Regel und eine Query-Variable `ca_page`. Polylang-Sprachpräfixe (z. B. `/de/sale/123`) werden berücksichtigt.

## Gutenberg-Blöcke

Das Plugin registriert sechs Blöcke in der Blockkategorie **Circuit Auction**. Jeder Block gibt das passende Mount-Div mit `class="circuit-user-ui"` aus, wobei die Attribute als `data-*`-Eigenschaften durchgereicht werden.

| Block | Name im Editor | Attribute | Zugehörige Doku |
|---|---|---|---|
| User block | `circuit-auction/user-block` | — | [Benutzermenü](user-block.md) |
| Featured items | `circuit-auction/featured-items` | `sale_nid`, `display_mode` | [Hervorgehobene Lose](featured-items.md) |
| Sale catalog parts | `circuit-auction/sale-catalog-part` | `sale_id`, `catalog_part` | — |
| Sale sessions | `circuit-auction/sale-sessions` | `sale_nid` | [Auktionsinfo](sale-info.md) |
| Sales archive | `circuit-auction/sales-archive` | `first_year`, `display_mode`, `remove_filters`, `search`, `year`, `department`, `status`, `show_featured_items`, `item_display` | [Auktionsliste](sales-list.md) |
| Prices realized | `circuit-auction/prices-realized` | `sale_nid`, `items_per_page`, `columns`, `show_filters`, `show_lot_filter`, `show_status_filter`, `show_items_per_page`, `show_pagination`, `title` | [Erzielte Preise](prices-realized.md) |

## SEO & Meta-Tags

Für dynamische Auktions- und Losseiten ruft das Plugin Titel und Beschreibung von der Backoffice-API ab und überschreibt damit die Meta-Tags von WordPress / AIOSEO.

- Ein erfolgreicher Abruf wird 12 Stunden in einem Transient zwischengespeichert.
- Ein fehlgeschlagener Abruf wird 5 Minuten zwischengespeichert, um das Backoffice nicht zu überlasten.

## Mehrsprachigkeit (Polylang)

Wenn Polylang aktiv ist:

- Der Hostname kann ohne Schema angegeben werden, sodass die URL mit Sprachpräfix je Sprache aufgebaut wird.
- URLs mit Sprachpräfix wie `/de/sale/123` funktionieren ohne weitere Konfiguration.
- Die CDN-App wird mit der aktiven Sprache initialisiert, sodass die Block-Divs übersetzte Inhalte darstellen.

## Fehlerüberwachung

Das Plugin ist in GlitchTip / Sentry integriert. Der DSN wird aus der Option `ca_glitchtip_dsn` gelesen und verweist standardmäßig auf die GlitchTip-Instanz von circuit.auction. Schlägt das Laden des CDN-App-Loaders fehl, wird clientseitig ein Hinweisbanner angezeigt.

## Abhängigkeiten

- PHP 8.0+
- WordPress 6.4+
- Composer: `yahnis-elsts/plugin-update-checker` (^5.3), `kint-php/kint` (^5.0)
- Optional: AIOSEO (umfangreichere Meta-Überschreibungen), Polylang (mehrsprachige URLs)

## Siehe auch

- [Übersicht](README.md) — das Einbettungsmodell mit Block-Divs (was das Plugin im Hintergrund einrichtet).
- Die einzelnen Blockseiten, die in den Tabellen oben verlinkt sind.
