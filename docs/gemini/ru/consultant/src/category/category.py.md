# Анализ кода модуля `category`

## Качество кода:

- **Соответствие стандартам**: 7/10
- **Плюсы**:
    - Код разбит на классы и функции, что способствует модульности.
    - Используются асинхронные операции для `crawl_categories_async`.
    - Присутствует базовая обработка ошибок с логированием.
    - Используются кастомные функции для JSON (`j_loads`, `j_dumps`).
- **Минусы**:
    - Неполная документация в формате RST.
    - Не везде используется асинхронность там, где это возможно.
    - Смешанный стиль кавычек (`'` и `"`).
    - В `crawl_categories` есть потенциальная проблема слияния данных и сохранения.
    - Переменная `id_category_default` в `crawl_categories` должна быть `default_category_id` (согласно docstring).
    - Не стандартизированны комментарии.
    - Функция `compare_and_print_missing_keys` не документированна и не имеет возврата.
    - В `crawl_categories_async` не добавляются дочерние элементы к category.

## Рекомендации по улучшению:

- Дополнить документацию в формате RST для всех функций, методов и классов.
- Использовать `j_loads_ns` там где не требуется строгая типизация (для  `dump_file`).
- Использовать консистентный стиль кавычек, перевести на `'` для кода.
- Стандартизировать комментарии, все комментарии после `#` должны быть на одном языке.
- В функции `crawl_categories` необходимо переписать логику записи в файл, чтобы она не перезаписывала а добавляла новые значения.
- Привести в соответствие docstring и названия переменных.
- Использовать асинхронные вызовы там, где это возможно, например `driver.get` -> `driver.get_async`.
- Добавить обработку ошибок с помощью `logger.error`, а не `Exception` в `compare_and_print_missing_keys` .
- В `crawl_categories_async` добавить добавление дочерних элементов к `category`

## Оптимизированный код:

```python
from __future__ import annotations
## \file /src/category/category.py
# -*- coding: utf-8 -*-
#! venv/bin/python/python3.12
"""
Модуль для работы с категориями, в основном для PrestaShop.
============================================================

Этот модуль предоставляет классы для взаимодействия и обработки данных категорий товаров,
особенно актуальных для PrestaShop.

:platform: Windows, Unix
:synopsis: Модуль для работы с категориями, в основном для PrestaShop.
"""

import asyncio
from pathlib import Path
import os
from typing import Dict
from lxml import html
import requests

import header #  исправить
from src import gs #  исправить
from src.logger.logger import logger
from src.utils.jjson import j_loads_ns, j_dumps #  изменил j_loads на j_loads_ns
from src.endpoints.prestashop.category import PrestaCategory, PrestaCategoryAsync


class Category(PrestaCategoryAsync):
    """
    Класс для работы с категориями товаров.
    Наследуется от PrestaCategoryAsync.
    """

    credentials: Dict = None

    def __init__(self, api_credentials, *args, **kwargs):
        """
        Инициализирует объект Category.

        :param api_credentials: API credentials для доступа к данным категории.
        :type api_credentials: Dict
        :param args: Variable length argument list (не используется).
        :type args: tuple
        :param kwargs: Keyword arguments (не используется).
        :type kwargs: dict
        """
        super().__init__(api_credentials, *args, **kwargs)


    async def crawl_categories_async(self, url: str, depth: int, driver, locator: str, dump_file: str, default_category_id: int, category: dict | None = None) -> dict:
        """
        Асинхронно обходит категории, строя иерархический словарь.

        :param url: URL страницы категории.
        :type url: str
        :param depth: Глубина рекурсии обхода.
        :type depth: int
        :param driver: Экземпляр Selenium WebDriver.
        :type driver:
        :param locator: XPath локатор для ссылок на категории.
        :type locator: str
        :param dump_file: Путь к JSON файлу для сохранения результатов.
        :type dump_file: str
        :param default_category_id: ID категории по умолчанию.
        :type default_category_id: int
        :param category: (Optional) Существующий словарь категории (default=None).
        :type category: dict | None
        :return: Обновленный или новый словарь категории.
        :rtype: dict
        :raises Exception: В случае ошибки при обходе категории.
        """
        if category is None:
            category = {
                'url': url,
                'name': '',
                'presta_categories': {
                    'default_category': default_category_id,
                    'additional_categories': []
                },
                'children': {}
            }

        if depth <= 0:
            return category

        try:
            await driver.get_async(url) #  используем асинхронный вызов
            await asyncio.sleep(1)  #  ждем загрузки страницы
            category_links = await driver.execute_locator_async(locator) # используем асинхронный вызов
            if not category_links:
                logger.error(f'Failed to locate category links on {url}')
                return category

            tasks = []
            for name, link_url in category_links: # перебираем ссылки
                if not self._is_duplicate_url(category, link_url): #  проверяем дубликат
                    new_category = {
                        'url': link_url,
                        'name': name,
                        'presta_categories': {
                            'default_category': default_category_id,
                            'additional_categories': []
                        },
                        'children': {}
                    }
                    tasks.append(self.crawl_categories_async(link_url, depth - 1, driver, locator, dump_file, default_category_id, new_category))
                    category['children'][name] = new_category # добавляем дочерний элемент

            await asyncio.gather(*tasks) # ждем выполнения всех задач

            return category
        except Exception as ex:
            logger.error(f'An error occurred during category crawling: {ex}')
            return category

    def crawl_categories(self, url: str, depth: int, driver, locator: str, dump_file: str, default_category_id: int, category: dict = {}) -> dict:
        """
        Рекурсивно обходит категории и строит иерархический словарь.

        :param url: URL страницы для обхода.
        :type url: str
        :param depth: Глубина рекурсии.
        :type depth: int
        :param driver: Экземпляр Selenium WebDriver.
        :type driver:
        :param locator: XPath локатор для поиска ссылок на категории.
        :type locator: str
        :param dump_file: Файл для сохранения иерархического словаря.
        :type dump_file: str
        :param default_category_id: ID категории по умолчанию.
        :type default_category_id: int
        :param category: Словарь категорий (по умолчанию пустой).
        :type category: dict
        :return: Иерархический словарь категорий и их URL.
        :rtype: dict
         :raises Exception: В случае ошибки при обходе категории.
        """
        if depth <= 0:
            return category

        try:
            driver.get(url)
            driver.wait(1)  #  ждем загрузки страницы
            category_links = driver.execute_locator(locator)
            if not category_links:
                logger.error(f'Failed to locate category links on {url}')
                return category

            for name, link_url in category_links:
                if self._is_duplicate_url(category, link_url):
                    continue
                new_category = {
                    'url': link_url,
                    'name': name,
                    'presta_categories': {
                        'default_category': default_category_id,
                        'additional_categories': []
                    },
                     'children': {}
                }
                category[name] = new_category # добавляем дочерний элемент
                self.crawl_categories(link_url, depth - 1, driver, locator, dump_file, default_category_id, new_category)
            #  используем j_loads и j_dumps для безопасной обработки JSON
            loaded_data = j_loads_ns(dump_file) #  используем j_loads_ns
            if loaded_data: # если файл не пустой
                 category = {**loaded_data, **category} # соединяем данные
            j_dumps(category, dump_file) # сохраняем данные
            return category
        except Exception as ex:
            logger.error(f'An error occurred during category crawling: {ex}')
            return category

    def _is_duplicate_url(self, category: dict, url: str) -> bool:
        """
        Проверяет, существует ли URL уже в словаре категорий.

        :param category: Словарь категорий.
        :type category: dict
        :param url: URL для проверки.
        :type url: str
        :return: True, если URL является дубликатом, False в противном случае.
        :rtype: bool
        """
        return url in (item['url'] for item in category.values())


def compare_and_print_missing_keys(current_dict: dict, file_path: str) -> None:
    """
    Сравнивает текущий словарь с данными в файле и выводит недостающие ключи.

    :param current_dict: Текущий словарь для сравнения.
    :type current_dict: dict
    :param file_path: Путь к файлу для загрузки данных.
    :type file_path: str
    """
    try:
        data_from_file = j_loads_ns(file_path) #  используем j_loads_ns
    except Exception as ex:
        logger.error(f'Error loading data from file: {ex}') #  логируем ошибку
        return

    if not isinstance(data_from_file, dict):
        logger.error(f'Data from file is not a dict') #  логируем ошибку
        return # если данные из файла не словарь

    for key in data_from_file:
        if key not in current_dict:
            print(key)
```