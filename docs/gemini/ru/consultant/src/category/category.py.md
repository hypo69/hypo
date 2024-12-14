# Анализ кода модуля category

**Качество кода**
8
-  Плюсы
    - Код хорошо структурирован и использует классы для организации функциональности.
    - Присутствует обработка исключений, что повышает надежность кода.
    - Используются асинхронные операции для повышения производительности.
    - Код соответствует PEP 8 и содержит docstrings для функций и классов.
    - Применяются кастомные функции `j_loads` и `j_dumps` для безопасной обработки JSON.
-  Минусы
    -  Смешение стилей обработки ошибок: где-то `try-except`, где-то логирование и возврат.
    -  В `crawl_categories` и `crawl_categories_async` присутствует дублирование логики.
    -  Использование `driver.wait(1)` вместо `asyncio.sleep(1)` в `crawl_categories`.
    -  Не полное использование возможностей `logger` (например, `debug`).
    -  В функции `_is_duplicate_url` используется генератор, который можно упростить.

**Рекомендации по улучшению**
1.  **Унификация обработки ошибок**: Следует использовать `logger.error` и возвращать значения или прерывать выполнение, но не смешивать `try-except` и `logger.error`.
2.  **Рефакторинг дублирования кода**: Необходимо вынести общую логику из `crawl_categories` и `crawl_categories_async` в отдельную функцию, чтобы избежать дублирования кода.
3.  **Унификация задержек**: Следует использовать `asyncio.sleep(1)` везде, где нужно ожидание.
4.  **Улучшение логирования**: Добавить больше `logger.debug` для отладки, чтобы отслеживать состояние программы.
5.  **Упрощение генератора**: В функции `_is_duplicate_url` заменить генератор на `any(url == item['url'] for item in category.values())` для улучшения читаемости.
6. **Улучшение форматирования**: форматировать код согласно pep8, избавиться от импортов не относящихся к логике модуля (например `header`).

**Оптимизированный код**
```python
# -*- coding: utf-8 -*-
"""
Модуль для работы с категориями, особенно для PrestaShop.
============================================================

Этот модуль предоставляет классы для взаимодействия и
обработки данных категорий товаров, что особенно актуально для PrestaShop.

:platform: Windows, Unix
:synopsis: Модуль для работы с категориями, особенно для PrestaShop.
"""
import asyncio
import os
from typing import Dict, List, Tuple, Any
from lxml import html
import requests

from src import gs
from src.logger.logger import logger
from src.utils.jjson import j_loads, j_dumps
from src.endpoints.prestashop import PrestaShop, PrestaCategory


class Category(PrestaCategory):
    """
    Обработчик категорий товаров. Наследует от PrestaCategory.

    :param api_credentials: API credentials for accessing the category data.
    :type api_credentials: Dict
    :param args: Variable length argument list (unused).
    :type args: tuple
    :param kwargs: Keyword arguments (unused).
    :type kwargs: Dict
    """
    credentials: Dict = None

    def __init__(self, api_credentials, *args, **kwargs):
        """
        Инициализирует объект Category.
        """
        super().__init__(api_credentials, *args, **kwargs)

    def get_parents(self, id_category: int, dept: int) -> List[Dict]:
        """
        Возвращает список родительских категорий.

        :param id_category: ID категории, для которой нужно получить родителей.
        :type id_category: int
        :param dept: Уровень вложенности категории (не используется).
        :type dept: int
        :return: Список родительских категорий.
        :rtype: List[Dict]
        """
        return super().get_list_parent_categories(id_category)

    async def _crawl_category(self, url: str, depth: int, driver, locator: str,
                             dump_file: str, default_category_id: int,
                             category: Dict = None) -> Dict:
        """
        Асинхронно обходит категории, строя иерархический словарь.

        :param url: URL страницы категории.
        :type url: str
        :param depth: Глубина рекурсии обхода.
        :type depth: int
        :param driver: Экземпляр Selenium WebDriver.
        :type driver: Any
        :param locator: XPath локатор для ссылок категорий.
        :type locator: str
        :param dump_file: Путь к JSON файлу для сохранения результатов.
        :type dump_file: str
        :param default_category_id: ID категории по умолчанию.
        :type default_category_id: int
        :param category: (Optional) Существующий словарь категории (по умолчанию=None).
        :type category: Dict
        :return: Обновленный или новый словарь категории.
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
            await asyncio.sleep(1)  # Ожидание загрузки страницы
            category_links = driver.execute_locator(locator)
            if not category_links:
                logger.error(f"Не удалось найти ссылки на категории на {url}")
                return category

            tasks = []
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
                tasks.append(
                    self._crawl_category(link_url, depth - 1, driver, locator,
                                         dump_file, default_category_id, new_category)
                )
            await asyncio.gather(*tasks)
            return category
        except Exception as ex:
            logger.error(f"Произошла ошибка при обходе категорий: {ex}", exc_info=True)
            return category

    async def crawl_categories_async(self, url: str, depth: int, driver,
                                     locator: str, dump_file: str,
                                     default_category_id: int,
                                     category: Dict = None) -> Dict:
        """
        Асинхронно обходит категории, строя иерархический словарь.

        :param url: URL страницы категории.
        :type url: str
        :param depth: Глубина рекурсии обхода.
        :type depth: int
        :param driver: Экземпляр Selenium WebDriver.
        :type driver: Any
        :param locator: XPath локатор для ссылок категорий.
        :type locator: str
        :param dump_file: Путь к JSON файлу для сохранения результатов.
        :type dump_file: str
        :param default_category_id: ID категории по умолчанию.
        :type default_category_id: int
        :param category: (Optional) Существующий словарь категории (по умолчанию=None).
        :type category: Dict
        :return: Обновленный или новый словарь категории.
        :rtype: Dict
        """
        return await self._crawl_category(url, depth, driver, locator, dump_file, default_category_id, category)

    def crawl_categories(self, url: str, depth: int, driver, locator: str,
                         dump_file: str, default_category_id: int,
                         category: Dict = None) -> Dict:
        """
        Рекурсивно обходит категории и строит иерархический словарь.

        :param url: URL страницы для обхода.
        :type url: str
        :param depth: Глубина рекурсии.
        :type depth: int
        :param driver: Экземпляр Selenium WebDriver.
        :type driver: Any
        :param locator: XPath локатор для поиска ссылок категорий.
        :type locator: str
        :param dump_file: Файл для сохранения иерархического словаря.
        :type dump_file: str
        :param default_category_id: ID категории по умолчанию.
        :type default_category_id: int
        :param category: Словарь категории (по умолчанию пустой).
        :type category: Dict
        :return: Иерархический словарь категорий и их URL.
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
            driver.wait(1)  # Ожидание загрузки страницы
            category_links = driver.execute_locator(locator)
            if not category_links:
                logger.error(f"Не удалось найти ссылки на категории на {url}")
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
                     'children':{}
                }

                category['children'][name] = new_category
                self.crawl_categories(link_url, depth - 1, driver, locator, dump_file, default_category_id, new_category)

            loaded_data = j_loads(dump_file)
            if loaded_data:
                category = {**loaded_data, **category}
            j_dumps(category, dump_file)

            return category
        except Exception as ex:
            logger.error(f"Произошла ошибка при обходе категорий: {ex}", exc_info=True)
            return category

    def _is_duplicate_url(self, category: Dict, url: str) -> bool:
        """
        Проверяет, существует ли URL уже в словаре категории.

        :param category: Словарь категории.
        :type category: Dict
        :param url: URL для проверки.
        :type url: str
        :return: True, если URL дубликат, иначе False.
        :rtype: bool
        """
        return any(url == item['url'] for item in category.values())


def compare_and_print_missing_keys(current_dict: Dict, file_path: str):
    """
    Сравнивает текущий словарь с данными из файла и выводит недостающие ключи.

    :param current_dict: Текущий словарь для сравнения.
    :type current_dict: Dict
    :param file_path: Путь к файлу с данными для сравнения.
    :type file_path: str
    """
    try:
        data_from_file = j_loads(file_path)
    except Exception as ex:
        logger.error(f"Ошибка при загрузке данных из файла: {ex}", exc_info=True)
        return  # Или выбросить исключение

    for key in data_from_file:
        if key not in current_dict:
            print(key)