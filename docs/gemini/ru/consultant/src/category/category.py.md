# Анализ кода модуля `category`

**Качество кода**
6
-  Плюсы
    -  Используется reStructuredText для docstring.
    -  Присутствует логирование ошибок через `logger.error`.
    -  Используется `j_loads` и `j_dumps` для работы с JSON.
    -  Код разбит на функции, что улучшает читаемость.
-  Минусы
    -  Не все комментарии соответствуют reStructuredText.
    -  Используется стандартный `try-except` без необходимости в некоторых местах.
    -  Не хватает проверки типов и валидации входных данных.
    -  Не везде соблюдается DRY (Don't Repeat Yourself) принцип.
    -  Не все импорты соответствуют ранее обработанным файлам.
    -  Использование `asyncio.sleep(1)` может быть нестабильным; лучше использовать явные ожидания Selenium.
    -   Не везде используется форматирование строк f-strings, где это уместно.
    -   Метод `compare_and_print_missing_keys` не имеет документации в формате RST
    -   В `crawl_categories` метод идет перезапись данных файла `dump_file`, что может привести к потере данных.

**Рекомендации по улучшению**

1.  **Документация**:
    -   Переписать все docstring в reStructuredText.
    -   Добавить docstring для функции `compare_and_print_missing_keys`.
    -   Переписать комментарии в стиле reStructuredText.

2.  **Импорты**:
    -   Проверить и добавить недостающие импорты, если они есть.
    -   Удалить неиспользуемые импорты.
    -   Привести импорты в соответствие с другими файлами.

3.  **Обработка ошибок**:
    -   Удалить избыточное использование `try-except` блоков, где это не нужно.
    -   Использовать `logger.error` для обработки ошибок в функциях.
    -   Добавить более конкретные сообщения об ошибках в `logger.error`.

4.  **Рефакторинг**:
    -   Избегать дублирования кода в методах `crawl_categories_async` и `crawl_categories`, по возможности вынести общую логику в отдельный метод.
    -   Улучшить читаемость кода.
    -  Добавить проверки типов.
    -   Избегать перезаписи файла в методе `crawl_categories` при каждой итерации.
5. **Асинхронность**:
    -   В `crawl_categories_async` при `await asyncio.sleep(1)` лучше использовать `driver.wait` из selenium.

**Оптимизированный код**

```python
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe
#! venv/bin/python/python3.12
"""
Модуль для работы с категориями, в основном для PrestaShop.
============================================================

Этот модуль предоставляет классы для взаимодействия и обработки данных о категориях товаров,
особенно актуальных для PrestaShop.

.. module:: src.category
   :platform: Windows, Unix
   :synopsis: Модуль для работы с категориями, в основном для PrestaShop.
"""

import asyncio
import os
from pathlib import Path
from typing import Dict, List, Any, Tuple

from lxml import html
import requests

from src import gs
from src.logger.logger import logger
from src.utils.jjson import j_loads, j_dumps
from src.endpoints.prestashop import PrestaShop, PrestaCategory
from src.header import header
from selenium.webdriver.remote.webdriver import WebDriver  # добавленный импорт для аннотации типов


class Category(PrestaCategory):
    """
    Класс для обработки категорий продуктов. Наследуется от PrestaCategory.

    :ivar credentials: Словарь с учетными данными API.
    :vartype credentials: Dict
    """
    credentials: Dict = None

    def __init__(self, api_credentials: Dict, *args, **kwargs) -> None:
        """
        Инициализирует объект Category.

        :param api_credentials: Учетные данные API для доступа к данным категории.
        :type api_credentials: Dict
        :param args: Список позиционных аргументов (не используется).
        :type args: tuple
        :param kwargs: Словарь именованных аргументов (не используется).
        :type kwargs: dict
        """
        super().__init__(api_credentials, *args, **kwargs)

    def get_parents(self, id_category: int, dept: int) -> List:
        """
        Извлекает список родительских категорий.

        :param id_category: ID категории, для которой нужно извлечь родителей.
        :type id_category: int
        :param dept: Уровень глубины категории.
        :type dept: int
        :return: Список родительских категорий.
        :rtype: List
        """
        return super().get_list_parent_categories(id_category)

    async def crawl_categories_async(self, url: str, depth: int, driver: WebDriver, locator: str, dump_file: str,
                                     default_category_id: int, category: Dict = None) -> Dict:
        """
        Асинхронно сканирует категории, строя иерархический словарь.

        :param url: URL страницы категории.
        :type url: str
        :param depth: Глубина рекурсии сканирования.
        :type depth: int
        :param driver: Экземпляр Selenium WebDriver.
        :type driver: WebDriver
        :param locator: XPath локатор для ссылок на категории.
        :type locator: str
        :param dump_file: Путь к JSON-файлу для сохранения результатов.
        :type dump_file: str
        :param default_category_id: ID категории по умолчанию.
        :type default_category_id: int
        :param category: (Опционально) Существующий словарь категорий (по умолчанию None).
        :type category: Dict, optional
        :return: Обновленный или новый словарь категорий.
        :rtype: Dict
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
            driver.get(url)
            driver.wait(1)  # Используем wait вместо asyncio.sleep для стабильности
            category_links = driver.execute_locator(locator)
            if not category_links:
                logger.error(f"Не удалось найти ссылки на категории по адресу {url}")
                return category

            tasks = [
                self._crawl_category_async(link_url, depth - 1, driver, locator, dump_file, default_category_id, new_category)
                for name, link_url in category_links
                if not self._is_duplicate_url(category, link_url)
                for new_category in [{'url': link_url, 'name': name, 'presta_categories': {'default_category': default_category_id, 'additional_categories': []}, 'children': {}}]
            ]
            await asyncio.gather(*tasks)

            return category
        except Exception as ex:
            logger.error(f"Произошла ошибка во время сканирования категорий: {ex}", exc_info=True)
            return category

    async def _crawl_category_async(self, url: str, depth: int, driver: WebDriver, locator: str, dump_file: str,
                                     default_category_id: int, category: Dict) -> Dict:
        """
        Внутренняя асинхронная функция для рекурсивного сканирования категорий.
        
        :param url: URL страницы категории.
        :type url: str
        :param depth: Глубина рекурсии сканирования.
        :type depth: int
        :param driver: Экземпляр Selenium WebDriver.
        :type driver: WebDriver
        :param locator: XPath локатор для ссылок на категории.
        :type locator: str
        :param dump_file: Путь к JSON-файлу для сохранения результатов.
        :type dump_file: str
        :param default_category_id: ID категории по умолчанию.
        :type default_category_id: int
        :param category: Существующий словарь категорий.
        :type category: Dict
        :return: Обновленный или новый словарь категорий.
        :rtype: Dict
        """
        if depth <= 0:
            return category

        try:
             driver.get(url)
             driver.wait(1)
             category_links = driver.execute_locator(locator)
             if not category_links:
                logger.error(f"Не удалось найти ссылки на категории по адресу {url}")
                return category
             
             tasks = [
                 self._crawl_category_async(link_url, depth - 1, driver, locator, dump_file, default_category_id, new_category)
                 for name, link_url in category_links
                 if not self._is_duplicate_url(category, link_url)
                 for new_category in [{'url': link_url, 'name': name, 'presta_categories': {'default_category': default_category_id, 'additional_categories': []}, 'children': {}}]
             ]
             await asyncio.gather(*tasks)
             return category
        except Exception as ex:
            logger.error(f"Произошла ошибка во время сканирования категории: {ex}", exc_info=True)
            return category

    def crawl_categories(self, url: str, depth: int, driver: WebDriver, locator: str, dump_file: str,
                         id_category_default: int, category: Dict = None) -> Dict:
        """
        Рекурсивно сканирует категории и строит иерархический словарь.

        :param url: URL страницы для сканирования.
        :type url: str
        :param depth: Глубина рекурсии.
        :type depth: int
        :param driver: Экземпляр Selenium WebDriver.
        :type driver: WebDriver
        :param locator: XPath локатор для поиска ссылок на категории.
        :type locator: str
        :param dump_file: Файл для сохранения иерархического словаря.
        :type dump_file: str
        :param id_category_default: ID категории по умолчанию.
        :type id_category_default: int
        :param category: Словарь категорий (по умолчанию пустой).
        :type category: Dict, optional
        :return: Иерархический словарь категорий и их URL.
        :rtype: Dict
        """
        if category is None:
            category = {}
        
        if depth <= 0:
            return category

        try:
            driver.get(url)
            driver.wait(1)
            category_links = driver.execute_locator(locator)
            if not category_links:
                logger.error(f"Не удалось найти ссылки на категории по адресу {url}")
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
                    },
                    'children': {}
                }
                category[name] = new_category
                self.crawl_categories(link_url, depth - 1, driver, locator, dump_file, id_category_default, new_category)
            
            # Загружаем данные из файла только один раз в начале
            loaded_data = j_loads(dump_file) if os.path.exists(dump_file) else {}
            # Объединяем загруженные данные с текущими, чтобы не перезаписать предыдущие
            category = {**loaded_data, **category}
            # Сохраняем все данные в конце
            j_dumps(category, dump_file)

            return category
        except Exception as ex:
            logger.error(f"Произошла ошибка во время сканирования категорий: {ex}", exc_info=True)
            return category

    def _is_duplicate_url(self, category: Dict, url: str) -> bool:
        """
        Проверяет, существует ли URL уже в словаре категорий.

        :param category: Словарь категорий.
        :type category: Dict
        :param url: URL для проверки.
        :type url: str
        :return: True, если URL дубликат, иначе False.
        :rtype: bool
        """
        return any(item['url'] == url for item in category.values())


def compare_and_print_missing_keys(current_dict: Dict, file_path: str) -> None:
    """
    Сравнивает текущий словарь с данными в файле и выводит отсутствующие ключи.

    :param current_dict: Текущий словарь для сравнения.
    :type current_dict: Dict
    :param file_path: Путь к файлу для загрузки данных.
    :type file_path: str
    """
    try:
        data_from_file = j_loads(file_path)
    except Exception as ex:
        logger.error(f"Ошибка при загрузке данных из файла: {ex}", exc_info=True)
        return

    for key in data_from_file:
        if key not in current_dict:
            print(key)