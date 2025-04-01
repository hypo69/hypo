# Модуль `Liaobots.py`

## Обзор

Модуль предоставляет класс `Liaobots`, который является асинхронным генератором для взаимодействия с провайдером Liaobots. Этот класс позволяет использовать различные модели, такие как Claude и Gemini, через API Liaobots. Он поддерживает сохранение истории сообщений и системные сообщения.

## Подробнее

Модуль содержит класс `Liaobots`, который наследуется от `AsyncGeneratorProvider` и `ProviderModelMixin`. Он определяет URL, поддерживает историю сообщений и системные сообщения. Также задаются модели по умолчанию и их алиасы. Класс использует асинхронные запросы для взаимодействия с API Liaobots и предоставляет методы для создания асинхронного генератора и инициализации кода аутентификации.

## Классы

### `Liaobots`

**Описание**: Класс для взаимодействия с провайдером Liaobots.

**Принцип работы**:
Класс `Liaobots` предназначен для обеспечения асинхронного взаимодействия с API Liaobots, поддерживающего различные модели, такие как Claude и Gemini. Он наследуется от `AsyncGeneratorProvider` и `ProviderModelMixin`, что позволяет использовать его как асинхронный генератор. Основной функционал класса включает создание асинхронного генератора для обмена сообщениями с API, инициализацию и обеспечение актуальности кода аутентификации, а также поддержку истории сообщений и системных сообщений.

**Методы**:
- `is_supported(model: str) -> bool`: Проверяет, поддерживается ли указанная модель.
- `create_async_generator(model: str, messages: Messages, proxy: str = None, connector: BaseConnector = None, **kwargs) -> AsyncResult`: Создает асинхронный генератор для взаимодействия с API Liaobots.
- `initialize_auth_code(session: ClientSession) -> None`: Инициализирует код аутентификации, выполняя необходимые запросы для входа в систему.
- `ensure_auth_code(session: ClientSession) -> None`: Проверяет, инициализирован ли код аутентификации, и выполняет инициализацию, если это необходимо.

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

**Назначение**: Проверяет, поддерживается ли указанная модель.

**Параметры**:
- `model` (str): Имя модели для проверки.

**Возвращает**:
- `bool`: `True`, если модель поддерживается, иначе `False`.

**Как работает функция**:
Функция проверяет, есть ли модель в списке поддерживаемых моделей (`models`) или в списке алиасов моделей (`model_aliases`). Если модель найдена хотя бы в одном из этих списков, функция возвращает `True`, иначе возвращает `False`.

**Примеры**:
```python
Liaobots.is_supported("gpt-4o-2024-08-06")  # Возвращает True
Liaobots.is_supported("claude-3.5-sonnet")  # Возвращает True
Liaobots.is_supported("unsupported-model")  # Возвращает False
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
    <Тут Ты пишешь что именно делает функция>
    """
```

**Назначение**: Создает асинхронный генератор для взаимодействия с API Liaobots.

**Параметры**:
- `model` (str): Имя модели для использования.
- `messages` (Messages): Список сообщений для отправки.
- `proxy` (str, optional): URL прокси-сервера. По умолчанию `None`.
- `connector` (BaseConnector, optional): Объект коннектора aiohttp. По умолчанию `None`.
- `**kwargs`: Дополнительные аргументы, такие как `system_message`.

**Возвращает**:
- `AsyncResult`: Асинхронный генератор, выдающий ответы от API.

**Вызывает исключения**:
- `RuntimeError`: Если не удается получить код аутентификации.

**Как работает функция**:

1. **Преобразование имени модели**:
   - `model = cls.get_model(model)`: Преобразует имя модели, используя алиасы, если это необходимо.

2. **Подготовка заголовков**:
   - Определяет заголовки HTTP-запроса, включая `referer`, `origin` и `user-agent`.

3. **Создание асинхронной сессии**:
   - `async with ClientSession(...) as session`: Создает асинхронную сессию для выполнения HTTP-запросов. Использует `get_connector` для настройки прокси и SSL.

4. **Подготовка данных для запроса**:
   - `data = {...}`: Формирует данные запроса, включая `conversationId` (случайный UUID), информацию о модели, сообщения и системное сообщение.

5. **Аутентификация**:
   - Проверяет, установлен ли код аутентификации (`cls._auth_code`). Если нет, пытается получить его, отправляя POST-запрос к `https://liaobots.work/recaptcha/api/login`.
   - Отправляет POST-запрос к `https://liaobots.work/api/user` с текущим кодом аутентификации. Если запрос успешен, обновляет `cls._auth_code` и `cls._cookie_jar`.

6. **Отправка сообщений и получение ответа**:
   - Отправляет POST-запрос к `https://liaobots.work/api/chat` с данными сообщения и заголовком `x-auth-code`.
   - Получает ответ от API и извлекает содержимое (`content`) из каждой строки, начинающейся с `data: `.
   - Возвращает содержимое в виде асинхронного генератора.

7. **Обработка исключений**:
   - Если происходит исключение во время аутентификации или отправки сообщений, функция повторяет попытку с альтернативным кодом аутентификации (`jGDRFOqHcZKAo`).

**Примеры**:
```python
messages = [{"role": "user", "content": "Hello, world!"}]
async for message in Liaobots.create_async_generator(model="gpt-4o", messages=messages):
    print(message)
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

**Назначение**: Инициализирует код аутентификации, выполняя необходимые запросы для входа в систему.

**Параметры**:
- `session` (ClientSession): Асинхронная сессия aiohttp для выполнения запросов.

**Как работает функция**:
Функция отправляет POST-запрос к `https://liaobots.work/api/user` с предопределенным кодом аутентификации (`pTIQr4FTnVRfr`). Если запрос успешен, извлекает код аутентификации из ответа, сохраняет его в `cls._auth_code` и обновляет `cls._cookie_jar`. Если код аутентификации не получен, вызывает исключение `RuntimeError`.

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

**Назначение**: Проверяет, инициализирован ли код аутентификации, и выполняет инициализацию, если это необходимо.

**Параметры**:
- `session` (ClientSession): Асинхронная сессия aiohttp для выполнения запросов.

**Как работает функция**:
Функция проверяет, установлен ли код аутентификации (`cls._auth_code`). Если код аутентификации не установлен, вызывает функцию `initialize_auth_code` для его инициализации.

**Примеры**:
```python
async with ClientSession() as session:
    await Liaobots.ensure_auth_code(session)