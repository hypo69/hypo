bangood Scenario Module
=======================

.. module:: hypotez.src.suppliers.bangood.scenario
    :platform: Windows, Unix
    :synopsis: This module defines functions for collecting product data from Banggood.

Module Description
------------------

This module handles the scenario for collecting product data from the Banggood website.  It includes functions for retrieving category lists, product lists within categories, and for processing product page data.  The module uses a web driver for interacting with the website.  The `MODE` variable determines the operation mode (e.g., 'dev').  The module also incorporates error handling and logging.

Functions
---------

.. autofunction:: get_list_products_in_category
.. autofunction:: get_list_categories_from_site