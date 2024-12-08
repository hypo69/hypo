# Модуль: Category

## Обзор

Модуль `Category` предоставляет функциональность для работы с категориями товаров, в первую очередь для PrestaShop. Он предлагает инструменты для взаимодействия с данными категорий, включая обход страниц категорий и управление иерархической структурой категорий.

## Оглавление

* [Модуль: Category](#модуль-category)
* [Обзор](#обзор)
* [Класс: Category](#класс-category)
    * [Конструктор: __init__](#конструктор-init)
    * [Метод: get_parents](#метод-get_parents)
    * [Метод: crawl_categories_async](#метод-crawl_categories_async)
    * [Метод: crawl_categories](#метод-crawl_categories)
    * [Метод: _is_duplicate_url](#метод-is_duplicate_url)
* [Функция: compare_and_print_missing_keys](#функция-compare_and_print_missing_keys)
* [Пример использования](#пример-использования)
* [Зависимости](#зависимости)


## Класс: `Category`

Класс `Category` наследует от `PrestaCategory` и отвечает за обработку категорий товаров, получение родительских категорий и рекурсивный обход страниц категорий.

### Конструктор: `__init__(self, api_credentials, *args, **kwargs)`

Инициализирует объект `Category`.

#### Аргументы:
- `api_credentials`: Учетные данные API для доступа к данным категорий.
- `args`: Список аргументов переменной длины (не используется).
- `kwargs`: Ключевые аргументы (не используется).

#### Примечания:
Требует `api_credentials` для работы.


### Метод: `get_parents(self, id_category, dept)`

Получает список родительских категорий.

#### Аргументы:
- `id_category` (int): ID категории, для которой нужно получить родительские категории.
- `dept` (int): Уровень глубины категории.


#### Возвращает:
- `list[dict]`: Список родительских категорий. Возвращает `None`, если категория не найдена или произошла ошибка.

#### Примечания:
Метод реализует логику поиска родительских категорий.


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
- `dict`: Обновленный или новый словарь категорий. Возвращает `None` при ошибке.

#### Примечания:
Используется асинхронно для повышения производительности. Сохраняет результат в файл.


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
- `dict`: Иерархический словарь категорий и их URL.

#### Примечания:
Синхронная версия метода обхода категорий.


### Метод: `_is_duplicate_url(self, category, url)`

Проверяет, существует ли URL в словаре категорий.

#### Аргументы:
- `category` (dict): Словарь категорий.
- `url` (str): URL для проверки.


#### Возвращает:
- `bool`: `True`, если URL является дубликатом, иначе `False`.


## Функция: `compare_and_print_missing_keys(current_dict, file_path)`

Сравнивает текущий словарь с данными из файла и выводит отсутствующие ключи.

#### Аргументы:
- `current_dict` (dict): Словарь для сравнения.
- `file_path` (str): Путь к файлу, содержащему данные для сравнения.

#### Примечания:
Проверяет соответствие значений в словаре `current_dict` со значениями в файле `file_path`.

## Пример использования

```python
from src.category import Category
# ... (код инициализации и использования)
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