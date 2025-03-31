# Модуль для работы с запросами к AliExpress

## Обзор

Модуль `alirequests.py` предназначен для обработки запросов к AliExpress с использованием библиотеки `requests`. Он включает в себя функциональность для загрузки cookies из файлов, управления сессиями и выполнения GET-запросов.

## Подробней

Модуль содержит класс `AliRequests`, который упрощает взаимодействие с AliExpress, автоматически управляя cookies и сессиями. Это позволяет выполнять запросы, требующие аутентификации, и обеспечивает стабильность соединения. Модуль использует логирование для отслеживания ошибок и успешных операций.

## Классы

### `AliRequests`

**Описание**: Класс `AliRequests` предназначен для управления запросами к AliExpress.

**Как работает класс**:
Класс инициализируется с настройками для работы с cookies и заголовками. Он загружает cookies из файла, создает сессию `requests` и предоставляет методы для выполнения GET-запросов и получения коротких партнерских ссылок.

**Методы**:
- `__init__`: Инициализирует экземпляр класса `AliRequests`.
- `_load_webdriver_cookies_file`: Загружает cookies из файла, созданного webdriver.
- `_refresh_session_cookies`: Обновляет cookies сессии.
- `_handle_session_id`: Обрабатывает идентификатор сессии JSESSIONID.
- `make_get_request`: Выполняет GET-запрос с заданными параметрами.
- `short_affiliate_link`: Генерирует короткую партнерскую ссылку.

#### `__init__`

```python
def __init__(self, webdriver_for_cookies: str = 'chrome'):
    """ Initializes the AliRequests class.

    @param webdriver_for_cookies The name of the webdriver for loading cookies.
    """
    ...
```

**Описание**: Инициализирует экземпляр класса `AliRequests`.

**Как работает функция**:
Конструктор класса `AliRequests` инициализирует куки, заголовки и сессию. Он загружает cookies из файла, если это удается, и устанавливает User-Agent.

**Параметры**:
- `webdriver_for_cookies` (str, optional): Имя веб-драйвера для загрузки cookies. По умолчанию `'chrome'`.

#### `_load_webdriver_cookies_file`

```python
def _load_webdriver_cookies_file(self, webdriver_for_cookies: str = 'chrome') -> bool:
    """ Loads cookies from a webdriver file.

    @param webdriver_for_cookies The name of the webdriver.
    @returns True if cookies loaded successfully, False otherwise.
    """
    ...
```

**Описание**: Загружает cookies из файла, созданного веб-драйвером.

**Как работает функция**:
Функция пытается открыть файл с cookies, десериализовать его содержимое и установить cookies для текущего сеанса. Если файл не найден или происходит ошибка десериализации, функция логирует ошибку и возвращает `False`.

**Параметры**:
- `webdriver_for_cookies` (str, optional): Имя веб-драйвера. По умолчанию `'chrome'`.

**Возвращает**:
- `bool`: `True`, если cookies успешно загружены, `False` в противном случае.

**Вызывает исключения**:
- `FileNotFoundError`: Если файл с cookies не найден.
- `ValueError`: Если возникает ошибка при десериализации cookies.
- `Exception`: При возникновении любой другой ошибки.

#### `_refresh_session_cookies`

```python
def _refresh_session_cookies(self):
    """ Refreshes session cookies."""
    ...
```

**Описание**: Обновляет cookies сессии.

**Как работает функция**:
Функция отправляет GET-запрос на указанный URL, чтобы обновить cookies сессии. Если cookies успешно обновлены, они сохраняются для дальнейших запросов. В случае ошибки при запросе или обработке cookies, функция логирует ошибку.

**Параметры**:
- Нет

**Вызывает исключения**:
- `requests.RequestException`: Если возникает ошибка при выполнении запроса.
- `Exception`: При возникновении любой другой ошибки.

#### `_handle_session_id`

```python
def _handle_session_id(self, response_cookies):
    """ Handles the JSESSIONID in response cookies."""
    ...
```

**Описание**: Обрабатывает идентификатор сессии JSESSIONID в cookies ответа.

**Как работает функция**:
Функция проверяет наличие cookie с именем `JSESSIONID` в cookies ответа. Если такой cookie найден, и его значение отличается от текущего `session_id`, он обновляется как в атрибуте `self.session_id`, так и в `self.cookies_jar`.

**Параметры**:
- `response_cookies`: Cookies, полученные в ответе на HTTP-запрос.

#### `make_get_request`

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

**Описание**: Выполняет GET-запрос с заданными параметрами.

**Как работает функция**:
Функция выполняет GET-запрос к указанному URL, используя cookies и заголовки, переданные в качестве аргументов. Если запрос выполнен успешно, функция возвращает объект `requests.Response`. В случае ошибки при выполнении запроса, функция логирует ошибку и возвращает `False`.

**Параметры**:
- `url` (str): URL для выполнения GET-запроса.
- `cookies` (List[dict], optional): Список cookies для использования в запросе.
- `headers` (dict, optional): Заголовки для включения в запрос.

**Возвращает**:
- `requests.Response`: Объект `requests.Response` в случае успеха, `False` в противном случае.

**Вызывает исключения**:
- `requests.RequestException`: Если возникает ошибка при выполнении запроса.
- `Exception`: При возникновении любой другой ошибки.

#### `short_affiliate_link`

```python
def short_affiliate_link(self, link_url: str):
    """ Get a short affiliate link.

    @param link_url The URL to shorten.

    @returns requests.Response object if successful, False otherwise.
    """
    ...
```

**Описание**: Получает короткую партнерскую ссылку.

**Как работает функция**:
Функция генерирует короткую партнерскую ссылку на основе предоставленного URL. Она использует метод `make_get_request` для выполнения GET-запроса к сервису сокращения ссылок.

**Параметры**:
- `link_url` (str): URL для сокращения.

**Возвращает**:
- `requests.Response`: Объект `requests.Response` в случае успеха, `False` в противном случае.