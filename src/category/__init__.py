## \file hypotez/src/category/__init__.py
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe # <- venv win
#! venv/bin/python # <- venv linux/macos
#! py # <- system win
#! /usr/bin/python # <- system linux/macos
## ~~~~~~~~~~~~~
""" module: src.category """
""" Manege product categories for Prestashop"""

from packaging.version import Version
from .version import __version__, __doc__, __details__

from .category import Category, crawl_categories
