Product Module
=============

.. module:: hypotez.src.product
    :platform: Windows, Unix
    :synopsis: Product module

External classes and attributes:
- `Product`: Methods and attributes of the product. Detailed description in `product.py`
- `ProductFields`: Product fields. Detailed description in `product_fields.py`
- `record`: A dictionary of product fields in flat format (without nesting)
- `translate_presta_fields_dict`: Function that translates multilingual fields of `ProductFields`


Module Constants
----------------

.. autodata:: hypotez.src.product.MODE


Classes
-------

.. autoclass:: hypotez.src.product.Product
    :members:
    :undoc-members:
    :show-inheritance:

.. autoclass:: hypotez.src.product.ProductFields
    :members:
    :undoc-members:
    :show-inheritance:


Functions
---------

.. autofunction:: hypotez.src.product.translate_presta_fields_dict
    :noindex: