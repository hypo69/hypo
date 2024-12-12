# Модуль: Category

## Обзор

Модуль `Category` предоставляет функциональность для работы с категориями товаров, в первую очередь для PrestaShop. Он предлагает инструменты для взаимодействия с данными категорий, включая обход страниц категорий и управление иерархической структурой категорий.

## Оглавление

* [Модуль: Category](#модуль-category)
* [Обзор](#обзор)
* [Класс: `Category`](#класс-category)
    * [Конструктор: `__init__(self, api_credentials, *args, **kwargs)`](#конструктор-initself-api_credentials-args-kwargs)
    * [Метод: `get_parents(self, id_category, dept)`](#метод-get_parentsself-id_category-dept)
    * [Метод: `crawl_categories_async(self, url, depth, driver, locator, dump_file, default_category_id, category=None)`](#метод-crawl_categories_asyncself-url-depth-driver-locator-dump_file-default_category_id-categorynone)
    * [Метод: `crawl_categories(self, url, depth, driver, locator, dump_file, id_category_default, category={})`](#метод-crawl_categoriesself-url-depth-driver-locator-dump_file-id_category_default-category)
    * [Метод: `_is_duplicate_url(self, category, url)`](#метод-is_duplicate_urlself-category-url)
* [Функция: `compare_and_print_missing_keys(current_dict, file_path)`](#функция-compare_and_print_missing_keyscurrent_dict-file_path)
* [Пример использования](#пример-использования)
* [Зависимости](#зависимости)


## Класс: `Category`

Класс `Category` наследует от `PrestaCategory` и отвечает за обработку категорий товаров, получение родительских категорий и рекурсивный обход страниц категорий.

### Конструктор: `__init__(self, api_credentials, *args, **kwargs)`

Инициализирует объект `Category`.

#### Аргументы:
- `api_credentials`: Учетные данные API для доступа к данным категорий.  (dict)
- `args`: Список аргументов переменной длины. (не используется)
- `kwargs`: Ключевые аргументы. (не используется)

### Метод: `get_parents(self, id_category, dept)`

Получает список родительских категорий.

#### Аргументы:
- `id_category` (int): ID категории, для которой нужно получить родительские категории.
- `dept` (int): Уровень глубины категории.

#### Возвращает:
- Список родительских категорий (list).

### Метод: `crawl_categories_async(self, url, depth, driver, locator, dump_file, default_category_id, category=None)`

Асинхронно обходит категории, строя иерархический словарь.

#### Аргументы:
- `url` (str): URL страницы категории.
- `depth` (int): Глубина рекурсии обхода.
- `driver` (object): Экземпляр Selenium WebDriver.
- `locator` (str): XPath локатор для ссылок на категории.
- `dump_file` (str): Путь к файлу JSON для сохранения результатов.
- `default_category_id` (int): ID категории по умолчанию.
- `category` (dict, optional): Существующий словарь категории (по умолчанию=None).

#### Возвращает:
- Обновленный или новый словарь категорий (dict).


### Метод: `crawl_categories(self, url, depth, driver, locator, dump_file, id_category_default, category={})`

Рекурсивно обходит категории и строит иерархический словарь.

#### Аргументы:
- `url` (str): URL страницы для обхода.
- `depth` (int): Глубина рекурсии.
- `driver` (object): Экземпляр Selenium WebDriver.
- `locator` (str): XPath локатор для поиска ссылок на категории.
- `dump_file` (str): Файл для сохранения иерархического словаря.
- `id_category_default` (int): ID категории по умолчанию.
- `category` (dict, optional): Словарь категории (по умолчанию пустой).

#### Возвращает:
- Иерархический словарь категорий и их URL (dict).


### Метод: `_is_duplicate_url(self, category, url)`

Проверяет, существует ли URL в словаре категорий.

#### Аргументы:
- `category` (dict): Словарь категорий.
- `url` (str): URL для проверки.

#### Возвращает:
- `True`, если URL является дубликатом, иначе `False`. (bool)


## Функция: `compare_and_print_missing_keys(current_dict, file_path)`

Сравнивает текущий словарь с данными из файла и выводит отсутствующие ключи.

### Аргументы:
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
import asyncio
from selenium import webdriver
# ... (создание driver_instance)
category_data = asyncio.run(category.crawl_categories_async(
    url='https://example.com/categories',
    depth=3,
    driver=driver_instance,
    locator='//a[@class="category-link"]',
    dump_file='categories.json',
    default_category_id=123
))

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