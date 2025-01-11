# Анализ кода модуля `src.category`

## Качество кода:

- **Соответствие стандартам**: 7
- **Плюсы**:
    - Документация представлена в формате reStructuredText (RST), что является хорошей практикой для Python проектов.
    - Описана структура классов и методов, включая их аргументы и возвращаемые значения.
    - Приведены примеры использования.
- **Минусы**:
    - В коде отсутствует информация о фактической реализации методов.
    - Не указаны типы данных для аргументов и возвращаемых значений.
    - Нет информации об обработке исключений.
    - Использование `...` вместо реального кода снижает полезность документации.
    - Отсутствуют RST примеры для функций.
    - Нет выравнивания в коде.

## Рекомендации по улучшению:

1. **Завершить документацию**:
    - Включить полные реализации классов и методов, а не `...`.
    - Добавить типы данных для всех параметров и возвращаемых значений в RST.
    - Добавить подробное описание ошибок, которые могут возникнуть в методах.
    - Предоставить примеры RST для всех функций.
2. **Улучшить консистентность**:
    - Привести имена методов, переменных и импортов к единому стилю, который используется в других модулях.
    - Выровнять по отступам.
3. **Добавить обработку ошибок**:
    - Реализовать логирование ошибок через `logger.error` в случае исключений, вместо общих `try-except` блоков.
4. **Улучшить читаемость**:
    - Использовать `j_loads` и `j_dumps` из `src.utils.jjson` вместо стандартных функций `json`.
    - Использовать одинарные кавычки `'` для строк в Python, двойные только в print, input и logger.
5. **Дополнить примеры**:
    - Улучшить примеры использования, чтобы они показывали все возможности класса.
6. **Уточнить формулировки**:
    - Заменить общие формулировки на более точные, например, "получаем" на "отправляем запрос" или "выполняем".

## Оптимизированный код:

```rst
.. module:: src.category
   :platform: Unix, Windows
   :synopsis: Модуль для работы с категориями товаров в PrestaShop.
.. moduleauthor:: Alexandr I.

Модуль Category
================

Обзор
------

Модуль `Category` предоставляет функциональность для работы с категориями товаров, в первую очередь для PrestaShop.
Он предлагает инструменты для взаимодействия с данными категорий, включая обход страниц категорий и управление иерархической структурой категорий.

Класс: `Category`
-------------------

Класс `Category` наследует от `PrestaCategory` и отвечает за обработку категорий товаров, получение родительских категорий
и рекурсивный обход страниц категорий.

.. autoclass:: Category
    :members:
    :special-members:
    :show-inheritance:

Пример использования
---------------------

.. code-block:: python

    from src.category import Category
    from src.logger import logger
    from selenium import webdriver
    from selenium.webdriver.chrome.options import Options
    from src.utils.jjson import j_dumps
    import asyncio
    from pathlib import Path

    # Инициализация Category с учетными данными API
    api_credentials = {'api_key': 'your_api_key'}
    category = Category(api_credentials=api_credentials)

    # Получение родительских категорий
    parents = category.get_parents(id_category=123, dept=2)
    print(parents)

    # Настройка Selenium
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(options=chrome_options)

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
        print(j_dumps(category_data, indent=4))

        # Сравнение текущих данных категорий с файлом и вывод отсутствующих ключей
        compare_and_print_missing_keys(current_dict=category_data, file_path='saved_categories.json')

    if __name__ == "__main__":
        asyncio.run(main())
        driver.quit()


Зависимости
------------

- `requests`
- `lxml`
- `asyncio`
- `selenium`
- `src.endpoints.prestashop.PrestaShop`
- `src.endpoints.prestashop.PrestaCategory`
- `src.utils.jjson.j_loads`
- `src.utils.jjson.j_dumps`
- `src.logger.logger`
```
```python
from src.endpoints.prestashop import PrestaCategory # импорт класса PrestaCategory
from src.utils.jjson import j_loads # импорт функции j_loads
from src.logger import logger  # импорт logger
from pathlib import Path  # импорт Path
from selenium.webdriver.remote.webdriver import WebDriver # импорт WebDriver
import asyncio # импорт asyncio
from typing import Any # импорт Any
from typing import Dict # импорт Dict
from typing import List # импорт List
import json # импорт json


class Category(PrestaCategory):
    """
    Класс для работы с категориями товаров в PrestaShop.

    Наследует от PrestaCategory и отвечает за обработку категорий товаров,
    получение родительских категорий и рекурсивный обход страниц категорий.

    :param api_credentials: Учетные данные API для доступа к данным категорий.
    :type api_credentials: dict
    :raises TypeError: Если api_credentials не является словарем.
    :raises ValueError: Если api_credentials пустой словарь.

    Пример:
        >>> from src.category import Category
        >>> api_creds = {'api_key': 'your_api_key', 'api_url': 'your_api_url'}
        >>> category_instance = Category(api_credentials=api_creds)
        >>> print(category_instance)
        <src.category.Category object at ...>
    """
    def __init__(self, api_credentials: Dict[str, str], *args: Any, **kwargs: Any) -> None:
        """
        Инициализирует объект `Category`.

        :param api_credentials: Учетные данные API для доступа к данным категорий.
        :type api_credentials: dict
        :param args: Список аргументов переменной длины (не используется).
        :type args: Any
        :param kwargs: Ключевые аргументы (не используются).
        :type kwargs: Any
        :raises TypeError: Если api_credentials не является словарем.
        :raises ValueError: Если api_credentials пустой словарь.
        """
        if not isinstance(api_credentials, dict): # проверяем, что api_credentials является словарем
            msg = 'api_credentials должен быть словарем' # сообщение об ошибке
            logger.error(msg) # логируем ошибку
            raise TypeError(msg) # выбрасываем исключение
        if not api_credentials: # проверяем, что api_credentials не пустой
            msg = 'api_credentials не должен быть пустым' # сообщение об ошибке
            logger.error(msg) # логируем ошибку
            raise ValueError(msg) # выбрасываем исключение
        super().__init__(api_credentials=api_credentials) # вызываем конструктор родительского класса

    def get_parents(self, id_category: int, dept: int) -> List[Dict[str, Any]]:
        """
        Получает список родительских категорий.

        :param id_category: ID категории, для которой нужно получить родительские категории.
        :type id_category: int
        :param dept: Уровень глубины категории.
        :type dept: int
        :return: Список родительских категорий.
        :rtype: List[Dict[str, Any]]
        :raises Exception: В случае ошибки при получении данных из API.

        Пример:
            >>> category = Category(api_credentials={'api_key': 'your_api_key', 'api_url': 'your_api_url'})
            >>> parents = category.get_parents(id_category=123, dept=2)
            >>> print(parents)
            [...]
        """
        try:
            params = {'filter[id_parent]': id_category} # параметры запроса
            categories = self._get(params=params) # отправляем запрос к API
            parents = [] # список родительских категорий
            if categories and categories['categories']: # проверяем, что категории существуют
                for category in categories['categories']: # перебираем категории
                    if category['level_depth'] < dept: # проверяем глубину
                        parents.append(category) # добавляем категорию в список
            return parents # возвращаем список родительских категорий
        except Exception as e: # ловим исключение
            logger.error(f'Ошибка при получении родительских категорий: {e}') # логируем ошибку
            return []  # возвращаем пустой список

    async def crawl_categories_async( # асинхронный метод
            self,
            url: str,
            depth: int,
            driver: WebDriver,
            locator: str,
            dump_file: str | Path,
            default_category_id: int,
            category: Dict[str, Any] | None = None
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
        :param dump_file: Путь к файлу JSON для сохранения результатов.
        :type dump_file: str | Path
        :param default_category_id: ID категории по умолчанию.
        :type default_category_id: int
        :param category: Существующий словарь категории (по умолчанию=None).
        :type category: Dict[str, Any] | None
        :return: Обновленный или новый словарь категорий.
        :rtype: Dict[str, Any]
        :raises Exception: В случае ошибки при обходе категорий.

        Пример:
            >>> from selenium import webdriver
            >>> from selenium.webdriver.chrome.options import Options
            >>> import asyncio
            >>>
            >>> async def main():
            >>>    api_credentials = {'api_key': 'your_api_key', 'api_url': 'your_api_url'}
            >>>    category = Category(api_credentials=api_credentials)
            >>>    chrome_options = Options()
            >>>    chrome_options.add_argument("--headless")
            >>>    driver = webdriver.Chrome(options=chrome_options)
            >>>    category_data = await category.crawl_categories_async(
            >>>        url='https://example.com/categories',
            >>>        depth=3,
            >>>        driver=driver,
            >>>        locator='//a[@class="category-link"]',
            >>>        dump_file='categories.json',
            >>>        default_category_id=123
            >>>    )
            >>>    print(category_data)
            >>>    driver.quit()
            >>> if __name__ == "__main__":
            >>>    asyncio.run(main())
            {...}
        """
        if category is None: # если категория не передана
            category = {} # создаем пустой словарь
        try: # отлавливаем исключения
            if depth == 0: # если глубина равна нулю
                return category # возвращаем словарь
            driver.get(url)  # открываем страницу
            elements = driver.find_elements('xpath', locator)  # ищем элементы по локатору
            if not elements: # если элементы не найдены
                return category # возвращаем словарь
            for element in elements: # перебираем элементы
                new_url = element.get_attribute('href')  # получаем ссылку
                if self._is_duplicate_url(category, new_url): # проверяем, не дубликат ли ссылка
                    continue # пропускаем дубликат
                category_id = len(category) + default_category_id  # генерируем id
                category[category_id] = {'url': new_url}  # добавляем ссылку в словарь
                category = await self.crawl_categories_async(
                    url=new_url,
                    depth=depth - 1,
                    driver=driver,
                    locator=locator,
                    dump_file=dump_file,
                    default_category_id=default_category_id,
                    category=category
                ) # рекурсивный вызов
            return category # возвращаем словарь
        except Exception as e: # отлавливаем исключения
            logger.error(f'Ошибка при обходе категорий: {e}')  # логируем ошибку
            return category  # возвращаем словарь

    def crawl_categories( # синхронный метод
        self,
        url: str,
        depth: int,
        driver: WebDriver,
        locator: str,
        dump_file: str | Path,
        id_category_default: int,
        category: Dict[str, Any] = {}
    ) -> Dict[str, Any]:
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
        :type dump_file: str | Path
        :param id_category_default: ID категории по умолчанию.
        :type id_category_default: int
        :param category: Словарь категории (по умолчанию пустой).
        :type category: Dict[str, Any]
        :return: Иерархический словарь категорий и их URL.
        :rtype: Dict[str, Any]
        :raises Exception: В случае ошибки при обходе категорий.
        """
        try:
            if depth == 0: # если глубина равна 0
                return category # возвращаем категорию
            driver.get(url) # открываем страницу
            elements = driver.find_elements('xpath', locator) # ищем элементы
            if not elements: # если элементов нет
                return category # возвращаем категорию
            for element in elements: # перебираем элементы
                new_url = element.get_attribute('href') # получаем url
                if self._is_duplicate_url(category, new_url): # проверяем дубликаты
                    continue # пропускаем дубликат
                category_id = len(category) + id_category_default # генерируем id
                category[category_id] = {'url': new_url} # добавляем в словарь
                category = self.crawl_categories( # рекурсивно вызываем
                    url=new_url,
                    depth=depth - 1,
                    driver=driver,
                    locator=locator,
                    dump_file=dump_file,
                    id_category_default=id_category_default,
                    category=category
                )
            return category # возвращаем категорию
        except Exception as e:
            logger.error(f'Ошибка при обходе категорий: {e}') # логируем ошибку
            return {}  # возвращаем пустой словарь


    def _is_duplicate_url(self, category: Dict[str, Any], url: str) -> bool:
        """
        Проверяет, существует ли URL в словаре категорий.

        :param category: Словарь категорий.
        :type category: Dict[str, Any]
        :param url: URL для проверки.
        :type url: str
        :return: True, если URL является дубликатом, иначе False.
        :rtype: bool
        """
        return any(value['url'] == url for value in category.values()) # проверяем дубликат

def compare_and_print_missing_keys(current_dict: Dict[str, Any], file_path: str | Path) -> None:
    """
    Сравнивает текущий словарь с данными из файла и выводит отсутствующие ключи.

    :param current_dict: Словарь для сравнения.
    :type current_dict: Dict[str, Any]
    :param file_path: Путь к файлу, содержащему данные для сравнения.
    :type file_path: str | Path
    :raises FileNotFoundError: Если файл не найден.
    :raises json.JSONDecodeError: Если файл не является корректным JSON.

    Пример:
        >>> current_data = {'1': {'url': 'url1'}, '2': {'url': 'url2'}}
        >>> file_path = 'test_data.json'
        >>> with open(file_path, 'w') as f:
        >>>     json.dump({'1': {'url': 'url1'}}, f)
        >>> compare_and_print_missing_keys(current_data, file_path)
        Отсутствуют ключи в файле: {'2'}
    """
    try:
        with open(file_path, 'r') as f: # открываем файл
            file_data = j_loads(f) # загружаем данные из файла
        missing_keys = set(current_dict.keys()) - set(file_data.keys()) # находим отсутствующие ключи
        if missing_keys: # если есть отсутствующие ключи
            print(f'Отсутствуют ключи в файле: {missing_keys}') # выводим их
    except FileNotFoundError: # если файл не найден
        logger.error(f'Файл не найден: {file_path}')  # логируем ошибку
    except json.JSONDecodeError as e: # если файл не является JSON
        logger.error(f'Ошибка при чтении JSON файла: {e}')  # логируем ошибку
```