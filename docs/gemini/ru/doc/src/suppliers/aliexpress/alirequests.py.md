# Модуль для работы с запросами к AliExpress
=================================================

Модуль `alirequests.py` предназначен для упрощения выполнения HTTP-запросов к AliExpress, включая обработку cookies и управление сессиями.
Он содержит класс :class:`AliRequests`, который предоставляет методы для выполнения GET-запросов, обновления cookies и генерации коротких партнерских ссылок.

## Оглавление
- [Обзор](#обзор)
- [Подробнее](#подробнее)
- [Классы](#классы)
    - [AliRequests](#AliRequests)
        - [Методы](#Методы)
            - [`__init__`](#__init__)
            - [`_load_webdriver_cookies_file`](#_load_webdriver_cookies_file)
            - [`_refresh_session_cookies`](#_refresh_session_cookies)
            - [`_handle_session_id`](#_handle_session_id)
            - [`make_get_request`](#make_get_request)
            - [`short_affiliate_link`](#short_affiliate_link)

## Обзор

Модуль `alirequests.py` предоставляет класс `AliRequests`, который упрощает взаимодействие с API AliExpress. 
Он автоматически управляет cookies, поддерживает сессии и позволяет выполнять GET-запросы. 
Модуль также включает функциональность для сокращения партнерских ссылок.

## Подробнее

Этот модуль предназначен для использования в проектах, требующих взаимодействия с AliExpress API. 
Он обеспечивает удобный интерфейс для выполнения запросов, автоматически обрабатывая cookies и управляя сессиями. 
Класс `AliRequests` использует библиотеку `requests` для выполнения HTTP-запросов и модуль `pickle` для работы с файлами cookies.

## Классы

### `AliRequests`

**Описание**: Класс `AliRequests` предназначен для обработки запросов к AliExpress с использованием библиотеки `requests`.

**Принцип работы**:
1.  **Инициализация**: При инициализации класса создается сессия `requests.Session` для хранения cookies и заголовков.
2.  **Загрузка Cookies**: Cookies загружаются из файла, указанного в параметре `webdriver_for_cookies`, для имитации сессии браузера.
3.  **Управление сессией**: Класс автоматически обновляет и обрабатывает `JSESSIONID` для поддержания активной сессии.
4.  **Выполнение запросов**: Предоставляет методы для выполнения GET-запросов с автоматическим управлением cookies и обработкой ошибок.
5.  **Сокращение ссылок**: Позволяет генерировать короткие партнерские ссылки.

#### Методы:
   - `__init__`: Инициализирует класс AliRequests.
   - `_load_webdriver_cookies_file`: Загружает cookies из файла, созданного webdriver.
   - `_refresh_session_cookies`: Обновляет cookies сессии.
   - `_handle_session_id`: Обрабатывает JSESSIONID из cookies ответа.
   - `make_get_request`: Выполняет GET-запрос с заданными параметрами.
   - `short_affiliate_link`: Генерирует короткую партнерскую ссылку.

#### `__init__`
```python
def __init__(self, webdriver_for_cookies: str = 'chrome'):
    """
    Инициализирует класс `AliRequests`.

    Args:
        webdriver_for_cookies (str, optional): Имя веб-драйвера для загрузки cookies. По умолчанию 'chrome'.
    """
    ...
```

**Назначение**: Инициализирует экземпляр класса `AliRequests`, настраивая сессию для выполнения HTTP-запросов к AliExpress.

**Параметры**:
- `webdriver_for_cookies` (str, optional): Определяет, из какого файла cookie веб-драйвера загружать. По умолчанию используется 'chrome'.

**Как работает функция**:

1.  Инициализирует пустой контейнер для хранения cookies (`self.cookies_jar`).
2.  Устанавливает User-Agent (`self.headers`) для имитации запросов от браузера.
3.  Создает объект сессии `requests.Session()` для хранения cookies между запросами.
4.  Вызывает метод `_load_webdriver_cookies_file` для загрузки cookies из файла, соответствующего указанному веб-драйверу.

**Примеры**:
```python
# Пример создания экземпляра класса AliRequests с использованием cookies Chrome
ali_requests = AliRequests(webdriver_for_cookies='chrome')

# Пример создания экземпляра класса AliRequests с использованием cookies Firefox
ali_requests = AliRequests(webdriver_for_cookies='firefox')
```

#### `_load_webdriver_cookies_file`
```python
def _load_webdriver_cookies_file(self, webdriver_for_cookies: str = 'chrome') -> bool:
    """
    Загружает cookies из файла, созданного веб-драйвером.

    Args:
        webdriver_for_cookies (str, optional): Имя веб-драйвера. По умолчанию 'chrome'.

    Returns:
        bool: `True`, если cookies успешно загружены, `False` в противном случае.
    """
    ...
```

**Назначение**: Загружает cookies из файла, сгенерированного веб-драйвером (например, Chrome или Firefox), для имитации поведения браузера при выполнении запросов.

**Параметры**:
- `webdriver_for_cookies` (str, optional): Имя веб-драйвера, cookies которого следует загрузить. По умолчанию 'chrome'.

**Возвращает**:
- `bool`: `True`, если cookies успешно загружены и применены к сессии, `False` в случае ошибки.

**Как работает функция**:

1.  Формирует путь к файлу cookie на основе переданного имени веб-драйвера и расположения в файловой системе.
2.  Пытается открыть файл cookie в бинарном режиме и загрузить из него список cookies с использованием `pickle.load`.
3.  Для каждого cookie из списка устанавливает его в `self.cookies_jar`, указывая домен, путь, параметры безопасности и другие атрибуты.
4.  После успешной загрузки cookies вызывает метод `_refresh_session_cookies` для обновления cookies сессии.
5.  В случае возникновения исключений, таких как `FileNotFoundError` или `ValueError`, логирует ошибку и возвращает `False`.

**Примеры**:
```python
# Пример загрузки cookies из файла Chrome
success = ali_requests._load_webdriver_cookies_file(webdriver_for_cookies='chrome')
if success:
    print("Cookies успешно загружены")
else:
    print("Не удалось загрузить cookies")

# Пример загрузки cookies из файла Firefox
success = ali_requests._load_webdriver_cookies_file(webdriver_for_cookies='firefox')
if success:
    print("Cookies успешно загружены")
else:
    print("Не удалось загрузить cookies")
```

#### `_refresh_session_cookies`
```python
def _refresh_session_cookies(self):
    """ Обновляет cookies сессии."""
    ...
```

**Назначение**: Обновляет cookies сессии, выполняя GET-запрос к AliExpress.

**Как работает функция**:

1. Определяет URL для обновления cookies (`https://portals.aliexpress.com`).
2. Выполняет GET-запрос к указанному URL, передавая текущие cookies и заголовки сессии.
3. Обрабатывает полученные cookies, извлекая `JSESSIONID` и обновляя его в `self.cookies_jar`.
4. В случае возникновения ошибок при выполнении запроса или обработке cookies логирует их.

**Примеры**:
```python
# Пример обновления cookies сессии
ali_requests._refresh_session_cookies()
```

#### `_handle_session_id`
```python
def _handle_session_id(self, response_cookies):
    """ Обрабатывает JSESSIONID в cookies ответа."""
    ...
```

**Назначение**: Обрабатывает `JSESSIONID`, полученный в cookies ответа от сервера, обновляя его в сессии.

**Параметры**:
- `response_cookies`: Cookies, полученные в ответе от сервера.

**Как работает функция**:

1.  Проходит по всем cookies в `response_cookies`.
2.  Ищет cookie с именем `JSESSIONID`.
3.  Если `JSESSIONID` найден, сравнивает его значение с текущим `self.session_id`. Если значения совпадают, функция завершается.
4.  Если `JSESSIONID` не совпадает с текущим или `self.session_id` еще не установлен, обновляет `self.session_id` и устанавливает cookie в `self.cookies_jar`.
5.  Если `JSESSIONID` не найден в cookies ответа, логирует предупреждение.

**Примеры**:
```python
# Пример обработки cookies ответа для обновления JSESSIONID
response = ali_requests.make_get_request(url='https://example.com')
if response:
    ali_requests._handle_session_id(response.cookies)
```

#### `make_get_request`
```python
def make_get_request(self, url: str, cookies: List[dict] = None, headers: dict = None):
    """ Выполняет GET-запрос с cookies.

    Args:
        url (str): URL для выполнения GET-запроса.
        cookies (List[dict], optional): Список cookies для использования в запросе. По умолчанию `None`.
        headers (dict, optional): Дополнительные заголовки для включения в запрос. По умолчанию `None`.

    Returns:
        requests.Response | False: Объект `requests.Response` в случае успеха, `False` в противном случае.
    """
    ...
```

**Назначение**: Выполняет GET-запрос к указанному URL с заданными cookies и заголовками.

**Параметры**:
- `url` (str): URL для выполнения GET-запроса.
- `cookies` (List[dict], optional): Список cookies для использования в запросе. По умолчанию `None`.
- `headers` (dict, optional): Дополнительные заголовки для включения в запрос. По умолчанию `None`.

**Возвращает**:
- `requests.Response | False`: Объект `requests.Response` в случае успеха, `False` в случае ошибки.

**Как работает функция**:

1.  Обновляет cookies сессии, добавляя cookies из `self.cookies_jar` в текущую сессию.
2.  Выполняет GET-запрос к указанному URL с заданными заголовками.
3.  Проверяет статус ответа и вызывает исключение `requests.RequestException` в случае ошибки.
4.  Обрабатывает полученные cookies, извлекая `JSESSIONID` и обновляя его в `self.cookies_jar`.
5.  Возвращает объект `requests.Response` в случае успеха.
6.  В случае возникновения ошибок логирует их и возвращает `False`.

**Примеры**:
```python
# Пример выполнения GET-запроса с использованием cookies и заголовков
url = 'https://example.com'
headers = {'Custom-Header': 'value'}
response = ali_requests.make_get_request(url=url, headers=headers)

if response:
    print("Запрос выполнен успешно")
    print(f"Код ответа: {response.status_code}")
    print(f"Содержимое: {response.text[:100]}...")
else:
    print("Ошибка при выполнении запроса")
```

#### `short_affiliate_link`
```python
def short_affiliate_link(self, link_url: str):
    """ Получает короткую партнерскую ссылку.

    Args:
        link_url (str): URL для сокращения.

    Returns:
        requests.Response | False: Объект `requests.Response` в случае успеха, `False` в противном случае.
    """
    ...
```

**Назначение**: Генерирует короткую партнерскую ссылку на основе предоставленного URL.

**Параметры**:
- `link_url` (str): URL, который нужно сократить.

**Возвращает**:
- `requests.Response | False`: Объект `requests.Response` в случае успеха, `False` в случае ошибки.

**Как работает функция**:

1.  Определяет базовый URL для генерации партнерских ссылок на AliExpress.
2.  Формирует полный URL запроса, добавляя параметры `trackId` и `targetUrl`.
3.  Вызывает метод `make_get_request` для выполнения GET-запроса к сформированному URL.
4.  Возвращает результат выполнения запроса.

**Примеры**:
```python
# Пример получения короткой партнерской ссылки
url = 'https://aliexpress.com/item/1234567890.html'
response = ali_requests.short_affiliate_link(link_url=url)

if response:
    print("Короткая партнерская ссылка получена")
    print(f"Код ответа: {response.status_code}")
    print(f"Содержимое: {response.text[:100]}...")
else:
    print("Ошибка при получении короткой партнерской ссылки")