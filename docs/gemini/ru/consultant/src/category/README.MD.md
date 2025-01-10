# Анализ кода модуля `src.category`

**Качество кода**
6
 -  Плюсы
    -   Код имеет подробное описание функциональности модуля и каждого метода.
    -   Присутствуют примеры использования методов.
    -   Используются docstring для описания функций.
    -   Есть разделение на классы и методы, что облегчает понимание структуры кода.
 -  Минусы
    -  Отсутствуют импорты в начале файла.
    -  Не хватает комментариев внутри кода, объясняющих логику работы.
    -  Не стандартизованы docstring согласно PEP257 (не хватает :param:, :return: и тд.).
    -  В коде встречаются блоки `try-except` без конкретной обработки ошибок.
    -  Не используются `j_loads` и `j_dumps` из `src.utils.jjson`.
    -   Не используется `from src.logger.logger import logger`.
    -   Форматирование кода требует улучшения (особенно отступы).

**Рекомендации по улучшению**

1.  **Импорты**: Добавить необходимые импорты в начало файла, включая `src.utils.jjson.j_loads`, `src.utils.jjson.j_dumps`, `src.logger.logger`, `src.endpoints.prestashop.PrestaShop` и `src.endpoints.prestashop.PrestaCategory`.
2.  **Комментарии**: Добавить комментарии внутри методов для более ясного понимания логики.
3.  **Docstring**: Привести docstring к стандартам PEP257.
4.  **Обработка ошибок**: Заменить общие `try-except` на более конкретные с использованием `logger.error`.
5.  **Использование `j_loads` и `j_dumps`**: Применить `j_loads` и `j_dumps` вместо стандартных `json.load` и `json.dump`.
6. **Логирование**: Использовать `from src.logger.logger import logger` для логирования.
7. **Форматирование**: Отформатировать код для улучшения читаемости.

**Оптимизированный код**

```python
"""
Модуль для работы с категориями товаров.
=========================================================================================

Этот модуль предоставляет функциональность для работы с категориями товаров, в частности для PrestaShop.
Он включает в себя инструменты для взаимодействия с данными категорий,
включая обход страниц категорий и управление иерархическими структурами категорий.

Пример использования
--------------------

Пример использования класса `Category`:

.. code-block:: python

    from src.category import Category
    from selenium import webdriver
    from src.utils.jjson import j_dumps
    import asyncio
    # Инициализация класса Category с учетными данными API
    category = Category(api_credentials={'api_key': 'your_api_key'})

    # Получение родительских категорий
    parents = category.get_parents(id_category=123, dept=2)

    # Настройка экземпляра Selenium WebDriver
    driver = webdriver.Chrome()  # или любой другой драйвер
    
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
        await j_dumps('categories.json', category_data)
        # Сравнение текущих данных категорий с файлом и печать отсутствующих ключей
        compare_and_print_missing_keys(current_dict=category_data, file_path='saved_categories.json')
    
    asyncio.run(main())
    driver.quit()

"""
import asyncio
from pathlib import Path
from typing import Any
from typing import Dict
from typing import List
from typing import Optional

from selenium.webdriver.remote.webdriver import WebDriver
from src.endpoints.prestashop import PrestaCategory
from src.endpoints.prestashop import PrestaShop
# Импортируем j_loads и j_dumps из src.utils.jjson
from src.utils.jjson import j_loads
from src.utils.jjson import j_dumps
# Импортируем logger из src.logger
from src.logger.logger import logger

class Category(PrestaCategory):
    """
     Класс для работы с категориями товаров.

    :param api_credentials: Учетные данные API для доступа к данным категорий.
    :type api_credentials: dict
    :param args: Произвольный список аргументов (не используется).
    :type args: tuple
    :param kwargs: Произвольный словарь аргументов (не используется).
    :type kwargs: dict
    """
    def __init__(self, api_credentials, *args, **kwargs):
        # Инициализирует объект Category.
        super().__init__(api_credentials, *args, **kwargs)

    def get_parents(self, id_category: int, dept: int) -> List[int]:
        """
        Извлекает список родительских категорий для заданной категории.

        :param id_category: ID категории, для которой нужно получить родительские категории.
        :type id_category: int
        :param dept: Глубина вложенности категории.
        :type dept: int
        :return: Список ID родительских категорий.
        :rtype: list[int]
        """
        # Код исполняет получение списка родительских категорий
        if not id_category:
            logger.error('Неверный id_category')
            return []
        if not dept:
            logger.error('Неверная глубина dept')
            return []
        try:
            parents_ids = self.get_parents_ids(id_category, dept)
            return parents_ids
        except Exception as e:
            logger.error(f'Ошибка при получении родительских категорий: {e}')
            return []

    async def crawl_categories_async(
        self,
        url: str,
        depth: int,
        driver: WebDriver,
        locator: str,
        dump_file: str | Path,
        default_category_id: int,
        category: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
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
        :param dump_file: Путь к JSON файлу для сохранения результатов.
        :type dump_file: str | Path
        :param default_category_id: ID категории по умолчанию.
        :type default_category_id: int
        :param category: Существующий словарь категорий (по умолчанию None).
        :type category: dict, optional
        :return: Обновленный или новый словарь категорий.
        :rtype: dict
        """
        # Код исполняет асинхронный обход категорий
        if category is None:
            category = {}
        if depth <= 0:
            return category
        try:
            category = await self._crawl_categories(
                url, depth, driver, locator, default_category_id, category
            )
        except Exception as e:
            logger.error(f'Ошибка при асинхронном обходе категорий: {e}')
        return category

    async def _crawl_categories(
        self,
        url: str,
        depth: int,
        driver: WebDriver,
        locator: str,
        default_category_id: int,
        category: Dict[str, Any],
    ) -> Dict[str, Any]:
        """
        Рекурсивно обходит категории и строит иерархический словарь.
        
        :param url: URL страницы для обхода.
        :type url: str
        :param depth: Глубина рекурсии.
        :type depth: int
        :param driver: Экземпляр Selenium WebDriver.
        :type driver: WebDriver
        :param locator: XPath локатор для поиска ссылок категорий.
        :type locator: str
        :param default_category_id: ID категории по умолчанию.
        :type default_category_id: int
        :param category: Словарь категорий (по умолчанию пустой).
        :type category: dict
        :return: Иерархический словарь категорий и их URL.
        :rtype: dict
        """
        # Код исполняет рекурсивный обход категорий
        if depth <= 0:
            return category

        try:
            driver.get(url)
            elements = driver.find_elements('xpath', locator)
            for element in elements:
                url_next = element.get_attribute('href')
                if not url_next:
                    continue
                if self._is_duplicate_url(category, url_next):
                     continue
                category[url_next] = {
                   'id_category': default_category_id,
                   'children': {}
                 }
                category[url_next]['children'] = await self._crawl_categories(
                    url_next,
                    depth - 1,
                    driver,
                    locator,
                    default_category_id,
                    category[url_next]['children'],
                )
        except Exception as e:
            logger.error(f'Ошибка при рекурсивном обходе категорий: {e}')
        return category


    def _is_duplicate_url(self, category: Dict[str, Any], url: str) -> bool:
        """
        Проверяет, существует ли URL уже в словаре категорий.
        
        :param category: Словарь категорий.
        :type category: dict
        :param url: URL для проверки.
        :type url: str
        :return: `True`, если URL является дубликатом, `False` в противном случае.
        :rtype: bool
        """
        # Код исполняет проверку на дубликат URL
        return url in category

def compare_and_print_missing_keys(current_dict: Dict[str, Any], file_path: str | Path) -> None:
    """
    Сравнивает текущий словарь с данными из файла и выводит любые отсутствующие ключи.
    
    :param current_dict: Словарь для сравнения.
    :type current_dict: dict
    :param file_path: Путь к файлу, содержащему данные для сравнения.
    :type file_path: str | Path
    """
    # Код исполняет сравнение словаря с данными из файла
    try:
        file_data = j_loads(file_path)
    except Exception as e:
        logger.error(f'Не удалось загрузить файл {file_path}: {e}')
        return
    
    if not isinstance(file_data, dict):
        logger.error('Данные в файле не являются словарем')
        return

    missing_keys = []
    for key in file_data:
        if key not in current_dict:
            missing_keys.append(key)
    if missing_keys:
        print(f'Отсутствуют ключи: {missing_keys}')
    else:
        print('Все ключи совпадают')
```