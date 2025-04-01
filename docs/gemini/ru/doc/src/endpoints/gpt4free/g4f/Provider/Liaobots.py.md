# Модуль для работы с провайдером Liaobots
================================================

Модуль содержит класс `Liaobots`, который используется для взаимодействия с API Liaobots для генерации текста.
Он поддерживает различные модели, включая Claude, DeepSeek, Gemini и GPT, и обеспечивает асинхронную генерацию текста.

## Обзор

Модуль `Liaobots` предоставляет класс `Liaobots`, который является асинхронным генераторным провайдером и миксином для моделей провайдеров.
Он использует API Liaobots для генерации текста на основе предоставленных сообщений и параметров модели.
Модуль поддерживает различные модели, включая Claude, DeepSeek, Gemini и GPT.
Он также обеспечивает поддержку истории сообщений и системных сообщений.

## Подробнее

Этот модуль предназначен для интеграции с API Liaobots, позволяя пользователям использовать различные модели искусственного интеллекта для генерации текста.
Он обрабатывает аутентификацию, создание сессий и отправку запросов к API Liaobots.
Модуль также обеспечивает обработку ошибок и извлечение контента из ответов API.

## Содержание

- [Классы](#классы)
    - [Liaobots](#liaobots)
- [Функции](#функции)
    - [is_supported](#is_supported)
    - [create_async_generator](#create_async_generator)
    - [initialize_auth_code](#initialize_auth_code)
    - [ensure_auth_code](#ensure_auth_code)

## Классы

### `Liaobots`

**Описание**: Класс `Liaobots` является асинхронным генераторным провайдером и миксином для моделей провайдеров.
Он использует API Liaobots для генерации текста на основе предоставленных сообщений и параметров модели.

**Наследует**:
- `AsyncGeneratorProvider`: Обеспечивает асинхронную генерацию данных.
- `ProviderModelMixin`: Предоставляет функциональность для работы с моделями провайдеров.

**Атрибуты**:
- `url` (str): URL-адрес сервиса Liaobots.
- `working` (bool): Указывает, работает ли провайдер в данный момент.
- `supports_message_history` (bool): Указывает, поддерживает ли провайдер историю сообщений.
- `supports_system_message` (bool): Указывает, поддерживает ли провайдер системные сообщения.
- `default_model` (str): Модель, используемая по умолчанию (gpt-4o-2024-08-06).
- `models` (list[str]): Список поддерживаемых моделей.
- `model_aliases` (dict[str, str]): Псевдонимы моделей для удобства использования.
- `_auth_code` (str): Код аутентификации для доступа к API Liaobots.
- `_cookie_jar` (aiohttp.CookieJar): Cookie Jar для хранения cookie сессии.

**Методы**:
- `is_supported(model: str) -> bool`: Проверяет, поддерживается ли указанная модель.
- `create_async_generator(model: str, messages: Messages, proxy: str = None, connector: BaseConnector = None, **kwargs) -> AsyncResult`: Создает асинхронный генератор для генерации текста.
- `initialize_auth_code(session: ClientSession) -> None`: Инициализирует код аутентификации, выполняя необходимые запросы для входа в систему.
- `ensure_auth_code(session: ClientSession) -> None`: Проверяет, инициализирован ли код аутентификации, и инициализирует его, если это необходимо.

## Функции

### `is_supported`

```python
@classmethod
def is_supported(cls, model: str) -> bool:
    """
    Check if the given model is supported.
    """
    return model in models or model in cls.model_aliases
```

**Назначение**: Проверяет, поддерживается ли указанная модель провайдером `Liaobots`.

**Параметры**:
- `model` (str): Имя модели для проверки.

**Возвращает**:
- `bool`: `True`, если модель поддерживается, иначе `False`.

**Как работает функция**:
1. Функция принимает имя модели `model` в качестве аргумента.
2. Проверяет, есть ли модель в словаре `models` или в словаре `model_aliases` класса `Liaobots`.
3. Возвращает `True`, если модель найдена в одном из этих словарей, и `False` в противном случае.

```
Проверка модели
   ↓
Модель в models? → Да: Возврат True
   ↓ Нет
Модель в model_aliases? → Да: Возврат True
   ↓ Нет
Возврат False
```

**Примеры**:
```python
# Пример 1: Поддерживаемая модель
Liaobots.is_supported("gpt-4o-2024-08-06")  # Возвращает True

# Пример 2: Модель с псевдонимом
Liaobots.is_supported("gpt-4o")  # Возвращает True, так как "gpt-4o" - это псевдоним для "gpt-4o-2024-08-06"

# Пример 3: Неподдерживаемая модель
Liaobots.is_supported("unknown-model")  # Возвращает False
```

### `create_async_generator`

```python
@classmethod
async def create_async_generator(
    cls,
    model: str,
    messages: Messages,
    proxy: str = None,
    connector: BaseConnector = None,
    **kwargs
) -> AsyncResult:
    """
    Создает асинхронный генератор для генерации текста.
    """
    ...
```

**Назначение**: Создает асинхронный генератор для генерации текста с использованием API Liaobots.

**Параметры**:
- `model` (str): Имя модели для использования.
- `messages` (Messages): Список сообщений для отправки в API.
- `proxy` (str, optional): URL прокси-сервера. По умолчанию `None`.
- `connector` (BaseConnector, optional): Объект коннектора aiohttp. По умолчанию `None`.
- `**kwargs`: Дополнительные параметры, такие как `system_message`.

**Возвращает**:
- `AsyncResult`: Асинхронный генератор, который выдает сгенерированный текст.

**Как работает функция**:
1. Функция принимает имя модели, список сообщений и другие параметры.
2. Получает фактическое имя модели, используя метод `get_model`.
3. Создает заголовки для HTTP-запросов, включая Referer и User-Agent.
4. Создает сессию `aiohttp.ClientSession` с заданными заголовками, Cookie Jar и коннектором.
5. Формирует данные для отправки в API, включая идентификатор разговора, модель, сообщения, ключ и системное сообщение.
6. Пытается получить код аутентификации, отправляя POST-запрос к `https://liaobots.work/recaptcha/api/login`.
7. Отправляет POST-запрос к `https://liaobots.work/api/user` для получения кода аутентификации.
8. Отправляет POST-запрос к `https://liaobots.work/api/chat` с данными и заголовком `x-auth-code` для получения сгенерированного текста.
9. Итерирует по строкам в ответе и извлекает содержимое из строк, начинающихся с `data: `.
10. В случае ошибки повторяет шаги 7-9, используя другой код аутентификации.

```
Получение параметров
   ↓
Получение имени модели
   ↓
Создание заголовков
   ↓
Создание сессии aiohttp
   ↓
Формирование данных для запроса
   ↓
Попытка получения кода аутентификации
   ↓
Отправка запроса к /api/user
   ↓
Отправка запроса к /api/chat
   ↓
Извлечение содержимого из ответа
   ↓
Обработка ошибок и повторная попытка
   ↓
Возврат асинхронного генератора
```

**Примеры**:

```python
# Пример 1: Создание асинхронного генератора с моделью и сообщениями
messages = [{"role": "user", "content": "Hello, how are you?"}]
async_generator = Liaobots.create_async_generator(model="gpt-4o-2024-08-06", messages=messages)

# Пример 2: Создание асинхронного генератора с прокси и системным сообщением
messages = [{"role": "user", "content": "Translate to French: Hello"}]
async_generator = Liaobots.create_async_generator(
    model="gpt-4o-2024-08-06", messages=messages, proxy="http://proxy.example.com", system_message="You are a translator."
)
```

### `initialize_auth_code`

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
- `session` (ClientSession): Сессия `aiohttp.ClientSession` для выполнения запросов.

**Возвращает**:
- `None`

**Как работает функция**:
1. Функция принимает сессию `aiohttp.ClientSession` в качестве аргумента.
2. Отправляет POST-запрос к `https://liaobots.work/api/user` с кодом аутентификации `"pTIQr4FTnVRfr"`.
3. Извлекает код аутентификации из ответа и сохраняет его в атрибуте `_auth_code` класса `Liaobots`.
4. Сохраняет Cookie Jar из сессии в атрибуте `_cookie_jar` класса `Liaobots`.
5. Если код аутентификации не получен, вызывает исключение `RuntimeError`.

```
Получение сессии
   ↓
Отправка запроса к /api/user
   ↓
Извлечение кода аутентификации из ответа
   ↓
Сохранение кода аутентификации в атрибуте _auth_code
   ↓
Сохранение Cookie Jar в атрибуте _cookie_jar
   ↓
Проверка наличия кода аутентификации
   ↓
Вызов исключения, если код аутентификации отсутствует
```

**Примеры**:
```python
# Пример: Инициализация кода аутентификации с использованием сессии
import aiohttp

async def example():
    async with aiohttp.ClientSession() as session:
        await Liaobots.initialize_auth_code(session)
        print(f"Auth code initialized: {Liaobots._auth_code}")

import asyncio
asyncio.run(example())
```

### `ensure_auth_code`

```python
@classmethod
async def ensure_auth_code(cls, session: ClientSession) -> None:
    """
    Ensure the auth code is initialized, and if not, perform the initialization.
    """
    ...
```

**Назначение**: Проверяет, инициализирован ли код аутентификации, и инициализирует его, если это необходимо.

**Параметры**:
- `session` (ClientSession): Сессия `aiohttp.ClientSession` для выполнения запросов.

**Возвращает**:
- `None`

**Как работает функция**:
1. Функция принимает сессию `aiohttp.ClientSession` в качестве аргумента.
2. Проверяет, инициализирован ли код аутентификации (`cls._auth_code`).
3. Если код аутентификации не инициализирован, вызывает метод `initialize_auth_code` для его инициализации.

```
Получение сессии
   ↓
Проверка, инициализирован ли код аутентификации
   ↓
Код аутентификации не инициализирован? → Да: Вызов initialize_auth_code
   ↓ Нет
Завершение
```

**Примеры**:
```python
# Пример: Обеспечение инициализации кода аутентификации с использованием сессии
import aiohttp

async def example():
    async with aiohttp.ClientSession() as session:
        await Liaobots.ensure_auth_code(session)
        print(f"Auth code ensured: {Liaobots._auth_code}")

import asyncio
asyncio.run(example())