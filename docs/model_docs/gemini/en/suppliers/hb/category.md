```rst
hb Category Module
==================

This module handles the retrieval of product information from the hb.co.il website.  It focuses on gathering categories, products within categories, and ultimately, detailed product information.


.. automodule:: hypotez.src.suppliers.hb.category
    :members:
    :undoc-members:
    :show-inheritance:

Functions
---------

.. autofunction:: hypotez.src.suppliers.hb.category.get_list_products_in_category
   :noindex:

   Retrieves a list of product URLs from a given category page.  It handles potential pagination, warnings for missing product links, and logging for debugging.

.. autofunction:: hypotez.src.suppliers.hb.category.paginator
   :noindex:

   Handles pagination on product category pages.

.. autofunction:: hypotez.src.suppliers.hb.category.get_list_categories_from_site
   :noindex:

   Retrieves a list of categories from the target website.
```
