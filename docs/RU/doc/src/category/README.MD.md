# Модуль: `src.category`

## Обзор

Модуль `src.category` предоставляет функциональность для работы с категориями продуктов, в основном для PrestaShop. Он предлагает инструменты для взаимодействия с данными о категориях, включая сканирование страниц категорий и управление иерархическими структурами категорий.

## Оглавление

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

Класс `Category` наследуется от `PrestaCategory` и отвечает за обработку категорий продуктов, получение родительских категорий и рекурсивное сканирование страниц категорий.

### Конструктор: `__init__`

Инициализирует объект `Category`.

**Параметры**:

- `api_credentials` (dict): API-ключи для доступа к данным категории.
- `*args`: Список неименованных аргументов (не используется).
- `**kwargs`: Словарь именованных аргументов (не используется).

### Метод: `get_parents`

Получает список родительских категорий.

**Параметры**:

- `id_category` (int): ID категории, для которой нужно получить родительские категории.
- `dept` (int): Глубина категории.

**Возвращает**:

- `list`: Список родительских категорий.

### Метод: `crawl_categories_async`

Асинхронно сканирует категории, создавая иерархический словарь.

**Параметры**:

- `url` (str): URL страницы категории.
- `depth` (int): Глубина рекурсии сканирования.
- `driver` (selenium.webdriver): Экземпляр Selenium WebDriver.
- `locator` (str): XPath-локатор для ссылок на категории.
- `dump_file` (str): Путь к JSON-файлу для сохранения результатов.
- `default_category_id` (int): ID категории по умолчанию.
- `category` (Optional[dict]): Существующий словарь категорий (по умолчанию `None`).

**Возвращает**:

- `dict`: Обновленный или новый словарь категорий.

### Метод: `crawl_categories`

Рекурсивно сканирует категории и строит иерархический словарь.

**Параметры**:

- `url` (str): URL страницы для сканирования.
- `depth` (int): Глубина рекурсии.
- `driver` (selenium.webdriver): Экземпляр Selenium WebDriver.
- `locator` (str): XPath-локатор для поиска ссылок на категории.
- `dump_file` (str): Файл для сохранения иерархического словаря.
- `id_category_default` (int): ID категории по умолчанию.
- `category` (dict): Словарь категорий (по умолчанию пустой).

**Возвращает**:

- `dict`: Иерархический словарь категорий и их URL-адресов.

### Метод: `_is_duplicate_url`

Проверяет, существует ли URL-адрес в словаре категорий.

**Параметры**:

- `category` (dict): Словарь категорий.
- `url` (str): URL-адрес для проверки.

**Возвращает**:

- `bool`: `True`, если URL-адрес является дубликатом, `False` в противном случае.

## Функция: `compare_and_print_missing_keys`

Сравнивает текущий словарь с данными из файла и печатает отсутствующие ключи.

**Параметры**:

- `current_dict` (dict): Словарь для сравнения.
- `file_path` (str): Путь к файлу, содержащему данные для сравнения.

## Пример использования

```python
from src.category import Category

# Инициализация Category с учетными данными API
category = Category(api_credentials={'api_key': 'your_api_key'})

# Получение родительских категорий
parents = category.get_parents(id_category=123, dept=2)

# Асинхронное сканирование категорий
category_data = await category.crawl_categories_async(
    url='https://example.com/categories',
    depth=3,
    driver=driver_instance,
    locator='//a[@class="category-link"]',
    dump_file='categories.json',
    default_category_id=123
)

# Сравнение текущих данных о категориях с файлом и вывод отсутствующих ключей
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