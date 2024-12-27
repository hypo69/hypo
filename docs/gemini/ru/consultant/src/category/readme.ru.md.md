# Анализ кода модуля src.category

**Качество кода: 7**
-  Плюсы
    -  Код хорошо документирован с использованием reStructuredText (RST).
    -  Присутствует описание основных функций и классов.
    -  Приведены примеры использования.
-  Минусы
    -  В коде отсутствуют проверки на наличие необходимых модулей и пакетов.
    -  Не все комментарии соответствуют стандарту reStructuredText (RST).
    -  В тексте есть излишние фразы типа "получает" или "делает"
    -  Нет обработки ошибок при загрузке данных из файла.
    -  Отсутствуют импорты необходимых модулей.
    -  Не все функции и методы имеют docstring в стиле reStructuredText.
    -  Используются избыточные блоки try-except.
    -  Не используется `from src.logger.logger import logger` для логирования ошибок.

**Рекомендации по улучшению**

1.  **Импорты:** Добавить необходимые импорты в начало модуля.
2.  **Комментарии:** Переписать все комментарии в соответствии со стандартом RST.
3.  **Обработка ошибок:** Использовать `logger.error` вместо общих `try-except` блоков.
4.  **Документация:** Дополнить docstring для всех функций, методов и классов.
5.  **Именование:** Имена функций, переменных и импортов должны соответствовать ранее обработанным файлам.
6.  **Загрузка данных:** Использовать `j_loads` из `src.utils.jjson` вместо стандартного `json.load`.
7.  **Убрать лишние фразы:**  Убрать из описаний фразы "получает", "делает" и подобные.
8.  **Добавить логирование:** Добавить логирование ошибок с помощью `logger.error`.

**Оптимизированный код**

```python
"""
Модуль для работы с категориями товаров PrestaShop
=========================================================================================

Этот модуль предоставляет функциональность для работы с категориями товаров,
в первую очередь для PrestaShop. Он предлагает инструменты для взаимодействия с данными категорий,
включая обход страниц категорий и управление иерархической структурой категорий.

Пример использования
--------------------

Пример использования класса `Category`:

.. code-block:: python

    from src.category import Category
    from src.utils.jjson import j_loads

    # Инициализация Category с учетными данными API
    category = Category(api_credentials={'api_key': 'your_api_key'})

    # Получение родительских категорий
    parents = category.get_parents(id_category=123, dept=2)

    # Асинхронный обход категорий
    # Предполагается, что driver_instance определён
    # category_data = await category.crawl_categories_async(
    #    url='https://example.com/categories',
    #    depth=3,
    #    driver=driver_instance,
    #    locator='//a[@class="category-link"]',
    #    dump_file='categories.json',
    #    default_category_id=123
    # )

    # Загрузка данных из файла
    file_path = 'saved_categories.json'
    try:
        loaded_data = j_loads(file_path)
    except FileNotFoundError as e:
        print(f"Файл не найден: {e}")
        loaded_data = {}


    # Сравнение текущих данных категорий с файлом и вывод отсутствующих ключей
    # compare_and_print_missing_keys(current_dict=category_data, file_path='saved_categories.json')

"""
import asyncio
from typing import Any, Dict, List, Optional
from lxml import html
import requests
from selenium import webdriver
from src.endpoints.prestashop import PrestaCategory
from src.utils.jjson import j_loads, j_dumps
from src.logger.logger import logger

class Category(PrestaCategory):
    """
    Класс для обработки категорий товаров.

    Наследуется от :class:`PrestaCategory`.
    Предназначен для обработки категорий товаров, получения родительских категорий
    и рекурсивного обхода страниц категорий.
    """
    def __init__(self, api_credentials, *args, **kwargs):
        """
        Инициализирует объект Category.

        :param api_credentials: Учетные данные API для доступа к данным категорий.
        :param args: Список аргументов переменной длины (не используется).
        :param kwargs: Ключевые аргументы (не используются).
        """
        super().__init__(api_credentials)

    def get_parents(self, id_category: int, dept: int) -> List[int]:
        """
        Возвращает список родительских категорий.

        :param id_category: ID категории, для которой нужно получить родительские категории.
        :param dept: Уровень глубины категории.
        :return: Список родительских категорий.
        """
        parents = []
        if id_category == 0 or dept <= 0:
            return parents
        try:
            category_data = self.get_category_by_id(id_category)
            if category_data and category_data.get('associations') and category_data['associations'].get('categories'):
                parent_ids = [int(cat['id']) for cat in category_data['associations']['categories'] if cat.get('id')]
                for parent_id in parent_ids:
                    parents.extend(self.get_parents(parent_id, dept - 1))
                parents.extend(parent_ids)
            return parents
        except Exception as e:
            logger.error(f'Ошибка при получении родительских категорий для {id_category=}', exc_info=e)
            return []

    async def crawl_categories_async(self, url: str, depth: int, driver: webdriver.Chrome,
                                     locator: str, dump_file: str, default_category_id: int,
                                     category: Optional[Dict] = None) -> Dict:
        """
        Асинхронно обходит категории, строя иерархический словарь.

        :param url: URL страницы категории.
        :param depth: Глубина рекурсии обхода.
        :param driver: Экземпляр Selenium WebDriver.
        :param locator: XPath локатор для ссылок на категории.
        :param dump_file: Путь к файлу JSON для сохранения результатов.
        :param default_category_id: ID категории по умолчанию.
        :param category: Существующий словарь категории (по умолчанию=None).
        :return: Обновленный или новый словарь категорий.
        """
        if category is None:
            category = {}
        if depth <= 0:
            return category

        try:
            driver.get(url)
            elements = driver.find_elements('xpath', locator)
            links = [el.get_attribute('href') for el in elements]
        except Exception as e:
            logger.error(f'Ошибка при загрузке страницы {url=}', exc_info=e)
            return category


        for link in links:
             if self._is_duplicate_url(category, link):
                 continue
             category[link] = {
                'url': link,
                'depth': depth,
                'id': default_category_id,
                'children': {},
             }
             category[link]['children'] = await self.crawl_categories_async(
                 link, depth - 1, driver, locator, dump_file, default_category_id
             )
        try:
             j_dumps(category, dump_file)
        except Exception as e:
            logger.error(f'Ошибка при сохранении данных в файл {dump_file=}', exc_info=e)

        return category

    def crawl_categories(self, url: str, depth: int, driver: webdriver.Chrome,
                         locator: str, dump_file: str, id_category_default: int,
                         category: Dict = None) -> Dict:
        """
        Рекурсивно обходит категории и строит иерархический словарь.

        :param url: URL страницы для обхода.
        :param depth: Глубина рекурсии.
        :param driver: Экземпляр Selenium WebDriver.
        :param locator: XPath локатор для поиска ссылок на категории.
        :param dump_file: Файл для сохранения иерархического словаря.
        :param id_category_default: ID категории по умолчанию.
        :param category: Словарь категории (по умолчанию пустой).
        :return: Иерархический словарь категорий и их URL.
        """
        if category is None:
             category = {}
        if depth <= 0:
            return category
        try:
            driver.get(url)
            elements = driver.find_elements('xpath', locator)
            links = [el.get_attribute('href') for el in elements]
        except Exception as e:
            logger.error(f'Ошибка при загрузке страницы {url=}', exc_info=e)
            return category


        for link in links:
            if self._is_duplicate_url(category, link):
                continue
            category[link] = {
                'url': link,
                'depth': depth,
                'id': id_category_default,
                'children': {},
            }
            category[link]['children'] = self.crawl_categories(
                link, depth - 1, driver, locator, dump_file, id_category_default,
            )
        try:
            j_dumps(category, dump_file)
        except Exception as e:
            logger.error(f'Ошибка при сохранении данных в файл {dump_file=}', exc_info=e)

        return category

    def _is_duplicate_url(self, category: Dict, url: str) -> bool:
        """
        Проверяет, существует ли URL в словаре категорий.

        :param category: Словарь категорий.
        :param url: URL для проверки.
        :return: True, если URL является дубликатом, иначе False.
        """
        return url in category


def compare_and_print_missing_keys(current_dict: Dict, file_path: str) -> None:
    """
    Сравнивает текущий словарь с данными из файла и выводит отсутствующие ключи.

    :param current_dict: Словарь для сравнения.
    :param file_path: Путь к файлу, содержащему данные для сравнения.
    """
    try:
        saved_data = j_loads(file_path)
    except FileNotFoundError as e:
         logger.error(f'Файл не найден {file_path=}', exc_info=e)
         return

    if not isinstance(saved_data, dict):
        logger.error(f'Ожидается словарь, получено {type(saved_data)=}')
        return

    current_keys = set(current_dict.keys())
    saved_keys = set(saved_data.keys())
    missing_keys = saved_keys - current_keys
    if missing_keys:
        print(f"Отсутствуют следующие ключи в текущем словаре: {missing_keys}")
    else:
        print("Все ключи из файла присутствуют в текущем словаре.")
```