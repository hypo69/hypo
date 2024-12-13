# Модуль `base.py`

## Обзор

Модуль `base.py` представляет собой базовый клиент для взаимодействия с API, предоставляемым AliExpress. Он включает в себя функции для подписи запросов, отправки HTTP-запросов и обработки ответов. Модуль также предоставляет классы `IopRequest`, `IopResponse` и `IopClient` для структурирования запросов и ответов.

## Содержание

1. [Константы](#константы)
2. [Функции](#функции)
    - [`sign`](#sign)
    - [`mixStr`](#mixStr)
    - [`logApiError`](#logApiError)
3. [Классы](#классы)
    - [`IopRequest`](#IopRequest)
        - [`__init__`](#__init__-1)
        - [`add_api_param`](#add_api_param)
        - [`add_file_param`](#add_file_param)
        - [`set_simplify`](#set_simplify)
        - [`set_format`](#set_format)
    - [`IopResponse`](#IopResponse)
        - [`__init__`](#__init__-2)
        - [`__str__`](#__str__)
    - [`IopClient`](#IopClient)
        - [`__init__`](#__init__-3)
        - [`execute`](#execute)

## Константы

В модуле определены следующие константы:

-   `P_SDK_VERSION`: Версия SDK.
-   `P_APPKEY`: Ключ приложения.
-   `P_ACCESS_TOKEN`: Токен доступа.
-   `P_TIMESTAMP`: Временная метка.
-   `P_SIGN`: Подпись запроса.
-   `P_SIGN_METHOD`: Метод подписи.
-   `P_PARTNER_ID`: ID партнера.
-   `P_METHOD`: Метод API.
-   `P_DEBUG`: Флаг отладки.
-   `P_SIMPLIFY`: Флаг упрощения ответа.
-   `P_FORMAT`: Формат ответа.
-   `P_CODE`: Код ответа.
-   `P_TYPE`: Тип ответа.
-   `P_MESSAGE`: Сообщение ответа.
-   `P_REQUEST_ID`: ID запроса.
-   `P_LOG_LEVEL_DEBUG`: Уровень логирования DEBUG.
-   `P_LOG_LEVEL_INFO`: Уровень логирования INFO.
-   `P_LOG_LEVEL_ERROR`: Уровень логирования ERROR.

## Функции

### `sign`

```python
def sign(secret: str, api: str, parameters: dict) -> str:
    """
    Генерирует подпись запроса.

    Args:
        secret (str): Секретный ключ приложения.
        api (str): Название API метода.
        parameters (dict): Словарь параметров запроса.

    Returns:
        str: Подпись запроса в верхнем регистре.
    """
```

### `mixStr`

```python
def mixStr(pstr: str | unicode | int) -> str:
    """
    Преобразует входные данные в строку.

    Args:
        pstr (str | unicode | int): Входные данные любого типа.

    Returns:
        str: Строковое представление входных данных.
    """
```

### `logApiError`

```python
def logApiError(appkey: str, sdkVersion: str, requestUrl: str, code: str, message: str) -> None:
    """
    Логирует ошибки API запросов.

    Args:
        appkey (str): Ключ приложения.
        sdkVersion (str): Версия SDK.
        requestUrl (str): URL запроса.
        code (str): Код ошибки.
        message (str): Сообщение об ошибке.

    Returns:
        None: Функция ничего не возвращает.
    """
```

## Классы

### `IopRequest`

#### Описание
Класс `IopRequest` представляет собой структуру данных для формирования запроса к API.

#### Методы

##### `__init__`

```python
def __init__(self, api_pame: str, http_method: str = 'POST') -> None:
    """
    Инициализирует объект IopRequest.

    Args:
        api_pame (str): Название API метода.
        http_method (str, optional): HTTP метод запроса. По умолчанию 'POST'.

    Returns:
        None: Функция ничего не возвращает.
    """
```

##### `add_api_param`

```python
def add_api_param(self, key: str, value: str) -> None:
    """
    Добавляет параметр API запроса.

    Args:
        key (str): Ключ параметра.
        value (str): Значение параметра.

    Returns:
        None: Функция ничего не возвращает.
    """
```

##### `add_file_param`

```python
def add_file_param(self, key: str, value: str) -> None:
    """
    Добавляет файл в параметры запроса.

    Args:
        key (str): Ключ файла.
        value (str): Значение файла.

    Returns:
        None: Функция ничего не возвращает.
    """
```

##### `set_simplify`

```python
def set_simplify(self) -> None:
    """
    Устанавливает флаг упрощенного ответа.

    Returns:
        None: Функция ничего не возвращает.
    """
```

##### `set_format`

```python
def set_format(self, value: str) -> None:
    """
    Устанавливает формат ответа.

    Args:
        value (str): Формат ответа.

    Returns:
        None: Функция ничего не возвращает.
    """
```

### `IopResponse`

#### Описание

Класс `IopResponse` представляет собой структуру данных для хранения ответа от API.

#### Методы

##### `__init__`

```python
def __init__(self) -> None:
    """
    Инициализирует объект IopResponse.

    Returns:
        None: Функция ничего не возвращает.
    """
```

##### `__str__`

```python
def __str__(self, *args, **kwargs) -> str:
    """
    Возвращает строковое представление объекта IopResponse.

    Returns:
        str: Строковое представление объекта.
    """
```

### `IopClient`

#### Описание

Класс `IopClient` представляет собой клиент для выполнения запросов к API.

#### Методы

##### `__init__`

```python
def __init__(self, server_url: str, app_key: str, app_secret: str, timeout: int = 30) -> None:
    """
    Инициализирует объект IopClient.

    Args:
        server_url (str): URL сервера API.
        app_key (str): Ключ приложения.
        app_secret (str): Секретный ключ приложения.
        timeout (int, optional): Тайм-аут запроса в секундах. По умолчанию 30.

    Returns:
        None: Функция ничего не возвращает.
    """
```

##### `execute`

```python
def execute(self, request: IopRequest, access_token: Optional[str] = None) -> IopResponse:
    """
    Выполняет запрос к API.

    Args:
        request (IopRequest): Объект запроса.
        access_token (Optional[str], optional): Токен доступа. По умолчанию `None`.

    Returns:
        IopResponse: Объект ответа.

    Raises:
        Exception: Если при выполнении запроса возникает ошибка.
    """
```