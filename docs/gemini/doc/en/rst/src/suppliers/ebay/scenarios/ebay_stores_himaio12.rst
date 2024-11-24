ebay_stores_himaio12.json
==========================

This file defines the eBay store configuration for the "himaio12" store. It includes details about the store, its products, and the scenarios for specific product categories.  The data is formatted as a JSON object.


.. code-block:: json
    {
      "store": {
        "store_id": "thegasketsman75",
        "supplier_id": 4534,
        "get store banners": true,
        "description": "thegasketsman75 Gasket KIT",
        "about": " ",
        "url": "https://www.ebay.com/str/himaio12",
        "shop categories page": "",
        "shop categories json file": ""
      },

      "scenarios": {
        "Gaming Concoles": {
          "url": "https://www.ebay.com/str/himaio12",
          "active": true,
          "condition":"new",
          "presta_categories": {
            "template": { "gaming": "CONSOLES" }
          },
          "checkbox": false,
          "price_rule": 1
        }
      }
    }



Store Details
-------------

*   `store_id`:  Identifies the eBay store.
*   `supplier_id`:  The supplier's unique identifier.
*   `get store banners`:  Indicates if store banners are required.
*   `description`: A brief description of the store.
*   `about`:  Additional details about the store (empty in this case).
*   `url`: The URL of the store on eBay.
*   `shop categories page`: (empty)
*   `shop categories json file`: (empty)


Scenarios
---------

~   `Gaming Concoles`:
    ^   `url`: The URL for the specific scenario.
    ^   `active`: Indicates if the scenario is active.
    ^   `condition`: The product condition.
    ^   `presta_categories`:  Details about the product categories.
        ~   `template`:  Provides the specific PrestaShop category mappings.
    ^   `checkbox`:  (Boolean) for filtering in the scenario.
    ^   `price_rule`:  Indicates a rule for pricing (value 1).