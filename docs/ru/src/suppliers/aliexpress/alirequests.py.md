# Модуль для работы с запросами к AliExpress
=================================================

Модуль `alirequests.py` предназначен для обработки запросов к AliExpress с использованием библиотеки `requests`. Он включает в себя функциональность для управления куки, сессиями и создания GET-запросов.

## Обзор

Модуль предоставляет класс `AliRequests`, который облегчает взаимодействие с AliExpress, автоматически управляя куки и сессиями. Он также включает в себя методы для загрузки куки из файлов, обновления сессий и создания сокращенных партнерских ссылок.

## Подробнее

Этот модуль предназначен для упрощения процесса взаимодействия с API AliExpress. Он автоматически управляет куки и сессиями, что позволяет избежать ручной обработки этих аспектов. Модуль также предоставляет удобные методы для выполнения GET-запросов и создания сокращенных партнерских ссылок.

## Классы

### `AliRequests`

**Описание**: Класс `AliRequests` предназначен для обработки запросов к AliExpress с использованием библиотеки `requests`.

**Принцип работы**: Класс инициализируется с настройками для работы с куками и заголовками. Он загружает куки из файла, создает сессию `requests` и предоставляет методы для выполнения GET-запросов и управления сессиями.

**Атрибуты**:
- `cookies_jar` (RequestsCookieJar): Объект для хранения куки.
- `session_id` (str | None): Идентификатор сессии.
- `headers` (dict): Заголовки по умолчанию для запросов.
- `session` (requests.Session): Объект сессии для выполнения запросов.

**Методы**:
- `__init__(self, webdriver_for_cookies: str = 'chrome')`: Инициализирует класс `AliRequests`.
- `_load_webdriver_cookies_file(self, webdriver_for_cookies: str = 'chrome') -> bool`: Загружает куки из файла, созданного webdriver.
- `_refresh_session_cookies(self)`: Обновляет куки сессии.
- `_handle_session_id(self, response_cookies)`: Обрабатывает `JSESSIONID` из куки ответа.
- `make_get_request(self, url: str, cookies: List[dict] = None, headers: dict = None)`: Выполняет GET-запрос с заданными куками и заголовками.
- `short_affiliate_link(self, link_url: str)`: Создает сокращенную партнерскую ссылку.

## Функции

### `__init__`

```python
def __init__(self, webdriver_for_cookies: str = 'chrome'):
    """ Initializes the AliRequests class.

    @param webdriver_for_cookies The name of the webdriver for loading cookies.
    """
    self.cookies_jar = RequestsCookieJar()
    self.session_id = None
    self.headers = {'User-Agent': UserAgent().random}
    self.session = requests.Session()
    
    self._load_webdriver_cookies_file(webdriver_for_cookies)
```

**Назначение**: Инициализирует экземпляр класса `AliRequests`, устанавливая необходимые атрибуты и загружая куки.

**Параметры**:
- `webdriver_for_cookies` (str): Имя веб-драйвера, используемого для загрузки куки. По умолчанию `'chrome'`.

**Как работает функция**:

1.  Инициализация атрибутов:
    *   Создается пустой контейнер для хранения куки (`self.cookies_jar`).
    *   Идентификатор сессии устанавливается в `None` (`self.session_id`).
    *   Формируются заголовки по умолчанию, включающие случайный User-Agent (`self.headers`).
    *   Создается объект сессии `requests` (`self.session`).
2.  Загрузка куки:
    *   Вызывается метод `_load_webdriver_cookies_file` для загрузки куки из файла, связанного с указанным веб-драйвером.

```
Инициализация AliRequests
│
├── Создание RequestsCookieJar (cookies_jar)
│
├── Установка session_id = None
│
├── Формирование заголовков (headers)
│
├── Создание requests.Session (session)
│
└── Вызов _load_webdriver_cookies_file
```

**Примеры**:

```python
ali_requests = AliRequests()
ali_requests = AliRequests(webdriver_for_cookies='firefox')
```

### `_load_webdriver_cookies_file`

```python
def _load_webdriver_cookies_file(self, webdriver_for_cookies: str = 'chrome') -> bool:
    """ Loads cookies from a webdriver file.

    @param webdriver_for_cookies The name of the webdriver.
    @returns True if cookies loaded successfully, False otherwise.
    """
    cookie_file_path = Path(gs.dir_cookies, 'aliexpress.com', webdriver_for_cookies, 'cookie')

    try:
        with open(cookie_file_path, 'rb') as file:
            cookies_list = pickle.load(file)
            for cookie in cookies_list:
                self.cookies_jar.set(
                    cookie['name'],
                    cookie['value'],
                    domain=cookie.get('domain', ''),
                    path=cookie.get('path', '/'),
                    secure=bool(cookie.get('secure', False)),
                    rest={'HttpOnly': cookie.get('HttpOnly', 'false'), 'SameSite': cookie.get('SameSite', 'unspecified')},
                    expires=cookie.get('expirationDate')
                )
            logger.success(f"Cookies loaded from {cookie_file_path}")
            self._refresh_session_cookies()  # Refresh session cookies after loading
            return True
    except (FileNotFoundError, ValueError) as ex:
        logger.error(f"Failed to load cookies from {cookie_file_path}", ex)
        return False
    except Exception as ex:
        logger.error("An error occurred while loading cookies", ex)
        return False
```

**Назначение**: Загружает куки из файла, созданного веб-драйвером.

**Параметры**:
- `webdriver_for_cookies` (str): Имя веб-драйвера. По умолчанию `'chrome'`.

**Возвращает**:
- `bool`: `True`, если куки успешно загружены, `False` в противном случае.

**Как работает функция**:

1.  Формирование пути к файлу с куками:
    *   Путь к файлу формируется на основе имени веб-драйвера и стандартного местоположения файлов куки.
2.  Чтение куки из файла:
    *   Файл открывается в бинарном режиме для чтения.
    *   Куки загружаются из файла с использованием `pickle.load`.
    *   Каждый куки добавляется в `self.cookies_jar` с помощью метода `set`.
3.  Обработка исключений:
    *   Если файл не найден или возникают ошибки при чтении, регистрируется ошибка и возвращается `False`.
4.  Обновление куки сессии:
    *   После успешной загрузки куки вызывается метод `_refresh_session_cookies` для обновления куки в сессии.

```
Загрузка куки из файла
│
├── Формирование пути к файлу куки
│
├── Открытие файла куки
│
├── Загрузка списка куки из файла
│
├── Для каждого куки в списке:
│   │
│   └── Добавление куки в cookies_jar
│
├── Логирование успешной загрузки
│
├── Обновление куки сессии (_refresh_session_cookies)
│
└── Возврат True
│
└── Обработка исключений (FileNotFoundError, ValueError, Exception)
│   │
│   └── Логирование ошибки
│
└── Возврат False
```

**Примеры**:

```python
ali_requests = AliRequests()
success = ali_requests._load_webdriver_cookies_file()
success = ali_requests._load_webdriver_cookies_file(webdriver_for_cookies='firefox')
```

### `_refresh_session_cookies`

```python
def _refresh_session_cookies(self):
    """ Refreshes session cookies."""
    url = 'https://portals.aliexpress.com'
    try:
        if self.cookies_jar:
            resp = self.session.get(url, headers=self.headers, cookies=self.cookies_jar)
        else:
            resp = self.session.get(url, headers=self.headers)

        self._handle_session_id(resp.cookies)
    except requests.RequestException as ex:
        logger.error(f"Failed to refresh session cookies from {url}", ex)
    except Exception as ex:
        logger.error("An error occurred while refreshing session cookies", ex)
```

**Назначение**: Обновляет куки сессии, выполняя GET-запрос к указанному URL.

**Как работает функция**:

1.  Определение URL:
    *   Устанавливается URL для обновления куки сессии (`https://portals.aliexpress.com`).
2.  Выполнение GET-запроса:
    *   Выполняется GET-запрос к указанному URL с использованием текущей сессии и заголовков.
    *   Если `self.cookies_jar` не пуст, куки передаются в запросе.
3.  Обработка куки ответа:
    *   Вызывается метод `_handle_session_id` для обработки `JSESSIONID` из куки ответа.
4.  Обработка исключений:
    *   Если возникают ошибки при выполнении запроса, регистрируется ошибка.

```
Обновление куки сессии
│
├── Определение URL
│
├── Если cookies_jar не пуст:
│   │
│   └── Выполнение GET-запроса с куками
│
├── Иначе:
│   │
│   └── Выполнение GET-запроса без куки
│
├── Обработка куки ответа (_handle_session_id)
│
└── Обработка исключений (requests.RequestException, Exception)
│   │
│   └── Логирование ошибки
```

**Примеры**:

```python
ali_requests = AliRequests()
ali_requests._refresh_session_cookies()
```

### `_handle_session_id`

```python
def _handle_session_id(self, response_cookies):
    """ Handles the JSESSIONID in response cookies."""
    session_id_found = False
    for cookie in response_cookies:
        if cookie.name == 'JSESSIONID':
            if self.session_id == cookie.value:
                return
            self.session_id = cookie.value
            self.cookies_jar.set(
                cookie.name,
                cookie.value,
                domain=cookie.domain,
                path=cookie.path,
                secure=cookie.secure,
                rest={'HttpOnly': cookie._rest.get('HttpOnly', 'false'), 'SameSite': cookie._rest.get('SameSite', 'unspecified')},
                expires=cookie.expires
            )
            session_id_found = True
            break
    
    if not session_id_found:
        logger.warning("JSESSIONID not found in response cookies")
```

**Назначение**: Обрабатывает `JSESSIONID` из куки ответа, обновляя его в `self.cookies_jar`, если он изменился.

**Параметры**:
- `response_cookies` (requests.cookies.RequestsCookieJar): Куки, полученные в ответе на запрос.

**Как работает функция**:

1.  Поиск `JSESSIONID` в куки ответа:
    *   Перебираются все куки в `response_cookies`.
    *   Если найден куки с именем `JSESSIONID`:
        *   Если значение `JSESSIONID` совпадает с текущим `self.session_id`, функция завершается.
        *   Если значение `JSESSIONID` отличается, `self.session_id` обновляется, и куки добавляется в `self.cookies_jar`.
2.  Логирование отсутствия `JSESSIONID`:
    *   Если `JSESSIONID` не найден в куки ответа, регистрируется предупреждение.

```
Обработка JSESSIONID
│
├── Инициализация session_id_found = False
│
├── Для каждого куки в response_cookies:
│   │
│   └── Если имя куки == 'JSESSIONID':
│       │   │
│       │   └── Если значение куки == self.session_id:
│       │       │
│       │       └── Выход из функции
│       │   │
│       │   └── Обновление self.session_id
│       │   │
│       │   └── Добавление куки в self.cookies_jar
│       │   │
│       │   └── Установка session_id_found = True
│       │   │
│       │   └── Выход из цикла
│
├── Если session_id_found == False:
│   │
│   └── Логирование предупреждения об отсутствии JSESSIONID
```

**Примеры**:

```python
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
    headers = headers or self.headers
    try:
        self.session.cookies.update(self.cookies_jar)
        resp = self.session.get(url, headers=headers)
        resp.raise_for_status()

        self._handle_session_id(resp.cookies)

        return resp
    except requests.RequestException as ex:
        logger.error(f"Request to {url} failed", ex)
        return False
    except Exception as ex:
        logger.error(f"An error occurred while making a GET request to {url}", ex)
        return False
```

**Назначение**: Выполняет GET-запрос с заданными куки и заголовками.

**Параметры**:
- `url` (str): URL для выполнения GET-запроса.
- `cookies` (List[dict] | None): Список куки для использования в запросе. По умолчанию `None`.
- `headers` (dict | None): Заголовки для включения в запрос. По умолчанию `None`.

**Возвращает**:
- `requests.Response | False`: Объект `requests.Response` в случае успеха, `False` в противном случае.

**Как работает функция**:

1.  Подготовка заголовков:
    *   Если заголовки не переданы, используются заголовки по умолчанию (`self.headers`).
2.  Выполнение GET-запроса:
    *   Куки из `self.cookies_jar` добавляются в сессию.
    *   Выполняется GET-запрос к указанному URL с заданными заголовками.
    *   Проверяется статус ответа с помощью `resp.raise_for_status()`.
3.  Обработка куки ответа:
    *   Вызывается метод `_handle_session_id` для обработки `JSESSIONID` из куки ответа.
4.  Обработка исключений:
    *   Если возникают ошибки при выполнении запроса, регистрируется ошибка и возвращается `False`.

```
Выполнение GET-запроса
│
├── Подготовка заголовков
│
├── Обновление куки сессии
│
├── Выполнение GET-запроса
│
├── Проверка статуса ответа
│
├── Обработка куки ответа (_handle_session_id)
│
└── Возврат ответа
│
└── Обработка исключений (requests.RequestException, Exception)
│   │
│   └── Логирование ошибки
│
└── Возврат False
```

**Примеры**:

```python
ali_requests = AliRequests()
response = ali_requests.make_get_request('https://portals.aliexpress.com')
response = ali_requests.make_get_request('https://portals.aliexpress.com', headers={'Custom-Header': 'value'})
```

### `short_affiliate_link`

```python
def short_affiliate_link(self, link_url: str):
    """ Get a short affiliate link.

    @param link_url The URL to shorten.

    @returns requests.Response object if successful, False otherwise.
    """
    base_url = 'https://portals.aliexpress.com/affiportals/web/link_generator.htm'
    track_id = 'default'
    url = f"{base_url}?trackId={track_id}&targetUrl={link_url}"
    return self.make_get_request(url)
```

**Назначение**: Создает сокращенную партнерскую ссылку на основе предоставленного URL.

**Параметры**:
- `link_url` (str): URL для сокращения.

**Возвращает**:
- `requests.Response | False`: Объект `requests.Response` в случае успеха, `False` в противном случае.

**Как работает функция**:

1.  Формирование URL:
    *   Формируется URL для создания сокращенной партнерской ссылки на основе `base_url`, `track_id` и `link_url`.
2.  Выполнение GET-запроса:
    *   Вызывается метод `make_get_request` для выполнения GET-запроса к сформированному URL.

```
Создание сокращенной партнерской ссылки
│
├── Формирование URL
│
└── Выполнение GET-запроса (make_get_request)
```

**Примеры**:

```python
ali_requests = AliRequests()
short_link = ali_requests.short_affiliate_link('https://aliexpress.com/item/1234567890.html')