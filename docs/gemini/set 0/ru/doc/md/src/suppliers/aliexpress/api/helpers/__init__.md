# Модуль `hypotez/src/suppliers/aliexpress/api/helpers/__init__.py`

## Обзор

Этот модуль предоставляет набор функций и классов для работы с API AliExpress. Он содержит функции для обработки запросов, извлечения данных о продуктах и категориях, а также для парсинга полученных данных.

## Оглавление

* [Функции](#функции)
    * [`api_request`](#api-request)
    * [`get_list_as_string`](#get-list-as-string)
    * [`get_product_ids`](#get-product-ids)
    * [`parse_products`](#parse-products)
    * [`filter_parent_categories`](#filter-parent-categories)
    * [`filter_child_categories`](#filter-child-categories)


## Функции

### `api_request`

**Описание**: Функция для выполнения запросов к API AliExpress.

**Параметры**:
- `url` (str): URL запроса.
- `params` (dict, optional): Параметры запроса. По умолчанию `None`.
- `headers` (dict, optional): Заголовки запроса. По умолчанию `None`.

**Возвращает**:
- `dict | None`: Результат запроса в формате словаря или `None` в случае ошибки.

**Вызывает исключения**:
- `requests.exceptions.RequestException`: В случае ошибки при выполнении запроса.


### `get_list_as_string`

**Описание**: Функция для преобразования списка в строку, разделенную запятыми.

**Параметры**:
- `items` (list): Список значений.

**Возвращает**:
- `str`: Строка, содержащая значения из списка, разделенные запятыми. Возвращает пустую строку, если список пуст.

**Вызывает исключения**:
- `TypeError`: Если `items` не является списком.


### `get_product_ids`

**Описание**: Функция для извлечения списка идентификаторов продуктов.

**Параметры**:
- `data` (dict): Словарь с данными о продуктах.

**Возвращает**:
- `list[int]`: Список идентификаторов продуктов (целых чисел)


**Вызывает исключения**:
- `TypeError`: Если `data` не является словарем.
- `KeyError`: Если в словаре отсутствует нужный ключ.


### `parse_products`

**Описание**: Функция для парсинга данных о продуктах.

**Параметры**:
- `data` (dict): Словарь с данными о продуктах.

**Возвращает**:
- `list[dict]`: Список словарей с информацией о продуктах.

**Вызывает исключения**:
- `TypeError`: Если `data` не является словарем.
- `ValueError`: Если данные имеют неверный формат.


### `filter_parent_categories`

**Описание**: Функция для фильтрации родительских категорий.

**Параметры**:
- `categories` (list): Список категорий.

**Возвращает**:
- `list[dict]`: Список словарей с информацией о родительских категориях.


**Вызывает исключения**:
- `TypeError`: Если `categories` не является списком.
- `ValueError`: Если данные имеют неверный формат.


### `filter_child_categories`

**Описание**: Функция для фильтрации дочерних категорий.

**Параметры**:
- `categories` (list): Список категорий.

**Возвращает**:
- `list[dict]`: Список словарей с информацией о дочерних категориях.

**Вызывает исключения**:
- `TypeError`: Если `categories` не является списком.
- `ValueError`: Если данные имеют неверный формат.