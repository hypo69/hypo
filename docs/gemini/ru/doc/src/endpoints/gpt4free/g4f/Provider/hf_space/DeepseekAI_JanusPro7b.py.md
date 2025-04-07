# Модуль DeepseekAI_JanusPro7b

## Обзор

Модуль `DeepseekAI_JanusPro7b` предоставляет асинхронный интерфейс для взаимодействия с моделью DeepseekAI Janus-Pro-7B, размещенной на платформе Hugging Face Spaces. Он поддерживает генерацию текста и изображений, а также обработку истории сообщений.

## Подробнее

Этот модуль является частью проекта `hypotez` и предназначен для обеспечения доступа к возможностям модели DeepseekAI Janus-Pro-7B через асинхронные запросы. Он использует `StreamSession` для обработки потоковых данных и поддерживает передачу изображений.

## Классы

### `DeepseekAI_JanusPro7b`

**Описание**: Класс `DeepseekAI_JanusPro7b` является провайдером для модели DeepseekAI Janus-Pro-7B. Он наследует функциональность от `AsyncGeneratorProvider` и `ProviderModelMixin` и предоставляет методы для взаимодействия с API модели.

**Наследует**:
- `AsyncGeneratorProvider`: Обеспечивает асинхронную генерацию данных.
- `ProviderModelMixin`: Предоставляет общие методы для работы с моделями.

**Атрибуты**:
- `label` (str): Метка провайдера ("DeepseekAI Janus-Pro-7B").
- `space` (str): Имя пространства Hugging Face, где размещена модель ("deepseek-ai/Janus-Pro-7B").
- `url` (str): URL страницы модели на Hugging Face Spaces.
- `api_url` (str): Базовый URL API модели.
- `referer` (str): Referer для HTTP-запросов.
- `working` (bool): Указывает, что провайдер в рабочем состоянии.
- `supports_stream` (bool): Указывает, что провайдер поддерживает потоковую передачу данных.
- `supports_system_message` (bool): Указывает, что провайдер поддерживает системные сообщения.
- `supports_message_history` (bool): Указывает, что провайдер поддерживает историю сообщений.
- `default_model` (str): Модель по умолчанию ("janus-pro-7b").
- `default_image_model` (str): Модель для генерации изображений по умолчанию ("janus-pro-7b-image").
- `default_vision_model` (str): Модель для обработки изображений по умолчанию.
- `image_models` (list[str]): Список моделей для генерации изображений.
- `vision_models` (list[str]): Список моделей для обработки изображений.
- `models` (list[str]): Список всех поддерживаемых моделей.

**Методы**:
- `run(method, session, prompt, conversation, image, seed)`: Выполняет HTTP-запрос к API модели.
- `create_async_generator(model, messages, media, prompt, proxy, cookies, api_key, zerogpu_uuid, return_conversation, conversation, seed, **kwargs)`: Создает асинхронный генератор для взаимодействия с моделью.

## Функции

### `run`

```python
@classmethod
def run(cls, method: str, session: StreamSession, prompt: str, conversation: JsonConversation, image: dict = None, seed: int = 0):
    """
    Выполняет HTTP-запрос к API модели.

    Args:
        method (str): HTTP-метод ("post" или "get").
        session (StreamSession): Асинхровая сессия для выполнения запросов.
        prompt (str): Текст запроса.
        conversation (JsonConversation): Объект, содержащий информацию о текущем разговоре.
        image (dict, optional): Данные изображения для запроса. По умолчанию `None`.
        seed (int): Зерно для генерации случайных чисел.

    Returns:
        StreamResponse: Объект ответа от API.

    Как работает функция:
    1. Функция принимает параметры, необходимые для выполнения запроса к API, включая метод запроса, сессию, текст запроса, объект разговора, данные изображения и зерно случайных чисел.
    2. Устанавливает заголовки запроса, включая `content-type`, `x-zerogpu-token`, `x-zerogpu-uuid` и `referer`.
    3. В зависимости от метода запроса, выполняет `POST` или `GET` запрос к API.
        - Если `method` равен "post", отправляет `POST` запрос с данными, включающими изображение, текст запроса, зерно, параметры генерации и информацию о сессии.
        - Если `method` равен "image", отправляет `POST` запрос для генерации изображения с параметрами, включающими текст запроса, зерно и информацию о сессии.
        - Если `method` не равен "post" или "image", отправляет `GET` запрос для получения данных очереди сессии.

    ASCII flowchart:

    Начало --> Установка заголовков
    Установка заголовков --> Проверка method
    Проверка method --(method == "post")--> POST запрос (текст)
    Проверка method --(method == "image")--> POST запрос (изображение)
    Проверка method --(else)--> GET запрос
    POST запрос (текст) --> Конец
    POST запрос (изображение) --> Конец
    GET запрос --> Конец
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
    media: MediaListType = None,
    prompt: str = None,
    proxy: str = None,
    cookies: Cookies = None,
    api_key: str = None,
    zerogpu_uuid: str = "[object Object]",
    return_conversation: bool = False,
    conversation: JsonConversation = None,
    seed: int = None,
    **kwargs
) -> AsyncResult:
    """
    Создает асинхронный генератор для взаимодействия с моделью.

    Args:
        model (str): Имя модели.
        messages (Messages): Список сообщений для отправки модели.
        media (MediaListType, optional): Список медиафайлов для отправки модели. По умолчанию `None`.
        prompt (str, optional): Текст запроса. По умолчанию `None`.
        proxy (str, optional): Адрес прокси-сервера. По умолчанию `None`.
        cookies (Cookies, optional): Файлы cookie для отправки с запросом. По умолчанию `None`.
        api_key (str, optional): Ключ API. По умолчанию `None`.
        zerogpu_uuid (str, optional): UUID для ZeroGPU. По умолчанию "[object Object]".
        return_conversation (bool, optional): Возвращать ли объект разговора. По умолчанию `False`.
        conversation (JsonConversation, optional): Объект, содержащий информацию о текущем разговоре. По умолчанию `None`.
        seed (int, optional): Зерно для генерации случайных чисел. По умолчанию `None`.
        **kwargs: Дополнительные аргументы.

    Yields:
        AsyncResult: Асинхронный результат от API.

    Как работает функция:

    1.  **Определение метода запроса**:
        *   Если указана модель для генерации изображений (`model == cls.default_image_model`) или передан `prompt`, устанавливается метод `"image"`. В противном случае используется метод `"post"`.

    2.  **Форматирование запроса**:
        *   Если `prompt` не передан и `conversation` не задан, `messages` форматируются в строку запроса с использованием `format_prompt`.
        *   Если `prompt` уже задан, он форматируется для включения медиа-данных с помощью `format_image_prompt`.

    3.  **Инициализация сессии и UUID**:
        *   Если `seed` не предоставлен, генерируется случайное целое число.
        *   Если `conversation` не передан или у него отсутствует `session_hash`, генерируется новый UUID для `session_hash` и создается объект `JsonConversation`.
        *   Если `conversation` предоставлен, обновляется `zerogpu_token` в объекте `conversation`.

    4.  **Обработка медиа-данных**:
        *   Если `media` предоставлены, они кодируются в байты и отправляются на сервер для загрузки.
        *   После успешной загрузки формируется список URL медиа-файлов.

    5.  **Выполнение запросов и потоковая обработка**:
        *   Выполняется основной запрос к API с использованием метода `cls.run`.
        *   Полученные данные обрабатываются построчно. Каждая строка декодируется и анализируется как JSON.
        *   В зависимости от типа сообщения (`msg`) генерируются различные типы результатов:
            *   `log`: `Reasoning` с информацией о статусе.
            *   `progress`: `Reasoning` с информацией о прогрессе.
            *   `heartbeat`: `Reasoning` с индикатором генерации.
            *   `process_completed`: Завершение процесса. Если в выводе есть ошибки, выбрасывается исключение `ResponseError`. Если есть данные изображения, возвращается `ImageResponse`.

    6.  **Обработка ошибок JSON**:
        *   При ошибке декодирования JSON сообщения в потоке выполняется логирование ошибки.

    ASCII flowchart:

    Определение метода запроса --> Форматирование запроса
    Форматирование запроса --> Инициализация сессии и UUID
    Инициализация сессии и UUID --> Обработка медиа-данных
    Обработка медиа-данных --> Выполнение запросов и потоковая обработка
    Выполнение запросов и потоковая обработка --> Обработка ошибок JSON
    Обработка ошибок JSON --> Завершение

    """
    ...
```

### `get_zerogpu_token`

```python
async def get_zerogpu_token(space: str, session: StreamSession, conversation: JsonConversation, cookies: Cookies = None):
    """
    Получает токен ZeroGPU и UUID сессии.

    Args:
        space (str): Имя пространства Hugging Face.
        session (StreamSession): Асинхровая сессия для выполнения запросов.
        conversation (JsonConversation): Объект, содержащий информацию о текущем разговоре.
        cookies (Cookies, optional): Файлы cookie для отправки с запросом. По умолчанию `None`.

    Returns:
        tuple[str | None, str]: Кортеж, содержащий UUID и токен ZeroGPU.

    Как работает функция:
    1. Функция пытается получить токен ZeroGPU и UUID сессии из пространства Hugging Face.
    2. Если UUID сессии не передан, функция отправляет GET-запрос к странице пространства и извлекает токен и UUID из HTML-кода страницы с использованием регулярных выражений.
    3. Если переданы cookies, функция также отправляет GET-запрос к API Hugging Face для получения токена, используя текущее время UTC + 10 минут в качестве времени истечения срока действия токена.

    ASCII flowchart:

    Начало --> Проверка UUID сессии
    Проверка UUID сессии --(UUID is None)--> GET запрос к странице пространства
    Проверка UUID сессии --(UUID is not None)--> Проверка cookies
    GET запрос к странице пространства --> Извлечение токена и UUID из HTML
    Извлечение токена и UUID из HTML --> Проверка cookies
    Проверка cookies --(cookies is not None)--> GET запрос к API Hugging Face
    GET запрос к API Hugging Face --> Получение токена из JSON
    Проверка cookies --(cookies is None)--> Возврат UUID и токена
    Получение токена из JSON --> Возврат UUID и токена
    """
    ...