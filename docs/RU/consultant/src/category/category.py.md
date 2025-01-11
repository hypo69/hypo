# Анализ кода модуля `category`

**Качество кода**
9
- Плюсы
    - Код хорошо структурирован и разбит на классы и функции, что облегчает его понимание и поддержку.
    - Используется асинхронное программирование для ускорения процесса обхода категорий.
    - Присутствует логирование ошибок, что помогает в отладке.
    - Используются `j_loads` и `j_dumps` для работы с JSON, что соответствует требованиям.
- Минусы
    - В функции `crawl_categories` происходит перезапись файла на каждом шаге рекурсии, что может быть неэффективным.
    - Функция `_is_duplicate_url` не обрабатывает случай, когда `category` является словарем, а не списком.
    - Отсутствует docstring для функции `compare_and_print_missing_keys`.
    - В `__init__` методе класса `Category` не используется `*args` и `**kwargs` и не добавлена документация.
    - Не все блоки `try-except` содержат `logger.error`.

**Рекомендации по улучшению**

1.  В функции `crawl_categories`, переписать логику сохранения в файл, вынести за пределы рекурсивного цикла. Это уменьшит количество операций записи.
2.  В функции `_is_duplicate_url` предусмотреть обработку случая, когда `category` является словарем.
3.  Добавить docstring для функции `compare_and_print_missing_keys`.
4.  Добавить описание `*args` и `**kwargs` в методе `__init__` класса `Category`.
5.  Добавить обработку исключений с `logger.error` во все `try-except` блоки.
6.  Изменить способ создания `new_category` в `crawl_categories_async`, чтобы не использовать list comprehension.
7.  Изменить импорт модуля `header`.
8.  Привести переменные в соответствие с остальными файлами `id_category_default` -> `default_category_id`.

**Оптимизированный код**

```python
"""
Модуль для работы с категориями, в основном для PrestaShop.
============================================================

Этот модуль предоставляет классы для взаимодействия и
обработки данных категорий товаров, особенно актуальных для PrestaShop.

:platform: Windows, Unix
:synopsis: Модуль для работы с категориями, в основном для PrestaShop.
"""
import asyncio
from pathlib import Path
import os
from typing import Dict, List, Any, Tuple
from lxml import html
import requests

# from header import get_header  # TODO:  check import
from src import gs
from src.logger.logger import logger
from src.utils.jjson import j_loads, j_dumps
from src.endpoints.prestashop import PrestaCategory


class Category(PrestaCategory):
    """
    Обработчик категорий для категорий товаров. Наследуется от PrestaCategory.

    Args:
        api_credentials (Dict): API credentials for accessing the category data.
        *args: Variable length argument list.
        **kwargs: Keyword arguments.

    """

    credentials: Dict = None

    def __init__(self, api_credentials, *args, **kwargs):
        """Инициализирует объект Category.

        Args:
            api_credentials (Dict): API credentials для доступа к данным категорий.
            *args:  Список позиционных аргументов.
            **kwargs:  Словарь именованных аргументов.
        """
        super().__init__(api_credentials, *args, **kwargs)

    def get_parents(self, id_category: int, dept: int) -> List:
        """Извлекает список родительских категорий.

        Args:
            id_category (int): ID категории, для которой нужно получить родительские категории.
            dept (int): Глубина уровня категории.
        Returns:
            List: Список родительских категорий.
        """
        return super().get_list_parent_categories(id_category)

    async def crawl_categories_async(self, url: str, depth: int, driver, locator: str, dump_file: str, default_category_id: int, category: Dict = None) -> Dict:
        """Асинхронно обходит категории, создавая иерархический словарь.

        Args:
            url (str): URL страницы категории.
            depth (int): Глубина рекурсии обхода.
            driver: Экземпляр Selenium WebDriver.
            locator (str): XPath локатор для ссылок на категории.
            dump_file (str): Путь к файлу JSON для сохранения результатов.
            default_category_id (int): ID категории по умолчанию.
            category (Dict, optional): Существующий словарь категорий (по умолчанию None).
        Returns:
            Dict: Обновленный или новый словарь категорий.
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
                logger.error(f'Не удалось найти ссылки на категории на {url}')
                return category

            tasks = []
            for name, link_url in category_links:
                if not self._is_duplicate_url(category, link_url):
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
            await asyncio.gather(*tasks)

            return category
        except Exception as ex:
            logger.error(f'Произошла ошибка во время обхода категорий: ', ex)
            return category

    def crawl_categories(self, url: str, depth: int, driver, locator: str, dump_file: str, default_category_id: int, category: Dict = None) -> Dict:
        """Обходит категории рекурсивно и строит иерархический словарь.

        Args:
            url (str): URL страницы для обхода.
            depth (int): Глубина рекурсии.
            driver: Экземпляр Selenium WebDriver.
            locator (str): XPath локатор для поиска ссылок на категории.
            dump_file (str): Файл для сохранения иерархического словаря.
            default_category_id (int): ID категории по умолчанию.
            category (Dict, optional): Словарь категорий (по умолчанию пустой).
        Returns:
            Dict: Иерархический словарь категорий и их URL.
        """
        if depth <= 0:
            return category

        if category is None:
            category = {}
        try:
            driver.get(url)
            driver.wait(1)  # Ожидание загрузки страницы
            category_links = driver.execute_locator(locator)
            if not category_links:
                logger.error(f'Не удалось найти ссылки на категории на {url}')
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
                    }
                }
                category[name] = new_category
                self.crawl_categories(link_url, depth - 1, driver, locator, dump_file, default_category_id, new_category)
            # Используем j_loads и j_dumps для безопасной обработки JSON
            loaded_data = j_loads(dump_file) if os.path.exists(dump_file) else {}
            category = {**loaded_data, **category}
            j_dumps(category, dump_file)
            return category
        except Exception as ex:
            logger.error(f'Произошла ошибка во время обхода категорий: ', ex)
            return category


    def _is_duplicate_url(self, category: Dict, url: str) -> bool:
        """Проверяет, существует ли URL уже в словаре категорий.

        Args:
            category (Dict): Словарь категорий.
            url (str): URL для проверки.
        Returns:
            bool: True, если URL является дубликатом, False в противном случае.
        """
        if isinstance(category, dict):
            return any(url == item.get('url') for item in category.values())
        return False


def compare_and_print_missing_keys(current_dict: Dict, file_path: str) -> None:
    """Сравнивает текущий словарь с данными в файле и выводит отсутствующие ключи.

     Args:
        current_dict (Dict): Текущий словарь для сравнения.
        file_path (str): Путь к файлу для загрузки данных.
    """
    try:
        data_from_file = j_loads(file_path)
    except Exception as ex:
        logger.error(f'Ошибка загрузки данных из файла: ', ex)
        return

    for key in data_from_file:
        if key not in current_dict:
            print(key)
```