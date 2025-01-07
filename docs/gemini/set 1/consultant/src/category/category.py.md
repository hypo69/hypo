# Анализ кода модуля `category`

**Качество кода**
7
-  Плюсы
    - Код использует асинхронные операции, где это уместно.
    - Присутствует базовая обработка ошибок с логированием.
    - Используются кастомные функции `j_loads` и `j_dumps` для работы с JSON.
    - Присутствует reStructuredText документация.
 -  Минусы
    - Некоторые docstring нуждаются в доработке для более четкого описания параметров и возвращаемых значений.
    - Использование `try-except` блоков можно упростить, полагаясь на логирование ошибок.
    - Функция `_is_duplicate_url` написана менее эффективно чем могла бы быть.
    - Проверка на дубликаты выполняется не правильно, так как идет проверка по значениям, а не по ключам.
    - Функция `compare_and_print_missing_keys` не используется.
    - Есть проблема с сохранением в файл, перезаписываются данные, нужно переделать на сохранения в структуру, для дальнейшего слияния.
    - Функция `crawl_categories` и `crawl_categories_async` очень похожи, следует рассмотреть возможность объеденить в одну.

**Рекомендации по улучшению**

1. **Улучшить docstring:**
   - Добавить более подробное описание параметров и возвращаемых значений для всех функций.

2. **Оптимизировать обработку ошибок:**
   - Использовать `logger.error` для логирования ошибок вместо общих `try-except` блоков, где это возможно.

3. **Оптимизировать `_is_duplicate_url`:**
   - Использовать более эффективный алгоритм для проверки дубликатов URL.

4. **Улучшить `crawl_categories`:**
   -  Переработать логику сохранения данных, чтобы избежать перезаписи, а правильно сливать и сохранять в структуру.
   - По возможности объединить функционал с `crawl_categories_async` в одну функцию с параметром асинхронности.

5. **Удалить неиспользуемый код:**
    - Удалить неиспользуемую функцию `compare_and_print_missing_keys` или найти ей применение.

6. **Улучшить именование переменных и параметров**
    - Использовать более описательные имена переменных, например `category_url` вместо `url`.

**Оптимизированный код**

```python
# -*- coding: utf-8 -*-

#! venv/bin/python/python3.12
"""
Модуль для работы с категориями, в основном для PrestaShop.
============================================================

Этот модуль предоставляет классы для взаимодействия и обработки данных категорий товаров,
что особенно актуально для PrestaShop.

.. module:: src.category
    :platform: Windows, Unix
    :synopsis: Модуль для работы с категориями, в основном для PrestaShop.
"""

import asyncio
import os
from pathlib import Path
from typing import Dict, Any, List, Tuple
from lxml import html
import requests

from src import gs
from src.logger.logger import logger
from src.utils.jjson import j_loads, j_dumps
from src.endpoints.prestashop import PrestaShop, PrestaCategory


class Category(PrestaCategory):
    """
    Класс для обработки категорий товаров.

    Наследует функциональность из :class:`src.endpoints.prestashop.PrestaCategory`.
    """
    credentials: Dict = None

    def __init__(self, api_credentials: Dict, *args: Any, **kwargs: Any) -> None:
        """
        Инициализирует объект Category.

        :param api_credentials: API credentials для доступа к данным категорий.
        :param args: Variable length argument list (не используется).
        :param kwargs: Keyword arguments (не используется).
        """
        super().__init__(api_credentials, *args, **kwargs)

    def get_parents(self, id_category: int, dept: int) -> List[Dict]:
        """
        Получает список родительских категорий.

        :param id_category: ID категории, для которой нужно получить родительские категории.
        :param dept: Глубина категории (не используется).
        :returns: Список родительских категорий.
        """
        return super().get_list_parent_categories(id_category)

    async def crawl_categories_async(
        self,
        category_url: str,
        depth: int,
        driver: Any,
        locator: str,
        dump_file: str,
        default_category_id: int,
        category: Dict = None,
    ) -> Dict:
        """
        Асинхронно сканирует категории, строя иерархический словарь.

        :param category_url: URL страницы категории.
        :param depth: Глубина рекурсии сканирования.
        :param driver: Экземпляр Selenium WebDriver.
        :param locator: XPath локатор для ссылок на категории.
        :param dump_file: Путь к JSON файлу для сохранения результатов.
        :param default_category_id: ID категории по умолчанию.
        :param category: Существующий словарь категорий (по умолчанию None).
        :returns: Обновленный или новый словарь категорий.
        """
        if category is None:
            category = {
                'url': category_url,
                'name': '',
                'presta_categories': {
                    'default_category': default_category_id,
                    'additional_categories': [],
                },
                'children': {},
            }

        if depth <= 0:
            return category

        try:
            driver.get(category_url)
            await asyncio.sleep(1)  # Wait for page load
            category_links = driver.execute_locator(locator)
            if not category_links:
                logger.error(f"Не удалось найти ссылки на категории на {category_url}")
                return category

            tasks = [
                self.crawl_categories_async(
                    link_url,
                    depth - 1,
                    driver,
                    locator,
                    dump_file,
                    default_category_id,
                    new_category,
                )
                for name, link_url in category_links
                if not self._is_duplicate_url(category, link_url)
                for new_category in [
                    {
                        'url': link_url,
                        'name': name,
                        'presta_categories': {
                            'default_category': default_category_id,
                            'additional_categories': [],
                        },
                        'children': {},
                    }
                ]
            ]
            await asyncio.gather(*tasks)

            return category
        except Exception as ex:
            logger.error("Произошла ошибка во время сканирования категорий: ", ex)
            return category

    def crawl_categories(
        self,
        category_url: str,
        depth: int,
        driver: Any,
        locator: str,
        dump_file: str,
        default_category_id: int,
        category: Dict = None,
    ) -> Dict:
        """
        Сканирует категории рекурсивно и строит иерархический словарь.

        :param category_url: URL страницы для сканирования.
        :param depth: Глубина рекурсии.
        :param driver: Экземпляр Selenium WebDriver.
        :param locator: XPath локатор для поиска ссылок на категории.
        :param dump_file: Файл для сохранения иерархического словаря.
        :param default_category_id: ID категории по умолчанию.
        :param category: Словарь категорий (по умолчанию пустой).
        :return: Иерархический словарь категорий и их URL.
        """
        if category is None:
            category = {
                'url': category_url,
                'name': '',
                'presta_categories': {
                    'default_category': default_category_id,
                    'additional_categories': [],
                },
                'children': {},
            }
        if depth <= 0:
            return category
        try:
            driver.get(category_url)
            driver.wait(1)  # Wait for page load
            category_links = driver.execute_locator(locator)
            if not category_links:
                logger.error(f"Не удалось найти ссылки на категории на {category_url}")
                return category

            for name, link_url in category_links:
                if self._is_duplicate_url(category, link_url):
                    continue
                new_category = {
                    'url': link_url,
                    'name': name,
                    'presta_categories': {
                        'default_category': default_category_id,
                        'additional_categories': [],
                    },
                     'children': {},
                }

                category['children'][name] = new_category
                self.crawl_categories(
                    link_url,
                    depth - 1,
                    driver,
                    locator,
                    dump_file,
                    default_category_id,
                    new_category,
                )
            # Используем j_loads и j_dumps для безопасной обработки JSON
            loaded_data = j_loads(dump_file) if os.path.exists(dump_file) else {}
            merged_category = self._merge_categories(loaded_data, category)
            j_dumps(merged_category, dump_file)

            return merged_category
        except Exception as ex:
            logger.error("Произошла ошибка во время сканирования категорий: ", ex)
            return category

    def _is_duplicate_url(self, category: Dict, url: str) -> bool:
        """
        Проверяет, существует ли URL уже в словаре категорий.

        :param category: Словарь категорий.
        :param url: URL для проверки.
        :returns: True, если URL дубликат, иначе False.
        """
        if not category or not isinstance(category, dict) or 'children' not in category:
            return False

        def _check_recursive(cat, target_url):
             if not cat or not isinstance(cat, dict):
                return False
             if 'url' in cat and cat['url'] == target_url:
                 return True
             if 'children' in cat:
                 for child in cat['children'].values():
                     if _check_recursive(child, target_url):
                         return True
             return False
        return _check_recursive(category, url)


    def _merge_categories(self, existing_data: Dict, new_data: Dict) -> Dict:
        """
        Объединяет существующие данные категорий с новыми данными.

        :param existing_data: Существующие данные категорий.
        :param new_data: Новые данные категорий.
        :returns: Объединенный словарь категорий.
        """
        if not existing_data:
             return new_data

        def _merge_recursive(existing, new):
            if not isinstance(existing, dict) or not isinstance(new, dict):
                return new
            for key, new_value in new.items():
                if key in existing:
                  if key == 'children':
                      existing[key] = _merge_recursive(existing.get(key, {}), new_value)
                  elif isinstance(new_value, dict) and isinstance(existing[key], dict):
                       _merge_recursive(existing[key],new_value)
                  else:
                       existing[key] = new_value
                else:
                    existing[key] = new_value
            return existing
        return _merge_recursive(existing_data, new_data)