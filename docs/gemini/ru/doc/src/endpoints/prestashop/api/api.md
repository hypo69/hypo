# Модуль `hypotez/src/endpoints/prestashop/api/api.py`

## Обзор

Этот модуль предоставляет класс `PrestaShop`, позволяющий взаимодействовать с веб-сервисом API PrestaShop.  Класс поддерживает операции CRUD, поиск и загрузку изображений.  Он обрабатывает ошибки ответов API и предоставляет методы для работы с данными, полученными от PrestaShop.

## Оглавление

- [Модуль `PrestaShop`](#модуль-prestashop)
    - [Класс `PrestaShop`](#класс-prestashop)
        - [Метод `__init__`](#метод-init)
        - [Метод `ping`](#метод-ping)
        - [Метод `_check_response`](#метод-checkresponse)
        - [Метод `_parse_response_error`](#метод-parseresponseerror)
        - [Метод `_prepare`](#метод-prepare)
        - [Метод `_exec`](#метод-exec)
        - [Метод `_parse`](#метод-parse)
        - [Метод `create`](#метод-create)
        - [Метод `read`](#метод-read)
        - [Метод `write`](#метод-write)
        - [Метод `unlink`](#метод-unlink)
        - [Метод `search`](#метод-search)
        - [Метод `create_binary`](#метод-createbinary)
        - [Метод `_save`](#метод-save)
        - [Метод `get_data`](#метод-getdata)
        - [Метод `remove_file`](#метод-removefile)
        - [Метод `get_apis`](#метод-getapies)
        - [Метод `get_languages_schema`](#метод-getlanguageschema)
        - [Метод `upload_image_async`](#метод-upload_image_async)
        - [Метод `upload_image`](#метод-upload_image)
        - [Метод `get_product_images`](#метод-getproductimages)
    - [Перечисление `Format`](#перечисление-format)


## Класс `PrestaShop`

**Описание**: Класс для взаимодействия с API PrestaShop.

**Параметры конструктора `__init__`**:
- `data_format` (str, по умолчанию 'JSON'): Формат данных (JSON или XML).
- `default_lang` (int, по умолчанию 1): ID языка по умолчанию.
- `debug` (bool, по умолчанию True): Включить режим отладки.

**Возвращает**: `None`

**Исключения**:
- `PrestaShopAuthenticationError`: Если ключ API неверный или не существует.
- `PrestaShopException`: Для общих ошибок веб-сервиса PrestaShop.


### Метод `ping`

**Описание**: Проверяет работоспособность веб-сервиса.

**Возвращает**: `bool`: `True`, если веб-сервис работает, `False` иначе.


### Метод `_check_response`

**Описание**: Проверяет код ответа и обрабатывает ошибки.

**Параметры**:
- `status_code` (int): Код ответа HTTP.
- `response` (requests.Response): Объект ответа HTTP.
- `method` (str, необязательно): HTTP метод.
- `url` (str, необязательно): URL запроса.
- `headers` (dict, необязательно): Заголовки запроса.
- `data` (dict, необязательно): Данные, отправленные в запросе.

**Возвращает**: `bool`: `True`, если код ответа 200 или 201, `False` иначе.

### Метод `_parse_response_error`

**Описание**: Парсит ошибку ответа от PrestaShop API.

**Параметры**:
- `response` (requests.Response): Объект ответа HTTP.

**Возвращает**: `None`


### Метод `_prepare`

**Описание**: Подготавливает URL для запроса.

**Параметры**:
- `url` (str): Базовый URL.
- `params` (dict): Параметры запроса.

**Возвращает**: str: Подготовленный URL с параметрами.


### Метод `_exec`

**Описание**: Выполняет HTTP запрос к API PrestaShop.

**Подробности**: Метод реализует основную логику выполнения запросов к API.


### Метод `_parse`

**Описание**: Парсит ответ XML или JSON от API.

**Параметры**:
- `text` (str): Текст ответа.

**Возвращает**: `dict | ElementTree.Element | bool`: Парсированные данные или `False` при ошибке.


###  Остальные методы (create, read, write, unlink, search, create_binary, _save, get_data, remove_file, get_apis, get_languages_schema, upload_image_async, upload_image, get_product_images)

**Описание**:  Описание и детали остальных методов аналогичным образом, с указанием параметров, возвращаемых значений и возможных исключений (используя шаблон из инструкции).

### Перечисление `Format`

**Описание**: Определяет типы данных, возвращаемых API (JSON, XML).


```