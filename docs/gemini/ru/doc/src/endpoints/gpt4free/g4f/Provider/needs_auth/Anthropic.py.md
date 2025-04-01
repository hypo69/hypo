# Модуль для работы с Anthropic API
## Обзор

Модуль `Anthropic` предоставляет интерфейс для взаимодействия с API Anthropic, включая поддержку текстовых и мультимодальных запросов (изображений). Он наследуется от класса `OpenaiAPI` и реализует методы для получения моделей, создания асинхронных генераторов и управления заголовками запросов.

## Подробнее

Модуль предназначен для интеграции с различными AI-моделями Anthropic. Он поддерживает потоковую передачу данных, системные сообщения и историю сообщений. Модуль также обрабатывает изображения, преобразуя их в формат base64 для отправки в API.

## Классы

### `Anthropic`

**Описание**: Класс для взаимодействия с API Anthropic.

**Наследует**:
- `OpenaiAPI`: Обеспечивает общую логику для работы с API на основе OpenAI.

**Атрибуты**:
- `label` (str): Метка провайдера API ("Anthropic API").
- `url` (str): URL консоли Anthropic ("https://console.anthropic.com").
- `login_url` (str): URL для получения ключей API ("https://console.anthropic.com/settings/keys").
- `working` (bool): Флаг, указывающий, работает ли API (True).
- `api_base` (str): Базовый URL API Anthropic ("https://api.anthropic.com/v1").
- `needs_auth` (bool): Флаг, указывающий, требуется ли аутентификация (True).
- `supports_stream` (bool): Флаг, указывающий, поддерживает ли API потоковую передачу данных (True).
- `supports_system_message` (bool): Флаг, указывающий, поддерживает ли API системные сообщения (True).
- `supports_message_history` (bool): Флаг, указывающий, поддерживает ли API историю сообщений (True).
- `default_model` (str): Модель, используемая по умолчанию ("claude-3-5-sonnet-latest").
- `models` (list[str]): Список поддерживаемых моделей.
- `models_aliases` (dict[str, str]): Словарь псевдонимов моделей.

**Методы**:
- `get_models`: Возвращает список доступных моделей.
- `create_async_generator`: Создает асинхронный генератор для обработки запросов к API.
- `get_headers`: Формирует заголовки для HTTP-запросов.

## Функции

### `get_models`

```python
@classmethod
def get_models(cls, api_key: str = None, **kwargs) -> list[str]:
    """
    Получает список доступных моделей из API Anthropic.

    Args:
        api_key (str, optional): Ключ API для аутентификации. По умолчанию `None`.
        **kwargs: Дополнительные параметры.

    Returns:
        list[str]: Список идентификаторов моделей.

    Raises:
        requests.exceptions.HTTPError: Если HTTP-запрос завершается с ошибкой.

    Example:
        >>> Anthropic.get_models(api_key='YOUR_API_KEY')
        ['claude-3-5-sonnet-latest', 'claude-3-5-sonnet-20241022', ...]
    """
    ...
```

**Назначение**: Получение списка доступных моделей из API Anthropic.

**Параметры**:
- `api_key` (str, optional): Ключ API для аутентификации. По умолчанию `None`.
- `**kwargs`: Дополнительные параметры.

**Возвращает**:
- `list[str]`: Список идентификаторов моделей.

**Вызывает исключения**:
- `requests.exceptions.HTTPError`: Если HTTP-запрос завершается с ошибкой.

**Как работает функция**:

1. **Проверка наличия моделей в кэше**:
   - Проверяется, если список моделей уже кэширован в `cls.models`. Если да, возвращается кэшированный список.
2. **Выполнение HTTP-запроса**:
   - Если список моделей не кэширован, выполняется GET-запрос к API Anthropic для получения списка моделей.
3. **Обработка ответа**:
   - Проверяется статус ответа HTTP-запроса и вызывается исключение в случае ошибки.
   - Извлекаются идентификаторы моделей из JSON-ответа и сохраняются в `cls.models`.
4. **Возврат списка моделей**:
   - Возвращается список идентификаторов моделей.

```ascii
A: Проверка кэша моделей
|
B: Если модели в кэше, возврат из кэша
|
C: HTTP-запрос к API Anthropic
|
D: Проверка статуса HTTP-ответа
|
E: Извлечение идентификаторов моделей из JSON
|
F: Сохранение моделей в кэш
|
G: Возврат списка моделей
```

**Примеры**:

```python
>>> Anthropic.get_models(api_key='YOUR_API_KEY')
['claude-3-5-sonnet-latest', 'claude-3-5-sonnet-20241022', 'claude-3-5-haiku-latest', 'claude-3-5-haiku-20241022', 'claude-3-opus-latest', 'claude-3-opus-20240229', 'claude-3-sonnet-20240229', 'claude-3-haiku-20240307']
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
    Создает асинхронный генератор для запросов к API Anthropic.

    Args:
        model (str): Идентификатор модели для использования.
        messages (Messages): Список сообщений для отправки.
        proxy (str, optional): URL прокси-сервера. По умолчанию `None`.
        timeout (int, optional): Время ожидания запроса в секундах. По умолчанию 120.
        media (MediaListType, optional): Список медиа-файлов для отправки. По умолчанию `None`.
        api_key (str, optional): Ключ API для аутентификации. По умолчанию `None`.
        temperature (float, optional): Температура для генерации текста. По умолчанию `None`.
        max_tokens (int, optional): Максимальное количество токенов в ответе. По умолчанию 4096.
        top_k (int, optional): Параметр top_k для генерации текста. По умолчанию `None`.
        top_p (float, optional): Параметр top_p для генерации текста. По умолчанию `None`.
        stop (list[str], optional): Список стоп-слов. По умолчанию `None`.
        stream (bool, optional): Флаг, указывающий, использовать ли потоковую передачу данных. По умолчанию `False`.
        headers (dict, optional): Дополнительные заголовки для запроса. По умолчанию `None`.
        impersonate (str, optional): Имя пользователя для имитации. По умолчанию `None`.
        tools (Optional[list], optional): Список инструментов для использования. По умолчанию `None`.
        extra_data (dict, optional): Дополнительные данные для запроса. По умолчанию `{}`.
        **kwargs: Дополнительные параметры.

    Returns:
        AsyncResult: Асинхронный генератор для получения ответов от API.

    Raises:
        MissingAuthError: Если отсутствует ключ API.

    Example:
        >>> async for message in Anthropic.create_async_generator(model='claude-3-5-sonnet-latest', messages=[{'role': 'user', 'content': 'Hello'}], api_key='YOUR_API_KEY'):
        ...     print(message)
    """
    ...
```

**Назначение**: Создание асинхронного генератора для обработки запросов к API Anthropic.

**Параметры**:
- `model` (str): Идентификатор модели для использования.
- `messages` (Messages): Список сообщений для отправки.
- `proxy` (str, optional): URL прокси-сервера. По умолчанию `None`.
- `timeout` (int, optional): Время ожидания запроса в секундах. По умолчанию 120.
- `media` (MediaListType, optional): Список медиа-файлов для отправки. По умолчанию `None`.
- `api_key` (str, optional): Ключ API для аутентификации. По умолчанию `None`.
- `temperature` (float, optional): Температура для генерации текста. По умолчанию `None`.
- `max_tokens` (int, optional): Максимальное количество токенов в ответе. По умолчанию 4096.
- `top_k` (int, optional): Параметр top_k для генерации текста. По умолчанию `None`.
- `top_p` (float, optional): Параметр top_p для генерации текста. По умолчанию `None`.
- `stop` (list[str], optional): Список стоп-слов. По умолчанию `None`.
- `stream` (bool, optional): Флаг, указывающий, использовать ли потоковую передачу данных. По умолчанию `False`.
- `headers` (dict, optional): Дополнительные заголовки для запроса. По умолчанию `None`.
- `impersonate` (str, optional): Имя пользователя для имитации. По умолчанию `None`.
- `tools` (Optional[list], optional): Список инструментов для использования. По умолчанию `None`.
- `extra_data` (dict, optional): Дополнительные данные для запроса. По умолчанию `{}`.
- `**kwargs`: Дополнительные параметры.

**Возвращает**:
- `AsyncResult`: Асинхронный генератор для получения ответов от API.

**Вызывает исключения**:
- `MissingAuthError`: Если отсутствует ключ API.

**Как работает функция**:

1. **Проверка аутентификации**:
   - Проверяется наличие `api_key`. Если ключ отсутствует, вызывается исключение `MissingAuthError`.
2. **Обработка медиа-файлов**:
   - Если предоставлены медиа-файлы, они преобразуются в формат base64 и добавляются в сообщение.
3. **Обработка системных сообщений**:
   - Извлекаются системные сообщения и объединяются в одну строку.
4. **Создание сессии**:
   - Создается асинхронная сессия с использованием `StreamSession`.
5. **Подготовка данных для запроса**:
   - Подготавливаются данные для POST-запроса, включая сообщения, модель, параметры генерации и дополнительные данные.
6. **Выполнение POST-запроса**:
   - Выполняется POST-запрос к API Anthropic.
7. **Обработка потокового ответа**:
   - Если `stream` установлен в `True`, ответ обрабатывается построчно.
   - Извлекаются данные из каждой строки и преобразуются в JSON.
   - Генерируются результаты на основе типа данных: текст, использование инструментов, причины остановки.
8. **Обработка не потокового ответа**:
   - Если `stream` установлен в `False`, ответ обрабатывается как JSON.
   - Извлекаются текстовые данные и информация об использовании.
9. **Возврат результатов**:
   - Возвращается асинхронный генератор для получения результатов.

```ascii
A: Проверка аутентификации
|
B: Обработка медиа-файлов
|
C: Обработка системных сообщений
|
D: Создание асинхронной сессии
|
E: Подготовка данных для запроса
|
F: Выполнение POST-запроса
|
G: Обработка потокового ответа?
|  Y: Обработка потокового ответа
|  N: Обработка не потокового ответа
|
H: Генерация результатов
|
I: Возврат асинхронного генератора
```

**Примеры**:

```python
>>> async for message in Anthropic.create_async_generator(model='claude-3-5-sonnet-latest', messages=[{'role': 'user', 'content': 'Hello'}], api_key='YOUR_API_KEY'):
...     print(message)
```

### `get_headers`

```python
@classmethod
def get_headers(cls, stream: bool, api_key: str = None, headers: dict = None) -> dict:
    """
    Формирует заголовки для HTTP-запросов.

    Args:
        stream (bool): Флаг, указывающий, использовать ли потоковую передачу данных.
        api_key (str, optional): Ключ API для аутентификации. По умолчанию `None`.
        headers (dict, optional): Дополнительные заголовки. По умолчанию `None`.

    Returns:
        dict: Словарь заголовков для HTTP-запроса.

    Example:
        >>> Anthropic.get_headers(stream=True, api_key='YOUR_API_KEY')
        {'Accept': 'text/event-stream', 'Content-Type': 'application/json', 'x-api-key': 'YOUR_API_KEY', 'anthropic-version': '2023-06-01'}
    """
    ...
```

**Назначение**: Формирование заголовков для HTTP-запросов к API Anthropic.

**Параметры**:
- `stream` (bool): Флаг, указывающий, использовать ли потоковую передачу данных.
- `api_key` (str, optional): Ключ API для аутентификации. По умолчанию `None`.
- `headers` (dict, optional): Дополнительные заголовки. По умолчанию `None`.

**Возвращает**:
- `dict`: Словарь заголовков для HTTP-запроса.

**Как работает функция**:

1. **Определение `Accept` заголовка**:
   - Устанавливается значение `Accept` в зависимости от того, используется ли потоковая передача данных. Если `stream` равен `True`, то `Accept` устанавливается в `text/event-stream`, иначе в `application/json`.
2. **Включение ключа API**:
   - Если предоставлен `api_key`, он включается в заголовок `x-api-key`.
3. **Добавление версии API**:
   - Добавляется заголовок `anthropic-version` с фиксированным значением `2023-06-01`.
4. **Объединение заголовков**:
   - Объединяются базовые заголовки с дополнительными заголовками, переданными в параметре `headers`.
5. **Возврат словаря заголовков**:
   - Возвращается словарь, содержащий все необходимые заголовки.

```ascii
A: Определение Accept-заголовка
|
B: Включение ключа API (если предоставлен)
|
C: Добавление версии API
|
D: Объединение заголовков
|
E: Возврат словаря заголовков
```

**Примеры**:

```python
>>> Anthropic.get_headers(stream=True, api_key='YOUR_API_KEY')
{'Accept': 'text/event-stream', 'Content-Type': 'application/json', 'x-api-key': 'YOUR_API_KEY', 'anthropic-version': '2023-06-01'}