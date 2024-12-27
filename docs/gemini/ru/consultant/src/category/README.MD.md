# Анализ кода модуля src.category

**Качество кода**
9
-  Плюсы
    -  Хорошая структура документации с использованием reStructuredText (RST).
    -  Предоставлено ясное описание класса `Category` и его методов.
    -  Есть пример использования модуля в `Usage Example`.
    -  Указаны зависимости модуля.
    -  Код предоставляет функционал для работы с категориями в PrestaShop.
-  Минусы
    -  Некоторые методы не имеют подробных RST-описаний аргументов и возвращаемых значений.
    -  Не использованы `j_loads` и `j_dumps` в коде.
    -  Отсутствуют обработки ошибок с использованием `logger.error`.
    -  Не указано использование `logger` из `src.logger.logger`.
    -  Не все комментарии в коде соответствуют формату RST.
    -  Некоторые аннотации типов отсутствуют.
    -  Присутствуют общие комментарии, вместо описания конкретных действий.

**Рекомендации по улучшению**

1.  **Документация**:
    - Добавить полное RST-описание для всех функций, методов и аргументов, включая типы данных и возвращаемые значения.
    - Переписать комментарии в коде в формате RST.
2.  **Обработка данных**:
    - Использовать `j_loads` и `j_dumps` из `src.utils.jjson` для чтения и записи файлов.
3.  **Логирование**:
    - Заменить `print` на логирование с использованием `logger.error` и `logger.debug` из `src.logger.logger` для обработки ошибок.
4.  **Импорты**:
    - Добавить отсутствующие импорты.
5.  **Обработка ошибок**:
    - Заменить общие блоки `try-except` на обработку ошибок с использованием `logger.error`.
6.  **Рефакторинг**:
    - Привести в соответствие имена функций, переменных и импортов с ранее обработанными файлами.
    - Избавиться от неиспользуемых аргументов в методах.
7.  **Аннотации типов**:
    - Добавить аннотации типов для аргументов и возвращаемых значений функций.
8. **Комментарии**
    - Заменить общие комментарии на более конкретные.
    - Избегать слов \'получаем\', \'делаем\' и подобных.
9. **Структура**
    - Убрать лишние импорты

**Оптимизированный код**
```python
"""
Модуль для работы с категориями товаров.
=========================================================================================

Этот модуль предоставляет функциональность для взаимодействия с категориями товаров,
включая извлечение иерархической структуры категорий, а также проверку дубликатов URL.

Он использует классы :class:`Category` и методы для работы с PrestaShop.

Пример использования
--------------------

Пример использования класса `Category`:

.. code-block:: python

    from src.category import Category
    from selenium import webdriver

    # Инициализация класса Category
    category_manager = Category(api_credentials={'api_key': 'your_api_key'})

    # Пример вызова метода get_parents
    parents = category_manager.get_parents(id_category=123, dept=2)

    # Пример асинхронного сканирования категорий
    async def main():
        driver = webdriver.Chrome()  # Инициализация драйвера Selenium
        category_data = await category_manager.crawl_categories_async(
            url='https://your-website.com/categories',
            depth=3,
            driver=driver,
            locator='//a[@class="category-link"]',
            dump_file='categories.json',
            default_category_id=123
        )
        driver.quit()

        # Сравнение полученных данных с сохраненными
        compare_and_print_missing_keys(current_dict=category_data, file_path='saved_categories.json')

    if __name__ == "__main__":
        import asyncio
        asyncio.run(main())
"""
import asyncio
from typing import Any, Dict, List, Optional
from selenium import webdriver
from src.endpoints.prestashop.PrestaShop import PrestaShop
from src.endpoints.prestashop.PrestaCategory import PrestaCategory
from src.utils.jjson import j_loads, j_dumps
from src.logger.logger import logger



class Category(PrestaCategory):
    """
    Класс для работы с категориями товаров.

    Наследуется от :class:`PrestaCategory` и предназначен для извлечения
    иерархической структуры категорий и управления данными о категориях.
    """
    def __init__(self, api_credentials: Dict[str, str], *args: Any, **kwargs: Any) -> None:
        """
        Инициализирует объект Category.

        :param api_credentials: API-ключи для доступа к данным.
        :param args: Произвольные аргументы (не используются).
        :param kwargs: Произвольные именованные аргументы (не используются).
        """
        super().__init__(api_credentials=api_credentials, *args, **kwargs)

    def get_parents(self, id_category: int, dept: int) -> List[Dict[str, Any]]:
        """
        Извлекает список родительских категорий.

        :param id_category: ID категории, для которой нужно извлечь родителей.
        :param dept: Глубина иерархии.
        :return: Список родительских категорий.
        """
        try:
            # Код исполняет получение родительских категорий
            parents = self.get_category_parents(id_category=id_category, dept=dept)
            return parents
        except Exception as ex:
            logger.error(f'Ошибка при получении родительских категорий для id {id_category}', exc_info=ex)
            return []

    async def crawl_categories_async(
        self,
        url: str,
        depth: int,
        driver: webdriver.Chrome,
        locator: str,
        dump_file: str,
        default_category_id: int,
        category: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        """
        Асинхронно обходит категории, создавая иерархический словарь.

        :param url: URL страницы с категориями.
        :param depth: Глубина рекурсии сканирования.
        :param driver: Экземпляр Selenium WebDriver.
        :param locator: XPath-локатор для ссылок на категории.
        :param dump_file: Путь к файлу JSON для сохранения результатов.
        :param default_category_id: ID категории по умолчанию.
        :param category: (Optional) Существующий словарь категорий.
        :return: Обновленный или новый словарь категорий.
        """
        category = category if category is not None else {}
        try:
            # Код исполняет рекурсивный обход категорий
            category = await self._crawl_categories_recursive_async(
                url=url,
                depth=depth,
                driver=driver,
                locator=locator,
                default_category_id=default_category_id,
                category=category,
                current_depth=0,
                )
            
            return category
        except Exception as ex:
           logger.error('Ошибка при асинхронном обходе категорий', exc_info=ex)
           return category

    async def _crawl_categories_recursive_async(
        self,
        url: str,
        depth: int,
        driver: webdriver.Chrome,
        locator: str,
        default_category_id: int,
        category: Dict[str, Any],
        current_depth: int
    ) -> Dict[str, Any]:
        """
        Рекурсивно обходит категории и строит иерархический словарь.

        :param url: URL страницы для обхода.
        :param depth: Глубина рекурсии.
        :param driver: Экземпляр Selenium WebDriver.
        :param locator: XPath-локатор для поиска ссылок на категории.
        :param default_category_id: ID категории по умолчанию.
        :param category: Словарь категорий (начинается с пустого).
        :param current_depth: Текущая глубина рекурсии.
        :return: Иерархический словарь категорий и их URL.
        """
        if current_depth >= depth:
            return category

        try:
            # Код исполняет открытие страницы
            driver.get(url)
            # Код исполняет поиск элементов по локатору
            elements = driver.find_elements("xpath", locator)
            
            for element in elements:
                url_element = element.get_attribute("href")
                if url_element and not self._is_duplicate_url(category, url_element):
                    # Код исполняет добавление новой категории
                    category[url_element] = {
                        "id_category": default_category_id,
                        "children": {},
                    }

                    # Код исполняет рекурсивный вызов для вложенных категорий
                    category[url_element]["children"] = await self._crawl_categories_recursive_async(
                        url=url_element,
                        depth=depth,
                        driver=driver,
                        locator=locator,
                        default_category_id=default_category_id,
                        category=category[url_element]["children"],
                        current_depth=current_depth+1
                    )
            return category

        except Exception as ex:
            logger.error(f'Ошибка при обходе категорий по url {url}', exc_info=ex)
            return category

    def crawl_categories(
        self,
        url: str,
        depth: int,
        driver: webdriver.Chrome,
        locator: str,
        dump_file: str,
        id_category_default: int,
        category: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        """
        Обходит категории рекурсивно и строит иерархический словарь.

        :param url: URL страницы для обхода.
        :param depth: Глубина рекурсии.
        :param driver: Экземпляр Selenium WebDriver.
        :param locator: XPath-локатор для поиска ссылок на категории.
        :param dump_file: Файл для сохранения иерархического словаря.
        :param id_category_default: ID категории по умолчанию.
        :param category: Словарь категорий (начинается с пустого).
        :return: Иерархический словарь категорий и их URL.
        """
        category = category if category is not None else {}
        try:
            # Код исполняет рекурсивный обход категорий
            category = self._crawl_categories_recursive(
                url=url,
                depth=depth,
                driver=driver,
                locator=locator,
                id_category_default=id_category_default,
                category=category,
                current_depth=0
            )
            return category

        except Exception as ex:
            logger.error('Ошибка при обходе категорий', exc_info=ex)
            return category
    
    def _crawl_categories_recursive(
        self,
        url: str,
        depth: int,
        driver: webdriver.Chrome,
        locator: str,
        id_category_default: int,
        category: Dict[str, Any],
        current_depth: int
    ) -> Dict[str, Any]:
         """
         Рекурсивно обходит категории и строит иерархический словарь.

         :param url: URL страницы для обхода.
         :param depth: Глубина рекурсии.
         :param driver: Экземпляр Selenium WebDriver.
         :param locator: XPath-локатор для поиска ссылок на категории.
         :param id_category_default: ID категории по умолчанию.
         :param category: Словарь категорий (начинается с пустого).
        :param current_depth: Текущая глубина рекурсии.
         :return: Иерархический словарь категорий и их URL.
         """
         if current_depth >= depth:
            return category

         try:
            # Код исполняет открытие страницы
            driver.get(url)
            # Код исполняет поиск элементов по локатору
            elements = driver.find_elements("xpath", locator)

            for element in elements:
                url_element = element.get_attribute("href")
                if url_element and not self._is_duplicate_url(category, url_element):
                    # Код исполняет добавление новой категории
                    category[url_element] = {
                         "id_category": id_category_default,
                         "children": {},
                     }
                    # Код исполняет рекурсивный вызов для вложенных категорий
                    category[url_element]["children"] = self._crawl_categories_recursive(
                        url=url_element,
                        depth=depth,
                        driver=driver,
                        locator=locator,
                        id_category_default=id_category_default,
                        category=category[url_element]["children"],
                        current_depth=current_depth + 1
                    )
            return category
         except Exception as ex:
             logger.error(f'Ошибка при обходе категорий по url {url}', exc_info=ex)
             return category

    def _is_duplicate_url(self, category: Dict[str, Any], url: str) -> bool:
        """
        Проверяет, существует ли уже такой URL в словаре категорий.

        :param category: Словарь категорий.
        :param url: URL для проверки.
        :return: `True`, если URL является дубликатом, `False` в противном случае.
        """
        return url in category

def compare_and_print_missing_keys(current_dict: Dict[str, Any], file_path: str) -> None:
    """
    Сравнивает текущий словарь с данными из файла и выводит отсутствующие ключи.

    :param current_dict: Словарь для сравнения.
    :param file_path: Путь к файлу с данными для сравнения.
    """
    try:
        # Код исполняет загрузку данных из файла
        with open(file_path, 'r') as f:
           file_data = j_loads(f)

        if not isinstance(file_data, dict):
            logger.error('Данные в файле не являются словарем')
            return

        # Код исполняет сравнение ключей и вывод отсутствующих
        missing_keys = set(file_data.keys()) - set(current_dict.keys())
        if missing_keys:
            logger.debug(f'Отсутствующие ключи: {missing_keys}')
        else:
            logger.debug('Все ключи совпадают')
    except FileNotFoundError:
         logger.error(f'Файл не найден: {file_path}')
    except Exception as ex:
        logger.error(f'Ошибка при сравнении ключей: {ex}', exc_info=ex)

```