## \file hypotez/src/endpoints/prestashop/__init__.py
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe # <- venv win
## ~~~~~~~~~~~~~
""" module: src.endpoints.prestashop """
""" Модуль обработки запросов к базам данных Prestashop.
Адаптер для API
"""
...

...
from packaging.version import Version
from .version import __version__, __doc__, __details__  

from .api import Prestashop
from .product import PrestaProduct
from .supplier import PrestaSupplier
from .category import PrestaCategory
from .warehouse import PrestaWarehouse
from .language import PrestaLanguage
from .shop import PrestaShop
from .pricelist import PriceListRequester
from .customer import PrestaCustomer
