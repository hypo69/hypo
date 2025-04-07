# Модуль для работы с DeepSeek API (требуется аутентификация)

## Обзор

Модуль `DeepSeekAPI.py` предназначен для взаимодействия с API DeepSeek, требующим аутентификации. Он предоставляет асинхронный интерфейс для создания и управления чат-сессиями, а также для получения ответов от модели DeepSeek. Модуль использует библиотеку `dsk.api` для взаимодействия с API DeepSeek и поддерживает модели `deepseek-v3` и `deepseek-r1`.

## Подробнее

Этот модуль является частью проекта `hypotez` и обеспечивает интеграцию с DeepSeek API для задач, требующих аутентификации. Он использует асинхронные вызовы для неблокирующей работы и предоставляет удобные методы для аутентификации, создания чат-сессий и получения ответов от модели.

## Классы

### `DeepSeekAPI`

**Описание**: Класс `DeepSeekAPI` является асинхронным провайдером, реализующим взаимодействие с API DeepSeek. Он требует аутентификации и использует `nodriver` для управления сессиями.

**Наследует**:

- `AsyncAuthedProvider`: Обеспечивает базовую функциональность для асинхронных провайдеров, требующих аутентификации.
- `ProviderModelMixin`: Предоставляет функциональность для работы с моделями провайдера.

**Атрибуты**:

- `url` (str): URL для взаимодействия с DeepSeek API (`"https://chat.deepseek.com"`).
- `working` (bool): Флаг, указывающий, работает ли модуль (`has_dsk`).
- `needs_auth` (bool): Флаг, указывающий, требуется ли аутентификация (`True`).
- `use_nodriver` (bool): Флаг, указывающий, используется ли `nodriver` (`True`).
- `_access_token` (str | None): Приватный атрибут для хранения токена доступа.
- `default_model` (str): Модель, используемая по умолчанию (`"deepseek-v3"`).
- `models` (List[str]): Список поддерживаемых моделей (`["deepseek-v3", "deepseek-r1"]`).

**Методы**:

- `on_auth_async(proxy: str = None, **kwargs) -> AsyncIterator`: Асинхронный метод для выполнения аутентификации.
- `create_authed(model: str, messages: Messages, auth_result: AuthResult, conversation: JsonConversation = None, web_search: bool = False, **kwargs) -> AsyncResult`: Асинхронный метод для создания аутентифицированного запроса к API.

### `on_auth_async`

```python
    @classmethod
    async def on_auth_async(cls, proxy: str = None, **kwargs) -> AsyncIterator:
        """Асинхронный метод для выполнения аутентификации.

        Args:
            proxy (str, optional): Прокси-сервер для использования. По умолчанию `None`.
            **kwargs: Дополнительные аргументы.

        Yields:
            RequestLogin: Объект, содержащий URL для логина.
            AuthResult: Объект, содержащий результат аутентификации.
        """
```

**Назначение**: Метод `on_auth_async` выполняет процесс аутентификации для DeepSeek API. Он получает токен доступа из локального хранилища браузера и возвращает его.

**Параметры**:

- `proxy` (str, optional): Прокси-сервер для использования. По умолчанию `None`.
- `**kwargs`: Дополнительные аргументы.

**Возвращает**:

- `AsyncIterator`: Асинхронный итератор, возвращающий объекты `RequestLogin` и `AuthResult`.

**Как работает функция**:

1. Проверяет, инициализирован ли браузер (`cls.browser`). Если нет, то получает экземпляр `nodriver` и функцию для его остановки.
2. Возвращает объект `RequestLogin` с URL для логина, полученным из переменной окружения `G4F_LOGIN_URL` или пустой строки.
3. Определяет асинхронную функцию `callback`, которая периодически проверяет наличие токена доступа в локальном хранилище браузера.
4. Получает аргументы из `nodriver` с помощью `get_args_from_nodriver`, передавая URL, прокси и функцию `callback`.
5. Возвращает объект `AuthResult` с токеном доступа и дополнительными аргументами.

```ascii
    +---------------------+
    |  Проверка browser   |
    +---------------------+
         |
         V
    +---------------------+
    |  Получение browser  |
    +---------------------+
         |
         V
    +---------------------+
    |  RequestLogin       |
    +---------------------+
         |
         V
    +---------------------+
    |  Определение callback|
    +---------------------+
         |
         V
    +---------------------+
    |  get_args_from_nodriver|
    +---------------------+
         |
         V
    +---------------------+
    |  AuthResult         |
    +---------------------+
```

**Примеры**:

```python
# Пример использования метода on_auth_async
async for result in DeepSeekAPI.on_auth_async():
    if isinstance(result, RequestLogin):
        print(f"Login URL: {result.url}")
    elif isinstance(result, AuthResult):
        print(f"API Key: {result.api_key}")
```

### `create_authed`

```python
    @classmethod
    async def create_authed(
        cls,
        model: str,
        messages: Messages,
        auth_result: AuthResult,
        conversation: JsonConversation = None,
        web_search: bool = False,
        **kwargs
    ) -> AsyncResult:
        """Асинхронный метод для создания аутентифицированного запроса к API.

        Args:
            model (str): Модель для использования.
            messages (Messages): Список сообщений для отправки.
            auth_result (AuthResult): Результат аутентификации.
            conversation (JsonConversation, optional): Объект разговора. По умолчанию `None`.
            web_search (bool, optional): Флаг, указывающий, использовать ли веб-поиск. По умолчанию `False`.
            **kwargs: Дополнительные аргументы.

        Yields:
            JsonConversation: Объект разговора.
            Reasoning: Объект, содержащий промежуточные результаты.
            str: Текст ответа.
            FinishReason: Объект, содержащий причину завершения.
        """
```

**Назначение**: Метод `create_authed` создает аутентифицированный запрос к DeepSeek API и получает ответ от модели. Он инициализирует API с использованием токена доступа, создает или использует существующую чат-сессию, и отправляет сообщения для получения ответа.

**Параметры**:

- `model` (str): Модель для использования.
- `messages` (Messages): Список сообщений для отправки.
- `auth_result` (AuthResult): Результат аутентификации.
- `conversation` (JsonConversation, optional): Объект разговора. По умолчанию `None`.
- `web_search` (bool, optional): Флаг, указывающий, использовать ли веб-поиск. По умолчанию `False`.
- `**kwargs`: Дополнительные аргументы.

**Возвращает**:

- `AsyncResult`: Асинхронный итератор, возвращающий объекты `JsonConversation`, `Reasoning`, `str` (текст ответа) и `FinishReason`.

**Как работает функция**:

1. Инициализирует API DeepSeek с использованием токена доступа из `auth_result`.
2. Создает новую чат-сессию, если `conversation` не предоставлен, или использует существующую.
3. Отправляет последнее сообщение пользователя из списка `messages` в API для получения ответа.
4. Итерируется по чанкам ответа, обрабатывая различные типы чанков (`thinking`, `text`, `finish_reason`).
5. Возвращает промежуточные результаты (`Reasoning`), текст ответа (`str`) и причину завершения (`FinishReason`) в виде асинхронного итератора.

```ascii
    +---------------------+
    |  Инициализация API  |
    +---------------------+
         |
         V
    +---------------------+
    |  Создание/использ.  |
    |  чат-сессии         |
    +---------------------+
         |
         V
    +---------------------+
    |  Отправка сообщения |
    +---------------------+
         |
         V
    +---------------------+
    |  Обработка чанков   |
    +---------------------+
         |
         V
    +---------------------+
    |  Возврат результатов|
    +---------------------+
```

**Примеры**:

```python
# Пример использования метода create_authed
auth_result = AuthResult(api_key="your_api_key")
messages = [{"role": "user", "content": "Hello, DeepSeek!"}]
async for result in DeepSeekAPI.create_authed(model="deepseek-v3", messages=messages, auth_result=auth_result):
    if isinstance(result, JsonConversation):
        print(f"Chat ID: {result.chat_id}")
    elif isinstance(result, Reasoning):
        print(f"Reasoning: {result.status} {result.content}")
    elif isinstance(result, str):
        print(f"Response: {result}")
    elif isinstance(result, FinishReason):
        print(f"Finish Reason: {result.finish_reason}")
```