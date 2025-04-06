# Модуль Anthropic

## Обзор

Модуль `Anthropic` предоставляет интерфейс для взаимодействия с API Anthropic, включая поддержку стриминга, системных сообщений и истории сообщений. Этот модуль является частью проекта `hypotez` и предназначен для работы с различными моделями Anthropic, такими как Claude.

## Подробней

Модуль определяет класс `Anthropic`, который наследуется от класса `OpenaiAPI`. Он содержит методы для получения списка доступных моделей, создания асинхронного генератора для взаимодействия с API, а также для формирования заголовков запросов. Модуль поддерживает работу с изображениями и инструментами (tools).

## Классы

### `Anthropic`

**Описание**: Класс для взаимодействия с API Anthropic.

**Наследует**:
- `OpenaiAPI`: Этот класс расширяет возможности `OpenaiAPI` для работы с Anthropic API.

**Атрибуты**:
- `label` (str): Метка провайдера API ("Anthropic API").
- `url` (str): URL консоли Anthropic ("https://console.anthropic.com").
- `login_url` (str): URL для входа в Anthropic ("https://console.anthropic.com/settings/keys").
- `working` (bool): Флаг, указывающий на работоспособность API (True).
- `api_base` (str): Базовый URL API Anthropic ("https://api.anthropic.com/v1").
- `needs_auth` (bool): Флаг, указывающий на необходимость аутентификации (True).
- `supports_stream` (bool): Флаг, указывающий на поддержку стриминга (True).
- `supports_system_message` (bool): Флаг, указывающий на поддержку системных сообщений (True).
- `supports_message_history` (bool): Флаг, указывающий на поддержку истории сообщений (True).
- `default_model` (str): Модель, используемая по умолчанию ("claude-3-5-sonnet-latest").
- `models` (list): Список поддерживаемых моделей.
- `models_aliases` (dict): Словарь с псевдонимами моделей.

**Методы**:
- `get_models()`: Получает список доступных моделей.
- `create_async_generator()`: Создает асинхронный генератор для взаимодействия с API.
- `get_headers()`: Формирует заголовки запроса.

## Функции

### `get_models`

```python
@classmethod
def get_models(cls, api_key: str = None, **kwargs) -> list:
    """
    Получает список доступных моделей Anthropic.

    Args:
        api_key (str, optional): API ключ для аутентификации. По умолчанию `None`.
        **kwargs: Дополнительные аргументы.

    Returns:
        list: Список идентификаторов доступных моделей.

    Raises:
        requests.exceptions.HTTPError: Если HTTP запрос завершается с ошибкой.

    Как работает функция:
    1. Проверяет, если список моделей (`cls.models`) уже заполнен. Если да, то возвращает его.
    2. Если список моделей пуст, формирует URL для запроса списка моделей у API Anthropic.
    3. Выполняет GET запрос к API Anthropic для получения списка моделей.
    4. Проверяет статус ответа и вызывает исключение `HTTPError` в случае ошибки.
    5. Извлекает идентификаторы моделей из JSON ответа и сохраняет их в `cls.models`.
    6. Возвращает список идентификаторов моделей.
    """
```

```ascii
Проверка списка моделей (cls.models)
    │
    ├──→  Список моделей заполнен?
    │       ├──→ Да: Возврат списка моделей
    │       └──→ Нет: Формирование URL
    │            │
    │            └──→ GET запрос к API Anthropic
    │                 │
    │                 └──→ Проверка статуса ответа
    │                      │
    │                      ├──→ Ошибка: Вызов исключения HTTPError
    │                      └──→ Успех: Извлечение идентификаторов моделей
    │                           │
    │                           └──→ Сохранение моделей в cls.models
    │                                │
    │                                └──→ Возврат списка моделей
    │
    └─────────────────────────────────────────────────────────────
```

**Примеры**:

```python
# Пример вызова функции
models = Anthropic.get_models(api_key='your_api_key')
print(models)
```

### `create_async_generator`

```python
@classmethod
async def create_async_generator(
    cls,
    model: str,
    messages: Messages,
    proxy: str = None,
    timeout: int = 120,
    media: MediaListType = None,
    api_key: str = None,
    temperature: float = None,
    max_tokens: int = 4096,
    top_k: int = None,
    top_p: float = None,
    stop: list[str] = None,
    stream: bool = False,
    headers: dict = None,
    impersonate: str = None,
    tools: Optional[list] = None,
    extra_data: dict = {},
    **kwargs
) -> AsyncResult:
    """
    Создает асинхронный генератор для взаимодействия с API Anthropic.

    Args:
        model (str): Имя используемой модели.
        messages (Messages): Список сообщений для отправки.
        proxy (str, optional): URL прокси-сервера. По умолчанию `None`.
        timeout (int, optional): Время ожидания запроса в секундах. По умолчанию 120.
        media (MediaListType, optional): Список медиафайлов для отправки. По умолчанию `None`.
        api_key (str, optional): API ключ для аутентификации. По умолчанию `None`.
        temperature (float, optional): Температура модели. По умолчанию `None`.
        max_tokens (int, optional): Максимальное количество токенов в ответе. По умолчанию 4096.
        top_k (int, optional): Параметр top_k. По умолчанию `None`.
        top_p (float, optional): Параметр top_p. По умолчанию `None`.
        stop (list[str], optional): Список стоп-последовательностей. По умолчанию `None`.
        stream (bool, optional): Флаг, указывающий на использование стриминга. По умолчанию `False`.
        headers (dict, optional): Дополнительные заголовки запроса. По умолчанию `None`.
        impersonate (str, optional): Имя пользователя для имитации. По умолчанию `None`.
        tools (Optional[list], optional): Список инструментов для использования. По умолчанию `None`.
        extra_data (dict, optional): Дополнительные данные для запроса. По умолчанию `{}`.
        **kwargs: Дополнительные аргументы.

    Returns:
        AsyncResult: Асинхронный генератор для получения ответов от API.

    Raises:
        MissingAuthError: Если отсутствует API ключ.

    Как работает функция:
    1. Проверяет наличие API ключа. Если ключ отсутствует, вызывает исключение `MissingAuthError`.
    2. Обрабатывает медиафайлы (изображения), кодирует их в base64 и вставляет в сообщения.
    3. Извлекает системные сообщения и удаляет их из основного списка сообщений.
    4. Создает асинхронную сессию для выполнения запросов к API Anthropic.
    5. Формирует данные запроса, включая сообщения, модель, параметры температуры, максимальное количество токенов и т.д.
    6. Выполняет POST запрос к API Anthropic.
    7. Обрабатывает ответ в зависимости от того, используется ли стриминг.
    8. Если стриминг не используется, извлекает текст ответа и возвращает его.
    9. Если стриминг используется, обрабатывает чанки данных, извлекает текст и возвращает его в виде генератора.
    """
```

```ascii
Проверка наличия API ключа
    │
    ├──→  API ключ отсутствует?
    │       ├──→ Да: Вызов исключения MissingAuthError
    │       └──→ Нет: Обработка медиафайлов
    │            │
    │            └──→ Извлечение системных сообщений
    │                 │
    │                 └──→ Создание асинхронной сессии
    │                      │
    │                      └──→ Формирование данных запроса
    │                           │
    │                           └──→ POST запрос к API Anthropic
    │                                │
    │                                └──→ Обработка ответа (стриминг?)
    │                                     │
    │                                     ├──→ Нет: Извлечение текста ответа
    │                                     │    │
    │                                     │    └──→ Возврат текста ответа
    │                                     │
    │                                     └──→ Да: Обработка чанков данных
    │                                          │
    │                                          └──→ Извлечение текста и возврат в виде генератора
    │
    └──────────────────────────────────────────────────────────────────
```

**Примеры**:

```python
# Пример вызова функции
messages = [{"role": "user", "content": "Hello, how are you?"}]
async for response in Anthropic.create_async_generator(model='claude-3-opus-latest', messages=messages, api_key='your_api_key'):
    print(response)
```

### `get_headers`

```python
@classmethod
def get_headers(cls, stream: bool, api_key: str = None, headers: dict = None) -> dict:
    """
    Формирует заголовки запроса для API Anthropic.

    Args:
        stream (bool): Флаг, указывающий на использование стриминга.
        api_key (str, optional): API ключ для аутентификации. По умолчанию `None`.
        headers (dict, optional): Дополнительные заголовки. По умолчанию `None`.

    Returns:
        dict: Словарь с заголовками запроса.

    Как работает функция:
    1. Определяет тип Accept в зависимости от того, используется ли стриминг.
    2. Добавляет заголовок Content-Type.
    3. Добавляет заголовок x-api-key, если предоставлен API ключ.
    4. Добавляет заголовок anthropic-version.
    5. Объединяет все заголовки в один словарь и возвращает его.
    """
```

```ascii
Определение типа Accept (стриминг?)
    │
    ├──→  Стриминг используется?
    │       ├──→ Да: Accept = text/event-stream
    │       └──→ Нет: Accept = application/json
    │
    └──→ Добавление Content-Type
         │
         └──→ Добавление x-api-key (если есть)
              │
              └──→ Добавление anthropic-version
                   │
                   └──→ Объединение заголовков и возврат
```

**Примеры**:

```python
# Пример вызова функции
headers = Anthropic.get_headers(stream=True, api_key='your_api_key')
print(headers)