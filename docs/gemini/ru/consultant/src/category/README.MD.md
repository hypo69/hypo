### Анализ кода модуля `src.category`

**Качество кода:**

- **Соответствие стандартам**: 7
- **Плюсы**:
    - Наличие подробного описания модуля, классов и методов.
    - Присутствуют примеры использования и указаны зависимости.
    - Использованы docstrings для описания функций и методов.
- **Минусы**:
    - Не все docstrings соответствуют стандарту RST.
    - Отсутствуют явные импорты в коде, что затрудняет понимание зависимостей.
    - Использование `*args`, `**kwargs` без явного пояснения не рекомендуется.
    - Не хватает примеров использования функций в формате doctest.
    - Нет обработки ошибок через `logger`.
    - Отсутствует выравнивание кода.

**Рекомендации по улучшению:**

-   Дополнить docstrings в формате RST, включая `param`, `type`, `return`, `rtype`, `raises` для каждого метода и функции.
-   Явно указать все необходимые импорты в коде.
-   Избегать использования `*args`, `**kwargs` без конкретного назначения.
-   Добавить примеры использования с `doctest` в docstrings для каждой функции и метода.
-   Внедрить обработку ошибок через `logger.error` вместо общих `try-except`.
-   Выровнять код в соответствии со стандартом PEP8, особенно названия функций, переменных и импортов.
-   Использовать `j_loads` и `j_dumps` из `src.utils.jjson`.
-   Заменить  `# Module:` на `"""` для rst документации модуля
-   Всегда используйте одинарные кавычки (`'`) в Python-коде.

**Оптимизированный код:**

```python
"""
Модуль для работы с категориями продуктов PrestaShop
===================================================

Этот модуль содержит класс :class:`Category`, который используется для взаимодействия с категориями продуктов PrestaShop.
Он включает функциональность для обхода категорий, получения родительских категорий и сравнения данных.

Пример использования
----------------------
.. code-block:: python

    from src.category import Category
    from src.logger import logger
    from selenium import webdriver
    from selenium.webdriver.chrome.options import Options


    # Пример инициализации класса Category
    api_credentials = {'api_key': 'your_api_key'}
    category_manager = Category(api_credentials=api_credentials)

    # Пример получения родительских категорий
    parents = category_manager.get_parents(id_category=123, dept=2)
    print(f"Родительские категории: {parents}")

    # Пример асинхронного обхода категорий
    async def main():
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        driver = webdriver.Chrome(options=chrome_options)
        try:
             category_data = await category_manager.crawl_categories_async(
                    url='https://example.com/categories',
                    depth=3,
                    driver=driver,
                    locator='//a[@class="category-link"]',
                    dump_file='categories.json',
                    default_category_id=123
                )
             print(f"Данные категорий: {category_data}")
        except Exception as e:
            logger.error(f"Ошибка при обходе категорий: {e}")
        finally:
           driver.quit()

    import asyncio
    asyncio.run(main())

    # Пример сравнения данных и вывода недостающих ключей
    current_data = {'key1': 'value1', 'key2': 'value2'}
    file_path = 'categories.json'
    compare_and_print_missing_keys(current_dict=current_data, file_path=file_path)
"""
import asyncio
from pathlib import Path
from typing import Any
from typing import Dict
from typing import List
from typing import Optional
from typing import Union

from selenium.webdriver.remote.webdriver import WebDriver

from src.endpoints.prestashop import PrestaCategory
from src.logger import logger
from src.utils.jjson import j_loads
from src.utils.jjson import j_dumps


class Category(PrestaCategory):
    """
    Класс для работы с категориями продуктов PrestaShop.

    Наследуется от :class:`PrestaCategory` и обеспечивает функциональность для обхода категорий,
    получения родительских категорий и управления иерархической структурой категорий.
    """

    def __init__(self, api_credentials: Dict, *args: tuple, **kwargs: dict) -> None:
        """
        Инициализирует объект класса Category.

        :param api_credentials: Словарь с учетными данными API.
        :type api_credentials: dict
        :param args: Произвольный список позиционных аргументов (не используется).
        :type args: tuple
        :param kwargs: Произвольный словарь именованных аргументов (не используется).
        :type kwargs: dict
        """
        super().__init__(api_credentials)

    def get_parents(self, id_category: int, dept: int) -> List[int]:
        """
        Получает список родительских категорий для заданной категории.

        :param id_category: ID категории, для которой нужно получить родительские категории.
        :type id_category: int
        :param dept: Глубина уровня категории.
        :type dept: int
        :return: Список родительских категорий.
        :rtype: list[int]
        :raises Exception: В случае ошибки при получении родительских категорий.

        Пример:
            >>> category = Category(api_credentials={'api_key': 'your_api_key'})
            >>> parents = category.get_parents(id_category=123, dept=2)
            >>> print(parents)
            []
        """
        try:
            parents = self.get_category_parents(id_category=id_category)
            return parents[0:dept] if parents else []
        except Exception as e:
            logger.error(f'Ошибка при получении родительских категорий: {e}')
            return []

    async def crawl_categories_async(
        self,
        url: str,
        depth: int,
        driver: WebDriver,
        locator: str,
        dump_file: Union[str, Path],
        default_category_id: int,
        category: Optional[Dict] = None,
    ) -> dict:
        """
        Асинхронно обходит категории, строя иерархический словарь.

        :param url: URL страницы категории для обхода.
        :type url: str
        :param depth: Глубина рекурсии обхода.
        :type depth: int
        :param driver: Экземпляр Selenium WebDriver.
        :type driver: WebDriver
        :param locator: XPath локатор для ссылок на категории.
        :type locator: str
        :param dump_file: Путь к файлу JSON для сохранения результатов.
        :type dump_file: str | Path
        :param default_category_id: ID категории по умолчанию.
        :type default_category_id: int
        :param category: Существующий словарь категорий (по умолчанию None).
        :type category: dict, optional
        :return: Обновленный или новый словарь категорий.
        :rtype: dict
         :raises Exception: В случае ошибки при обходе категорий.

        Пример:
            >>> import asyncio
            >>> from selenium import webdriver
            >>> from selenium.webdriver.chrome.options import Options
            >>> async def test_crawl():
            ...    chrome_options = Options()
            ...    chrome_options.add_argument("--headless")
            ...    driver = webdriver.Chrome(options=chrome_options)
            ...    category = Category(api_credentials={'api_key': 'your_api_key'})
            ...    result = await category.crawl_categories_async(
            ...         url='https://example.com/categories',
            ...         depth=1,
            ...         driver=driver,
            ...         locator='//a[@class="category-link"]',
            ...         dump_file='test_categories.json',
            ...         default_category_id=123
            ...    )
            ...    driver.quit()
            ...    print(result)
            >>> asyncio.run(test_crawl())
            {}
        """
        if category is None:
            category = {}
        try:
            if depth == 0:
                return category

            driver.get(url)
            links = driver.find_elements("xpath", locator)
            if not links:
                return category

            category_list = category.get(str(default_category_id), [])
            for link in links:
                url_ = link.get_attribute('href')
                if not url_:
                     continue
                if self._is_duplicate_url(category, url_):
                    continue
                category_list.append({'url': url_})
                category[str(default_category_id)] = category_list
                await asyncio.sleep(0.2)
            for link_ in links:
                url__ = link_.get_attribute('href')
                if not url__:
                     continue
                await self.crawl_categories_async(
                    url=url__,
                    depth=depth - 1,
                    driver=driver,
                    locator=locator,
                    dump_file=dump_file,
                    default_category_id=default_category_id,
                    category=category,
                )
            self._save_to_file(dump_file, category) # сохраняем данные в файл
            return category
        except Exception as e:
            logger.error(f"Ошибка при асинхронном обходе категорий: {e}")
            return category

    def crawl_categories(
        self,
        url: str,
        depth: int,
        driver: WebDriver,
        locator: str,
        dump_file: Union[str, Path],
        id_category_default: int,
        category: Optional[Dict] = None,
    ) -> dict:
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
        :param dump_file: Путь к файлу для сохранения иерархического словаря.
        :type dump_file: str | Path
        :param id_category_default: ID категории по умолчанию.
        :type id_category_default: int
        :param category: Словарь категорий (по умолчанию пустой).
        :type category: dict, optional
        :return: Иерархический словарь категорий и их URL.
        :rtype: dict
         :raises Exception: В случае ошибки при обходе категорий.
        """
        if category is None:
             category = {}
        try:
            if depth == 0:
                return category

            driver.get(url)
            links = driver.find_elements('xpath', locator)
            if not links:
               return category

            category_list = category.get(str(id_category_default), [])
            for link in links:
                url_ = link.get_attribute('href')
                if not url_:
                    continue
                if self._is_duplicate_url(category, url_):
                   continue
                category_list.append({'url': url_})
                category[str(id_category_default)] = category_list

            for link_ in links:
                 url__ = link_.get_attribute('href')
                 if not url__:
                     continue
                 self.crawl_categories(
                   url=url__,
                   depth=depth - 1,
                   driver=driver,
                   locator=locator,
                   dump_file=dump_file,
                   id_category_default=id_category_default,
                   category=category,
                 )
            self._save_to_file(dump_file, category)  # Сохраняем данные в файл
            return category
        except Exception as e:
            logger.error(f'Ошибка при обходе категорий: {e}')
            return category

    def _is_duplicate_url(self, category: Dict, url: str) -> bool:
        """
        Проверяет, существует ли URL уже в словаре категорий.

        :param category: Словарь категорий.
        :type category: dict
        :param url: URL для проверки.
        :type url: str
        :return: True, если URL является дубликатом, иначе False.
        :rtype: bool

        Пример:
            >>> category_data = {'123': [{'url': 'https://example.com/page1'}, {'url': 'https://example.com/page2'}]}
            >>> category = Category(api_credentials={'api_key': 'your_api_key'})
            >>> category._is_duplicate_url(category_data, 'https://example.com/page1')
            True
            >>> category._is_duplicate_url(category_data, 'https://example.com/page3')
            False
        """
        for _, items in category.items():
            for item in items:
                if item.get('url') == url:
                    return True
        return False
    def _save_to_file(self, file_path: Union[str, Path], data: dict) -> None:
         """
         Сохраняет данные в файл.

         :param file_path: Путь к файлу.
         :type file_path: str | Path
         :param data: Данные для сохранения.
         :type data: dict
         :raises Exception: В случае ошибки при сохранении в файл.
         """
         try:
             with open(file_path, 'w', encoding='utf-8') as f:
                 f.write(j_dumps(data))
         except Exception as e:
              logger.error(f'Ошибка при сохранении данных в файл: {e}')

def compare_and_print_missing_keys(current_dict: Dict, file_path: Union[str, Path]) -> None:
    """
    Сравнивает текущий словарь с данными из файла и выводит отсутствующие ключи.

    :param current_dict: Словарь для сравнения.
    :type current_dict: dict
    :param file_path: Путь к файлу с данными для сравнения.
    :type file_path: str | Path
    :raises Exception: В случае ошибки при чтении данных из файла.

    Пример:
        >>> current_data = {'key1': 'value1', 'key2': 'value2'}
        >>> from pathlib import Path
        >>> file_path_example = Path('test_file.json')
        >>> with open(file_path_example, 'w') as f:
        ...    f.write(j_dumps({'key2': 'value2', 'key3': 'value3'}))
        >>> compare_and_print_missing_keys(current_data, file_path_example)
        Missing keys: {'key3'}
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
             file_data = j_loads(f.read())
    except Exception as e:
        logger.error(f'Ошибка при чтении данных из файла: {e}')
        return

    missing_keys = set(file_data.keys()) - set(current_dict.keys())
    if missing_keys:
       print(f'Missing keys: {missing_keys}')