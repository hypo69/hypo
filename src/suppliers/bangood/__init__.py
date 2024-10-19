## \file src/suppliers/bangood/__init__.py
## \file ../src/suppliers/bangood/__init__.py
# -*- coding: utf-8 -*-
# /path/to/interpreter/python
"""  Поставщик <I>hb.co.il</I> """

from packaging.version import Version
from .version import __version__, __doc__, __details__  

from .via_webdriver import get_list_products_in_category, get_list_categories_from_site
from .grabber import grab_product_pagee