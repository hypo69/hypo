## \file hypotez/src/product/product_fields/utils/__init__.py
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe # <- venv win
## ~~~~~~~~~~~~~
""" module: src.product.product_fields.utils """

"""   Модуль в основном используется для обработки полей товара Prestashop. 
@details Внешние классы и аттрибуты:
- `Product`   методы и атрибуты товара   Подробное описание см в `product.py`
- `ProductFields`  поля товара. Подробное описание см в `product_fields.py`
- `record` словарь полей товара в плоском виде (без вложенностей)
- `translate_presta_fields_dict` Функция переводит мультиязычные поля  ProductFields
"""
...
from packaging.version import Version
from .version import __version__, __doc__, __details__

from .product_fields_normalizer import (normalize_product_name,
                                        normalize_bool,
                                        )