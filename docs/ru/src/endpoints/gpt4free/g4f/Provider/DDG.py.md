# Модуль `DDG.py`

## Обзор

Модуль предоставляет класс `DDG`, который является асинхронным провайдером для взаимодействия с DuckDuckGo AI Chat. Он поддерживает потоковую передачу сообщений, системные сообщения и историю сообщений. Модуль включает в себя механизмы для обработки ошибок, таких как ограничение скорости запросов и тайм-ауты.

## Подробней

Модуль `DDG.py` предназначен для интеграции с DuckDuckGo AI Chat через асинхронные запросы. Он обеспечивает функциональность для получения ответов от AI-моделей DuckDuckGo, обрабатывает куки, заголовки и параметры запросов. Модуль также реализует логику повторных попыток при сбоях и ограничениях скорости, обеспечивая надежное взаимодействие с сервисом.

## Содержание

1.  [Классы](#Классы)
    *   [DuckDuckGoSearchException](#DuckDuckGoSearchException)
    *   [Conversation](#Conversation)
    *   [DDG](#DDG)
2.  [Функции](#Функции)
    *   [sha256_base64](#sha256_base64)
    *   [parse_dom_fingerprint](#parse_dom_fingerprint)
    *   [parse_server_hashes](#parse_server_hashes)
    *   [build_x_vqd_hash_1](#build_x_vqd_hash_1)
    *   [validate_model](#validate_model)
    *   [sleep](#sleep)
    *   [get_default_cookies](#get_default_cookies)
    *   [fetch_fe_version](#fetch_fe_version)
    *   [fetch_vqd_and_hash](#fetch_vqd_and_hash)
    *   [create_async_generator](#create_async_generator)

## Классы

### `DuckDuckGoSearchException`

**Описание**: Базовый класс исключений для модуля `duckduckgo_search`.

**Наследует**:
*   `Exception`

**Атрибуты**:
*   отсутствуют

**Методы**:
*   отсутствуют

### `Conversation`

**Описание**: Класс для хранения состояния разговора с DuckDuckGo AI Chat.

**Наследует**:
*   `JsonConversation`

**Атрибуты**:

*   `vqd` (str): VQD токен для сессии.
*   `vqd_hash_1` (str): Хэш VQD токена.
*   `message_history` (Messages): История сообщений в формате списка словарей.
*   `cookies` (dict): Куки для сессии.
*   `fe_version` (str): Версия FE.

**Методы**:

*   `__init__(self, model: str)`:
    *   **Назначение**: Инициализирует объект разговора с указанной моделью.
    *   **Параметры**:
        *   `model` (str): Название модели для разговора.
    *   **Возвращает**:
        *   None
    *   **Вызывает исключения**:
        *   отсутствуют

### `DDG`

**Описание**: Класс, предоставляющий асинхронный интерфейс для взаимодействия с DuckDuckGo AI Chat.

**Наследует**:

*   `AsyncGeneratorProvider`, `ProviderModelMixin`

**Атрибуты**:

*   `label` (str): Метка провайдера ("DuckDuckGo AI Chat").
*   `url` (str): URL главной страницы DuckDuckGo AI Chat ("https://duckduckgo.com/aichat").
*   `api_endpoint` (str): URL API для чата ("https://duckduckgo.com/duckchat/v1/chat").
*   `status_url` (str): URL для получения статуса сессии ("https://duckduckgo.com/duckchat/v1/status").
*   `working` (bool): Флаг, указывающий, работает ли провайдер (True).
*   `supports_stream` (bool): Флаг, указывающий, поддерживает ли провайдер потоковую передачу (True).
*   `supports_system_message` (bool): Флаг, указывающий, поддерживает ли провайдер системные сообщения (True).
*   `supports_message_history` (bool): Флаг, указывающий, поддерживает ли провайдер историю сообщений (True).
*   `default_model` (str): Модель по умолчанию ("gpt-4o-mini").
*   `models` (list[str]): Список поддерживаемых моделей.
*   `model_aliases` (dict[str, str]): Словарь псевдонимов моделей.
*   `last_request_time` (float): Время последнего запроса.
*   `max_retries` (int): Максимальное количество повторных попыток при сбое запроса.
*   `base_delay` (int): Базовая задержка между повторными попытками (в секундах).
*   `_chat_xfe` (str):  версия `x-fe-version` для запроса

**Методы**:

*   `sha256_base64(text: str) -> str`
*   `parse_dom_fingerprint(js_text: str) -> str`
*   `parse_server_hashes(js_text: str) -> list`
*   `build_x_vqd_hash_1(vqd_hash_1: str, headers: dict) -> str`
*   `validate_model(cls, model: str) -> str`
*   `sleep(multiplier=1.0)`
*   `get_default_cookies(session: ClientSession) -> dict`
*   `fetch_fe_version(session: ClientSession) -> str`
*   `fetch_vqd_and_hash(session: ClientSession, retry_count: int = 0) -> tuple[str, str]`
*   `create_async_generator(...) -> AsyncResult`

## Функции

### `sha256_base64`

```python
@staticmethod
def sha256_base64(text: str) -> str:
    """Return the base64 encoding of the SHA256 digest of the text."""
    sha256_hash = hashlib.sha256(text.encode("utf-8")).digest()
    return base64.b64encode(sha256_hash).decode()
```

**Назначение**: Вычисляет SHA256-хеш заданной строки и возвращает его base64-представление.

**Параметры**:

*   `text` (str): Строка для хеширования.

**Возвращает**:

*   `str`: Base64-представление SHA256-хеша строки.

**Как работает функция**:

1.  Кодирует входную строку `text` в UTF-8.
2.  Вычисляет SHA256-хеш закодированной строки.
3.  Кодирует полученный хеш в base64.
4.  Декодирует base64-представление в строку UTF-8 и возвращает ее.

```
Текст -> SHA256 -> Base64 -> Строка
```

**Примеры**:

```python
text = "example"
result = DDG.sha256_base64(text)
print(result)  # Вывод: rnuZwdQjNlOn84YpjWQv+D9sGg4wJ848Gq2zbRfKtJs=
```

### `parse_dom_fingerprint`

```python
@staticmethod
def parse_dom_fingerprint(js_text: str) -> str:
    """Parse the dom fingerprint from the js text."""
    ...
```

**Назначение**: Извлекает значение fingerprint из JavaScript кода.

**Параметры**:

*   `js_text` (str): JavaScript код, содержащий fingerprint.

**Возвращает**:

*   `str`: Значение fingerprint в виде строки. Если `BeautifulSoup` недоступен, возвращает `"1000"`. Если парсинг не удался, возвращает `"1000"`.

**Как работает функция**:

1.  Проверяет, установлен ли `BeautifulSoup`. Если нет, возвращает `"1000"`.
2.  Извлекает HTML-фрагмент из `js_text`, используя разделители `e.innerHTML = '` и `';`.
3.  Извлекает значение offset из `js_text`, используя разделители `return String(` и ` `.
4.  Использует `BeautifulSoup` для парсинга HTML-фрагмента.
5.  Извлекает содержимое тега `body`.
6.  Вычисляет длину содержимого тега `body`.
7.  Суммирует значение offset и длину содержимого `body`.
8.  Возвращает сумму в виде строки.
9.  Если любой из шагов завершился ошибкой, возвращает `"1000"`.

```
JavaScript код -> Извлечение HTML-фрагмента -> Извлечение offset -> BeautifulSoup парсинг -> Извлечение длины содержимого body -> Вычисление fingerprint -> Строка
```

**Примеры**:

```python
js_text = "e.innerHTML = '<body id=\"fingerprint\">Test</body>';" \
          "return String(10) "
result = DDG.parse_dom_fingerprint(js_text)
print(result) # 14
```

### `parse_server_hashes`

```python
@staticmethod
def parse_server_hashes(js_text: str) -> list:
    """Parse the server hashes from the js text."""
    ...
```

**Назначение**: Извлекает список хешей сервера из JavaScript кода.

**Параметры**:

*   `js_text` (str): JavaScript код, содержащий хеши сервера.

**Возвращает**:

*   `list[str]`: Список хешей сервера. Если парсинг не удался, возвращает `["1", "2"]`.

**Как работает функция**:

1.  Извлекает подстроку, содержащую хеши сервера, используя разделители `server_hashes: ["` и `"]`.
2.  Разделяет подстроку на отдельные хеши, используя разделитель `","`.
3.  Возвращает список хешей.
4.  Если любой из шагов завершился ошибкой, возвращает `["1", "2"]`.

```
JavaScript код -> Извлечение подстроки с хешами -> Разделение на отдельные хеши -> Список хешей
```

**Примеры**:

```python
js_text = 'server_hashes: ["hash1","hash2"]'
result = DDG.parse_server_hashes(js_text)
print(result)  # ['hash1', 'hash2']
```

### `build_x_vqd_hash_1`

```python
@classmethod
def build_x_vqd_hash_1(cls, vqd_hash_1: str, headers: dict) -> str:
    """Build the x-vqd-hash-1 header value."""
    ...
```

**Назначение**: Формирует значение заголовка `x-vqd-hash-1` на основе переданных данных.

**Параметры**:

*   `vqd_hash_1` (str): Base64-encoded строка, содержащая данные для формирования хеша.
*   `headers` (dict): Словарь HTTP-заголовков запроса.

**Возвращает**:

*   `str`: Base64-encoded строка, представляющая собой значение заголовка `x-vqd-hash-1`. Если во время выполнения возникла ошибка, возвращает пустую строку `""`.

**Как работает функция**:

1.  Декодирует строку `vqd_hash_1` из Base64 в UTF-8.
2.  Извлекает хеши сервера из декодированной строки с помощью метода `parse_server_hashes`.
3.  Извлекает fingerprint DOM из декодированной строки с помощью метода `parse_dom_fingerprint`.
4.  Формирует строку `ua_fingerprint` путем конкатенации значений заголовков "User-Agent" и "sec-ch-ua" из словаря `headers`.
5.  Вычисляет SHA256-хеш строки `ua_fingerprint` и кодирует его в Base64.
6.  Вычисляет SHA256-хеш fingerprint DOM и кодирует его в Base64.
7.  Формирует словарь `final_result`, содержащий хеши сервера, хеши User-Agent и fingerprint DOM, а также пустой словарь `signals`.
8.  Кодирует словарь `final_result` в JSON и затем в Base64.
9.  Возвращает полученную Base64-encoded строку.

```
vqd_hash_1 (Base64) -> Декодирование Base64 -> Извлечение хешей сервера -> Извлечение fingerprint DOM -> Формирование ua_fingerprint -> Вычисление хеша User-Agent -> Вычисление хеша DOM -> Формирование final_result (JSON) -> Кодирование Base64 -> x-vqd-hash-1 (Base64)
```

**Примеры**:

```python
vqd_hash_1 = "SGVsbG8gV29ybGQh"  # Пример Base64-encoded строки
headers = {"User-Agent": "Test Agent", "sec-ch-ua": '"Test Brand";v="100"'}
result = DDG.build_x_vqd_hash_1(vqd_hash_1, headers)
print(result)
```

### `validate_model`

```python
@classmethod
def validate_model(cls, model: str) -> str:
    """Validates and returns the correct model name"""
    ...
```

**Назначение**: Проверяет и возвращает корректное имя модели.

**Параметры**:

*   `model` (str): Имя модели для проверки.

**Возвращает**:

*   `str`: Корректное имя модели.

**Вызывает исключения**:

*   `ModelNotSupportedError`: Если указанная модель не поддерживается.

**Как работает функция**:

1.  Если `model` не указана, возвращает `default_model`.
2.  Если `model` есть в `model_aliases`, заменяет ее на соответствующее значение.
3.  Если `model` нет в `models`, вызывает исключение `ModelNotSupportedError`.
4.  Возвращает `model`.

```
Model -> Проверка на None -> Замена alias -> Проверка на поддержку -> Возврат Model
```

**Примеры**:

```python
model = "gpt-4"
result = DDG.validate_model(model)
print(result)  # gpt-4o-mini
```

### `sleep`

```python
@classmethod
async def sleep(cls, multiplier=1.0):
    """Implements rate limiting between requests"""
    ...
```

**Назначение**: Реализует ограничение скорости между запросами.

**Параметры**:

*   `multiplier` (float, optional): Множитель задержки. По умолчанию 1.0.

**Возвращает**:

*   `None`

**Как работает функция**:

1.  Получает текущее время.
2.  Если `last_request_time` больше 0, вычисляет задержку на основе разницы между текущим временем и `last_request_time`.
3.  Если задержка больше 0, ждет указанное время.
4.  Обновляет `last_request_time` текущим временем.

```
Получение текущего времени -> Вычисление задержки -> Ожидание -> Обновление last_request_time
```

**Примеры**:

```python
await DDG.sleep()
```

### `get_default_cookies`

```python
@classmethod
async def get_default_cookies(cls, session: ClientSession) -> dict:
    """Obtains default cookies needed for API requests"""
    ...
```

**Назначение**: Получает куки по умолчанию, необходимые для API-запросов.

**Параметры**:

*   `session` (ClientSession): Асинхронная HTTP-сессия.

**Возвращает**:

*   `dict`: Словарь с куками или пустой словарь в случае ошибки.

**Как работает функция**:

1.  Выполняет асинхронный GET-запрос к `cls.url` для получения куки.
2.  Вручную устанавливает необходимые куки (`dcs` и `dcm`) в сессию.
3.  Возвращает словарь с куками.

```
Создание сессии -> GET-запрос к cls.url -> Установка куки -> Возврат словаря с куками
```

**Примеры**:

```python
async with ClientSession() as session:
    cookies = await DDG.get_default_cookies(session)
    print(cookies)
```

### `fetch_fe_version`

```python
@classmethod
async def fetch_fe_version(cls, session: ClientSession) -> str:
    """Fetches the fe-version from the initial page load."""
    ...
```

**Назначение**: Извлекает версию FE из исходного кода страницы.

**Параметры**:

*   `session` (ClientSession): Асинхронная HTTP-сессия.

**Возвращает**:

*   `str`: Версия FE. Если извлечение не удалось, возвращает пустую строку `""`.

**Как работает функция**:

1.  Если `cls._chat_xfe` уже определена, возвращает её.
2.  Выполняет GET-запрос к URL.
3.  Извлекает компоненты версии FE из содержимого ответа, используя разделители `__DDG_BE_VERSION__="` и `"` для `xfe1` и `__DDG_FE_CHAT_HASH__="` и `"` для `xfe2`.
4.  Формирует версию FE как `f"{xfe1}-{xfe2}"`.
5.  Сохраняет версию FE в `cls._chat_xfe`.
6.  Если извлечение не удалось, возвращает пустую строку `""`.

```
Проверка cls._chat_xfe -> Создание сессии -> GET-запрос -> Извлечение версии FE -> Возврат версии FE
```

**Примеры**:

```python
async with ClientSession() as session:
    fe_version = await DDG.fetch_fe_version(session)
    print(fe_version)
```

### `fetch_vqd_and_hash`

```python
 @classmethod
    async def fetch_vqd_and_hash(cls, session: ClientSession, retry_count: int = 0) -> tuple[str, str]:
        """Fetches the required VQD token and hash for the chat session with retries."""
        ...
```

**Назначение**: Получает VQD токен и хеш, необходимые для чат-сессии, с повторными попытками.

**Параметры**:

*   `session` (ClientSession): Асинхронная HTTP-сессия.
*   `retry_count` (int, optional): Количество выполненных повторных попыток. По умолчанию 0.

**Возвращает**:

*   `tuple[str, str]`: Кортеж, содержащий VQD токен и хеш.

**Вызывает исключения**:

*   `RuntimeError`: Если не удалось получить VQD токен и хеш после максимального количества попыток.

**Как работает функция**:

1.  Формирует заголовки запроса, включая User-Agent, origin и referer.
2.  Выполняет GET-запрос к `cls.status_url`.
3.  Извлекает VQD токен и хеш из заголовков ответа (`x-vqd-4` и `x-vqd-hash-1`).
4.  Если VQD токен найден, возвращает его вместе с хешем.
5.  Если VQD токен не найден, вызывает исключение `RuntimeError`.
6.  В случае ошибки увеличивает счетчик `retry_count` и повторяет попытку, если `retry_count` меньше `cls.max_retries`.

```
Формирование заголовков -> GET-запрос -> Извлечение VQD токена и хеша -> Возврат токена и хеша
```

**Примеры**:

```python
async with ClientSession() as session:
    vqd, vqd_hash = await DDG.fetch_vqd_and_hash(session)
    print(f"VQD: {vqd}, Hash: {vqd_hash}")
```

### `create_async_generator`

```python
@classmethod
async def create_async_generator(
    cls,
    model: str,
    messages: Messages,
    proxy: str = None,
    timeout: int = 60,
    cookies: Cookies = None,
    conversation: Conversation = None,
    return_conversation: bool = False,
    **kwargs
) -> AsyncResult:
    """Creates an async generator for chat completion."""
    ...
```

**Назначение**: Создает асинхронный генератор для завершения чата.

**Параметры**:

*   `model` (str): Имя модели для использования.
*   `messages` (Messages): Список сообщений для отправки.
*   `proxy` (str, optional): URL прокси-сервера. По умолчанию `None`.
*   `timeout` (int, optional): Время ожидания запроса в секундах. По умолчанию 60.
*   `cookies` (Cookies, optional): Куки для использования в запросе. По умолчанию `None`.
*   `conversation` (Conversation, optional): Объект разговора для продолжения существующей сессии. По умолчанию `None`.
*   `return_conversation` (bool, optional): Флаг, указывающий, нужно ли возвращать объект разговора. По умолчанию `False`.
*   `**kwargs`: Дополнительные аргументы.

**Возвращает**:

*   `AsyncResult`: Асинхронный генератор, выдающий ответы от модели.

**Вызывает исключения**:

*   `ModelNotSupportedError`: Если указанная модель не поддерживается.
*   `RateLimitError`: Если достигнуто ограничение скорости запросов.
*   `TimeoutError`: Если запрос превысил время ожидания.
*   `Exception`: В случае других ошибок.

**Как работает функция**:

1.  Проверяет и получает имя модели.
2.  Инициализирует или обновляет объект разговора.
3.  Получает VQD токен и хеш, если это новый разговор.
4.  Формирует заголовки запроса, включая User-Agent, origin и referer.
5.  Формирует данные запроса, включая модель и историю сообщений.
6.  Отправляет POST-запрос к API-endpoint.
7.  Обрабатывает потоковый ответ, извлекая сообщения и возвращая их через генератор.
8.  Обновляет объект разговора с информацией об ответе, если `return_conversation` установлен в `True`.
9.  Обрабатывает ошибки, такие как ограничение скорости и тайм-ауты, и выполняет повторные попытки, если необходимо.

```
Проверка модели -> Инициализация/обновление разговора -> Получение VQD токена и хеша -> Формирование заголовков -> Формирование данных -> POST-запрос -> Обработка потокового ответа -> Обновление разговора -> Возврат генератора
```

**Примеры**:

```python
messages = [{"role": "user", "content": "Hello, world!"}]
async for message in DDG.create_async_generator(model="gpt-4o-mini", messages=messages):
    print(message)