# Модуль `category`

## Обзор

Модуль `category` предназначен для работы с категориями товаров, в основном для платформы PrestaShop. Он предоставляет классы и функции для сбора, обработки и организации данных о категориях.

## Подробней

Модуль содержит класс `Category`, который наследуется от `PrestaCategoryAsync` и предоставляет методы для рекурсивного обхода категорий, построения иерархических структур данных и сохранения результатов в файл. Модуль использует библиотеки `lxml`, `requests` и `Selenium` для сбора данных с веб-страниц. Для работы с данными используются `j_loads` и `j_dumps` из модуля `src.utils.jjson`.

## Классы

### `Category`

**Описание**: Класс `Category` является обработчиком категорий товаров. Он наследуется от `PrestaCategoryAsync` и предоставляет методы для работы с иерархией категорий.

**Как работает класс**:
1.  При инициализации класса создается объект `Category`, который принимает учетные данные API для доступа к данным категорий.
2.  Метод `crawl_categories_async` используется для асинхронного обхода категорий и построения иерархического словаря.
3.  Метод `crawl_categories` выполняет аналогичную задачу, но в синхронном режиме.
4.  Метод `_is_duplicate_url` проверяет, существует ли URL-адрес в словаре категорий.

**Методы**:

*   `__init__(self, api_credentials, *args, **kwargs)`: Инициализирует объект `Category`.
*   `crawl_categories_async(self, url, depth, driver, locator, dump_file, default_category_id, category=None)`: Асинхронно обходит категории, строя иерархический словарь.
*   `crawl_categories(self, url, depth, driver, locator, dump_file, default_category_id, category={})`: Обходит категории рекурсивно и строит иерархический словарь.
*   `_is_duplicate_url(self, category, url)`: Проверяет, существует ли URL-адрес в словаре категорий.

**Параметры**:

*   `api_credentials` (Dict): Учетные данные API для доступа к данным категорий.
*   `url` (str): URL-адрес страницы для обхода.
*   `depth` (int): Глубина рекурсии.
*   `driver` (selenium.webdriver): Экземпляр Selenium WebDriver.
*   `locator` (str): XPath-локатор для поиска ссылок на категории.
*   `dump_file` (str): Путь к файлу для сохранения иерархического словаря.
*   `default_category_id` (int): ID категории по умолчанию.
*   `category` (Dict, optional): Словарь категорий (по умолчанию пустой).
*   `args`: Variable length argument list (unused).
*   `kwargs`: Keyword arguments (unused).

**Примеры**

```python
# Пример инициализации класса Category
api_credentials = {'api_key': 'your_api_key', 'api_url': 'your_api_url'}
category_handler = Category(api_credentials)
```

## Функции

### `crawl_categories_async`

```python
async def crawl_categories_async(self, url, depth, driver, locator, dump_file, default_category_id, category=None):
    """Asynchronously crawls categories, building a hierarchical dictionary.

    :param url: The URL of the category page.
    :param depth: The depth of the crawling recursion.
    :param driver: The Selenium WebDriver instance.
    :param locator: The XPath locator for category links.
    :param dump_file: The path to the JSON file for saving results.
    :param default_category_id: The default category ID.
    :param category: (Optional) An existing category dictionary (default=None).
    :returns: The updated or new category dictionary.
    """
    ...
```

**Описание**: Асинхронно обходит категории, строя иерархический словарь.

**Как работает функция**:

1.  Проверяет глубину рекурсии. Если глубина равна или меньше 0, возвращает текущий словарь категорий.
2.  Получает HTML-код страницы по заданному URL с использованием Selenium WebDriver.
3.  Извлекает ссылки на категории с использованием XPath-локатора.
4.  Если ссылки не найдены, регистрирует ошибку и возвращает текущий словарь категорий.
5.  Создает список задач для асинхронного обхода каждой категории.
6.  Ожидает завершения всех задач с использованием `asyncio.gather`.
7.  Возвращает обновленный словарь категорий.

**Параметры**:

*   `url` (str): URL-адрес страницы для обхода.
*   `depth` (int): Глубина рекурсии.
*   `driver` (selenium.webdriver): Экземпляр Selenium WebDriver.
*   `locator` (str): XPath-локатор для поиска ссылок на категории.
*   `dump_file` (str): Путь к файлу для сохранения результатов.
*   `default_category_id` (int): ID категории по умолчанию.
*   `category` (Dict, optional): Словарь категорий (по умолчанию `None`).

**Возвращает**:

*   `Dict`: Обновленный словарь категорий.

**Вызывает исключения**:

*   `Exception`: Если возникает ошибка во время обхода категорий.

**Примеры**:

```python
# Пример вызова функции crawl_categories_async
import asyncio
from selenium import webdriver
from src.category.category import Category

async def main():
    api_credentials = {'api_key': 'your_api_key', 'api_url': 'your_api_url'}
    category_handler = Category(api_credentials)
    url = 'https://example.com/categories'
    depth = 2
    driver = webdriver.Chrome()
    locator = '//a[@class="category-link"]'
    dump_file = 'categories.json'
    default_category_id = 1

    result = await category_handler.crawl_categories_async(url, depth, driver, locator, dump_file, default_category_id)
    print(result)

    driver.quit()

if __name__ == "__main__":
    asyncio.run(main())
```

### `crawl_categories`

```python
def crawl_categories(self, url, depth, driver, locator, dump_file, default_category_id, category={}):
    """
    Crawls categories recursively and builds a hierarchical dictionary.

    :param url: URL of the page to crawl.
    :param depth: Depth of recursion.
    :param driver: Selenium WebDriver instance.
    :param locator: XPath locator for finding category links.
    :param dump_file: File for saving the hierarchical dictionary.
    :param id_category_default: Default category ID.
    :param category: Category dictionary (default is empty).
    :return: Hierarchical dictionary of categories and their URLs.
    """
    ...
```

**Описание**: Рекурсивно обходит категории и строит иерархический словарь.

**Как работает функция**:

1.  Проверяет глубину рекурсии. Если глубина равна или меньше 0, возвращает текущий словарь категорий.
2.  Получает HTML-код страницы по заданному URL с использованием Selenium WebDriver.
3.  Извлекает ссылки на категории с использованием XPath-локатора.
4.  Если ссылки не найдены, регистрирует ошибку и возвращает текущий словарь категорий.
5.  Для каждой найденной ссылки создает новый словарь категорий и рекурсивно вызывает `crawl_categories` для обхода подкатегорий.
6.  Сохраняет иерархический словарь в файл с использованием `j_dumps`.

**Параметры**:

*   `url` (str): URL-адрес страницы для обхода.
*   `depth` (int): Глубина рекурсии.
*   `driver` (selenium.webdriver): Экземпляр Selenium WebDriver.
*   `locator` (str): XPath-локатор для поиска ссылок на категории.
*   `dump_file` (str): Путь к файлу для сохранения результатов.
*   `default_category_id` (int): ID категории по умолчанию.
*   `category` (Dict, optional): Словарь категорий (по умолчанию `{}`).

**Возвращает**:

*   `Dict`: Иерархический словарь категорий.

**Вызывает исключения**:

*   `Exception`: Если возникает ошибка во время обхода категорий или при работе с файлом.

**Примеры**:

```python
# Пример вызова функции crawl_categories
from selenium import webdriver
from src.category.category import Category

api_credentials = {'api_key': 'your_api_key', 'api_url': 'your_api_url'}
category_handler = Category(api_credentials)
url = 'https://example.com/categories'
depth = 2
driver = webdriver.Chrome()
locator = '//a[@class="category-link"]'
dump_file = 'categories.json'
default_category_id = 1

result = category_handler.crawl_categories(url, depth, driver, locator, dump_file, default_category_id)
print(result)

driver.quit()
```

### `_is_duplicate_url`

```python
def _is_duplicate_url(self, category, url):
    """
    Checks if a URL already exists in the category dictionary.

    :param category: Category dictionary.
    :param url: URL to check.
    :return: True if the URL is a duplicate, False otherwise.
    """
    ...
```

**Описание**: Проверяет, существует ли URL-адрес в словаре категорий.

**Как работает функция**:

1.  Проходит по всем значениям в словаре `category`.
2.  Для каждого значения проверяет, совпадает ли URL-адрес с заданным.
3.  Если совпадение найдено, возвращает `True`.
4.  Если совпадений не найдено, возвращает `False`.

**Параметры**:

*   `category` (Dict): Словарь категорий.
*   `url` (str): URL-адрес для проверки.

**Возвращает**:

*   `bool`: `True`, если URL-адрес является дубликатом, `False` в противном случае.

**Примеры**:

```python
# Пример вызова функции _is_duplicate_url
from src.category.category import Category

api_credentials = {'api_key': 'your_api_key', 'api_url': 'your_api_url'}
category_handler = Category(api_credentials)
category = {
    'Category1': {'url': 'https://example.com/category1'},
    'Category2': {'url': 'https://example.com/category2'}
}
url = 'https://example.com/category1'

result = category_handler._is_duplicate_url(category, url)
print(result)  # Вывод: True
```

### `compare_and_print_missing_keys`

```python
def compare_and_print_missing_keys(current_dict, file_path):
    """
    Compares current dictionary with data in a file and prints missing keys.
    """
    ...
```

**Описание**: Сравнивает текущий словарь с данными в файле и печатает отсутствующие ключи.

**Как работает функция**:

1.  Загружает данные из файла с использованием `j_loads`.
2.  Проходит по всем ключам в загруженных данных.
3.  Для каждого ключа проверяет, существует ли он в текущем словаре.
4.  Если ключ отсутствует в текущем словаре, выводит его на экран.

**Параметры**:

*   `current_dict` (Dict): Текущий словарь для сравнения.
*   `file_path` (str): Путь к файлу с данными для сравнения.

**Возвращает**:

*   `None`

**Вызывает исключения**:

*   `Exception`: Если возникает ошибка при загрузке данных из файла.

**Примеры**:

```python
# Пример вызова функции compare_and_print_missing_keys
from src.category.category import compare_and_print_missing_keys

current_dict = {'key1': 'value1', 'key2': 'value2'}
file_path = 'data.json'  # Предполагается, что data.json содержит {"key1": "value1", "key3": "value3"}

compare_and_print_missing_keys(current_dict, file_path)  # Вывод: key3