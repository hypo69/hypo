# Модуль `Gemini`

## Обзор

Модуль `Gemini` предоставляет асинхронный генератор для взаимодействия с моделью Google Gemini. Он включает в себя функциональность для аутентификации, обновления cookies, загрузки изображений и генерации текста на основе предоставленных сообщений.

## Подробнее

Модуль предназначен для интеграции с другими частями проекта `hypotez`, обеспечивая возможность использования модели Gemini для обработки текста и изображений. Он использует асинхронные запросы для обеспечения высокой производительности и включает в себя механизмы для автоматического обновления cookies для поддержания активной сессии.

## Классы

### `Gemini`

**Описание**: Класс `Gemini` предоставляет методы для взаимодействия с моделью Google Gemini, включая аутентификацию, обновление cookies, загрузку изображений и генерацию текста.

**Наследует**: `AsyncGeneratorProvider`, `ProviderModelMixin`

**Атрибуты**:

- `label` (str): Метка провайдера ("Google Gemini").
- `url` (str): URL для доступа к Gemini ("https://gemini.google.com").
- `needs_auth` (bool): Флаг, указывающий на необходимость аутентификации (True).
- `working` (bool): Флаг, указывающий на работоспособность провайдера (True).
- `use_nodriver` (bool): Флаг, указывающий на использование nodriver (True).
- `default_model` (str): Модель по умолчанию (пустая строка).
- `default_image_model` (str): Модель для обработки изображений по умолчанию (пустая строка).
- `default_vision_model` (str): Модель для обработки изображений по умолчанию (пустая строка).
- `image_models` (List[str]): Список моделей для обработки изображений.
- `models` (List[str]): Список поддерживаемых моделей.
- `model_aliases` (Dict[str, str]): Алиасы моделей.
- `synthesize_content_type` (str): Тип контента для синтеза речи ("audio/vnd.wav").
- `_cookies` (Cookies): Cookies для аутентификации.
- `_snlm0e` (str): Токен для аутентификации.
- `_sid` (str): SID для аутентификации.
- `auto_refresh` (bool): Флаг автоматического обновления cookies (True).
- `refresh_interval` (int): Интервал обновления cookies в секундах (540).
- `rotate_tasks` (Dict[str, asyncio.Task]): Словарь задач для ротации cookies.

**Методы**:

- `nodriver_login(proxy: str = None) -> AsyncIterator[str]`: Асинхронный генератор для выполнения входа в систему с использованием nodriver.
- `start_auto_refresh(proxy: str = None) -> None`: Запускает фоновую задачу для автоматического обновления cookies.
- `create_async_generator(model: str, messages: Messages, proxy: str = None, cookies: Cookies = None, connector: BaseConnector = None, media: MediaListType = None, return_conversation: bool = False, conversation: Conversation = None, language: str = "en", **kwargs) -> AsyncResult`: Создает асинхронный генератор для взаимодействия с моделью Gemini.
- `synthesize(params: dict, proxy: str = None) -> AsyncIterator[bytes]`: Синтезирует речь на основе предоставленного текста.
- `build_request(prompt: str, language: str, conversation: Conversation = None, uploads: list[list[str, str]] = None, tools: list[list[str]] = []) -> list`: Строит запрос к модели Gemini.
- `upload_images(connector: BaseConnector, media: MediaListType) -> list`: Загружает изображения на сервер Gemini.
- `fetch_snlm0e(session: ClientSession, cookies: Cookies) -> None`: Извлекает токен `SNlM0e` из cookies.

### `Conversation`

**Описание**: Класс `Conversation` представляет собой JSON-совместимый объект разговора, используемый для хранения и передачи информации о текущем взаимодействии с моделью Gemini.

**Наследует**: `JsonConversation`

**Атрибуты**:

- `conversation_id` (str): Идентификатор разговора.
- `response_id` (str): Идентификатор ответа.
- `choice_id` (str): Идентификатор выбора.
- `model` (str): Модель, используемая в разговоре.

**Методы**:

- `__init__(conversation_id: str, response_id: str, choice_id: str, model: str) -> None`: Инициализирует объект разговора.

## Функции

### `nodriver_login`

```python
@classmethod
async def nodriver_login(cls, proxy: str = None) -> AsyncIterator[str]:
    """Асинхронный генератор для выполнения входа в систему с использованием nodriver.

    Args:
        proxy (str, optional): Прокси-сервер для использования. По умолчанию None.

    Yields:
        AsyncIterator[str]: Части ответа сервера.

    Raises:
        ImportError: Если модуль `nodriver` не установлен.

    Как работает функция:
    1. Проверяет, установлен ли модуль `nodriver`. Если нет, функция завершается.
    2. Получает экземпляр браузера и функцию остановки браузера с помощью `get_nodriver`.
    3. Пытается получить URL для входа из переменной окружения `G4F_LOGIN_URL` и возвращает его в виде `RequestLogin`, если он присутствует.
    4. Переходит на страницу `f"{cls.url}/app"` в браузере.
    5. Выбирает текстовое поле `div.ql-editor.textarea` и ждет 240мс.
    6. Получает cookies из браузера для домена `cls.url`.
    7. Закрывает страницу браузера.
    8. Сохраняет полученные cookies в `cls._cookies`.
    9. Останавливает браузер.
    """
```

**Назначение**: Выполняет вход в систему с использованием `nodriver` для получения cookies.

**Параметры**:

- `proxy` (str, optional): Прокси-сервер для использования. По умолчанию `None`.

**Возвращает**:
- `AsyncIterator[str]`: Асинхронный генератор, возвращающий части ответа сервера.

**Вызывает исключения**:
- `ImportError`: Если модуль `nodriver` не установлен.

**Как работает функция**:

```
A: Проверка наличия nodriver
|
B: Получение экземпляра браузера и функции остановки
|
C: Получение URL для входа из переменной окружения (если есть)
|
D: Переход на страницу /app
|
E: Получение cookies
|
F: Закрытие страницы и остановка браузера
|
G: Сохранение cookies
```

**Примеры**:

```python
# Пример вызова функции
async for chunk in Gemini.nodriver_login(proxy='http://proxy.example.com'):
    print(chunk)
```

### `start_auto_refresh`

```python
@classmethod
async def start_auto_refresh(cls, proxy: str = None) -> None:
    """Запускает фоновую задачу для автоматического обновления cookies.
    Args:
        proxy (str, optional): Прокси-сервер для использования. По умолчанию None.

    Raises:
        Exception: Если не удалось обновить cookies.
        MissingAuthError: Если cookies невалидные.

    Как работает функция:
    1. Запускает бесконечный цикл.
    2. Внутри цикла пытается обновить cookies с помощью функции `rotate_1psidts`.
    3. Если обновление завершается успешно, обновляет `cls._cookies` и логирует информацию об этом.
    4. Если обновление завершается с ошибкой, логирует ошибку и отменяет фоновую задачу обновления cookies, если она существует.
    5. Засыпает на `cls.refresh_interval` секунд.
    """
```

**Назначение**: Запускает фоновую задачу для автоматического обновления cookies.

**Параметры**:
- `proxy` (str, optional): Прокси-сервер для использования. По умолчанию `None`.

**Возвращает**:
- `None`

**Вызывает исключения**:
- `Exception`: Если не удалось обновить cookies.
- `MissingAuthError`: Если cookies невалидные.

**Как работает функция**:

```
A: Запуск бесконечного цикла
|
B: Попытка обновления cookies
|
C: Обновление cookies или обработка ошибки
|
D: Ожидание
```

**Примеры**:

```python
# Пример вызова функции
async def main():
    await Gemini.start_auto_refresh(proxy='http://proxy.example.com')

asyncio.run(main())
```

### `create_async_generator`

```python
@classmethod
async def create_async_generator(
    cls,
    model: str,
    messages: Messages,
    proxy: str = None,
    cookies: Cookies = None,
    connector: BaseConnector = None,
    media: MediaListType = None,
    return_conversation: bool = False,
    conversation: Conversation = None,
    language: str = "en",
    **kwargs
) -> AsyncResult:
    """Создает асинхронный генератор для взаимодействия с моделью Gemini.

    Args:
        model (str): Модель для использования.
        messages (Messages): Список сообщений для отправки.
        proxy (str, optional): Прокси-сервер для использования. По умолчанию None.
        cookies (Cookies, optional): Cookies для аутентификации. По умолчанию None.
        connector (BaseConnector, optional): Aiohttp коннектор. По умолчанию None.
        media (MediaListType, optional): Список медиафайлов для отправки. По умолчанию None.
        return_conversation (bool, optional): Флаг, указывающий на необходимость возврата объекта Conversation. По умолчанию False.
        conversation (Conversation, optional): Объект Conversation для продолжения разговора. По умолчанию None.
        language (str, optional): Язык для использования. По умолчанию "en".

    Yields:
        AsyncResult: Части ответа сервера.

    Raises:
        MissingAuthError: Если отсутствует или недействителен cookie "__Secure-1PSID".
        RuntimeError: Если не удалось получить токен SNlM0e.

    Как работает функция:
    1. Инициализирует cookies и conversation.
    2. Форматирует prompt из messages.
    3. Создает ClientSession с заданными headers и connector.
    4. Если _snlm0e не существует, пытается получить его с помощью fetch_snlm0e или nodriver_login.
    5. Если не удается получить _snlm0e, выбрасывает исключение.
    6. Если GGOGLE_SID_COOKIE есть в cookies, запускает задачу auto_refresh.
    7. Загружает изображения с помощью upload_images.
    8. Отправляет POST запрос к REQUEST_URL с данными и параметрами.
    9. Обрабатывает ответ сервера и извлекает содержимое, reasoning и изображения.
    10. Возвращает Conversation, Reasoning, ImageResponse или текст в зависимости от ответа сервера.
    """
```

**Назначение**: Создает асинхронный генератор для взаимодействия с моделью Gemini.

**Параметры**:

- `model` (str): Модель для использования.
- `messages` (Messages): Список сообщений для отправки.
- `proxy` (str, optional): Прокси-сервер для использования. По умолчанию `None`.
- `cookies` (Cookies, optional): Cookies для аутентификации. По умолчанию `None`.
- `connector` (BaseConnector, optional): Aiohttp коннектор. По умолчанию `None`.
- `media` (MediaListType, optional): Список медиафайлов для отправки. По умолчанию `None`.
- `return_conversation` (bool, optional): Флаг, указывающий на необходимость возврата объекта `Conversation`. По умолчанию `False`.
- `conversation` (Conversation, optional): Объект `Conversation` для продолжения разговора. По умолчанию `None`.
- `language` (str, optional): Язык для использования. По умолчанию `"en"`.

**Возвращает**:

- `AsyncResult`: Асинхронный генератор, возвращающий части ответа сервера.

**Вызывает исключения**:

- `MissingAuthError`: Если отсутствует или недействителен cookie `__Secure-1PSID`.
- `RuntimeError`: Если не удалось получить токен `SNlM0e`.

**Как работает функция**:

```
A: Инициализация cookies и conversation
|
B: Форматирование prompt
|
C: Создание ClientSession
|
D: Получение _snlm0e (если необходимо)
|
E: Запуск задачи auto_refresh (если необходимо)
|
F: Загрузка изображений
|
G: Отправка POST запроса
|
H: Обработка ответа сервера
|
I: Возврат Conversation, Reasoning, ImageResponse или текста
```

**Примеры**:

```python
# Пример вызова функции
async def main():
    messages = [{"role": "user", "content": "Hello, Gemini!"}]
    async for chunk in Gemini.create_async_generator(model="gemini-2.0-flash", messages=messages):
        print(chunk)

asyncio.run(main())
```

### `synthesize`

```python
@classmethod
async def synthesize(cls, params: dict, proxy: str = None) -> AsyncIterator[bytes]:
    """Синтезирует речь на основе предоставленного текста.

    Args:
        params (dict): Параметры для синтеза речи, включая текст.
        proxy (str, optional): Прокси-сервер для использования. По умолчанию None.

    Yields:
        AsyncIterator[bytes]: Части синтезированной речи в формате bytes.

    Raises:
        ValueError: Если отсутствует параметр "text".

    Как работает функция:
    1. Проверяет наличие параметра "text" в params.
    2. Создает ClientSession с заданными cookies, headers и connector.
    3. Если _snlm0e не существует, пытается получить его с помощью fetch_snlm0e.
    4. Формирует inner_data для отправки в запросе.
    5. Отправляет POST запрос к "https://gemini.google.com/_/BardChatUi/data/batchexecute" с данными и параметрами.
    6. Обрабатывает ответ сервера, фильтрует и декодирует base64 данные.
    7. Возвращает части синтезированной речи.
    """
```

**Назначение**: Синтезирует речь на основе предоставленного текста.

**Параметры**:

- `params` (dict): Параметры для синтеза речи, включая текст.
- `proxy` (str, optional): Прокси-сервер для использования. По умолчанию `None`.

**Возвращает**:

- `AsyncIterator[bytes]`: Части синтезированной речи в формате bytes.

**Вызывает исключения**:

- `ValueError`: Если отсутствует параметр `"text"`.

**Как работает функция**:

```
A: Проверка наличия параметра "text"
|
B: Создание ClientSession
|
C: Получение _snlm0e (если необходимо)
|
D: Формирование inner_data
|
E: Отправка POST запроса
|
F: Обработка ответа сервера
|
G: Возврат частей синтезированной речи
```

**Примеры**:

```python
# Пример вызова функции
async def main():
    params = {"text": "Hello, world!"}
    async for chunk in Gemini.synthesize(params=params):
        print(chunk)

asyncio.run(main())
```

### `build_request`

```python
def build_request(
    prompt: str,
    language: str,
    conversation: Conversation = None,
    uploads: list[list[str, str]] = None,
    tools: list[list[str]] = []
) -> list:
    """Строит запрос к модели Gemini.

    Args:
        prompt (str): Текст запроса.
        language (str): Язык запроса.
        conversation (Conversation, optional): Объект Conversation для продолжения разговора. По умолчанию None.
        uploads (list[list[str, str]], optional): Список загруженных изображений. По умолчанию None.
        tools (list[list[str]], optional): Список инструментов. По умолчанию [].

    Returns:
        list: Список, представляющий запрос к модели Gemini.

    Как работает функция:
    1. Формирует список image_list из uploads.
    2. Строит и возвращает список, представляющий запрос к модели Gemini, включая prompt, language, conversation details, image_list и tools.
    """
```

**Назначение**: Строит запрос к модели Gemini.

**Параметры**:

- `prompt` (str): Текст запроса.
- `language` (str): Язык запроса.
- `conversation` (Conversation, optional): Объект `Conversation` для продолжения разговора. По умолчанию `None`.
- `uploads` (list[list[str, str]], optional): Список загруженных изображений. По умолчанию `None`.
- `tools` (list[list[str]], optional): Список инструментов. По умолчанию `[]`.

**Возвращает**:

- `list`: Список, представляющий запрос к модели Gemini.

**Как работает функция**:

```
A: Формирование списка image_list
|
B: Построение списка запроса
|
C: Возврат списка запроса
```

**Примеры**:

```python
# Пример вызова функции
request = Gemini.build_request(
    prompt="Hello, Gemini!",
    language="en",
    conversation=None,
    uploads=[["image_url", "image_name"]],
    tools=[]
)
print(request)
```

### `upload_images`

```python
    async def upload_images(connector: BaseConnector, media: MediaListType) -> list:
        """Загружает изображения на сервер Gemini.

        Args:
            connector (BaseConnector): Aiohttp коннектор.
            media (MediaListType): Список медиафайлов для отправки.

        Returns:
            list: Список URL загруженных изображений.

        Как работает функция:
        1. Определяет асинхронную функцию upload_image для загрузки одного изображения.
        2. upload_image:
            - Создает ClientSession с заданными headers и connector.
            - Преобразует изображение в bytes.
            - Отправляет OPTIONS запрос к UPLOAD_IMAGE_URL.
            - Отправляет POST запрос к UPLOAD_IMAGE_URL с заголовком "x-goog-upload-command": "start" для получения upload_url.
            - Отправляет OPTIONS запрос к upload_url.
            - Отправляет POST запрос к upload_url с заголовком "x-goog-upload-command": "upload, finalize" и данными изображения.
            - Возвращает URL загруженного изображения.
        3. Вызывает upload_image для каждого изображения в media с помощью asyncio.gather.
        4. Возвращает список URL загруженных изображений.
        """
```

**Назначение**: Загружает изображения на сервер Gemini.

**Параметры**:

- `connector` (BaseConnector): Aiohttp коннектор.
- `media` (MediaListType): Список медиафайлов для отправки.

**Возвращает**:

- `list`: Список URL загруженных изображений.

**Как работает функция**:

```
A: Определение асинхронной функции upload_image
|
B: upload_image:
    - Создание ClientSession
    - Преобразование изображения в bytes
    - Отправка OPTIONS запроса
    - Отправка POST запроса для получения upload_url
    - Отправка OPTIONS запроса к upload_url
    - Отправка POST запроса с данными изображения
    - Возврат URL загруженного изображения
|
C: Вызов upload_image для каждого изображения в media
|
D: Возврат списка URL загруженных изображений
```

**Примеры**:

```python
# Пример вызова функции
async def main():
    media = [("image_data", "image_name")]
    connector = get_connector()
    urls = await Gemini.upload_images(connector=connector, media=media)
    print(urls)

asyncio.run(main())
```

### `fetch_snlm0e`

```python
@classmethod
async def fetch_snlm0e(cls, session: ClientSession, cookies: Cookies):
    """Извлекает токен `SNlM0e` из cookies.

    Args:
        session (ClientSession): Aiohttp ClientSession.
        cookies (Cookies): Cookies для аутентификации.

    Как работает функция:
    1. Отправляет GET запрос к cls.url с заданными cookies.
    2. Извлекает текст ответа.
    3. Ищет токен SNlM0e в тексте ответа с помощью регулярного выражения.
    4. Если токен найден, сохраняет его в cls._snlm0e.
    5. Ищет SID в тексте ответа с помощью регулярного выражения.
    6. Если SID найден, сохраняет его в cls._sid.
    """
```

**Назначение**: Извлекает токен `SNlM0e` из cookies.

**Параметры**:

- `session` (ClientSession): Aiohttp `ClientSession`.
- `cookies` (Cookies): Cookies для аутентификации.

**Как работает функция**:

```
A: Отправка GET запроса к cls.url
|
B: Извлечение текста ответа
|
C: Поиск токена SNlM0e с помощью регулярного выражения
|
D: Сохранение токена SNlM0e
|
E: Поиск SID с помощью регулярного выражения
|
F: Сохранение SID
```

**Примеры**:

```python
# Пример вызова функции
async def main():
    cookies = {"__Secure-1PSID": "example_cookie"}
    async with ClientSession() as session:
        await Gemini.fetch_snlm0e(session=session, cookies=cookies)
        print(Gemini._snlm0e)

asyncio.run(main())
```

### `iter_filter_base64`

```python
async def iter_filter_base64(chunks: AsyncIterator[bytes]) -> AsyncIterator[bytes]:
    """Фильтрует base64 данные из асинхронного итератора чанков.

    Args:
        chunks (AsyncIterator[bytes]): Асинхронный итератор чанков в формате bytes.

    Yields:
        AsyncIterator[bytes]: Отфильтрованные base64 данные.

    Raises:
        ValueError: Если response не содержит `search_for`.

    Как работает функция:
    1. Устанавливает маркер `is_started` в `False`.
    2. Проходит по каждому чанку в chunks:
        - Если `is_started` равен `True`:
            - Если `end_with` присутствует в чанке, возвращает часть чанка до `end_with` и завершает итерацию.
            - Иначе, возвращает чанк.
        - Если `search_for` присутствует в чанке:
            - Устанавливает `is_started` в `True`.
            - Возвращает часть чанка после `search_for`.
        - Иначе, выбрасывает исключение `ValueError`.
    """
```

**Назначение**: Фильтрует base64 данные из асинхронного итератора чанков.

**Параметры**:

- `chunks` (AsyncIterator[bytes]): Асинхронный итератор чанков в формате bytes.

**Возвращает**:

- `AsyncIterator[bytes]`: Отфильтрованные base64 данные.

**Вызывает исключения**:

- `ValueError`: Если response не содержит `search_for`.

**Как работает функция**:

```
A: Установка is_started в False
|
B: Проход по каждому чанку
|
C: Если is_started:
    - Проверка наличия end_with
    - Возврат части чанка или всего чанка
|
D: Если search_for:
    - Установка is_started в True
    - Возврат части чанка после search_for
|
E: Иначе:
    - Выброс ValueError
```

**Примеры**:

```python
# Пример вызова функции
async def main():
    async def chunk_generator():
        yield b'some data [["wrb.fr","XqA3Ic","[\\\\"base64data\\\\"\'] more data'
    async for chunk in iter_filter_base64(chunk_generator()):
        print(chunk)

asyncio.run(main())
```

### `iter_base64_decode`

```python
async def iter_base64_decode(chunks: AsyncIterator[bytes]) -> AsyncIterator[bytes]:
    """Декодирует base64 данные из асинхронного итератора чанков.

    Args:
        chunks (AsyncIterator[bytes]): Асинхронный итератор чанков в формате bytes.

    Yields:
        AsyncIterator[bytes]: Декодированные base64 данные.

    Как работает функция:
    1. Инициализирует буфер и переменную для остатка.
    2. Проходит по каждому чанку в chunks:
        - Объединяет буфер и чанк.
        - Вычисляет остаток от деления длины чанка на 4.
        - Обновляет буфер, сохраняя последние `rest` байт.
        - Декодирует base64 данные до `rest`.
        - Возвращает декодированные данные.
    3. Если остаток больше 0, декодирует оставшиеся данные в буфере, дополняя их символами `=` до кратности 4.
    """
```

**Назначение**: Декодирует base64 данные из асинхронного итератора чанков.

**Параметры**:

- `chunks` (AsyncIterator[bytes]): Асинхронный итератор чанков в формате bytes.

**Возвращает**:

- `AsyncIterator[bytes]`: Декодированные base64 данные.

**Как работает функция**:

```
A: Инициализация буфера и переменной для остатка
|
B: Проход по каждому чанку
|
C: Объединение буфера и чанка
|
D: Вычисление остатка
|
E: Обновление буфера
|
F: Декодирование base64 данных
|
G: Возврат декодированных данных
|
H: Если остаток > 0:
    - Декодирование остатка данных
```

**Примеры**:

```python
# Пример вызова функции
import base64
async def main():
    async def chunk_generator():
        encoded_data = base64.b64encode(b'some data')
        yield encoded_data
    async for chunk in iter_base64_decode(chunk_generator()):
        print(chunk)

asyncio.run(main())
```

### `rotate_1psidts`

```python
async def rotate_1psidts(url, cookies: dict, proxy: str | None = None) -> str:
    """Обновляет cookie `__Secure-1PSIDTS` путем запроса к `ROTATE_COOKIES_URL`.

    Args:
        url (str): URL для запроса.
        cookies (dict): Словарь с текущими cookies.
        proxy (str | None, optional): Прокси-сервер для использования. По умолчанию None.

    Returns:
        str: Новое значение cookie `__Secure-1PSIDTS`.

    Raises:
        MissingAuthError: Если cookies невалидные (статус ответа 401).
        HTTPError: Если произошла ошибка при выполнении запроса.

    Как работает функция:
    1.  Создает директорию для хранения cookies, если она не существует.
    2.  Проверяет, был ли файл кэша изменен в течение последней минуты, чтобы избежать 429 ошибок.
    3.  Создает асинхронную сессию клиента.
    4.  Выполняет POST запрос к `ROTATE_COOKIES_URL` с текущими cookies.
    5.  Если статус ответа 401, вызывает исключение `MissingAuthError`.
    6.  Вызывает `response.raise_for_status()` для проверки на наличие ошибок в ответе.
    7.  Обновляет словарь `cookies` значениями из ответа.
    8.  Получает новое значение cookie `__Secure-1PSIDTS` из ответа.
    9.  Записывает cookies в файл.
    10. Возвращает новое значение `__Secure-1PSIDTS`.
    """
```

**Назначение**: Обновляет cookie `__Secure-1PSIDTS` путем запроса к `ROTATE_COOKIES_URL`.

**Параметры**:

- `url` (str): URL для запроса.
- `cookies` (dict): Словарь с текущими cookies.
- `proxy` (str | None, optional): Прокси-сервер для использования. По умолчанию `None`.

**Возвращает**:

- `str`: Новое значение cookie `__Secure-1PSIDTS`.

**Вызывает исключения**:

- `MissingAuthError`: Если cookies невалидные (статус ответа 401).
- `HTTPError`: Если произошла ошибка при выполнении запроса.

**Как работает функция**:

```
A: Создание директории для хранения cookies
|
B: Проверка времени изменения файла кэша
|
C: Создание асинхронной сессии клиента
|
D: Выполнение POST запроса к ROTATE_COOKIES_URL
|
E: Проверка статуса ответа (401)
|
F: Вызов response.raise_for_status()
|
G: Обновление словаря cookies
|
H: Получение нового значения __Secure-1PSIDTS
|
I: Запись cookies в файл
|
J: Возврат нового значения __Secure-1PSIDTS
```

**Примеры**:

```python
# Пример вызова функции
async def main():
    cookies = {"__Secure-1PSID": "old_cookie", "__Secure-1PSIDTS": "old_ts"}
    new_ts = await rotate_1psidts("https://gemini.google.com", cookies)
    print(new_ts)

asyncio.run(main())