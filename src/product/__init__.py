## \file hypotez/src/product/__init__.py
# -*- coding: utf-8 -*-

""" module: src.product """
MODE = 'debug'
""" module: src.product """
MODE = 'debug'
""" Product module
External classes and attributes:
- `Product`: Methods and attributes of the product. Detailed description in `product.py`
- `ProductFields`: Product fields. Detailed description in `product_fields.py`
- `record`: A dictionary of product fields in flat format (without nesting)
- `translate_presta_fields_dict`: Function that translates multilingual fields of `ProductFields`
"""

from packaging.version import Version
from .version import __version__, __doc__, __details__

from .product import Product
from .product_fields.product_fields import ProductFields
from .product_fields.product_fields_translator import translate_presta_fields_dict
