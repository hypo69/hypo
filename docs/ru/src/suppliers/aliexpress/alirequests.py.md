# Модуль `alirequests.py`

## Обзор

Модуль `alirequests.py` предназначен для обработки запросов к AliExpress с использованием библиотеки `requests`. Он включает в себя функциональность для загрузки файлов cookie, обновления сессионных cookie и выполнения GET-запросов.

## Подробней

Этот модуль является частью проекта `hypotez` и обеспечивает взаимодействие с AliExpress. Он использует библиотеку `requests` для отправки HTTP-запросов и управления cookie. Модуль позволяет загружать cookie из файла, обновлять сессионные cookie и выполнять GET-запросы к AliExpress.

## Классы

### `AliRequests`

**Описание**: Класс `AliRequests` предназначен для обработки запросов к AliExpress с использованием библиотеки `requests`. Он инициализирует сессию, загружает cookie из файла и предоставляет методы для выполнения GET-запросов.

**Как работает класс**:
1.  Класс инициализируется с указанием имени веб-драйвера для загрузки cookie.
2.  Создается объект `RequestsCookieJar` для хранения cookie.
3.  Устанавливаются заголовки User-Agent для имитации запросов от браузера.
4.  Создается объект `requests.Session` для управления сессией.
5.  Вызывается метод `_load_webdriver_cookies_file` для загрузки cookie из файла.

**Методы**:

*   `__init__`: Инициализирует класс `AliRequests`.
*   `_load_webdriver_cookies_file`: Загружает cookie из файла веб-драйвера.
*   `_refresh_session_cookies`: Обновляет сессионные cookie.
*   `_handle_session_id`: Обрабатывает JSESSIONID в cookie ответа.
*   `make_get_request`: Выполняет GET-запрос с использованием cookie.
*   `short_affiliate_link`: Возвращает короткую партнерскую ссылку.

## Функции

### `__init__`

```python
def __init__(self, webdriver_for_cookies: str = 'chrome'):
    """ Инициализирует класс AliRequests.

    Args:
        webdriver_for_cookies (str, optional): Имя веб-драйвера для загрузки файлов cookie. По умолчанию 'chrome'.
    """
    ...
```

**Назначение**: Инициализирует экземпляр класса `AliRequests`, настраивая сессию для выполнения запросов к AliExpress.

**Как работает функция**:

1.  Инициализирует `RequestsCookieJar` для хранения cookie.
2.  Устанавливает `session_id` в `None`.
3.  Устанавливает заголовки `User-Agent` для имитации запросов браузера.
4.  Инициализирует сессию `requests.Session`.
5.  Загружает cookie из файла, соответствующего указанному веб-драйверу.

### `_load_webdriver_cookies_file`

```python
def _load_webdriver_cookies_file(self, webdriver_for_cookies: str = 'chrome') -> bool:
    """ Загружает файлы cookie из файла веб-драйвера.

    Args:
        webdriver_for_cookies (str, optional): Имя веб-драйвера. По умолчанию 'chrome'.

    Returns:
        bool: `True`, если cookie успешно загружены, `False` в противном случае.

    Raises:
        FileNotFoundError: Если файл cookie не найден.
        ValueError: Если файл cookie содержит некорректные данные.
        Exception: Если произошла общая ошибка при загрузке cookie.
    """
    ...
```

**Назначение**: Загружает cookie из файла, который содержит cookie, сохраненные веб-драйвером.

**Как работает функция**:

1.  Формирует путь к файлу cookie на основе имени веб-драйвера.
2.  Открывает файл cookie в бинарном режиме.
3.  Загружает список cookie из файла с использованием `pickle.load`.
4.  Перебирает cookie и устанавливает их в `cookies_jar`.
5.  Обновляет сессионные cookie, вызывая метод `_refresh_session_cookies`.
6.  Логирует успешную загрузку cookie.
7.  В случае ошибки логирует ошибку и возвращает `False`.

### `_refresh_session_cookies`

```python
def _refresh_session_cookies(self):
    """ Обновляет сессионные файлы cookie.
    """
    ...
```

**Назначение**: Обновляет сессионные cookie, выполняя GET-запрос к AliExpress.

**Как работает функция**:

1.  Определяет URL для обновления cookie.
2.  Выполняет GET-запрос к указанному URL с использованием текущих cookie и заголовков.
3.  Обрабатывает полученные cookie для обновления `JSESSIONID`.
4.  В случае ошибки логирует ошибку.

### `_handle_session_id`

```python
def _handle_session_id(self, response_cookies):
    """ Обрабатывает JSESSIONID в cookie ответа.

    Args:
        response_cookies: cookie ответа.
    """
    ...
```

**Назначение**: Обрабатывает cookie ответа для извлечения и обновления `JSESSIONID`.

**Как работает функция**:

1.  Перебирает cookie в ответе.
2.  Ищет cookie с именем `JSESSIONID`.
3.  Если `JSESSIONID` найден, сравнивает его значение с текущим значением `session_id`.
4.  Если значение изменилось, обновляет `session_id` и устанавливает cookie в `cookies_jar`.
5.  Если `JSESSIONID` не найден, логирует предупреждение.

### `make_get_request`

```python
def make_get_request(self, url: str, cookies: List[dict] = None, headers: dict = None):
    """ Выполняет GET-запрос с использованием cookie.

    Args:
        url (str): URL для выполнения GET-запроса.
        cookies (List[dict], optional): Список cookie для использования в запросе. По умолчанию `None`.
        headers (dict, optional): Необязательные заголовки для включения в запрос. По умолчанию `None`.

    Returns:
        requests.Response | bool: Объект `requests.Response` в случае успеха, `False` в противном случае.
    """
    ...
```

**Назначение**: Выполняет GET-запрос к указанному URL с использованием предоставленных cookie и заголовков.

**Как работает функция**:

1.  Обновляет cookie сессии из `cookies_jar`.
2.  Выполняет GET-запрос к указанному URL с использованием заголовков и cookie.
3.  Обрабатывает ответ для обновления `JSESSIONID`.
4.  В случае успеха возвращает объект `requests.Response`.
5.  В случае ошибки логирует ошибку и возвращает `False`.

### `short_affiliate_link`

```python
def short_affiliate_link(self, link_url: str):
    """ Получает короткую партнерскую ссылку.

    Args:
        link_url (str): URL для сокращения.

    Returns:
        requests.Response | bool: Объект `requests.Response` в случае успеха, `False` в противном случае.
    """
    ...
```

**Назначение**: Генерирует короткую партнерскую ссылку на основе предоставленного URL.

**Как работает функция**:

1.  Определяет базовый URL для генерации партнерских ссылок.
2.  Формирует URL для запроса на основе базового URL и предоставленного URL.
3.  Вызывает метод `make_get_request` для выполнения GET-запроса к URL генерации партнерской ссылки.
4.  Возвращает результат выполнения GET-запроса.