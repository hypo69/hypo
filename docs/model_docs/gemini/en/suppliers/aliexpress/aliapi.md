```rst
aliapi.py
===========

.. module:: hypotez.src.suppliers.aliexpress.aliapi
    :members:
    :undoc-members:
    :show-inheritance:

Module Description
------------------

This module provides an API interface for interacting with the AliExpress platform.  It handles tasks such as retrieving product details, generating affiliate links, and potentially managing data from AliExpress into databases, and working with XLS files.  It utilizes various external libraries like `requests`, `json`, and `asyncio` for its functionality.  It is designed to be integrated with other parts of the application for data collection and processing.  It also defines a custom class `AliApi` inheriting from `AliexpressApi` to extend its functionalities.

Classes
-------

.. autoclass:: hypotez.src.suppliers.aliexpress.aliapi.AliApi
    :members:
    :undoc-members:
    :show-inheritance:

Functions
---------

.. autofunction:: hypotez.src.suppliers.aliexpress.aliapi.AliApi.__init__
.. autofunction:: hypotez.src.suppliers.aliexpress.aliapi.AliApi.retrieve_product_details_as_dict
.. autofunction:: hypotez.src.suppliers.aliexpress.aliapi.AliApi.get_affiliate_links
```
