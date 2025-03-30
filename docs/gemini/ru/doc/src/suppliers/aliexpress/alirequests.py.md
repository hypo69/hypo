# Модуль для работы с запросами к AliExpress

## Обзор

Модуль `alirequests.py` предназначен для осуществления HTTP-запросов к AliExpress с использованием библиотеки `requests`. Он включает в себя функциональность для управления cookie-файлами, заголовками запросов и обработку сессий. Модуль предоставляет класс `AliRequests`, который упрощает взаимодействие с API AliExpress, обеспечивая автоматическую обработку сессионных cookie и пользовательских агентов.

## Подробней

Этот модуль играет важную роль в процессе сбора данных с AliExpress, так как он предоставляет инструменты для эмуляции поведения браузера и обхода ограничений, связанных с аутентификацией и отслеживанием сессий. Он использует библиотеку `requests` для отправки HTTP-запросов, а также `fake_useragent` для генерации случайных User-Agent, что помогает избежать блокировок со стороны сервера.

## Классы

### `AliRequests`

**Описание**: Класс `AliRequests` предназначен для управления HTTP-запросами к AliExpress. Он включает в себя функциональность для загрузки cookie-файлов, обновления сессионных cookie, установки заголовков запросов и выполнения GET-запросов.

**Методы**:
- `__init__`: Инициализирует экземпляр класса `AliRequests`.
- `_load_webdriver_cookies_file`: Загружает cookie-файлы из указанного файла, созданного webdriver.
- `_refresh_session_cookies`: Обновляет сессионные cookie, выполняя GET-запрос к AliExpress.
- `_handle_session_id`: Обрабатывает JSESSIONID, полученный в cookie ответа.
- `make_get_request`: Выполняет GET-запрос с заданными параметрами.
- `short_affiliate_link`: Получает короткую партнерскую ссылку.

**Параметры**:
- `webdriver_for_cookies` (str): Имя webdriver, используемого для загрузки cookie-файлов. По умолчанию `'chrome'`.

**Примеры**
```python
from src.suppliers.aliexpress.alirequests import AliRequests

# Пример использования класса AliRequests
ali_requests = AliRequests(webdriver_for_cookies='chrome')
```

## Функции

### `__init__`

```python
def __init__(self, webdriver_for_cookies: str = 'chrome'):
    """ Initializes the AliRequests class.

    @param webdriver_for_cookies The name of the webdriver for loading cookies.
    """
```

**Описание**: Инициализирует класс `AliRequests`, загружает cookie-файлы и устанавливает заголовки запросов.

**Параметры**:
- `webdriver_for_cookies` (str): Имя webdriver, используемого для загрузки cookie-файлов. По умолчанию `'chrome'`.

**Примеры**:
```python
ali_requests = AliRequests(webdriver_for_cookies='chrome')
```

### `_load_webdriver_cookies_file`

```python
def _load_webdriver_cookies_file(self, webdriver_for_cookies: str = 'chrome') -> bool:
    """ Loads cookies from a webdriver file.

    @param webdriver_for_cookies The name of the webdriver.
    @returns True if cookies loaded successfully, False otherwise.
    """
```

**Описание**: Загружает cookie-файлы из файла, созданного webdriver.

**Параметры**:
- `webdriver_for_cookies` (str): Имя webdriver, используемого для загрузки cookie-файлов. По умолчанию `'chrome'`.

**Возвращает**:
- `bool`: `True`, если cookie-файлы успешно загружены, `False` в противном случае.

**Вызывает исключения**:
- `FileNotFoundError`: Если файл с cookie не найден.
- `ValueError`: Если файл с cookie имеет неверный формат.
- `Exception`: В случае возникновения других ошибок при загрузке cookie.

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
```

**Описание**: Обновляет сессионные cookie, выполняя GET-запрос к AliExpress.

**Примеры**:
```python
ali_requests = AliRequests()
ali_requests._load_webdriver_cookies_file()
ali_requests._refresh_session_cookies()
```

### `_handle_session_id`

```python
def _handle_session_id(self, response_cookies):
    """ Handles the JSESSIONID in response cookies."""
```

**Описание**: Обрабатывает JSESSIONID, полученный в cookie ответа.

**Параметры**:
- `response_cookies`: Cookie, полученные в ответе от сервера.

**Примеры**:
```python
import requests
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
```

**Описание**: Выполняет GET-запрос с заданными параметрами.

**Параметры**:
- `url` (str): URL для выполнения GET-запроса.
- `cookies` (List[dict], optional): Список cookie для использования в запросе. По умолчанию `None`.
- `headers` (dict, optional): Дополнительные заголовки для включения в запрос. По умолчанию `None`.

**Возвращает**:
- `requests.Response`: Объект `requests.Response` в случае успеха, `False` в противном случае.

**Вызывает исключения**:
- `requests.RequestException`: В случае ошибки при выполнении запроса.
- `Exception`: В случае возникновения других ошибок при выполнении запроса.

**Примеры**:
```python
ali_requests = AliRequests()
response = ali_requests.make_get_request(url='https://portals.aliexpress.com')
if response:
    print("Request successful")
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
```

**Описание**: Получает короткую партнерскую ссылку.

**Параметры**:
- `link_url` (str): URL для сокращения.

**Возвращает**:
- `requests.Response`: Объект `requests.Response` в случае успеха, `False` в противном случае.

**Примеры**:
```python
ali_requests = AliRequests()
response = ali_requests.short_affiliate_link(link_url='https://aliexpress.com/item/1234567890.html')
if response:
    print("Short link generated successfully")
else:
    print("Failed to generate short link")
```