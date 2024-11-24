Module src.suppliers.hb.category
==============================

.. module:: src.suppliers.hb.category
   :platform: Windows, Unix
   :synopsis: Module for collecting product data from the category pages of hb.co.il supplier using a webdriver.

Description
-----------

This module handles the process of gathering product information from category pages on the hb.co.il website.  Each supplier has a unique approach to handling categories, requiring tailored logic.

- **Category Listing (`get_list_categories_from_site`):**  Collects a list of available categories from the supplier's site.  **Note:** Needs implementation to handle potential category changes (new, renamed, hidden/removed categories). The module should maintain a mapping between `PrestaShop` categories and the supplier's categories.
- **Product Listing (`get_list_products_in_category`):** Gathers a list of product URLs within a given category. It handles potential pagination by calling the `paginator` function if there are more pages.
- **Product Data Retrieval (`grab_product_page` - *implied*):** (Not implemented in the provided code, but implied.) Processes the details for each product from its individual page.  The functionality will likely involve extracting product attributes and passing them to a `Product` class for storage or further processing.


Functions
---------

.. autofunction:: get_list_products_in_category
   :noindex:

.. autofunction:: paginator
   :noindex:

.. autofunction:: get_list_categories_from_site
   :noindex:


.. automodule:: src.suppliers.hb.category
    :members:
    :undoc-members:
    :show-inheritance: