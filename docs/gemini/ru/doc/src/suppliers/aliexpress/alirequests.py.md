# Модуль для работы с запросами к AliExpress
=================================================

Модуль `alirequests.py` предоставляет класс `AliRequests`, предназначенный для упрощения выполнения HTTP-запросов к AliExpress с использованием библиотеки `requests`. Класс автоматически управляет cookies, User-Agent и обработкой сессий.

## Обзор

Модуль содержит класс `AliRequests`, который инкапсулирует логику для выполнения HTTP-запросов к AliExpress. Он автоматически управляет cookies, User-Agent и обработкой сессий, что упрощает взаимодействие с API AliExpress.

## Подробнее

Этот модуль предназначен для упрощения взаимодействия с API AliExpress. Он предоставляет удобный интерфейс для выполнения GET-запросов, обработки cookies и управления сессиями.

## Классы

### `AliRequests`

**Описание**: Класс для выполнения запросов к AliExpress с использованием библиотеки `requests`.

**Принцип работы**:
1.  При инициализации загружает cookies из файла, если он существует. Файл содержит сериализованный список cookies, сохраненных веб-драйвером.
2.  Управляет cookies для поддержания сессии с AliExpress.
3.  Предоставляет методы для выполнения GET-запросов и получения коротких партнерских ссылок.

**Аттрибуты**:
-   `cookies_jar` (RequestsCookieJar): Объект для хранения cookies.
-   `session_id` (str | None): Идентификатор сессии.
-   `headers` (dict): Заголовки HTTP-запроса, включая User-Agent.
-   `session` (requests.Session): Объект сессии `requests` для выполнения запросов.

**Методы**:
-   `__init__(webdriver_for_cookies: str = 'chrome')`: Инициализирует класс `AliRequests`.
-   `_load_webdriver_cookies_file(webdriver_for_cookies: str = 'chrome') -> bool`: Загружает cookies из файла веб-драйвера.
-   `_refresh_session_cookies()`: Обновляет cookies сессии.
-   `_handle_session_id(response_cookies)`: Обрабатывает JSESSIONID в cookies ответа.
-   `make_get_request(self, url: str, cookies: List[dict] = None, headers: dict = None)`: Выполняет GET-запрос с заданными cookies и заголовками.
-   `short_affiliate_link(self, link_url: str)`: Получает короткую партнерскую ссылку.

### `__init__`

```python
def __init__(self, webdriver_for_cookies: str = 'chrome'):
    """ Initializes the AliRequests class.

    @param webdriver_for_cookies The name of the webdriver for loading cookies.
    """
    ...
```

**Назначение**: Инициализирует класс `AliRequests`, загружает cookies, устанавливает User-Agent и создает сессию `requests`.

**Параметры**:
-   `webdriver_for_cookies` (str): Название веб-драйвера для загрузки cookies. По умолчанию `'chrome'`.

**Как работает функция**:
1.  Создает экземпляр `RequestsCookieJar` для хранения cookies.
2.  Инициализирует `session_id` как `None`.
3.  Устанавливает случайный `User-Agent` с помощью библиотеки `fake_useragent`.
4.  Создает объект сессии `requests.Session()`.
5.  Вызывает метод `_load_webdriver_cookies_file` для загрузки cookies из файла.

```
Инициализация AliRequests
│
├──► Создание RequestsCookieJar
│
├──► Установка User-Agent
│
├──► Создание requests.Session
│
└──► Загрузка cookies из файла (если есть)
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

**Назначение**: Загружает cookies из файла, сохраненного веб-драйвером.

**Параметры**:
-   `webdriver_for_cookies` (str): Название веб-драйвера. По умолчанию `'chrome'`.

**Возвращает**:
-   `bool`: `True`, если cookies успешно загружены, `False` в противном случае.

**Вызывает исключения**:
-   `FileNotFoundError`: Если файл с cookies не найден.
-   `ValueError`: Если файл содержит некорректные данные.
-   `Exception`: При возникновении других ошибок при загрузке cookies.

**Как работает функция**:
1.  Формирует путь к файлу с cookies на основе переданного имени веб-драйвера.
2.  Пытается открыть файл и загрузить cookies с помощью `pickle`.
3.  Для каждого cookie устанавливает значения домена, пути, безопасности и HTTPOnly атрибутов.
4.  Логирует успешную загрузку cookies или ошибку, если загрузка не удалась.
5.  После загрузки вызывает метод `_refresh_session_cookies` для обновления cookies сессии.

```
Загрузка cookies из файла
│
├──► Формирование пути к файлу
│
├──► Чтение файла (pickle)
│
├──► Установка значений cookie
│   │
│   ├──► domain
│   │
│   ├──► path
│   │
│   ├──► secure
│   │
│   └──► HttpOnly
│
├──► Обновление cookies сессии
│
└──► Логирование результата
```

**Примеры**:

```python
ali_requests = AliRequests('chrome')
success = ali_requests._load_webdriver_cookies_file('chrome')
print(success)
```

### `_refresh_session_cookies`

```python
def _refresh_session_cookies(self):
    """ Refreshes session cookies."""
    ...
```

**Назначение**: Обновляет cookies сессии, выполняя GET-запрос к AliExpress.

**Как работает функция**:
1.  Выполняет GET-запрос к `https://portals.aliexpress.com`.
2.  Если `cookies_jar` не пустой, добавляет cookies к запросу.
3.  Вызывает метод `_handle_session_id` для обработки JSESSIONID из cookies ответа.
4.  Логирует ошибки, если запрос не удался.

```
Обновление cookies сессии
│
├──► GET-запрос к AliExpress
│
├──► Добавление cookies к запросу (если есть)
│
└──► Обработка JSESSIONID
```

### `_handle_session_id`

```python
def _handle_session_id(self, response_cookies):
    """ Handles the JSESSIONID in response cookies."""
    ...
```

**Назначение**: Обрабатывает JSESSIONID из cookies ответа, чтобы поддерживать сессию.

**Параметры**:
-   `response_cookies`: Cookies, полученные в ответе на HTTP-запрос.

**Как работает функция**:
1.  Перебирает cookies в ответе.
2.  Если находит cookie с именем `JSESSIONID`:
    *   Если `session_id` уже установлен и совпадает с новым значением, выходит из функции.
    *   Иначе обновляет `session_id` и добавляет cookie в `cookies_jar`.
3.  Логирует предупреждение, если JSESSIONID не найден.

```
Обработка JSESSIONID
│
├──► Перебор cookies
│
├──► Поиск JSESSIONID
│
└──► Обновление session_id и cookies_jar (если найден)
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

**Назначение**: Выполняет GET-запрос с заданными cookies и заголовками.

**Параметры**:
-   `url` (str): URL для выполнения GET-запроса.
-   `cookies` (List[dict] | None): Список cookies для использования в запросе. По умолчанию `None`.
-   `headers` (dict | None): Дополнительные заголовки для включения в запрос. По умолчанию `None`.

**Возвращает**:
-   `requests.Response`: Объект `requests.Response` в случае успеха.
-   `False`: В случае ошибки.

**Вызывает исключения**:
-   `requests.RequestException`: Если запрос завершился неудачей.
-   `Exception`: При возникновении других ошибок.

**Как работает функция**:
1.  Обновляет cookies сессии из `cookies_jar`.
2.  Выполняет GET-запрос к заданному URL с заданными заголовками.
3.  Вызывает `resp.raise_for_status()` для проверки статуса ответа.
4.  Вызывает метод `_handle_session_id` для обработки JSESSIONID из cookies ответа.
5.  Возвращает объект `requests.Response` в случае успеха.
6.  Логирует ошибки, если запрос не удался.

```
Выполнение GET-запроса
│
├──► Обновление cookies сессии
│
├──► GET-запрос к URL
│
├──► Проверка статуса ответа
│
└──► Обработка JSESSIONID
```

**Примеры**:

```python
ali_requests = AliRequests()
response = ali_requests.make_get_request('https://www.aliexpress.com/')
if response:
    print(f'Status code: {response.status_code}')
else:
    print('Request failed')
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

**Назначение**: Получает короткую партнерскую ссылку для заданного URL.

**Параметры**:
-   `link_url` (str): URL для сокращения.

**Возвращает**:
-   `requests.Response`: Объект `requests.Response` в случае успеха.
-   `False`: В случае ошибки.

**Как работает функция**:
1.  Формирует URL для запроса короткой партнерской ссылки.
2.  Вызывает метод `make_get_request` для выполнения GET-запроса.
3.  Возвращает результат выполнения запроса.

```
Получение короткой партнерской ссылки
│
├──► Формирование URL запроса
│
└──► Выполнение GET-запроса
```

**Примеры**:

```python
ali_requests = AliRequests()
response = ali_requests.short_affiliate_link('https://www.aliexpress.com/item/1234567890.html')
if response:
    print(f'Status code: {response.status_code}')
else:
    print('Request failed')