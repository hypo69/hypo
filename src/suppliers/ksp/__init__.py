## \file src/suppliers/ksp/__init__.py
"""  Поставщик <I>ksp.co.il</I>

 @section libs imports:
  - .scrapper 
  - .via_webdriver 
"""

## \file ../src/suppliers/ksp/__init__.py
# -*- coding: utf-8 -*-
# /path/to/interpreter/python


from .scrapper import grab_product_page as grab_product_page
from .via_webdriver import get_list_products_in_category as get_list_products_in_category


