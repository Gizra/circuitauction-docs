# How to Create a Consignment

The best practice is to create a consignment from the consignor \(Client\) page.

1. Make sure you are on the right [Sale context](../sale/sale-context.md).
2. Go to the consignor page \(See [How to Find a Client](../client/how-to-find-an-existing-client.md)\).
3. Click on `+create consignment` ![image](https://user-images.githubusercontent.com/20393485/48546000-dd17d100-e8cf-11e8-8744-0220da32e1c7.png)
4. Fill in the relevant fields:

**Seller** - select the client that gave you this consignment. When you create the consignment from the consignor \(Client\) page this will be filled-in automatically.

**Underbid percentage** - if an item wasn't sold during mail or live auction, determine how much discount will be given on a post sale. Check **No post sale purchase** to not allow this item to be sold after the auction.

**Tax type** - select Tax Type to override the client default tax type if needed. If this field is left empty the client's tax type will be used to calculate the tax added to the invoice.

**Payment Instructions** - enter special payment instructions for the consignor \(if any\), this data will appear in the consignor order.

**Finder fees** - if this consignment was referenced to you by another client \(“Finder”\), you can add the finder name here and add the commission, in percentage, they will get from this consignment. You can add more than one finder.

**Commission steps** - If you want to override the default consignor commission \(set by the Admin on the backend\), you can add a consignment-based commission step here.

* **Steps type** - determine if the calculation will be done on a single lot \(item\) basis or on the entire consignment. 
* **Commission** - percentage used to calculate the commission. \(eg. 10% 5%\)
* **From amount** - the step the consignment needs to reach to. \(eg. $1,000, $5,000\)  

Examples:  
_Case 1_ - In this case the commission Step type is set to Single lots. As a result, all lots that sell below $200 will get a 10% commission. All lots that sell for $200 and above will get a 7% commission.  
![image](https://user-images.githubusercontent.com/20393485/50416975-1bd46b80-082c-11e9-83ad-12687cd2681f.png)

_Case 2_ - In this case the commission Step type is set to Entire consignment. If the entire collection of lots sells for less than $200 then it will get a 10% commission. If the entire collection of lots sell for a combined value of $200 or more then it will get a 7% commission.  
![image](https://user-images.githubusercontent.com/20393485/50417048-93a29600-082c-11e9-85b5-c1dfe0ffc7a1.png)

**Additional Charges** - enter additional charges that will be added to the [Consignment Statement](how-consignment-statement-are-created.md).

1. Click **Save.**

You can also create a consignment from the Consignment dashboard. 1. Go to **Consignment** 2. Click on `+create new consignment`

![](../.gitbook/assets/consignments___backoffice.jpg)

1. Fill in the relevant fields. Make sure you select the consignor \(client\) in the seller field.  
2. Click **Save.**

