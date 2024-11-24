PrestaShop Module Overview
==========================

This module provides an interface for interacting with the PrestaShop API,
offering functionalities for various aspects of the platform, from managing
products and categories to handling customer data, languages, and more.


.. toctree::
   :maxdepth: 2

   category
   customer
   language
   pricelist
   product
   shop
   supplier
   version
   warehouse
   api
   api_schemas
   domains


Category
--------

~ Purpose: Manages category-related functionality.
~ Functionality: Handles operations related to product categories,
  interacting with the PrestaShop API to manage category data.

.. automodule:: PrestaShop.category
    :members:
    :undoc-members:
    :show-inheritance:


Customer
--------

~ Purpose: Manages customer-related functionality.
~ Functionality: Handles operations related to customers,
  interacting with the PrestaShop API to manage customer data.

.. automodule:: PrestaShop.customer
    :members:
    :undoc-members:
    :show-inheritance:


Language
--------

~ Purpose: Manages language-related functionality.
~ Functionality: Handles operations related to languages,
  interacting with the PrestaShop API to manage language data.

.. automodule:: PrestaShop.language
    :members:
    :undoc-members:
    :show-inheritance:


Pricelist
---------

~ Purpose: Manages price list-related functionality.
~ Functionality: Handles operations related to price lists,
  interacting with the PrestaShop API to manage price list data.

.. automodule:: PrestaShop.pricelist
    :members:
    :undoc-members:
    :show-inheritance:


Product
-------

~ Purpose: Manages product-related functionality.
~ Functionality: Handles operations related to products,
  interacting with the PrestaShop API to manage product data.

.. automodule:: PrestaShop.product
    :members:
    :undoc-members:
    :show-inheritance:


Shop
----

~ Purpose: Manages shop-related functionality.
~ Functionality: Handles operations related to shops,
  interacting with the PrestaShop API to manage shop data.

.. automodule:: PrestaShop.shop
    :members:
    :undoc-members:
    :show-inheritance:


Supplier
--------

~ Purpose: Manages supplier-related functionality.
~ Functionality: Handles operations related to suppliers,
  interacting with the PrestaShop API to manage supplier data.

.. automodule:: PrestaShop.supplier
    :members:
    :undoc-members:
    :show-inheritance:


Version
-------

^ Purpose: Manages the version information of the module.

.. automodule:: PrestaShop.version
    :members:
    :undoc-members:
    :show-inheritance:


Warehouse
---------

~ Purpose: Manages warehouse-related functionality.
~ Functionality: Handles operations related to warehouses,
  interacting with the PrestaShop API to manage warehouse data.

.. automodule:: PrestaShop.warehouse
    :members:
    :undoc-members:
    :show-inheritance:


API
---

^ Purpose: Provides an interface for interacting with the PrestaShop API.
^ Functionality: Contains the main logic for making API requests and handling responses,
  providing methods for accessing various API resources.

.. automodule:: PrestaShop.api
    :members:
    :undoc-members:
    :show-inheritance:



API Schemas
-----------

^ Purpose: Defines schemas for the PrestaShop API resources.
^ Functionality: Contains JSON schema files for various API resources,
  providing scripts for building and managing API schemas.

.. automodule:: PrestaShop.api_schemas
    :members:
    :undoc-members:
    :show-inheritance:



Domains
-------

^ Purpose: Contains subdirectories for different domains, each with their own settings and configurations.

.. toctree::
   :maxdepth: 1

   domains/ecat_co_il
   domains/emildesign_com
   domains/sergey_mymaster_co_il


Example Usage
============

^ Here's an example of how to use the `product` module:

.. code-block:: python

    from PrestaShop.product import Product

    product = Product()
    product_data = product.get_product_data(product_id="12345")
    print(product_data)