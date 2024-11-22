## \file hypotez/src/db/manager_coupons_and_sales/__init__.py
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe
#! venv/bin/python/python3.12

"""
.. module: src.db.manager_coupons_and_sales 
	:platform: Windows, Unix
	:synopsis:

"""
MODE = 'development'

from .product_group_reduction_cache_manager import ProductGroupReductionCacheManager
from .product_campaigns import ProductCampaignsManager