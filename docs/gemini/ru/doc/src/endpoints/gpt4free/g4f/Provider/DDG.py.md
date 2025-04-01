# Модуль `DDG.py`

## Обзор

Модуль `DDG.py` предоставляет асинхронный интерфейс для взаимодействия с AI Chat DuckDuckGo. Он включает в себя функциональность для получения токенов VQD, отправки сообщений и обработки потоковых ответов. Модуль поддерживает различные модели, такие как `gpt-4o-mini`, `meta-llama/Llama-3.3-70B-Instruct-Turbo`, `claude-3-haiku-20240307` и другие.

## Подробней

Этот модуль предназначен для интеграции с AI Chat DuckDuckGo. Он выполняет следующие задачи:

- Получение необходимых токенов (VQD) для аутентификации.
- Отправка сообщений в AI Chat DuckDuckGo и получение потоковых ответов.
- Обработка ошибок, таких как лимиты скорости и ошибки подключения.
- Поддержка различных AI-моделей и управление сессиями.

## Классы

### `DuckDuckGoSearchException`

**Описание**: Базовый класс исключений для `duckduckgo_search`.

**Принцип работы**: Используется в качестве базового класса для других исключений, специфичных для модуля `duckduckgo_search`.

### `Conversation(JsonConversation)`

**Описание**: Класс для хранения состояния разговора с AI Chat DuckDuckGo.

**Наследует**: `JsonConversation`

**Атрибуты**:

- `vqd` (str): Токен VQD для аутентификации.
- `vqd_hash_1` (str): Хэш токена VQD.
- `message_history` (Messages): История сообщений в разговоре.
- `cookies` (dict): Куки, используемые в сессии.
- `fe_version` (str): Версия frontend.
- `model` (str): Модель, используемая в разговоре.

**Методы**:

- `__init__(model: str)`: Инициализирует объект разговора с указанной моделью.

### `DDG(AsyncGeneratorProvider, ProviderModelMixin)`

**Описание**: Класс провайдера для взаимодействия с AI Chat DuckDuckGo.

**Наследует**: `AsyncGeneratorProvider`, `ProviderModelMixin`

**Атрибуты**:

- `label` (str): Метка провайдера ("DuckDuckGo AI Chat").
- `url` (str): URL главной страницы AI Chat DuckDuckGo ("https://duckduckgo.com/aichat").
- `api_endpoint` (str): URL API для чата ("https://duckduckgo.com/duckchat/v1/chat").
- `status_url` (str): URL для получения статуса ("https://duckduckgo.com/duckchat/v1/status").
- `working` (bool): Указывает, работает ли провайдер (True).
- `supports_stream` (bool): Поддерживает ли провайдер потоковую передачу (True).
- `supports_system_message` (bool): Поддерживает ли провайдер системные сообщения (True).
- `supports_message_history` (bool): Поддерживает ли провайдер историю сообщений (True).
- `default_model` (str): Модель по умолчанию ("gpt-4o-mini").
- `models` (list): Список поддерживаемых моделей.
- `model_aliases` (dict): Алиасы моделей для удобства использования.
- `last_request_time` (float): Время последнего запроса для управления лимитами.
- `max_retries` (int): Максимальное количество повторных попыток при сбое запроса.
- `base_delay` (int): Базовая задержка между повторными попытками.
- `_chat_xfe` (str):  Классовая переменная для хранения `x-fe-version` для всех инстансов.

**Методы**:

- `sha256_base64(text: str) -> str`: Возвращает base64-кодировку SHA256-хеша текста.
- `parse_dom_fingerprint(js_text: str) -> str`: Извлекает fingerprint DOM из JavaScript кода.
- `parse_server_hashes(js_text: str) -> list`: Извлекает server hashes из JavaScript кода.
- `build_x_vqd_hash_1(vqd_hash_1: str, headers: dict) -> str`: Строит значение заголовка `x-vqd-hash-1`.
- `validate_model(model: str) -> str`: Проверяет и возвращает корректное имя модели.
- `sleep(multiplier=1.0)`: Реализует ограничение скорости между запросами.
- `get_default_cookies(session: ClientSession) -> dict`: Получает куки по умолчанию, необходимые для запросов API.
- `fetch_fe_version(session: ClientSession) -> str`: Получает `fe-version` из начальной загрузки страницы.
- `fetch_vqd_and_hash(session: ClientSession, retry_count: int = 0) -> tuple[str, str]`: Получает токены VQD и hash для сессии чата с повторными попытками.
- `create_async_generator(...) -> AsyncResult`: Создает асинхронный генератор для взаимодействия с AI Chat DuckDuckGo.

## Функции

### `sha256_base64`

```python
    @staticmethod
    def sha256_base64(text: str) -> str:
        """Return the base64 encoding of the SHA256 digest of the text."""
        sha256_hash = hashlib.sha256(text.encode("utf-8")).digest()
        return base64.b64encode(sha256_hash).decode()
```

**Назначение**: Вычисляет SHA256-хеш заданной строки, кодирует его в base64 и возвращает результат.

**Параметры**:

- `text` (str): Строка, для которой вычисляется хеш.

**Возвращает**:

- `str`: Base64-кодированная строка SHA256-хеша.

**Как работает функция**:

1. Кодирует входную строку `text` в формат UTF-8.
2. Вычисляет SHA256-хеш закодированной строки.
3. Кодирует полученный хеш в base64.
4. Декодирует base64-представление в строку UTF-8 и возвращает результат.

```
    Текст -> Кодирование UTF-8 -> SHA256-хеш -> Кодирование Base64 -> Строка UTF-8
```

**Примеры**:

```python
text = "Пример текста"
result = DDG.sha256_base64(text)
print(result)  # Вывод: "ZHcxYWcxVkludFdNb3NYWm4wdnFZQT09"
```

### `parse_dom_fingerprint`

```python
    @staticmethod
    def parse_dom_fingerprint(js_text: str) -> str:
        if not has_bs4:
            # Fallback if BeautifulSoup is not available
            return "1000"
        
        try:
            html_snippet = js_text.split("e.innerHTML = \'")[1].split("\';")[0]
            offset_value = js_text.split("return String(")[1].split(" ")[0]
            soup = BeautifulSoup(html_snippet, "html.parser")
            corrected_inner_html = soup.body.decode_contents()
            inner_html_length = len(corrected_inner_html)
            fingerprint = int(offset_value) + inner_html_length
            return str(fingerprint)
        except Exception:
            # Return a fallback value if parsing fails
            return "1000"
```

**Назначение**: Извлекает значение DOM fingerprint из JavaScript-текста. Использует BeautifulSoup для парсинга HTML, если он доступен.

**Параметры**:

- `js_text` (str): JavaScript-текст, содержащий HTML snippet и offset value.

**Возвращает**:

- `str`: Строковое представление DOM fingerprint. Возвращает "1000" в случае ошибки или если BeautifulSoup не установлен.

**Как работает функция**:

1. Проверяет, установлен ли BeautifulSoup (`has_bs4`). Если нет, возвращает "1000".
2. Извлекает HTML snippet и offset value из JavaScript-текста с помощью строковых операций.
3. Использует BeautifulSoup для парсинга HTML snippet.
4. Извлекает содержимое тега `<body>` и вычисляет его длину.
5. Складывает offset value и длину содержимого `<body>`, чтобы получить DOM fingerprint.
6. Возвращает строковое представление DOM fingerprint.
7. В случае возникновения исключения, возвращает "1000".

```
    JavaScript-текст -> Извлечение HTML snippet и offset value -> Парсинг HTML (BeautifulSoup) -> Извлечение содержимого <body> -> Вычисление длины -> DOM fingerprint (offset + длина) -> Строка
```

**Примеры**:

```python
js_text = "e.innerHTML = '<div id=\"test\">Пример</div>';" \
          "return String(100);"
result = DDG.parse_dom_fingerprint(js_text)
print(result)  # Вывод: "118" (100 + длина "<body><div id="test">Пример</div></body>")

js_text = "e.innerHTML = '<div id=\"test\">Пример</div>';" \
          "return String(1000);"
result = DDG.parse_dom_fingerprint(js_text)
print(result)

```

### `parse_server_hashes`

```python
    @staticmethod
    def parse_server_hashes(js_text: str) -> list:
        try:
            return js_text.split('server_hashes: ["', maxsplit=1)[1].split('"]', maxsplit=1)[0].split('","')
        except Exception:
            # Return a fallback value if parsing fails
            return ["1", "2"]
```

**Назначение**: Извлекает список server hashes из JavaScript-текста.

**Параметры**:

- `js_text` (str): JavaScript-текст, содержащий список server hashes.

**Возвращает**:

- `list`: Список server hashes. Возвращает `["1", "2"]` в случае ошибки.

**Как работает функция**:

1. Пытается извлечь список server hashes, используя строковые операции для разделения JavaScript-текста.
2. В случае успеха возвращает список.
3. В случае возникновения исключения, возвращает `["1", "2"]`.

```
    JavaScript-текст -> Извлечение списка server_hashes -> Список server_hashes
```

**Примеры**:

```python
js_text = 'server_hashes: ["hash1","hash2"]'
result = DDG.parse_server_hashes(js_text)
print(result)  # Вывод: ['hash1', 'hash2']

js_text = 'server_hashes: ["hash1"]'
result = DDG.parse_server_hashes(js_text)
print(result) # Вывод: ['hash1']

js_text = 'server_hashes: []'
result = DDG.parse_server_hashes(js_text)
print(result) # Вывод: []

js_text = 'some_text'
result = DDG.parse_server_hashes(js_text)
print(result) # Вывод: ['1', '2']
```

### `build_x_vqd_hash_1`

```python
    @classmethod
    def build_x_vqd_hash_1(cls, vqd_hash_1: str, headers: dict) -> str:
        """Build the x-vqd-hash-1 header value."""
        try:
            decoded = base64.b64decode(vqd_hash_1).decode()
            server_hashes = cls.parse_server_hashes(decoded)
            dom_fingerprint = cls.parse_dom_fingerprint(decoded)

            ua_fingerprint = headers.get("User-Agent", "") + headers.get("sec-ch-ua", "")
            ua_hash = cls.sha256_base64(ua_fingerprint)
            dom_hash = cls.sha256_base64(dom_fingerprint)

            final_result = {
                "server_hashes": server_hashes,
                "client_hashes": [ua_hash, dom_hash],
                "signals": {},
            }
            base64_final_result = base64.b64encode(json.dumps(final_result).encode()).decode()
            return base64_final_result
        except Exception as e:
            # If anything fails, return an empty string
            return ""
```

**Назначение**: Создает значение заголовка `x-vqd-hash-1` на основе предоставленных данных и заголовков.

**Параметры**:

- `vqd_hash_1` (str): Base64-encoded строка, содержащая данные для построения хеша.
- `headers` (dict): Словарь HTTP-заголовков, содержащий `User-Agent` и `sec-ch-ua`.

**Возвращает**:

- `str`: Base64-encoded строка, представляющая собой хеш `x-vqd-hash-1`. В случае ошибки возвращает пустую строку.

**Как работает функция**:

1. Декодирует `vqd_hash_1` из Base64 в UTF-8.
2. Извлекает server hashes, используя `cls.parse_server_hashes`.
3. Извлекает fingerprint DOM, используя `cls.parse_dom_fingerprint`.
4. Комбинирует `User-Agent` и `sec-ch-ua` из headers для создания `ua_fingerprint`.
5. Вычисляет SHA256 хеш `ua_fingerprint` и кодирует его в Base64.
6. Вычисляет SHA256 хеш `dom_fingerprint` и кодирует его в Base64.
7. Создает словарь `final_result`, содержащий `server_hashes`, `client_hashes` (ua_hash, dom_hash) и пустой словарь `signals`.
8. Кодирует `final_result` в JSON и затем в Base64.
9. Возвращает полученную Base64-encoded строку.
10. В случае возникновения ошибки возвращает пустую строку.

```
    vqd_hash_1, headers -> Декодирование Base64 -> Извлечение server hashes -> Извлечение fingerprint DOM -> Комбинирование User-Agent и sec-ch-ua -> Вычисление хеша UA -> Вычисление хеша DOM -> Создание final_result -> Кодирование JSON -> Кодирование Base64 -> x-vqd-hash-1
```

**Примеры**:

```python
headers = {"User-Agent": "Mozilla/5.0", "sec-ch-ua": '"Chromium";v="133"'}
vqd_hash_1 = "some_base64_encoded_string"
result = DDG.build_x_vqd_hash_1(vqd_hash_1, headers)
print(result)
```

### `validate_model`

```python
    @classmethod
    def validate_model(cls, model: str) -> str:
        """Validates and returns the correct model name"""
        if not model:
            return cls.default_model
        if model in cls.model_aliases:
            model = cls.model_aliases[model]
        if model not in cls.models:
            raise ModelNotSupportedError(f"Model {model} not supported. Available models: {cls.models}")
        return model
```

**Назначение**: Проверяет и возвращает корректное имя модели.

**Параметры**:

- `model` (str): Имя модели для проверки.

**Возвращает**:

- `str`: Корректное имя модели.

**Вызывает исключения**:

- `ModelNotSupportedError`: Если модель не поддерживается.

**Как работает функция**:

1. Если `model` не указана, возвращает `cls.default_model`.
2. Если `model` есть в `cls.model_aliases`, заменяет `model` на соответствующий алиас.
3. Если `model` отсутствует в `cls.models`, вызывает исключение `ModelNotSupportedError`.
4. Возвращает проверенное и, при необходимости, замененное имя модели.

```
    model -> Проверка на None -> Проверка в model_aliases -> Замена алиаса -> Проверка в models -> Возврат model
```

**Примеры**:

```python
model = "gpt-4"
result = DDG.validate_model(model)
print(result)  # Вывод: "gpt-4o-mini"

model = "unsupported_model"
try:
    DDG.validate_model(model)
except ModelNotSupportedError as ex:
    print(ex)  # Вывод: Model unsupported_model not supported. Available models: ['gpt-4o-mini', 'meta-llama/Llama-3.3-70B-Instruct-Turbo', 'claude-3-haiku-20240307', 'o3-mini', 'mistralai/Mistral-Small-24B-Instruct-2501']
```

### `sleep`

```python
    @classmethod
    async def sleep(cls, multiplier=1.0):
        """Implements rate limiting between requests"""
        now = time.time()
        if cls.last_request_time > 0:
            delay = max(0.0, 1.5 - (now - cls.last_request_time)) * multiplier
            if delay > 0:
                await asyncio.sleep(delay)
        cls.last_request_time = time.time()
```

**Назначение**: Реализует ограничение частоты запросов между запросами.

**Параметры**:

- `multiplier` (float): Множитель для задержки. По умолчанию 1.0.

**Как работает функция**:

1. Получает текущее время.
2. Если `cls.last_request_time` больше 0, вычисляет задержку на основе времени, прошедшего с последнего запроса, и множителя.
3. Если задержка больше 0, ожидает указанное время с помощью `asyncio.sleep`.
4. Обновляет `cls.last_request_time` текущим временем.

```
    multiplier -> Получение текущего времени -> Вычисление задержки -> Ожидание (asyncio.sleep) -> Обновление last_request_time
```

**Примеры**:

```python
await DDG.sleep()
await DDG.sleep(multiplier=0.5)
```

### `get_default_cookies`

```python
    @classmethod
    async def get_default_cookies(cls, session: ClientSession) -> dict:
        """Obtains default cookies needed for API requests"""
        try:
            await cls.sleep()
            # Make initial request to get cookies
            async with session.get(cls.url) as response:
                # We also manually set required cookies
                cookies = {}
                cookies_dict = {'dcs': '1', 'dcm': '3'}
                
                for name, value in cookies_dict.items():
                    cookies[name] = value
                    url_obj = URL(cls.url)
                    session.cookie_jar.update_cookies({name: value}, url_obj)
                
                return cookies
        except Exception as e:
            return {}
```

**Назначение**: Получает куки по умолчанию, необходимые для запросов API.

**Параметры**:

- `session` (ClientSession): Асинхронная клиентская сессия для выполнения HTTP-запросов.

**Возвращает**:

- `dict`: Словарь куки. Возвращает пустой словарь в случае ошибки.

**Как работает функция**:

1.  Вызывает `cls.sleep()` для соблюдения ограничений по частоте запросов.
2.  Выполняет GET-запрос к `cls.url` для получения начальных куки.
3.  Создает словарь `cookies_dict` с необходимыми куки (`{'dcs': '1', 'dcm': '3'}`).
4.  Добавляет куки из `cookies_dict` в словарь `cookies` и обновляет `session.cookie_jar`.
5.  Возвращает словарь `cookies`.
6.  В случае возникновения исключения возвращает пустой словарь.

```
    session -> Ожидание (cls.sleep) -> GET-запрос к cls.url -> Создание словаря cookies -> Обновление session.cookie_jar -> Возврат словаря cookies
```

**Примеры**:

```python
async with ClientSession() as session:
    cookies = await DDG.get_default_cookies(session)
    print(cookies)  # Вывод: {'dcs': '1', 'dcm': '3'}
```

### `fetch_fe_version`

```python
    @classmethod
    async def fetch_fe_version(cls, session: ClientSession) -> str:
        """Fetches the fe-version from the initial page load."""
        if cls._chat_xfe:
            return cls._chat_xfe
            
        try:
            url = "https://duckduckgo.com/?q=DuckDuckGo+AI+Chat&ia=chat&duckai=1"
            await cls.sleep()
            async with session.get(url) as response:
                await raise_for_status(response)
                content = await response.text()
                
                # Extract x-fe-version components
                try:
                    xfe1 = content.split('__DDG_BE_VERSION__="', 1)[1].split('"', 1)[0]
                    xfe2 = content.split('__DDG_FE_CHAT_HASH__="', 1)[1].split('"', 1)[0]
                    cls._chat_xfe = f"{xfe1}-{xfe2}"
                    return cls._chat_xfe
                except Exception:
                    # If extraction fails, return an empty string
                    return ""
        except Exception:
            return ""
```

**Назначение**: Получает `fe-version` из начальной загрузки страницы.

**Параметры**:

- `session` (ClientSession): Асинхронная клиентская сессия для выполнения HTTP-запросов.

**Возвращает**:

- `str`: Значение `fe-version`. Возвращает пустую строку в случае ошибки.

**Как работает функция**:

1. Проверяет, если значение `cls._chat_xfe` уже установлено. Если да - возвращает его.
2.  Вызывает `cls.sleep()` для соблюдения ограничений по частоте запросов.
3.  Выполняет GET-запрос к URL.
4.  Извлекает значения `xfe1` и `xfe2` из содержимого ответа с помощью строковых операций.
5.  Формирует `cls._chat_xfe` как `f"{xfe1}-{xfe2}"`.
6.  Возвращает `cls._chat_xfe`.
7.  В случае возникновения исключения возвращает пустую строку.

```
    session -> Ожидание (cls.sleep) -> GET-запрос к URL -> Извлечение xfe1 и xfe2 -> Формирование cls._chat_xfe -> Возврат cls._chat_xfe
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
        headers = {
            "accept": "text/event-stream",
            "accept-language": "en-US,en;q=0.9",
            "cache-control": "no-cache",
            "content-type": "application/json", 
            "pragma": "no-cache",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36",
            "origin": "https://duckduckgo.com",
            "referer": "https://duckduckgo.com/",
            "x-vqd-accept": "1",
        }

        # Make sure we have cookies first
        if len(session.cookie_jar) == 0:
            await cls.get_default_cookies(session)

        try:
            await cls.sleep(multiplier=1.0 + retry_count * 0.5)
            async with session.get(cls.status_url, headers=headers) as response:
                await raise_for_status(response)
                
                vqd = response.headers.get("x-vqd-4", "")
                vqd_hash_1 = response.headers.get("x-vqd-hash-1", "")
                
                if vqd:
                    # Return the fetched vqd and vqd_hash_1
                    return vqd, vqd_hash_1
                
                response_text = await response.text()
                raise RuntimeError(f"Failed to fetch VQD token and hash: {response.status} {response_text}")
                
        except Exception as ex:
            if retry_count < cls.max_retries:
                wait_time = cls.base_delay * (2 ** retry_count) * (1 + random.random())
                await asyncio.sleep(wait_time)
                return await cls.fetch_vqd_and_hash(session, retry_count + 1)
            else:
                raise RuntimeError(f"Failed to fetch VQD token and hash after {cls.max_retries} attempts: {str(ex)}")
```

**Назначение**: Получает необходимые VQD token и hash для сессии чата с повторными попытками.

**Параметры**:

- `session` (ClientSession): Асинхронная клиентская сессия для выполнения HTTP-запросов.
- `retry_count` (int): Счетчик повторных попыток. По умолчанию 0.

**Возвращает**:

- `tuple[str, str]`: Кортеж, содержащий VQD token и hash.

**Вызывает исключения**:

- `RuntimeError`: Если не удалось получить VQD token и hash после нескольких попыток.

**Как работает функция**:

1.  Определяет заголовки запроса.
2.  Проверяет наличие куки в `session.cookie_jar`. Если куки отсутствуют, вызывает `cls.get_default_cookies(session)`.
3.  Вызывает `cls.sleep()` для соблюдения ограничений по частоте запросов.
4.  Выполняет GET-запрос к `cls.status_url` с определенными заголовками.
5.  Извлекает VQD token и hash из заголовков ответа.
6.  Если VQD token получен, возвращает кортеж с VQD token и hash.
7.  Если VQD token отсутствует, вызывает исключение `RuntimeError`.
8.  В случае возникновения исключения проверяет, не превышено ли максимальное количество повторных попыток. Если нет, вычисляет время ожидания и рекурсивно вызывает `cls.fetch_vqd_and_hash` с увеличенным счетчиком попыток.
9.  Если максимальное количество попыток превышено, вызывает исключение `RuntimeError`.

```
    session, retry_count -> Проверка наличия куки -> Ожидание (cls.sleep) -> GET-запрос к cls.status_url -> Извлечение VQD token и hash -> Возврат VQD token и hash (или повторная попытка/исключение)
```

**Примеры**:

```python
async with ClientSession() as session:
    vqd, vqd_hash = await DDG.fetch_vqd_and_hash(session)
    print(vqd, vqd_hash)
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
        model = cls.validate_model(model)
        retry_count = 0

        while retry_count <= cls.max_retries:
            try:
                session_timeout = ClientTimeout(total=timeout)
                async with ClientSession(timeout=session_timeout, cookies=cookies) as session:
                    # Step 1: Ensure we have the fe_version
                    if not cls._chat_xfe:
                        cls._chat_xfe = await cls.fetch_fe_version(session)
                    
                    # Step 2: Initialize or update conversation
                    if conversation is None:
                        # Get initial cookies if not provided
                        if not cookies:
                            await cls.get_default_cookies(session)
                        
                        # Create a new conversation
                        conversation = Conversation(model)
                        conversation.fe_version = cls._chat_xfe
                        
                        # Step 3: Get VQD tokens
                        vqd, vqd_hash_1 = await cls.fetch_vqd_and_hash(session)
                        conversation.vqd = vqd
                        conversation.vqd_hash_1 = vqd_hash_1
                        conversation.message_history = [{"role": "user", "content": format_prompt(messages)}]
                    else:
                        # Update existing conversation with new message
                        last_message = get_last_user_message(messages.copy())
                        conversation.message_history.append({"role": "user", "content": last_message})
                    
                    # Step 4: Prepare headers - IMPORTANT: send empty x-vqd-hash-1 for the first request
                    headers = {
                        "accept": "text/event-stream",
                        "accept-language": "en-US,en;q=0.9",
                        "content-type": "application/json",
                        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36",
                        "origin": "https://duckduckgo.com",
                        "referer": "https://duckduckgo.com/",
                        "sec-ch-ua": '"Chromium";v="133", "Not_A Brand";v="8"',
                        "x-fe-version": conversation.fe_version or cls._chat_xfe,
                        "x-vqd-4": conversation.vqd,
                        "x-vqd-hash-1": "",  # Send empty string initially
                    }

                    # Step 5: Prepare the request data
                    data = {
                        "model": model,
                        "messages": conversation.message_history,
                    }

                    # Step 6: Send the request
                    await cls.sleep(multiplier=1.0 + retry_count * 0.5)
                    async with session.post(cls.api_endpoint, json=data, headers=headers, proxy=proxy) as response:
                        # Handle 429 errors specifically
                        if response.status == 429:
                            response_text = await response.text()
                            
                            if retry_count < cls.max_retries:
                                retry_count += 1
                                wait_time = cls.base_delay * (2 ** retry_count) * (1 + random.random())
                                await asyncio.sleep(wait_time)
                                
                                # Get fresh tokens and cookies
                                cookies = await cls.get_default_cookies(session)
                                continue
                            else:
                                raise RateLimitError(f"Rate limited after {cls.max_retries} retries")
                        
                        await raise_for_status(response)
                        reason = None
                        full_message = ""

                        # Step 7: Process the streaming response
                        async for line in response.content:
                            line = line.decode("utf-8").strip()

                            if line.startswith("data:") :
                                try:
                                    message = json.loads(line[5:].strip())
                                except json.JSONDecodeError:
                                    continue

                                if "action" in message and message["action"] == "error":
                                    error_type = message.get("type", "")
                                    if message.get("status") == 429:
                                        if error_type == "ERR_CONVERSATION_LIMIT":
                                            raise ConversationLimitError(error_type)
                                        raise RateLimitError(error_type)
                                    raise DuckDuckGoSearchException(error_type)

                                if "message" in message:
                                    if message["message"]:
                                        yield message["message"]
                                        full_message += message["message"]
                                        reason = "length"
                                    else:
                                        reason = "stop"

                        # Step 8: Update conversation with response information
                        if return_conversation:
                            conversation.message_history.append({"role": "assistant", "content": full_message})
                            # Update tokens from response headers
                            conversation.vqd = response.headers.get("x-vqd-4", conversation.vqd)
                            conversation.vqd_hash_1 = response.headers.get("x-vqd-hash-1", conversation.vqd_hash_1)
                            conversation.cookies = {
                                n: c.value 
                                for n, c in session.cookie_jar.filter_cookies(URL(cls.url)).items()
                            }
                            yield conversation

                        if reason is not None:
                            yield FinishReason(reason)
                        
                        # If we got here, the request was successful
                        break

            except (RateLimitError, ResponseStatusError) as ex:
                if "429" in str(ex) and retry_count < cls.max_retries:
                    retry_count += 1
                    wait_time = cls.base_delay * (2 ** retry_count) * (1 + random.random())
                    await asyncio.sleep(wait_time)
                else:
                    raise
            except asyncio.TimeoutError as ex:
                raise TimeoutError(f"Request timed out: {str(ex)}")
            except Exception as ex:
                raise
```

**Назначение**: Создает асинхронный генератор для взаимодействия с AI Chat DuckDuckGo.

**