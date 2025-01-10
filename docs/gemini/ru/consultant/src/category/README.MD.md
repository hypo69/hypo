# Анализ кода модуля `src.category`

**Качество кода**
9
-  Плюсы
    -   Модуль хорошо документирован с использованием reStructuredText.
    -   Присутствует подробное описание класса и его методов.
    -   Используется асинхронный подход для обхода категорий.
    -   Есть обработка дубликатов URL.
    -   Код структурирован и легко читается.
 -  Минусы
    -  Не хватает обработки ошибок.
    -  Отсутствуют docstring для функций `compare_and_print_missing_keys`.
    -  Используется стандартный `json.load` вместо `j_loads` или `j_loads_ns` из `src.utils.jjson`.
    -  Не указаны импорты в коде.

**Рекомендации по улучшению**

1.  Добавить docstring для функции `compare_and_print_missing_keys`, следуя стандартам reStructuredText.
2.  Использовать `j_loads` или `j_loads_ns` для чтения данных из файлов.
3.  Добавить обработку ошибок с использованием `logger.error`.
4.  Удалить неиспользуемые параметры `*args`, `**kwargs` из метода `__init__`.
5.  Импортировать все необходимые модули, включая `asyncio`, `json`, `Path`.
6.  Добавить проверку типов и валидацию входных данных.
7.  Добавить описание модуля в начале файла.

**Оптимизированный код**

```python
"""
Модуль для работы с категориями продуктов, в основном для PrestaShop.
====================================================================

Этот модуль предоставляет класс :class:`Category`, который наследуется от `PrestaCategory` и
отвечает за управление категориями продуктов, получение родительских категорий
и рекурсивный обход страниц категорий.

Пример использования
--------------------

Пример использования класса `Category`:

.. code-block:: python

    from src.category import Category
    from selenium import webdriver
    from pathlib import Path
    import asyncio

    # Инициализация класса Category с учетными данными API
    category = Category(api_credentials={'api_key': 'your_api_key'})

    # Получение родительских категорий
    parents = category.get_parents(id_category=123, dept=2)

    # Создание экземпляра WebDriver (пример)
    driver = webdriver.Chrome()

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
        # Сравнение текущих данных категорий с данными из файла
        compare_and_print_missing_keys(current_dict=category_data, file_path='saved_categories.json')

    if __name__ == "__main__":
        asyncio.run(main())
        driver.quit()
"""
import asyncio
import json
from pathlib import Path
from typing import Any

from src.endpoints.prestashop import PrestaCategory
from src.logger.logger import logger  # Corrected import
from src.utils.jjson import j_loads, j_dumps  # Corrected import


class Category(PrestaCategory):
    """
    Класс для работы с категориями продуктов.

    Наследуется от PrestaCategory и предоставляет методы для
    получения родительских категорий и обхода страниц категорий.
    """
    def __init__(self, api_credentials, *args, **kwargs):
        """
        Инициализирует объект Category.

        Args:
            api_credentials (dict): Учетные данные API для доступа к данным категорий.
        """
        super().__init__(api_credentials=api_credentials)

    def get_parents(self, id_category: int, dept: int) -> list:
        """
        Возвращает список родительских категорий.

        Args:
            id_category (int): ID категории для получения родительских категорий.
            dept (int): Уровень глубины категории.

        Returns:
            list: Список родительских категорий.
        """
        parents = []
        ...
        return parents

    async def crawl_categories_async(self, url: str, depth: int, driver, locator: str, dump_file: str,
                                     default_category_id: int, category: dict = None) -> dict:
        """
        Асинхронно обходит категории, строя иерархический словарь.

        Args:
            url (str): URL страницы категории.
            depth (int): Глубина рекурсии обхода.
            driver: Экземпляр Selenium WebDriver.
            locator (str): XPath локатор для ссылок на категории.
            dump_file (str): Путь к JSON файлу для сохранения результатов.
            default_category_id (int): ID категории по умолчанию.
            category (dict, optional): Существующий словарь категории (по умолчанию None).

        Returns:
            dict: Обновленный или новый словарь категории.
        """
        if category is None:
            category = {}
        if depth <= 0:
            return category

        try:
           # код исполняет получение списка элементов по локатору
            elements = await driver.find_elements(locator)
        except Exception as ex:
             logger.error(f"Ошибка при получении элементов по локатору {locator}: {ex}")
             return category

        for element in elements:
            try:
                 # код исполняет получение URL из элемента
                url = element.get_attribute('href')
            except Exception as ex:
                logger.error(f"Ошибка при получении атрибута href из элемента: {ex}")
                continue
            if not url:
                continue
                
            if self._is_duplicate_url(category, url):
                continue
            
            # код формирует структуру для категории
            category[url] = {
                'id_category': default_category_id,
                'url': url,
                'children': {}
            }
           # код рекурсивно обходит дочерние категории
            category[url]['children'] = await self.crawl_categories_async(
                url=url,
                depth=depth - 1,
                driver=driver,
                locator=locator,
                dump_file=dump_file,
                default_category_id=default_category_id,
                category=category[url]['children']
            )

        try:
            # Код сохраняет результаты в JSON файл
            await self.save_dump(dump_file, category)

        except Exception as ex:
            logger.error(f"Ошибка при сохранении результатов в файл {dump_file}: {ex}")
        return category

    def crawl_categories(self, url: str, depth: int, driver, locator: str, dump_file: str,
                         id_category_default: int, category: dict = None) -> dict:
        """
        Рекурсивно обходит категории и строит иерархический словарь.

        Args:
            url (str): URL страницы для обхода.
            depth (int): Глубина рекурсии.
            driver: Экземпляр Selenium WebDriver.
            locator (str): XPath локатор для поиска ссылок на категории.
            dump_file (str): Файл для сохранения иерархического словаря.
            id_category_default (int): ID категории по умолчанию.
            category (dict, optional): Словарь категории (по умолчанию пустой).

        Returns:
            dict: Иерархический словарь категорий и их URL.
        """
        if category is None:
             category = {}
        if depth <= 0:
            return category
        
        try:
            # Код получает список элементов
            elements = driver.find_elements(locator)
        except Exception as ex:
            logger.error(f"Ошибка при получении элементов по локатору {locator}: {ex}")
            return category

        for element in elements:
            try:
                 # Код получает URL из элемента
                url = element.get_attribute('href')
            except Exception as ex:
                logger.error(f"Ошибка при получении атрибута href из элемента: {ex}")
                continue
            if not url:
                continue
            
            if self._is_duplicate_url(category, url):
               continue
            
            # Код формирует структуру для категории
            category[url] = {
                'id_category': id_category_default,
                'url': url,
                'children': {}
            }

            # Код рекурсивно обходит дочерние категории
            category[url]['children'] = self.crawl_categories(
                url=url,
                depth=depth - 1,
                driver=driver,
                locator=locator,
                dump_file=dump_file,
                id_category_default=id_category_default,
                category=category[url]['children']
            )
            
        try:
            # Код сохраняет результаты в JSON файл
            self.save_dump(dump_file, category)
        except Exception as ex:
            logger.error(f"Ошибка при сохранении результатов в файл {dump_file}: {ex}")
        return category
    

    def _is_duplicate_url(self, category: dict, url: str) -> bool:
        """
        Проверяет, существует ли URL уже в словаре категорий.

        Args:
            category (dict): Словарь категории.
            url (str): URL для проверки.

        Returns:
            bool: True, если URL является дубликатом, False в противном случае.
        """
        if url in category:
            return True
        for key, value in category.items():
          if 'children' in value and self._is_duplicate_url(value['children'], url):
              return True
        return False

    async def save_dump(self, file_path: str | Path, data: dict) -> bool:
        """
        Асинхронно сохраняет данные в файл JSON.

        Args:
            file_path (str | Path): Путь к файлу для сохранения.
            data (dict): Данные для записи.

        Returns:
            bool: True, если файл успешно сохранен, False в противном случае.
        Raises:
            Exception: При возникновении ошибки при записи в файл.
        """
        try:
            # Код преобразует данные в JSON строку
            json_data = j_dumps(data)
            
            # Код открывает файл и записывает данные
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(json_data)
            return True
        except Exception as ex:
            logger.error(f"Ошибка при сохранении в файл {file_path}: {ex}")
            return False

def compare_and_print_missing_keys(current_dict: dict, file_path: str | Path) -> None:
    """
    Сравнивает текущий словарь с данными из файла и выводит отсутствующие ключи.

    Args:
        current_dict (dict): Словарь для сравнения.
        file_path (str | Path): Путь к файлу, содержащему данные для сравнения.

    Returns:
        None
    """
    try:
        # Код загружает данные из файла
        with open(file_path, 'r', encoding='utf-8') as f:
             file_data = j_loads(f)
    except FileNotFoundError:
         logger.error(f"Файл {file_path} не найден")
         return
    except Exception as ex:
         logger.error(f"Ошибка при чтении файла {file_path}: {ex}")
         return

    if not isinstance(file_data, dict):
        logger.error(f"Ожидается словарь, получен {type(file_data)} из файла {file_path}")
        return

    def _compare_recursive(current: dict, file_data: dict, parent_key: str = None):
        """Рекурсивно сравнивает словари и находит отсутствующие ключи"""
        for key, value in file_data.items():
            if key not in current:
                full_key = f"{parent_key}.{key}" if parent_key else key
                print(f"Отсутствует ключ: {full_key}")
                continue
            if isinstance(value, dict) and isinstance(current.get(key), dict):
                _compare_recursive(current.get(key), value, key)
            elif isinstance(value, dict) and not isinstance(current.get(key), dict):
                 full_key = f"{parent_key}.{key}" if parent_key else key
                 print(f"Тип данных ключа '{full_key}' в файле - словарь, а в текущем - {type(current.get(key))}")


    _compare_recursive(current_dict, file_data)
```