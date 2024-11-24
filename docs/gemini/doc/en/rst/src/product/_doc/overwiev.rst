Product Module Overview
=======================

This document provides an overview of the `product` module, including its key components, functionality, and example usage.

.. toctree::
   :maxdepth: 2

   locator
   product
   product_fields
   version

Key Components
-------------

The `product` module consists of several interconnected components:

* **Locator:** Defines locators for web elements related to product pages, enabling interaction using Selenium WebDriver.

* **Product:** Manages product-related functionality, including retrieving product data and interacting with product fields.

* **Product Fields:** Manages product attributes, including defining fields, default values, and translations.

* **Version Management:** Defines the current version of the module.

* **Documentation and Examples:** Provides documentation and examples to aid developers in understanding and using the module effectively.  (Located in the `_examples` directory).

Example Usage
------------

Here's a simplified example of how to use the `product` module:

.. code-block:: python
   :linenos:

   from product.product import Product
   from product.product_fields import ProductFields

   # Initialize the Product and ProductFields
   product = Product()
   product_fields = ProductFields()

   # Example operation on product
   product_data = product.get_product_data(product_id="12345")
   product_fields.update_field("price", 19.99)

   print(product_data)

Additional Information
---------------------

The `product_fields` directory contains the following files:

* `product_fields.py`: Defines the product fields and their associated operations.
* `product_fields_default_values.json`: JSON file containing default values for product fields.
* `product_fields_translator.py`: Handles translation of field names and values (if applicable).

The `_examples` directory contains example scripts and documentation files to aid in understanding the module's usage.

.. note::

    This is a high-level overview. More detailed information about specific classes and functions can be found in the individual module documentation.