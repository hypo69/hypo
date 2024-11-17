

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

import header
from src import gs
from src.logger import logger 
from src.utils import j_loads, j_dumps, pprint
from src.utils.string import StringFormatter
from src.endpoints.prestashop import PrestaShop
from src.endpoints.prestashop import PrestaCategory 


class Category(PrestaCategory):
    """ Класс категорий товара. Наследует `PrestaCategory` """

    credentials: dict = None

    def __init__(self, api_credentials, *args, **kwards):
        super().__init__(api_credentials, *args, **kwards)

    def get_parents(self, id_category, dept):
        """ Получение родительских категорий """
        return super().get_list_parent_categories(id_category)

    async def crawl_categories_async(self, url, depth, driver, locator, dump_file, id_category_default, category: dict = None):
        """ Асинхронная рекурсивная функция для обхода категорий и построения иерархического словаря.

        :param url: URL страницы для обхода.
        :param depth: Глубина рекурсии.
        :param driver: Экземпляр Selenium webdriver.
        :param locator: Xpath локатор для поиска ссылок на категории.
        :param dump_file: Файл для записи иерархического словаря.
        :param id_category_default: Идентификатор категории по умолчанию.
        :param category: Словарь, представляющий категорию, по умолчанию None.

        :return: Иерархический словарь, представляющий категории и их URL.
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
                task = self.crawl_categories_async(url=link_url,
                                                   depth=depth - 1,
                                                   driver=driver,
                                                   locator=locator,
                                                   dump_file=dump_file,
                                                   id_category_default=id_category_default,
                                                   category=new_category)
                tasks.append(task)

        # Ждем завершения всех задач
        await asyncio.gather(*tasks)

        return category

    def crawl_categories(self, url, depth: int, driver, locator: dict, dump_file: Path, id_category_default, category: dict = {}):
        """ Рекурсивная функция для обхода категорий с сайта и построения иерархического словаря.

        :param url: URL страницы для обхода.
        :param depth: Глубина рекурсии.
        :param driver: Экземпляр Selenium webdriver.
        :param locator: Xpath локатор для поиска ссылок на категории.
        :param dump_file: Файл для записи иерархического словаря.
        :param id_category_default: Идентификатор категории по умолчанию.
        :param category: Словарь, представляющий категорию, по умолчанию пустой словарь.

        :return: Иерархический словарь, представляющий категории и их URL.
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

                self.crawl_categories(url=link_url,
                                      depth=depth - 1,
                                      driver=driver,
                                      locator=locator,
                                      dump_file=dump_file,
                                      id_category_default=id_category_default,
                                      category=new_category)
                try:
                    dumped_dict: dict = j_loads(dump_file)
                    category = {**dumped_dict, **category}
                    j_dumps(category, dump_file)
                except Exception:
                    ...

        j_dumps(category, dump_file)

        return category


def check_duplicate_url(dictionary, url) -> bool:
    """ Проверка, существует ли данный URL в иерархическом словаре.

    :param dictionary: Иерархический словарь для проверки.
    :param url: URL для проверки на дубли.

    :return: True, если URL уже существует, иначе False.
    """
    for key, value in dictionary.items():
        if key == 'url' and value == url:
            print(f"Category URL '{url}' уже существует.")
            return True
        for key, value in dictionary.get('children', {}).items():
            if key == 'url' and value == url:
                print(f"Category URL '{url}' уже существует.")
                return True

    return False


def compare_and_print_new_keys(current_dict, file_path):
    """ Сравнение актуальных значений с теми, что в файле.

    :param current_dict: Текущий словарь для сравнения.
    :param file_path: Путь к файлу с данными для сравнения.

    Выводит ключи, которые отсутствуют в текущем словаре.
    """
    json_data = j_loads(file_path)

    # Пройти по всем ключам из файла JSON
    for key in json_data:
        # Если ключ уже существует в текущем словаре, пропустить его
        if key in current_dict:
            continue
        # Вывести ключ, если он не существует в текущем словаре
        print(key)
