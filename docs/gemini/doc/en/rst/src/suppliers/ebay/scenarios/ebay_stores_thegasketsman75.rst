ebay_stores_thegasketsman75.json
=================================

This file contains configuration data for the eBay store "thegasketsman75".
It defines store details, scenarios for products, and related settings.

.. code-block:: json
   :linenos:

   ```json
   {
     "store": {
       "store_id": "thegasketsman75",
       "supplier_id": 4534,
       "get store banners": true,
       "description": "thegasketsman75 Gasket KIT",
       "about": " ",
       "url": "https://www.ebay.com/str/thegasketsman75",
       "shop categories page": "",
       "shop categories json file": ""
     },
     "scenarios": {
       "Gasket KIT": {
         "url": "https://www.ebay.com/str/thegasketsman75",
         "active": true,
         "condition":"new",
         "presta_categories": {
           "template": { "gasket KIT": "GASKET KIT" }
         },
         "checkbox": false,
         "price_rule": 1
       }
     }
   }
   ```