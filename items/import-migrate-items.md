---
description: Google sheet migration of items.
---

# Import / Migrate Items

**Example Sheet:** [https://docs.google.com/spreadsheets/d/13OhdvytrpmdOLLAUoC2mRi7jTs6lzKCccyNDqus8lgo/edit#gid=219859970](https://docs.google.com/spreadsheets/d/13OhdvytrpmdOLLAUoC2mRi7jTs6lzKCccyNDqus8lgo/edit#gid=219859970)

## Required Fields

* **`_unique_id`** - Unique identifier for each row (required for tracking)

## Consignment & Sale Fields

* **`_consignment`** - Supports multiple formats:
  * `<seller email>|<consignment ID>|<consignment name>`
  * `<customer ID>` (numeric)
  * `nid:<node_id>` (consignor node ID)
  * `<email address>` (consignor email)

{% hint style="info" %}
If no consignment is found, a new consignment will be created automatically. The system will:
1. Search for consignor by customer ID, email, or NID
2. Auto-create consignor if not found (requires consignor_email and consignor_last_name or consignor_full_name)
3. Create consignment linked to the sale and consignor
{% endhint %}

* **`_sale`** - Sale node ID (required)
* **`_sale_number`** - Alternative: Sale number if `_sale` is not provided

## Lot Information

* **`_lot_number`** - Lot number
* **`_lot_letter`** - Lot letter
* **`_temp_lot_number`** - Temporary lot number
* **`_internal_id`** - Internal item ID
* **`_position_of_consignment`** - Position within the consignment

## Content Fields (Multi-language Support)

Replace `{language}` with language code (e.g., `en`, `he`):

* **`_title_{language}`** - Item title
* **`_item_subtitle_{language}`** - Item subtitle
* **`_body_{language}`** - Item description (HTML supported, will be cleaned)
* **`_footer_{language}`** - Footer text (HTML supported, will be cleaned)
* **`_provenance_{language}`** - Provenance information (HTML supported, will be cleaned)

Example: `_title_en`, `_title_he`, `_body_en`, `_body_he`

## Pricing Fields

* **`_opening_price`** - Opening bid price
* **`_minimum_price`** - Reserve/minimum price
* **`_estimation_low`** / **`_estimate_low`** - Low estimate
* **`_estimation_high`** / **`_estimate_high`** - High estimate
* **`_buy_now_price`** - Buy now price
* **`_buy_now_setting`** - Buy now setting

{% hint style="info" %}
Currency symbols will be automatically removed and numbers converted to proper float format.
{% endhint %}

## Category Fields

* **`_main_category`** - Main category name (pipe-separated for multiple)
* **`_main_category_{language}`** - Main category in second language
* **`_sub_category`** - Sub category (child of main category)
* **`_sub_category_{language}`** - Sub category in second language
* **`_extra_category`** - Extra category (child of sub category)
* **`_extra_category_{language}`** - Extra category in second language
* **`_main_category_id`** - Philaworksplace category ID

{% hint style="info" %}
Categories support hierarchical structure: Main > Sub > Extra. Terms are auto-created if they don't exist.
{% endhint %}

## Catalog Fields

Supports up to 2 catalogs per item:

**First Catalog:**
* **`_catalog_name`** - Catalog name (e.g., "Scott", "Stanley Gibbons")
* **`_catalog_number`** - Catalog number
* **`_catalog_number_value`** - Catalog value/price

**Second Catalog:**
* **`_catalog_name_2`** - Second catalog name
* **`_catalog_number_2`** - Second catalog number
* **`_catalog_number_value_2`** - Second catalog value/price

**Catalog Part:**
* **`_catalog_part`** - Catalog part/section

## Philatelic Symbols

* **`_symbols`** - Philatelic symbols (pipe-separated)
  * Supports special notation:
    * `**` → Mint
    * `*` → Unused
    * `o` or `O` → Used
    * `(*)` → Without gum
  * Or use text names directly (e.g., "Mint|Used")
* **`_sub_symbol`** - Sub symbol

## Physical Properties

* **`_year`** - Year
* **`_country`** - Country
* **`_mediums`** - Mediums (pipe-separated for multiple values)
* **`_grade`** - Grade/condition
* **`_thematics`** - Thematic categories

## Dimensions

**Individual Dimensions:**
* **`_height`** - Height
* **`_width`** - Width
* **`_depth`** - Depth
* **`_size_description`** - Description of dimensions

**Combined Dimensions:**
* **`_size`** - Format: "H x W x D unit" (e.g., "35.75 x 26.75 x 1.25 in")
* **`_framed`** - Framed dimensions (same format as `_size`)
* **`_quantity`** - Number of items (creates multiple dimension records)

{% hint style="info" %}
Units default to inches (in). System automatically creates dimension nodes and parses combined dimension formats.
{% endhint %}

## Links & Certificates

**Certificate:**
* **`_certificate_link`** - Certificate URL
* **`_certificate_link_title`** - Certificate link title

**References:**
* **`_reference_link1`** - First reference URL
* **`_reference_link_title1`** - First reference link title
* **`_reference_link2`** - Second reference URL
* **`_reference_link_title2`** - Second reference link title

## Item Settings

* **`_item_type`** - Item type (defaults to "single")
* **`_field_item_status`** - Item status (defaults to "ready")
* **`_collectible_type`** - Collectible type:
  * `Artwork` → converted to `fine_art`
  * `Book` → converted to `books`
  * Or use direct values: `stamps`, `coins`, etc.
* **`_language`** - Language code (defaults to site default)

## Additional Information

* **`_auctioneer_notes`** - Internal auctioneer notes
* **`_search_tag`** - Search tags for better discoverability
* **`_public_message`** - Public message visible to bidders
* **`_post_sale_purchase`** - Post-sale purchase flag
* **`_responsible_user`** - Responsible user (username or full name)

## Commission

* **`_consignor_commission`** - Consignor commission percentage
* **`_commission`** - Commission for the consignment (converted from decimal to percentage if < 1)

## Consignor Auto-Creation Fields

When consignor doesn't exist, these fields enable auto-creation:

* **`consignor_email`** - Consignor email address
* **`consignor_first_name`** - First name
* **`consignor_last_name`** - Last name
* **`consignor_full_name`** - Full name (will be split into first/last)

{% hint style="warning" %}
In non-live environments, ".test" is appended to emails to prevent sending to real clients.
{% endhint %}

## Sold Items (Creates Winning Bid)

* **`_sold_for`** - Sold price (triggers automatic winning bid creation)
* **`_winning_user`** - Winning user ID (if migrate mapping enabled)
* **`_winning_user_nid`** - Winning user node ID

## Processing Logic

1. **Consignment Resolution:**
   * Searches by customer ID → NID → email → consignment ID → consignment name
   * Auto-creates consignor if email and name provided
   * Auto-creates consignment if consignor found but no matching consignment

2. **Price Conversion:**
   * Removes currency symbols automatically
   * Converts to proper float format

3. **Category Hierarchy:**
   * Creates multi-level taxonomy: Main → Sub → Extra
   * Supports multi-language term names
   * Auto-creates missing terms

4. **Dimension Nodes:**
   * Creates separate dimension node entities
   * Supports multiple instances based on `_quantity`
   * Parses combined dimension strings automatically

5. **HTML Cleaning:**
   * Body, provenance, and footer fields are cleaned of unsafe HTML

6. **Symbol Mapping:**
   * Converts philatelic shorthand to full term names
   * Creates terms if they don't exist in symbols vocabulary



