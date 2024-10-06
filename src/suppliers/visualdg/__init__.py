## \file src/suppliers/visualdg/__init__.py
"""    Поставщик <i>visualdg.co.il</i>

@namespace src: src
 \package src.suppliers.visualdg
\file __init__.py
 
 @section libs imports:
  - .login 
  - .scrapper 
  - .via_webdriver 
Author(s):
  - Created by [Name] [Last Name] on 07.11.2023 .
"""

## \file ../src/suppliers/visualdg/__init__.py
# -*- coding: utf-8 -*-
# /path/to/interpreter/python



from .login import login as login
from .scrapper import grab_product_page as grab_product_page
from .via_webdriver import get_list_products_in_category as get_list_products_in_category


