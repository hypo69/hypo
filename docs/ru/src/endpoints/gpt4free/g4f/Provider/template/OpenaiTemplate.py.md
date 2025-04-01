# Модуль `OpenaiTemplate.py`

## Обзор

Модуль `OpenaiTemplate.py` предоставляет шаблон для взаимодействия с API OpenAI. Он включает в себя функциональность для получения списка доступных моделей, создания асинхронного генератора для запросов к API, обработки потоковых ответов и управления заголовками запросов. Этот шаблон предназначен для упрощения интеграции с различными моделями OpenAI, включая модели генерации изображений.

## Подробней

Модуль `OpenaiTemplate` содержит абстрактный класс, который служит базовым шаблоном для реализации провайдеров, работающих с API OpenAI. Он предоставляет методы для получения списка моделей, создания асинхронных генераторов для взаимодействия с API, обработки ошибок и формирования заголовков запросов. Класс также поддерживает работу с историей сообщений и системными сообщениями, что позволяет использовать его для различных задач, таких как генерация текста и изображений.

## Классы

### `OpenaiTemplate`

**Описание**: Базовый класс-шаблон для провайдеров OpenAI.

**Принцип работы**:
Класс `OpenaiTemplate` предоставляет интерфейс для взаимодействия с API OpenAI. Он определяет основные параметры, такие как `api_base`, `api_key`, `api_endpoint` и другие настройки. Класс содержит методы для получения списка моделей, создания асинхронных генераторов для запросов и обработки ответов от API. Он также реализует поддержку истории сообщений, системных сообщений и различные параметры запросов, такие как температуру, максимальное количество токенов и другие.

**Атрибуты**:

- `api_base` (str): Базовый URL API OpenAI.
- `api_key` (str | None): Ключ API для аутентификации.
- `api_endpoint` (str | None): Конечная точка API для запросов.
- `supports_message_history` (bool): Указывает, поддерживает ли провайдер историю сообщений.
- `supports_system_message` (bool): Указывает, поддерживает ли провайдер системные сообщения.
- `default_model` (str): Модель, используемая по умолчанию.
- `fallback_models` (list[str]): Список моделей для переключения в случае ошибки.
- `sort_models` (bool): Указывает, нужно ли сортировать список моделей.
- `ssl` (bool | None): Параметр для проверки SSL сертификата.

**Методы**:

- `get_models(api_key: str = None, api_base: str = None) -> list[str]`: Возвращает список доступных моделей.
- `create_async_generator(...) -> AsyncResult`: Создает асинхронный генератор для запросов к API.
- `get_headers(stream: bool, api_key: str = None, headers: dict = None) -> dict`: Формирует заголовки запроса.

## Функции

### `get_models`

```python
@classmethod
def get_models(cls, api_key: str = None, api_base: str = None) -> list[str]:
    """
    Получает список доступных моделей из API OpenAI.

    Args:
        api_key (str, optional): Ключ API для аутентификации. Если не указан, используется `cls.api_key`. По умолчанию `None`.
        api_base (str, optional): Базовый URL API OpenAI. Если не указан, используется `cls.api_base`. По умолчанию `None`.

    Returns:
        list[str]: Список идентификаторов доступных моделей. Возвращает `cls.fallback_models` в случае ошибки.
    """
```

**Назначение**: Получение списка доступных моделей из API OpenAI.

**Параметры**:

- `api_key` (str, optional): Ключ API для аутентификации. Если не указан, используется `cls.api_key`. По умолчанию `None`.
- `api_base` (str, optional): Базовый URL API OpenAI. Если не указан, используется `cls.api_base`. По умолчанию `None`.

**Возвращает**:

- `list[str]`: Список идентификаторов доступных моделей. Возвращает `cls.fallback_models` в случае ошибки.

**Как работает функция**:

1. Проверяет, был ли уже получен список моделей (`cls.models`).
2. Если список моделей не был получен, выполняет запрос к API OpenAI для получения списка доступных моделей.
3. Формирует заголовки запроса, включая ключ API, если он предоставлен.
4. Выполняет GET-запрос к API OpenAI (`f"{api_base}/models"`) для получения списка моделей.
5. Обрабатывает ответ от API, извлекая идентификаторы моделей из JSON-данных.
6. Если происходит ошибка во время запроса или обработки ответа, логирует ошибку и возвращает `cls.fallback_models`.
7. Если список моделей был успешно получен, сохраняет его в `cls.models` и возвращает его.

```
A: Проверка наличия моделей в cls.models
|
B: Если модели есть -> Возврат cls.models
|
C: Если моделей нет -> Формирование заголовков запроса
|
D: Выполнение GET-запроса к API OpenAI
|
E: Обработка ответа от API -> Извлечение идентификаторов моделей
|
F: Сохранение списка моделей в cls.models и возврат
|
G: Если произошла ошибка -> Логирование ошибки и возврат cls.fallback_models
```

**Примеры**:

```python
# Пример вызова функции get_models без параметров
models = OpenaiTemplate.get_models()

# Пример вызова функции get_models с указанием api_key и api_base
models = OpenaiTemplate.get_models(api_key="your_api_key", api_base="https://api.openai.com/v1")
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
    Создает асинхронный генератор для взаимодействия с API OpenAI.

    Args:
        model (str): Идентификатор модели для использования.
        messages (Messages): Список сообщений для отправки в API.
        proxy (str, optional): URL прокси-сервера. По умолчанию `None`.
        timeout (int, optional): Максимальное время ожидания ответа от API в секундах. По умолчанию `120`.
        media (MediaListType, optional): Список медиа-файлов для отправки в API. По умолчанию `None`.
        api_key (str, optional): Ключ API для аутентификации. Если не указан, используется `cls.api_key`. По умолчанию `None`.
        api_endpoint (str, optional): Конечная точка API для запросов. Если не указан, используется `cls.api_endpoint`. По умолчанию `None`.
        api_base (str, optional): Базовый URL API OpenAI. Если не указан, используется `cls.api_base`. По умолчанию `None`.
        temperature (float, optional): Параметр температуры для управления случайностью генерации. По умолчанию `None`.
        max_tokens (int, optional): Максимальное количество токенов в ответе. По умолчанию `None`.
        top_p (float, optional): Параметр top_p для управления разнообразием генерации. По умолчанию `None`.
        stop (Union[str, list[str]], optional): Список стоп-слов, при обнаружении которых генерация прекращается. По умолчанию `None`.
        stream (bool, optional): Указывает, нужно ли использовать потоковый режим. По умолчанию `False`.
        prompt (str, optional): Промпт для генерации изображения, если используется модель генерации изображений. По умолчанию `None`.
        headers (dict, optional): Дополнительные заголовки для запроса. По умолчанию `None`.
        impersonate (str, optional): Идентификатор для имитации пользователя. По умолчанию `None`.
        extra_parameters (list[str], optional): Список дополнительных параметров, которые будут переданы в API. По умолчанию `["tools", "parallel_tool_calls", "tool_choice", "reasoning_effort", "logit_bias", "modalities", "audio"]`.
        extra_data (dict, optional): Дополнительные данные для запроса. По умолчанию `{}`.
        **kwargs: Дополнительные параметры.

    Yields:
        str | ToolCalls | Usage | FinishReason | ImageResponse: Части ответа от API в зависимости от типа запроса и ответа.
    """
```

**Назначение**: Создание асинхронного генератора для взаимодействия с API OpenAI.

**Параметры**:

- `model` (str): Идентификатор модели для использования.
- `messages` (Messages): Список сообщений для отправки в API.
- `proxy` (str, optional): URL прокси-сервера. По умолчанию `None`.
- `timeout` (int, optional): Максимальное время ожидания ответа от API в секундах. По умолчанию `120`.
- `media` (MediaListType, optional): Список медиа-файлов для отправки в API. По умолчанию `None`.
- `api_key` (str, optional): Ключ API для аутентификации. Если не указан, используется `cls.api_key`. По умолчанию `None`.
- `api_endpoint` (str, optional): Конечная точка API для запросов. Если не указан, используется `cls.api_endpoint`. По умолчанию `None`.
- `api_base` (str, optional): Базовый URL API OpenAI. Если не указан, используется `cls.api_base`. По умолчанию `None`.
- `temperature` (float, optional): Параметр температуры для управления случайностью генерации. По умолчанию `None`.
- `max_tokens` (int, optional): Максимальное количество токенов в ответе. По умолчанию `None`.
- `top_p` (float, optional): Параметр top_p для управления разнообразием генерации. По умолчанию `None`.
- `stop` (Union[str, list[str]], optional): Список стоп-слов, при обнаружении которых генерация прекращается. По умолчанию `None`.
- `stream` (bool, optional): Указывает, нужно ли использовать потоковый режим. По умолчанию `False`.
- `prompt` (str, optional): Промпт для генерации изображения, если используется модель генерации изображений. По умолчанию `None`.
- `headers` (dict, optional): Дополнительные заголовки для запроса. По умолчанию `None`.
- `impersonate` (str, optional): Идентификатор для имитации пользователя. По умолчанию `None`.
- `extra_parameters` (list[str], optional): Список дополнительных параметров, которые будут переданы в API. По умолчанию `["tools", "parallel_tool_calls", "tool_choice", "reasoning_effort", "logit_bias", "modalities", "audio"]`.
- `extra_data` (dict, optional): Дополнительные данные для запроса. По умолчанию `{}`.
- `**kwargs`: Дополнительные параметры.

**Возвращает**:

- `AsyncResult`: Асинхронный генератор, выдающий части ответа от API в зависимости от типа запроса и ответа.

**Как работает функция**:

1.  **Проверка аутентификации**:
    *   Если `api_key` не предоставлен, использует `cls.api_key`.
    *   Если требуется аутентификация и `api_key` отсутствует, вызывает исключение `MissingAuthError`.
2.  **Инициализация сессии**:
    *   Создает асинхронную сессию (`StreamSession`) с использованием прокси, заголовков и таймаута.
3.  **Получение модели**:
    *   Получает модель с использованием `cls.get_model`.
4.  **Генерация изображений**:
    *   Если модель поддерживает генерацию изображений (`model in cls.image_models`):
        *   Форматирует промпт для генерации изображений.
        *   Выполняет POST-запрос к API для генерации изображения.
        *   Обрабатывает ответ и выдает URL изображений.
5.  **Генерация текста**:
    *   Если модель не поддерживает генерацию изображений:
        *   Формирует данные для запроса (`data`) с использованием предоставленных параметров и сообщений.
        *   Выполняет POST-запрос к API для генерации текста.
        *   Обрабатывает ответ в зависимости от типа контента (`content_type`):
            *   Если `content_type` начинается с `"application/json"`:
                *   Извлекает контент сообщения, `tool_calls`, `usage` и `finish_reason` из JSON-ответа и выдает их.
            *   Если `content_type` начинается с `"text/event-stream"`:
                *   Обрабатывает потоковый ответ (`response.sse()`) и выдает дельты контента, `usage` и `finish_reason`.
            *   Если `content_type` не поддерживается, вызывает исключение `ResponseError`.

```
A: Проверка наличия api_key и необходимости аутентификации
|
B: Создание асинхронной сессии
|
C: Получение модели
|
D: Проверка, является ли модель моделью генерации изображений
|
E1: Если да -> Форматирование промпта и выполнение POST-запроса для генерации изображения
|
E2: Если нет -> Формирование данных для запроса
|
F: Выполнение POST-запроса к API
|
G: Обработка ответа в зависимости от content_type
|
H1: Если content_type == "application/json" -> Извлечение и выдача контента, tool_calls, usage и finish_reason
|
H2: Если content_type == "text/event-stream" -> Обработка потокового ответа и выдача дельт контента, usage и finish_reason
|
H3: Если content_type не поддерживается -> Вызов исключения ResponseError
```

**Примеры**:

```python
# Пример вызова функции create_async_generator для генерации текста
messages = [{"role": "user", "content": "Hello, how are you?"}]
async_generator = OpenaiTemplate.create_async_generator(model="gpt-3.5-turbo", messages=messages, api_key="your_api_key")

# Пример вызова функции create_async_generator для генерации изображения
messages = [{"role": "user", "content": "A cat sitting on a mat."}]
async_generator = OpenaiTemplate.create_async_generator(model="dall-e-3", messages=messages, api_key="your_api_key", prompt="A cat sitting on a mat.")
```

### `get_headers`

```python
@classmethod
def get_headers(cls, stream: bool, api_key: str = None, headers: dict = None) -> dict:
    """
    Формирует заголовки запроса.

    Args:
        stream (bool): Указывает, нужно ли использовать потоковый режим.
        api_key (str, optional): Ключ API для аутентификации. По умолчанию `None`.
        headers (dict, optional): Дополнительные заголовки для запроса. По умолчанию `None`.

    Returns:
        dict: Словарь с заголовками запроса.
    """
```

**Назначение**: Формирование заголовков запроса.

**Параметры**:

- `stream` (bool): Указывает, нужно ли использовать потоковый режим.
- `api_key` (str, optional): Ключ API для аутентификации. По умолчанию `None`.
- `headers` (dict, optional): Дополнительные заголовки для запроса. По умолчанию `None`.

**Возвращает**:

- `dict`: Словарь с заголовками запроса.

**Как работает функция**:

1.  Формирует базовые заголовки, включая `Accept` и `Content-Type`.
2.  Добавляет заголовок `Authorization` с ключом API, если `api_key` предоставлен.
3.  Объединяет базовые заголовки с дополнительными заголовками, если они предоставлены.
4.  Возвращает словарь с заголовками запроса.

```
A: Формирование базовых заголовков (Accept, Content-Type)
|
B: Проверка наличия api_key
|
C: Если api_key есть -> Добавление заголовка Authorization
|
D: Объединение базовых заголовков с дополнительными заголовками
|
E: Возврат словаря с заголовками запроса
```

**Примеры**:

```python
# Пример вызова функции get_headers без параметров
headers = OpenaiTemplate.get_headers(stream=True)

# Пример вызова функции get_headers с указанием api_key и дополнительными заголовками
headers = OpenaiTemplate.get_headers(stream=False, api_key="your_api_key", headers={"X-Custom-Header": "value"})