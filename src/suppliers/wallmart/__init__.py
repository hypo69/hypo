## \file ../src/suppliers/wallmart/__init__.py
## \file ../src/suppliers/wallmart/__init__.py
# -*- coding: utf-8 -*-
# /path/to/interpreter/python
"""  Постaвщик <i>wallmart</i>
"""
...
from packaging.version import Version
from .version import __version__, __doc__, __details__ 

from src import gs
from .login import login as login
from .scrapper import grab_product_page as grab_product_page
from .via_webdriver import get_list_products_in_category as get_list_products_in_category


