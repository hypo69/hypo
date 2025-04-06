# Модуль для работы с ChatGptEs
=====================================

Модуль предоставляет асинхронный генератор для взаимодействия с сервисом ChatGptEs. 
Он использует `curl_cffi` для обхода защиты Cloudflare и получения ответов от API.

## Обзор

Модуль предназначен для асинхронного взаимодействия с сервисом ChatGptEs. Он включает в себя:

- Поддержку моделей `gpt-4`, `gpt-4o`, `gpt-4o-mini`.
- Использование `curl_cffi` для обхода защиты Cloudflare.
- Автоматическое извлечение `nonce` и `post_id` из HTML страницы.

## Подробнее

Модуль `ChatGptEs` является частью проекта `hypotez` и предназначен для предоставления доступа к моделям GPT через API `chatgpt.es`. Он использует библиотеку `curl_cffi` для обхода защиты Cloudflare, что позволяет выполнять запросы к API без блокировки.

## Классы

### `ChatGptEs`

**Описание**: Класс для взаимодействия с ChatGptEs.

**Наследует**:
- `AsyncGeneratorProvider`: Обеспечивает асинхронную генерацию ответов.
- `ProviderModelMixin`: Предоставляет общие методы для работы с моделями.

**Атрибуты**:
- `url` (str): URL сервиса ChatGptEs (`"https://chatgpt.es"`).
- `api_endpoint` (str): URL API для отправки сообщений (`"https://chatgpt.es/wp-admin/admin-ajax.php"`).
- `working` (bool): Указывает, работает ли провайдер (всегда `True`).
- `supports_stream` (bool): Указывает, поддерживает ли провайдер потоковую передачу (`True`).
- `supports_system_message` (bool): Указывает, поддерживает ли провайдер системные сообщения (`False`).
- `supports_message_history` (bool): Указывает, поддерживает ли провайдер историю сообщений (`False`).
- `default_model` (str): Модель, используемая по умолчанию (`'gpt-4o'`).
- `models` (list): Список поддерживаемых моделей (`['gpt-4', default_model, 'gpt-4o-mini']`).
- `SYSTEM_PROMPT` (str): Системное сообщение, используемое для форматирования запросов.

**Методы**:
- `create_async_generator`: Создает асинхронный генератор для получения ответов от ChatGptEs.

## Функции

### `create_async_generator`

```python
@classmethod
async def create_async_generator(
    cls,
    model: str,
    messages: Messages,
    proxy: str = None,
    **kwargs
) -> AsyncResult:
    """Создает асинхронный генератор для получения ответов от ChatGptEs.

    Args:
        model (str): Модель для использования.
        messages (Messages): Список сообщений для отправки.
        proxy (str, optional): Прокси-сервер для использования. По умолчанию `None`.
        **kwargs: Дополнительные аргументы.

    Returns:
        AsyncResult: Асинхронный генератор, возвращающий ответы от ChatGptEs.

    Raises:
        MissingRequirementsError: Если не установлен пакет `curl_cffi`.
        ValueError: Если получен неожиданный формат ответа или произошла ошибка при запросе.

    **Как работает функция**:

    1.  **Проверка зависимостей**: Проверяет, установлен ли пакет `curl_cffi`. Если нет, вызывает исключение `MissingRequirementsError`.
    2.  **Подготовка запроса**:
        - Получает модель, используя `cls.get_model(model)`.
        - Форматирует промпт, объединяя системное сообщение и сообщения пользователя.
    3.  **Создание сессии**:
        - Создает сессию `curl_cffi.requests.Session`.
        - Устанавливает заголовки для имитации браузера.
        - Если указан прокси, устанавливает его для сессии.
    4.  **Первый запрос**:
        - Выполняет GET-запрос к `cls.url` для получения `nonce` и `post_id`.
        - Извлекает `nonce` и `post_id` из ответа, используя регулярные выражения.
    5.  **Подготовка данных**:
        - Генерирует случайный `client_id`.
        - Формирует данные для POST-запроса, включая `nonce`, `post_id`, `message` и другие параметры.
    6.  **POST-запрос**:
        - Отправляет POST-запрос к `cls.api_endpoint` с подготовленными данными.
        - Проверяет статус код ответа. Если он не равен 200, вызывает исключение `ValueError`.
    7.  **Обработка ответа**:
        - Извлекает данные из JSON-ответа.
        - Если в данных содержится сообщение об ошибке, вызывает исключение `ValueError`.
        - Генерирует данные из поля `data` результата.

    **Внутренние функции**: Нет.

    **ASCII flowchart**:

    ```
    Проверка зависимостей (curl_cffi установлен?)
    ↓
    Подготовка запроса (модель, промпт)
    ↓
    Создание сессии (headers, proxy)
    ↓
    Первый GET-запрос (получение nonce и post_id)
    ↓
    Извлечение nonce и post_id (регулярные выражения)
    ↓
    Подготовка данных (client_id, data)
    ↓
    POST-запрос (отправка данных)
    ↓
    Обработка ответа (статус код, JSON)
    ↓
    Генерация данных
    ```

    **Примеры**:

    ```python
    # Пример вызова функции create_async_generator
    model = "gpt-4o"
    messages = [{"role": "user", "content": "Hello"}]
    proxy = None
    generator = ChatGptEs.create_async_generator(model, messages, proxy)

    # Асинхронное получение данных из генератора
    async for message in generator:
        print(message)
    ```
    """
    if not has_curl_cffi:
        raise MissingRequirementsError('Install or update "curl_cffi" package | pip install -U curl_cffi')

    model = cls.get_model(model)
    prompt = f"{cls.SYSTEM_PROMPT} {format_prompt(messages)}"

    # Use curl_cffi with automatic Cloudflare bypass
    session = Session()
    session.headers.update({
        "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36",
        "referer": cls.url,
        "origin": cls.url,
        "accept": "*/*",
        "accept-language": "en-US,en;q=0.9",
        "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
        "x-requested-with": "XMLHttpRequest",
    })

    if proxy:
        session.proxies = {"https": proxy, "http": proxy}

    # First request to get nonce and post_id
    initial_response = session.get(cls.url, impersonate="chrome110")
    initial_text = initial_response.text

    # More comprehensive nonce extraction
    nonce_patterns = [
        r'<input\s+type=[\'"]hidden[\'"]\s+name=[\'"]_wpnonce[\'"]\s+value=[\'"]([^\'"]+)[\'"]',
        r'"_wpnonce":"([^"]+)"',
        r'var\s+wpaicg_nonce\s*=\s*[\'"]([^\'"]+)[\'"]',
        r'wpaicg_nonce\s*:\s*[\'"]([^\'"]+)[\'"]'
    ]

    nonce_ = None
    for pattern in nonce_patterns:
        match = re.search(pattern, initial_text)
        if match:
            nonce_ = match.group(1)
            break

    if not nonce_:
        # Try to find any nonce-like pattern as a last resort
        general_nonce = re.search(r'nonce[\'"]?\s*[=:]\s*[\'"]([a-zA-Z0-9]+)[\'"]', initial_text)
        if general_nonce:
            nonce_ = general_nonce.group(1)
        else:
            # Fallback, but this likely won't work
            nonce_ = "8cf9917be2"

    # Look for post_id in HTML
    post_id_patterns = [
        r'<input\s+type=[\'"]hidden[\'"]\s+name=[\'"]post_id[\'"]\s+value=[\'"]([^\'"]+)[\'"]',
        r'"post_id":"([^"]+)"',
        r'var\s+post_id\s*=\s*[\'"]?(\d+)[\'"]?'
    ]

    post_id = None
    for pattern in post_id_patterns:
        match = re.search(pattern, initial_text)
        if match:
            post_id = match.group(1)
            break

    if not post_id:
        post_id = "106"  # Default from curl example

    client_id = os.urandom(5).hex()

    # Prepare data
    data = {
        '_wpnonce': nonce_,
        'post_id': post_id,
        'url': cls.url,
        'action': 'wpaicg_chat_shortcode_message',
        'message': prompt,
        'bot_id': '0',
        'chatbot_identity': 'shortcode',
        'wpaicg_chat_client_id': client_id,
        'wpaicg_chat_history': json.dumps([f"Human: {prompt}"])
    }

    # Execute POST request
    response = session.post(
        cls.api_endpoint,
        data=data,
        impersonate="chrome110"
    )

    if response.status_code != 200:
        raise ValueError(f"Error: {response.status_code} - {response.text}")

    result = response.json()
    if "data" in result:
        if isinstance(result['data'], str) and "Du musst das Kästchen anklicken!" in result['data']:\
            raise ValueError(result['data'])
        yield result['data']
    else:
        raise ValueError(f"Unexpected response format: {result}")