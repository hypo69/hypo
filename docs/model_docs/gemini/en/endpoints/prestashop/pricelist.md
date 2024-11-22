```rst
Pricelist Endpoint
==================

.. module:: hypotez.src.endpoints.prestashop.pricelist
   :platform: Windows, Unix
   :synopsis: Module for interacting with PrestaShop API to get and modify product prices.


Description
----------

This module provides a `PriceListRequester` class for interacting with the PrestaShop API to fetch and modify product prices. It inherits from the `PrestaShop` class, allowing it to use the API's methods to retrieve necessary data.

Classes
-------

.. autoclass:: PriceListRequester
   :members:
   :undoc-members:
   :show-inheritance:

Functions
--------

.. autofunction:: hypotez.src.endpoints.prestashop.pricelist.PriceListRequester.__init__
.. autofunction:: hypotez.src.endpoints.prestashop.pricelist.PriceListRequester.request_prices
.. autofunction:: hypotez.src.endpoints.prestashop.pricelist.PriceListRequester.update_source
.. autofunction:: hypotez.src.endpoints.prestashop.pricelist.PriceListRequester.modify_product_price
```
