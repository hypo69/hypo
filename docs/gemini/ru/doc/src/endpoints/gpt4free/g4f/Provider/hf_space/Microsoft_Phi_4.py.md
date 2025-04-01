# Модуль Microsoft_Phi_4

## Обзор

Модуль `Microsoft_Phi_4` предоставляет асинхронный интерфейс для взаимодействия с мультимодальной моделью `phi-4` от Microsoft, размещенной на платформе Hugging Face Spaces. Он поддерживает отправку текстовых и графических запросов к модели и получение ответов в потоковом режиме.

## Подробнее

Модуль использует асинхронные запросы для обмена данными с API Hugging Face Spaces, предоставляя возможность отправлять текстовые подсказки и медиафайлы (изображения) для получения ответов от модели `phi-4`. Он включает в себя функции для форматирования подсказок, загрузки медиафайлов и обработки потоковых ответов от API.

## Классы

### `Microsoft_Phi_4`

**Описание**: Класс `Microsoft_Phi_4` является асинхронным провайдером и реализует взаимодействие с моделью `Microsoft Phi-4`. Он наследует функциональность от `AsyncGeneratorProvider` и `ProviderModelMixin`.

**Наследует**:
- `AsyncGeneratorProvider`: Обеспечивает асинхронную генерацию данных.
- `ProviderModelMixin`: Предоставляет общие методы для работы с моделями провайдера.

**Атрибуты**:
- `label` (str): Метка провайдера, `"Microsoft Phi-4"`.
- `space` (str): Имя пространства на Hugging Face, `"microsoft/phi-4-multimodal"`.
- `url` (str): URL пространства на Hugging Face, `"https://huggingface.co/spaces/{space}"`.
- `api_url` (str): Базовый URL API, `"https://microsoft-phi-4-multimodal.hf.space"`.
- `referer` (str): Referer для HTTP-запросов, `"{api_url}?__theme=light"`.
- `working` (bool): Указывает, работает ли провайдер, `True`.
- `supports_stream` (bool): Поддерживает ли потоковую передачу, `True`.
- `supports_system_message` (bool): Поддерживает ли системные сообщения, `True`.
- `supports_message_history` (bool): Поддерживает ли историю сообщений, `True`.
- `default_model` (str): Модель по умолчанию, `"phi-4-multimodal"`.
- `default_vision_model` (str): Модель для работы с изображениями по умолчанию, `"phi-4-multimodal"`.
- `model_aliases` (dict): Псевдонимы моделей, `{"phi-4": default_vision_model}`.
- `vision_models` (list): Список моделей для работы с изображениями.
- `models` (list): Список поддерживаемых моделей.

**Методы**:
- `run(method: str, session: StreamSession, prompt: str, conversation: JsonConversation, media: list = None)`: Выполняет HTTP-запросы к API в зависимости от указанного метода.
- `create_async_generator(model: str, messages: Messages, media: MediaListType = None, prompt: str = None, proxy: str = None, cookies: Cookies = None, api_key: str = None, zerogpu_uuid: str = "[object Object]", return_conversation: bool = False, conversation: JsonConversation = None, **kwargs)`: Создает асинхронный генератор для взаимодействия с моделью.

### `Microsoft_Phi_4.run`

```python
@classmethod
def run(cls, method: str, session: StreamSession, prompt: str, conversation: JsonConversation, media: list = None):
    """
    Выполняет HTTP-запросы к API в зависимости от указанного метода.

    Args:
        method (str): Метод запроса (`"predict"`, `"post"` или `"get"`).
        session (StreamSession): Асинхровая сессия для выполнения запросов.
        prompt (str): Текстовый запрос.
        conversation (JsonConversation): Объект, содержащий информацию о сессии и токены.
        media (list, optional): Список медиафайлов для отправки. По умолчанию `None`.

    Returns:
        StreamResponse: Объект ответа от API.

    Как работает функция:
    1. Функция `run` выполняет HTTP-запросы к API в зависимости от переданного метода (`method`).
    2. Она использует предоставленную `StreamSession` для выполнения асинхронных запросов.
    3. В зависимости от метода, она отправляет `POST` или `GET` запросы к соответствующим эндпоинтам API.
    4. Заголовки запроса включают `content-type`, `x-zerogpu-token`, `x-zerogpu-uuid` и `referer`.

    ASCII Flowchart:

    method (predict, post, get)
    |
    switch method
    |
    case "predict": POST запрос к f"{cls.api_url}/gradio_api/run/predict"
    case "post": POST запрос к f"{cls.api_url}/gradio_api/queue/join?__theme=light"
    case "get": GET запрос к f"{cls.api_url}/gradio_api/queue/data?session_hash={conversation.session_hash}"
    |
    return response
    """
    ...
```

### `Microsoft_Phi_4.create_async_generator`

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
    """
    Создает асинхронный генератор для взаимодействия с моделью.

    Args:
        model (str): Имя модели.
        messages (Messages): Список сообщений для формирования запроса.
        media (MediaListType, optional): Список медиафайлов для отправки. По умолчанию `None`.
        prompt (str, optional): Текстовый запрос. По умолчанию `None`.
        proxy (str, optional): URL прокси-сервера. По умолчанию `None`.
        cookies (Cookies, optional): Файлы cookie для отправки с запросом. По умолчанию `None`.
        api_key (str, optional): API-ключ для доступа к модели. По умолчанию `None`.
        zerogpu_uuid (str, optional): UUID для ZeroGPU. По умолчанию `"[object Object]"`.
        return_conversation (bool, optional): Возвращать ли объект `conversation`. По умолчанию `False`.
        conversation (JsonConversation, optional): Объект для хранения информации о диалоге. По умолчанию `None`.
        **kwargs: Дополнительные аргументы.

    Returns:
        AsyncResult: Асинхронный генератор, возвращающий ответы от модели.

    Как работает функция:
    1. Функция `create_async_generator` создает асинхронный генератор для взаимодействия с моделью `phi-4`.
    2. Она форматирует текстовые подсказки и медиафайлы для отправки в API.
    3. Функция получает или создает идентификатор сессии (`session_hash`) для отслеживания разговора.
    4. Она создает `StreamSession` для выполнения асинхронных запросов.
    5. Если `api_key` не предоставлен, функция получает `zerogpu_uuid` и `api_key` с использованием `get_zerogpu_token`.
    6. Если `conversation` не предоставлен, функция создает `JsonConversation` для хранения информации о диалоге.
    7. Если `return_conversation` установлен в `True`, функция возвращает объект `conversation`.
    8. Если `media` предоставлены, функция загружает медиафайлы на сервер и получает их URL.
    9. Она вызывает `cls.run` для отправки запросов `"predict"`, `"post"` и `"get"` к API и обрабатывает потоковый ответ, извлекая содержимое из JSON.

    ASCII Flowchart:

    messages, media, prompt, proxy, cookies, api_key, zerogpu_uuid, return_conversation, conversation
    |
    format_prompt(messages) -> prompt
    format_image_prompt(messages, prompt) -> prompt
    |
    session_hash = uuid.uuid4().hex
    |
    StreamSession(proxy=proxy, impersonate="chrome") -> session
    |
    api_key is None?
    |
    Yes -> get_zerogpu_token(cls.space, session, conversation, cookies) -> zerogpu_uuid, api_key
    |
    conversation is None?
    |
    Yes -> JsonConversation(session_hash=session_hash, zerogpu_token=api_key, zerogpu_uuid=zerogpu_uuid) -> conversation
    |
    return_conversation?
    |
    Yes -> yield conversation
    |
    media is not None?
    |
    Yes -> upload media files to server -> image_files
    |
    cls.run("predict", session, prompt, conversation, media) -> response
    cls.run("post", session, prompt, conversation, media) -> response
    cls.run("get", session, prompt, conversation) -> response
    |
    process stream response and yield content
    """
    ...
```
## Функции

### `get_zerogpu_token`

Эта функция импортируется из модуля `.DeepseekAI_JanusPro7b` и используется для получения токена ZeroGPU, необходимого для аутентификации при использовании сервиса.

## Примеры

```python
# Пример использования класса Microsoft_Phi_4
messages = [{"role": "user", "content": "Hello, Phi-4!"}]
model = "phi-4-multimodal"

async def main():
    async for response in Microsoft_Phi_4.create_async_generator(model=model, messages=messages):
        print(response)

# Пример отправки изображения
media = [("path_to_image.jpg", "image.jpg")]
async def main():
    async for response in Microsoft_Phi_4.create_async_generator(model=model, messages=messages, media=media):
        print(response)