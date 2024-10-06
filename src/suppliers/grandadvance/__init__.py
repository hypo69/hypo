## \file src/suppliers/grandadvance/__init__.py
"""  Поставщик <I>granadvance.co.il</I>

 
 @section libs imports:
  - .login 
  - .scrapper 
  - .via_webdriver 

"""


## \file ../src/suppliers/grandadvance/__init__.py
# -*- coding: utf-8 -*-
# /path/to/interpreter/python


from .login import login as login
from .scrapper import scrape_product_page as scrape_product_page
from .via_webdriver import get_list_products_in_category as get_list_products_in_category

