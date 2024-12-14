# Анализ кода модуля src.category

**Качество кода**
7
-   Плюсы
    -  Документация написана в формате reStructuredText, что соответствует требованиям.
    -  Присутствует общее описание модуля и описание каждого класса и метода.
    -  Есть пример использования.
-   Минусы
    -  Не все docstring методы и класса заполнены, что может затруднить понимание кода.
    -  Не хватает обработки ошибок и логирования в методах.
    -  В коде присутствуют `...` как точки остановки, что требует доработки.
    -  Отсутствует обработка исключений с использованием `logger.error`.
    -  Некоторые переменные и параметры не имеют четких описаний в docstring.

**Рекомендации по улучшению**
1.  Добавить полные docstring для всех методов и классов, включая описание параметров и возвращаемых значений.
2.  Внедрить логирование ошибок с использованием `logger.error` для обработки возможных исключений.
3.  Использовать `j_loads` и `j_dumps` из `src.utils.jjson` для работы с JSON-файлами.
4.  Добавить проверки на валидность данных, получаемых извне, для предотвращения ошибок.
5.  Удалить или заменить `...` на корректную логику или комментарии.
6.  Пересмотреть структуру и логику `crawl_categories` и `crawl_categories_async` для повышения читаемости и удобства.
7.  Добавить комментарии к коду для лучшего понимания его работы, используя RST.
8.  Привести в соответствие имена функций и импортов с ранее обработанными файлами.

**Оптимизированный код**

```python
"""
Модуль для работы с категориями товаров, включая обход страниц и управление иерархией категорий.
=========================================================================================

Этот модуль предоставляет класс :class:`Category`, который наследует от :class:`src.endpoints.prestashop.PrestaCategory`
и используется для обработки категорий товаров, получения родительских категорий и рекурсивного обхода страниц категорий.

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

    # Асинхронный обход категорий
    driver = webdriver.Chrome()  # Инициализация драйвера Selenium
    category_data = await category.crawl_categories_async(
        url='https://example.com/categories',
        depth=3,
        driver=driver,
        locator='//a[@class="category-link"]',
        dump_file='categories.json',
        default_category_id=123
    )
    driver.quit()
    # Сравнение текущих данных категорий с файлом и вывод отсутствующих ключей
    compare_and_print_missing_keys(current_dict=category_data, file_path='saved_categories.json')
"""
import asyncio
import requests
from lxml import html
from typing import Any, Dict, List
from selenium.webdriver.remote.webdriver import WebDriver
from src.endpoints.prestashop import PrestaCategory
from src.utils.jjson import j_loads, j_dumps
from src.logger.logger import logger


class Category(PrestaCategory):
    """
    Класс для работы с категориями товаров PrestaShop.

    Наследует от :class:`src.endpoints.prestashop.PrestaCategory`
    и предоставляет методы для обработки категорий, включая получение родительских категорий,
    рекурсивный обход страниц категорий и сохранение результатов.
    """
    def __init__(self, api_credentials, *args, **kwargs):
        """
        Инициализирует объект Category.

        :param api_credentials: Учетные данные API для доступа к данным категорий.
        :type api_credentials: Dict[str, str]
        :param args: Список аргументов переменной длины (не используется).
        :type args: tuple
        :param kwargs: Ключевые аргументы (не используются).
        :type kwargs: Dict[str, Any]
        """
        super().__init__(api_credentials)

    def get_parents(self, id_category: int, dept: int) -> List[int]:
        """
        Получает список ID родительских категорий для заданной категории.

        :param id_category: ID категории, для которой нужно получить родительские категории.
        :type id_category: int
        :param dept: Уровень глубины категории.
        :type dept: int
        :return: Список ID родительских категорий.
        :rtype: List[int]
        """
        try:
            # Выполняется запрос к API для получения информации о категории.
            response = self.get_category(id_category)
            if response and 'associations' in response and 'categories' in response['associations']:
                # Извлекается список родительских категорий.
                parents = [int(cat['id']) for cat in response['associations']['categories']]
                return parents
            return []
        except Exception as ex:
            # Логирование ошибки при получении родительских категорий.
            logger.error(f'Ошибка при получении родительских категорий для категории {id_category}: {ex}')
            return []

    async def crawl_categories_async(self, url: str, depth: int, driver: WebDriver, locator: str, dump_file: str,
                                     default_category_id: int, category: Dict = None) -> Dict:
        """
        Асинхронно обходит категории, строя иерархический словарь.

        :param url: URL страницы категории.
        :type url: str
        :param depth: Глубина рекурсии обхода.
        :type depth: int
        :param driver: Экземпляр Selenium WebDriver.
        :type driver: WebDriver
        :param locator: XPath локатор для ссылок на категории.
        :type locator: str
        :param dump_file: Путь к файлу JSON для сохранения результатов.
        :type dump_file: str
        :param default_category_id: ID категории по умолчанию.
        :type default_category_id: int
        :param category: (Необязательно) Существующий словарь категории (по умолчанию=None).
        :type category: Dict, optional
        :return: Обновленный или новый словарь категорий.
        :rtype: Dict
        """
        category = category or {}
        if depth == 0:
            return category

        try:
            # Выполняется получение контента страницы с помощью Selenium.
            driver.get(url)
            page_content = driver.page_source
            tree = html.fromstring(page_content)
            # Извлекаются ссылки на категории с помощью XPath локатора.
            links = tree.xpath(locator)
        except Exception as ex:
            # Логирование ошибки, если не удаётся получить контент страницы.
            logger.error(f'Ошибка при загрузке страницы {url} или парсинге ссылок: {ex}')
            return category

        for link in links:
            try:
                # Извлекается URL категории из атрибута href.
                url_category = link.get('href')
                if not url_category:
                     # Логирование ошибки, если URL отсутствует.
                    logger.error(f"Не удалось извлечь URL из ссылки: {link}")
                    continue
                if self._is_duplicate_url(category, url_category):
                    # Проверка на дубликат URL.
                    logger.debug(f"Дубликат URL: {url_category}")
                    continue

                # Инициализируется словарь для новой категории.
                category_data = {
                    'url': url_category,
                    'children': {},
                    'id_parent': self.get_parents(default_category_id, depth)
                }
                # Рекурсивный вызов для обработки дочерних категорий.
                category_data['children'] = await self.crawl_categories_async(
                    url_category, depth - 1, driver, locator, dump_file, default_category_id
                    )
                # Обновление общего словаря категорий.
                category[url_category] = category_data
            except Exception as ex:
                # Логирование ошибки в процессе обработки отдельной ссылки.
                logger.error(f'Ошибка при обработке ссылки {link}: {ex}')
        try:
            # Код сохраняет иерархический словарь категорий в файл.
            with open(dump_file, 'w', encoding='utf-8') as f:
                j_dumps(category, f)
        except Exception as ex:
            # Логирование ошибки при записи в файл.
            logger.error(f'Ошибка при записи в файл {dump_file}: {ex}')
        return category

    def crawl_categories(self, url: str, depth: int, driver: WebDriver, locator: str, dump_file: str,
                         id_category_default: int, category: Dict = None) -> Dict:
        """
        Рекурсивно обходит категории и строит иерархический словарь.

        :param url: URL страницы для обхода.
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
        :param category: Словарь категории (по умолчанию пустой).
        :type category: Dict, optional
        :return: Иерархический словарь категорий и их URL.
        :rtype: Dict
        """
        category = category or {}
        if depth == 0:
            return category
        try:
            # Код получает контент страницы с помощью Selenium.
            driver.get(url)
            page_content = driver.page_source
            tree = html.fromstring(page_content)
            # Код извлекает ссылки на категории с помощью XPath локатора.
            links = tree.xpath(locator)
        except Exception as ex:
            # Логирование ошибки при загрузке страницы.
            logger.error(f'Ошибка при загрузке страницы {url} или парсинге ссылок: {ex}')
            return category
        for link in links:
            try:
                # Извлекает URL категории из атрибута href.
                url_category = link.get('href')
                if not url_category:
                   # Логирование ошибки, если URL отсутствует.
                    logger.error(f"Не удалось извлечь URL из ссылки: {link}")
                    continue
                if self._is_duplicate_url(category, url_category):
                    # Проверка на дубликат URL.
                    logger.debug(f"Дубликат URL: {url_category}")
                    continue
                # Инициализируется словарь для новой категории.
                category_data = {
                    'url': url_category,
                    'children': {},
                    'id_parent': self.get_parents(id_category_default, depth)
                }
                # Рекурсивный вызов для обработки дочерних категорий.
                category_data['children'] = self.crawl_categories(
                    url_category, depth - 1, driver, locator, dump_file, id_category_default
                    )
                # Обновление общего словаря категорий.
                category[url_category] = category_data
            except Exception as ex:
                # Логирование ошибки при обработке отдельной ссылки.
                logger.error(f'Ошибка при обработке ссылки {link}: {ex}')
        try:
             # Код сохраняет иерархический словарь категорий в файл.
            with open(dump_file, 'w', encoding='utf-8') as f:
                j_dumps(category, f)
        except Exception as ex:
           # Логирование ошибки при записи в файл.
           logger.error(f'Ошибка при записи в файл {dump_file}: {ex}')
        return category

    def _is_duplicate_url(self, category: Dict, url: str) -> bool:
        """
        Проверяет, существует ли URL в словаре категорий.

        :param category: Словарь категорий.
        :type category: Dict
        :param url: URL для проверки.
        :type url: str
        :return: True, если URL является дубликатом, иначе False.
        :rtype: bool
        """
        return url in category


def compare_and_print_missing_keys(current_dict: Dict, file_path: str):
    """
    Сравнивает текущий словарь с данными из файла и выводит отсутствующие ключи.

    :param current_dict: Словарь для сравнения.
    :type current_dict: Dict
    :param file_path: Путь к файлу, содержащему данные для сравнения.
    :type file_path: str
    """
    try:
        # Загружает словарь из файла.
        with open(file_path, 'r', encoding='utf-8') as f:
            file_dict = j_loads(f)
    except FileNotFoundError:
        # Логирование ошибки, если файл не найден.
        logger.error(f"Файл не найден: {file_path}")
        return
    except Exception as ex:
        # Логирование ошибки при чтении файла.
        logger.error(f'Ошибка при чтении файла {file_path}: {ex}')
        return

    # Код сравнивает ключи словарей и выводит отсутствующие.
    missing_keys = set(file_dict.keys()) - set(current_dict.keys())
    if missing_keys:
        print(f"Отсутствуют следующие ключи в текущем словаре: {missing_keys}")
    else:
        print("Все ключи из файла присутствуют в текущем словаре.")

```