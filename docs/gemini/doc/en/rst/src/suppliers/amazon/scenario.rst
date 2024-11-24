Amazon Supplier Scenario Module
=============================

.. module:: hypotez.src.suppliers.amazon.scenario
    :platform: Windows, Unix
    :synopsis: Module for collecting product data from Amazon category pages using a web driver.

Module Description
------------------

This module defines the scenario for collecting products from Amazon category pages.  Each supplier has a specific scenario for handling categories.  This module handles the following:

- Gathering a list of categories from the supplier's pages (`get_list_categories_from_site()`).  Note the need to implement a check for changes in categories to handle updates, renames, and deletions/hiding of categories.  This involves maintaining a table mapping `PrestaShop.categories` to `aliexpress.shop.categories`.
- Gathering a list of product URLs from a given category page (`get_list_products_in_category()`).
- Iterating through the product list and calling `grab_product_page()` for each product URL to process product details and pass them to the `Product` class.


Functions
---------

.. autofunction:: get_list_products_in_category