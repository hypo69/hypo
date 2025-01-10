# Анализ кода модуля `src.category`

**Качество кода**
7
-   Плюсы
    -   Хорошая структурированная документация с описанием класса, методов и функций.
    -   Приведен пример использования класса и функций.
    -   Указаны основные зависимости модуля.
-   Минусы
    -   Отсутствуют RST комментарии к функциям, методам и классам, кроме документации модуля.
    -   Не используется `j_loads` для чтения данных из файла.
    -   Не все импорты добавлены.
    -   Присутствует избыточный `try-except` блок.
    -   Используются `...` как точки остановки.

**Рекомендации по улучшению**

1.  Добавить RST комментарии ко всем функциям, методам и классам для соответствия стандартам оформления docstring в Python.
2.  Заменить использование `json.load` на `j_loads` из `src.utils.jjson` для чтения файлов.
3.  Использовать `from src.logger.logger import logger` для логирования ошибок.
4.  Избегать избыточного использования стандартных блоков `try-except`, предпочитать обработку ошибок с помощью `logger.error`.
5.  Удалить неиспользуемые аргументы `*args, **kwargs` в конструкторе `__init__`.
6.  В комментариях избегать слов 'получаем', 'делаем'. Использовать конкретные формулировки, такие как 'проверка', 'отправка', 'код исполняет ...'.
7.  Удалить `...` из кода и добавить логирование с использованием `logger.debug` или `logger.error`.

**Оптимизированный код**

```python
"""
Модуль для работы с категориями товаров, в первую очередь для PrestaShop.
=========================================================================================

Этот модуль содержит класс :class:`Category`, который используется для обработки категорий
товаров, включая обход страниц категорий и управление иерархической структурой категорий.

Пример использования
--------------------

Пример использования класса `Category`:

.. code-block:: python

    from src.category import Category
    from selenium import webdriver

    # Инициализация Category с учетными данными API
    category = Category(api_credentials={'api_key': 'your_api_key'})

    # Получение родительских категорий
    parents = category.get_parents(id_category=123, dept=2)

    # Пример использования с Selenium WebDriver
    driver = webdriver.Chrome()  # Или другой драйвер
    try:
        # Асинхронный обход категорий
        category_data = await category.crawl_categories_async(
            url='https://example.com/categories',
            depth=3,
            driver=driver,
            locator='//a[@class="category-link"]',
            dump_file='categories.json',
            default_category_id=123
        )
    finally:
        driver.quit()


    # Сравнение текущих данных категорий с файлом и вывод отсутствующих ключей
    compare_and_print_missing_keys(current_dict=category_data, file_path='saved_categories.json')

"""
import asyncio
from pathlib import Path
from typing import Any
import json

from lxml import html
import requests
from selenium.webdriver.remote.webdriver import WebDriver

from src.endpoints.prestashop import PrestaCategory
from src.utils.jjson import j_loads, j_dumps
from src.logger.logger import logger


class Category(PrestaCategory):
    """
    Класс для обработки категорий товаров, включая получение родительских категорий
    и рекурсивный обход страниц категорий.
    """
    def __init__(self, api_credentials: dict):
        """
        Инициализирует объект Category.

        Args:
            api_credentials (dict): Учетные данные API для доступа к данным категорий.
        """
        super().__init__(api_credentials)


    def get_parents(self, id_category: int, dept: int) -> list[dict]:
        """
        Получает список родительских категорий.

        Args:
            id_category (int): ID категории, для которой нужно получить родительские категории.
            dept (int): Уровень глубины категории.

        Returns:
            list[dict]: Список родительских категорий.
        """
        try:
            # код исполняет запрос к API для получения родительских категорий
            category = self.get_category(id_category)
            if not category:
                return []
            parents = [category]
            for _ in range(dept):
                if category['id_parent'] == 0:
                    break
                category = self.get_category(category['id_parent'])
                if category:
                    parents.append(category)
                else:
                    break
            return parents
        except Exception as ex:
             logger.error(f'Ошибка при получении родительских категорий для id {id_category}: {ex}')
             return []


    async def crawl_categories_async(
        self,
        url: str,
        depth: int,
        driver: WebDriver,
        locator: str,
        dump_file: str | Path,
        default_category_id: int,
        category: dict | None = None,
    ) -> dict:
        """
        Асинхронно обходит категории, строя иерархический словарь.

        Args:
            url (str): URL страницы категории.
            depth (int): Глубина рекурсии обхода.
            driver (WebDriver): Экземпляр Selenium WebDriver.
            locator (str): XPath локатор для ссылок на категории.
            dump_file (str | Path): Путь к файлу JSON для сохранения результатов.
            default_category_id (int): ID категории по умолчанию.
            category (dict, optional): Существующий словарь категории. Defaults to None.

        Returns:
             dict: Обновленный или новый словарь категорий.
        """
        if category is None:
            category = {}
        
        if depth <= 0:
            return category
        
        try:
            # код исполняет открытие страницы в браузере
            driver.get(url)
            # код исполняет получение HTML-кода страницы
            page = html.fromstring(driver.page_source)
            # код исполняет поиск ссылок на категории
            links = page.xpath(locator)
        except Exception as ex:
            logger.error(f'Ошибка при получении списка категорий по URL {url}: {ex}')
            return category
        
        for link in links:
            try:
                # код исполняет получение URL и текста ссылки
                url_ = link.get('href')
                text = link.text.strip()
                if not url_ or not text:
                    logger.debug(f'Невалидный URL или текст: {url_=} {text=}')
                    continue

                # Проверка на дубликат URL
                if self._is_duplicate_url(category, url_):
                     logger.debug(f'Дубликат URL: {url_}')
                     continue
                
                # Добавление новой категории
                category[text] = {'url': url_, 'children': {}}
                
                # Рекурсивный вызов для подкатегорий
                category[text]['children'] = await self.crawl_categories_async(url_, depth - 1, driver, locator, dump_file, default_category_id)
            except Exception as ex:
                 logger.error(f'Ошибка при обработке категории {link}: {ex}')
                 continue
        
        return category


    def crawl_categories(
        self,
        url: str,
        depth: int,
        driver: WebDriver,
        locator: str,
        dump_file: str | Path,
        id_category_default: int,
        category: dict | None = None,
    ) -> dict:
        """
        Рекурсивно обходит категории и строит иерархический словарь.

        Args:
            url (str): URL страницы для обхода.
            depth (int): Глубина рекурсии.
            driver (WebDriver): Экземпляр Selenium WebDriver.
            locator (str): XPath локатор для поиска ссылок на категории.
            dump_file (str | Path): Файл для сохранения иерархического словаря.
            id_category_default (int): ID категории по умолчанию.
            category (dict, optional): Словарь категории. Defaults to {}.

        Returns:
             dict: Иерархический словарь категорий и их URL.
        """
        if category is None:
            category = {}

        if depth <= 0:
            return category
        
        try:
            # код исполняет открытие страницы в браузере
            driver.get(url)
            # код исполняет получение HTML-кода страницы
            page = html.fromstring(driver.page_source)
            # код исполняет поиск ссылок на категории
            links = page.xpath(locator)
        except Exception as ex:
            logger.error(f'Ошибка при получении списка категорий по URL {url}: {ex}')
            return category

        for link in links:
            try:
                # код исполняет получение URL и текста ссылки
                url_ = link.get('href')
                text = link.text.strip()
                if not url_ or not text:
                     logger.debug(f'Невалидный URL или текст: {url_=} {text=}')
                     continue

                # Проверка на дубликат URL
                if self._is_duplicate_url(category, url_):
                     logger.debug(f'Дубликат URL: {url_}')
                     continue
                
                # Добавление новой категории
                category[text] = {'url': url_, 'children': {}}

                # Рекурсивный вызов для подкатегорий
                category[text]['children'] = self.crawl_categories(url_, depth - 1, driver, locator, dump_file, id_category_default,category= category[text]['children'])
            except Exception as ex:
                 logger.error(f'Ошибка при обработке категории {link}: {ex}')
                 continue

        return category


    def _is_duplicate_url(self, category: dict, url: str) -> bool:
        """
        Проверяет, существует ли URL в словаре категорий.

        Args:
            category (dict): Словарь категорий.
            url (str): URL для проверки.

        Returns:
            bool: True, если URL является дубликатом, иначе False.
        """
        for cat in category.values():
            if isinstance(cat, dict):
                if cat.get('url') == url:
                    return True
                if 'children' in cat and self._is_duplicate_url(cat['children'], url):
                    return True
        return False


def compare_and_print_missing_keys(current_dict: dict, file_path: str | Path) -> None:
    """
    Сравнивает текущий словарь с данными из файла и выводит отсутствующие ключи.

    Args:
        current_dict (dict): Словарь для сравнения.
        file_path (str | Path): Путь к файлу, содержащему данные для сравнения.
    """
    try:
        # код исполняет чтение данных из файла
        file_data = j_loads(file_path)
        if not file_data:
             logger.error(f'Файл {file_path} пуст или не содержит данных JSON.')
             return

        # код исполняет сравнение ключей
        missing_keys = set(file_data.keys()) - set(current_dict.keys())
        if missing_keys:
            print(f'Отсутствующие ключи: {missing_keys}')
        else:
            print('Все ключи совпадают.')
    except Exception as ex:
        logger.error(f'Ошибка при сравнении ключей с файлом {file_path}: {ex}')
```