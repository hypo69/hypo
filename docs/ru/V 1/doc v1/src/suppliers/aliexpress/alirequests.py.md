# Модуль `alirequests`

## Обзор

Модуль `alirequests` предназначен для работы с запросами к AliExpress. Он включает в себя функциональность для загрузки cookies из файла, обновления cookies сессии и выполнения GET-запросов. Модуль использует библиотеку `requests` для выполнения HTTP-запросов и модуль `logger` для логирования.

## Подробней

Этот модуль предоставляет класс `AliRequests`, который инкапсулирует логику для взаимодействия с API AliExpress. Он автоматически управляет cookies, загружая их из файла, и поддерживает сессию для выполнения запросов. Это особенно важно для работы с партнерской программой AliExpress, где требуется авторизация и отслеживание сессии. Расположение файла в проекте указывает на то, что он является частью подсистемы, отвечающей за взаимодействие с AliExpress.

## Классы

### `AliRequests`

**Описание**: Класс `AliRequests` предназначен для обработки запросов к AliExpress с использованием библиотеки `requests`.

**Методы**:
- `__init__`: Инициализирует экземпляр класса `AliRequests`.
- `_load_webdriver_cookies_file`: Загружает cookies из файла, созданного драйвером веб-браузера.
- `_refresh_session_cookies`: Обновляет cookies сессии.
- `_handle_session_id`: Обрабатывает `JSESSIONID` из cookies ответа.
- `make_get_request`: Выполняет GET-запрос с использованием cookies.
- `short_affiliate_link`: Генерирует короткую партнерскую ссылку.

**Параметры**:
- `webdriver_for_cookies` (str, optional): Имя веб-драйвера, используемого для загрузки cookies. По умолчанию `'chrome'`.

**Примеры**

```python
from src.suppliers.aliexpress.alirequests import AliRequests

ali_requests = AliRequests(webdriver_for_cookies='chrome')
```

## Функции

### `__init__`

```python
def __init__(self, webdriver_for_cookies: str = 'chrome'):
    """ Initializes the AliRequests class.

    @param webdriver_for_cookies The name of the webdriver for loading cookies.
    """
    ...
```

**Описание**: Инициализирует класс `AliRequests`, загружает cookies и устанавливает User-Agent.

**Параметры**:
- `webdriver_for_cookies` (str, optional): Имя веб-драйвера, используемого для загрузки cookies. По умолчанию `'chrome'`.

**Примеры**:

```python
ali_requests = AliRequests(webdriver_for_cookies='firefox')
```

### `_load_webdriver_cookies_file`

```python
def _load_webdriver_cookies_file(self, webdriver_for_cookies: str = 'chrome') -> bool:
    """ Loads cookies from a webdriver file.

    @param webdriver_for_cookies The name of the webdriver.
    @returns True if cookies loaded successfully, False otherwise.
    """
    ...
```

**Описание**: Загружает cookies из файла, созданного драйвером веб-браузера.

**Параметры**:
- `webdriver_for_cookies` (str, optional): Имя веб-драйвера. По умолчанию `'chrome'`.

**Возвращает**:
- `bool`: `True`, если cookies успешно загружены, `False` в противном случае.

**Вызывает исключения**:
- `FileNotFoundError`: Если файл с cookies не найден.
- `ValueError`: Если файл с cookies содержит некорректные данные.
- `Exception`: Если произошла ошибка при загрузке cookies.

**Примеры**:

```python
ali_requests = AliRequests()
success = ali_requests._load_webdriver_cookies_file(webdriver_for_cookies='chrome')
if success:
    print("Cookies loaded successfully")
else:
    print("Failed to load cookies")
```

### `_refresh_session_cookies`

```python
def _refresh_session_cookies(self):
    """ Refreshes session cookies."""
    ...
```

**Описание**: Обновляет cookies сессии, выполняя GET-запрос к `https://portals.aliexpress.com`.

**Вызывает исключения**:
- `requests.RequestException`: Если не удалось выполнить запрос для обновления cookies.
- `Exception`: Если произошла ошибка при обновлении cookies.

**Примеры**:

```python
ali_requests = AliRequests()
ali_requests._load_webdriver_cookies_file(webdriver_for_cookies='chrome')
ali_requests._refresh_session_cookies()
```

### `_handle_session_id`

```python
def _handle_session_id(self, response_cookies):
    """ Handles the JSESSIONID in response cookies."""
    ...
```

**Описание**: Обрабатывает `JSESSIONID` из cookies ответа, сохраняя его в cookies jar.

**Параметры**:
- `response_cookies`: Cookies, полученные в ответе на запрос.

**Примеры**:

```python
import requests
from src.suppliers.aliexpress.alirequests import AliRequests

ali_requests = AliRequests()
response = requests.get('https://portals.aliexpress.com')
ali_requests._handle_session_id(response.cookies)
```

### `make_get_request`

```python
def make_get_request(self, url: str, cookies: List[dict] = None, headers: dict = None):
    """ Makes a GET request with cookies.

    @param url The URL to make the GET request to.
    @param cookies List of cookies to use for the request.
    @param headers Optional headers to include in the request.

    @returns requests.Response object if successful, False otherwise.
    """
    ...
```

**Описание**: Выполняет GET-запрос с использованием cookies.

**Параметры**:
- `url` (str): URL для выполнения GET-запроса.
- `cookies` (List[dict], optional): Список cookies для использования в запросе. По умолчанию `None`.
- `headers` (dict, optional): Дополнительные заголовки для включения в запрос. По умолчанию `None`.

**Возвращает**:
- `requests.Response`: Объект `requests.Response` в случае успеха, `False` в противном случае.

**Вызывает исключения**:
- `requests.RequestException`: Если запрос завершился неудачей.
- `Exception`: Если произошла ошибка при выполнении GET-запроса.

**Примеры**:

```python
ali_requests = AliRequests()
response = ali_requests.make_get_request(url='https://www.aliexpress.com')
if response:
    print(f"Request successful with status code: {response.status_code}")
else:
    print("Request failed")
```

### `short_affiliate_link`

```python
def short_affiliate_link(self, link_url: str):
    """ Get a short affiliate link.

    @param link_url The URL to shorten.

    @returns requests.Response object if successful, False otherwise.
    """
    ...
```

**Описание**: Генерирует короткую партнерскую ссылку.

**Параметры**:
- `link_url` (str): URL для укорачивания.

**Возвращает**:
- `requests.Response`: Объект `requests.Response` в случае успеха, `False` в противном случае.

**Примеры**:

```python
ali_requests = AliRequests()
short_link = ali_requests.short_affiliate_link(link_url='https://www.aliexpress.com/item/1234567890.html')
if short_link:
    print(f"Short affiliate link generated successfully")
else:
    print("Failed to generate short affiliate link")
```