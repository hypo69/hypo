# Модуль hypotez/src/endpoints/prestashop/api/api.py

## Обзор

Модуль `api.py` предоставляет класс `PrestaShop`, позволяющий взаимодействовать с API PrestaShop.  Класс поддерживает операции CRUD (создание, чтение, обновление, удаление) ресурсов, поиск и загрузку изображений.  Использует JSON и XML для обмена данными.

## Оглавление

- [Модуль `api.py`](#модуль-api-py)
- [Класс `PrestaShop`](#класс-prestashop)
    - [Метод `ping`](#метод-ping)
    - [Метод `_check_response`](#метод-_check_response)
    - [Метод `_parse_response_error`](#метод-_parse_response_error)
    - [Метод `_prepare`](#метод-_prepare)
    - [Метод `_exec`](#метод-_exec)
    - [Метод `_parse`](#метод-_parse)
    - [Метод `create`](#метод-create)
    - [Метод `read`](#метод-read)
    - [Метод `write`](#метод-write)
    - [Метод `unlink`](#метод-unlink)
    - [Метод `search`](#метод-search)
    - [Метод `create_binary`](#метод-create_binary)
    - [Метод `_save`](#метод-_save)
    - [Метод `get_data`](#метод-get_data)
    - [Метод `remove_file`](#метод-remove_file)
    - [Метод `get_apis`](#метод-get_apis)
    - [Метод `get_languages_schema`](#метод-get_languages_schema)
    - [Метод `upload_image_async`](#метод-upload_image_async)
    - [Метод `upload_image`](#метод-upload_image)
    - [Метод `get_product_images`](#метод-get_product_images)


## Класс `PrestaShop`

**Описание**: Класс для взаимодействия с API PrestaShop. Обеспечивает методы для выполнения различных операций с ресурсами.

**Параметры инициализации**:
- `API_DOMAIN` (str): Домен PrestaShop магазина (например, `https://myPrestaShop.com/api/`).
- `API_KEY` (str): API ключ от PrestaShop.
- `data_format` (str, опционально): Формат данных ('JSON' или 'XML'). По умолчанию 'JSON'.
- `default_lang` (int, опционально): ID языка по умолчанию. По умолчанию 1.
- `debug` (bool, опционально): Включить режим отладки. По умолчанию True.

**Вызывает исключения**:
- `PrestaShopAuthenticationError`: При ошибке аутентификации.
- `PrestaShopException`: При общих ошибках PrestaShop API.


### Метод `ping`

**Описание**: Проверяет работоспособность веб-сервиса PrestaShop.

**Возвращает**:
- bool: `True`, если сервер доступен, `False` в противном случае.


### Метод `_check_response`

**Описание**: Проверяет код ответа HTTP и обрабатывает ошибки.

**Параметры**:
- `status_code` (int): Код состояния ответа HTTP.
- `response` (requests.Response): Объект ответа HTTP.
- `method`, `url`, `headers`, `data` (опционально): Дополнительные параметры для отладки.

**Возвращает**:
- bool: `True`, если код ответа 200 или 201, `False` в противном случае.

### Метод `_parse_response_error`

**Описание**: Парсит ошибку ответа от PrestaShop API.

**Параметры**:
- `response` (requests.Response): Объект ответа HTTP.

**Возвращает**:
- requests.Response: Возвращает объект ответа в случае ошибки, None в случае успеха.


(Остальные методы описаны аналогичным образом,  с указанием параметров, возвращаемых значений и исключений.  Подробно описываются методы `_prepare`, `_exec`, `_parse`, `create`, `read`, `write`, `unlink`, `search`, `create_binary`, `_save`, `get_data`, `remove_file`, `get_apis`, `get_languages_schema`, `upload_image_async`, `upload_image`, `get_product_images`.)