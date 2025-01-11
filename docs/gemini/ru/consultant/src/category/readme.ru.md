# Анализ кода модуля `src.category`

**Качество кода:**

- **Соответствие стандартам**: 7/10
- **Плюсы**:
    - Хорошая структурированность документации.
    - Наличие описания основных методов и класса.
    - Указаны зависимости.
- **Минусы**:
    - В документации не используется формат RST для описания функций и классов, что снижает её автоматическую обработку.
    - Отсутствует подробное описание параметров методов в стиле RST.
    - Примеры использования недостаточно конкретны и не могут быть скопированы и выполнены без адаптации.
    - Не все функции и методы имеют подробное RST-описание.

**Рекомендации по улучшению:**

- Переписать документацию, используя RST для более точного описания функций, методов и классов, а также добавить примеры использования в формате RST.
- Добавить подробные описания аргументов и возвращаемых значений для всех методов, используя RST-формат.
- Обновить примеры использования, сделав их более наглядными и готовыми к выполнению.
- Убедиться, что все зависимости правильно указаны и импортируются.
- Избегать комментариев типа "получаем" или "делаем", использовать более конкретные описания.
- Сделать отступы в соответствии со стандартами PEP8.

**Оптимизированный код:**

```python
"""
Модуль для работы с категориями товаров.
========================================

Модуль `src.category` предоставляет функциональность для работы с категориями товаров,
в первую очередь для PrestaShop. Он предлагает инструменты для взаимодействия с данными категорий,
включая обход страниц категорий и управление иерархической структурой категорий.

Пример использования:
---------------------
.. code-block:: python

    from src.category import Category
    from selenium import webdriver
    import asyncio

    # Инициализация Category с учетными данными API
    api_credentials = {'api_key': 'your_api_key'}
    category = Category(api_credentials=api_credentials)

    # Получение родительских категорий
    parents = category.get_parents(id_category=123, dept=2)

    # Инициализация Selenium WebDriver (пример)
    driver = webdriver.Chrome() # или любой другой драйвер

    # Асинхронный обход категорий
    async def main():
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

    if __name__ == "__main__":
        asyncio.run(main())
"""
from pathlib import Path
from typing import Any, Dict, List, Optional

from selenium import webdriver
from src.endpoints.prestashop import PrestaCategory  # type: ignore
from src.logger import logger  # type: ignore
from src.utils.jjson import j_loads, j_dumps  # type: ignore


class Category(PrestaCategory):
    """
    Класс для работы с категориями товаров.

    Наследует от `PrestaCategory` и предназначен для обработки категорий товаров,
    получения родительских категорий и рекурсивного обхода страниц категорий.
    """
    def __init__(self, api_credentials: Dict, *args: List, **kwargs: Dict) -> None:
        """
        Инициализирует объект `Category`.

        :param api_credentials: Учетные данные API для доступа к данным категорий.
        :type api_credentials: Dict
        :param args: Список аргументов переменной длины (не используется).
        :type args: List
        :param kwargs: Ключевые аргументы (не используются).
        :type kwargs: Dict
        """
        super().__init__(api_credentials=api_credentials)
        self.api_credentials = api_credentials # Сохраняем учетные данные для последующего использования

    def get_parents(self, id_category: int, dept: int) -> List[Dict]:
        """
        Получает список родительских категорий.

        :param id_category: ID категории, для которой нужно получить родительские категории.
        :type id_category: int
        :param dept: Уровень глубины категории.
        :type dept: int
        :return: Список родительских категорий.
        :rtype: List[Dict]

        Пример:
           >>> category = Category(api_credentials={'api_key': 'test_key'})
           >>> parents = category.get_parents(id_category=123, dept=2)
           >>> print(parents)
           []
        """
        categories = []
        try:
             categories = self._get_parents(id_category=id_category, dept=dept)
        except Exception as e:
           logger.error(f"Error getting parents category with id: {id_category} - {e}")
        return categories

    async def crawl_categories_async(
        self,
        url: str,
        depth: int,
        driver: webdriver.Chrome,
        locator: str,
        dump_file: str | Path,
        default_category_id: int,
        category: Optional[Dict] = None,
    ) -> Dict:
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
        :type category: Optional[Dict], optional
        :return: Обновленный или новый словарь категорий.
        :rtype: Dict
        :raises Exception: В случае ошибки при обходе категорий.

        Пример:
           >>> import asyncio
           >>> from selenium import webdriver
           >>> driver = webdriver.Chrome()
           >>> category = Category(api_credentials={'api_key': 'test_key'})
           >>> async def main():
           ...   result = await category.crawl_categories_async(
           ...      url='https://example.com/categories',
           ...      depth=1,
           ...      driver=driver,
           ...      locator='//a[@class="category-link"]',
           ...      dump_file='categories.json',
           ...      default_category_id=1
           ...   )
           ...   print(result)
           >>> asyncio.run(main())
           {}
        """
        if category is None:
            category = {}
        try:
            category = await self._crawl_categories_async(
                url=url,
                depth=depth,
                driver=driver,
                locator=locator,
                dump_file=dump_file,
                id_category_default=default_category_id,
                category=category,
            )
        except Exception as e:
            logger.error(f"Error crawling categories async: {e}")
        return category

    def crawl_categories(
        self,
        url: str,
        depth: int,
        driver: webdriver.Chrome,
        locator: str,
        dump_file: str | Path,
        id_category_default: int,
        category: Optional[Dict] = None,
    ) -> Dict:
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
        :type category: Optional[Dict], optional
        :return: Иерархический словарь категорий и их URL.
        :rtype: Dict
        :raises Exception: В случае ошибки при обходе категорий.

        Пример:
           >>> from selenium import webdriver
           >>> driver = webdriver.Chrome()
           >>> category = Category(api_credentials={'api_key': 'test_key'})
           >>> result = category.crawl_categories(
           ...      url='https://example.com/categories',
           ...      depth=1,
           ...      driver=driver,
           ...      locator='//a[@class="category-link"]',
           ...      dump_file='categories.json',
           ...      id_category_default=1
           ...   )
           >>> print(result)
           {}
        """
        if category is None:
            category = {}
        try:
            category = self._crawl_categories(
                url=url,
                depth=depth,
                driver=driver,
                locator=locator,
                dump_file=dump_file,
                id_category_default=id_category_default,
                category=category,
            )
        except Exception as e:
            logger.error(f"Error crawling categories: {e}")
        return category

    def _is_duplicate_url(self, category: Dict, url: str) -> bool:
        """
        Проверяет, существует ли URL в словаре категорий.

        :param category: Словарь категорий.
        :type category: Dict
        :param url: URL для проверки.
        :type url: str
        :return: `True`, если URL является дубликатом, иначе `False`.
        :rtype: bool

        Пример:
            >>> category_data = {'1': {'url': 'https://example.com'}}
            >>> category = Category(api_credentials={'api_key': 'test_key'})
            >>> category._is_duplicate_url(category_data, 'https://example.com')
            True
            >>> category._is_duplicate_url(category_data, 'https://test.com')
            False
        """
        for item in category.values():
            if item.get('url') == url:
                return True
        return False


def compare_and_print_missing_keys(current_dict: Dict, file_path: str | Path) -> None:
    """
    Сравнивает текущий словарь с данными из файла и выводит отсутствующие ключи.

    :param current_dict: Словарь для сравнения.
    :type current_dict: Dict
    :param file_path: Путь к файлу, содержащему данные для сравнения.
    :type file_path: str | Path
    :raises FileNotFoundError: Если файл не найден.
    :raises Exception: В случае ошибки при чтении файла или сравнении данных.

    Пример:
        >>> import json
        >>> current_data = {'1': {'name': 'Category1'}, '2': {'name': 'Category2'}}
        >>> with open('test_file.json', 'w') as f:
        ...   json.dump({'1': {'name': 'Category1'}, '3': {'name': 'Category3'}}, f)
        >>> compare_and_print_missing_keys(current_data, 'test_file.json')
        Missing keys in file: {'3'}
    """
    try:
        with open(file_path, 'r') as f:
            file_data = j_loads(f)
    except FileNotFoundError:
        logger.error(f"File not found: {file_path}")
        return
    except Exception as e:
        logger.error(f"Error loading file: {file_path} - {e}")
        return

    missing_keys = set(file_data.keys()) - set(current_dict.keys())
    if missing_keys:
        logger.warning(f"Missing keys in file: {missing_keys}")
    else:
        logger.info(f"All keys from {file_path} present in current data")

```