# Version 3.1

Released July 2025. This version introduces content types for items, a complete item family tree on consignments, an AI assistant in the help section, connected backoffices, and several website features for WordPress sites.

## Items & Cataloging

### Content type selection with dynamic previews

Items now have a **Content Type**. Choose it from a list that includes stamps, coins, books, postcards, baseball cards, sports memorabilia, watches & jewelry, wine & spirits, fine art, antiques, trading cards and vintage posters.

- The item preview updates instantly according to the selected content type.
- Only the fields relevant to the chosen content type are shown, which removes clutter from the item form.
- The feature is available in the backoffice for all clients. Front-end display of the new fields requires the WordPress site integration.
- Additional fields for a content type can be added as a paid customisation.

### Item tags filter and featured items

- The items table has a new **item tags** filter to find tagged items faster.
- WordPress sites can show a **featured item carousel** driven by this tagging, see [Featured Items](../website/featured-items.md).

## Consignments

### All Items (Family Tree) tab

A new **All Items (Family Tree)** tab on the consignment page shows every item connected to the original consignment, across multiple sales.

- Moved or cloned items keep their relationship to the original consignment.
- Each item's history expands in an accordion, and several histories can be open at the same time.

## Help & Support

### AI assistant

The help section now includes an **AI Assistant** that answers level-1 questions about using the backoffice. It is available around the clock and improves over time as the knowledge base grows.

## Clients & Website

### Professional references

A new **Professional References** field in the Circuit User UI syncs with the backoffice client record.

### Email preferences on My Account

Clients can opt in or out of emails directly from the **My Account** page of the website, see [My Account](../website/my-account.md).

### Magazine subscription management (WordPress)

WordPress sites can manage client magazine subscriptions: subscription types, automatic expiration tracking and a streamlined subscription workflow, see [Magazine Subscription](../website/subscription-magazine.md).

## Connected Backoffices (Beta)

Several backoffices belonging to the same group can now be connected.

- Clients are matched by email and their relations are synced between the connected backoffices.
- Items can be cloned from one backoffice to another (beta). Cloning requires a custom field-mapping configuration, provided as a paid setup.

## Shipping

### EasyPost integration discontinued

Because of persistent reliability issues, the EasyPost integration has been removed from the backoffice. A replacement shipping API was evaluated and introduced in [Version 3.3](version-3.3.md).
