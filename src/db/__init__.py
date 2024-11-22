## \file hypotez/src/db/__init__.py
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe
#! venv/bin/python/python3.12

"""
.. module: src.db 
	:platform: Windows, Unix
	:synopsis:

"""
MODE = 'development'

from .manager_translations import ProductTranslationsManager
from .manager_translations import CategoryTranslationsManager
from .manager_categories import CategoryManager
from .manager_categories import AliexpressCategory
from .manager_categories import AmazonCategory
from .manager_categories import EbayCategory
from .manager_categories import KualaCategory

from .manager_coupons_and_sales import ProductCampaignsManager
from .manager_coupons_and_sales import ProductGroupReductionCacheManager