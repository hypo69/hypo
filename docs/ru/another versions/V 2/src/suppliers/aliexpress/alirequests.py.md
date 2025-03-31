# Модуль `alirequests`

## Обзор

Модуль `alirequests` предоставляет класс `AliRequests` для управления HTTP-запросами к AliExpress с использованием библиотеки `requests`. Он также обрабатывает управление куками и обеспечивает возможность создания коротких партнерских ссылок.

## Оглавление

- [Классы](#классы)
    - [`AliRequests`](#alirequests)
- [Функции](#функции)
    - [`_load_webdriver_cookies_file`](#_load_webdriver_cookies_file)
    - [`_refresh_session_cookies`](#_refresh_session_cookies)
    - [`_handle_session_id`](#_handle_session_id)
    - [`make_get_request`](#make_get_request)
    - [`short_affiliate_link`](#short_affiliate_link)

## Классы

### `AliRequests`

**Описание**: Класс для обработки запросов к AliExpress с использованием библиотеки `requests`.

**Методы**:
- `__init__`: Инициализирует класс `AliRequests`, загружает куки и создает сессию.
- `_load_webdriver_cookies_file`: Загружает куки из файла webdriver.
- `_refresh_session_cookies`: Обновляет сессионные куки.
- `_handle_session_id`: Обрабатывает идентификатор JSESSIONID в куках ответа.
- `make_get_request`: Выполняет GET-запрос с куками.
- `short_affiliate_link`: Получает короткую партнерскую ссылку.

**Параметры**:
- `webdriver_for_cookies` (str, optional): Название веб-драйвера для загрузки кук. По умолчанию `chrome`.

## Функции

### `_load_webdriver_cookies_file`

**Описание**: Загружает куки из файла webdriver.

**Параметры**:
- `webdriver_for_cookies` (str, optional): Имя веб-драйвера. По умолчанию `chrome`.

**Возвращает**:
- `bool`: `True`, если куки загружены успешно, иначе `False`.

**Вызывает исключения**:
- `FileNotFoundError`: Если файл с куками не найден.
- `ValueError`: Если файл с куками поврежден.
- `Exception`: При возникновении любых других ошибок при загрузке кук.

### `_refresh_session_cookies`

**Описание**: Обновляет сессионные куки.

**Вызывает исключения**:
- `requests.RequestException`: Если запрос на обновление сессионных кук не удался.
- `Exception`: При возникновении любой ошибки во время обновления сессионных кук.

### `_handle_session_id`

**Описание**: Обрабатывает `JSESSIONID` в куках ответа.

**Параметры**:
- `response_cookies` (RequestsCookieJar): Куки, полученные в ответе.

### `make_get_request`

**Описание**: Выполняет GET-запрос с куками.

**Параметры**:
- `url` (str): URL для выполнения GET-запроса.
- `cookies` (List[dict], optional): Список кук для использования в запросе. По умолчанию `None`.
- `headers` (dict, optional): Заголовки для включения в запрос. По умолчанию `None`.

**Возвращает**:
- `requests.Response | bool`: Объект `requests.Response` в случае успешного выполнения запроса или `False` в случае ошибки.

**Вызывает исключения**:
- `requests.RequestException`: Если запрос не удался.
- `Exception`: При возникновении любой ошибки во время выполнения GET-запроса.

### `short_affiliate_link`

**Описание**: Получает короткую партнерскую ссылку.

**Параметры**:
- `link_url` (str): URL для сокращения.

**Возвращает**:
- `requests.Response | bool`: Объект `requests.Response` в случае успешного выполнения запроса или `False` в случае ошибки.