## \file src/suppliers/gearbest/__init__.py
## \file ../src/suppliers/gearbest/__init__.py
# -*- coding: utf-8 -*-
# /path/to/interpreter/python
"""  Поставщик <I>gearbest.com</I>
"""
...
from .login import login as login
from .scrapper import grab_product_page as grab_product_page
from .via_webdriver import get_list_products_in_category as get_list_products_in_category

# ----------------------------------
from src import gs

from src.logger import logger
from src.webdriver import Driver
from src.scenario import scenario
# ----------------------------------

