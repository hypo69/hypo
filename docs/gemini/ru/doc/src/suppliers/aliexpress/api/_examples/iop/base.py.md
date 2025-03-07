# Модуль `base.py`

## Обзор

Модуль `base.py` представляет собой базовый SDK для взаимодействия с API AliExpress. Он включает в себя функциональность для формирования запросов, их подписи, отправки и обработки ответов. SDK поддерживает логирование ошибок и предоставляет классы для работы с запросами и ответами.

## Оглавление

- [Функции](#функции)
    - [`sign`](#sign)
    - [`mixStr`](#mixStr)
    - [`logApiError`](#logApiError)
- [Классы](#классы)
    - [`IopRequest`](#IopRequest)
        - [`__init__`](#__init__-ioprequest)
        - [`add_api_param`](#add_api_param)
        - [`add_file_param`](#add_file_param)
        - [`set_simplify`](#set_simplify)
        - [`set_format`](#set_format)
    - [`IopResponse`](#IopResponse)
        - [`__init__`](#__init__-iopresponse)
        - [`__str__`](#__str__)
    - [`IopClient`](#IopClient)
        - [`__init__`](#__init__-iopclient)
        - [`execute`](#execute)

## Функции

### `sign`

**Описание**: Функция для генерации подписи запроса с использованием HMAC-SHA256.

**Параметры**:
- `secret` (str): Секретный ключ приложения.
- `api` (str): Название API метода.
- `parameters` (dict): Словарь параметров запроса.

**Возвращает**:
- `str`: Подпись запроса в верхнем регистре.

### `mixStr`

**Описание**: Функция для преобразования различных типов данных в строку.

**Параметры**:
- `pstr` (str | unicode | any): Значение для преобразования в строку.

**Возвращает**:
- `str`: Строковое представление входного значения.

### `logApiError`

**Описание**: Функция для логирования ошибок API запросов.

**Параметры**:
- `appkey` (str): Ключ приложения.
- `sdkVersion` (str): Версия SDK.
- `requestUrl` (str): URL запроса.
- `code` (str): Код ошибки.
- `message` (str): Сообщение об ошибке.

**Возвращает**:
- `None`

## Классы

### `IopRequest`

**Описание**: Класс для представления запроса к API.

#### `__init__`

**Описание**: Конструктор класса `IopRequest`.

**Параметры**:
- `api_pame` (str): Название API метода.
- `http_method` (str, optional): HTTP метод запроса (по умолчанию 'POST').

#### `add_api_param`

**Описание**: Метод для добавления параметра API запроса.

**Параметры**:
- `key` (str): Ключ параметра.
- `value` (any): Значение параметра.

**Возвращает**:
- `None`

#### `add_file_param`

**Описание**: Метод для добавления файла к запросу.

**Параметры**:
- `key` (str): Ключ файла.
- `value` (any): Значение файла.

**Возвращает**:
- `None`

#### `set_simplify`

**Описание**: Метод для установки параметра `simplify` в значение "true".

**Параметры**:
- `None`

**Возвращает**:
- `None`

#### `set_format`

**Описание**: Метод для установки формата ответа.

**Параметры**:
- `value` (str): Формат ответа.

**Возвращает**:
- `None`

### `IopResponse`

**Описание**: Класс для представления ответа от API.

#### `__init__`

**Описание**: Конструктор класса `IopResponse`.

**Параметры**:
- `None`

#### `__str__`

**Описание**: Метод для строкового представления объекта `IopResponse`.

**Параметры**:
- `*args`: Произвольные позиционные аргументы.
- `**kwargs`: Произвольные именованные аргументы.

**Возвращает**:
- `str`: Строковое представление объекта `IopResponse`.

### `IopClient`

**Описание**: Класс для выполнения запросов к API.

#### `__init__`

**Описание**: Конструктор класса `IopClient`.

**Параметры**:
- `server_url` (str): URL сервера API.
- `app_key` (str): Ключ приложения.
- `app_secret` (str): Секретный ключ приложения.
- `timeout` (int, optional): Время ожидания ответа (по умолчанию 30 секунд).

#### `execute`

**Описание**: Метод для выполнения API запроса.

**Параметры**:
- `request` (IopRequest): Объект запроса.
- `access_token` (str, optional): Токен доступа.

**Возвращает**:
- `IopResponse`: Объект ответа от API.

**Вызывает исключения**:
- `Exception`: При возникновении ошибки во время выполнения HTTP запроса.