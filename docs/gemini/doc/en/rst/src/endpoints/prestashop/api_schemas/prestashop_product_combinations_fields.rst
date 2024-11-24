PrestaShop Product Combinations Fields
====================================

This file defines the schema for PrestaShop product combinations fields.  It lists the various fields that are used to define different product combinations.


.. code-block:: json
   :linenos:

   ```json
   {
     "Product ID": "",
     "Attribute (Name:Type:Position)": "",
     "Value (Value:Position)": "",
     "Supplier reference": "",
     "reference": "",
     "EAN13": "",
     "UPC": "",
     "Wholesale price": "",
     "Impact on price": "",
     "Ecotax": "",
     "Quantity": "",
     "Minimal quantity": "",
     "Low stock level": "",
     "Impact on weight": "",
     "Default (0/1)": "",
     "Combination available date": "",
     "Image position": "",
     "Image URLs(x,y,z)": "",
     "Image Alt Text(x,y,z)": "",
     "shop": "1,2,3,4",
     "Advanced Stock Mangment": 0,
     "Depends On Stock": 0,
     "Warehouse": 0
   }
   ```

Fields
-------

The JSON schema defines the following fields:

*  `Product ID`:  (Empty String) -  Represents the product identifier.
*  `Attribute (Name:Type:Position)`: (Empty String) - Details of the attribute, including its name, type, and position.
*  `Value (Value:Position)`: (Empty String) -  Describes the value of an attribute and its position.
*  `Supplier reference`: (Empty String) -  The supplier's reference for the product.
*  `reference`: (Empty String) -  The product's reference.
*  `EAN13`: (Empty String) -  The EAN13 code of the product.
*  `UPC`: (Empty String) -  The UPC code of the product.
*  `Wholesale price`: (Empty String) -  The wholesale price of the product.
*  `Impact on price`: (Empty String) -  Details how this combination impacts the price.
*  `Ecotax`: (Empty String) -  Ecotax details.
*  `Quantity`: (Empty String) -  The available quantity for this combination.
*  `Minimal quantity`: (Empty String) -  The minimum quantity allowed for this combination.
*  `Low stock level`: (Empty String) -  The level at which the stock is considered low.
*  `Impact on weight`: (Empty String) -  The effect of this combination on the product weight.
*  `Default (0/1)`: (Empty String) -  Indicates if this combination is the default.  0 for no, 1 for yes.
*  `Combination available date`: (Empty String) -  Date when this combination became available.
*  `Image position`: (Empty String) -  Position of the image for this combination.
*  `Image URLs(x,y,z)`: (Empty String) -  A comma-separated list of image URLs for this combination (x, y, z represent different variations).
*  `Image Alt Text(x,y,z)`: (Empty String) -  Comma-separated list of alt text for images.
*  `shop`: `"1,2,3,4"` - Comma-separated list of shop identifiers where this combination is available.
*  `Advanced Stock Mangment`: `0` - Flag for advanced stock management (0 for no, 1 for yes).
*  `Depends On Stock`: `0` - Flag indicating whether this combination depends on the stock of another product (0 for no, 1 for yes).
*  `Warehouse`: `0` - Warehouse assigned to this product combination.