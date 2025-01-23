## \file /src/suppliers/amazon/scenario.py
# -*- coding: utf-8 -*-

#! .pyenv/bin/python3

"""
.. module:: src.suppliers.amazon 
	:platform: Windows, Unix
	:synopsis:

"""


"""
	:platform: Windows, Unix
	:synopsis:

"""

"""
	:platform: Windows, Unix
	:synopsis:

"""

"""
  :platform: Windows, Unix

"""
"""
  :platform: Windows, Unix
  :platform: Windows, Unix
  :synopsis:
"""
  
""" module: src.suppliers.amazon """


"""  Модуль сбора товаров со страницы категорий поставщика aliexpress.com через вебдрайвер

У каждого поставщика свой сценарий обреботки категорий

-Модуль Собирает список категорий со страниц продавца . `get_list_categories_from_site()`.
@todo Сделать проверку на изменение категорий на страницах продавца. 
Продавец может добавлять новые категории, переименовывать или удалять/прятать уже существующие. 
По большому счету надо держать таблицу категории `PrestaShop.categories <-> aliexpress.shop.categoies`
- Собирает список товаров со страницы категории `get_list_products_in_category()`
- Итерируясь по списку передает управление в `grab_product_page()` отсылая функции текущий url страницы  
`grab_product_page()` обрабатывает поля товара и передает управление классу `Product` 

"""



from typing import Union
from pathlib import Path

from src import gs
from src.logger.logger import logger


def get_list_products_in_category(s) -> list[str,str,None]:    
    """ Returns list of products urls from category page
    Если надо пролистстать - страницы категорий - листаю ??????

    Attrs:
    @param s: Supplier - Supplier intstance
    @returns list or one of products urls or None
    """
    d = s.driver
    l: dict = s.locators['category']
    if not l:
        """ Много проверок, потому, что код можно запускать от лица разных ихполнителей: Supplier, Product, Scenario """
        logger.error(f"А где локаторы? {l}")
        return
    d.scroll()

    #TODO: Нет листалки

    list_products_in_category = d.execute_locator(l['product_links'])
    """ Собираю ссылки на товары.  """
    if not list_products_in_category:
        logger.warning('Нет ссылок на товары')
        return
    
    list_products_in_category = [list_products_in_category] if isinstance(list_products_in_category, str) else list_products_in_category


    logger.info(f""" Найдено {len(list_products_in_category)} товаров """)
    
    #""" Проверяю наличие товара в базе данных магазина """
    #for asin in list_products_in_category:
    #    _asin = asin.split(f'''/''')[-2]
    #    _sku = f'''{s.supplier_id}_{_asin}''' 
    #    if PrestaShopProduct.check(_sku) == False:
    #        """ Синтаксис для того, чтобы помнить,
    #        что я проверяю ОТСУТСТВИЕ товара в базе данных
    #        """
    #        continue
    #    else:
    #        """ Товар в базе данных """
    #        continue
            #TODO: Логику 


    return list_products_in_category

     