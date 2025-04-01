# Модуль Anthropic
## Обзор
Модуль `Anthropic` предоставляет интерфейс для взаимодействия с API Anthropic. Он наследует функциональность от класса `OpenaiAPI` и адаптирует её для работы с особенностями API Anthropic, включая поддержку потоковой передачи, системных сообщений и истории сообщений. Модуль позволяет отправлять текстовые и мультимедийные запросы к моделям Anthropic, таким как Claude 3.

## Подробней

Модуль `Anthropic` используется для интеграции с моделями Anthropic в проекте `hypotez`. Он обеспечивает удобный способ отправки запросов к API Anthropic, обработки ответов и управления аутентификацией. Модуль поддерживает как синхронные, так и асинхронные вызовы API, а также позволяет передавать изображения в запросах.
Модуль содержит методы для получения списка доступных моделей, создания асинхронных генераторов для обработки потоковых ответов и формирования заголовков запросов.

## Классы

### `Anthropic(OpenaiAPI)`

**Описание**: Класс `Anthropic` предназначен для взаимодействия с API Anthropic.

**Наследует**:
- `OpenaiAPI`: Наследует базовую функциональность для работы с API OpenAI, адаптируя её для API Anthropic.

**Атрибуты**:
- `label` (str): Метка, идентифицирующая провайдера как "Anthropic API".
- `url` (str): URL главной страницы Anthropic.
- `login_url` (str): URL страницы для получения ключа API.
- `working` (bool): Указывает, что провайдер в настоящее время работает.
- `api_base` (str): Базовый URL для API Anthropic.
- `needs_auth` (bool): Указывает, требуется ли аутентификация для использования API.
- `supports_stream` (bool): Указывает, поддерживает ли API потоковую передачу данных.
- `supports_system_message` (bool): Указывает, поддерживает ли API системные сообщения.
- `supports_message_history` (bool): Указывает, поддерживает ли API историю сообщений.
- `default_model` (str): Модель, используемая по умолчанию ("claude-3-5-sonnet-latest").
- `models` (list[str]): Список поддерживаемых моделей Anthropic.
- `models_aliases` (dict[str, str]): Словарь псевдонимов моделей для удобства использования.

**Методы**:
- `get_models(api_key: str = None, **kwargs)`: Получает список доступных моделей Anthropic.
- `create_async_generator(...)`: Создает асинхронный генератор для взаимодействия с API Anthropic.
- `get_headers(stream: bool, api_key: str = None, headers: dict = None)`: Формирует заголовки запроса для API Anthropic.

## Функции

### `get_models`

```python
@classmethod
def get_models(cls, api_key: str = None, **kwargs) -> list[str]:
    """
    Получает список доступных моделей Anthropic.

    Args:
        api_key (str, optional): Ключ API для аутентификации. По умолчанию `None`.
        **kwargs: Дополнительные аргументы.

    Returns:
        list[str]: Список идентификаторов моделей.

    Raises:
        requests.exceptions.HTTPError: Если HTTP-запрос завершается с ошибкой.

    Как работает функция:
    1. Проверяет, был ли уже получен список моделей. Если да, возвращает его.
    2. Если список моделей не был получен, выполняет GET-запрос к API Anthropic для получения списка моделей.
    3. Формирует заголовок запроса, включающий ключ API и версию API Anthropic.
    4. Извлекает идентификаторы моделей из JSON-ответа и сохраняет их в атрибуте `cls.models`.
    5. Возвращает список идентификаторов моделей.
    """
```
**Назначение**: Получение списка доступных моделей Anthropic.

**Параметры**:
- `api_key` (str, optional): Ключ API для аутентификации. По умолчанию `None`.
- `**kwargs`: Дополнительные аргументы.

**Возвращает**:
- `list[str]`: Список идентификаторов моделей.

**Вызывает исключения**:
- `requests.exceptions.HTTPError`: Если HTTP-запрос завершается с ошибкой.

**Как работает функция**:

```
A[Проверка наличия моделей в cls.models]
|
B[Если модели есть: возврат cls.models] - C[Если моделей нет: HTTP GET запрос к API Anthropic]
|
D[Формирование заголовка запроса (API Key, версия)]
|
E[Извлечение идентификаторов моделей из JSON ответа]
|
F[Сохранение моделей в cls.models]
|
G[Возврат списка моделей]
```
**Примеры**:

```python
# Пример получения списка моделей с использованием API-ключа
models = Anthropic.get_models(api_key="YOUR_API_KEY")
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
            model (str): Идентификатор модели для использования.
            messages (Messages): Список сообщений для отправки в API.
            proxy (str, optional): URL прокси-сервера. По умолчанию `None`.
            timeout (int, optional): Время ожидания запроса в секундах. По умолчанию 120.
            media (MediaListType, optional): Список медиафайлов для отправки. По умолчанию `None`.
            api_key (str, optional): Ключ API для аутентификации. По умолчанию `None`.
            temperature (float, optional): Температура для управления случайностью генерации. По умолчанию `None`.
            max_tokens (int, optional): Максимальное количество токенов в ответе. По умолчанию 4096.
            top_k (int, optional): Параметр top_k для управления генерацией. По умолчанию `None`.
            top_p (float, optional): Параметр top_p для управления генерацией. По умолчанию `None`.
            stop (list[str], optional): Список стоп-слов для остановки генерации. По умолчанию `None`.
            stream (bool, optional): Включить потоковую передачу данных. По умолчанию `False`.
            headers (dict, optional): Дополнительные заголовки для запроса. По умолчанию `None`.
            impersonate (str, optional): Имя пользователя для имитации. По умолчанию `None`.
            tools (Optional[list], optional): Список инструментов для использования. По умолчанию `None`.
            extra_data (dict, optional): Дополнительные данные для отправки в запросе. По умолчанию `{}`.
            **kwargs: Дополнительные аргументы.

        Returns:
            AsyncResult: Асинхронный генератор для получения ответов от API.

        Raises:
            MissingAuthError: Если не указан ключ API.

        Как работает функция:
        1. Проверяет наличие API-ключа. Если ключ отсутствует, вызывает исключение `MissingAuthError`.
        2. Обрабатывает медиафайлы (изображения), если они предоставлены, преобразуя их в формат base64 и добавляя в сообщение.
        3. Извлекает системные сообщения из списка сообщений и объединяет их в одну строку.
        4. Инициализирует асинхронную сессию с использованием `StreamSession`.
        5. Формирует словарь данных для отправки в API, включающий сообщения, модель, параметры генерации и другие настройки.
        6. Выполняет POST-запрос к API Anthropic.
        7. Обрабатывает потоковые и не потоковые ответы от API.
        8. Для потоковых ответов разбирает чанки данных и извлекает текст, вызовы инструментов и информацию об использовании.
        9. Для не потоковых ответов извлекает содержимое и информацию об использовании из JSON-ответа.
        10. Возвращает асинхронный генератор, который предоставляет ответы от API.

        """
```
**Назначение**: Создание асинхронного генератора для взаимодействия с API Anthropic.

**Параметры**:
- `model` (str): Идентификатор модели для использования.
- `messages` (Messages): Список сообщений для отправки в API.
- `proxy` (str, optional): URL прокси-сервера. По умолчанию `None`.
- `timeout` (int, optional): Время ожидания запроса в секундах. По умолчанию 120.
- `media` (MediaListType, optional): Список медиафайлов для отправки. По умолчанию `None`.
- `api_key` (str, optional): Ключ API для аутентификации. По умолчанию `None`.
- `temperature` (float, optional): Температура для управления случайностью генерации. По умолчанию `None`.
- `max_tokens` (int, optional): Максимальное количество токенов в ответе. По умолчанию 4096.
- `top_k` (int, optional): Параметр top_k для управления генерацией. По умолчанию `None`.
- `top_p` (float, optional): Параметр top_p для управления генерацией. По умолчанию `None`.
- `stop` (list[str], optional): Список стоп-слов для остановки генерации. По умолчанию `None`.
- `stream` (bool, optional): Включить потоковую передачу данных. По умолчанию `False`.
- `headers` (dict, optional): Дополнительные заголовки для запроса. По умолчанию `None`.
- `impersonate` (str, optional): Имя пользователя для имитации. По умолчанию `None`.
- `tools` (Optional[list], optional): Список инструментов для использования. По умолчанию `None`.
- `extra_data` (dict, optional): Дополнительные данные для отправки в запросе. По умолчанию `{}`.
- `**kwargs`: Дополнительные аргументы.

**Возвращает**:
- `AsyncResult`: Асинхронный генератор для получения ответов от API.

**Вызывает исключения**:
- `MissingAuthError`: Если не указан ключ API.

**Как работает функция**:

```
A[Проверка API Key]
|
B[Если API Key отсутствует: MissingAuthError] - C[Если API Key присутствует: Обработка медиафайлов (если есть)]
|
D[Извлечение и объединение системных сообщений]
|
E[Инициализация StreamSession]
|
F[Формирование данных для POST-запроса]
|
G[POST-запрос к API Anthropic]
|
H[Обработка потоковых/непотоковых ответов]
|
I[Разбор чанков данных (потоковые ответы)]
|
J[Извлечение содержимого/информации (непотоковые ответы)]
|
K[ToolCalls]
|
L[Возврат асинхронного генератора]
```

**Примеры**:

```python
# Пример создания асинхронного генератора для получения ответа от API Anthropic
messages = [{"role": "user", "content": "Hello, how are you?"}]
async for message in Anthropic.create_async_generator(model="claude-3-opus-latest", messages=messages, api_key="YOUR_API_KEY", stream=True):
    print(message)
```

### `get_headers`

```python
    @classmethod
    def get_headers(cls, stream: bool, api_key: str = None, headers: dict = None) -> dict:
        """
        Формирует заголовки запроса для API Anthropic.

        Args:
            stream (bool): Указывает, является ли запрос потоковым.
            api_key (str, optional): Ключ API для аутентификации. По умолчанию `None`.
            headers (dict, optional): Дополнительные заголовки для запроса. По умолчанию `None`.

        Returns:
            dict: Словарь заголовков запроса.

        Как работает функция:
        1. Определяет значение заголовка "Accept" в зависимости от того, является ли запрос потоковым или нет.
        2. Добавляет заголовок "Content-Type" со значением "application/json".
        3. Добавляет заголовок "x-api-key" с ключом API, если он предоставлен.
        4. Добавляет заголовок "anthropic-version" с версией API Anthropic.
        5. Объединяет все заголовки в один словарь и возвращает его.
        """
```

**Назначение**: Формирование заголовков запроса для API Anthropic.

**Параметры**:
- `stream` (bool): Указывает, является ли запрос потоковым.
- `api_key` (str, optional): Ключ API для аутентификации. По умолчанию `None`.
- `headers` (dict, optional): Дополнительные заголовки для запроса. По умолчанию `None`.

**Возвращает**:
- `dict`: Словарь заголовков запроса.

**Как работает функция**:

```
A[Определение Accept: text/event-stream (stream=True) или application/json (stream=False)]
|
B[Добавление Content-Type: application/json]
|
C[Добавление x-api-key (если api_key предоставлен)]
|
D[Добавление anthropic-version: 2023-06-01]
|
E[Объединение всех заголовков в словарь]
|
F[Возврат словаря заголовков]
```

**Примеры**:

```python
# Пример получения заголовков для потокового запроса с использованием API-ключа
headers = Anthropic.get_headers(stream=True, api_key="YOUR_API_KEY")
print(headers)