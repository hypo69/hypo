# Модуль `hypotez/src/category/category.py`

## Обзор

Модуль `src.category` предназначен для работы с категориями, в основном для платформы PrestaShop. Он предоставляет классы и функции для получения родительских категорий, а также для асинхронного и синхронного обхода категорий на сайте и построения иерархического словаря категорий.

## Классы

### `Category`

**Описание**: Класс `Category` расширяет функциональность класса `PrestaCategory`, предоставляя методы для работы с категориями товаров на платформе PrestaShop.

**Атрибуты**:

- `credentials`: Словарь, содержащий данные для аутентификации.

**Методы**:

#### `__init__`

**Описание**: Инициализирует объект `Category`.

**Параметры**:

- `api_credentials`: Словарь с данными для доступа к API.
- `*args`: Переменное количество позиционных аргументов.
- `**kwargs`: Переменное количество именованных аргументов.


#### `get_parents`

**Описание**: Получает список родительских категорий для заданной категории по ID.

**Параметры**:

- `id_category` (int): ID категории.
- `dept` (int): Глубина категории.

**Возвращает**:

- `list`: Список родительских категорий.


#### `crawl_categories_async`

**Описание**: Асинхронно обходит категории на сайте и строит иерархический словарь.

**Параметры**:

- `url` (str): URL страницы для обхода.
- `depth` (int): Глубина рекурсии.
- `driver`: Экземпляр Selenium WebDriver.
- `locator` (str): Xpath локатор для поиска ссылок на категории.
- `dump_file` (str): Путь к файлу для сохранения словаря.
- `id_category_default` (int): ID категории по умолчанию.
- `category` (dict, optional): Словарь, представляющий категорию (по умолчанию `None`).

**Возвращает**:

- `dict`: Иерархический словарь, представляющий категории и их URL.

**Обрабатываемые исключения**:

- `Exception`: Обработка любых исключений, возникающих при обходе.


#### `crawl_categories`

**Описание**: Синхронно обходит категории на сайте и строит иерархический словарь.

**Параметры**:

- `url` (str): URL страницы для обхода.
- `depth` (int): Глубина рекурсии.
- `driver`: Экземпляр Selenium WebDriver.
- `locator` (str): Xpath локатор для поиска ссылок на категории.
- `dump_file` (str): Путь к файлу для сохранения словаря.
- `id_category_default` (int): ID категории по умолчанию.
- `category` (dict, optional): Словарь, представляющий категорию (по умолчанию пустой словарь).

**Возвращает**:

- `dict`: Иерархический словарь, представляющий категории и их URL.

**Обрабатываемые исключения**:

- `Exception`: Обработка любых исключений, возникающих при обходе.


#### `_is_duplicate_url`

**Описание**: Проверяет, существует ли URL в словаре категорий.

**Параметры**:

- `category` (dict): Словарь категорий.
- `url` (str): URL для проверки.

**Возвращает**:

- `bool`: `True`, если URL дублируется, иначе `False`.


## Функции

### `compare_and_print_new_keys`

**Описание**: Сравнивает текущий словарь с данными в файле и выводит отсутствующие ключи.

**Параметры**:

- `current_dict` (dict): Текущий словарь для сравнения.
- `file_path` (str): Путь к файлу с данными для сравнения.

**Обрабатываемые исключения**:

- `Exception`: Обработка исключений при загрузке данных из файла.


## Замечания

- В модуле используется асинхронный метод `crawl_categories_async` и синхронный метод `crawl_categories` для обхода категорий.
- Функция `_is_duplicate_url` предотвращает добавление дублирующихся URL в иерархический словарь.
- Используется модуль `json` для работы с JSON-данными, а не `pprint`.
- Поддержка работы с PrestaShop.