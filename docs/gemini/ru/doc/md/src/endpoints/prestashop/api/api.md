# Модуль `hypotez/src/endpoints/prestashop/api/api.py`

## Обзор

Этот модуль предоставляет класс `PrestaShop`, позволяющий взаимодействовать с API веб-сервиса PrestaShop.  Класс поддерживает операции CRUD, поиск и загрузку изображений.  Он обрабатывает ошибки ответов API и предоставляет методы для работы с данными, возвращаемыми API.  Поддерживает передачу данных в формате JSON и XML.

## Оглавление

- [Модуль `PrestaShop`](#модуль-prestashop)
    - [Класс `PrestaShop`](#класс-prestashop)
        - [Метод `__init__`](#метод-init)
        - [Метод `ping`](#метод-ping)
        - [Метод `_check_response`](#метод-check-response)
        - [Метод `_parse_response_error`](#метод-parse-response-error)
        - [Метод `_prepare`](#метод-prepare)
        - [Метод `_exec`](#метод-exec)
        - [Метод `_parse`](#метод-parse)
        - [Метод `create`](#метод-create)
        - [Метод `read`](#метод-read)
        - [Метод `write`](#метод-write)
        - [Метод `unlink`](#метод-unlink)
        - [Метод `search`](#метод-search)
        - [Метод `create_binary`](#метод-create-binary)
        - [Метод `_save`](#метод-save)
        - [Метод `get_data`](#метод-get-data)
        - [Метод `remove_file`](#метод-remove-file)
        - [Метод `get_apis`](#метод-get-apis)
        - [Метод `get_languages_schema`](#метод-get-languages-schema)
        - [Метод `upload_image_async`](#метод-upload-image-async)
        - [Метод `upload_image`](#метод-upload-image)
        - [Метод `get_product_images`](#метод-get-product-images)
- [Перечисление `Format`](#перечисление-format)


## Перечисление `Format`

### `Format`

**Описание**: Перечисление `Format` определяет типы данных, которые могут возвращаться (JSON или XML). По умолчанию используется JSON.

**Элементы**:
- `JSON`
- `XML`


## Класс `PrestaShop`

### `__init__`

**Описание**: Инициализирует класс `PrestaShop`.

**Параметры**:
- `data_format` (str, по умолчанию 'JSON'): Формат данных (JSON или XML).
- `default_lang` (int, по умолчанию 1): ID языка по умолчанию.
- `debug` (bool, по умолчанию True): Включает отладочный режим.

**Возвращает**:
- `None`


### `ping`

**Описание**: Проверяет доступность веб-сервиса PrestaShop.

**Возвращает**:
- `bool`: `True`, если веб-сервис доступен, иначе `False`.


### `_check_response`

**Описание**: Проверяет код ответа и обрабатывает ошибки.

**Параметры**:
- `status_code` (int): Код HTTP ответа.
- `response` (`requests.Response`): Объект ответа HTTP.
- `method`, `url`, `headers`, `data` (опционально): Дополнительные параметры запроса.


**Возвращает**:
- `bool`: `True`, если код ответа 200 или 201, иначе `False`.


### `_parse_response_error`

**Описание**: Парсит ошибку ответа от PrestaShop API.

**Параметры**:
- `response` (`requests.Response`): Объект ответа HTTP от сервера.


**Возвращает**:
-  `requests.Response` (если формат JSON) или кортеж (код ошибки, сообщение об ошибке) (если формат XML).


### `_prepare`

**Описание**: Подготавливает URL для запроса, добавляя параметры.

**Параметры**:
- `url` (str): Базовый URL.
- `params` (dict): Параметры запроса.

**Возвращает**:
- str: Подготовленный URL с параметрами.


### `_exec`

**Описание**: Выполняет HTTP-запрос к API PrestaShop.

**Параметры**:
- `resource` (str): Ресурс API (например, 'products', 'categories').
- `resource_id` (int | str, опционально): ID ресурса.
- `resource_ids` (int | tuple, опционально): ID нескольких ресурсов.
- `method` (str, по умолчанию 'GET'): HTTP-метод.
- `data` (dict, опционально): Данные для отправки.
- `headers` (dict, опционально): Дополнительные заголовки.
- `search_filter`, `display`, `schema`, `sort`, `limit`, `language`, `io_format` (опционально): Параметры для запроса.

**Возвращает**:
- `dict | None`: Ответ от API или `False` при ошибке.


### `_parse`

**Описание**: Парсит ответ в формате XML или JSON.

**Параметры**:
- `text` (str): Текст ответа.

**Возвращает**:
- `dict | ElementTree.Element | bool`: Разбор данных или `False` при ошибке.


### `create`, `read`, `write`, `unlink`, `search`, `create_binary`, `get_data`, `remove_file`, `get_apis`, `get_languages_schema`, `upload_image_async`, `upload_image`, `get_product_images`

**Описание**: Методы для выполнения CRUD-операций, поиска, загрузки изображений и получения данных из разных ресурсов PrestaShop API. Подробные описания см. в исходном коде.


**Примечание**: Документация для методов `_parse` и `_check_response` дополнена, чтобы соответствовать заданным требованиям.  Также добавлено пояснение к возвращаемым значениям для `_parse_response_error`.