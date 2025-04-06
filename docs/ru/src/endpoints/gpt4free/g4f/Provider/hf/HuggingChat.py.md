# Модуль HuggingChat

## Обзор

Модуль `HuggingChat.py` предоставляет класс `HuggingChat`, который позволяет взаимодействовать с чат-моделью Hugging Face. Он поддерживает как текстовые, так и визуальные модели, требующие авторизации. Модуль асинхронный и использует библиотеку `curl_cffi` для эффективного выполнения HTTP-запросов.

## Подробнее

Этот модуль является частью проекта `hypotez` и предназначен для интеграции с различными AI-моделями, предоставляемыми Hugging Face. Он позволяет создавать и поддерживать диалоги с этими моделями, отправлять текстовые запросы и изображения, а также получать ответы в режиме реального времени. Модуль также поддерживает авторизацию через cookies и предоставляет функциональность для автоматического обновления conversation ID.

## Классы

### `Conversation`

**Описание**: Класс для хранения информации о текущем диалоге с моделью.

**Атрибуты**:
- `models` (dict): Словарь, содержащий conversation ID для каждой используемой модели.

### `HuggingChat`

**Описание**: Класс, реализующий взаимодействие с Hugging Face Chat API.

**Наследует**:
- `AsyncAuthedProvider`: Обеспечивает асинхронную авторизацию.
- `ProviderModelMixin`: Предоставляет функциональность выбора модели.

**Атрибуты**:
- `domain` (str): Домен Hugging Face.
- `origin` (str): Базовый URL Hugging Face.
- `url` (str): URL для взаимодействия с чатом.
- `working` (bool): Флаг, указывающий на работоспособность провайдера.
- `use_nodriver` (bool): Флаг, указывающий на использование без драйвера.
- `supports_stream` (bool): Флаг, указывающий на поддержку потоковой передачи данных.
- `needs_auth` (bool): Флаг, указывающий на необходимость авторизации.
- `default_model` (str): Модель, используемая по умолчанию для текста.
- `default_vision_model` (str): Модель, используемая по умолчанию для изображений.
- `model_aliases` (dict): Псевдонимы моделей.
- `image_models` (list): Список моделей, поддерживающих обработку изображений.
- `text_models` (list): Список моделей, поддерживающих обработку текста.
- `models` (list): Список доступных моделей.
- `vision_models` (list): Список моделей, поддерживающих обработку визуальных данных.

**Методы**:
- `get_models()`: Получает список доступных моделей из Hugging Face.
- `on_auth_async()`: Выполняет асинхронную авторизацию пользователя.
- `create_authed()`: Создает аутентифицированный запрос к Hugging Face Chat API.
- `create_conversation()`: Создает новый диалог с моделью.
- `fetch_message_id()`: Получает ID последнего сообщения в диалоге.

## Функции

### `get_models`

```python
@classmethod
def get_models(cls):
    """Получает список доступных моделей из Hugging Face.

    Args:
        cls: Класс `HuggingChat`.

    Returns:
        list: Список доступных моделей.

    Raises:
        Exception: Если не удается получить список моделей.

    Как работает функция:
    1. Выполняется HTTP-запрос к странице чата Hugging Face для получения списка моделей.
    2. Извлекается JSON с моделями из HTML-кода страницы.
    3. Обновляется список текстовых моделей и общий список моделей класса.
    4. В случае ошибки логируется исключение и устанавливается резервный список моделей.

    ASCII flowchart:

    A[Начало]
    │
    B[HTTP-запрос к Hugging Face]
    │
    C[Извлечение JSON с моделями]
    │
    D[Обновление списков моделей]
    │
    E[Обработка ошибок]
    │
    F[Конец]

    Примеры:
        >>> HuggingChat.get_models()
        ['model1', 'model2', 'model3']
    """
    ...
```

### `on_auth_async`

```python
@classmethod
async def on_auth_async(cls, cookies: Cookies = None, proxy: str = None, **kwargs) -> AsyncIterator:
    """Выполняет асинхронную авторизацию пользователя.

    Args:
        cls: Класс `HuggingChat`.
        cookies (Cookies, optional): Cookies для авторизации. По умолчанию `None`.
        proxy (str, optional): Прокси-сервер для подключения. По умолчанию `None`.
        **kwargs: Дополнительные аргументы.

    Yields:
        AuthResult: Результат авторизации.
        RequestLogin: Запрос на авторизацию, если требуется.

    Как работает функция:
    1. Проверяет наличие cookies. Если cookies содержат `hf-chat`, возвращает результат авторизации.
    2. Если cookies отсутствуют, запрашивает URL для логина и выполняет авторизацию через `get_args_from_nodriver`.
    3. Генерирует session ID, если авторизация не требуется.

    ASCII flowchart:

    A[Начало]
    │
    B[Проверка наличия cookies]
    │
    C[Авторизация через cookies]
    │
    D[Запрос URL для логина]
    │
    E[Авторизация через get_args_from_nodriver]
    │
    F[Генерация session ID]
    │
    G[Конец]

    Примеры:
        >>> async for result in HuggingChat.on_auth_async(cookies={'hf-chat': 'session_id'}):
        ...     print(result)
        AuthResult(cookies={'hf-chat': 'session_id'}, impersonate='chrome', headers={'header1': 'value1'})
    """
    ...
```

### `create_authed`

```python
@classmethod
async def create_authed(
    cls,
    model: str,
    messages: Messages,
    auth_result: AuthResult,
    prompt: str = None,
    media: MediaListType = None,
    return_conversation: bool = False,
    conversation: Conversation = None,
    web_search: bool = False,
    **kwargs
) -> AsyncResult:
    """Создает аутентифицированный запрос к Hugging Face Chat API.

    Args:
        cls: Класс `HuggingChat`.
        model (str): Имя используемой модели.
        messages (Messages): Список сообщений для отправки.
        auth_result (AuthResult): Результат авторизации.
        prompt (str, optional): Дополнительный промпт. По умолчанию `None`.
        media (MediaListType, optional): Список медиафайлов для отправки. По умолчанию `None`.
        return_conversation (bool, optional): Флаг, указывающий на необходимость возврата объекта диалога. По умолчанию `False`.
        conversation (Conversation, optional): Объект диалога. По умолчанию `None`.
        web_search (bool, optional): Флаг, указывающий на необходимость использования веб-поиска. По умолчанию `False`.
        **kwargs: Дополнительные аргументы.

    Yields:
        str: Текст ответа от модели.
        ImageResponse: Ответ с изображением, если модель вернула изображение.
        Sources: Источники, найденные в интернете.
        TitleGeneration: Сгенерированный заголовок для диалога.
        Reasoning: Объяснение от модели.
        FinishReason: Причина завершения диалога.

    Raises:
        MissingRequirementsError: Если не установлена библиотека `curl_cffi`.

    Как работает функция:
    1. Проверяет наличие необходимых библиотек и выбирает модель.
    2. Создает или использует существующий объект диалога.
    3. Создает conversation ID, если его нет.
    4. Форматирует запрос и отправляет его в Hugging Face Chat API.
    5. Обрабатывает ответ и возвращает текст, изображения или другие данные.

    ASCII flowchart:

    A[Начало]
    │
    B[Проверка библиотек и выбор модели]
    │
    C[Создание/использование объекта диалога]
    │
    D[Создание conversation ID]
    │
    E[Форматирование запроса]
    │
    F[Отправка запроса в Hugging Face Chat API]
    │
    G[Обработка ответа]
    │
    H[Конец]

    Примеры:
        >>> async for response in HuggingChat.create_authed(model='model1', messages=[{'role': 'user', 'content': 'Hello'}]):
        ...     print(response)
        Hello, how can I help you?
    """
    ...
```

### `create_conversation`

```python
@classmethod
def create_conversation(cls, session: Session, model: str):
    """Создает новый диалог с моделью.

    Args:
        cls: Класс `HuggingChat`.
        session (Session): Сессия `curl_cffi`.
        model (str): Имя модели для диалога.

    Returns:
        str: Conversation ID.

    Raises:
        MissingAuthError: Если отсутствует авторизация.
        ResponseError: Если произошла ошибка при создании диалога.

    Как работает функция:
    1. Формирует JSON-запрос с указанием модели.
    2. Отправляет POST-запрос к Hugging Face API для создания диалога.
    3. Обрабатывает ответ и возвращает conversation ID.
    4. В случае ошибок вызывает исключения `MissingAuthError` или `ResponseError`.

    ASCII flowchart:

    A[Начало]
    │
    B[Формирование JSON-запроса]
    │
    C[Отправка POST-запроса]
    │
    D[Обработка ответа]
    │
    E[Возврат conversation ID]
    │
    F[Конец]

    Примеры:
        >>> conversation_id = HuggingChat.create_conversation(session, 'model1')
        >>> print(conversation_id)
        conversation_123
    """
    ...
```

### `fetch_message_id`

```python
@classmethod
def fetch_message_id(cls, session: Session, conversation_id: str):
    """Получает ID последнего сообщения в диалоге.

    Args:
        cls: Класс `HuggingChat`.
        session (Session): Сессия `curl_cffi`.
        conversation_id (str): ID диалога.

    Returns:
        str: ID последнего сообщения.

    Raises:
        RuntimeError: Если не удается извлечь ID сообщения.

    Как работает функция:
    1. Отправляет GET-запрос к Hugging Face API для получения данных диалога.
    2. Разбирает ответ, извлекая JSON-объекты из каждой строки.
    3. Находит JSON с информацией о сообщениях и извлекает ID последнего сообщения.
    4. В случае ошибок вызывает исключение `RuntimeError`.

    ASCII flowchart:

    A[Начало]
    │
    B[Отправка GET-запроса]
    │
    C[Разбор ответа]
    │
    D[Извлечение JSON]
    │
    E[Извлечение ID сообщения]
    │
    F[Конец]

    Примеры:
        >>> message_id = HuggingChat.fetch_message_id(session, 'conversation_123')
        >>> print(message_id)
        message_456
    """
    ...