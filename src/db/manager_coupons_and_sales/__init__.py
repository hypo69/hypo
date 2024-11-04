""" Менеджер скидок, купонов и т.п. в Prestashop  """
...
## \file ../src/db/manager_coupons_and_sales/__init__.py
# -*- coding: utf-8 -*-
# /path/to/interpreter/python
...
from packaging.version import Version
from .version import __version__, __doc__, __details__  

from .product_group_reduction_cache_manager import ProductGroupReductionCacheManager
from .product_campaigns import ProductCampaignsManager