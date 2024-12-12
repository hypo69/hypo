# Модуль: Category

## Обзор

Модуль `Category` предоставляет функциональность для работы с категориями товаров, в первую очередь для PrestaShop. Он предлагает инструменты для взаимодействия с данными категорий, включая обход страниц категорий и управление иерархической структурой категорий.

## Содержание

- [Класс: `Category`](#класс-category)
    - [Конструктор: `__init__`](#конструктор-__init__)
    - [Метод: `get_parents`](#метод-get_parents)
    - [Метод: `crawl_categories_async`](#метод-crawl_categories_async)
    - [Метод: `crawl_categories`](#метод-crawl_categories)
    - [Метод: `_is_duplicate_url`](#метод-_is_duplicate_url)
- [Функция: `compare_and_print_missing_keys`](#функция-compare_and_print_missing_keys)
- [Пример использования](#пример-использования)
- [Зависимости](#зависимости)

## Класс: `Category`

Класс `Category` наследует от `PrestaCategory` и отвечает за обработку категорий товаров, получение родительских категорий и рекурсивный обход страниц категорий.

### Конструктор: `__init__(self, api_credentials, *args, **kwargs)`

Инициализирует объект `Category`.

**Параметры:**
- `api_credentials` (dict): Учетные данные API для доступа к данным категорий.
- `*args`: Список аргументов переменной длины (не используется).
- `**kwargs`: Ключевые аргументы (не используются).

### Метод: `get_parents(self, id_category, dept)`

Получает список родительских категорий.

**Параметры:**
- `id_category` (int): ID категории, для которой нужно получить родительские категории.
- `dept` (int): Уровень глубины категории.

**Возвращает:**
- `list`: Список родительских категорий.

### Метод: `crawl_categories_async(self, url, depth, driver, locator, dump_file, default_category_id, category=None)`

Асинхронно обходит категории, строя иерархический словарь.

**Параметры:**
- `url` (str): URL страницы категории.
- `depth` (int): Глубина рекурсии обхода.
- `driver` (selenium.webdriver.remote.webdriver.WebDriver): Экземпляр Selenium WebDriver.
- `locator` (str): XPath локатор для ссылок на категории.
- `dump_file` (str): Путь к файлу JSON для сохранения результатов.
- `default_category_id` (int): ID категории по умолчанию.
- `category` (dict, optional): Существующий словарь категории. По умолчанию `None`.

**Возвращает:**
- `dict`: Обновленный или новый словарь категорий.

### Метод: `crawl_categories(self, url, depth, driver, locator, dump_file, id_category_default, category={})`

Рекурсивно обходит категории и строит иерархический словарь.

**Параметры:**
- `url` (str): URL страницы для обхода.
- `depth` (int): Глубина рекурсии.
- `driver` (selenium.webdriver.remote.webdriver.WebDriver): Экземпляр Selenium WebDriver.
- `locator` (str): XPath локатор для поиска ссылок на категории.
- `dump_file` (str): Файл для сохранения иерархического словаря.
- `id_category_default` (int): ID категории по умолчанию.
- `category` (dict, optional): Словарь категории. По умолчанию пустой словарь `{}`.

**Возвращает:**
- `dict`: Иерархический словарь категорий и их URL.

### Метод: `_is_duplicate_url(self, category, url)`

Проверяет, существует ли URL в словаре категорий.

**Параметры:**
- `category` (dict): Словарь категорий.
- `url` (str): URL для проверки.

**Возвращает:**
- `bool`: `True`, если URL является дубликатом, иначе `False`.

## Функция: `compare_and_print_missing_keys(current_dict, file_path)`

Сравнивает текущий словарь с данными из файла и выводит отсутствующие ключи.

**Параметры:**
- `current_dict` (dict): Словарь для сравнения.
- `file_path` (str): Путь к файлу, содержащему данные для сравнения.

## Пример использования

```python
from src.category import Category

# Инициализация Category с учетными данными API
category = Category(api_credentials={'api_key': 'your_api_key'})

# Получение родительских категорий
parents = category.get_parents(id_category=123, dept=2)

# Асинхронный обход категорий
category_data = await category.crawl_categories_async(
    url='https://example.com/categories',
    depth=3,
    driver=driver_instance,
    locator='//a[@class="category-link"]',
    dump_file='categories.json',
    default_category_id=123
)

# Сравнение текущих данных категорий с файлом и вывод отсутствующих ключей
compare_and_print_missing_keys(current_dict=category_data, file_path='saved_categories.json')
```

## Зависимости

- `requests`
- `lxml`
- `asyncio`
- `selenium`
- `src.endpoints.prestashop.PrestaShop`
- `src.endpoints.prestashop.PrestaCategory`
- `src.utils.jjson.j_loads`
- `src.utils.jjson.j_dumps`
- `src.logger.logger`