# Shipping

Shipping covers everything that happens to a bidder invoice once the lots have to leave the building: choosing a carrier and a price, buying the carrier label, packing the lots into boxes, and following the parcel until it arrives.

## Where to find it

* **On an invoice:** open the invoice and click the **Shipping & Packing** tab. Everything about that invoice's parcels is done here.
* **Across all invoices:** the **Shipments** page in the main menu lists every shipment, with filters, label printing and return labels. See [The Shipments Page](shipments-page.md).
* **Settings:** the shipping provider, insurance, handling markup and sender address are set by an administrator. See [Shipping Settings](shipping-settings.md).

## Key ideas

| Term | Meaning |
| :--- | :--- |
| **Shipment** | One parcel (or a group of boxes sent together) for an invoice. An invoice can have several shipments, and one shipment can hold the lots of several invoices of the same buyer. |
| **Shipping provider** | Where the prices come from. With **ShipStation** the system asks the carriers for live rates and buys real carrier labels. With the **Manual** provider the price comes from your own tariff tables and no label is bought. |
| **Rate** | One carrier service with its price and delivery estimate, for example *UPS Ground*. You pick one rate per shipment. |
| **Label** | The carrier label bought for a shipment. Once a label is bought, the shipment's contents and price are locked until you cancel the label. |
| **Total billed** | What the buyer pays for the shipment: the carrier cost plus insurance, handling markup and carrier charges, rounded. It is added to the invoice as one **Shipping** charge. |
| **Delivery status** | Where the parcel is: *Pending processing*, *To pack*, *Packed*, *Out of the door*, *Received* or *Error*. |

## The usual flow

1. [Create a shipment](create-a-shipment.md): choose the address, get the rates and pick a carrier.
2. Save it, and [buy the label](labels-and-tracking.md) now or later.
3. [Pack the lots](packing.md): mark each lot as packed, or scan them. The shipment turns to *Packed* when the last lot is packed.
4. Hand the parcel to the carrier and [follow the tracking](labels-and-tracking.md#tracking-and-delivery-status) until it is *Received*.

When a buyer has several invoices, or one invoice must go out in several parcels, see [Combined and Split Shipments](combined-and-split-shipments.md).
