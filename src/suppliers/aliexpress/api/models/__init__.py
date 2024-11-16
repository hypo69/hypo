## \file hypotez/src/suppliers/aliexpress/api/models/__init__.py
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe

""" module: src.suppliers.aliexpress.api.models """
MODE = 'debug'
""" module: src.suppliers.aliexpress.api.models """
MODE = 'debug'
from .languages import Language
from .currencies import Currency
from .request_parameters import ProductType, SortBy, LinkType
from .affiliate_link import AffiliateLink
from .hotproducts import HotProductsResponse
from .product import Product
from .category import Category, ChildCategory

