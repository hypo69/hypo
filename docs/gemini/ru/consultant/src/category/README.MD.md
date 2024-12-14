# Анализ кода модуля src.category

**Качество кода**
7
-  Плюсы
    - Код содержит подробное описание модуля и его классов.
    - Присутствуют описания методов и их параметров.
    - Есть пример использования модуля.
-  Минусы
    - Отсутствуют doctring в коде
    - Не все импорты указаны
    - Использованы стандартные блоки try-except без логирования
    - Не используется `j_loads` для чтения файлов
    - Отсутсвуют комментарии в коде 

**Рекомендации по улучшению**
1.  Добавить docstring к классам и методам в формате reStructuredText.
2.  Использовать `from src.logger.logger import logger` для логирования ошибок.
3.  Заменить стандартные `try-except` на `logger.error`.
4.  Использовать `j_loads` для загрузки json файлов.
5.  Добавить импорты.
6.  Добавить комментарии в коде.
7.  Использовать одинарные кавычки.

**Оптимизированный код**
```python
"""
Модуль для работы с категориями товаров.
=========================================================================================

Этот модуль предоставляет класс :class:`Category`, который наследуется от :class:`PrestaCategory`
и предоставляет функциональность для работы с категориями товаров, включая получение родительских категорий,
асинхронный и синхронный обход страниц категорий.

Пример использования
--------------------

Пример использования класса `Category`:

.. code-block:: python

    from src.category import Category
    from selenium import webdriver
    from src.utils.jjson import j_loads
    from src.logger.logger import logger
    import asyncio

    # Инициализация класса Category с параметрами для API
    category = Category(api_credentials={'api_key': 'your_api_key'})

    # Асинхронный обход категорий
    async def main():
        driver = webdriver.Chrome()
        categories_data = await category.crawl_categories_async(
            url='https://example.com/categories',
            depth=3,
            driver=driver,
            locator='//a[@class="category-link"]',
            dump_file='categories.json',
            default_category_id=123
        )
        driver.quit()
        return categories_data

    if __name__ == "__main__":
        categories_data = asyncio.run(main())
        print(categories_data)

"""
import asyncio
import json
from typing import Any, Dict, List, Optional
# from typing import TYPE_CHECKING

from selenium import webdriver  # Import webdriver
# if TYPE_CHECKING:
#     from selenium.webdriver.remote.webdriver import WebDriver

from src.endpoints.prestashop import PrestaCategory
from src.logger.logger import logger
from src.utils.jjson import j_loads, j_dumps

# from src.utils.jjson import j_loads, j_dumps # Перенес импорты наверх
# from src.logger.logger import logger # Перенес импорты наверх
# from src.endpoints.prestashop import PrestaCategory # Перенес импорты наверх


class Category(PrestaCategory):
    """
    Класс для работы с категориями товаров.

    Наследуется от :class:`PrestaCategory` и предоставляет методы для получения родительских категорий,
    асинхронного и синхронного обхода страниц категорий.
    """

    def __init__(self, api_credentials, *args, **kwargs):
        """
        Инициализирует объект класса Category.

        :param api_credentials: API credentials для доступа к данным категории.
        :param args: Произвольные позиционные аргументы.
        :param kwargs: Произвольные именованные аргументы.
        """
        super().__init__(api_credentials=api_credentials, *args, **kwargs)

    def get_parents(self, id_category: int, dept: int) -> List[Dict[str, Any]]:
        """
        Получает список родительских категорий.

        :param id_category: ID категории, для которой нужно получить родительские категории.
        :param dept: Глубина уровня категории.
        :return: Список родительских категорий.
        """
        parents = []
        _id = id_category
        for _ in range(dept):
            category = self.get_category(_id)
            if category:
                if 'associations' in category and 'categories' in category['associations']:
                    categories = category['associations']['categories']
                    if categories:
                        _id = categories[0]['id']
                        parents.append(category)
                    else:
                        break
                else:
                    break
        return parents

    async def crawl_categories_async(
        self,
        url: str,
        depth: int,
        driver: webdriver.Chrome, # Указал тип webdriver
        locator: str,
        dump_file: str,
        default_category_id: int,
        category: Optional[Dict] = None,
    ) -> Dict:
        """
        Асинхронно обходит страницы категорий, строя иерархический словарь.

        :param url: URL страницы категории.
        :param depth: Глубина рекурсии.
        :param driver: Экземпляр Selenium WebDriver.
        :param locator: XPath-локатор для ссылок на категории.
        :param dump_file: Путь к JSON-файлу для сохранения результатов.
        :param default_category_id: ID категории по умолчанию.
        :param category: Существующий словарь категорий (по умолчанию None).
        :return: Обновленный или новый словарь категорий.
        """
        if category is None:
            category = {}
        if depth <= 0:
            return category
        try:
            # код исполняет переход по URL
            driver.get(url)
        except Exception as ex:
            logger.error(f'Ошибка при переходе по URL {url}', exc_info=ex)
            return category
        try:
            # код исполняет поиск элементов по локатору
            elements = driver.find_elements('xpath', locator)
        except Exception as ex:
            logger.error(f'Ошибка при поиске элементов по локатору {locator} на странице {url}', exc_info=ex)
            return category

        for element in elements:
            try:
                # код исполняет получение URL элемента
                url = element.get_attribute('href')
            except Exception as ex:
                logger.error(f'Ошибка при получении URL элемента {element} на странице {url}', exc_info=ex)
                continue
            # код проверяет, дублируется ли URL
            if self._is_duplicate_url(category, url):
                continue

            category[url] = {
                'url': url,
                'id_category': default_category_id,
                'children': {},
            }

            # код исполняет рекурсивный вызов для дочерних категорий
            category[url]['children'] = await self.crawl_categories_async(
                url,
                depth - 1,
                driver,
                locator,
                dump_file,
                default_category_id,
                category[url]['children'],
            )
        # Код исполняет сохранение данных в файл
        with open(dump_file, 'w', encoding='utf-8') as file:
            json.dump(category, file, indent=4, ensure_ascii=False)
        return category

    def crawl_categories(
        self,
        url: str,
        depth: int,
        driver: webdriver.Chrome, # Указал тип webdriver
        locator: str,
        dump_file: str,
        id_category_default: int,
        category: Dict = None,
    ) -> Dict:
        """
        Рекурсивно обходит страницы категорий и строит иерархический словарь.

        :param url: URL страницы для обхода.
        :param depth: Глубина рекурсии.
        :param driver: Экземпляр Selenium WebDriver.
        :param locator: XPath-локатор для поиска ссылок на категории.
        :param dump_file: Файл для сохранения иерархического словаря.
        :param id_category_default: ID категории по умолчанию.
        :param category: Словарь категорий (по умолчанию пустой).
        :return: Иерархический словарь категорий и их URL.
        """
        if category is None:
            category = {}
        if depth <= 0:
            return category
        try:
            # код исполняет переход по URL
            driver.get(url)
        except Exception as ex:
            logger.error(f'Ошибка при переходе по URL {url}', exc_info=ex)
            return category
        try:
            # код исполняет поиск элементов по локатору
            elements = driver.find_elements('xpath', locator)
        except Exception as ex:
            logger.error(f'Ошибка при поиске элементов по локатору {locator} на странице {url}', exc_info=ex)
            return category
        for element in elements:
            try:
                # код исполняет получение URL элемента
                url = element.get_attribute('href')
            except Exception as ex:
                logger.error(f'Ошибка при получении URL элемента {element} на странице {url}', exc_info=ex)
                continue
            # Код проверяет наличие дубликатов URL
            if self._is_duplicate_url(category, url):
                continue

            category[url] = {
                'url': url,
                'id_category': id_category_default,
                'children': {},
            }
            # код исполняет рекурсивный обход дочерних категорий
            category[url]['children'] = self.crawl_categories(
                url,
                depth - 1,
                driver,
                locator,
                dump_file,
                id_category_default,
                category[url]['children'],
            )
        # Код исполняет сохранение данных в файл
        with open(dump_file, 'w', encoding='utf-8') as file:
            json.dump(category, file, indent=4, ensure_ascii=False)

        return category

    def _is_duplicate_url(self, category: Dict, url: str) -> bool:
        """
        Проверяет, существует ли URL уже в словаре категорий.

        :param category: Словарь категорий.
        :param url: URL для проверки.
        :return: True, если URL дублируется, False в противном случае.
        """
        if url in category:
            return True
        for value in category.values():
            if isinstance(value, dict) and 'children' in value:
                if self._is_duplicate_url(value['children'], url):
                    return True
        return False


def compare_and_print_missing_keys(current_dict: Dict, file_path: str):
    """
    Сравнивает текущий словарь с данными из файла и выводит отсутствующие ключи.

    :param current_dict: Словарь для сравнения.
    :param file_path: Путь к файлу с данными для сравнения.
    """
    try:
        # код исполняет загрузку данных из файла
        with open(file_path, 'r', encoding='utf-8') as f:
            file_data = j_loads(f)
        if not isinstance(file_data, dict):
             logger.error(f'Некорректный формат данных в файле {file_path}')
             return
    except Exception as ex:
        logger.error(f'Ошибка при загрузке файла {file_path}', exc_info=ex)
        return

    def _find_missing_keys(current, file_data, path=''):
        """Рекурсивная функция для поиска отличий."""
        if isinstance(current, dict) and isinstance(file_data, dict):
            for key in file_data:
                new_path = f'{path}.{key}' if path else key
                if key not in current:
                     print(f'Отсутствует ключ {new_path}')
                     continue
                _find_missing_keys(current.get(key), file_data.get(key), new_path)
    # код исполняет поиск отсутствующих ключей
    _find_missing_keys(current_dict, file_data)
```