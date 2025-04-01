# Модуль для работы с провайдером You.com
=================================================

Модуль содержит класс `You`, который используется для взаимодействия с моделью You.com для генерации текста и изображений.

## Обзор

Модуль `You` предоставляет асинхронный генератор для обмена сообщениями с You.com, поддерживая различные модели, включая `gpt-4o-mini`, `dall-e` и другие. Он также включает функциональность для загрузки изображений и обработки ответов.

## Подробней

Модуль предназначен для интеграции с платформой You.com, обеспечивая возможность использования различных AI-моделей для генерации текста и изображений. Он включает в себя механизмы для управления cookies, загрузки файлов и обработки ответов от API You.com.

## Классы

### `You(AsyncGeneratorProvider, ProviderModelMixin)`

**Описание**: Класс `You` предоставляет интерфейс для взаимодействия с сервисом You.com.

**Наследует**:
- `AsyncGeneratorProvider`: Обеспечивает асинхронную генерацию ответов.
- `ProviderModelMixin`: Предоставляет функциональность для работы с моделями.

**Атрибуты**:
- `label` (str): Метка провайдера ("You.com").
- `url` (str): URL сервиса You.com ("https://you.com").
- `working` (bool): Указывает, работает ли провайдер (True).
- `default_model` (str): Модель, используемая по умолчанию ("gpt-4o-mini").
- `default_vision_model` (str): Модель для работы с изображениями по умолчанию ("agent").
- `image_models` (List[str]): Список моделей для генерации изображений (["dall-e"]).
- `models` (List[str]): Список поддерживаемых моделей, включая текстовые и графические модели.
- `_cookies` (Optional[Cookies]): Cookies для аутентификации на сервисе You.com.
- `_cookies_used` (int): Счетчик использования cookies.
- `_telemetry_ids` (List[str]): Список идентификаторов для телеметрии.

**Методы**:
- `create_async_generator()`: Создает асинхронный генератор для взаимодействия с You.com.
- `upload_file()`: Загружает файл на сервер You.com.

### `create_async_generator`

```python
@classmethod
async def create_async_generator(
    cls,
    model: str,
    messages: Messages,
    stream: bool = True,
    image: ImageType = None,
    image_name: str = None,
    proxy: str = None,
    timeout: int = 240,
    chat_mode: str = "default",
    cookies: Cookies = None,
    **kwargs,
) -> AsyncResult:
    """
    Создает асинхронный генератор для взаимодействия с You.com.

    Args:
        cls (Type[You]): Класс You.
        model (str): Модель для использования (например, "gpt-4o-mini", "dall-e").
        messages (Messages): Список сообщений для отправки.
        stream (bool): Включить потоковую передачу ответов. По умолчанию `True`.
        image (ImageType): Изображение для отправки. По умолчанию `None`.
        image_name (str): Имя файла изображения. По умолчанию `None`.
        proxy (str): Прокси-сервер для использования. По умолчанию `None`.
        timeout (int): Время ожидания запроса в секундах. По умолчанию 240.
        chat_mode (str): Режим чата ("default", "agent", "create", "custom"). По умолчанию "default".
        cookies (Cookies): Cookies для аутентификации. По умолчанию `None`.
        **kwargs: Дополнительные аргументы.

    Returns:
        AsyncResult: Асинхронный генератор для получения ответов.

    Raises:
        ResponseError: Если возникает ошибка при получении ответа от сервера.

    """
```

**Назначение**: Создает асинхронный генератор для отправки сообщений в You.com и получения ответов в асинхронном режиме.

**Параметры**:
- `cls` (Type[You]): Класс You.
- `model` (str): Определяет используемую модель, например, "gpt-4o-mini" или "dall-e".
- `messages (Messages)`: Список сообщений для отправки в You.com.
- `stream` (bool, optional): Если `True`, ответы передаются потоком. По умолчанию `True`.
- `image` (ImageType, optional): Изображение для отправки. По умолчанию `None`.
- `image_name` (str, optional): Имя файла изображения. По умолчанию `None`.
- `proxy` (str, optional): Прокси-сервер для использования. По умолчанию `None`.
- `timeout` (int, optional): Максимальное время ожидания ответа в секундах. По умолчанию `240`.
- `chat_mode` (str, optional): Режим чата, который может быть "default", "agent", "create" или "custom". По умолчанию "default".
- `cookies` (Cookies, optional): Cookies для аутентификации. По умолчанию `None`.
- `**kwargs`: Дополнительные параметры, которые могут быть переданы.

**Возвращает**:
- `AsyncResult`: Асинхронный генератор, который выдает ответы от You.com.

**Вызывает исключения**:
- `ResponseError`: Если при получении ответа от сервера возникает ошибка.

**Как работает функция**:

1. **Определение режима чата**: Функция определяет режим чата в зависимости от наличия изображения или выбранной модели. Если передано изображение или модель vision, режим устанавливается в "agent".
2. **Выбор модели**: Если модель не указана или равна `default_model`, ничего не происходит. Для моделей, начинающихся с "dall-e", режим чата устанавливается в "create", и берется последнее сообщение из списка. Для других моделей режим устанавливается в "custom", и модель форматируется.
3. **Получение cookies**: Если cookies не переданы и режим чата не "default", функция пытается получить cookies из домена ".you.com". Если это не удается, запускается браузер без драйвера для получения cookies.
4. **Создание сессии**: Создается асинхронная сессия с использованием `StreamSession` для выполнения запросов.
5. **Загрузка файла**: Если передано изображение, оно загружается на сервер с помощью метода `upload_file`.
6. **Формирование данных**: Формируются данные для отправки в API, включая сообщения, режим чата и выбранную модель.
7. **Выполнение запроса**: Выполняется GET-запрос к API `streamingSearch` с использованием сформированных данных и заголовков.
8. **Обработка ответов**: Функция итерирует по строкам ответа, обрабатывая события "error", "youChatUpdate" и "youChatToken". В случае ошибки выбрасывается исключение `ResponseError`.
9. **Генерация ответов**: В зависимости от события и режима чата, функция генерирует текстовые или графические ответы.

**Внутренние функции**: Нет

**ASCII flowchart**:

```
    Определение режима чата (image, model)
    │
    └──► Выбор модели (default, dall-e, custom)
    │
    └──► Получение cookies (from .you.com or nodriver)
    │
    └──► Создание сессии (StreamSession)
    │
    └──► Загрузка файла (upload_file, if image)
    │
    └──► Формирование данных (messages, chat_mode, model)
    │
    └──► Выполнение запроса (GET streamingSearch)
    │
    └──► Обработка ответов (events: error, youChatUpdate, youChatToken)
    │
    └──► Генерация ответов (text or image)
```

**Примеры**:

```python
# Пример использования с текстовой моделью
messages = [{"role": "user", "content": "Привет!"}]
async for message in You.create_async_generator(model="gpt-4o-mini", messages=messages):
    print(message)

# Пример использования с моделью для генерации изображений
messages = [{"role": "user", "content": "Нарисуй котика."}]
async for message in You.create_async_generator(model="dall-e", messages=messages):
    print(message)
```

### `upload_file`

```python
@classmethod
async def upload_file(cls, client: StreamSession, cookies: Cookies, file: bytes, filename: str = None) -> dict:
    """
    Загружает файл на сервер You.com.

    Args:
        cls (Type[You]): Класс You.
        client (StreamSession): Асинхронная сессия для выполнения запросов.
        cookies (Cookies): Cookies для аутентификации.
        file (bytes): Содержимое файла в байтах.
        filename (str): Имя файла. По умолчанию `None`.

    Returns:
        dict: Информация о загруженном файле.

    Raises:
        ResponseError: Если возникает ошибка при загрузке файла.

    """
```

**Назначение**: Загружает файл (обычно изображение) на сервер You.com и возвращает информацию о загруженном файле.

**Параметры**:
- `cls` (Type[You]): Класс You.
- `client` (StreamSession): Асинхронная сессия для выполнения HTTP-запросов.
- `cookies` (Cookies): Cookies для аутентификации на сервере.
- `file` (bytes): Содержимое файла, представленное в виде байтов.
- `filename` (str, optional): Имя файла. Если не указано, имя генерируется автоматически. По умолчанию `None`.

**Возвращает**:
- `dict`: Словарь с информацией о загруженном файле, включая имя файла, размер и другие метаданные.

**Вызывает исключения**:
- `ResponseError`: Если при загрузке файла возникает ошибка.

**Как работает функция**:

1. **Получение nonce**: Функция получает nonce (одноразовый токен) с сервера You.com, который используется для защиты от CSRF-атак.
2. **Формирование данных формы**: Создается объект FormData, в который добавляется файл. Если имя файла не указано, оно генерируется автоматически на основе типа содержимого файла.
3. **Отправка файла**: Файл отправляется на сервер You.com с использованием POST-запроса. В заголовках запроса передается nonce.
4. **Обработка ответа**: Функция обрабатывает ответ от сервера, преобразует его в JSON и возвращает словарь с информацией о загруженном файле.

**Внутренние функции**: Нет

**ASCII flowchart**:

```
    Получение nonce (GET api/get_nonce)
    │
    └──► Формирование данных формы (FormData)
    │
    └──► Определение имени файла (if filename is None)
    │
    └──► Отправка файла (POST api/upload)
    │
    └──► Обработка ответа (JSON)
    │
    └──► Возврат информации о файле (dict)
```

**Примеры**:

```python
# Пример загрузки файла
import aiohttp
from src.cookies import Cookies

async def upload_example():
    # Замените на реальные значения
    file_path = "path/to/your/image.jpg"
    cookies = {"afUserId": "some_user_id"}

    async with aiohttp.ClientSession() as session:
        with open(file_path, "rb") as f:
            file_data = f.read()

        result = await You.upload_file(session, cookies, file_data, filename="my_image.jpg")
        print(result)

# Запуск примера (в асинхронной среде)
# import asyncio
# asyncio.run(upload_example())