#! /usr/bin/python
﻿## \file src/product/product_fields/__init__.py
## \file /src/product/product_fields/__init__.py
# -*- coding: utf-8 -*-
# /path/to/interpreter/python
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

from .product_fields import ProductFields
from .product_fields_translator import translate_presta_fields_dict