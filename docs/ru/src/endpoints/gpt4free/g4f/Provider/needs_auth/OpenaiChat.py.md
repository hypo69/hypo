# Модуль OpenaiChat

## Обзор

Модуль `OpenaiChat` предоставляет класс `OpenaiChat`, предназначенный для создания и управления диалогами с сервисом OpenAI ChatGPT. Он поддерживает аутентификацию, загрузку изображений, создание сообщений, взаимодействие с различными моделями (включая GPT-4) и синтез речи.

## Подробнее

Этот модуль является частью проекта `hypotez` и предназначен для интеграции с OpenAI ChatGPT. Он обеспечивает асинхронное взаимодействие с API OpenAI, поддерживая различные функции, такие как загрузка изображений, создание сообщений и синтез речи. Модуль также включает в себя механизмы для аутентификации и обработки ошибок.

## Классы

### `OpenaiChat`

**Описание**: Класс для создания и управления диалогами с сервисом OpenAI ChatGPT.

**Наследует**: `AsyncAuthedProvider`, `ProviderModelMixin`

**Атрибуты**:
- `label` (str): Метка провайдера ("OpenAI ChatGPT").
- `url` (str): URL сервиса ("https://chatgpt.com").
- `working` (bool): Флаг, указывающий на работоспособность (True).
- `use_nodriver` (bool): Флаг, указывающий на использование nodriver (True).
- `supports_gpt_4` (bool): Флаг, указывающий на поддержку GPT-4 (True).
- `supports_message_history` (bool): Флаг, указывающий на поддержку истории сообщений (True).
- `supports_system_message` (bool): Флаг, указывающий на поддержку системных сообщений (True).
- `default_model` (str): Модель по умолчанию (определена в `default_model`).
- `default_image_model` (str): Модель для изображений по умолчанию (определена в `default_image_model`).
- `image_models` (list): Список моделей для изображений (определен в `image_models`).
- `vision_models` (list): Список моделей для работы с изображениями и текстом (определен в `text_models`).
- `models` (list): Список поддерживаемых моделей (определен в `models`).
- `synthesize_content_type` (str): Тип контента для синтеза речи ("audio/aac").
- `request_config` (RequestConfig): Объект конфигурации запросов.
- `_api_key` (str): API-ключ для аутентификации.
- `_headers` (dict): Заголовки запросов.
- `_cookies` (Cookies): Куки для запросов.
- `_expires` (int): Время истечения срока действия API-ключа.

**Методы**:
- `on_auth_async(proxy: str = None, **kwargs) -> AsyncIterator`: Асинхронный метод для аутентификации.
- `upload_images(session: StreamSession, auth_result: AuthResult, media: MediaListType) -> ImageRequest`: Загружает изображение на сервис и получает URL для скачивания.
- `create_messages(messages: Messages, image_requests: ImageRequest = None, system_hints: list = None) -> list`: Создает список сообщений для пользовательского ввода.
- `get_generated_image(session: StreamSession, auth_result: AuthResult, element: dict, prompt: str = None) -> ImageResponse`: Получает сгенерированное изображение.
- `create_authed(model: str, messages: Messages, auth_result: AuthResult, proxy: str = None, timeout: int = 180, auto_continue: bool = False, action: str = "next", conversation: Conversation = None, media: MediaListType = None, return_conversation: bool = False, web_search: bool = False, **kwargs) -> AsyncResult`: Создает асинхронный генератор для диалога.
- `iter_messages_line(cls, session: StreamSession, auth_result: AuthResult, line: bytes, fields: Conversation, sources: Sources) -> AsyncIterator`: Итерирует строки сообщений.
- `synthesize(params: dict) -> AsyncIterator[bytes]`: Синтезирует речь.
- `login(proxy: str = None, api_key: str = None, proof_token: str = None, cookies: Cookies = None, headers: dict = None, **kwargs) -> AsyncIterator`: Выполняет вход в систему.
- `nodriver_auth(proxy: str = None)`: Аутентификация с использованием nodriver.
- `get_default_headers() -> Dict[str, str]`: Возвращает заголовки по умолчанию.
- `_create_request_args(cookies: Cookies = None, headers: dict = None, user_agent: str = None)`: Создает аргументы запроса.
- `_update_request_args(auth_result: AuthResult, session: StreamSession)`: Обновляет аргументы запроса.
- `_set_api_key(api_key: str) -> bool`: Устанавливает API-ключ.
- `_update_cookie_header()`: Обновляет заголовок cookie.

#### `OpenaiChat.on_auth_async`

```python
@classmethod
async def on_auth_async(cls, proxy: str = None, **kwargs) -> AsyncIterator:
    """
    Асинхронный метод для аутентификации.

    Args:
        proxy (str, optional): Прокси для использования. По умолчанию `None`.
        **kwargs: Дополнительные аргументы.

    Yields:
        AsyncIterator: Асинхронный итератор результатов аутентификации.
    """
```

**Как работает функция**:
1. Выполняет вход в систему, используя метод `login`.
2. Возвращает результаты аутентификации, включая API-ключ, куки, заголовки и токены.

```
    login
    ↓
    AuthResult
```

#### `OpenaiChat.upload_images`

```python
@classmethod
async def upload_images(
    cls,
    session: StreamSession,
    auth_result: AuthResult,
    media: MediaListType,
) -> ImageRequest:
    """
    Загружает изображение на сервис и получает URL для скачивания.

    Args:
        session (StreamSession): Объект StreamSession для выполнения запросов.
        auth_result (AuthResult): Результаты аутентификации.
        media (MediaListType): Изображения для загрузки (PIL Image или bytes).

    Returns:
        ImageRequest: Объект ImageRequest с URL для скачивания, именем файла и другими данными.
    """
```

**Как работает функция**:
1. Преобразует изображение в формат bytes и PIL Image.
2. Отправляет данные изображения на сервис для получения информации о загрузке.
3. Загружает изображение по полученному URL.
4. Получает URL для скачивания загруженного изображения.

```
    Преобразование изображения
    ↓
    Отправка данных изображения
    ↓
    Загрузка изображения
    ↓
    Получение URL для скачивания
```

#### `OpenaiChat.create_messages`

```python
@classmethod
def create_messages(cls, messages: Messages, image_requests: ImageRequest = None, system_hints: list = None) -> list:
    """
    Создает список сообщений для пользовательского ввода.

    Args:
        messages (Messages): Список предыдущих сообщений.
        image_requests (ImageRequest, optional): Объекты ImageRequest с информацией об изображениях. По умолчанию `None`.
        system_hints (list, optional): Системные подсказки. По умолчанию `None`.

    Returns:
        list: Список сообщений с пользовательским вводом и изображениями (если есть).
    """
```

**Как работает функция**:
1. Формирует структуру сообщений для отправки в API OpenAI.
2. Добавляет информацию об изображениях (если есть) в структуру сообщений.

```
    Формирование структуры сообщений
    ↓
    Добавление информации об изображениях
```

#### `OpenaiChat.get_generated_image`

```python
@classmethod
async def get_generated_image(cls, session: StreamSession, auth_result: AuthResult, element: dict, prompt: str = None) -> ImageResponse:
    """
    Получает сгенерированное изображение.

    Args:
        session (StreamSession): Объект StreamSession для выполнения запросов.
        auth_result (AuthResult): Результаты аутентификации.
        element (dict): Элемент с информацией об изображении.
        prompt (str, optional): Промпт для генерации изображения. По умолчанию `None`.

    Returns:
        ImageResponse: Объект ImageResponse с URL для скачивания изображения и промптом.
    """
```

**Как работает функция**:
1. Извлекает ID файла изображения из элемента `element`.
2. Получает URL для скачивания изображения по ID файла.

```
    Извлечение ID файла изображения
    ↓
    Получение URL для скачивания
```

#### `OpenaiChat.create_authed`

```python
@classmethod
async def create_authed(
    cls,
    model: str,
    messages: Messages,
    auth_result: AuthResult,
    proxy: str = None,
    timeout: int = 180,
    auto_continue: bool = False,
    action: str = "next",
    conversation: Conversation = None,
    media: MediaListType = None,
    return_conversation: bool = False,
    web_search: bool = False,
    **kwargs
) -> AsyncResult:
    """
    Создает асинхронный генератор для диалога.

    Args:
        model (str): Имя модели.
        messages (Messages): Список предыдущих сообщений.
        auth_result (AuthResult): Результаты аутентификации.
        proxy (str, optional): Прокси для использования. По умолчанию `None`.
        timeout (int, optional): Время ожидания запроса. По умолчанию 180.
        auto_continue (bool, optional): Флаг автоматического продолжения диалога. По умолчанию `False`.
        action (str, optional): Тип действия ("next", "continue", "variant"). По умолчанию "next".
        conversation (Conversation, optional): Объект Conversation с информацией о диалоге. По умолчанию `None`.
        media (MediaListType, optional): Изображения для включения в диалог. По умолчанию `None`.
        return_conversation (bool, optional): Флаг возврата объекта Conversation в результате. По умолчанию `False`.
        web_search (bool, optional): Флаг использования веб-поиска. По умолчанию `False`.
        **kwargs: Дополнительные аргументы.

    Yields:
        AsyncResult: Асинхронные результаты из генератора.
    """
```

**Как работает функция**:
1. Инициализирует сессию StreamSession для выполнения запросов.
2. Загружает изображения (если есть) с использованием метода `upload_images`.
3. Формирует данные запроса для отправки в API OpenAI.
4. Отправляет запрос и обрабатывает ответы, используя метод `iter_messages_line`.
5. Возвращает результаты в виде асинхронного генератора.

```
    Инициализация сессии
    ↓
    Загрузка изображений
    ↓
    Формирование данных запроса
    ↓
    Отправка запроса и обработка ответов
    ↓
    Возврат результатов
```

#### `OpenaiChat.iter_messages_line`

```python
@classmethod
async def iter_messages_line(cls, session: StreamSession, auth_result: AuthResult, line: bytes, fields: Conversation, sources: Sources) -> AsyncIterator:
    """
    Итерирует строки сообщений.

    Args:
        session (StreamSession): Объект StreamSession для выполнения запросов.
        auth_result (AuthResult): Результаты аутентификации.
        line (bytes): Строка сообщения.
        fields (Conversation): Объект Conversation с информацией о диалоге.
        sources (Sources): Объект Sources для хранения информации об источниках.

    Yields:
        AsyncIterator: Асинхронный итератор сообщений.
    """
```

**Как работает функция**:
1. Обрабатывает строку сообщения, извлекая информацию о тексте, изображениях и источниках.
2. Обновляет объект Conversation с информацией о диалоге.
3. Возвращает результаты в виде асинхронного итератора.

```
    Обработка строки сообщения
    ↓
    Извлечение информации
    ↓
    Обновление объекта Conversation
    ↓
    Возврат результатов
```

#### `OpenaiChat.synthesize`

```python
@classmethod
async def synthesize(cls, params: dict) -> AsyncIterator[bytes]:
    """
    Синтезирует речь.

    Args:
        params (dict): Параметры для синтеза речи.

    Yields:
        AsyncIterator[bytes]: Асинхронный итератор байтов синтезированной речи.
    """
```

**Как работает функция**:
1. Выполняет вход в систему, используя метод `login`.
2. Отправляет запрос на синтез речи в API OpenAI.
3. Возвращает байты синтезированной речи в виде асинхронного итератора.

```
    Выполнение входа
    ↓
    Отправка запроса на синтез речи
    ↓
    Возврат байтов синтезированной речи
```

#### `OpenaiChat.login`

```python
@classmethod
async def login(
    cls,
    proxy: str = None,
    api_key: str = None,
    proof_token: str = None,
    cookies: Cookies = None,
    headers: dict = None,
    **kwargs
) -> AsyncIterator:
    """
    Выполняет вход в систему.

    Args:
        proxy (str, optional): Прокси для использования. По умолчанию `None`.
        api_key (str, optional): API-ключ для аутентификации. По умолчанию `None`.
        proof_token (str, optional): Токен подтверждения. По умолчанию `None`.
        cookies (Cookies, optional): Куки для аутентификации. По умолчанию `None`.
        headers (dict, optional): Заголовки для аутентификации. По умолчанию `None`.
        **kwargs: Дополнительные аргументы.

    Yields:
        AsyncIterator: Асинхронный итератор результатов входа.
    """
```

**Как работает функция**:
1. Проверяет срок действия API-ключа.
2. Обновляет заголовки и куки.
3. Выполняет аутентификацию с использованием API-ключа, куки или nodriver.
4. Возвращает результаты в виде асинхронного итератора.

```
    Проверка срока действия API-ключа
    ↓
    Обновление заголовков и куки
    ↓
    Выполнение аутентификации
    ↓
    Возврат результатов
```

#### `OpenaiChat.nodriver_auth`

```python
@classmethod
async def nodriver_auth(cls, proxy: str = None):
    """
    Аутентификация с использованием nodriver.

    Args:
        proxy (str, optional): Прокси для использования. По умолчанию `None`.
    """
```

**Как работает функция**:
1. Запускает браузер с использованием nodriver.
2. Перехватывает запросы для получения API-ключа, токенов и куки.
3. Обновляет конфигурацию запроса с полученными данными.

```
    Запуск браузера
    ↓
    Перехват запросов
    ↓
    Обновление конфигурации запроса
```

#### `OpenaiChat.get_default_headers`

```python
@staticmethod
def get_default_headers() -> Dict[str, str]:
    """
    Возвращает заголовки по умолчанию.

    Returns:
        Dict[str, str]: Словарь заголовков по умолчанию.
    """
```

**Как работает функция**:
1. Возвращает словарь, содержащий заголовки по умолчанию.

#### `OpenaiChat._create_request_args`

```python
@classmethod
def _create_request_args(cls, cookies: Cookies = None, headers: dict = None, user_agent: str = None):
    """
    Создает аргументы запроса.

    Args:
        cookies (Cookies, optional): Куки для запроса. По умолчанию `None`.
        headers (dict, optional): Заголовки для запроса. По умолчанию `None`.
        user_agent (str, optional): User-agent для запроса. По умолчанию `None`.
    """
```

**Как работает функция**:
1. Устанавливает заголовки и куки для запроса.
2. Обновляет заголовок cookie.

#### `OpenaiChat._update_request_args`

```python
@classmethod
def _update_request_args(cls, auth_result: AuthResult, session: StreamSession):
    """
    Обновляет аргументы запроса.

    Args:
        auth_result (AuthResult): Результаты аутентификации.
        session (StreamSession): Объект StreamSession для выполнения запросов.
    """
```

**Как работает функция**:
1. Обновляет куки из сессии StreamSession.
2. Обновляет заголовок cookie.

#### `OpenaiChat._set_api_key`

```python
@classmethod
def _set_api_key(cls, api_key: str) -> bool:
    """
    Устанавливает API-ключ.

    Args:
        api_key (str): API-ключ.

    Returns:
        bool: `True`, если API-ключ установлен успешно, `False` в противном случае.
    """
```

**Как работает функция**:
1. Декодирует API-ключ для получения времени истечения срока действия.
2. Проверяет срок действия API-ключа.
3. Устанавливает API-ключ в заголовках запроса.

#### `OpenaiChat._update_cookie_header`

```python
@classmethod
def _update_cookie_header(cls):
    """
    Обновляет заголовок cookie.
    """
```

**Как работает функция**:
1. Формирует строку cookie из словаря куки.
2. Устанавливает строку cookie в заголовках запроса.

### `Conversation`

**Описание**: Класс для инкапсуляции полей ответа.

**Наследует**: `JsonConversation`

**Атрибуты**:
- `conversation_id` (str): ID диалога.
- `message_id` (str): ID сообщения.
- `finish_reason` (str): Причина завершения диалога.
- `is_recipient` (bool): Флаг, указывающий на то, является ли сообщение предназначенным для получателя.
- `parent_message_id` (str): ID родительского сообщения.
- `user_id` (str): ID пользователя.
- `is_thinking` (bool): Флаг, указывающий на то, что диалог находится в состоянии "размышления".

## Функции

### `get_cookies`

```python
def get_cookies(
    urls: Optional[Iterator[str]] = None
) -> Generator[Dict, Dict, Dict[str, str]]:
    """
    Получает куки для указанных URL.

    Args:
        urls (Optional[Iterator[str]], optional): Итератор URL. По умолчанию `None`.

    Yields:
        Generator[Dict, Dict, Dict[str, str]]: Генератор словарей куки.
    """
```

**Как работает функция**:
1. Формирует команду для получения куки.
2. Возвращает словарь куки.

```
    Формирование команды
    ↓
    Возврат словаря куки
```