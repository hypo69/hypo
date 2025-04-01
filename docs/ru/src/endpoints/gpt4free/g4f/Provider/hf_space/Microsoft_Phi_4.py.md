# Модуль Microsoft_Phi_4

## Обзор

Модуль `Microsoft_Phi_4` предоставляет асинхронный интерфейс для взаимодействия с моделью Microsoft Phi-4 Multimodal, размещенной на платформе Hugging Face Spaces. Он позволяет отправлять текстовые и медиа-сообщения, а также получать ответы от модели в режиме реального времени.

## Подробней

Этот модуль является частью проекта `hypotez` и предназначен для интеграции с AI-моделью Microsoft Phi-4. Он использует асинхронные запросы для обеспечения неблокирующего взаимодействия с API модели. Модуль поддерживает отправку как текстовых, так и мультимедийных запросов, а также предоставляет возможность работы с историей сообщений и системными сообщениями.

## Классы

### `Microsoft_Phi_4`

**Описание**: Класс `Microsoft_Phi_4` реализует асинхронного провайдера для взаимодействия с моделью Microsoft Phi-4 Multimodal.

**Наследует**:
- `AsyncGeneratorProvider`: Обеспечивает асинхронную генерацию ответов.
- `ProviderModelMixin`: Предоставляет функциональность для работы с моделями провайдера.

**Атрибуты**:
- `label` (str): Метка провайдера ("Microsoft Phi-4").
- `space` (str): Имя пространства на Hugging Face ("microsoft/phi-4-multimodal").
- `url` (str): URL пространства на Hugging Face.
- `api_url` (str): URL API для взаимодействия с моделью.
- `referer` (str): Referer для HTTP-запросов.
- `working` (bool): Указывает, что провайдер работает.
- `supports_stream` (bool): Указывает, что провайдер поддерживает потоковую передачу.
- `supports_system_message` (bool): Указывает, что провайдер поддерживает системные сообщения.
- `supports_message_history` (bool): Указывает, что провайдер поддерживает историю сообщений.
- `default_model` (str): Модель по умолчанию ("phi-4-multimodal").
- `default_vision_model` (str): Модель для обработки изображений по умолчанию.
- `model_aliases` (dict): Псевдонимы моделей.
- `vision_models` (list): Список моделей для обработки изображений.
- `models` (list): Список поддерживаемых моделей.

**Методы**:
- `run(method: str, session: StreamSession, prompt: str, conversation: JsonConversation, media: list = None)`: Выполняет HTTP-запрос к API модели.
- `create_async_generator(model: str, messages: Messages, media: MediaListType = None, prompt: str = None, proxy: str = None, cookies: Cookies = None, api_key: str = None, zerogpu_uuid: str = "[object Object]", return_conversation: bool = False, conversation: JsonConversation = None, **kwargs)`: Создает асинхронный генератор для получения ответов от модели.

## Функции

### `run`

```python
@classmethod
def run(cls, method: str, session: StreamSession, prompt: str, conversation: JsonConversation, media: list = None):
    """
    Выполняет HTTP-запрос к API модели.

    Args:
        method (str): HTTP-метод ("predict", "post" или "get").
        session (StreamSession): Асинхронная сессия для выполнения запросов.
        prompt (str): Текст запроса.
        conversation (JsonConversation): Объект, содержащий информацию о сессии и токены.
        media (list, optional): Список медиа-файлов для отправки. По умолчанию `None`.

    Returns:
        aiohttp.ClientResponse: Объект ответа от сервера.

    Как работает функция:
    1. Функция `run` принимает параметры, необходимые для выполнения HTTP-запроса к API Microsoft Phi-4 Multimodal.
    2. В зависимости от значения параметра `method`, функция выполняет разные типы запросов:
       - Если `method` равен "predict", выполняется POST-запрос к `/gradio_api/run/predict` для отправки текстового запроса.
       - Если `method` равен "post", выполняется POST-запрос к `/gradio_api/queue/join` для отправки запроса с медиа-файлами.
       - Если `method` равен "get", выполняется GET-запрос к `/gradio_api/queue/data` для получения потока данных.
    3. Функция добавляет необходимые заголовки, включая токены авторизации и информацию о сессии.
    4. Возвращает объект ответа от сервера.

    ASCII flowchart:

    Начало
     │
     ├─── method == "predict"? ── Да ── POST /gradio_api/run/predict
     │   │
     │   └─── Нет
     │
     ├─── method == "post"? ───── Да ── POST /gradio_api/queue/join
     │   │
     │   └─── Нет
     │
     └─── GET /gradio_api/queue/data
     │
    Конец
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
    **kwargs
) -> AsyncResult:
    """
    Создает асинхронный генератор для получения ответов от модели.

    Args:
        model (str): Название модели.
        messages (Messages): Список сообщений для отправки.
        media (MediaListType, optional): Список медиа-файлов для отправки. По умолчанию `None`.
        prompt (str, optional): Текст запроса. По умолчанию `None`.
        proxy (str, optional): URL прокси-сервера. По умолчанию `None`.
        cookies (Cookies, optional): Cookies для отправки. По умолчанию `None`.
        api_key (str, optional): API-ключ. По умолчанию `None`.
        zerogpu_uuid (str, optional): UUID для ZeroGPU. По умолчанию "[object Object]".
        return_conversation (bool, optional): Возвращать ли объект разговора. По умолчанию `False`.
        conversation (JsonConversation, optional): Объект разговора. По умолчанию `None`.

    Yields:
        str: Ответ от модели.

    Raises:
        ResponseError: Если в ответе от сервера содержится ошибка.

    Как работает функция:
    1. Функция `create_async_generator` создает асинхронный генератор, который позволяет получать ответы от модели Microsoft Phi-4 Multimodal в режиме реального времени.
    2. Сначала функция форматирует запрос, объединяя сообщения и текст запроса.
    3. Затем создается или используется существующий объект `JsonConversation` для хранения информации о сессии.
    4. Если переданы медиа-файлы, они загружаются на сервер.
    5. Далее выполняются последовательные запросы к API модели:
       - "predict": Отправка запроса на предсказание.
       - "post": Отправка данных.
       - "get": Получение потока данных с ответом.
    6. Функция обрабатывает поток данных, извлекая ответы от модели из JSON-ответов.
    7. Если в ответе содержится ошибка, выбрасывается исключение `ResponseError`.
    8. Генератор возвращает текст ответа от модели.

    ASCII flowchart:

    Начало
     │
     ├─── Форматирование запроса
     │
     ├─── Создание/использование JsonConversation
     │
     ├─── media is not None? ── Да ── Загрузка медиа-файлов
     │   │
     │   └─── Нет
     │
     ├─── cls.run("predict")
     │
     ├─── cls.run("post")
     │
     ├─── cls.run("get")
     │
     ├─── Обработка потока данных
     │
     ├─── Обнаружена ошибка? ── Да ── ResponseError
     │   │
     │   └─── Нет
     │
     └─── yield ответ
     │
    Конец
    """
    ...
```

**Примеры**:
```python
# Пример использования create_async_generator
async def example():
    messages = [{"role": "user", "content": "Hello, Phi-4!"}]
    async for response in Microsoft_Phi_4.create_async_generator(
        model="phi-4-multimodal",
        messages=messages
    ):
        print(response)

# Запуск примера (необходим асинхронный контекст)
# asyncio.run(example())