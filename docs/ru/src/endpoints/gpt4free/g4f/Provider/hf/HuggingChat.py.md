# Модуль HuggingChat

## Обзор

Модуль `HuggingChat` предоставляет асинхронный интерфейс для взаимодействия с моделями Hugging Face. Он позволяет вести диалоги, отправлять изображения и выполнять другие задачи, используя API Hugging Face. Модуль поддерживает потоковую передачу ответов, аутентификацию и работу с мультимедийными данными.

## Подробнее

Модуль `HuggingChat` является частью проекта `hypotez` и предназначен для интеграции с различными AI-моделями через API Hugging Face. Он обеспечивает удобный способ аутентификации, создания и управления диалогами, а также обработки ответов от моделей.

Модуль использует `curl_cffi` для выполнения асинхронных HTTP-запросов, что обеспечивает высокую производительность и надежность. Он также включает поддержку прокси-серверов и обработку ошибок.

## Классы

### `Conversation`

**Описание**: Класс для управления состоянием диалога с моделью Hugging Face.

**Наследует**: `JsonConversation`

**Аттрибуты**:

- `models` (dict): Словарь, содержащий информацию о моделях, используемых в диалоге, включая идентификаторы диалогов и сообщений.

### `HuggingChat`

**Описание**: Класс, реализующий асинхронный интерфейс для взаимодействия с моделями Hugging Face.

**Наследует**: `AsyncAuthedProvider`, `ProviderModelMixin`

**Аттрибуты**:

- `domain` (str): Доменное имя Hugging Face ("huggingface.co").
- `origin` (str): Базовый URL для Hugging Face ("https://huggingface.co").
- `url` (str): URL для чата Hugging Face ("https://huggingface.co/chat").
- `working` (bool): Указывает, работает ли провайдер (всегда `True`).
- `use_nodriver` (bool): Указывает, использует ли провайдер драйвер браузера (всегда `True`).
- `supports_stream` (bool): Указывает, поддерживает ли провайдер потоковую передачу ответов (всегда `True`).
- `needs_auth` (bool): Указывает, требуется ли аутенентификация (всегда `True`).
- `default_model` (str): Модель, используемая по умолчанию.
- `default_vision_model` (str): Модель для обработки изображений, используемая по умолчанию.
- `model_aliases` (dict): Псевдонимы моделей.
- `image_models` (list): Список моделей, поддерживающих обработку изображений.
- `text_models` (list): Список текстовых моделей.

**Методы**:

- `get_models()`: Получает список доступных моделей из API Hugging Face.
- `on_auth_async()`: Выполняет аутентификацию пользователя и возвращает результат аутентификации.
- `create_authed()`: Создает аутентифицированный запрос к API Hugging Face и возвращает асинхронный результат.
- `create_conversation()`: Создает новый диалог с указанной моделью.
- `fetch_message_id()`: Получает идентификатор последнего сообщения в диалоге.

## Функции

### `get_models`

```python
@classmethod
def get_models(cls):
    """
    Получает список доступных моделей из API Hugging Face.

    Если список моделей еще не был загружен, функция выполняет HTTP-запрос к странице чата Hugging Face,
    извлекает список моделей из HTML-кода и сохраняет его в атрибуте `cls.models`.

    Returns:
        list: Список идентификаторов доступных моделей.

    Raises:
        Exception: Если происходит ошибка при чтении моделей.

    Как работает функция:
    1. Проверяет, загружены ли уже модели. Если да, возвращает сохраненный список.
    2. Если модели не загружены, выполняет HTTP-запрос к странице чата Hugging Face.
    3. Извлекает список моделей из HTML-кода, используя регулярные выражения.
    4. Преобразует извлеченный текст в JSON-формат.
    5. Обновляет атрибуты `cls.text_models`, `cls.models` и `cls.vision_models` класса `HuggingChat`.
    6. Логирует ошибки, если они возникают, и использует резервный список моделей.

    ASCII flowchart:

    A: Проверка, загружены ли модели
    |
    No
    |
    B: HTTP-запрос к странице чата Hugging Face
    |
    C: Извлечение списка моделей из HTML-кода
    |
    D: Преобразование текста в JSON
    |
    E: Обновление атрибутов класса
    |
    F: Возврат списка моделей
    Yes
    |
    F
    """
    ...
```

**Примеры**:

```python
models = HuggingChat.get_models()
print(models)
```

### `on_auth_async`

```python
@classmethod
async def on_auth_async(cls, cookies: Cookies = None, proxy: str = None, **kwargs) -> AsyncIterator:
    """
    Выполняет асинхронную аутентификацию пользователя.

    Функция проверяет наличие cookies для домена Hugging Face. Если cookies найдены,
    функция возвращает результат аутентификации с использованием этих cookies.
    Если cookies отсутствуют, функция запрашивает учетные данные у пользователя и выполняет вход.

    Args:
        cookies (Cookies, optional): Cookies для аутентификации. По умолчанию `None`.
        proxy (str, optional): URL прокси-сервера. По умолчанию `None`.
        **kwargs: Дополнительные аргументы.

    Returns:
        AsyncIterator: Асинхронный итератор, возвращающий результат аутентификации.

    Raises:
        MissingAuthError: Если аутентификация не удалась.

    Как работает функция:

    1. Проверяет наличие cookies. Если есть "hf-chat" в cookies, возвращает AuthResult с cookies.
    2. Если cookies нет, проверяет, требуется ли аутентификация. Если требуется, запрашивает логин.
    3. Получает аргументы из nodriver и возвращает AuthResult.
    4. Если аутентификация не требуется, генерирует session ID и возвращает AuthResult.

    ASCII flowchart:

    A: Проверка наличия cookies
    |
    Yes
    |
    B: Возврат AuthResult с cookies
    |
    End
    No
    |
    C: Проверка необходимости аутентификации
    |
    Yes
    |
    D: Запрос логина
    |
    E: Получение аргументов из nodriver
    |
    F: Возврат AuthResult
    |
    End
    No
    |
    G: Генерация session ID
    |
    H: Возврат AuthResult с session ID
    |
    End
    """
    ...
```

**Примеры**:

```python
async for auth_result in HuggingChat.on_auth_async(cookies={'hf-chat': 'session_id'}):
    print(auth_result)
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
    """
    Создает аутентифицированный запрос к API Hugging Face.

    Функция создает сессию `curl_cffi` с использованием предоставленных учетных данных
    и отправляет запрос к API Hugging Face для получения ответа от модели.

    Args:
        model (str): Идентификатор модели.
        messages (Messages): Список сообщений для отправки модели.
        auth_result (AuthResult): Результат аутентификации.
        prompt (str, optional): Дополнительный текст подсказки. По умолчанию `None`.
        media (MediaListType, optional): Список медиафайлов для отправки модели. По умолчанию `None`.
        return_conversation (bool, optional): Указывает, следует ли возвращать объект диалога. По умолчанию `False`.
        conversation (Conversation, optional): Объект диалога. По умолчанию `None`.
        web_search (bool, optional): Указывает, следует ли использовать веб-поиск. По умолчанию `False`.
        **kwargs: Дополнительные аргументы.

    Returns:
        AsyncResult: Асинхронный итератор, возвращающий результат запроса.

    Raises:
        MissingRequirementsError: Если не установлен пакет `curl_cffi`.
        MissingAuthError: Если аутентификация не удалась.
        ResponseError: Если произошла ошибка при выполнении запроса.

    Как работает функция:

    1. Проверяет наличие `curl_cffi`.
    2. Получает модель (если model не указана и есть media, использует default_vision_model).
    3. Создает сессию с использованием auth_result.
    4. Если conversation не существует, создает новый conversation и запрашивает conversationId.
    5. Если conversation существует, использует существующий conversationId.
    6. Форматирует запрос в зависимости от conversation.
    7. Настраивает заголовки и данные для запроса.
    8. Отправляет POST-запрос к API.
    9. Обрабатывает ответы (stream, finalAnswer, file, webSearch, title, reasoning).

    ASCII flowchart:

    A: Проверка наличия curl_cffi
    |
    No
    |
    B: Выброс исключения MissingRequirementsError
    |
    End
    Yes
    |
    C: Получение модели
    |
    D: Создание сессии
    |
    E: Проверка наличия conversation
    |
    No
    |
    F: Создание conversation и получение conversationId
    |
    Yes
    |
    G: Использование существующего conversationId
    |
    H: Форматирование запроса
    |
    I: Настройка заголовков и данных
    |
    J: Отправка POST-запроса
    |
    K: Обработка ответов
    |
    End
    """
    ...
```

**Примеры**:

```python
auth_result = AuthResult(cookies={'hf-chat': 'session_id'})
messages = [{'role': 'user', 'content': 'Hello, world!'}]
async for result in HuggingChat.create_authed(model='default', messages=messages, auth_result=auth_result):
    print(result)
```

### `create_conversation`

```python
@classmethod
def create_conversation(cls, session: Session, model: str):
    """
    Создает новый диалог с указанной моделью.

    Функция отправляет POST-запрос к API Hugging Face для создания нового диалога
    с указанной моделью и возвращает идентификатор нового диалога.

    Args:
        session (Session): Сессия `curl_cffi` для выполнения запроса.
        model (str): Идентификатор модели.

    Returns:
        str: Идентификатор нового диалога.

    Raises:
        MissingAuthError: Если аутентификация не удалась.
        ResponseError: Если произошла ошибка при выполнении запроса.

    Как работает функция:

    1. Если модель является image_model, заменяет на default_model.
    2. Подготавливает json_data с указанной моделью.
    3. Отправляет POST-запрос к API /conversation.
    4. Обрабатывает возможные ошибки аутентификации (401) и ошибки запроса (400).
    5. Возвращает conversationId из JSON ответа.

    ASCII flowchart:

    A: Проверка, является ли модель image_model
    |
    Yes
    |
    B: Замена модели на default_model
    |
    No
    |
    C: Подготовка json_data
    |
    D: Отправка POST-запроса
    |
    E: Обработка ошибок (401, 400)
    |
    F: Возврат conversationId

    """
    ...
```

**Примеры**:

```python
session = Session()
conversation_id = HuggingChat.create_conversation(session, 'default')
print(conversation_id)
```

### `fetch_message_id`

```python
@classmethod
def fetch_message_id(cls, session: Session, conversation_id: str):
    """
    Получает идентификатор последнего сообщения в диалоге.

    Функция отправляет GET-запрос к API Hugging Face для получения данных диалога
    и извлекает идентификатор последнего сообщения из полученных данных.

    Args:
        session (Session): Сессия `curl_cffi` для выполнения запроса.
        conversation_id (str): Идентификатор диалога.

    Returns:
        str: Идентификатор последнего сообщения в диалоге.

    Raises:
        RuntimeError: Если не удалось извлечь идентификатор сообщения.
        MissingAuthError: Если аутентификация не удалась.
        ResponseError: Если произошла ошибка при выполнении запроса.

    Как работает функция:

    1. Отправляет GET-запрос к API /conversation/{conversation_id}/__data.json.
    2. Разделяет ответ по newline и пытается распарсить каждую строку как JSON.
    3. Ищет JSON, содержащий "nodes".
    4. Проверяет, является ли последний node ошибкой. Если да, обрабатывает её.
    5. Извлекает message_id из JSON структуры.

    ASCII flowchart:

    A: Отправка GET-запроса
    |
    B: Разделение ответа по newline
    |
    C: Поиск JSON с "nodes"
    |
    D: Проверка последнего node на ошибку
    |
    E: Извлечение message_id
    |
    F: Возврат message_id
    """
    ...
```

**Примеры**:

```python
session = Session()
message_id = HuggingChat.fetch_message_id(session, 'conversation_id')
print(message_id)