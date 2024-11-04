""" Class of product category in `Prestashop`
The class provides methods for adding, deleting, updating categories, 
as well as obtaining a list of parent categories from a given one.

@details `PrestaCategory` layer between client categories (Prestashop, in my case) and suppliers
 
locator_description Clients can each have their own unique category tree, which is only understandable to them. 
Product binding to category is described in supplier scenarios

@image html categories_tree.png 
"""
...
## \file src/endpoints/prestashop/category.py
# -*- coding: utf-8 -*-
# /path/to/interpreter/python
...
import requests
from attr import attr, attrs
from pathlib import Path
from typing import List, Dict

from src import gs
from src.utils import j_loads
from .api import Prestashop
from src.logger import logger


class PrestaCategory(Prestashop):
    """    
        Пример использования класса:
        @code    
        prestacategory = PrestaCategory(API_DOMAIN=API_DOMAIN, API_KEY=API_KEY)
        prestacategory.add_category_prestashop('New Category', 'Parent Category')
        prestacategory.delete_category_prestashop(3)
        prestacategory.update_category_prestashop(4, 'Updated Category Name')
        print(prestacategory.get_parent_categories_list_prestashop(5))
        ```    
    """

    
    def __init__(self, credentials, *args,**kwards):
        super().__init__(credentials)

    
    def get_parent_categories_list(self, id_category: str | int,  parent_categories_list:List[int] = []) -> list:
        """  Вытаскивет из базы данных Prestashop родительские категории от заданной 
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