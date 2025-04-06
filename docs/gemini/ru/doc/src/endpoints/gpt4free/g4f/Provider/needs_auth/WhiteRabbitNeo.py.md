# Модуль WhiteRabbitNeo.py

## Обзор

Модуль `WhiteRabbitNeo.py` предоставляет асинхронный интерфейс для взаимодействия с сервисом WhiteRabbitNeo. Он предназначен для генерации текста на основе предоставленных сообщений и поддерживает использование cookies для аутентификации. Этот модуль является частью проекта `hypotez` и предназначен для работы с различными поставщиками (providers) в асинхронном режиме.

## Подробнее

Модуль использует библиотеку `aiohttp` для выполнения асинхронных HTTP-запросов. Он создает асинхронный генератор, который отправляет запросы к API WhiteRabbitNeo и возвращает чанки сгенерированного текста.

## Классы

### `WhiteRabbitNeo`

**Описание**: Класс `WhiteRabbitNeo` является асинхронным провайдером, который взаимодействует с сервисом WhiteRabbitNeo.

**Наследует**:
- `AsyncGeneratorProvider`: Этот класс наследует функциональность асинхронного генератора от `AsyncGeneratorProvider`, позволяя асинхронно получать данные чанками.

**Атрибуты**:
- `url` (str): URL сервиса WhiteRabbitNeo (`"https://www.whiterabbitneo.com"`).
- `working` (bool): Флаг, указывающий, что провайдер находится в рабочем состоянии (`True`).
- `supports_message_history` (bool): Флаг, указывающий, что провайдер поддерживает историю сообщений (`True`).
- `needs_auth` (bool): Флаг, указывающий, что для работы с провайдером требуется аутентификация (`True`).

**Методы**:
- `create_async_generator()`: Создает асинхронный генератор для взаимодействия с API WhiteRabbitNeo.

## Функции

### `create_async_generator`

```python
@classmethod
async def create_async_generator(
    cls,
    model: str,
    messages: Messages,
    cookies: Cookies = None,
    connector: BaseConnector = None,
    proxy: str = None,
    **kwargs
) -> AsyncResult:
    """Создает асинхронный генератор для взаимодействия с API WhiteRabbitNeo.

    Args:
        model (str): Модель, используемая для генерации текста.
        messages (Messages): Список сообщений для отправки в API.
        cookies (Cookies, optional): Cookies для аутентификации. По умолчанию `None`.
        connector (BaseConnector, optional): Aiohttp connector. По умолчанию `None`.
        proxy (str, optional): Прокси-сервер для использования. По умолчанию `None`.
        **kwargs: Дополнительные параметры.

    Returns:
        AsyncResult: Асинхронный генератор, возвращающий чанки сгенерированного текста.

    Raises:
        Exception: Если возникает ошибка при выполнении запроса.

    """
```

**Назначение**: Создает асинхронный генератор для взаимодействия с API WhiteRabbitNeo.

**Параметры**:
- `cls` (class): Ссылка на класс `WhiteRabbitNeo`.
-   `model` (str): Модель, используемая для генерации текста.
-   `messages` (Messages): Список сообщений для отправки в API.
-   `cookies` (Cookies, optional): Cookies для аутентификации. По умолчанию `None`. Если `cookies` не предоставлены, используются cookies, полученные для домена `"www.whiterabbitneo.com"`.
-   `connector` (BaseConnector, optional): Aiohttp connector. По умолчанию `None`.
-   `proxy` (str, optional): Прокси-сервер для использования. По умолчанию `None`.
-   `**kwargs`: Дополнительные параметры.

**Возвращает**:
- `AsyncResult`: Асинхронный генератор, возвращающий чанки сгенерированного текста.

**Вызывает исключения**:
- `Exception`: Если возникает ошибка при выполнении запроса.

**Как работает функция**:

1.  **Инициализация**:
    - Функция `create_async_generator` является classmethod, предназначенным для создания асинхронного генератора, который будет взаимодействовать с API WhiteRabbitNeo.
    - Проверяется, предоставлены ли cookies. Если нет, используются cookies, полученные для домена `"www.whiterabbitneo.com"` с помощью функции `get_cookies`.
    - Определяются HTTP-заголовки, включая `User-Agent`, `Accept`, `Referer`, `Content-Type` и другие. Заголовки имитируют запрос от браузера Firefox.
    - Создается сессия `aiohttp.ClientSession` с заданными заголовками, cookies и коннектором (если предоставлен).

2.  **Формирование данных запроса**:
    - Создается словарь `data`, содержащий сообщения (`messages`), случайный идентификатор (`id`), флаги `enhancePrompt` и `useFunctions`.
    - Случайный идентификатор генерируется с помощью функции `get_random_string(6)`.

3.  **Выполнение POST-запроса**:
    - Выполняется POST-запрос к API WhiteRabbitNeo (`f"{cls.url}/api/chat"`) с использованием асинхронной сессии.
    - В теле запроса передаются данные в формате JSON, а также прокси-сервер (если указан).

4.  **Обработка ответа**:
    - Функция `raise_for_status` проверяет статус ответа и вызывает исключение в случае ошибки.
    - Асинхронно итерируется по чанкам содержимого ответа (`response.content.iter_any()`).
    - Каждый чанк декодируется в строку (с обработкой ошибок декодирования) и возвращается через `yield`, что делает функцию генератором.

5.  **Завершение**:
    - После завершения итерации по чанкам сессия `aiohttp.ClientSession` автоматически закрывается благодаря использованию `async with`.

**Внутренние функции**: Нет внутренних функций.

**Flowchart**:

```
    Cookies Check
    │
    │ (Cookies are provided?)
    │
    No───────────────────────────Yes
    │                               │
    │                               │
    Get Cookies from "www.whiterabbitneo.com"
    │
    │
    Create Headers
    │
    │
    Create ClientSession with Headers, Cookies, and Connector
    │
    │
    Create Request Data (messages, id, flags)
    │
    │
    POST Request to WhiteRabbitNeo API
    │
    │
    Check Response Status
    │
    │ (Status is OK?)
    │
    No───────────────────────────Yes
    │                               │
    │                               │
    Raise Exception                 Iterate over Response Chunks
    │                               │
    │                               Decode Chunk and Yield
    │                               │
    End of Function                 End of Iteration
```

**Примеры**:

```python
# Пример использования (требуется асинхронный контекст)
# from asyncio import run
# async def main():
#     messages = [{"role": "user", "content": "Hello, how are you?"}]
#     async for chunk in WhiteRabbitNeo.create_async_generator(model="default", messages=messages):
#         print(chunk, end="")

# run(main())
```

```python
# Пример использования с cookies и прокси (требуется асинхронный контекст)
# from asyncio import run
# async def main():
#     messages = [{"role": "user", "content": "Tell me a joke."}]
#     cookies = {"some_cookie": "some_value"}
#     proxy = "http://your_proxy:8080"
#     async for chunk in WhiteRabbitNeo.create_async_generator(model="default", messages=messages, cookies=cookies, proxy=proxy):
#         print(chunk, end="")

# run(main())
```