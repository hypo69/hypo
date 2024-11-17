## \file hypotez/src/endpoints/prestashop/category.py
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe
#! venv/bin/python
""" module: src.endpoints.prestashop """
MODE = 'development'


""" Class of product category in `PrestaShop`
The class provides methods for adding, deleting, updating categories, 
as well as obtaining a list of parent categories from a given one.

@details `PrestaCategory` layer between client categories (PrestaShop, in my case) and suppliers
 
locator_description Clients can each have their own unique category tree, which is only understandable to them. 
Product binding to category is described in supplier scenarios

@image html categories_tree.png 
"""
...

...
import requests
from attr import attr, attrs
from pathlib import Path
from typing import List, Dict
from types import SimpleNamespace

import header
from src import gs
from src.utils import j_loads
from .api import PrestaShop
from src.logger import logger


from typing import Optional

class PrestaCategory(PrestaShop):
    """    
    Класс для работы с категориями в PrestaShop.

    Пример использования класса:

    .. code-block:: python

        prestacategory = PrestaCategory(API_DOMAIN=API_DOMAIN, API_KEY=API_KEY)
        prestacategory.add_category_PrestaShop('New Category', 'Parent Category')
        prestacategory.delete_category_PrestaShop(3)
        prestacategory.update_category_PrestaShop(4, 'Updated Category Name')
        print(prestacategory.get_parent_categories_list_PrestaShop(5))
    """
    
    def __init__(self, 
                 credentials: Optional[dict | SimpleNamespace] = None, 
                 api_domain: Optional[str] = None, 
                 api_key: Optional[str] = None, 
                 *args, **kwards):
        """Инициализация категории PrestaShop.

        Args:
            credentials (Optional[dict | SimpleNamespace], optional): Словарь или объект SimpleNamespace с параметрами `api_domain` и `api_key`. Defaults to None.
            api_domain (Optional[str], optional): Домен API. Defaults to None.
            api_key (Optional[str], optional): Ключ API. Defaults to None.
        """
        
        if credentials is not None:
            api_domain = credentials.get('api_domain', api_domain)
            api_key = credentials.get('api_key', api_key)
        
        if not api_domain or not api_key:
            raise ValueError('Необходимы оба параметра: api_domain и api_key.')
        
        super().__init__(api_domain, api_key, *args, **kwards)


    
    def get_parent_categories_list(self, id_category: str | int,  parent_categories_list:List[int] = []) -> list:
        """  Вытаскивет из базы данных PrestaShop родительские категории от заданной 
        @details функция через API получает список категорий

        @param id_category `int`  категория для которой надо вытащить родителя
        @param dept `int = 0` : глубина рекурсии. Если 0, глубина не ограчинена
        @returns `list`  Список родительских категорий
        @todo обработать ситуацию, кода у клиента нет такой категории. 
        Напимер в магазине мебели не должно быть категории `motherboards`
        """
        #logger.debug(f"\n\n Собираю родительские категории для {id_category} \n\n")
        
        # 1. Получение родительской категории у `id_category`
        
        if not id_category:
            logger.error(f"""Нет id категории!!!
                         {parent_categories_list}
                    Если отправить запрос без id вернется словарь со всми категориями""")
            return parent_categories_list
        category = super().get('categories', resource_id = id_category, display='full', io_format='JSON')
        """ возвращает словарь
        @code
        {'category': 
                {'id': 11259, 
                'id_parent': '11248', 
                'level_depth': '5', 
                'nb_products_recursive': -1, 
                'active': '1', 
                'id_shop_default': '1', 
                'is_root_category': '0', 
                'position': '0', 
                'date_add': '2023-07-25 11:58:08', ...}
        }```"""
        ...
        if not category:
            logger.error(f'Что-то не так с категориями')
            return

        _parent_category: int = int(category['id_parent'])         
        parent_categories_list.append (_parent_category)     
        # for category_dict in category_dict['categories'] :
        #     _parent_category: int = int (category_dict['id_parent'])
        #     parent_categories_list.append (_parent_category)

        if _parent_category <= 2: ## <- `2` корневая директория
            #logger.debug (f'\n\n\n Собрал родительские категории: {parent_categories_list} \n\n')
            return parent_categories_list
            ...
        else:
            return self.get_parent_categories_list(_parent_category, parent_categories_list)