# Анализ кода модуля `category`

**Качество кода: 7/10**
-  Плюсы
     -  Хорошее описание модуля и классов, а также их методов в формате RST.
     -  Присутствует пример использования модуля.
     -  Перечислены зависимости модуля.
-  Минусы
    -  Не хватает документации в коде, особенно для функций и переменных.
    -  Не все импорты указаны явно.
    -  Используется `try-except` без конкретизации исключений, что затрудняет отладку.
    -  Не везде используется `logger.error` для логирования ошибок.

**Рекомендации по улучшению**

1. Добавить документацию в виде docstring для каждой функции, метода и класса, включая описание аргументов и возвращаемых значений.
2. Явно импортировать все необходимые модули и классы.
3. Изменить обработку исключений, используя `logger.error` для логирования, и добавить конкретизацию исключений.
4. Использовать `j_loads` и `j_dumps` из `src.utils.jjson` для работы с JSON файлами.
5. Добавить комментарии для каждого блока кода, объясняющие его назначение.

**Оптимизированный код**

```python
"""
Модуль для работы с категориями товаров, в первую очередь для PrestaShop.
=========================================================================================

Этот модуль содержит класс :class:`Category`, который используется для обхода и управления категориями товаров,
включая получение родительских категорий и рекурсивный обход страниц категорий.

Пример использования
--------------------

Пример использования класса `Category`:

.. code-block:: python

    from src.category import Category
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    from src.utils.jjson import j_loads
    from src.utils.jjson import j_dumps
    from src.logger.logger import logger
    import asyncio

    # Инициализация Category с учетными данными API
    category = Category(api_credentials={'api_key': 'your_api_key'})

    # Получение родительских категорий
    parents = category.get_parents(id_category=123, dept=2)

    # Асинхронный обход категорий
    async def main():
        driver = webdriver.Chrome()  # Инициализация драйвера Chrome
        try:
            category_data = await category.crawl_categories_async(
                url='https://example.com/categories',
                depth=3,
                driver=driver,
                locator='//a[@class="category-link"]',
                dump_file='categories.json',
                default_category_id=123
            )
            # Сравнение текущих данных категорий с файлом и вывод отсутствующих ключей
            compare_and_print_missing_keys(current_dict=category_data, file_path='saved_categories.json')
        finally:
           driver.quit()

    asyncio.run(main())
"""
import asyncio
from pathlib import Path
from typing import Any

from lxml import html
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By

from src.endpoints.prestashop import PrestaCategory
from src.logger.logger import logger
from src.utils.jjson import j_loads, j_dumps


class Category(PrestaCategory):
    """
    Класс для работы с категориями товаров, наследуется от PrestaCategory.
    Предназначен для обхода и управления иерархической структурой категорий.
    """

    def __init__(self, api_credentials, *args, **kwargs):
        """
        Инициализирует объект Category.

        :param api_credentials: Учетные данные API для доступа к данным категорий.
        :param args: Список аргументов переменной длины (не используется).
        :param kwargs: Ключевые аргументы (не используются).
        """
        super().__init__(api_credentials=api_credentials)

    def get_parents(self, id_category: int, dept: int) -> list:
        """
        Получает список родительских категорий для заданной категории.

        :param id_category: ID категории, для которой нужно получить родительские категории.
        :type id_category: int
        :param dept: Уровень глубины категории.
        :type dept: int
        :return: Список родительских категорий.
        :rtype: list
        """
        parents = []
        # Код получает информацию о родительских категориях, используя API
        try:
            category = self.get_category(id_category)
        except Exception as ex:
            logger.error(f'Ошибка при получении категории {id_category}: {ex}')
            return parents

        if category:
            # Код добавляет родительскую категорию в список и рекурсивно вызывает этот метод, если есть родительская категория
            if category.get('id_parent') and category.get('id_parent') != '0':
                parents.append(category)
                if dept > 0:
                    parents.extend(self.get_parents(category.get('id_parent'), dept - 1))
        return parents

    async def crawl_categories_async(self, url: str, depth: int, driver: webdriver.Chrome,
                                   locator: str, dump_file: str | Path,
                                   default_category_id: int, category: dict = None) -> dict:
        """
        Асинхронно обходит категории, строя иерархический словарь.

        :param url: URL страницы категории.
        :type url: str
        :param depth: Глубина рекурсии обхода.
        :type depth: int
        :param driver: Экземпляр Selenium WebDriver.
        :type driver: webdriver.Chrome
        :param locator: XPath локатор для ссылок на категории.
        :type locator: str
        :param dump_file: Путь к файлу JSON для сохранения результатов.
        :type dump_file: str | Path
        :param default_category_id: ID категории по умолчанию.
        :type default_category_id: int
        :param category: (Необязательно) Существующий словарь категории (по умолчанию=None).
        :type category: dict
        :return: Обновленный или новый словарь категорий.
        :rtype: dict
        """
        if category is None:
            category = {}
        if depth < 0:
            return category

        try:
            # Код выполняет запрос к странице и получает HTML
            driver.get(url)
            page_source = driver.page_source
            tree = html.fromstring(page_source)
            links = tree.xpath(locator)
        except Exception as ex:
             logger.error(f'Ошибка при загрузке страницы {url}: {ex}')
             return category
        
        for link in links:
             # Код извлекает URL и текст из ссылки
             url_category = link.get('href')
             text_category = link.text
             
             if self._is_duplicate_url(category, url_category):
                logger.debug(f'Пропущен дубликат URL: {url_category}')
                continue

             # Код добавляет новую категорию в словарь или обновляет существующую
             category[url_category] = {
                 'url': url_category,
                 'name': text_category,
                 'children': {},
                 'id_parent': default_category_id
             }

             # Код рекурсивно вызывает этот метод для дочерних категорий
             category[url_category]['children'] = await self.crawl_categories_async(
                 url_category, depth - 1, driver, locator, dump_file, default_category_id, category[url_category]['children']
             )
        # Код сохраняет категории в JSON файл
        j_dumps(category, dump_file)
        return category


    def crawl_categories(self, url: str, depth: int, driver: webdriver.Chrome,
                         locator: str, dump_file: str | Path,
                         id_category_default: int, category: dict = None) -> dict:
        """
        Рекурсивно обходит категории и строит иерархический словарь.

        :param url: URL страницы для обхода.
        :type url: str
        :param depth: Глубина рекурсии.
        :type depth: int
        :param driver: Экземпляр Selenium WebDriver.
        :type driver: webdriver.Chrome
        :param locator: XPath локатор для поиска ссылок на категории.
        :type locator: str
        :param dump_file: Файл для сохранения иерархического словаря.
        :type dump_file: str | Path
        :param id_category_default: ID категории по умолчанию.
        :type id_category_default: int
        :param category: Словарь категории (по умолчанию пустой).
        :type category: dict
        :return: Иерархический словарь категорий и их URL.
        :rtype: dict
        """
        if category is None:
           category = {}

        if depth < 0:
            return category

        try:
            # Код выполняет запрос к странице и получает HTML
            driver.get(url)
            page_source = driver.page_source
            tree = html.fromstring(page_source)
            links = tree.xpath(locator)
        except Exception as ex:
             logger.error(f'Ошибка при загрузке страницы {url}: {ex}')
             return category

        for link in links:
            # Код извлекает URL и текст из ссылки
             url_category = link.get('href')
             text_category = link.text
            
             if self._is_duplicate_url(category, url_category):
                logger.debug(f'Пропущен дубликат URL: {url_category}')
                continue
             # Код добавляет новую категорию в словарь или обновляет существующую
             category[url_category] = {
                 'url': url_category,
                 'name': text_category,
                 'children': {},
                 'id_parent': id_category_default
             }
             # Код рекурсивно вызывает этот метод для дочерних категорий
             category[url_category]['children'] = self.crawl_categories(
                 url_category, depth - 1, driver, locator, dump_file, id_category_default, category[url_category]['children']
             )
        # Код сохраняет категории в JSON файл
        j_dumps(category, dump_file)
        return category

    def _is_duplicate_url(self, category: dict, url: str) -> bool:
        """
        Проверяет, существует ли URL в словаре категорий.

        :param category: Словарь категорий.
        :type category: dict
        :param url: URL для проверки.
        :type url: str
        :return: `True`, если URL является дубликатом, иначе `False`.
        :rtype: bool
        """
        # Код проверяет, есть ли уже такой URL в словаре
        return url in category

def compare_and_print_missing_keys(current_dict: dict, file_path: str | Path):
    """
    Сравнивает текущий словарь с данными из файла и выводит отсутствующие ключи.

    :param current_dict: Словарь для сравнения.
    :type current_dict: dict
    :param file_path: Путь к файлу, содержащему данные для сравнения.
    :type file_path: str | Path
    """
    try:
        # Код загружает данные из файла JSON
        file_data = j_loads(file_path)
        # Код ищет отсутствующие ключи
        missing_keys = [key for key in file_data if key not in current_dict]
        if missing_keys:
            print(f'Отсутствуют ключи: {missing_keys}')
        else:
           print('Все ключи присутствуют')
    except Exception as ex:
        logger.error(f'Ошибка при сравнении ключей: {ex}')
```