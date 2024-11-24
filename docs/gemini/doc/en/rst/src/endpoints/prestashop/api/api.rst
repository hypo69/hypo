hypotez/src/endpoints/prestashop/api/api.py
=========================================

.. module:: hypotez.src.endpoints.prestashop.api.api
    :platform: Windows, Unix
    :synopsis: This module provides a class for interacting with the PrestaShop web service API, using JSON or XML for communication.

Classes
-------

.. autoclass:: Format
    :members:
    :undoc-members:
    :show-inheritance:

.. autoclass:: PrestaShop
    :members:
    :undoc-members:
    :show-inheritance:

Functions
---------

.. autofunction:: PrestaShop._check_response
.. autofunction:: PrestaShop._parse_response_error
.. autofunction:: PrestaShop._prepare
.. autofunction:: PrestaShop._exec
.. autofunction:: PrestaShop._parse
.. autofunction:: PrestaShop.create
.. autofunction:: PrestaShop.read
.. autofunction:: PrestaShop.write
.. autofunction:: PrestaShop.unlink
.. autofunction:: PrestaShop.search
.. autofunction:: PrestaShop.create_binary
.. autofunction:: PrestaShop._save
.. autofunction:: PrestaShop.get_data
.. autofunction:: PrestaShop.remove_file
.. autofunction:: PrestaShop.get_apis
.. autofunction:: PrestaShop.get_languages_schema
.. autofunction:: PrestaShop.upload_image_async
.. autofunction:: PrestaShop.upload_image
.. autofunction:: PrestaShop.get_product_images
.. autofunction:: PrestaShop.ping