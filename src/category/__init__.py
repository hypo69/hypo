## \file src/category/__init__.py
## \file ../src/category/__init__.py
# -*- coding: utf-8 -*-
""" Manege product categories for Prestashop"""

from packaging.version import Version
from .version import __version__, __doc__, __details__

from .category import Category, crawl_categories
