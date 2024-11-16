## \file hypotez/src/suppliers/etzmaleh/via_webdriver.py
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe

""" module: src.suppliers.etzmaleh """
MODE = 'debug'
""" module: src.suppliers.etzmaleh """
MODE = 'debug'
"""   [File's Description]

@namespace src: src
 \package src.suppliers.etzmaleh
\file via_webdriver.py
 
 @section libs imports:
  - helpers 
  - typing 
  - gs 
Author(s):
  - Created by Davidka on 09.11.2023 .
"""


from src.logger import logger
from typing import Union

from __init__ import gs, logger

# def run_scenario_via_webdriver(s, scenario_files: list[str,str]) -> bool:
#     """ runs scerarios for supplier
#     @param
#         s (Supplier) - Supplier object
#         scenario_files (`list`,`str`) - scenario files names from scerarios directory
#     @returns
#         True, False
#         """
#     if isinstance(scenario_files, list):
#         return run_scenarios(s, scenario_files)
#     else:
#         return run_scenario_file(s, scenario_files)

def get_list_products_in_category(s) -> list[str,str,None]:    
    """ Returns list of products urls from category page
    Attrs:
        s - Suplier
    @returns
        list of products urls or None
    """
    _d = s.driver
    _l: dict = s.locators.get('category')
    
    _d.scroll()
    list_products_in_category = _d.execute_locator(_l['product_links'])
    """ Собираю ссылки на товары.  """
    if not list_products_in_category:
        logger.info('Нет ссылок на товары')
        return
    if isinstance(list_products_in_category, str) and len(list_products_in_category)>0:
        list_products_in_category = [list_products_in_category]

    logger.info(f""" Найдено {len(list_products_in_category)} товаров """)

    #""" Проверяю наличие товара в базе данных магазина """
    #for asin in list_products_in_category:
    #    _asin = asin.split(f'''/''')[-2]
    #    _sku = f'''{s.supplier_id}_{_asin}''' 
    #    if PrestashopProduct.check(_sku) == False:
    #        """ Синтаксис для того, чтобы помнить,
    #        что я проверяю ОТСУТСТВИЕ товара в базе данных
    #        """
    #        continue
    #    else:
    #        """ Товар в базе данных """
    #        continue
            #TODO: Логику 
    return list_products_in_category

