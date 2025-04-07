# Модуль `DDG.py`

## Обзор

Модуль `DDG.py` предоставляет асинхронный интерфейс для взаимодействия с DuckDuckGo AI Chat. Он включает в себя функциональность для получения ответов от различных AI-моделей, таких как `gpt-4o-mini`, `meta-llama/Llama-3.3-70B-Instruct-Turbo`, `claude-3-haiku-20240307`, `o3-mini`, `mistralai/Mistral-Small-24B-Instruct-2501`. Модуль обеспечивает поддержку стриминга ответов, управление cookies, обработку ошибок и лимитов запросов.

## Подробнее

Модуль предназначен для интеграции с проектами, требующими взаимодействия с AI-моделями через DuckDuckGo AI Chat. Он обрабатывает установление соединения, аутентификацию, отправку запросов и получение ответов в асинхронном режиме. Модуль также содержит механизмы для обработки ошибок, таких как превышение лимита запросов и тайм-ауты, а также для повторных попыток отправки запросов.

## Классы

### `DuckDuckGoSearchException`

**Описание**: Базовый класс исключений для модуля `duckduckgo_search`.

### `Conversation`

**Описание**: Класс для хранения состояния разговора с AI-моделью.
**Inherits**:
- `JsonConversation` - предоставляет функциональность для сериализации и десериализации состояния разговора в JSON.

**Атрибуты**:

- `vqd` (str): Токен VQD (Visitor Query Data), необходимый для аутентификации запросов.
- `vqd_hash_1` (str): Хэш VQD, используемый для проверки подлинности запросов.
- `message_history` (Messages): Список сообщений в истории разговора.
- `cookies` (dict): Словарь cookies, используемых для аутентификации запросов.
- `fe_version` (str): Версия front-end, используемая для запросов.
- `model` (str): Модель, используемая в разговоре.

**Методы**:

- `__init__(self, model: str)`: Инициализирует объект `Conversation` с указанной моделью.

### `DDG`

**Описание**: Класс, предоставляющий функциональность для взаимодействия с DuckDuckGo AI Chat.
**Inherits**:
- `AsyncGeneratorProvider` - обеспечивает асинхронную генерацию ответов.
- `ProviderModelMixin` - предоставляет методы для работы с моделями.

**Атрибуты**:

- `label` (str): Метка провайдера ("DuckDuckGo AI Chat").
- `url` (str): URL главной страницы DuckDuckGo AI Chat ("https://duckduckgo.com/aichat").
- `api_endpoint` (str): URL API для отправки запросов ("https://duckduckgo.com/duckchat/v1/chat").
- `status_url` (str): URL для получения статуса ("https://duckduckgo.com/duckchat/v1/status").
- `working` (bool): Флаг, указывающий, работает ли провайдер (True).
- `supports_stream` (bool): Флаг, указывающий, поддерживает ли провайдер стриминг ответов (True).
- `supports_system_message` (bool): Флаг, указывающий, поддерживает ли провайдер системные сообщения (True).
- `supports_message_history` (bool): Флаг, указывающий, поддерживает ли провайдер историю сообщений (True).
- `default_model` (str): Модель, используемая по умолчанию ("gpt-4o-mini").
- `models` (list): Список поддерживаемых моделей.
- `model_aliases` (dict): Словарь псевдонимов моделей.
- `last_request_time` (float): Время последнего запроса.
- `max_retries` (int): Максимальное количество повторных попыток.
- `base_delay` (int): Базовая задержка между повторными попытками.
- `_chat_xfe` (str): Классовая переменная для хранения версии front-end.

**Методы**:

- `sha256_base64(text: str) -> str`: Возвращает base64-encoded SHA256 хэш переданного текста.
- `parse_dom_fingerprint(js_text: str) -> str`: Извлекает и возвращает DOM fingerprint из JavaScript текста.
- `parse_server_hashes(js_text: str) -> list`: Извлекает и возвращает список server hashes из JavaScript текста.
- `build_x_vqd_hash_1(vqd_hash_1: str, headers: dict) -> str`: Строит значение заголовка `x-vqd-hash-1` на основе переданных параметров.
- `validate_model(model: str) -> str`: Проверяет и возвращает корректное имя модели.
- `sleep(multiplier=1.0)`: Реализует ограничение скорости между запросами.
- `get_default_cookies(session: ClientSession) -> dict`: Получает cookies по умолчанию, необходимые для API запросов.
- `fetch_fe_version(session: ClientSession) -> str`: Получает версию front-end из начальной загрузки страницы.
- `fetch_vqd_and_hash(session: ClientSession, retry_count: int = 0) -> tuple[str, str]`: Получает VQD токен и хэш для чат-сессии с повторными попытками.
- `create_async_generator(...) -> AsyncResult`: Создает асинхронный генератор для взаимодействия с DuckDuckGo AI Chat.

## Функции

### `sha256_base64`

```python
@staticmethod
def sha256_base64(text: str) -> str:
    """Return the base64 encoding of the SHA256 digest of the text."""
    sha256_hash = hashlib.sha256(text.encode("utf-8")).digest()
    return base64.b64encode(sha256_hash).decode()
```

**Назначение**: Вычисляет SHA256 хэш переданного текста и возвращает его base64 представление.

**Параметры**:
- `text` (str): Текст для вычисления хэша.

**Возвращает**:
- `str`: Base64 представление SHA256 хэша текста.

**Как работает функция**:
1. Кодирует входной текст `text` в байты, используя кодировку UTF-8.
2. Вычисляет SHA256 хэш полученных байтов.
3. Кодирует полученный хэш в формат base64.
4. Декодирует base64 представление в строку UTF-8 и возвращает результат.

```
Текст -> Кодирование в UTF-8 -> Вычисление SHA256 хэша -> Кодирование в base64 -> Декодирование в UTF-8 -> Результат
```

**Примеры**:

```python
text = "example text"
result = DDG.sha256_base64(text)
print(result)  # Вывод: некоторая строка base64
```

### `parse_dom_fingerprint`

```python
@staticmethod
def parse_dom_fingerprint(js_text: str) -> str:
    """ """
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

**Назначение**: Извлекает DOM fingerprint из JavaScript текста.

**Параметры**:
- `js_text` (str): JavaScript текст, содержащий DOM fingerprint.

**Возвращает**:
- `str`: DOM fingerprint в виде строки.

**Как работает функция**:
1. Проверяет, установлен ли `BeautifulSoup`. Если нет, возвращает "1000".
2. Извлекает HTML сниппет и значение смещения из JavaScript текста.
3. Использует `BeautifulSoup` для парсинга HTML сниппета.
4. Вычисляет длину содержимого `body` в HTML сниппете.
5. Вычисляет DOM fingerprint как сумму значения смещения и длины содержимого `body`.
6. Возвращает DOM fingerprint в виде строки.

```
js_text -> Проверка BeautifulSoup -> Извлечение HTML сниппета и значения смещения -> Парсинг HTML с BeautifulSoup -> Вычисление длины содержимого body -> Вычисление DOM fingerprint -> Результат
```

**Примеры**:

```python
js_text = "example javascript text with e.innerHTML = '<p>test</p>'; and return String(100)"
result = DDG.parse_dom_fingerprint(js_text)
print(result)  # Вывод: строка с DOM fingerprint
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

**Назначение**: Извлекает список server hashes из JavaScript текста.

**Параметры**:
- `js_text` (str): JavaScript текст, содержащий server hashes.

**Возвращает**:
- `list`: Список server hashes.

**Как работает функция**:
1. Пытается извлечь список server hashes из JavaScript текста, разделяя строку по определенным разделителям.
2. Возвращает список server hashes.
3. Если извлечение не удалось, возвращает `["1", "2"]`.

```
js_text -> Извлечение server hashes -> Результат
```

**Примеры**:

```python
js_text = 'example javascript text with server_hashes: ["hash1","hash2"]'
result = DDG.parse_server_hashes(js_text)
print(result)  # Вывод: ['hash1', 'hash2']
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

**Назначение**: Создает значение заголовка `x-vqd-hash-1` на основе предоставленных параметров.

**Параметры**:
- `vqd_hash_1` (str): Хэш VQD в формате base64.
- `headers` (dict): Словарь заголовков запроса.

**Возвращает**:
- `str`: Значение заголовка `x-vqd-hash-1`.

**Как работает функция**:
1. Декодирует `vqd_hash_1` из base64 в строку.
2. Извлекает server hashes из декодированной строки с помощью `parse_server_hashes`.
3. Извлекает DOM fingerprint из декодированной строки с помощью `parse_dom_fingerprint`.
4. Формирует строку `ua_fingerprint` из User-Agent и `sec-ch-ua` заголовков.
5. Вычисляет SHA256 хэш `ua_fingerprint` и DOM fingerprint с помощью `sha256_base64`.
6. Формирует словарь `final_result`, содержащий server hashes, client hashes (ua_hash и dom_hash) и пустой словарь signals.
7. Кодирует словарь `final_result` в JSON и затем в base64.
8. Возвращает закодированную строку.

```
vqd_hash_1, headers -> Декодирование vqd_hash_1 из base64 -> Извлечение server hashes -> Извлечение DOM fingerprint -> Формирование ua_fingerprint -> Вычисление SHA256 хэшей ua_fingerprint и DOM fingerprint -> Формирование словаря final_result -> Кодирование словаря в JSON и base64 -> Результат
```

**Примеры**:

```python
vqd_hash_1 = "some_base64_vqd_hash"
headers = {"User-Agent": "Mozilla/5.0", "sec-ch-ua": "Chromium"}
result = DDG.build_x_vqd_hash_1(vqd_hash_1, headers)
print(result)  # Вывод: строка x-vqd-hash-1
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
- `ModelNotSupportedError`: Если указанная модель не поддерживается.

**Как работает функция**:
1. Если `model` не указана, возвращает `default_model`.
2. Если `model` есть в `model_aliases`, заменяет `model` на соответствующий псевдоним.
3. Если `model` нет в `models`, вызывает исключение `ModelNotSupportedError`.
4. Возвращает `model`.

```
model -> Проверка на None -> Проверка в model_aliases -> Проверка в models -> Результат
```

**Примеры**:

```python
model = "gpt-4"
result = DDG.validate_model(model)
print(result)  # Вывод: "gpt-4o-mini"

model = "unsupported_model"
try:
    result = DDG.validate_model(model)
except ModelNotSupportedError as ex:
    print(f"Error: {ex}")  # Вывод: "Error: Model unsupported_model not supported. Available models: ..."
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

**Назначение**: Реализует ограничение скорости между запросами.

**Параметры**:
- `multiplier` (float, optional): Множитель задержки. По умолчанию `1.0`.

**Как работает функция**:
1. Получает текущее время.
2. Если `last_request_time` больше 0, вычисляет задержку на основе разницы между текущим временем и `last_request_time`, умноженной на `multiplier`.
3. Если задержка больше 0, ожидает в течение вычисленного времени.
4. Обновляет `last_request_time` текущим временем.

```
multiplier -> Вычисление задержки -> Ожидание -> Обновление last_request_time
```

**Примеры**:

```python
await DDG.sleep(multiplier=2.0)
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
    except Exception as ex:
        return {}
```

**Назначение**: Получает cookies по умолчанию, необходимые для API запросов.

**Параметры**:
- `session` (ClientSession): Асинхронная клиентская сессия.

**Возвращает**:
- `dict`: Словарь cookies.

**Как работает функция**:
1. Ожидает с помощью `sleep`.
2. Отправляет GET запрос к `cls.url` для получения cookies.
3. Устанавливает необходимые cookies вручную (`dcs` и `dcm`).
4. Обновляет `session.cookie_jar` с установленными cookies.
5. Возвращает словарь cookies.

```
session -> Ожидание -> GET запрос к cls.url -> Установка cookies -> Обновление session.cookie_jar -> Результат
```

**Примеры**:

```python
async with ClientSession() as session:
    cookies = await DDG.get_default_cookies(session)
    print(cookies)  # Вывод: словарь cookies
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
    except Exception as ex:
        return ""
```

**Назначение**: Получает версию front-end из начальной загрузки страницы.

**Параметры**:
- `session` (ClientSession): Асинхронная клиентская сессия.

**Возвращает**:
- `str`: Версия front-end.

**Как работает функция**:
1. Если `cls._chat_xfe` уже установлена, возвращает её.
2. Отправляет GET запрос к URL для получения версии front-end.
3. Извлекает компоненты версии front-end из содержимого ответа.
4. Формирует версию front-end и сохраняет её в `cls._chat_xfe`.
5. Возвращает версию front-end.

```
session -> Проверка cls._chat_xfe -> GET запрос к URL -> Извлечение компонентов версии front-end -> Формирование и сохранение версии front-end -> Результат
```

**Примеры**:

```python
async with ClientSession() as session:
    fe_version = await DDG.fetch_fe_version(session)
    print(fe_version)  # Вывод: версия front-end
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

**Назначение**: Получает VQD токен и хэш для чат-сессии с повторными попытками.

**Параметры**:
- `session` (ClientSession): Асинхронная клиентская сессия.
- `retry_count` (int, optional): Количество повторных попыток. По умолчанию `0`.

**Возвращает**:
- `tuple[str, str]`: Кортеж, содержащий VQD токен и хэш.

**Вызывает исключения**:
- `RuntimeError`: Если не удалось получить VQD токен и хэш после `cls.max_retries` попыток.

**Как работает функция**:
1. Проверяет наличие cookies в сессии и, если их нет, получает их с помощью `get_default_cookies`.
2. Отправляет GET запрос к `cls.status_url` с заданными заголовками.
3. Извлекает VQD токен и хэш из заголовков ответа.
4. Если VQD токен получен, возвращает его вместе с хэшем.
5. Если VQD токен не получен, вызывает исключение `RuntimeError`.
6. В случае ошибки увеличивает счетчик повторных попыток и повторяет запрос, если количество попыток не превышает `cls.max_retries`.

```
session, retry_count -> Проверка наличия cookies -> GET запрос к cls.status_url -> Извлечение VQD токена и хэша -> Результат
```

**Примеры**:

```python
async with ClientSession() as session:
    vqd, vqd_hash = await DDG.fetch_vqd_and_hash(session)
    print(vqd, vqd_hash)  # Вывод: VQD токен и хэш
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

                        if line.startswith("data:"):
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

**Назначение**: Создает асинхронный генератор для взаимодействия с DuckDuckGo AI Chat.

**Параметры**:
- `model` (str): Имя модели для использования.
- `messages` (Messages): Список сообщений для отправки.
- `proxy` (str, optional): URL прокси-сервера. По умолчанию `None`.
- `timeout` (int, optional): Время ожидания запроса в секундах. По умолчанию `60`.
- `cookies` (Cookies, optional): Словарь cookies. По умолчанию `None`.
- `conversation` (Conversation, optional): Объект `Conversation` для продолжения существующего разговора. По умолчанию `None`.
- `return_conversation` (bool, optional): Флаг, указывающий, нужно ли возвращать объект `Conversation` после каждого ответа. По умолчанию `False`.

**Возвращает**:
- `AsyncResult`: Асинхронный генератор, возвращающий ответы от AI-модели.

**Вызывает исключения**:
- `ModelNotSupportedError`: Если указанная модель не поддерживается.
- `RateLimitError`: Если превышен лимит запросов.
- `TimeoutError`: Если время ожидания запроса истекло.
- `DuckDuckGoSearchException`: Если произошла ошибка при взаимодействии с DuckDuckGo AI Chat.
- `ConversationLimitError`: Если превышен лимит на количество разговоров.

**Как работает функция**:

1. **Шаг 1: Валидация модели**:
   - Проверяет и приводит имя модели к корректному виду с помощью `validate_model`.

2. **Шаг 2: Цикл повторных попыток**:
   - Организует цикл `while`, который позволяет повторить запрос в случае ошибки (например, при лимите запросов).
   - Максимальное количество попыток определяется параметром `cls.max_retries`.

3. **Шаг 3: Создание асинхронной сессии**:
   - Создает асинхронную сессию `ClientSession` с заданным таймаутом и cookies.

4. **Шаг 4: Получение версии Front-End**:
   - Если версия Front-End (`cls._chat_xfe`) еще не известна, запрашивает её с помощью `fetch_fe_version`.

5. **Шаг 5: Инициализация или обновление разговора**:
   - Если объект `conversation` не передан, создается новый объект `Conversation`:
     - Запрашиваются начальные cookies, если они не были переданы.
     - Получаются VQD-токены с помощью `fetch_vqd_and_hash`.
     - Формируется начальное сообщение пользователя на основе переданных сообщений `messages`.
   - Если объект `conversation` передан, он обновляется новым сообщением пользователя.

6. **Шаг 6: Подготовка заголовков запроса**:
   - Формируются заголовки запроса, включая версию Front-End, VQD-токены и User-Agent.
   - Важно: при первом запросе `x-vqd-hash-1` переда