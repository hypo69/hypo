# Модуль `hypotez/src/category/category.py`

## Обзор

Модуль `category.py` предоставляет классы для работы с категориями продуктов, в основном для PrestaShop.  Он содержит функции для получения родительских категорий, асинхронного сканирования категорий и построения иерархической структуры категорий, сохраняющей результаты в JSON-файле.

## Оглавление

* [Модуль `category.py`](#модуль-categorypy)
* [Класс `Category`](#класс-category)
    * [`get_parents`](#get-parents)
    * [`crawl_categories_async`](#crawl-categories-async)
    * [`crawl_categories`](#crawl-categories)
    * [`_is_duplicate_url`](#_is-duplicate-url)
* [Функция `compare_and_print_missing_keys`](#функция-compare-and-print-missing-keys)


## Класс `Category`

**Описание**: Обработчик категорий продуктов. Наследуется от `PrestaCategory`.

**Атрибуты**:

* `credentials`: Словарь с данными авторизации.

**Методы**:

### `get_parents`

**Описание**: Возвращает список родительских категорий для заданной категории.

**Параметры**:

* `id_category` (int): Идентификатор категории.
* `dept` (int): Уровень вложенности категории.

**Возвращает**:

* list: Список родительских категорий.


### `crawl_categories_async`

**Описание**: Асинхронно сканирует категории, строит иерархический словарь.

**Параметры**:

* `url` (str): URL страницы категории.
* `depth` (int): Глубина рекурсивного сканирования.
* `driver` (object): Экземпляр Selenium WebDriver.
* `locator` (str): XPath локатор для ссылок на категории.
* `dump_file` (str): Путь к файлу JSON для сохранения результатов.
* `default_category_id` (int): Идентификатор категории по умолчанию.
* `category` (dict, optional): Существующий словарь категории (по умолчанию `None`).

**Возвращает**:

* dict: Обновленный или новый словарь категории.

**Обрабатываемые исключения**:

* `Exception`: Общее исключение при сканировании категорий.


### `crawl_categories`

**Описание**: Рекурсивно сканирует категории и строит иерархический словарь.

**Параметры**:

* `url` (str): URL страницы для сканирования.
* `depth` (int): Глубина рекурсии.
* `driver` (object): Экземпляр Selenium WebDriver.
* `locator` (str): XPath локатор для нахождения ссылок на категории.
* `dump_file` (str): Файл для сохранения иерархического словаря.
* `id_category_default` (int): Идентификатор категории по умолчанию.
* `category` (dict, optional): Словарь категории (по умолчанию пустой).

**Возвращает**:

* dict: Иерархический словарь категорий и их URL-адресов.

**Обрабатываемые исключения**:

* `Exception`: Общее исключение при сканировании категорий.


### `_is_duplicate_url`

**Описание**: Проверяет, существует ли URL уже в словаре категории.

**Параметры**:

* `category` (dict): Словарь категории.
* `url` (str): URL для проверки.

**Возвращает**:

* bool: `True`, если URL является дубликатом, `False` в противном случае.


## Функция `compare_and_print_missing_keys`

**Описание**: Сравнивает текущий словарь с данными в файле и выводит отсутствующие ключи.

**Параметры**:

* `current_dict` (dict): Текущий словарь.
* `file_path` (str): Путь к файлу.

**Обрабатываемые исключения**:

* `Exception`: Общее исключение при загрузке данных из файла.