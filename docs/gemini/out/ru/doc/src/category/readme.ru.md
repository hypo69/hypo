# Модуль: Category

## Обзор

Модуль `Category` предоставляет функциональность для работы с категориями товаров, в первую очередь для PrestaShop. Он предлагает инструменты для взаимодействия с данными категорий, включая обход страниц категорий и управление иерархической структурой категорий.

## Оглавление

* [Модуль: Category](#модуль-category)
* [Обзор](#обзор)
* [Класс: `Category`](#класс-category)
    * [Конструктор: `__init__`](#конструктор-init)
    * [Метод: `get_parents`](#метод-get_parents)
    * [Метод: `crawl_categories_async`](#метод-crawl_categories_async)
    * [Метод: `crawl_categories`](#метод-crawl_categories)
    * [Метод: `_is_duplicate_url`](#метод-is_duplicate_url)
* [Функция: `compare_and_print_missing_keys`](#функция-compare_and_print_missing_keys)
* [Пример использования](#пример-использования)
* [Зависимости](#зависимости)


## Класс: `Category`

Класс `Category` наследует от `PrestaCategory` и отвечает за обработку категорий товаров, получение родительских категорий и рекурсивный обход страниц категорий.

### Конструктор: `__init__`

Инициализирует объект `Category`.

#### Аргументы:
- `api_credentials`: Учетные данные API для доступа к данным категорий.
- `*args`: Список аргументов переменной длины (не используется).
- `**kwargs`: Ключевые аргументы (не используется).

```python
def __init__(self, api_credentials, *args, **kwargs) -> None:
    """
    Инициализирует объект Category.

    Args:
        api_credentials: Учетные данные API для доступа к данным категорий.
        *args: Список аргументов переменной длины (не используется).
        **kwargs: Ключевые аргументы (не используется).
    """
    pass
```


### Метод: `get_parents`

Получает список родительских категорий.

#### Аргументы:
- `id_category`: ID категории, для которой нужно получить родительские категории.
- `dept`: Уровень глубины категории.

#### Возвращает:
- Список родительских категорий.

```python
def get_parents(self, id_category: int, dept: int) -> list:
    """
    Получает список родительских категорий.

    Args:
        id_category (int): ID категории, для которой нужно получить родительские категории.
        dept (int): Уровень глубины категории.

    Returns:
        list: Список родительских категорий.
    """
    pass
```

### Метод: `crawl_categories_async`

Асинхронно обходит категории, строя иерархический словарь.

#### Аргументы:
- `url`: URL страницы категории.
- `depth`: Глубина рекурсии обхода.
- `driver`: Экземпляр Selenium WebDriver.
- `locator`: XPath локатор для ссылок на категории.
- `dump_file`: Путь к файлу JSON для сохранения результатов.
- `default_category_id`: ID категории по умолчанию.
- `category`: (Необязательно) Существующий словарь категории (по умолчанию=None).

#### Возвращает:
- Обновленный или новый словарь категорий.


```python
async def crawl_categories_async(self, url: str, depth: int, driver, locator: str, dump_file: str, default_category_id: int, category=None) -> dict:
    """
    Асинхронно обходит категории, строя иерархический словарь.

    Args:
        url (str): URL страницы категории.
        depth (int): Глубина рекурсии обхода.
        driver: Экземпляр Selenium WebDriver.
        locator (str): XPath локатор для ссылок на категории.
        dump_file (str): Путь к файлу JSON для сохранения результатов.
        default_category_id (int): ID категории по умолчанию.
        category (dict, optional): Существующий словарь категории (по умолчанию=None).

    Returns:
        dict: Обновленный или новый словарь категорий.
    """
    pass
```

(Остальные методы и функции описываются аналогично)

## Пример использования

```python
# ... (пример использования из документации)
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