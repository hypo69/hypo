## \file hypotez/src/category/category.py
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe # <- venv win
## ~~~~~~~~~~~~~
""" module: src.category """
""" @namespace src.category """

""" Модуль работы с категориями 
На сегодняшний день модуль заточен в основном под Престашоп
"""

from pathlib import Path
import os
import asyncio
from typing import List, Dict
from lxml import html
import requests
...
from __init__ import gs
from src.logger import  logger 
from src.utils import j_loads, j_dumps,  pprint
from src.utils.string import StringFormatter
from src.endpoints.prestashop import Prestashop
from src.endpoints.prestashop import PrestaCategory 


class Category (PrestaCategory):
    """ Класс категорий товара. Наследует `PrestaCategory` """
    ...
    
    credentials: dict = None

    def __init__(self, api_credentials, *args, **kwards):
        super().__init__(api_credentials, *args, **kwards)
        
    def get_parents(id_category, dept):
        return super().get_list_parent_categories(id_category)


async def crawl_categories_async(url, depth, driver, locator, dump_file, id_category_default, category: dict = None):
    """Asynchronous recursive function to crawl categories and build a hierarchical dictionary.

    @param url: The URL of the page to crawl.
    @param depth: The depth of recursion.
    @param driver: Selenium webdriver instance.
    @param locator: The xpath locator to find category links.
    @param parent_url: The URL of the parent category. Defaults to None.

    @return: A hierarchical dictionary representing categories and their URLs.
    """
    if category is None:
        category = {'url': url,
                    'name': '',
                    "presta_categories": {
                        "default_category": id_category_default,
                        "additional_categories": []
                    },
                    'children': {}}

    if depth <= 0:
        return category

    driver.get(url)
    driver.wait(1)
    category_links = driver.execute_locator(locator)
    if not category_links:
        logger.error(f"Что-то упало")
        ...
        return category

    tasks = []
    for link in category_links:
        for name, link_url in link.items():
            if check_duplicate_url(category, link_url):
                continue
            new_category = {'url': link_url,
                            'name': name,
                            "presta_categories": {
                                "default_category": id_category_default,
                                "additional_categories": []
                            },
                            'children': {}}
            task = crawl_categories_async(url=link_url,
                                          depth=depth - 1,
                                          driver=driver,
                                          locator=locator,
                                          dump_file=dump_file,
                                          id_category_default=id_category_default,
                                          category=new_category)
            tasks.append(task)

    # Wait for all tasks to complete
    await asyncio.gather(*tasks)

    return category

def crawl_categories(url, depth:int, driver, locator:dict, dump_file: Path, id_category_default, category: dict = {}):
    """Recursive function to crawl categories from website and build a hierarchical dictionary.

    @param url: The URL of the page to crawl.
    @param depth: The depth of recursion.
    @param driver: Selenium webdriver instance.
    @param locator: The xpath locator to find category links.
    @param dump_file: The file to dump the hierarchical dictionary.
    @param id_category_default: The default category ID.

    @return: A hierarchical dictionary representing categories and their URLs.
    """

    if depth <= 0:
        return category

    driver.get(url)
    driver.wait(1)
    category_links = driver.execute_locator(locator)
    if not category_links:
        ...
        return category

    for link in category_links:
        
        for name, link_url in link.items():
            
            
            if check_duplicate_url(category, link_url):
                continue
            new_category = {
                'url': link_url,
                'name': name,
                'presta_categories': {
                    "default_category": id_category_default,
                    "additional_categories": []
                }
            }
            category[name] = new_category
            
            

            crawl_categories(url=link_url,
                                             depth=depth - 1,
                                             driver=driver,
                                             locator=locator,
                                             dump_file=dump_file,
                                             id_category_default=id_category_default,
                                             category = new_category)
            try:
                dumped_dict:dict = j_loads(dump_file)
                category = {**dumped_dict, **category}
                j_dumps(category, dump_file)
            except Exception:
                ...
            
        j_dumps(category, dump_file)

    return category


def check_duplicate_url(dictionary, url) -> bool:
    """Check if the given URL already exists in the entire dictionary.

    @param dictionary: The hierarchical dictionary to check.
    @param url: The URL to check for duplicates.
    """
    for key, value in dictionary.items():
        if key == 'url' and value == url:
            print(f"Category URL '{url}' already exists.")
            return True
        for key, value in dictionary.get('children', {}).items():
            if key == 'url' and value == url:
                print(f"Category URL '{url}' already exists.")
                return True
            

    return


def compare_and_print_new_keys(current_dict, file_path):
    """ Сранвнение актуальных значений"""
    json_data = j_loads(file_path)

    # Пройти по всем ключам из файла JSON
    for key in json_data:
        # Если ключ уже существует в текущем словаре, пропустить его
        if key in current_dict:
            continue
        # Вывести ключ, если он не существует в текущем словаре
        print(key)



