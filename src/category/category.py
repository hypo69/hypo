## \file hypotez/src/category/category.py
# -*- coding: utf-8 -*-\
#! venv/Scripts/python.exe
#! venv/bin/python/python3.12

"""
.. module: src.category 
	:platform: Windows, Unix
	:synopsis: Module for working with categories, primarily for PrestaShop.

"""

import asyncio
from pathlib import Path
import os
from typing import Dict
from lxml import html
import requests

import header
from src import gs
from src.logger import logger
from src.utils import j_loads, j_dumps
from src.utils.string import StringFormatter
from src.endpoints.prestashop import PrestaShop, PrestaCategory


## \file hypotez/src/category/category.py
# -*- coding: utf-8 -*-
"""
Module for working with categories, primarily for PrestaShop.
============================================================

This module provides classes for interacting with and
processing product category data, particularly relevant for PrestaShop.
"""

import asyncio
from pathlib import Path
import os
from typing import Dict
from lxml import html
import requests

import header
from src import gs
from src.logger import logger
from src.utils import j_loads, j_dumps
from src.utils.string import StringFormatter
from src.endpoints.prestashop import PrestaShop, PrestaCategory


class Category(PrestaCategory):
    """Category handler for product categories. Inherits from PrestaCategory."""
    credentials: Dict = None

    def __init__(self, api_credentials, *args, **kwargs):
        """Initializes a Category object.

        :param api_credentials: API credentials for accessing the category data.
        :param args: Variable length argument list (unused).
        :param kwargs: Keyword arguments (unused).
        """
        super().__init__(api_credentials, *args, **kwargs)

    def get_parents(self, id_category, dept):
        """Retrieves a list of parent categories.

        :param id_category: The ID of the category to retrieve parents for.
        :param dept: Depth level of the category.
        :returns: A list of parent categories.
        """
        return super().get_list_parent_categories(id_category)

    async def crawl_categories_async(self, url, depth, driver, locator, dump_file, default_category_id, category=None):
        """Asynchronously crawls categories, building a hierarchical dictionary.

        :param url: The URL of the category page.
        :param depth: The depth of the crawling recursion.
        :param driver: The Selenium WebDriver instance.
        :param locator: The XPath locator for category links.
        :param dump_file: The path to the JSON file for saving results.
        :param default_category_id: The default category ID.
        :param category: (Optional) An existing category dictionary (default=None).
        :returns: The updated or new category dictionary.
        """

        if category is None:
            category = {
                'url': url,
                'name': '',
                'presta_categories': {
                    'default_category': id_category_default,
                    'additional_categories': []
                },
                'children': {}
            }

        if depth <= 0:
            return category

        try:
            driver.get(url)
            await asyncio.sleep(1)  # Wait for page load
            category_links = driver.execute_locator(locator)
            if not category_links:
                logger.error(f"Failed to locate category links on {url}")
                return category

            tasks = [
                self.crawl_categories_async(link_url, depth - 1, driver, locator, dump_file, id_category_default, new_category)
                for name, link_url in category_links
                if not self._is_duplicate_url(category, link_url)
                for new_category in [{'url': link_url, 'name': name, 'presta_categories': {'default_category': id_category_default, 'additional_categories': []}, 'children': {}}]
            ]
            await asyncio.gather(*tasks)

            return category
        except Exception as ex:
            logger.error(f"An error occurred during category crawling: ",ex)
            return category

    def crawl_categories(self, url, depth, driver, locator, dump_file, id_category_default, category={}):
        """
        Crawls categories recursively and builds a hierarchical dictionary.

        :param url: URL of the page to crawl.
        :param depth: Depth of recursion.
        :param driver: Selenium WebDriver instance.
        :param locator: XPath locator for finding category links.
        :param dump_file: File for saving the hierarchical dictionary.
        :param id_category_default: Default category ID.
        :param category: Category dictionary (default is empty).
        :return: Hierarchical dictionary of categories and their URLs.
        """
        if depth <= 0:
            return category

        try:
            driver.get(url)
            driver.wait(1)  # Wait for page load
            category_links = driver.execute_locator(locator)
            if not category_links:
                logger.error(f"Failed to locate category links on {url}")
                return category

            for name, link_url in category_links:
                if self._is_duplicate_url(category, link_url):
                    continue
                new_category = {
                    'url': link_url,
                    'name': name,
                    'presta_categories': {
                        'default_category': id_category_default,
                        'additional_categories': []
                    }
                }
                category[name] = new_category
                self.crawl_categories(link_url, depth - 1, driver, locator, dump_file, id_category_default, new_category)
            # Using j_loads and j_dumps for safe JSON handling
            loaded_data = j_loads(dump_file)
            category = {**loaded_data, **category}
            j_dumps(category, dump_file)
            return category
        except Exception as ex:
            logger.error(f"An error occurred during category crawling: ",ex)
            return category

    def _is_duplicate_url(self, category, url):
        """
        Checks if a URL already exists in the category dictionary.

        :param category: Category dictionary.
        :param url: URL to check.
        :return: True if the URL is a duplicate, False otherwise.
        """
        return url in (item['url'] for item in category.values())


def compare_and_print_missing_keys(current_dict, file_path):
    """
    Compares current dictionary with data in a file and prints missing keys.
    """
    try:
        data_from_file = j_loads(file_path)
    except Exception as ex:
        logger.error(f"Error loading data from file: ",ex)
        return  # Or raise the exception


    for key in data_from_file:
        if key not in current_dict:
            print(key)



























# """
# .. module: src.category 
# 	:platform: Windows, Unix
# 	:synopsis: Модуль работы с категориями 
# На сегодняшний день модуль заточен в основном под Престашоп

# """
# MODE = 'dev'

# from pathlib import Path
# import os
# import asyncio
# from typing import List, Dict
# from lxml import html
# import requests

# import header
# from src import gs
# from src.logger import logger 
# from src.utils import j_loads, j_dumps, pprint
# from src.utils.string import StringFormatter
# from src.endpoints.prestashop import PrestaShop
# from src.endpoints.prestashop import PrestaCategory 


# class Category(PrestaCategory):
#     """ Класс категорий товара. Наследует `PrestaCategory` """

#     credentials: dict = None

#     def __init__(self, api_credentials, *args, **kwards):
#         super().__init__(api_credentials, *args, **kwards)

#     def get_parents(self, id_category, dept):
#         """ Получение родительских категорий """
#         return super().get_list_parent_categories(id_category)

#     async def crawl_categories_async(self, url, depth, driver, locator, dump_file, id_category_default, category: dict = None):
#         """ Асинхронная рекурсивная функция для обхода категорий и построения иерархического словаря.

#         :param url: URL страницы для обхода.
#         :param depth: Глубина рекурсии.
#         :param driver: Экземпляр Selenium webdriver.
#         :param locator: Xpath локатор для поиска ссылок на категории.
#         :param dump_file: Файл для записи иерархического словаря.
#         :param id_category_default: Идентификатор категории по умолчанию.
#         :param category: Словарь, представляющий категорию, по умолчанию None.

#         :return: Иерархический словарь, представляющий категории и их URL.
#         """
#         if category is None:
#             category = {'url': url,
#                         'name': '',
#                         "presta_categories": {
#                             "default_category": id_category_default,
#                             "additional_categories": []
#                         },
#                         'children': {}}

#         if depth <= 0:
#             return category

#         driver.get(url)
#         driver.wait(1)
#         category_links = driver.execute_locator(locator)
#         if not category_links:
#             logger.error(f"Что-то упало")
#             ...
#             return category

#         tasks = []
#         for link in category_links:
#             for name, link_url in link.items():
#                 if check_duplicate_url(category, link_url):
#                     continue
#                 new_category = {'url': link_url,
#                                 'name': name,
#                                 "presta_categories": {
#                                     "default_category": id_category_default,
#                                     "additional_categories": []
#                                 },
#                                 'children': {}}
#                 task = self.crawl_categories_async(url=link_url,
#                                                    depth=depth - 1,
#                                                    driver=driver,
#                                                    locator=locator,
#                                                    dump_file=dump_file,
#                                                    id_category_default=id_category_default,
#                                                    category=new_category)
#                 tasks.append(task)

#         # Ждем завершения всех задач
#         await asyncio.gather(*tasks)

#         return category

#     def crawl_categories(self, url, depth: int, driver, locator: dict, dump_file: Path, id_category_default, category: dict = {}):
#         """ Рекурсивная функция для обхода категорий с сайта и построения иерархического словаря.

#         :param url: URL страницы для обхода.
#         :param depth: Глубина рекурсии.
#         :param driver: Экземпляр Selenium webdriver.
#         :param locator: Xpath локатор для поиска ссылок на категории.
#         :param dump_file: Файл для записи иерархического словаря.
#         :param id_category_default: Идентификатор категории по умолчанию.
#         :param category: Словарь, представляющий категорию, по умолчанию пустой словарь.

#         :return: Иерархический словарь, представляющий категории и их URL.
#         """
#         if depth <= 0:
#             return category

#         driver.get(url)
#         driver.wait(1)
#         category_links = driver.execute_locator(locator)
#         if not category_links:
#             ...
#             return category

#         for link in category_links:
#             for name, link_url in link.items():
#                 if check_duplicate_url(category, link_url):
#                     continue
#                 new_category = {
#                     'url': link_url,
#                     'name': name,
#                     'presta_categories': {
#                         "default_category": id_category_default,
#                         "additional_categories": []
#                     }
#                 }
#                 category[name] = new_category

#                 self.crawl_categories(url=link_url,
#                                       depth=depth - 1,
#                                       driver=driver,
#                                       locator=locator,
#                                       dump_file=dump_file,
#                                       id_category_default=id_category_default,
#                                       category=new_category)
#                 try:
#                     dumped_dict: dict = j_loads(dump_file)
#                     category = {**dumped_dict, **category}
#                     j_dumps(category, dump_file)
#                 except Exception:
#                     ...

#         j_dumps(category, dump_file)

#         return category


# def check_duplicate_url(dictionary, url) -> bool:
#     """ Проверка, существует ли данный URL в иерархическом словаре.

#     :param dictionary: Иерархический словарь для проверки.
#     :param url: URL для проверки на дубли.

#     :return: True, если URL уже существует, иначе False.
#     """
#     for key, value in dictionary.items():
#         if key == 'url' and value == url:
#             print(f"Category URL '{url}' уже существует.")
#             return True
#         for key, value in dictionary.get('children', {}).items():
#             if key == 'url' and value == url:
#                 print(f"Category URL '{url}' уже существует.")
#                 return True

#     return False


# def compare_and_print_missing_keys(current_dict, file_path):
#     """ Сравнение актуальных значений с теми, что в файле.

#     :param current_dict: Текущий словарь для сравнения.
#     :param file_path: Путь к файлу с данными для сравнения.

#     Выводит ключи, которые отсутствуют в текущем словаре.
#     """
#     json_data = j_loads(file_path)

#     # Пройти по всем ключам из файла JSON
#     for key in json_data:
#         # Если ключ уже существует в текущем словаре, пропустить его
#         if key in current_dict:
#             continue
#         # Вывести ключ, если он не существует в текущем словаре
#         print(key)
