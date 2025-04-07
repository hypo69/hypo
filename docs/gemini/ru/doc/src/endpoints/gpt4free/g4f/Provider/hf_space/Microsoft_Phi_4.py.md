# Модуль `Microsoft_Phi_4`

## Обзор

Модуль `Microsoft_Phi_4` предоставляет асинхронный интерфейс для взаимодействия с моделью Microsoft Phi-4 Multimodal, размещенной на платформе Hugging Face Spaces. Он позволяет отправлять текстовые запросы и изображения, а также получать ответы в режиме потока.

## Подробней

Этот модуль предназначен для работы с мультимодальной моделью Microsoft Phi-4, обеспечивая возможность отправки текстовых запросов в сочетании с изображениями. Он использует асинхронные запросы для взаимодействия с API Hugging Face Spaces, обеспечивая эффективную обработку данных и потоковую передачу ответов.

## Классы

### `Microsoft_Phi_4`

**Описание**: Класс `Microsoft_Phi_4` является асинхронным провайдером и миксином моделей, предназначенным для взаимодействия с моделью Microsoft Phi-4 Multimodal.

**Наследует**:
- `AsyncGeneratorProvider`: Обеспечивает асинхронную генерацию данных.
- `ProviderModelMixin`: Предоставляет функциональность для работы с моделями провайдера.

**Атрибуты**:
- `label` (str): Метка провайдера, `"Microsoft Phi-4"`.
- `space` (str): Название пространства на Hugging Face, `"microsoft/phi-4-multimodal"`.
- `url` (str): URL пространства на Hugging Face.
- `api_url` (str): URL API для взаимодействия с моделью.
- `referer` (str): Referer для HTTP-запросов.
- `working` (bool): Указывает, работает ли провайдер.
- `supports_stream` (bool): Поддерживает ли провайдер потоковую передачу данных.
- `supports_system_message` (bool): Поддерживает ли провайдер системные сообщения.
- `supports_message_history` (bool): Поддерживает ли провайдер историю сообщений.
- `default_model` (str): Модель по умолчанию, `"phi-4-multimodal"`.
- `default_vision_model` (str): Модель для обработки изображений по умолчанию.
- `model_aliases` (dict): Псевдонимы моделей.
- `vision_models` (list): Список моделей для обработки изображений.
- `models` (list): Список поддерживаемых моделей.

### `run`

```python
 @classmethod
 def run(cls, method: str, session: StreamSession, prompt: str, conversation: JsonConversation, media: list = None):
 ```

**Назначение**: Выполняет HTTP-запросы к API Hugging Face Spaces в зависимости от указанного метода.

**Параметры**:
- `cls` (Microsoft_Phi_4): Класс, к которому принадлежит метод.
- `method` (str): Метод запроса (`"predict"`, `"post"`, `"get"`).
- `session` (StreamSession): Асинхронная сессия для выполнения HTTP-запросов.
- `prompt` (str): Текстовый запрос.
- `conversation` (JsonConversation): Объект, содержащий информацию о текущем разговоре (например, идентификаторы сессии).
- `media` (list, optional): Список медиафайлов (например, изображений) для отправки. По умолчанию `None`.

**Возвращает**:
- `aiohttp.ClientResponse`: Объект ответа от HTTP-запроса.

**Как работает функция**:
1. **Подготовка заголовков**: Создаются заголовки запроса, включающие `content-type`, `x-zerogpu-token`, `x-zerogpu-uuid` и `referer`.
2. **Выбор метода**: В зависимости от значения параметра `method`, выполняется соответствующий HTTP-запрос (`POST` или `GET`).
3. **Формирование данных запроса**: Данные запроса формируются в формате JSON и включают текстовый запрос (`prompt`), медиафайлы (`media`), идентификаторы сессии (`session_hash`) и другие параметры.
4. **Выполнение запроса**: С использованием асинхронной сессии (`session`) выполняется HTTP-запрос к API Hugging Face Spaces.

```
Запрос к API
     │
     ├── method == "predict"
     │    │
     │    └── Создание JSON payload для запроса predict
     │         │
     │         └── Отправка POST запроса на /gradio_api/run/predict
     │
     ├── method == "post"
     │    │
     │    └── Создание JSON payload для запроса post
     │         │
     │         └── Отправка POST запроса на /gradio_api/queue/join
     │
     └── method == "get"
          │
          └── Отправка GET запроса на /gradio_api/queue/data
```

**Примеры**:
```python
# Пример вызова метода run с method="predict"
response = Microsoft_Phi_4.run("predict", session, "Hello, world!", conversation, media=[])

# Пример вызова метода run с method="post"
response = Microsoft_Phi_4.run("post", session, "Translate to French.", conversation, media=[{"path": "img.jpg", "url": "url", "orig_name": "img", "size": 1000, "mime_type": "img", "meta": {}}])

# Пример вызова метода run с method="get"
response = Microsoft_Phi_4.run("get", session, "How are you?", conversation)
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
        **kwargs
    ) -> AsyncResult:
```

**Назначение**: Создает асинхронный генератор для взаимодействия с моделью Microsoft Phi-4 Multimodal.

**Параметры**:
- `cls` (Microsoft_Phi_4): Класс, к которому принадлежит метод.
- `model` (str): Название модели.
- `messages` (Messages): Список сообщений для отправки.
- `media` (MediaListType, optional): Список медиафайлов для отправки. По умолчанию `None`.
- `prompt` (str, optional): Текстовый запрос. По умолчанию `None`.
- `proxy` (str, optional): URL прокси-сервера. По умолчанию `None`.
- `cookies` (Cookies, optional): Cookies для отправки. По умолчанию `None`.
- `api_key` (str, optional): Ключ API. По умолчанию `None`.
- `zerogpu_uuid` (str, optional): UUID для ZeroGPU. По умолчанию `"[object Object]"`.
- `return_conversation` (bool, optional): Возвращать ли объект разговора. По умолчанию `False`.
- `conversation` (JsonConversation, optional): Объект разговора. По умолчанию `None`.
- `**kwargs`: Дополнительные параметры.

**Возвращает**:
- `AsyncResult`: Асинхронный генератор, возвращающий ответы от модели.

**Как работает функция**:

1. **Форматирование запроса**: Форматирует текстовый запрос (`prompt`) с учетом истории сообщений (`messages`).
2. **Инициализация сессии**: Создается асинхронная сессия (`StreamSession`) для выполнения HTTP-запросов.
3. **Получение токена**: Если `api_key` не предоставлен, получает токен ZeroGPU.
4. **Создание объекта разговора**: Создается или обновляется объект `JsonConversation`, содержащий информацию о текущем разговоре.
5. **Загрузка медиафайлов**: Если предоставлены медиафайлы (`media`), они загружаются на сервер Hugging Face Spaces.
6. **Выполнение запросов**: Выполняются последовательные HTTP-запросы (`"predict"`, `"post"`, `"get"`) к API Hugging Face Spaces для получения ответа от модели.
7. **Потоковая передача ответов**: Ответы от модели передаются в виде потока данных (`async for line in response.iter_lines()`).
8. **Обработка JSON**: Каждая строка ответа обрабатывается как JSON-данные, и извлекается полезная информация (`"content"`).
9. **Обработка ошибок**: В случае ошибок в JSON-данных или ответах от сервера, они логируются.

```
Форматирование запроса
     │
     ├── Создание/обновление JsonConversation
     │    │
     │    └── Проверка наличия медиафайлов
     │         │
     │         └── Загрузка медиафайлов на сервер
     │              │
     │              └── Выполнение запросов "predict", "post", "get"
     │                   │
     │                   └── Потоковая обработка ответов
     │                        │
     │                        └── Извлечение и передача данных "content"
     │                             │
     │                             └── Обработка ошибок
     │
     └── Возврат асинхронного генератора с ответами
```

**Примеры**:

```python
# Пример вызова create_async_generator с текстовым запросом
result = Microsoft_Phi_4.create_async_generator(
    model="phi-4-multimodal",
    messages=[{"role": "user", "content": "Hello, world!"}],
    return_conversation=True
)

# Пример вызова create_async_generator с медиафайлами
result = Microsoft_Phi_4.create_async_generator(
    model="phi-4-multimodal",
    messages=[{"role": "user", "content": "Describe this image."}],
    media=[("image_data", "image.jpg")],
    return_conversation=True
)