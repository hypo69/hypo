# Модуль для работы с Google Gemini
## Обзор

Модуль `Gemini.py` предназначен для взаимодействия с моделями Google Gemini. Он предоставляет асинхронный интерфейс для генерации текста, обработки изображений и выполнения других задач, используя API Gemini. Модуль поддерживает автоматическое обновление cookies для поддержания активной сессии.

## Подробней

Этот модуль является частью проекта `hypotez` и обеспечивает интеграцию с моделями Google Gemini для генерации контента и обработки мультимедийных данных. Он включает в себя функциональность для аутентификации, управления cookies, загрузки изображений и взаимодействия с API Gemini. Модуль использует асинхронные запросы для обеспечения высокой производительности и масштабируемости.

## Классы

### `Gemini`

**Описание**: Класс `Gemini` предоставляет интерфейс для взаимодействия с моделями Google Gemini. Он наследует функциональность от `AsyncGeneratorProvider` и `ProviderModelMixin`.

**Наследует**:
- `AsyncGeneratorProvider`: Обеспечивает асинхронную генерацию контента.
- `ProviderModelMixin`: Предоставляет методы для работы с моделями.

**Аттрибуты**:
- `label` (str): Название провайдера ("Google Gemini").
- `url` (str): URL сервиса Gemini ("https://gemini.google.com").
- `needs_auth` (bool): Требуется ли аутентификация (True).
- `working` (bool): Указывает, работает ли провайдер (True).
- `use_nodriver` (bool): Использовать ли `nodriver` для аутентификации (True).
- `default_model` (str): Модель по умолчанию (пустая строка).
- `default_image_model` (str): Модель по умолчанию для изображений (пустая строка).
- `default_vision_model` (str): Модель по умолчанию для анализа изображений (пустая строка).
- `image_models` (list): Список моделей, поддерживающих обработку изображений.
- `models` (list): Список поддерживаемых моделей.
- `model_aliases` (dict): Алиасы моделей.
- `synthesize_content_type` (str): Тип контента для синтеза речи ("audio/vnd.wav").
- `_cookies` (Cookies): Cookies для аутентификации.
- `_snlm0e` (str): Токен `SNlM0e`, необходимый для запросов.
- `_sid` (str): Идентификатор сессии.
- `auto_refresh` (bool): Автоматически обновлять cookies (True).
- `refresh_interval` (int): Интервал обновления cookies в секундах (540).
- `rotate_tasks` (dict): Словарь задач для ротации cookies.

**Методы**:
- `nodriver_login`: Выполняет вход в систему с использованием `nodriver`.
- `start_auto_refresh`: Запускает фоновую задачу для автоматического обновления cookies.
- `create_async_generator`: Создает асинхронный генератор для взаимодействия с API Gemini.
- `synthesize`: Синтезирует речь на основе заданного текста.
- `build_request`: Строит запрос к API Gemini.
- `upload_images`: Загружает изображения в Gemini.
- `fetch_snlm0e`: Получает токен `SNlM0e` из cookies.

### `nodriver_login`

```python
@classmethod
async def nodriver_login(cls, proxy: str = None) -> AsyncIterator[str]:
    """
    Выполняет вход в систему с использованием `nodriver` для получения cookies.

    Args:
        proxy (str, optional): Прокси-сервер для использования. По умолчанию `None`.

    Yields:
        AsyncIterator[str]: Асинхронный итератор, возвращающий URL для входа.

    Raises:
        ImportError: Если модуль `nodriver` не установлен.
    """
    ...
```

**Назначение**:
Функция `nodriver_login` выполняет вход в систему Gemini с использованием `nodriver`, если это возможно. Она получает cookies, необходимые для аутентификации.

**Параметры**:
- `proxy` (str, optional): Прокси-сервер для использования. По умолчанию `None`.

**Возвращает**:
- `AsyncIterator[str]`: Асинхронный итератор, возвращающий URL для входа.

**Вызывает исключения**:
- `ImportError`: Если модуль `nodriver` не установлен.

**Как работает функция**:

1. **Проверка наличия `nodriver`**: Проверяет, установлен ли модуль `nodriver`. Если нет, функция завершается.
2. **Получение экземпляра браузера**: Получает экземпляр браузера и функцию для его остановки с помощью `get_nodriver`.
3. **Получение URL для входа**: Получает URL для входа из переменной окружения `G4F_LOGIN_URL`.
4. **Переход на страницу Gemini**: Переходит на страницу Gemini (`f"{cls.url}/app"`).
5. **Выбор текстовой области**: Выбирает текстовую область на странице.
6. **Получение cookies**: Получает cookies из браузера.
7. **Закрытие страницы**: Закрывает страницу браузера.
8. **Остановка браузера**: Останавливает браузер.

**Примеры**:

```python
async for chunk in Gemini.nodriver_login(proxy='http://proxy.example.com'):
    print(chunk)
```

### `start_auto_refresh`

```python
@classmethod
async def start_auto_refresh(cls, proxy: str = None) -> None:
    """
    Запускает фоновую задачу для автоматического обновления cookies.

    Args:
        proxy (str, optional): Прокси-сервер для использования. По умолчанию `None`.

    Raises:
        Exception: Если не удается обновить cookies.
    """
    ...
```

**Назначение**:
Функция `start_auto_refresh` запускает фоновую задачу для автоматического обновления cookies. Это необходимо для поддержания активной сессии с Gemini.

**Параметры**:
- `proxy` (str, optional): Прокси-сервер для использования. По умолчанию `None`.

**Возвращает**:
- `None`

**Вызывает исключения**:
- `Exception`: Если не удается обновить cookies.

**Как работает функция**:

1. **Бесконечный цикл**: Запускает бесконечный цикл для периодического обновления cookies.
2. **Обновление cookies**: Пытается обновить cookies с помощью функции `rotate_1psidts`.
3. **Обработка ошибок**: Если обновление cookies не удается, регистрирует ошибку и отменяет задачу ротации cookies.
4. **Обновление `__Secure-1PSIDTS`**: Обновляет значение `__Secure-1PSIDTS` в cookies.
5. **Ожидание**: Ожидает заданный интервал (`cls.refresh_interval`) перед следующей попыткой обновления.

**Примеры**:

```python
asyncio.create_task(Gemini.start_auto_refresh(proxy='http://proxy.example.com'))
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
    """
    Создает асинхронный генератор для взаимодействия с API Gemini.

    Args:
        model (str): Модель для использования.
        messages (Messages): Список сообщений для отправки.
        proxy (str, optional): Прокси-сервер для использования. По умолчанию `None`.
        cookies (Cookies, optional): Cookies для аутентификации. По умолчанию `None`.
        connector (BaseConnector, optional): Aiohttp коннектор. По умолчанию `None`.
        media (MediaListType, optional): Список медиафайлов для отправки. По умолчанию `None`.
        return_conversation (bool, optional): Возвращать ли объект Conversation. По умолчанию `False`.
        conversation (Conversation, optional): Объект Conversation. По умолчанию `None`.
        language (str, optional): Язык. По умолчанию "en".
        **kwargs: Дополнительные аргументы.

    Yields:
        AsyncResult: Асинхронный генератор, возвращающий результат взаимодействия с API Gemini.

    Raises:
        MissingAuthError: Если отсутствуют или недействительны cookies.
        RuntimeError: Если не удается получить токен `SNlM0e`.
    """
    ...
```

**Назначение**:
Функция `create_async_generator` создает асинхронный генератор для взаимодействия с API Gemini. Она отправляет сообщения, обрабатывает ответы и возвращает результаты.

**Параметры**:
- `model` (str): Модель для использования.
- `messages` (Messages): Список сообщений для отправки.
- `proxy` (str, optional): Прокси-сервер для использования. По умолчанию `None`.
- `cookies` (Cookies, optional): Cookies для аутентификации. По умолчанию `None`.
- `connector` (BaseConnector, optional): Aiohttp коннектор. По умолчанию `None`.
- `media` (MediaListType, optional): Список медиафайлов для отправки. По умолчанию `None`.
- `return_conversation` (bool, optional): Возвращать ли объект Conversation. По умолчанию `False`.
- `conversation` (Conversation, optional): Объект Conversation. По умолчанию `None`.
- `language` (str, optional): Язык. По умолчанию "en".
- `**kwargs`: Дополнительные аргументы.

**Возвращает**:
- `AsyncResult`: Асинхронный генератор, возвращающий результат взаимодействия с API Gemini.

**Вызывает исключения**:
- `MissingAuthError`: Если отсутствуют или недействительны cookies.
- `RuntimeError`: Если не удается получить токен `SNlM0e`.

**Как работает функция**:

1. **Инициализация cookies**: Инициализирует cookies из переданных параметров или из файла.
2. **Формирование запроса**: Формирует запрос к API Gemini на основе переданных сообщений и параметров.
3. **Получение токена `SNlM0e`**: Получает токен `SNlM0e` из cookies или запрашивает его с помощью `nodriver_login`.
4. **Загрузка изображений**: Загружает изображения, если они есть в списке медиафайлов.
5. **Отправка запроса**: Отправляет POST-запрос к API Gemini с использованием `aiohttp.ClientSession`.
6. **Обработка ответа**: Обрабатывает ответ от API Gemini, извлекая текст, изображения и другие данные.
7. **Генерация результатов**: Генерирует результаты в виде асинхронного генератора.

**Примеры**:

```python
async for chunk in Gemini.create_async_generator(
    model='gemini-2.0-flash',
    messages=[{'role': 'user', 'content': 'Hello'}],
    proxy='http://proxy.example.com'
):
    print(chunk)
```

### `synthesize`

```python
@classmethod
async def synthesize(cls, params: dict, proxy: str = None) -> AsyncIterator[bytes]:
    """
    Синтезирует речь на основе заданного текста.

    Args:
        params (dict): Параметры для синтеза речи, включая текст.
        proxy (str, optional): Прокси-сервер для использования. По умолчанию `None`.

    Yields:
        AsyncIterator[bytes]: Асинхронный итератор, возвращающий аудиоданные в формате bytes.

    Raises:
        ValueError: Если отсутствует параметр "text".
    """
    ...
```

**Назначение**:
Функция `synthesize` синтезирует речь на основе заданного текста.

**Параметры**:
- `params` (dict): Параметры для синтеза речи, включая текст.
- `proxy` (str, optional): Прокси-сервер для использования. По умолчанию `None`.

**Возвращает**:
- `AsyncIterator[bytes]`: Асинхронный итератор, возвращающий аудиоданные в формате bytes.

**Вызывает исключения**:
- `ValueError`: Если отсутствует параметр "text".

**Как работает функция**:

1. **Проверка наличия текста**: Проверяет, передан ли текст для синтеза речи.
2. **Инициализация сессии**: Инициализирует асинхронную сессию с использованием `aiohttp.ClientSession`.
3. **Получение токена `SNlM0e`**: Получает токен `SNlM0e` из cookies.
4. **Формирование запроса**: Формирует POST-запрос к API Gemini для синтеза речи.
5. **Обработка ответа**: Обрабатывает ответ от API Gemini, извлекая аудиоданные в формате base64.
6. **Декодирование base64**: Декодирует аудиоданные из формата base64 в bytes.
7. **Генерация результатов**: Генерирует результаты в виде асинхронного генератора.

**Примеры**:

```python
async for chunk in Gemini.synthesize(
    params={'text': 'Hello, world!'},
    proxy='http://proxy.example.com'
):
    print(chunk)
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
    """
    Строит запрос к API Gemini.

    Args:
        prompt (str): Текст запроса.
        language (str): Язык запроса.
        conversation (Conversation, optional): Объект Conversation. По умолчанию `None`.
        uploads (list[list[str, str]], optional): Список загруженных изображений. По умолчанию `None`.
        tools (list[list[str]], optional): Список инструментов. По умолчанию `[]`.

    Returns:
        list: Сформированный запрос для API Gemini.
    """
    ...
```

**Назначение**:
Функция `build_request` строит запрос к API Gemini на основе переданных параметров.

**Параметры**:
- `prompt` (str): Текст запроса.
- `language` (str): Язык запроса.
- `conversation` (Conversation, optional): Объект Conversation. По умолчанию `None`.
- `uploads` (list[list[str, str]], optional): Список загруженных изображений. По умолчанию `None`.
- `tools` (list[list[str]], optional): Список инструментов. По умолчанию `[]`.

**Возвращает**:
- `list`: Сформированный запрос для API Gemini.

**Как работает функция**:

1. **Формирование списка изображений**: Формирует список изображений для запроса.
2. **Формирование запроса**: Формирует запрос в виде списка, содержащего текст запроса, язык, информацию о разговоре, список изображений и другие параметры.

**Примеры**:

```python
request = Gemini.build_request(
    prompt='Hello',
    language='en',
    conversation=Conversation(
        conversation_id='123',
        response_id='456',
        choice_id='789',
        model='gemini-2.0-flash'
    ),
    uploads=[['http://example.com/image.jpg', 'image.jpg']]
)
```

### `upload_images`

```python
async def upload_images(connector: BaseConnector, media: MediaListType) -> list:
    """
    Загружает изображения в Gemini.

    Args:
        connector (BaseConnector): Aiohttp коннектор.
        media (MediaListType): Список медиафайлов для загрузки.

    Returns:
        list: Список URL загруженных изображений.
    """
    ...
```

**Назначение**:
Функция `upload_images` загружает изображения в Gemini.

**Параметры**:
- `connector` (BaseConnector): Aiohttp коннектор.
- `media` (MediaListType): Список медиафайлов для загрузки.

**Возвращает**:
- `list`: Список URL загруженных изображений.

**Как работает функция**:

1. **Определение внутренней функции `upload_image`**: Функция определяет внутреннюю асинхронную функцию `upload_image`, которая выполняет загрузку одного изображения.
2. **Инициализация сессии**: Внутренняя функция инициализирует асинхронную сессию с использованием `aiohttp.ClientSession`.
3. **Преобразование изображения в bytes**: Преобразует изображение в формат bytes.
4. **Запрос URL для загрузки**: Отправляет OPTIONS-запрос к API Gemini для получения URL для загрузки изображения.
5. **Загрузка изображения**: Отправляет POST-запрос к полученному URL для загрузки изображения.
6. **Возврат URL загруженного изображения**: Возвращает URL загруженного изображения.
7. **Параллельная загрузка**: Функция `upload_images` использует `asyncio.gather` для параллельной загрузки всех изображений из списка `media`.

**Примеры**:

```python
connector = get_connector()
media = [('http://example.com/image.jpg', 'image.jpg')]
urls = await Gemini.upload_images(connector, media)
```

### `fetch_snlm0e`

```python
@classmethod
async def fetch_snlm0e(cls, session: ClientSession, cookies: Cookies):
    """
    Получает токен `SNlM0e` из cookies.

    Args:
        session (ClientSession): Aiohttp сессия.
        cookies (Cookies): Cookies для аутентификации.
    """
    ...
```

**Назначение**:
Функция `fetch_snlm0e` получает токен `SNlM0e` из cookies.

**Параметры**:
- `session` (ClientSession): Aiohttp сессия.
- `cookies` (Cookies): Cookies для аутентификации.

**Как работает функция**:

1. **Получение страницы**: Отправляет GET-запрос к URL Gemini с использованием переданных cookies.
2. **Поиск токена `SNlM0e`**: Ищет токен `SNlM0e` в тексте ответа с использованием регулярного выражения.
3. **Сохранение токена `SNlM0e`**: Сохраняет найденный токен `SNlM0e` в атрибуте `_snlm0e` класса `Gemini`.
4. **Поиск sid** : Ищет `sid` в тексте ответа с использованием регулярного выражения.
5.  **Сохранение sid** : Сохраняет найденный `sid` в атрибуте `_sid` класса `Gemini`.

**Примеры**:

```python
session = ClientSession()
cookies = {'__Secure-1PSID': 'example'}
await Gemini.fetch_snlm0e(session, cookies)
```

### `Conversation`

**Описание**: Класс `Conversation` представляет собой структуру данных для хранения информации о разговоре с Gemini. Он наследует функциональность от `JsonConversation`.

**Наследует**:
- `JsonConversation`: Предоставляет базовую функциональность для работы с разговорами в формате JSON.

**Аттрибуты**:
- `conversation_id` (str): Идентификатор разговора.
- `response_id` (str): Идентификатор ответа.
- `choice_id` (str): Идентификатор выбора.
- `model` (str): Модель, используемая в разговоре.

```python
class Conversation(JsonConversation):
    def __init__(self,\
        conversation_id: str,\
        response_id: str,\
        choice_id: str,\
        model: str\
    ) -> None:
        self.conversation_id = conversation_id
        self.response_id = response_id
        self.choice_id = choice_id
        self.model = model
```

### `iter_filter_base64`

```python
async def iter_filter_base64(chunks: AsyncIterator[bytes]) -> AsyncIterator[bytes]:
    """
    Фильтрует итератор байтовых чанков для извлечения данных в формате base64.

    Args:
        chunks (AsyncIterator[bytes]): Асинхронный итератор байтовых чанков.

    Yields:
        AsyncIterator[bytes]: Асинхронный итератор, возвращающий отфильтрованные байтовые чанки.

    Raises:
        ValueError: Если ответ не содержит ожидаемую структуру.
    """
    ...
```

**Назначение**:
Функция `iter_filter_base64` фильтрует асинхронный итератор байтовых чанков, чтобы извлечь данные в формате base64.

**Параметры**:
- `chunks` (AsyncIterator[bytes]): Асинхронный итератор байтовых чанков.

**Возвращает**:
- `AsyncIterator[bytes]`: Асинхронный итератор, возвращающий отфильтрованные байтовые чанки.

**Вызывает исключения**:
- `ValueError`: Если ответ не содержит ожидаемую структуру.

**Как работает функция**:

1. **Поиск начала данных**: Ищет начало данных в формате base64 в чанках.
2. **Извлечение данных**: Извлекает данные в формате base64 из чанков.
3. **Фильтрация данных**: Фильтрует данные, чтобы удалить лишние символы.

### `iter_base64_decode`

```python
async def iter_base64_decode(chunks: AsyncIterator[bytes]) -> AsyncIterator[bytes]:
    """
    Декодирует итератор байтовых чанков из формата base64.

    Args:
        chunks (AsyncIterator[bytes]): Асинхронный итератор байтовых чанков.

    Yields:
        AsyncIterator[bytes]: Асинхронный итератор, возвращающий декодированные байтовые чанки.
    """
    ...
```

**Назначение**:
Функция `iter_base64_decode` декодирует асинхронный итератор байтовых чанков из формата base64.

**Параметры**:
- `chunks` (AsyncIterator[bytes]): Асинхронный итератор байтовых чанков.

**Возвращает**:
- `AsyncIterator[bytes]`: Асинхронный итератор, возвращающий декодированные байтовые чанки.

**Как работает функция**:

1. **Буферизация данных**: Буферизует данные из чанков.
2. **Декодирование base64**: Декодирует данные из формата base64.
3. **Генерация результатов**: Генерирует результаты в виде асинхронного итератора.

### `rotate_1psidts`

```python
async def rotate_1psidts(url, cookies: dict, proxy: str | None = None) -> str:
    """
    Обновляет cookies, получая новое значение для `__Secure-1PSIDTS`.

    Args:
        url (str): URL для запроса обновления cookies.
        cookies (dict): Текущие cookies.
        proxy (str | None, optional): Прокси-сервер для использования. По умолчанию `None`.

    Returns:
        str: Новое значение для `__Secure-1PSIDTS`.

    Raises:
        MissingAuthError: Если cookies недействительны.
        HTTPError: Если возникает HTTP ошибка при запросе.
    """
    ...
```

**Назначение**:
Функция `rotate_1psidts` обновляет cookies, получая новое значение для `__Secure-1PSIDTS`.

**Параметры**:
- `url` (str): URL для запроса обновления cookies.
- `cookies` (dict): Текущие cookies.
- `proxy` (str | None, optional): Прокси-сервер для использования. По умолчанию `None`.

**Возвращает**:
- `str`: Новое значение для `__Secure-1PSIDTS`.

**Вызывает исключения**:
- `MissingAuthError`: Если cookies недействительны.
- `HTTPError`: Если возникает HTTP ошибка при запросе.

**Как работает функция**:

1. **Инициализация сессии**: Инициализирует асинхронную сессию с использованием `aiohttp.ClientSession`.
2. **Отправка запроса**: Отправляет POST-запрос к API Gemini для обновления cookies.
3. **Обновление cookies**: Обновляет cookies в локальном хранилище.
4. **Получение нового значения `__Secure-1PSIDTS`**: Получает новое значение `__Secure-1PSIDTS` из ответа.

## Функции

### `build_request`

```python
def build_request(\n        prompt: str,\n        language: str,\n        conversation: Conversation = None,\n        uploads: list[list[str, str]] = None,\n        tools: list[list[str]] = []\n    ) -> list:
    """
    Строит запрос к API Gemini.

    Args:
        prompt (str): Текст запроса.
        language (str): Язык запроса.
        conversation (Conversation, optional): Объект Conversation. По умолчанию `None`.
        uploads (list[list[str, str]], optional): Список загруженных изображений. По умолчанию `None`.
        tools (list[list[str]], optional): Список инструментов. По умолчанию `[]`.

    Returns:
        list: Сформированный запрос для API Gemini.
    """
    ...
```

**Как работает функция**:

1. **Преобразование списка изображений**:
   - Код берет список загруженных изображений `uploads`, который состоит из пар `[image_url, image_name]`.
   - Преобразует этот список в формат, ожидаемый API Gemini, создавая список `image_list`, где каждое изображение представлено в виде `[[[image_url, 1], image_name]]`. Это необходимо для правильной передачи информации об изображениях в запросе.

2. **Формирование структуры запроса**:
   - Создает основную структуру запроса в виде списка, содержащего несколько элементов, необходимых для API Gemini.
   - `prompt`: Текст запроса, который необходимо обработать.
   - `0`: Неизвестный параметр (возможно, связан с форматированием или типом запроса).
   - `None`: Заполнитель для неиспользуемых параметров.
   - `image_list`: Список изображений в формате, подготовленном на предыдущем шаге.
   - `[language]`: Язык запроса.
   - Информация о текущем разговоре (`conversation`):
     - Если `conversation` предоставлен, извлекаются `conversation_id`, `response_id` и `choice_id`.
     - Если `conversation` отсутствует (None), используются значения `None` для соответствующих полей.
   - `[1]`, `0`, `[]`, `tools`, `1`, `0`: Другие параметры и заполнители, необходимые для структуры запроса (их назначение не указано в коде).

3. **Возврат структуры запроса**:
   - Возвращает сформированный список, который представляет собой полную структуру запроса, готовую для отправки в API Gemini.

**Примеры**:

```python
# Пример 1: Базовый запрос с текстом и языком
prompt = "Как дела?"
language = "ru"
request = build_request(prompt=prompt, language=language)

# Пример 2: Запрос с добавлением информации о разговоре
prompt = "Продолжи предложение: 'Солнце светит ярко...'"
language = "ru"
conversation = Conversation(conversation_id="123", response_id="456", choice_id="789", model="gemini-2.0-flash")
request = build_request(prompt=prompt, language=language, conversation=conversation)

# Пример 3: Запрос с загрузкой изображений
prompt = "Опиши, что на картинке."
language = "ru"
uploads = [["https://example.com/image1.jpg", "image1.jpg"], ["https://example.com/image2.jpg", "image2.jpg"]]
request = build_request(prompt=prompt, language=language, uploads=uploads)

# Пример 4: Запрос с использованием инструментов (tools)
prompt = "Найди информацию о Python."
language = "ru"
tools = [["search", "python"]]
request = build_request(prompt=prompt, language=language, tools=tools)
```

```
              Начало
                 ↓
      Преобразование списка
          изображений
                 ↓
     Формирование структуры
              запроса
                 ↓
      Возврат структуры
              запроса
                 ↓
                Конец