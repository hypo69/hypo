ensure_https Module
===================

.. module:: hypotez.src.suppliers.aliexpress.utils.ensure_https
   :platform: Windows, Unix
   :synopsis: Ensures that the provided URL string(s) contain the https:// prefix. If the input is a product ID, it constructs a full URL with https:// prefix.

Functions
--------

.. autofunction:: ensure_https
   :members:
   :undoc-members:
   :show-inheritance:

.. autofunction:: ensure_https_single
   :members:
   :undoc-members:
   :show-inheritance:


Example Usage
------------

.. code-block:: python
   # Example usage
   url = "example_product_id"
   url_with_https = ensure_https(url)
   print(url_with_https)  # Output: https://www.aliexpress.com/item/example_product_id.html

   urls = ["example_product_id1", "https://www.aliexpress.com/item/example_product_id2.html"]
   urls_with_https = ensure_https(urls)
   print(urls_with_https)  # Output: ['https://www.aliexpress.com/item/example_product_id1.html', 'https://www.aliexpress.com/item/example_product_id2.html']