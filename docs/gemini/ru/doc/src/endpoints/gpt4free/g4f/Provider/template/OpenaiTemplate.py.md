# Модуль OpenaiTemplate

## Обзор

Модуль `OpenaiTemplate` предоставляет базовый класс для взаимодействия с API OpenAI. Он включает в себя функциональность для получения списка моделей, создания асинхронного генератора для обработки запросов к API и обработки ответов, включая потоковую передачу данных. Модуль поддерживает как текстовые запросы, так и запросы на генерацию изображений.

## Подробнее

Модуль предназначен для упрощения интеграции с OpenAI API. Он предоставляет удобные методы для аутентификации, формирования запросов и обработки ответов. Класс `OpenaiTemplate` является абстрактным и должен быть унаследован для реализации конкретных провайдеров OpenAI.

## Классы

### `OpenaiTemplate`

**Описание**: Базовый класс для взаимодействия с API OpenAI.

**Принцип работы**:

Класс `OpenaiTemplate` предоставляет следующие возможности:

-   Аутентификация с использованием API-ключа.
-   Получение списка доступных моделей.
-   Создание асинхронного генератора для отправки запросов и получения ответов в потоковом режиме.
-   Поддержка текстовых и графических запросов.
-   Обработка ошибок и исключений.

**Наследует**:

-   `AsyncGeneratorProvider`: Обеспечивает асинхронную генерацию данных.
-   `ProviderModelMixin`: Предоставляет функциональность для работы с моделями.
-   `RaiseErrorMixin`: Обеспечивает обработку ошибок.

**Атрибуты**:

-   `api_base` (str): Базовый URL API OpenAI.
-   `api_key` (str | None): API-ключ для аутентификации.
-   `api_endpoint` (str | None): URL конечной точки API.
-   `supports_message_history` (bool): Поддержка истории сообщений.
-   `supports_system_message` (bool): Поддержка системных сообщений.
-   `default_model` (str): Модель, используемая по умолчанию.
-   `fallback_models` (list[str]): Список моделей для переключения в случае ошибки.
-   `sort_models` (bool): Флаг, указывающий, нужно ли сортировать список моделей.
-   `ssl` (bool | None): Параметр, определяющий необходимость использования SSL.

**Методы**:

-   `get_models(api_key: str = None, api_base: str = None) -> list[str]`: Возвращает список доступных моделей.
-   `create_async_generator(...) -> AsyncResult`: Создает асинхронный генератор для выполнения запросов к API.
-   `get_headers(stream: bool, api_key: str = None, headers: dict = None) -> dict`: Формирует заголовки запроса.

### `get_models`

```python
@classmethod
def get_models(cls, api_key: str = None, api_base: str = None) -> list[str]:
    """
    Возвращает список доступных моделей.

    Args:
        api_key (str, optional): API-ключ для аутентификации. Defaults to None.
        api_base (str, optional): Базовый URL API. Defaults to None.

    Returns:
        list[str]: Список идентификаторов моделей.
    """
    ...
```

**Назначение**: Получение списка доступных моделей из API OpenAI.

**Параметры**:

-   `api_key` (str, optional): API-ключ для аутентификации. Если не указан, используется `cls.api_key`. По умолчанию `None`.
-   `api_base` (str, optional): Базовый URL API. Если не указан, используется `cls.api_base`. По умолчанию `None`.

**Возвращает**:

-   `list[str]`: Список идентификаторов моделей. Если произошла ошибка, возвращается `cls.fallback_models`.

**Вызывает исключения**:

-   `Exception`: В случае ошибки при выполнении HTTP-запроса.

**Как работает функция**:

1.  Проверяет, был ли уже получен список моделей (`cls.models`). Если да, возвращает его.
2.  Если список моделей не был получен, выполняет HTTP-запрос к API OpenAI для получения списка моделей.
3.  Формирует заголовок `Authorization` с API-ключом, если он предоставлен.
4.  Выполняет GET-запрос к конечной точке `/models` API OpenAI.
5.  Обрабатывает ответ, извлекая идентификаторы моделей из JSON-данных.
6.  Сохраняет список моделей в `cls.models` и список моделей изображений в `cls.image_models`.
7.  В случае ошибки логирует ее и возвращает `cls.fallback_models`.

**ASCII flowchart**:

```
A: Проверка наличия cls.models
|
B: HTTP GET запрос к API OpenAI (/models)
|
C: Обработка ответа API
|
D: Извлечение идентификаторов моделей
|
E: Сохранение списка моделей в cls.models
|
F: Возврат списка моделей
```

**Примеры**:

```python
# Пример получения списка моделей без указания api_key и api_base (используются значения по умолчанию)
models = OpenaiTemplate.get_models()

# Пример получения списка моделей с указанием api_key и api_base
models = OpenaiTemplate.get_models(api_key="YOUR_API_KEY", api_base="https://api.openai.com/v1")
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
    api_endpoint: str = None,
    api_base: str = None,
    temperature: float = None,
    max_tokens: int = None,
    top_p: float = None,
    stop: Union[str, list[str]] = None,
    stream: bool = False,
    prompt: str = None,
    headers: dict = None,
    impersonate: str = None,
    extra_parameters: list[str] = ["tools", "parallel_tool_calls", "tool_choice", "reasoning_effort", "logit_bias", "modalities", "audio"],
    extra_data: dict = {},
    **kwargs
) -> AsyncResult:
    """
    Создает асинхронный генератор для выполнения запросов к API OpenAI.

    Args:
        model (str): Идентификатор модели.
        messages (Messages): Список сообщений для отправки.
        proxy (str, optional): URL прокси-сервера. Defaults to None.
        timeout (int, optional): Время ожидания ответа в секундах. Defaults to 120.
        media (MediaListType, optional): Список медиафайлов для отправки. Defaults to None.
        api_key (str, optional): API-ключ для аутентификации. Defaults to None.
        api_endpoint (str, optional): URL конечной точки API. Defaults to None.
        api_base (str, optional): Базовый URL API. Defaults to None.
        temperature (float, optional): Температура модели. Defaults to None.
        max_tokens (int, optional): Максимальное количество токенов в ответе. Defaults to None.
        top_p (float, optional): Top P sampling. Defaults to None.
        stop (Union[str, list[str]], optional): Список стоп-слов. Defaults to None.
        stream (bool, optional): Флаг, указывающий, нужно ли использовать потоковую передачу данных. Defaults to False.
        prompt (str, optional): Дополнительный промпт. Defaults to None.
        headers (dict, optional): Дополнительные заголовки запроса. Defaults to None.
        impersonate (str, optional): Пользователь для имитации. Defaults to None.
        extra_parameters (list[str], optional): Список дополнительных параметров, которые будут переданы в запрос.
        extra_data (dict, optional): Словарь дополнительных данных, которые будут переданы в запрос.
        **kwargs: Дополнительные параметры.

    Returns:
        AsyncResult: Асинхронный генератор, возвращающий ответы от API.

    Raises:
        MissingAuthError: Если не указан API-ключ и требуется аутентификация.
        ResponseError: Если получен неподдерживаемый Content-Type.
    """
    ...
```

**Назначение**: Создание асинхронного генератора для взаимодействия с API OpenAI.

**Параметры**:

-   `model` (str): Идентификатор модели, которую следует использовать.
-   `messages` (Messages): Список сообщений, отправляемых в API.
-   `proxy` (str, optional): URL прокси-сервера для использования. По умолчанию `None`.
-   `timeout` (int, optional): Максимальное время ожидания ответа от API в секундах. По умолчанию 120.
-   `media` (MediaListType, optional): Список медиафайлов, связанных с сообщением. По умолчанию `None`.
-   `api_key` (str, optional): API-ключ для аутентификации. Если не указан, используется `cls.api_key`. По умолчанию `None`.
-   `api_endpoint` (str, optional): URL конечной точки API. Если не указан, используется `cls.api_endpoint`. По умолчанию `None`.
-   `api_base` (str, optional): Базовый URL API. Если не указан, используется `cls.api_base`. По умолчанию `None`.
-   `temperature` (float, optional): Температура для управления случайностью ответов. По умолчанию `None`.
-   `max_tokens` (int, optional): Максимальное количество токенов в ответе. По умолчанию `None`.
-   `top_p` (float, optional): Значение Top P для дискретизации. По умолчанию `None`.
-   `stop` (Union[str, list[str]], optional): Список строк, при обнаружении которых генерация должна остановиться. По умолчанию `None`.
-   `stream` (bool, optional): Флаг, определяющий, использовать ли потоковую передачу данных. По умолчанию `False`.
-   `prompt` (str, optional): Дополнительный промпт для API. По умолчанию `None`.
-   `headers` (dict, optional): Дополнительные HTTP-заголовки для запроса. По умолчанию `None`.
-   `impersonate` (str, optional): Пользователь для имитации. По умолчанию `None`.
-   `extra_parameters` (list[str], optional): Список дополнительных параметров, передаваемых в API. По умолчанию `["tools", "parallel_tool_calls", "tool_choice", "reasoning_effort", "logit_bias", "modalities", "audio"]`.
-   `extra_data` (dict, optional): Дополнительные данные для включения в запрос. По умолчанию `{}`.
-   `**kwargs`: Дополнительные параметры, передаваемые в API.

**Возвращает**:

-   `AsyncResult`: Асинхронный генератор, который выдает ответы от API. Это может быть текстовое содержимое, вызовы инструментов (`ToolCalls`), информация об использовании (`Usage`), причина завершения (`FinishReason`) или ответ с изображением (`ImageResponse`).

**Вызывает исключения**:

-   `MissingAuthError`: Если для провайдера требуется аутентификация, но `api_key` не предоставлен.
-   `ResponseError`: Если API возвращает неподдерживаемый тип контента.

**Как работает функция**:

1.  Проверяет и использует `api_key` из аргументов или атрибута класса.
2.  Вызывает `MissingAuthError`, если требуется аутентификация, но `api_key` не предоставлен.
3.  Создает асинхронную сессию с использованием `StreamSession` для выполнения HTTP-запросов.
4.  Определяет `model` и `api_base` из аргументов или атрибутов класса.
5.  Если `model` является моделью для генерации изображений, формирует запрос к конечной точке `/images/generations` и возвращает `ImageResponse`.
6.  Формирует полезную нагрузку (`data`) для запроса, включая сообщения, модель, параметры температуры, максимальное количество токенов и другие параметры.
7.  Определяет `api_endpoint` из аргументов или атрибутов класса и выполняет POST-запрос к API.
8.  Обрабатывает ответ в зависимости от типа контента:
    -   Если тип контента `application/json`, извлекает и возвращает текстовое содержимое, `ToolCalls`, `Usage` и `FinishReason`.
    -   Если тип контента `text/event-stream`, обрабатывает потоковые события SSE и возвращает дельты содержимого, `Usage` и `FinishReason`.
9.  Вызывает `ResponseError`, если получен неподдерживаемый тип контента.

**ASCII flowchart**:

```
A: Проверка api_key
|
B: Создание StreamSession
|
C: Определение model и api_base
|
D: Проверка, является ли модель моделью для генерации изображений
|   |
D1: Да -> HTTP POST запрос к /images/generations -> ImageResponse
|   |
D2: Нет -> Формирование полезной нагрузки (data)
|
E: Определение api_endpoint и выполнение HTTP POST запроса
|
F: Обработка ответа в зависимости от типа контента
|   |
F1: application/json -> извлечение и возврат данных
|   |
F2: text/event-stream -> обработка потоковых событий SSE и возврат данных
|   |
F3: другой -> ResponseError
```

**Примеры**:

```python
# Пример создания асинхронного генератора для текстового запроса
messages = [{"role": "user", "content": "Hello, how are you?"}]
generator = OpenaiTemplate.create_async_generator(model="gpt-3.5-turbo", messages=messages)

# Пример создания асинхронного генератора для запроса изображения
messages = [{"role": "user", "content": "A cat wearing a hat"}]
generator = OpenaiTemplate.create_async_generator(model="dall-e-3", messages=messages)
```

### `get_headers`

```python
@classmethod
def get_headers(cls, stream: bool, api_key: str = None, headers: dict = None) -> dict:
    """
    Формирует заголовки запроса.

    Args:
        stream (bool): Флаг, указывающий, нужно ли использовать потоковую передачу данных.
        api_key (str, optional): API-ключ для аутентификации. Defaults to None.
        headers (dict, optional): Дополнительные заголовки запроса. Defaults to None.

    Returns:
        dict: Словарь заголовков запроса.
    """
    ...
```

**Назначение**: Формирование заголовков HTTP-запроса для API OpenAI.

**Параметры**:

-   `stream` (bool): Указывает, используется ли потоковая передача данных. Если `True`, заголовок `Accept` устанавливается в `text/event-stream`.
-   `api_key` (str, optional): API-ключ для аутентификации. По умолчанию `None`.
-   `headers` (dict, optional): Дополнительные заголовки, которые нужно включить в запрос. По умолчанию `None`.

**Возвращает**:

-   `dict`: Словарь, содержащий заголовки для HTTP-запроса.

**Как работает функция**:

1.  Определяет значение заголовка `Accept` в зависимости от параметра `stream`. Если `stream` равен `True`, `Accept` устанавливается в `text/event-stream`, иначе в `application/json`.
2.  Устанавливает `Content-Type` в `application/json`.
3.  Если предоставлен `api_key`, добавляет заголовок `Authorization` с API-ключом.
4.  Объединяет все заголовки в один словарь и возвращает его.

**ASCII flowchart**:

```
A: Определение Accept в зависимости от stream
|
B: Установка Content-Type
|
C: Добавление Authorization, если есть api_key
|
D: Объединение заголовков
|
E: Возврат словаря заголовков
```

**Примеры**:

```python
# Пример получения заголовков для потокового запроса с API-ключом
headers = OpenaiTemplate.get_headers(stream=True, api_key="YOUR_API_KEY")

# Пример получения заголовков для обычного запроса без API-ключа и дополнительных заголовков
headers = OpenaiTemplate.get_headers(stream=False)

# Пример получения заголовков с дополнительными заголовками
headers = OpenaiTemplate.get_headers(stream=False, headers={"X-Custom-Header": "value"})