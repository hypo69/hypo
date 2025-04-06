# Модуль `Liaobots.py`

## Обзор

Модуль `Liaobots.py` предоставляет асинхронный генератор для взаимодействия с провайдером Liaobots, который поддерживает различные модели, включая Claude, DeepSeek, Gemini и GPT. Он включает в себя поддержку истории сообщений и системных сообщений.

## Подробнее

Этот модуль предназначен для обеспечения асинхронного взаимодействия с API Liaobots. Он использует `aiohttp` для выполнения HTTP-запросов и предоставляет методы для получения ответов от моделей Liaobots. Модуль поддерживает выбор различных моделей, установку прокси и управление авторизацией.
Расположение модуля: `hypotez/src/endpoints/gpt4free/g4f/Provider/Liaobots.py`

## Содержание

- [Классы](#классы)
  - [Liaobots](#liaobots)
- [Словари](#словари)
  - [models](#models)
- [Функции](#функции)
  - [is_supported](#is_supported)
  - [create_async_generator](#create_async_generator)
  - [initialize_auth_code](#initialize_auth_code)
  - [ensure_auth_code](#ensure_auth_code)

## Словари

### `models`

Словарь содержит информацию о поддерживаемых моделях, включая их ID, имена, провайдеров, максимальную длину и лимиты токенов.

## Классы

### `Liaobots`

**Описание**: Класс `Liaobots` предоставляет асинхронный генератор для работы с моделями Liaobots.

**Наследует**:
- `AsyncGeneratorProvider`: Обеспечивает асинхронную генерацию ответов.
- `ProviderModelMixin`: Предоставляет функциональность для работы с моделями провайдера.

**Атрибуты**:
- `url` (str): URL провайдера Liaobots (`https://liaobots.site`).
- `working` (bool): Флаг, указывающий, работает ли провайдер (всегда `True`).
- `supports_message_history` (bool): Флаг, указывающий, поддерживается ли история сообщений (всегда `True`).
- `supports_system_message` (bool): Флаг, указывающий, поддерживаются ли системные сообщения (всегда `True`).
- `default_model` (str): Модель, используемая по умолчанию (`gpt-4o-2024-08-06`).
- `models` (list): Список поддерживаемых моделей.
- `model_aliases` (dict): Словарь псевдонимов моделей для удобства использования.
- `_auth_code` (str): Код авторизации для доступа к API Liaobots (изначально пустая строка).
- `_cookie_jar`: Объект для хранения cookie-файлов сессии.

**Методы**:
- `is_supported(model: str) -> bool`: Проверяет, поддерживается ли указанная модель.
- `create_async_generator(model: str, messages: Messages, proxy: str = None, connector: BaseConnector = None, **kwargs) -> AsyncResult`: Создает асинхронный генератор для получения ответов от Liaobots.
- `initialize_auth_code(session: ClientSession) -> None`: Инициализирует код авторизации, выполняя необходимые запросы для входа.
- `ensure_auth_code(session: ClientSession) -> None`: Проверяет и при необходимости инициализирует код авторизации.

## Функции

### `is_supported`

```python
@classmethod
def is_supported(cls, model: str) -> bool:
    """
    Check if the given model is supported.
    """
    return model in models or model in cls.model_aliases
```

**Назначение**: Проверяет, поддерживается ли указанная модель провайдером Liaobots.

**Параметры**:
- `model` (str): Имя модели, которую необходимо проверить.

**Возвращает**:
- `bool`: `True`, если модель поддерживается, `False` в противном случае.

**Как работает функция**:
1. Функция проверяет, содержится ли `model` в словаре `models` или в словаре `model_aliases` класса `Liaobots`.
2. Если модель найдена в одном из этих словарей, функция возвращает `True`, иначе возвращает `False`.

**Примеры**:

```python
Liaobots.is_supported("gpt-4o-2024-08-06")  # Вернет True
Liaobots.is_supported("nonexistent-model")  # Вернет False
```

### `create_async_generator`

```python
@classmethod
async def create_async_generator(
    cls,
    model: str,
    messages: Messages,
    proxy: str = None,
    connector: BaseConnector = None,
    **kwargs
) -> AsyncResult:
    """
    
    """
    model = cls.get_model(model)
    
    headers = {
        "referer": "https://liaobots.work/",
        "origin": "https://liaobots.work",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36",
    }
    async with ClientSession(
        headers=headers,
        cookie_jar=cls._cookie_jar,
        connector=get_connector(connector, proxy, True)
    ) as session:
        data = {
            "conversationId": str(uuid.uuid4()),
            "model": models[model],
            "messages": messages,
            "key": "",
            "prompt": kwargs.get("system_message", "You are a helpful assistant."),
        }
        if not cls._auth_code:
            async with session.post(
                "https://liaobots.work/recaptcha/api/login",
                data={"token": "abcdefghijklmnopqrst"},
                verify_ssl=False
            ) as response:
                await raise_for_status(response)
        try:
            async with session.post(
                "https://liaobots.work/api/user",
                json={"authcode": cls._auth_code},
                verify_ssl=False
            ) as response:
                await raise_for_status(response)
                cls._auth_code = (await response.json(content_type=None))["authCode"]
                if not cls._auth_code:
                    raise RuntimeError("Empty auth code")
                cls._cookie_jar = session.cookie_jar
            async with session.post(
                "https://liaobots.work/api/chat",
                json=data,
                headers={"x-auth-code": cls._auth_code},
                verify_ssl=False
            ) as response:
                await raise_for_status(response)
                async for line in response.content:
                    if line.startswith(b"data: "):\
                        yield json.loads(line[6:]).get("content")
        except:
            async with session.post(
                "https://liaobots.work/api/user",
                json={"authcode": "jGDRFOqHcZKAo"},
                verify_ssl=False
            ) as response:
                await raise_for_status(response)
                cls._auth_code = (await response.json(content_type=None))["authCode"]
                if not cls._auth_code:
                    raise RuntimeError("Empty auth code")
                cls._cookie_jar = session.cookie_jar
            async with session.post(
                "https://liaobots.work/api/chat",
                json=data,
                headers={"x-auth-code": cls._auth_code},
                verify_ssl=False
            ) as response:
                await raise_for_status(response)
                async for line in response.content:
                    if line.startswith(b"data: "):\
                        yield json.loads(line[6:]).get("content")
```

**Назначение**: Создает асинхронный генератор для получения ответов от API Liaobots.

**Параметры**:
- `model` (str): Имя модели, которую необходимо использовать.
- `messages` (Messages): Список сообщений для отправки в API.
- `proxy` (str, optional): URL прокси-сервера. По умолчанию `None`.
- `connector` (BaseConnector, optional): Aiohttp коннектор. По умолчанию `None`.
- `**kwargs`: Дополнительные аргументы, такие как `system_message`.

**Возвращает**:
- `AsyncResult`: Асинхронный генератор, выдающий ответы от API.

**Как работает функция**:
1. **Получение модели**: Преобразует псевдоним модели в фактическое имя модели, используя `cls.get_model(model)`.
2. **Формирование заголовков**: Создает заголовки HTTP-запроса, включая `referer`, `origin` и `user-agent`.
3. **Создание сессии**: Использует `aiohttp.ClientSession` для управления HTTP-соединениями.
4. **Формирование данных**: Создает словарь `data` с информацией о запросе, включая ID разговора, модель, сообщения и системное сообщение.
5. **Авторизация (если необходимо)**:
   - Если `cls._auth_code` пуст, выполняется запрос к `https://liaobots.work/recaptcha/api/login` для получения кода авторизации.
6. **Отправка запроса и получение ответа**:
   - Отправляется POST-запрос к `https://liaobots.work/api/user` для получения кода авторизации.
   - Отправляется POST-запрос к `https://liaobots.work/api/chat` с данными запроса и заголовком `x-auth-code`.
   - Полученный ответ обрабатывается построчно, и каждая строка, начинающаяся с `data: `, декодируется как JSON и извлекается содержимое поля `content`.
   - Асинхронно генерирует содержимое поля `content` для каждой строки ответа.
7. **Обработка ошибок**:
   - В случае возникновения ошибки, происходит повторная попытка запроса кода авторизации и отправки запроса к API.

**ASCII flowchart**:

```
    Получение модели (model)
    ↓
    Формирование заголовков (headers)
    ↓
    Создание сессии (session)
    ↓
    Формирование данных (data)
    ↓
    Проверка авторизации (cls._auth_code)
    ├── Нет авторизации
    │   ↓
    │   Запрос кода авторизации (/recaptcha/api/login)
    │   ↓
    └── Есть авторизация или код получен
        ↓
        Отправка запроса к API (/api/user) для получения кода авторизации
        ↓
        Отправка запроса к API (/api/chat)
        ↓
        Обработка ответа
        ↓
        Генерация содержимого (content)
```

**Примеры**:

```python
messages = [{"role": "user", "content": "Hello"}
async for response in Liaobots.create_async_generator(model="gpt-4o-2024-08-06", messages=messages):
    print(response)
```

### `initialize_auth_code`

```python
@classmethod
async def initialize_auth_code(cls, session: ClientSession) -> None:
    """
    Initialize the auth code by making the necessary login requests.
    """
    async with session.post(
        "https://liaobots.work/api/user",
        json={"authcode": "pTIQr4FTnVRfr"},
        verify_ssl=False
    ) as response:
        await raise_for_status(response)
        cls._auth_code = (await response.json(content_type=None))["authCode"]
        if not cls._auth_code:
            raise RuntimeError("Empty auth code")
        cls._cookie_jar = session.cookie_jar
```

**Назначение**: Инициализирует код авторизации, выполняя необходимые запросы для входа.

**Параметры**:
- `session` (ClientSession): Aiohttp клиентская сессия.

**Возвращает**:
- `None`

**Как работает функция**:
1. Отправляет POST-запрос к `https://liaobots.work/api/user` с фиксированным кодом авторизации.
2. Получает код авторизации из JSON-ответа.
3. Если код авторизации пуст, вызывает исключение `RuntimeError`.
4. Сохраняет cookie-файлы сессии в `cls._cookie_jar`.

**ASCII flowchart**:

```
    Отправка запроса к API (/api/user)
    ↓
    Получение кода авторизации из ответа
    ↓
    Проверка кода авторизации
    ├── Код пуст
    │   ↓
    │   Вызов исключения RuntimeError
    │   ↓
    └── Код получен
        ↓
        Сохранение cookie-файлов
```

**Примеры**:

```python
async with ClientSession() as session:
    await Liaobots.initialize_auth_code(session)
```

### `ensure_auth_code`

```python
@classmethod
async def ensure_auth_code(cls, session: ClientSession) -> None:
    """
    Ensure the auth code is initialized, and if not, perform the initialization.
    """
    if not cls._auth_code:
        await cls.initialize_auth_code(session)
```

**Назначение**: Проверяет, инициализирован ли код авторизации, и если нет, выполняет инициализацию.

**Параметры**:
- `session` (ClientSession): Aiohttp клиентская сессия.

**Возвращает**:
- `None`

**Как работает функция**:
1. Проверяет, является ли `cls._auth_code` пустой строкой.
2. Если `cls._auth_code` пуст, вызывает `cls.initialize_auth_code(session)` для инициализации кода авторизации.

**ASCII flowchart**:

```
    Проверка авторизации (cls._auth_code)
    ├── Нет авторизации
    │   ↓
    │   Инициализация кода авторизации (initialize_auth_code)
    │   ↓
    └── Есть авторизация
        ↓
        Конец
```

**Примеры**:

```python
async with ClientSession() as session:
    await Liaobots.ensure_auth_code(session)