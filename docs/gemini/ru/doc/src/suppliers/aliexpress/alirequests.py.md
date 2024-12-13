# Модуль `alirequests.py`

## Обзор

Модуль `alirequests.py` предназначен для обработки запросов к AliExpress с использованием библиотеки `requests`. Он включает функциональность для загрузки куки из файла, обновления сессионных куки и выполнения GET-запросов с куками и заголовками. Также модуль предоставляет возможность получить короткую партнерскую ссылку.

## Содержание

1. [Классы](#Классы)
    - [`AliRequests`](#AliRequests)
2. [Функции](#Функции)
    - [`_load_webdriver_cookies_file`](#_load_webdriver_cookies_file)
    - [`_refresh_session_cookies`](#_refresh_session_cookies)
    - [`_handle_session_id`](#_handle_session_id)
    - [`make_get_request`](#make_get_request)
    - [`short_affiliate_link`](#short_affiliate_link)

<br>

## Классы

### `AliRequests`

**Описание**: Класс `AliRequests` предназначен для управления запросами к AliExpress.

**Методы**:
- `__init__`: Инициализирует класс, загружает куки из файла и устанавливает заголовки.
- `_load_webdriver_cookies_file`: Загружает куки из файла вебдрайвера.
- `_refresh_session_cookies`: Обновляет сессионные куки.
- `_handle_session_id`: Обрабатывает JSESSIONID в куках ответа.
- `make_get_request`: Выполняет GET-запрос с куками и заголовками.
- `short_affiliate_link`: Получает короткую партнерскую ссылку.

<br>

## Функции

### `_load_webdriver_cookies_file`

**Описание**: Загружает куки из файла, созданного вебдрайвером.

**Параметры**:
- `webdriver_for_cookies` (str, optional): Имя вебдрайвера. По умолчанию `chrome`.

**Возвращает**:
- `bool`: `True`, если куки успешно загружены, `False` в противном случае.

**Вызывает исключения**:
- `FileNotFoundError`: Если файл с куки не найден.
- `ValueError`: Если возникает ошибка при десериализации данных из файла.
- `Exception`: При возникновении любой другой ошибки.

### `_refresh_session_cookies`

**Описание**: Обновляет сессионные куки, выполняя GET-запрос к `https://portals.aliexpress.com`.

**Возвращает**:
- `None`: Функция ничего не возвращает.

**Вызывает исключения**:
- `requests.RequestException`: Если возникает ошибка при выполнении запроса.
- `Exception`: При возникновении любой другой ошибки.

### `_handle_session_id`

**Описание**: Обрабатывает куку `JSESSIONID` из ответа, обновляя ее в куки-хранилище, если она изменилась.

**Параметры**:
- `response_cookies` (requests.cookies.RequestsCookieJar): Куки, полученные в ответе.

**Возвращает**:
- `None`: Функция ничего не возвращает.

### `make_get_request`

**Описание**: Выполняет GET-запрос по указанному URL с куками и заголовками.

**Параметры**:
- `url` (str): URL, по которому нужно выполнить GET-запрос.
- `cookies` (List[dict], optional): Список куки для использования в запросе. По умолчанию `None`.
- `headers` (dict, optional): Заголовки для включения в запрос. По умолчанию `None`.

**Возвращает**:
- `requests.Response | False`: Объект `requests.Response` в случае успешного запроса, `False` в случае ошибки.

**Вызывает исключения**:
- `requests.RequestException`: Если запрос завершается с ошибкой.
- `Exception`: При возникновении любой другой ошибки.

### `short_affiliate_link`

**Описание**: Получает короткую партнерскую ссылку для указанного URL.

**Параметры**:
- `link_url` (str): URL, для которого нужно получить короткую ссылку.

**Возвращает**:
- `requests.Response | False`: Объект `requests.Response` в случае успешного запроса, `False` в случае ошибки.