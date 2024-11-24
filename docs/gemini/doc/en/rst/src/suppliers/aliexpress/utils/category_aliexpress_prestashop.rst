Module category_aliexpress_prestashop
=====================================

This module contains mappings between AliExpress categories and PrestaShop categories.  It defines a structure to connect product categories on AliExpress with corresponding categories in PrestaShop.

Data Structure
-------------

The data is stored in a JSON format, mapping AliExpress category IDs to dictionaries containing the AliExpress category name, parent category ID (if any), a list of corresponding PrestaShop category IDs, and the main PrestaShop category.

.. code-block:: json
  :linenos:

  ```json
  {
    "39": {
      "ali_category_name": "Lights & Lighting",
      "ali_parent": "",
      "PrestaShop_categories": [],
      "PrestaShop_main_category": ""
    },
    "1504": {
      "ali_category_name": "Indoor Lighting",
      "ali_parent": "39",
      "PrestaShop_categories": [],
      "PrestaShop_main_category": ""
    }
  }
  ```


Data Format Details
------------------

~ Key:
  ^ `ali_category_name`: String representing the name of the AliExpress category.
  ^ `ali_parent`: String representing the parent category ID on AliExpress (empty string if root).
  ^ `PrestaShop_categories`: A list of strings representing the corresponding PrestaShop category IDs.
  ^ `PrestaShop_main_category`: String representing the main PrestaShop category to which the AliExpress category is linked.


Usage Notes
-----------

This module is intended to be used in conjunction with a mapping/matching mechanism between AliExpress and PrestaShop product catalogs for enhanced product organization and display.  The exact methods for utilizing this mapping depend on the system architecture.