# Модуль `hypotez/src/suppliers/aliexpress/api/helpers/__init__.py`

## Обзор

Этот модуль предоставляет вспомогательные функции для работы с API AliExpress. Он содержит функции для обработки запросов, получения списков, идентификаторов продуктов, разбора данных о продуктах и фильтрации категорий.

## Оглавление

- [Функции](#функции)


## Функции

### `api_request`

**Описание**: Функция для отправки запросов к API AliExpress.

**Параметры**:
- `url` (str): URL запроса.
- `params` (dict, optional): Параметры запроса. По умолчанию `None`.
- `headers` (dict, optional): Заголовки запроса. По умолчанию `None`.


**Возвращает**:
- `dict | None`: Результат запроса в формате словаря или `None` в случае ошибки.


**Вызывает исключения**:
- `requests.exceptions.RequestException`: Возникает при проблемах с отправкой запроса.


### `get_list_as_string`

**Описание**: Функция для преобразования списка в строку, подходящую для API запросов.

**Параметры**:
- `data` (list): Список элементов.


**Возвращает**:
- `str`: Строковое представление списка.


**Вызывает исключения**:
- `TypeError`: Если входные данные не являются списком.


### `get_product_ids`

**Описание**: Функция для извлечения списков идентификаторов продуктов.

**Параметры**:
- `data` (dict): Словарь данных.


**Возвращает**:
- `list`: Список идентификаторов продуктов.


**Вызывает исключения**:
- `TypeError`: Если входные данные не являются словарем.
- `KeyError`: Если ключи не найдены в словаре.


### `parse_products`

**Описание**: Функция для парсинга данных о продуктах.

**Параметры**:
- `data` (dict): Словарь данных.


**Возвращает**:
- `list`: Список данных о продуктах.


**Вызывает исключения**:
- `TypeError`: Если входные данные не являются словарем.
- `KeyError`: Если ключи не найдены в словаре.


### `filter_parent_categories`

**Описание**: Функция для фильтрации родительских категорий.

**Параметры**:
- `data` (list): Список данных.
- `search_term` (str):  Критерий поиска.


**Возвращает**:
- `list`: отфильтрованный список родительских категорий.

**Вызывает исключения**:
- `TypeError`: Если входные данные не являются списком.


### `filter_child_categories`

**Описание**: Функция для фильтрации дочерних категорий.

**Параметры**:
- `data` (list): Список данных.
- `search_term` (str): Критерий поиска.


**Возвращает**:
- `list`: отфильтрованный список дочерних категорий.

**Вызывает исключения**:
- `TypeError`: Если входные данные не являются списком.