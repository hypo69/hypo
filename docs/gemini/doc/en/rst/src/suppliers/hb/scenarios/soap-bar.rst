Soap Bar Data
============

This file contains data about soap bars, including the product URL, name, condition, and PrestaShop categories.


Data Structure
--------------

The data is structured as a JSON object with the following keys:

~ url (~):
    The URL of the product page.

~ name (~):
    The name of the product.

~ condition (~):
    An array of strings representing the product condition.  In this case, only "new" is present.

~ presta_categories (~):
    A dictionary containing PrestaShop category information.

    ^ default_category (^):
        The ID of the default category for the product.

    ^ additional_categories (^):
        An array of additional category IDs.  Currently empty.


JSON Data Example
----------------

.. code-block:: json
    
    {
        "url": "https://hbdeadsea.co.il/product-category/soap-bar/",
        "name": "סבונים מוצקים",
        "condition": [
            "new"
        ],
        "presta_categories": {
            "default_category": 11111,
            "additional_categories": [
                ""
            ]
        }
    }