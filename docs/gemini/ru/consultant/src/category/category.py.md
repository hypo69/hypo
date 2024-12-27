# Анализ кода модуля `category`

**Качество кода**
9
- Плюсы
    - Код хорошо структурирован и разделен на классы и методы.
    - Используется асинхронность для `crawl_categories_async`.
    - Присутствует логирование ошибок.
    - Использование `j_loads` и `j_dumps` для обработки JSON.
    - Есть docstring для классов и методов.
 - Минусы
    - В некоторых местах документация неполная и не соответствует reStructuredText (RST).
    -  Метод `crawl_categories` перезаписывает файл на каждом вызове.
    -  Метод `compare_and_print_missing_keys` выводит результат в консоль, что не соответствует общей логике логирования.

**Рекомендации по улучшению**

1. **Документация**:
   - Улучшить docstring, привести к стандарту reStructuredText.
   - Добавить описание параметров и возвращаемых значений для всех функций и методов.
   - Заменить простые комментарии `#` на комментарии в формате RST.

2. **Обработка JSON**:
   - Устранить дублирование записи в файл в `crawl_categories`.

3. **Логирование**:
   - Избегать вывода в консоль в `compare_and_print_missing_keys`, использовать `logger.info` для отчета о найденных ключах.

4. **Структура кода**:
   - Упростить логику проверки дубликатов URL, сделав её более читаемой.

5. **Импорты**:
   -  Упорядочить импорты по алфавиту и группам.
    - Удалить неиспользуемый импорт `header`

6. **Асинхронность**:
   - Сделать метод `crawl_categories` асинхронным, для согласованности.
   - Использовать `asyncio.sleep` вместо `driver.wait` для асинхронных задач.

**Оптимизированный код**

```python
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe
#! venv/bin/python/python3.12
"""
Модуль для работы с категориями, в основном для PrestaShop.
============================================================

Этот модуль предоставляет классы для взаимодействия и обработки данных
категорий продуктов, особенно актуальных для PrestaShop.

.. module:: src.category
   :platform: Windows, Unix
   :synopsis: Module for working with categories, primarily for PrestaShop.
"""

import asyncio
import os
from pathlib import Path
from typing import Any, Dict, List, Tuple

import requests
from lxml import html

# from header import header # Удален неиспользуемый импорт
from src import gs
from src.endpoints.prestashop import PrestaCategory
from src.logger.logger import logger
from src.utils.jjson import j_dumps, j_loads


class Category(PrestaCategory):
    """
    Класс для обработки категорий продуктов.
    Наследует от :class:`PrestaCategory`.
    """
    credentials: Dict = None

    def __init__(self, api_credentials, *args, **kwargs):
        """
        Инициализирует объект Category.

        :param api_credentials: Учетные данные API для доступа к данным категории.
        :type api_credentials: Dict
        :param args: Переменное количество аргументов.
        :type args: tuple
        :param kwargs: Переменное количество именованных аргументов.
        :type kwargs: dict
        """
        super().__init__(api_credentials, *args, **kwargs)

    def get_parents(self, id_category: int, dept: int) -> List[Dict[str, Any]]:
        """
        Извлекает список родительских категорий.

        :param id_category: Идентификатор категории, для которой нужно получить родителей.
        :type id_category: int
        :param dept: Глубина уровня категории (не используется).
        :type dept: int
        :return: Список родительских категорий.
        :rtype: List[Dict[str, Any]]
        """
        return super().get_list_parent_categories(id_category)

    async def crawl_categories_async(self, url: str, depth: int, driver: Any, locator: str, dump_file: str, default_category_id: int, category: Dict = None) -> Dict:
        """
        Асинхронно сканирует категории, создавая иерархический словарь.

        :param url: URL страницы категории.
        :type url: str
        :param depth: Глубина рекурсии сканирования.
        :type depth: int
        :param driver: Экземпляр Selenium WebDriver.
        :type driver: Any
        :param locator: XPath локатор для ссылок на категории.
        :type locator: str
        :param dump_file: Путь к JSON файлу для сохранения результатов.
        :type dump_file: str
        :param default_category_id: Идентификатор категории по умолчанию.
        :type default_category_id: int
        :param category: (Опционально) Существующий словарь категорий.
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
            await asyncio.sleep(1)  # Ожидание загрузки страницы.
            category_links = driver.execute_locator(locator)
            if not category_links:
                logger.error(f"Не удалось найти ссылки на категории по адресу: {url}")
                return category

            tasks = [
                self.crawl_categories_async(link_url, depth - 1, driver, locator, dump_file, default_category_id, new_category)
                for name, link_url in category_links
                if not self._is_duplicate_url(category, link_url)
                for new_category in [{'url': link_url, 'name': name, 'presta_categories': {'default_category': default_category_id, 'additional_categories': []}, 'children': {}}]
            ]
            await asyncio.gather(*tasks)

            return category
        except Exception as ex:
            logger.error(f"Произошла ошибка при сканировании категорий: ", ex)
            return category

    async def crawl_categories(self, url: str, depth: int, driver: Any, locator: str, dump_file: str, default_category_id: int, category: Dict = None) -> Dict:
        """
        Рекурсивно сканирует категории и строит иерархический словарь.

        :param url: URL страницы для сканирования.
        :type url: str
        :param depth: Глубина рекурсии.
        :type depth: int
        :param driver: Экземпляр Selenium WebDriver.
        :type driver: Any
        :param locator: XPath локатор для поиска ссылок на категории.
        :type locator: str
        :param dump_file: Файл для сохранения иерархического словаря.
        :type dump_file: str
        :param default_category_id: Идентификатор категории по умолчанию.
        :type default_category_id: int
         :param category: (Опционально) Словарь категорий.
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
            await asyncio.sleep(1)  # Ожидание загрузки страницы.
            category_links = driver.execute_locator(locator)
            if not category_links:
                logger.error(f"Не удалось найти ссылки на категории по адресу: {url}")
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

                category[name] = new_category
                await self.crawl_categories(link_url, depth - 1, driver, locator, dump_file, default_category_id, new_category)

            # Загружаем данные из файла и объединяем
            loaded_data = j_loads(dump_file) if os.path.exists(dump_file) else {}
            merged_category = {**loaded_data, **category}
            j_dumps(merged_category, dump_file)
            return merged_category

        except Exception as ex:
            logger.error(f"Произошла ошибка во время сканирования категорий: ", ex)
            return category

    def _is_duplicate_url(self, category: Dict, url: str) -> bool:
        """
        Проверяет, существует ли URL уже в словаре категорий.

        :param category: Словарь категорий.
        :type category: Dict
        :param url: URL для проверки.
        :type url: str
        :return: True, если URL является дубликатом, иначе False.
        :rtype: bool
        """
        return any(item.get('url') == url for item in category.values())


def compare_and_print_missing_keys(current_dict: Dict, file_path: str):
    """
    Сравнивает текущий словарь с данными в файле и выводит отсутствующие ключи.

    :param current_dict: Текущий словарь.
    :type current_dict: Dict
    :param file_path: Путь к файлу с данными.
    :type file_path: str
    """
    try:
        data_from_file = j_loads(file_path)
    except Exception as ex:
        logger.error(f"Ошибка загрузки данных из файла: ", ex)
        return

    missing_keys = [key for key in data_from_file if key not in current_dict]
    if missing_keys:
        logger.info(f"Обнаружены отсутствующие ключи: {', '.join(missing_keys)}")
```