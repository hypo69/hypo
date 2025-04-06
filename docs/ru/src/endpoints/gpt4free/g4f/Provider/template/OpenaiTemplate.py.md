# Модуль OpenaiTemplate
## Обзор

Модуль `OpenaiTemplate` предоставляет базовый класс для взаимодействия с API OpenAI, включая поддержку асинхронной генерации текста, получения списка моделей и обработки ошибок. Он предназначен для использования в качестве шаблона при создании провайдеров, работающих с OpenAI.

## Подробнее

Модуль содержит класс `OpenaiTemplate`, который наследуется от `AsyncGeneratorProvider`, `ProviderModelMixin` и `RaiseErrorMixin`. Он предоставляет методы для получения списка доступных моделей, создания асинхронного генератора для взаимодействия с API и формирования заголовков запросов. Модуль также обрабатывает различные типы ответов от API, включая JSON и `text/event-stream`.

## Классы

### `OpenaiTemplate`

**Описание**:
Базовый класс для работы с OpenAI API, предоставляющий функциональность для асинхронной генерации текста и получения списка моделей.

**Наследует**:

- `AsyncGeneratorProvider`: Обеспечивает поддержку асинхронной генерации данных.
- `ProviderModelMixin`: Предоставляет методы для работы с моделями.
- `RaiseErrorMixin`: Содержит методы для обработки и поднятия ошибок.

**Атрибуты**:

- `api_base` (str): Базовый URL API OpenAI.
- `api_key` (str | None): Ключ API для аутентификации. По умолчанию `None`.
- `api_endpoint` (str | None): URL эндпоинта API. По умолчанию `None`.
- `supports_message_history` (bool): Флаг, указывающий на поддержку истории сообщений. По умолчанию `True`.
- `supports_system_message` (bool): Флаг, указывающий на поддержку системных сообщений. По умолчанию `True`.
- `default_model` (str): Модель, используемая по умолчанию.
- `fallback_models` (list[str]): Список запасных моделей.
- `sort_models` (bool): Флаг, указывающий на необходимость сортировки моделей. По умолчанию `True`.
- `ssl` (bool | None): Флаг, указывающий на необходимость проверки SSL-сертификата. По умолчанию `None`.

**Методы**:

- `get_models(api_key: str = None, api_base: str = None) -> list[str]`: Получает список доступных моделей.
- `create_async_generator(...) -> AsyncResult`: Создает асинхронный генератор для взаимодействия с API.
- `get_headers(stream: bool, api_key: str = None, headers: dict = None) -> dict`: Формирует заголовки запроса.

## Функции

### `get_models`

```python
@classmethod
def get_models(cls, api_key: str = None, api_base: str = None) -> list[str]:
    """
    Получает список доступных моделей от OpenAI API.

    Args:
        api_key (str, optional): Ключ API для аутентификации. Если не указан, используется значение `cls.api_key`. По умолчанию `None`.
        api_base (str, optional): Базовый URL API OpenAI. Если не указан, используется значение `cls.api_base`. По умолчанию `None`.

    Returns:
        list[str]: Список идентификаторов доступных моделей.

    Raises:
        Exception: Если происходит ошибка при выполнении запроса.

    Example:
        >>> OpenaiTemplate.get_models(api_key="your_api_key")
        ['gpt-3.5-turbo', 'gpt-4']
    """
```

**Назначение**:
Функция `get_models` получает список доступных моделей из API OpenAI.

**Параметры**:

- `api_key` (str, optional): Ключ API для аутентификации. Если не указан, используется значение `cls.api_key`. По умолчанию `None`.
- `api_base` (str, optional): Базовый URL API OpenAI. Если не указан, используется значение `cls.api_base`. По умолчанию `None`.

**Возвращает**:

- `list[str]`: Список идентификаторов доступных моделей.

**Вызывает исключения**:

- `Exception`: Если происходит ошибка при выполнении запроса.

**Как работает функция**:

1. **Проверка кэша моделей**: Функция проверяет, был ли уже получен список моделей. Если список моделей `cls.models` не пуст, функция возвращает его.
2. **Формирование заголовков**: Если требуется получить список моделей, функция формирует заголовки для запроса, включая ключ API (если он предоставлен).
3. **Выполнение запроса**: Функция выполняет GET-запрос к эндпоинту `/models` API OpenAI.
4. **Обработка ответа**: Функция обрабатывает ответ от API, извлекая идентификаторы моделей из JSON-ответа.
5. **Кэширование моделей**: Функция сохраняет полученный список моделей в `cls.models` и список моделей, поддерживающих изображения, в `cls.image_models` для последующего использования.
6. **Обработка ошибок**: В случае возникновения ошибки при выполнении запроса, функция логирует ошибку и возвращает список запасных моделей `cls.fallback_models`.

**ASCII flowchart**:

```
A [Проверка наличия моделей в кэше cls.models]
│
├───> B [Если модели в кэше есть]
│       │
│       └───> Вернуть cls.models
│
└───> C [Если моделей в кэше нет]
│       │
│       D [Формирование заголовков запроса (включая API-ключ, если предоставлен)]
│       │
│       E [Выполнение GET-запроса к эндпоинту /models]
│       │
│       F [Обработка JSON-ответа для извлечения идентификаторов моделей]
│       │
│       G [Сохранение списка моделей в cls.models и списка image_models]
│       │
│       H [Обработка возможных ошибок при запросе]
│       │
│       └───> I [Логирование ошибки и возврат cls.fallback_models]
│
└───> Вернуть cls.models
```

**Примеры**:

```python
# Пример получения списка моделей с использованием API-ключа
models = OpenaiTemplate.get_models(api_key="your_api_key")
print(models)

# Пример получения списка моделей без указания API-ключа (если он уже установлен в классе)
OpenaiTemplate.api_key = "your_api_key"
models = OpenaiTemplate.get_models()
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
        timeout (int, optional): Максимальное время ожидания запроса в секундах. По умолчанию `120`.
        media (MediaListType, optional): Список медиафайлов для отправки в API. По умолчанию `None`.
        api_key (str, optional): Ключ API для аутентификации. Если не указан, используется значение `cls.api_key`. По умолчанию `None`.
        api_endpoint (str, optional): URL эндпоинта API. По умолчанию `None`.
        api_base (str, optional): Базовый URL API OpenAI. По умолчанию `None`.
        temperature (float, optional): Параметр temperature для управления случайностью генерации. По умолчанию `None`.
        max_tokens (int, optional): Максимальное количество токенов в ответе. По умолчанию `None`.
        top_p (float, optional): Параметр top_p для управления разнообразием генерации. По умолчанию `None`.
        stop (Union[str, list[str]], optional): Список стоп-слов, при встрече которых генерация прекращается. По умолчанию `None`.
        stream (bool, optional): Флаг, указывающий на использование потоковой передачи данных. По умолчанию `False`.
        prompt (str, optional): Дополнительный промпт для отправки в API. По умолчанию `None`.
        headers (dict, optional): Дополнительные заголовки для отправки в API. По умолчанию `None`.
        impersonate (str, optional): Идентификатор пользователя для выполнения запроса от его имени. По умолчанию `None`.
        extra_parameters (list[str], optional): Список дополнительных параметров, которые будут переданы в API.
        extra_data (dict, optional): Дополнительные данные для отправки в API.
        **kwargs: Дополнительные параметры.

    Returns:
        AsyncResult: Асинхронный генератор, возвращающий данные от API.

    Raises:
        MissingAuthError: Если не предоставлен ключ API и `cls.needs_auth` равен `True`.
        ResponseError: Если получен неподдерживаемый `content-type`.

    """
```

**Назначение**:
Функция `create_async_generator` создает асинхронный генератор для взаимодействия с API OpenAI.

**Параметры**:

- `model` (str): Идентификатор модели для использования.
- `messages` (Messages): Список сообщений для отправки в API.
- `proxy` (str, optional): URL прокси-сервера. По умолчанию `None`.
- `timeout` (int, optional): Максимальное время ожидания запроса в секундах. По умолчанию `120`.
- `media` (MediaListType, optional): Список медиафайлов для отправки в API. По умолчанию `None`.
- `api_key` (str, optional): Ключ API для аутентификации. Если не указан, используется значение `cls.api_key`. По умолчанию `None`.
- `api_endpoint` (str, optional): URL эндпоинта API. По умолчанию `None`.
- `api_base` (str, optional): Базовый URL API OpenAI. По умолчанию `None`.
- `temperature` (float, optional): Параметр temperature для управления случайностью генерации. По умолчанию `None`.
- `max_tokens` (int, optional): Максимальное количество токенов в ответе. По умолчанию `None`.
- `top_p` (float, optional): Параметр top_p для управления разнообразием генерации. По умолчанию `None`.
- `stop` (Union[str, list[str]], optional): Список стоп-слов, при встрече которых генерация прекращается. По умолчанию `None`.
- `stream` (bool, optional): Флаг, указывающий на использование потоковой передачи данных. По умолчанию `False`.
- `prompt` (str, optional): Дополнительный промпт для отправки в API. По умолчанию `None`.
- `headers` (dict, optional): Дополнительные заголовки для отправки в API. По умолчанию `None`.
- `impersonate` (str, optional): Идентификатор пользователя для выполнения запроса от его имени. По умолчанию `None`.
- `extra_parameters` (list[str], optional): Список дополнительных параметров, которые будут переданы в API.
- `extra_data` (dict, optional): Дополнительные данные для отправки в API.
- `**kwargs`: Дополнительные параметры.

**Возвращает**:

- `AsyncResult`: Асинхронный генератор, возвращающий данные от API.

**Вызывает исключения**:

- `MissingAuthError`: Если не предоставлен ключ API и `cls.needs_auth` равен `True`.
- `ResponseError`: Если получен неподдерживаемый `content-type`.

**Как работает функция**:

1. **Получение API-ключа**: Функция проверяет, предоставлен ли API-ключ. Если API-ключ не предоставлен, функция пытается использовать значение `cls.api_key`.
2. **Проверка аутентификации**: Если требуется аутентификация (`cls.needs_auth` равен `True`), и API-ключ не предоставлен, функция вызывает исключение `MissingAuthError`.
3. **Создание StreamSession**: Функция создает асинхронную сессию `StreamSession` для выполнения запросов к API.
4. **Получение модели**: Функция получает идентификатор модели для использования, вызывая `cls.get_model`.
5. **Генерация изображений (если модель поддерживает)**: Если модель поддерживает генерацию изображений (присутствует в `cls.image_models`), функция формирует данные для запроса и отправляет POST-запрос к эндпоинту `/images/generations`. Результатом является генератор, возвращающий URL сгенерированных изображений.
6. **Формирование данных для запроса**: Если модель не поддерживает генерацию изображений, функция формирует данные для запроса, включая сообщения, параметры температуры, максимальное количество токенов и другие параметры.
7. **Отправка POST-запроса**: Функция отправляет POST-запрос к эндпоинту `/chat/completions` (или `api_endpoint`, если он указан).
8. **Обработка ответа**: Функция обрабатывает ответ от API, который может быть в формате JSON или `text/event-stream`.
    - **JSON**: Функция извлекает содержимое сообщения, вызовы инструментов (tool_calls), информацию об использовании токенов (usage) и причину завершения генерации (finish_reason) из JSON-ответа.
    - **text/event-stream**: Функция обрабатывает потоковые данные, извлекая дельты содержимого сообщения, информацию об использовании токенов и причину завершения генерации.
9. **Генерация данных**: Функция генерирует данные на основе ответа от API, возвращая содержимое сообщения, вызовы инструментов, информацию об использовании токенов и причину завершения генерации.
10. **Обработка ошибок**: Если получен неподдерживаемый `content-type`, функция вызывает исключение `ResponseError`.

**ASCII flowchart**:

```
A [Получение API-ключа]
│
├───> B [Проверка необходимости аутентификации и наличия API-ключа]
│       │
│       └───> C [Если API-ключ отсутствует и требуется аутентификация, вызвать MissingAuthError]
│
└───> D [Создание StreamSession]
│       │
│       E [Получение идентификатора модели]
│       │
│       F [Проверка, поддерживает ли модель генерацию изображений]
│       │
│       ├───> G [Если модель поддерживает генерацию изображений]
│       │       │
│       │       H [Формирование данных и отправка POST-запроса к /images/generations]
│       │       │
│       │       └───> I [Генерация URL сгенерированных изображений]
│       │
│       └───> J [Если модель не поддерживает генерацию изображений]
│               │
│               K [Формирование данных для запроса (сообщения, параметры и т.д.)]
│               │
│               L [Отправка POST-запроса к /chat/completions]
│               │
│               M [Обработка ответа (JSON или text/event-stream)]
│               │
│               ├───> N [JSON]
│               │       │
│               │       O [Извлечение содержимого сообщения, вызовов инструментов, usage и finish_reason]
│               │
│               └───> P [text/event-stream]
│                       │
│                       Q [Обработка потоковых данных, извлечение дельт содержимого, usage и finish_reason]
│               │
│               R [Генерация данных (содержимое сообщения, вызовы инструментов, usage и finish_reason)]
│
└───> S [Обработка ошибок (неподдерживаемый content-type)]
```

**Примеры**:

```python
# Пример создания асинхронного генератора с использованием API-ключа и модели
async def main():
    async for chunk in OpenaiTemplate.create_async_generator(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": "Hello, how are you?"}],
        api_key="your_api_key"
    ):
        print(chunk)

# Пример создания асинхронного генератора с использованием прокси-сервера
async def main():
    async for chunk in OpenaiTemplate.create_async_generator(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": "Hello, how are you?"}],
        api_key="your_api_key",
        proxy="http://your_proxy:8080"
    ):
        print(chunk)
```

### `get_headers`

```python
@classmethod
def get_headers(cls, stream: bool, api_key: str = None, headers: dict = None) -> dict:
    """
    Формирует заголовки запроса для API OpenAI.

    Args:
        stream (bool): Флаг, указывающий на использование потоковой передачи данных.
        api_key (str, optional): Ключ API для аутентификации. Если не указан, используется значение `cls.api_key`. По умолчанию `None`.
        headers (dict, optional): Дополнительные заголовки для отправки в API. По умолчанию `None`.

    Returns:
        dict: Словарь с заголовками запроса.

    Example:
        >>> OpenaiTemplate.get_headers(stream=True, api_key="your_api_key")
        {'Accept': 'text/event-stream', 'Content-Type': 'application/json', 'Authorization': 'Bearer your_api_key'}
    """
```

**Назначение**:
Функция `get_headers` формирует заголовки запроса для API OpenAI.

**Параметры**:

- `stream` (bool): Флаг, указывающий на использование потоковой передачи данных.
- `api_key` (str, optional): Ключ API для аутентификации. Если не указан, используется значение `cls.api_key`. По умолчанию `None`.
- `headers` (dict, optional): Дополнительные заголовки для отправки в API. По умолчанию `None`.

**Возвращает**:

- `dict`: Словарь с заголовками запроса.

**Как работает функция**:

1. **Определение типа Accept**: Функция определяет значение заголовка `Accept` в зависимости от того, используется ли потоковая передача данных (`stream`). Если `stream` равен `True`, `Accept` устанавливается в `text/event-stream`, иначе в `application/json`.
2. **Формирование заголовков**: Функция формирует словарь с заголовками, включающий `Accept` и `Content-Type`. Если предоставлен API-ключ, функция добавляет заголовок `Authorization`.
3. **Объединение заголовков**: Функция объединяет сформированные заголовки с дополнительными заголовками, предоставленными в параметре `headers`.

**ASCII flowchart**:

```
A [Определение типа Accept (stream ? text/event-stream : application/json)]
│
B [Формирование словаря с заголовками (Accept, Content-Type)]
│
C [Проверка наличия API-ключа]
│
├───> D [Если API-ключ присутствует, добавление заголовка Authorization]
│
E [Объединение сформированных заголовков с дополнительными заголовками]
│
F [Возврат словаря с заголовками]
```

**Примеры**:

```python
# Пример получения заголовков для потоковой передачи данных с API-ключом
headers = OpenaiTemplate.get_headers(stream=True, api_key="your_api_key")
print(headers)

# Пример получения заголовков без API-ключа
headers = OpenaiTemplate.get_headers(stream=False)
print(headers)