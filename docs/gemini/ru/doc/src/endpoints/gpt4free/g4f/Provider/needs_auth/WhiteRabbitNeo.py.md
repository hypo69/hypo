# Модуль WhiteRabbitNeo

## Обзор

Модуль `WhiteRabbitNeo` предоставляет асинхронный генератор для взаимодействия с провайдером WhiteRabbitNeo. Он предназначен для обмена сообщениями, поддерживает историю сообщений и требует аутентификацию. Модуль использует `aiohttp` для асинхронных HTTP-запросов и предоставляет функциональность для получения ответов от API WhiteRabbitNeo.

## Подробней

Модуль `WhiteRabbitNeo` является частью проекта `hypotez` и предназначен для интеграции с сервисом WhiteRabbitNeo. Он обеспечивает асинхронное взаимодействие с API WhiteRabbitNeo, поддерживая передачу сообщений и получение ответов в режиме реального времени. Модуль требует аутентификации и использует файлы cookie для поддержания сессии.

## Классы

### `WhiteRabbitNeo`

**Описание**: Класс `WhiteRabbitNeo` является асинхронным провайдером генератора, который взаимодействует с API WhiteRabbitNeo.

**Наследует**:
- `AsyncGeneratorProvider`: Класс наследует функциональность асинхронного генератора от `AsyncGeneratorProvider`.

**Атрибуты**:
- `url` (str): URL-адрес сервиса WhiteRabbitNeo.
- `working` (bool): Указывает, работает ли провайдер в данный момент.
- `supports_message_history` (bool): Указывает, поддерживается ли история сообщений.
- `needs_auth` (bool): Указывает, требуется ли аутенентификация.

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
            model (str): Модель для использования.
            messages (Messages): Список сообщений для отправки.
            cookies (Cookies, optional): Cookie для аутентификации. Defaults to None.
            connector (BaseConnector, optional): Connector для асинхронных запросов. Defaults to None.
            proxy (str, optional): Proxy для использования. Defaults to None.
            **kwargs: Дополнительные аргументы.

        Returns:
            AsyncResult: Асинхронный генератор, возвращающий ответы от API WhiteRabbitNeo.
        """
```

**Назначение**: Функция `create_async_generator` создает и возвращает асинхронный генератор, который используется для взаимодействия с API WhiteRabbitNeo. Она отвечает за установку соединения, отправку запросов и получение ответов в режиме реального времени.

**Параметры**:
- `model` (str): Модель, используемая для генерации ответов.
- `messages` (Messages): Список сообщений, которые будут отправлены в API.
- `cookies` (Cookies, optional): Cookie для аутентификации. Если не указаны, используются значения по умолчанию. По умолчанию `None`.
- `connector` (BaseConnector, optional): Connector для асинхронных запросов. Если не указан, используется значение по умолчанию. По умолчанию `None`.
- `proxy` (str, optional): Proxy-сервер для использования при отправке запросов. Если не указан, proxy не используется. По умолчанию `None`.
- `**kwargs`: Дополнительные аргументы, которые могут быть переданы в функцию.

**Возвращает**:
- `AsyncResult`: Асинхронный генератор, возвращающий ответы от API WhiteRabbitNeo.

**Вызывает исключения**:
- `Exception`: В случае возникновения ошибок при выполнении запроса или обработке ответа.

**Как работает функция**:

1. **Инициализация**:
   - Проверяет наличие `cookies`. Если `cookies` не предоставлены, функция пытается получить их с домена `"www.whiterabbitneo.com"` с помощью функции `get_cookies`.
   - Определяет HTTP-заголовки, включая `User-Agent`, `Accept`, `Accept-Language`, `Content-Type` и другие.

2. **Создание сессии**:
   - Создает асинхронную сессию `ClientSession` с заданными заголовками, cookie и connector. Connector используется для управления соединениями, а cookie для аутентификации.

3. **Формирование данных**:
   - Формирует словарь `data`, который содержит сообщения (`messages`), случайный идентификатор (`id`), а также флаги `enhancePrompt` и `useFunctions`.

4. **Отправка запроса и обработка ответа**:
   - Отправляет POST-запрос к API WhiteRabbitNeo (`f"{cls.url}/api/chat"`) с использованием сформированных данных и proxy.
   - Использует `raise_for_status` для проверки статуса ответа и вызывает исключение в случае ошибки.
   - Итерируется по содержимому ответа (`response.content.iter_any()`) и декодирует каждый чанк данных, возвращая его через `yield`.

```
Инициализация -> Проверка Cookies -> Определение HTTP-заголовков
     ↓
Создание сессии ClientSession (headers, cookies, connector)
     ↓
Формирование данных (messages, id, enhancePrompt, useFunctions)
     ↓
Отправка POST-запроса к API (data, proxy)
     ↓
Проверка статуса ответа (raise_for_status)
     ↓
Итерация по содержимому ответа (response.content.iter_any()) -> Декодирование чанка данных (decode) -> yield chunk
     ↓
Конец
```

**Примеры**:

```python
# Пример вызова функции create_async_generator
messages = [{"role": "user", "content": "Hello, how are you?"}]
model = "default"

# Предположим, что cookies уже получены
cookies = {"sessionid": "example_session_id"}

# Вызов функции с cookies
async_generator = WhiteRabbitNeo.create_async_generator(model=model, messages=messages, cookies=cookies)

# Пример использования async generator
async for chunk in async_generator:
    print(chunk)
```
```python
# Пример вызова функции create_async_generator без cookies
messages = [{"role": "user", "content": "Как дела?"}]
model = "default"

# Вызов функции без cookies (cookies будут получены автоматически)
async_generator = WhiteRabbitNeo.create_async_generator(model=model, messages=messages)

# Пример использования async generator
async for chunk in async_generator:
    print(chunk)
```
```python
# Пример вызова функции create_async_generator c использованием proxy
messages = [{"role": "user", "content": "Tell me a joke."}]
model = "default"
proxy = "http://proxy.example.com:8080"

# Вызов функции с proxy
async_generator = WhiteRabbitNeo.create_async_generator(model=model, messages=messages, proxy=proxy)

# Пример использования async generator
async for chunk in async_generator:
    print(chunk)
```