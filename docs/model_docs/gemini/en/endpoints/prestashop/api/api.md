```rst
hypotez.endpoints.prestashop.api
===============================

.. module:: hypotez.endpoints.prestashop.api
    :members:
    :undoc-members:
    :show-inheritance:

This module provides an interface for interacting with the PrestaShop API. It allows various operations such as creating, reading, updating, deleting resources, searching, and uploading images.  The module handles both JSON and XML data formats.


Classes
-------

.. autoclass:: hypotez.endpoints.prestashop.api.Format
    :members:
    :show-inheritance:

.. autoclass:: hypotez.endpoints.prestashop.api.PrestaShop
    :members:
    :show-inheritance:


Functions
---------

.. autofunction:: hypotez.endpoints.prestashop.api.PrestaShop.__init__
.. autofunction:: hypotez.endpoints.prestashop.api.PrestaShop.ping
.. autofunction:: hypotez.endpoints.prestashop.api.PrestaShop._check_response
.. autofunction:: hypotez.endpoints.prestashop.api.PrestaShop._parse_response_error
.. autofunction:: hypotez.endpoints.prestashop.api.PrestaShop._prepare
.. autofunction:: hypotez.endpoints.prestashop.api.PrestaShop._exec
.. autofunction:: hypotez.endpoints.prestashop.api.PrestaShop._parse
.. autofunction:: hypotez.endpoints.prestashop.api.PrestaShop.create
.. autofunction:: hypotez.endpoints.prestashop.api.PrestaShop.read
.. autofunction:: hypotez.endpoints.prestashop.api.PrestaShop.write
.. autofunction:: hypotez.endpoints.prestashop.api.PrestaShop.unlink
.. autofunction:: hypotez.endpoints.prestashop.api.PrestaShop.search
.. autofunction:: hypotez.endpoints.prestashop.api.PrestaShop.create_binary
.. autofunction:: hypotez.endpoints.prestashop.api.PrestaShop._save
.. autofunction:: hypotez.endpoints.prestashop.api.PrestaShop.get_data
.. autofunction:: hypotez.endpoints.prestashop.api.PrestaShop.remove_file
.. autofunction:: hypotez.endpoints.prestashop.api.PrestaShop.get_apis
.. autofunction:: hypotez.endpoints.prestashop.api.PrestaShop.get_languages_schema
.. autofunction:: hypotez.endpoints.prestashop.api.PrestaShop.upload_image_async
.. autofunction:: hypotez.endpoints.prestashop.api.PrestaShop.upload_image
.. autofunction:: hypotez.endpoints.prestashop.api.PrestaShop.get_product_images


Module Constants
-----------------

.. data:: hypotez.endpoints.prestashop.api.MODE
    :type: str
    :value: 'development'
```