# Модуль category

## Обзор

Модуль `category` предназначен для работы с категориями товаров, в основном для PrestaShop. Он предоставляет классы для взаимодействия и обработки данных категорий товаров.

## Подробнее

Модуль содержит класс `Category`, который наследуется от `PrestaCategoryAsync` и предназначен для асинхронного обхода категорий, построения иерархического словаря, а также проверки наличия дубликатов URL.
Расположение файла: `hypotez/src/scenario/category.py`

## Классы

### `Category`

**Описание**: Обработчик категорий для категорий товаров. Наследуется от `PrestaCategoryAsync`.

**Методы**:
- `__init__`: Инициализирует объект `Category`.
- `crawl_categories_async`: Асинхронно обходит категории, строя иерархический словарь.
- `crawl_categories`: Рекурсивно обходит категории и строит иерархический словарь.
- `_is_duplicate_url`: Проверяет, существует ли URL уже в словаре категорий.

**Параметры**:
- `api_credentials` (Dict): Учетные данные API для доступа к данным категорий.

**Примеры**

```python
from src.category.category import Category
# Предположим, что api_credentials - это словарь с учетными данными API
api_credentials = {'api_key': 'your_api_key', 'api_secret': 'your_api_secret'}
category_handler = Category(api_credentials)
```

## Функции

### `crawl_categories_async`

```python
async def crawl_categories_async(self, url, depth, driver, locator, dump_file, default_category_id, category=None):
    """
    Args:
        url (str): The URL of the category page.
        depth (int): The depth of the crawling recursion.
        driver: The Selenium WebDriver instance.
        locator: The XPath locator for category links.
        dump_file: The path to the JSON file for saving results.
        default_category_id: The default category ID.
        category (Optional[dict], optional): An existing category dictionary (default=None).

    Returns:
        dict: The updated or new category dictionary.

    Raises:
        Exception: An error occurred during category crawling.

    **Как работает функция**:
    1. Проверяет глубину рекурсии. Если глубина <= 0, возвращает текущую категорию.
    2. Получает страницу по URL с помощью Selenium WebDriver.
    3. Ожидает загрузки страницы в течение 1 секунды.
    4. Извлекает ссылки на категории, используя XPath-локатор.
    5. Если ссылки не найдены, логирует ошибку и возвращает текущую категорию.
    6. Создает список задач для асинхронного обхода каждой найденной категории.
    7. Запускает задачи асинхронно и собирает результаты.
    8. Возвращает обновленный словарь категорий.
    """
    ...
```

**Описание**: Асинхронно обходит категории, строя иерархический словарь.

**Параметры**:
- `url` (str): URL страницы категории.
- `depth` (int): Глубина рекурсии обхода.
- `driver`: Экземпляр Selenium WebDriver.
- `locator`: XPath-локатор для ссылок на категории.
- `dump_file` (str): Путь к JSON-файлу для сохранения результатов.
- `default_category_id`: ID категории по умолчанию.
- `category` (Optional[dict], optional): Существующий словарь категорий (по умолчанию `None`).

**Возвращает**:
- `dict`: Обновленный или новый словарь категорий.

**Вызывает исключения**:
- `Exception`: Возникает при ошибке во время обхода категорий.

**Примеры**:

```python
import asyncio
from selenium import webdriver
from src.category.category import Category
from src.utils.webdriver import WebDriver

async def main():
    # Предположим, что api_credentials - это словарь с учетными данными API
    api_credentials = {'api_key': 'your_api_key', 'api_secret': 'your_api_secret'}
    category_handler = Category(api_credentials)
    url = 'https://example.com/categories'
    depth = 2
    dump_file = 'categories.json'
    default_category_id = 1

    driver = WebDriver().get_driver()
    locator = '//a[@class="category-link"]'  # Example XPath locator

    result = await category_handler.crawl_categories_async(url, depth, driver, locator, dump_file, default_category_id)
    print(result)

if __name__ == "__main__":
    asyncio.run(main())
```

### `crawl_categories`

```python
def crawl_categories(self, url, depth, driver, locator, dump_file, default_category_id, category={}):
    """
    Args:
        url (str): URL of the page to crawl.
        depth (int): Depth of recursion.
        driver: Selenium WebDriver instance.
        locator: XPath locator for finding category links.
        dump_file (str): File for saving the hierarchical dictionary.
        id_category_default: Default category ID.
        category (dict, optional): Category dictionary (default is empty).

    Returns:
        dict: Hierarchical dictionary of categories and their URLs.

    Raises:
        Exception: An error occurred during category crawling.

    **Как работает функция**:
    1. Проверяет глубину рекурсии. Если глубина <= 0, возвращает текущую категорию.
    2. Получает страницу по URL с помощью Selenium WebDriver.
    3. Ожидает загрузки страницы в течение 1 секунды.
    4. Извлекает ссылки на категории, используя XPath-локатор.
    5. Если ссылки не найдены, логирует ошибку и возвращает текущую категорию.
    6. Для каждой найденной ссылки проверяет, не является ли URL дубликатом.
    7. Если URL не является дубликатом, создает новый словарь категории и рекурсивно вызывает себя для обхода подкатегорий.
    8. Загружает данные из файла дампа, объединяет с текущей категорией и сохраняет в файл дампа.
    9. Возвращает иерархический словарь категорий.
    """
    ...
```

**Описание**: Рекурсивно обходит категории и строит иерархический словарь.

**Параметры**:
- `url` (str): URL страницы для обхода.
- `depth` (int): Глубина рекурсии.
- `driver`: Экземпляр Selenium WebDriver.
- `locator`: XPath-локатор для поиска ссылок на категории.
- `dump_file` (str): Файл для сохранения иерархического словаря.
- `default_category_id`: ID категории по умолчанию.
- `category` (dict, optional): Словарь категорий (по умолчанию пустой).

**Возвращает**:
- `dict`: Иерархический словарь категорий и их URL.

**Вызывает исключения**:
- `Exception`: Возникает при ошибке во время обхода категорий.

**Примеры**:

```python
from selenium import webdriver
from src.category.category import Category
from src.utils.webdriver import WebDriver

# Предположим, что api_credentials - это словарь с учетными данными API
api_credentials = {'api_key': 'your_api_key', 'api_secret': 'your_api_secret'}
category_handler = Category(api_credentials)
url = 'https://example.com/categories'
depth = 2
dump_file = 'categories.json'
default_category_id = 1

driver = WebDriver().get_driver()
locator = '//a[@class="category-link"]'  # Example XPath locator

result = category_handler.crawl_categories(url, depth, driver, locator, dump_file, default_category_id)
print(result)
```

### `_is_duplicate_url`

```python
def _is_duplicate_url(self, category, url):
    """
    Args:
        category (dict): Category dictionary.
        url (str): URL to check.

    Returns:
        bool: True if the URL is a duplicate, False otherwise.

    **Как работает функция**:
    Проверяет, существует ли URL уже в словаре категорий.
    """
    ...
```

**Описание**: Проверяет, существует ли URL уже в словаре категорий.

**Параметры**:
- `category` (dict): Словарь категорий.
- `url` (str): URL для проверки.

**Возвращает**:
- `bool`: `True`, если URL является дубликатом, `False` в противном случае.

**Примеры**:

```python
from src.category.category import Category

# Предположим, что api_credentials - это словарь с учетными данными API
api_credentials = {'api_key': 'your_api_key', 'api_secret': 'your_api_secret'}
category_handler = Category(api_credentials)
category = {
    'Category1': {'url': 'https://example.com/category1'},
    'Category2': {'url': 'https://example.com/category2'}
}
url_to_check = 'https://example.com/category1'
is_duplicate = category_handler._is_duplicate_url(category, url_to_check)
print(is_duplicate)  # Вывод: True

url_to_check = 'https://example.com/category3'
is_duplicate = category_handler._is_duplicate_url(category, url_to_check)
print(is_duplicate)  # Вывод: False
```

### `compare_and_print_missing_keys`

```python
def compare_and_print_missing_keys(current_dict, file_path):
    """
    Args:
        current_dict (dict): The current dictionary to compare.
        file_path (str): The path to the file containing data to compare with.

    Raises:
        Exception: Error loading data from file

    **Как работает функция**:
    Сравнивает текущий словарь с данными в файле и выводит отсутствующие ключи.
    """
    ...
```

**Описание**: Сравнивает текущий словарь с данными в файле и выводит отсутствующие ключи.

**Параметры**:
- `current_dict` (dict): Текущий словарь для сравнения.
- `file_path` (str): Путь к файлу, содержащему данные для сравнения.

**Вызывает исключения**:
- `Exception`: Возникает при ошибке загрузки данных из файла.

**Примеры**:

```python
from src.category.category import compare_and_print_missing_keys

current_dict = {'key1': 'value1', 'key2': 'value2'}
file_path = 'data.json'  # Файл data.json содержит: {"key2": "value2", "key3": "value3"}

compare_and_print_missing_keys(current_dict, file_path)  # Вывод: key3
```
```output