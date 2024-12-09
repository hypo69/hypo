# Модуль alirequests.py

## Обзор

Этот модуль предоставляет класс `AliRequests` для работы с API AliExpress, включая загрузку кукисов из файлов веб-драйвера и выполнение GET-запросов. Он обрабатывает кукисы, обновляет сессию и проверяет наличие JSESSIONID.

## Классы

### `AliRequests`

**Описание**: Класс `AliRequests` отвечает за обработку запросов к AliExpress. Он загружает кукисы из файла, обновляет сессию и обрабатывает JSESSIONID.

**Методы**:

#### `__init__(self, webdriver_for_cookies: str = 'chrome')`

**Описание**: Инициализирует класс `AliRequests`. Загружает кукисы из файла веб-драйвера.

**Параметры**:

- `webdriver_for_cookies` (str, опционально): Название веб-драйвера для загрузки кукисов. По умолчанию 'chrome'.

#### `_load_webdriver_cookies_file(self, webdriver_for_cookies: str = 'chrome') -> bool`

**Описание**: Загружает кукисы из файла веб-драйвера.

**Параметры**:

- `webdriver_for_cookies` (str, опционально): Название веб-драйвера. По умолчанию 'chrome'.

**Возвращает**:

- bool: `True`, если кукисы загружены успешно; `False`, в противном случае.

**Обрабатывает исключения**:

- `FileNotFoundError`, `ValueError`: Если файл кукисов не найден или содержит некорректные данные.
- `Exception`: Общее исключение при ошибке загрузки.

#### `_refresh_session_cookies(self)`

**Описание**: Обновляет сессию кукисов.

**Обрабатывает исключения**:

- `requests.RequestException`: Если произошла ошибка при обновлении сессии.
- `Exception`: Общее исключение.

#### `_handle_session_id(self, response_cookies)`

**Описание**: Обрабатывает JSESSIONID в кукисах ответа.

**Параметры**:

- `response_cookies`: Кукисы ответа.

**Обрабатывает исключения**:

- `Exception`: Общее исключение.

#### `make_get_request(self, url: str, cookies: List[dict] = None, headers: dict = None) -> requests.Response | bool`

**Описание**: Выполняет GET-запрос с указанными кукисами.

**Параметры**:

- `url` (str): URL для запроса.
- `cookies` (List[dict], опционально): Список кукисов для запроса.
- `headers` (dict, опционально): Заголовки для запроса.

**Возвращает**:

- `requests.Response`: Объект ответа, если запрос успешен.
- `False`: Если запрос не успешен.

**Обрабатывает исключения**:

- `requests.RequestException`: Если произошла ошибка при выполнении запроса.
- `Exception`: Общее исключение.


#### `short_affiliate_link(self, link_url: str) -> requests.Response | bool`

**Описание**: Получает короткий аффилиат-ссылку.

**Параметры**:

- `link_url` (str): URL для укорачивания.

**Возвращает**:

- `requests.Response`: Объект ответа, если запрос успешен.
- `False`: Если запрос не успешен.

**Обрабатывает исключения**:

- `requests.RequestException`: Если произошла ошибка при выполнении запроса.
- `Exception`: Общее исключение.


## Константы

- `MODE` (str): Значение переменной `MODE`.


## Модули

- `pickle`
- `requests`
- `pathlib`
- `typing`
- `requests.cookies`
- `urllib.parse`
- `fake_useragent`
- `src.gs`
- `src.utils.jjson`
- `src.logger`


## Зависимости

- `requests`
- `fake_useragent`
- `src`