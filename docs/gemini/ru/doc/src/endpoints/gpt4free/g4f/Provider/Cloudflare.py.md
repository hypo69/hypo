# Модуль Cloudflare

## Обзор

Модуль `Cloudflare` предоставляет асинхронный интерфейс для взаимодействия с AI-моделями, размещенными на платформе Cloudflare AI. Он поддерживает потоковую передачу данных и предоставляет функциональность для управления cookies и заголовками HTTP-запросов. Модуль предназначен для использования в проекте `hypotez`.

## Подробней

Модуль `Cloudflare` является провайдером AI-моделей и реализует асинхронный генератор для получения результатов. Он использует библиотеки `asyncio`, `json` и другие для асинхронной обработки запросов и потоковой передачи данных. Модуль также предоставляет функциональность для работы с cookies, заголовками HTTP-запросов и кэшированием аргументов для повышения производительности.

## Классы

### `Cloudflare`

**Описание**: Класс `Cloudflare` предоставляет асинхронный интерфейс для взаимодействия с AI-моделями на платформе Cloudflare AI.

**Наследует**:
- `AsyncGeneratorProvider`: Обеспечивает функциональность асинхронного генератора.
- `ProviderModelMixin`: Предоставляет методы для работы с моделями.
- `AuthFileMixin`: Добавляет поддержку аутентификации через файлы.

**Атрибуты**:
- `label` (str): Метка провайдера ("Cloudflare AI").
- `url` (str): URL главной страницы Cloudflare AI ("https://playground.ai.cloudflare.com").
- `working` (bool): Флаг, указывающий, работает ли провайдер (True).
- `use_nodriver` (bool): Флаг, указывающий, использовать ли nodriver (True).
- `api_endpoint` (str): URL API для инференса ("https://playground.ai.cloudflare.com/api/inference").
- `models_url` (str): URL для получения списка моделей ("https://playground.ai.cloudflare.com/api/models").
- `supports_stream` (bool): Флаг, указывающий, поддерживает ли провайдер потоковую передачу данных (True).
- `supports_system_message` (bool): Флаг, указывающий, поддерживает ли провайдер системные сообщения (True).
- `supports_message_history` (bool): Флаг, указывающий, поддерживает ли провайдер историю сообщений (True).
- `default_model` (str): Модель по умолчанию ("@cf/meta/llama-3.3-70b-instruct-fp8-fast").
- `model_aliases` (dict): Алиасы моделей.
- `_args` (dict): Аргументы для сессии.

**Методы**:
- `get_models()`: Получает список доступных моделей.
- `create_async_generator()`: Создает асинхронный генератор для получения результатов от AI-модели.

### `get_models`

```python
@classmethod
def get_models(cls) -> str:
    """Получает список доступных моделей из Cloudflare AI.

    Args:
        cls (Cloudflare): Ссылка на класс `Cloudflare`.

    Returns:
        str: Список доступных моделей.

    Raises:
        ResponseStatusError: Если возникает ошибка при получении списка моделей.

    Как работает функция:
    1. Проверяет, если список моделей уже загружен. Если да, возвращает его.
    2. Проверяет, если аргументы сессии (`cls._args`) не инициализированы. Если да, пытается получить их из кэша,
       используя `get_args_from_nodriver` или устанавливает значения по умолчанию.
    3. Создает HTTP-сессию с использованием аргументов сессии.
    4. Отправляет GET-запрос к `cls.models_url` для получения списка моделей.
    5. Обновляет cookies из ответа в аргументах сессии.
    6. Обрабатывает возможные ошибки статуса ответа.
    7. Извлекает имена моделей из JSON-ответа и сохраняет их в `cls.models`.
    8. Возвращает список моделей.

    ASCII Flowchart:
    A [Проверка наличия моделей в cls.models]
    |
    B [Если модели есть: Возврат cls.models]
    |
    C [Если моделей нет: Проверка cls._args]
    |
    D [Если cls._args нет: Получение аргументов сессии (из кэша или nodriver)]
    |
    E [Создание HTTP-сессии]
    |
    F [GET-запрос к cls.models_url]
    |
    G [Обновление cookies]
    |
    H [Обработка ошибок статуса ответа]
    |
    I [Извлечение имен моделей из JSON]
    |
    J [Сохранение моделей в cls.models]
    |
    K [Возврат cls.models]

    Примеры:
    >>> Cloudflare.get_models()
    ['@cf/meta/llama-3.3-70b-instruct-fp8-fast', ...]
    """
    ...
```

### `create_async_generator`

```python
@classmethod
async def create_async_generator(
    cls,
    model: str,
    messages: Messages,
    proxy: str = None,
    max_tokens: int = 2048,
    cookies: Cookies = None,
    timeout: int = 300,
    **kwargs
) -> AsyncResult:
    """Создает асинхронный генератор для получения результатов от AI-модели.

    Args:
        cls (Cloudflare): Ссылка на класс `Cloudflare`.
        model (str): Имя модели для использования.
        messages (Messages): Список сообщений для отправки в модель.
        proxy (str, optional): URL прокси-сервера. По умолчанию `None`.
        max_tokens (int, optional): Максимальное количество токенов в ответе. По умолчанию 2048.
        cookies (Cookies, optional): Cookies для отправки с запросом. По умолчанию `None`.
        timeout (int, optional): Время ожидания ответа в секундах. По умолчанию 300.
        **kwargs: Дополнительные аргументы.

    Returns:
        AsyncResult: Асинхронный генератор для получения результатов.

    Raises:
        ResponseStatusError: Если возникает ошибка при отправке запроса.

    Как работает функция:
    1. Получает путь к файлу кэша.
    2. Проверяет, если аргументы сессии (`cls._args`) не инициализированы. Если да, пытается загрузить их из кэша
       или получает их с помощью `get_args_from_nodriver`.
    3. Преобразует имя модели с помощью `cls.get_model`.
    4. Формирует JSON-данные для отправки в API.
    5. Создает асинхронную HTTP-сессию с использованием `StreamSession`.
    6. Отправляет POST-запрос к `cls.api_endpoint` с JSON-данными.
    7. Обновляет cookies из ответа в аргументах сессии.
    8. Обрабатывает возможные ошибки статуса ответа.
    9. Итерируется по строкам ответа и извлекает данные.
    10. Извлекает информацию об использовании и причине завершения из строк ответа.
    11. Сохраняет аргументы сессии в файл кэша.
    12. Возвращает асинхронный генератор.

    ASCII Flowchart:
    A [Получение пути к файлу кэша]
    |
    B [Проверка наличия cls._args]
    |
    C [Если cls._args нет: Загрузка из кэша или получение с помощью get_args_from_nodriver]
    |
    D [Преобразование имени модели]
    |
    E [Формирование JSON-данных]
    |
    F [Создание асинхронной HTTP-сессии]
    |
    G [POST-запрос к cls.api_endpoint]
    |
    H [Обновление cookies]
    |
    I [Обработка ошибок статуса ответа]
    |
    J [Итерация по строкам ответа]
    |
    K [Извлечение данных из строк]
    |
    L [Извлечение информации об использовании и причине завершения]
    |
    M [Сохранение cls._args в файл кэша]
    |
    N [Возврат асинхронного генератора]

    Примеры:
    >>> async for result in Cloudflare.create_async_generator(model='@cf/meta/llama-3.3-70b-instruct-fp8-fast', messages=[{'role': 'user', 'content': 'Hello'}]):
    ...     print(result)
    """
    ...
```

## Функции

### `get_running_loop`

```python
from ..typing import AsyncResult, Messages, Cookies
from .base_provider import AsyncGeneratorProvider, ProviderModelMixin, AuthFileMixin, get_running_loop
from ..requests import Session, StreamSession, get_args_from_nodriver, raise_for_status, merge_cookies
from ..requests import DEFAULT_HEADERS, has_nodriver, has_curl_cffi
from ..providers.response import FinishReason, Usage
from ..errors import ResponseStatusError, ModelNotFoundError
```

**Назначение**: Импортирует необходимые модули и классы для работы `Cloudflare`.

**Параметры**:
- `AsyncResult`: Тип для асинхронных результатов.
- `Messages`: Тип для сообщений.
- `Cookies`: Тип для cookies.
- `AsyncGeneratorProvider`: Базовый класс для асинхронных провайдеров-генераторов.
- `ProviderModelMixin`: Миксин для работы с моделями провайдера.
- `AuthFileMixin`: Миксин для аутентификации через файл.
- `get_running_loop`: Функция для получения текущего event loop.
- `Session`: Класс для HTTP-сессий.
- `StreamSession`: Класс для потоковых HTTP-сессий.
- `get_args_from_nodriver`: Функция для получения аргументов из nodriver.
- `raise_for_status`: Функция для проверки статуса ответа.
- `merge_cookies`: Функция для объединения cookies.
- `DEFAULT_HEADERS`: Заголовки HTTP по умолчанию.
- `has_nodriver`: Проверка наличия nodriver.
- `has_curl_cffi`: Проверка наличия curl_cffi.
- `FinishReason`: Тип для причины завершения.
- `Usage`: Тип для информации об использовании.
- `ResponseStatusError`: Ошибка статуса ответа.
- `ModelNotFoundError`: Ошибка, если модель не найдена.

**Как работает функция**:
1. Импортирует все необходимые модули и классы.
2. Определяет типы и базовые классы, используемые в модуле `Cloudflare`.

**Примеры**:
```python
from ..typing import AsyncResult, Messages, Cookies
from .base_provider import AsyncGeneratorProvider, ProviderModelMixin, AuthFileMixin, get_running_loop
from ..requests import Session, StreamSession, get_args_from_nodriver, raise_for_status, merge_cookies
from ..requests import DEFAULT_HEADERS, has_nodriver, has_curl_cffi
from ..providers.response import FinishReason, Usage
from ..errors import ResponseStatusError, ModelNotFoundError
```

## Переменные

### `DEFAULT_HEADERS`

**Назначение**: `DEFAULT_HEADERS` - словарь, содержащий заголовки HTTP по умолчанию, используемые при выполнении запросов к API Cloudflare.

**Описание**:
- Этот словарь содержит стандартные заголовки, которые обычно включают информацию о типе контента (`Content-Type`) и User-Agent.

**Пример**:
```python
DEFAULT_HEADERS = {
    "Content-Type": "application/json",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}