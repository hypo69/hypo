## \file src/suppliers/kualastyle/via_webdriver.py
"""    parsing kualastyle via webdriver

@namespace src: src
 \package src.suppliers.kualastyle
\file via_webdriver.py
 
 @section libs imports:
  - helpers 
  - typing 
  - gs 
  
Author(s):
  - Created by [Name] [Last Name] on 08.11.2023 .
"""


## \file ../src/suppliers/kualastyle/via_webdriver.py
# -*- coding: utf-8 -*-
# /path/to/interpreter/python


from src.logger import logger
from typing import Union

from src import gs
from src.logger import logger

def get_list_products_in_category(s) -> list[str,str,None]:    
    """ Returns list of products urls from category page
    Attrs:
        s - Suplier
    @returns
        list of products urls or None
    """
    d = s.driver
    l: dict = s.locators.get('category')
    d.scroll(scroll_count = 10, direction = "forward")

    _ = d.execute_locator
    list_products_in_category = _(l['product_links'])
    #pprint(list_products_in_category)
    return list_products_in_categoryy