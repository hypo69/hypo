# Модуль `Liaobots.py`

## Обзор

Модуль предоставляет класс `Liaobots`, который является асинхронным генератором для взаимодействия с моделями Liaobots.  
Он поддерживает сохранение истории сообщений и использование системных сообщений. 
Модуль использует API `liaobots.site` для получения ответов от различных AI-моделей, таких как `GPT-4o`, `Claude-3.5-Sonnet`, `DeepSeek-R1` и `Gemini-2.0-Flash`.

## Подробнее

Этот модуль интегрируется с сервисом `liaobots.site`, который предоставляет доступ к различным моделям ИИ. Он использует асинхронные запросы для взаимодействия с API и возвращает результаты в виде асинхронного генератора. Класс `Liaobots` поддерживает различные модели, предоставляемые `liaobots.site`, и имеет механизмы для автоматической аутентификации и обработки ошибок. Он также предоставляет возможность использования прокси-серверов и пользовательских коннекторов для `aiohttp`.

## Классы

### `Liaobots`

**Описание**: Класс `Liaobots` является асинхронным генератором провайдера и реализует методы для взаимодействия с API `liaobots.site`.
Он поддерживает различные модели, такие как `GPT-4o`, `Claude-3.5-Sonnet`, `DeepSeek-R1` и `Gemini-2.0-Flash`.

**Наследует**:
- `AsyncGeneratorProvider`: Обеспечивает асинхронную генерацию ответов.
- `ProviderModelMixin`: Предоставляет общие методы для работы с моделями провайдера.

**Атрибуты**:
- `url` (str): URL сервиса `liaobots.site`.
- `working` (bool): Указывает, работает ли провайдер.
- `supports_message_history` (bool): Указывает, поддерживает ли провайдер историю сообщений.
- `supports_system_message` (bool): Указывает, поддерживает ли провайдер системные сообщения.
- `default_model` (str): Модель, используемая по умолчанию (`gpt-4o-2024-08-06`).
- `models` (list): Список поддерживаемых моделей.
- `model_aliases` (dict): Словарь псевдонимов моделей для упрощения использования.
- `_auth_code` (str): Код аутентификации для доступа к API.
- `_cookie_jar` (aiohttp.CookieJar): Объект для хранения и управления куки.

**Методы**:
- `is_supported(model: str) -> bool`: Проверяет, поддерживается ли указанная модель.
- `create_async_generator(model: str, messages: Messages, proxy: str | None = None, connector: BaseConnector | None = None, **kwargs) -> AsyncResult`: Создает асинхронный генератор для получения ответов от API.
- `initialize_auth_code(session: ClientSession) -> None`: Инициализирует код аутентификации, выполняя необходимые запросы для входа в систему.
- `ensure_auth_code(session: ClientSession) -> None`: Обеспечивает инициализацию кода аутентификации, если он еще не был инициализирован.

## Функции

### `is_supported(cls, model: str) -> bool`

```python
@classmethod
def is_supported(cls, model: str) -> bool:
    """
    Check if the given model is supported.
    """
    return model in models or model in cls.model_aliases
```

**Назначение**: Проверяет, поддерживается ли указанная модель.

**Параметры**:
- `cls` (type[Liaobots]): Ссылка на класс `Liaobots`.
- `model` (str): Имя модели для проверки.

**Возвращает**:
- `bool`: `True`, если модель поддерживается, иначе `False`.

**Как работает функция**:

1. Функция `is_supported` принимает имя модели в качестве аргумента.
2. Проверяет, есть ли указанная модель в списке поддерживаемых моделей (`models`) или в словаре псевдонимов моделей (`model_aliases`).
3. Возвращает `True`, если модель найдена в одном из этих мест, и `False` в противном случае.

**Примеры**:

```python
# Пример использования функции is_supported
Liaobots.is_supported("gpt-4o-2024-08-06")  # Возвращает True
Liaobots.is_supported("unsupported-model")  # Возвращает False
```

### `create_async_generator(cls, model: str, messages: Messages, proxy: str | None = None, connector: BaseConnector | None = None, **kwargs) -> AsyncResult`

```python
@classmethod
async def create_async_generator(
    cls,
    model: str,
    messages: Messages,
    proxy: str | None = None,
    connector: BaseConnector | None = None,
    **kwargs
) -> AsyncResult:
    """
    Создает асинхронный генератор для получения ответов от API.
    """
    ...
```

**Назначение**: Создает асинхронный генератор для получения ответов от API `liaobots.site`.

**Параметры**:
- `cls` (type[Liaobots]): Ссылка на класс `Liaobots`.
- `model` (str): Имя модели для использования.
- `messages` (Messages): Список сообщений для отправки в API.
- `proxy` (str | None, optional): URL прокси-сервера для использования. По умолчанию `None`.
- `connector` (BaseConnector | None, optional): Пользовательский коннектор `aiohttp`. По умолчанию `None`.
- `**kwargs`: Дополнительные аргументы, такие как `system_message`.

**Возвращает**:
- `AsyncResult`: Асинхронный генератор, возвращающий ответы от API.

**Вызывает исключения**:
- `RuntimeError`: Если не удалось получить код аутентификации.

**Как работает функция**:

1. **Подготовка заголовков**: Функция `create_async_generator` устанавливает необходимые HTTP-заголовки, включая `referer`, `origin` и `user-agent`.
2. **Создание сессии `aiohttp`**: Создается асинхронная сессия `aiohttp` с настроенными заголовками, куками и коннектором (если указан).
3. **Подготовка данных для запроса**: Формируются данные для отправки в API, включая `conversationId`, `model`, `messages`, `key` и `prompt` (системное сообщение).
4. **Аутентификация**:
   - Если `_auth_code` отсутствует, выполняется запрос к `https://liaobots.work/recaptcha/api/login` для получения кода аутентификации.
   - Затем выполняется запрос к `https://liaobots.work/api/user` для обновления `_auth_code` и получения кук.
5. **Отправка запроса и получение ответа**:
   - Отправляется `POST`-запрос к `https://liaobots.work/api/chat` с данными и заголовком `x-auth-code`.
   - Полученный ответ обрабатывается построчно, и каждая строка, начинающаяся с `data: `, преобразуется в JSON и извлекается содержимое (`content`).
   - Содержимое возвращается как часть асинхронного генератора.
6. **Обработка ошибок**:
   - Если происходит ошибка, выполняется повторная попытка аутентификации с использованием статического `authcode`.

**Внутренние функции**:
- Отсутствуют

**ASCII flowchart**:

```
+-----------------------------------------------------+
|                create_async_generator               |
+-----------------------------------------------------+
| Заголовки и сессия aiohttp                         |
+-----------------------+-----------------------------+
                        |
                        V
+-----------------------+-----------------------------+
|        Подготовка данных для запроса               |
+-----------------------+-----------------------------+
                        |
                        V
+-----------------------+-----------------------------+
|      Проверка наличия _auth_code                   |
+-----------------------+-----------------------------+
          | ДА                 | НЕТ
          |                    |
          V                    V
+-----------------------+-----------------------------+
|   Запрос логина для    |  Пропуск запроса логина   |
|   получения _auth_code   |                           |
+-----------------------+-----------------------------+
          |
          V
+-----------------------+-----------------------------+
| Отправка POST-запроса  |
| к /api/chat с данными |
+-----------------------+-----------------------------+
          |
          V
+-----------------------+-----------------------------+
|   Обработка ответа и   |
|   генерация контента   |
+-----------------------+
```

**Примеры**:

```python
# Пример использования функции create_async_generator
messages = [{"role": "user", "content": "Hello, world!"}]
async def print_response():
    async for response in Liaobots.create_async_generator(model="gpt-4o-2024-08-06", messages=messages):
        print(response)

# Запуск асинхронной функции
import asyncio
asyncio.run(print_response())
```

### `initialize_auth_code(cls, session: ClientSession) -> None`

```python
@classmethod
async def initialize_auth_code(cls, session: ClientSession) -> None:
    """
    Initialize the auth code by making the necessary login requests.
    """
    ...
```

**Назначение**: Инициализирует код аутентификации, выполняя необходимые запросы для входа в систему.

**Параметры**:
- `cls` (type[Liaobots]): Ссылка на класс `Liaobots`.
- `session` (ClientSession): Асинхронная сессия `aiohttp` для выполнения запросов.

**Как работает функция**:

1. Функция отправляет POST-запрос к `https://liaobots.work/api/user` с фиксированным `authcode` ("pTIQr4FTnVRfr").
2. Получает ответ в формате JSON и извлекает значение `authCode`, которое присваивается атрибуту `_auth_code` класса.
3. Если `authCode` отсутствует в ответе, вызывается исключение `RuntimeError` с сообщением "Empty auth code".
4. Обновляет `cookie_jar` сессии, чтобы сохранить полученные куки.

**Внутренние функции**:
- Отсутствуют

**ASCII flowchart**:

```
+-----------------------------------------------------+
|              initialize_auth_code                   |
+-----------------------------------------------------+
|  Отправка POST-запроса к /api/user с authcode       |
+-----------------------+-----------------------------+
                        |
                        V
+-----------------------+-----------------------------+
|   Извлечение authCode из ответа JSON               |
+-----------------------+-----------------------------+
                        |
                        V
+-----------------------+-----------------------------+
|    Проверка наличия authCode в ответе               |
+-----------------------+-----------------------------+
          | ДА                 | НЕТ
          |                    |
          V                    V
+-----------------------+-----------------------------+
|   Присвоение authCode  |  Вызов исключения RuntimeError |
|  и обновление кук      |  ("Empty auth code")          |
+-----------------------+-----------------------------+
```

**Примеры**:

```python
# Пример использования функции initialize_auth_code
import asyncio
from aiohttp import ClientSession

async def initialize():
    async with ClientSession() as session:
        await Liaobots.initialize_auth_code(session)
        print(Liaobots._auth_code)

asyncio.run(initialize())
```

### `ensure_auth_code(cls, session: ClientSession) -> None`

```python
@classmethod
async def ensure_auth_code(cls, session: ClientSession) -> None:
    """
    Ensure the auth code is initialized, and if not, perform the initialization.
    """
    if not cls._auth_code:
        await cls.initialize_auth_code(session)
```

**Назначение**: Обеспечивает инициализацию кода аутентификации, если он еще не был инициализирован.

**Параметры**:
- `cls` (type[Liaobots]): Ссылка на класс `Liaobots`.
- `session` (ClientSession): Асинхронная сессия `aiohttp` для выполнения запросов.

**Как работает функция**:

1. Функция проверяет, инициализирован ли атрибут `_auth_code`.
2. Если `_auth_code` не инициализирован (пустая строка), вызывается функция `initialize_auth_code` для его инициализации.

**Внутренние функции**:
- Отсутствуют

**ASCII flowchart**:

```
+-----------------------------------------------------+
|               ensure_auth_code                      |
+-----------------------------------------------------+
|          Проверка наличия _auth_code               |
+-----------------------+-----------------------------+
          | ДА                 | НЕТ
          |                    |
          V                    V
+-----------------------+-----------------------------+
|       Код выполнен     |  Вызов initialize_auth_code  |
+-----------------------+-----------------------------+
```

**Примеры**:

```python
# Пример использования функции ensure_auth_code
import asyncio
from aiohttp import ClientSession

async def ensure():
    async with ClientSession() as session:
        await Liaobots.ensure_auth_code(session)
        print(Liaobots._auth_code)

asyncio.run(ensure())