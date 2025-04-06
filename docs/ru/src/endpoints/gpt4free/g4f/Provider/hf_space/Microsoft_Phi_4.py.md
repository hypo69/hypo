# Модуль `Microsoft_Phi_4`

## Обзор

Модуль `Microsoft_Phi_4` предоставляет класс `Microsoft_Phi_4`, который является асинхронным провайдером для взаимодействия с мультимодальной моделью Microsoft Phi-4, размещенной на платформе Hugging Face Spaces. Этот модуль поддерживает потоковую передачу данных, использование системных сообщений и истории сообщений, а также работу с изображениями.

## Подробней

Модуль обеспечивает подключение к API Microsoft Phi-4 через Hugging Face Spaces. Он использует асинхронные запросы для отправки и получения данных, поддерживает загрузку изображений и предоставляет возможность получения ответов в режиме реального времени через потоковую передачу.

## Классы

### `Microsoft_Phi_4`

**Описание**: Класс `Microsoft_Phi_4` является асинхронным провайдером для мультимодальной модели Microsoft Phi-4.

**Наследует**:
- `AsyncGeneratorProvider`: Обеспечивает асинхронную генерацию данных.
- `ProviderModelMixin`: Предоставляет общие методы для работы с моделями провайдеров.

**Атрибуты**:
- `label` (str): Метка провайдера (Microsoft Phi-4).
- `space` (str): Имя пространства на Hugging Face (microsoft/phi-4-multimodal).
- `url` (str): URL пространства на Hugging Face.
- `api_url` (str): Базовый URL API.
- `referer` (str): Referer для HTTP-запросов.
- `working` (bool): Указывает, работает ли провайдер.
- `supports_stream` (bool): Поддержка потоковой передачи данных.
- `supports_system_message` (bool): Поддержка системных сообщений.
- `supports_message_history` (bool): Поддержка истории сообщений.
- `default_model` (str): Модель по умолчанию (phi-4-multimodal).
- `default_vision_model` (str): Модель для работы с изображениями по умолчанию.
- `model_aliases` (dict): Псевдонимы моделей.
- `vision_models` (list): Список моделей для работы с изображениями.
- `models` (list): Список поддерживаемых моделей.

**Методы**:
- `run`: Выполняет HTTP-запрос к API.
- `create_async_generator`: Создает асинхронный генератор для взаимодействия с моделью.

## Функции

### `run`

```python
@classmethod
def run(cls, method: str, session: StreamSession, prompt: str, conversation: JsonConversation, media: list = None):
    """Выполняет HTTP-запрос к API в зависимости от указанного метода.

    Args:
        cls (Microsoft_Phi_4): Класс Microsoft_Phi_4.
        method (str): Метод запроса (predict, post, get).
        session (StreamSession): Асинхронная сессия для выполнения запросов.
        prompt (str): Текст запроса.
        conversation (JsonConversation): Объект, содержащий информацию о текущем диалоге.
        media (list, optional): Список медиафайлов для отправки. По умолчанию None.

    Returns:
        StreamResponse: Объект ответа от API.

    Как работает функция:
    1.  Формирует заголовки запроса, включая токен и UUID сессии.
    2.  В зависимости от значения `method` выполняет `POST` или `GET` запрос к соответствующему endpoint API.
    3.  Для `predict` и `post` методов формирует JSON-данные с учетом текста запроса и медиафайлов.
    4.  Возвращает объект `StreamResponse`, содержащий ответ от API.

    Внутренние функции:
    - Отсутствуют

    ASCII flowchart:

    Заголовки запроса (headers)
    │
    └─── Определение метода запроса (method)
        │
        ├─── "predict": POST запрос к /gradio_api/run/predict
        │   │   JSON данные (data)
        │   │
        ├─── "post": POST запрос к /gradio_api/queue/join
        │   │   JSON данные (data)
        │   │
        └─── "get": GET запрос к /gradio_api/queue/data
            │
            └─── StreamResponse

    Примеры:
        # Пример вызова функции run с методом "predict"
        >>> Microsoft_Phi_4.run("predict", session, "Hello", conversation, media=[])

        # Пример вызова функции run с методом "post"
        >>> Microsoft_Phi_4.run("post", session, "Hello", conversation, media=[{"file": "image.jpg"}])

        # Пример вызова функции run с методом "get"
        >>> Microsoft_Phi_4.run("get", session, "Hello", conversation)
    """
    headers = {
        "content-type": "application/json",
        "x-zerogpu-token": conversation.zerogpu_token,
        "x-zerogpu-uuid": conversation.zerogpu_uuid,
        "referer": cls.referer,
    }
    if method == "predict":
        return session.post(f"{cls.api_url}/gradio_api/run/predict", **{
            "headers": {k: v for k, v in headers.items() if v is not None},
            "json": {
                "data":[
                    [],
                    {
                        "text": prompt,
                        "files": media,
                    },
                    None
                ],
                "event_data": None,
                "fn_index": 10,
                "trigger_id": 8,
                "session_hash": conversation.session_hash
            },
        })
    if method == "post":
        return session.post(f"{cls.api_url}/gradio_api/queue/join?__theme=light", **{
            "headers": {k: v for k, v in headers.items() if v is not None},
            "json": {
                "data": [[\
                        {\
                        "role": "user",\
                        "content": prompt,\
                        }\
                    ]] + [[\
                        {\
                            "role": "user",\
                            "content": {"file": image}\
                        } for image in media\
                    ]],
                "event_data": None,
                "fn_index": 11,
                "trigger_id": 8,
                "session_hash": conversation.session_hash
            },
        })
    return session.get(f"{cls.api_url}/gradio_api/queue/data?session_hash={conversation.session_hash}", **{
        "headers": {
            "accept": "text/event-stream",
            "content-type": "application/json",
            "referer": cls.referer,
        }
    })
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
    """Создает асинхронный генератор для взаимодействия с моделью Microsoft Phi-4.

    Args:
        cls (Microsoft_Phi_4): Класс Microsoft_Phi_4.
        model (str): Название модели.
        messages (Messages): Список сообщений для отправки.
        media (MediaListType, optional): Список медиафайлов. По умолчанию None.
        prompt (str, optional): Текст запроса. По умолчанию None.
        proxy (str, optional): Прокси-сервер. По умолчанию None.
        cookies (Cookies, optional): Cookies для отправки. По умолчанию None.
        api_key (str, optional): API ключ. По умолчанию None.
        zerogpu_uuid (str, optional): UUID для ZeroGPU. По умолчанию "[object Object]".
        return_conversation (bool, optional): Возвращать ли объект Conversation. По умолчанию False.
        conversation (JsonConversation, optional): Объект JsonConversation. По умолчанию None.
        **kwargs: Дополнительные аргументы.

    Returns:
        AsyncResult: Асинхронный генератор, возвращающий ответы от API.

    Как работает функция:
    1.  Форматирует запрос на основе предоставленных сообщений и промпта.
    2.  Создает или использует существующий `session_hash` для идентификации сессии.
    3.  Инициализирует асинхронную сессию `StreamSession` с учетом прокси.
    4.  Если `api_key` не предоставлен, получает его и `zerogpu_uuid` с использованием `get_zerogpu_token`.
    5.  Создает или обновляет объект `JsonConversation` с информацией о сессии и токенах.
    6.  Загружает медиафайлы на сервер, если они предоставлены, и формирует список файлов для запроса.
    7.  Выполняет последовательность запросов к API (`predict`, `post`, `get`) для получения ответа.
    8.  Преобразует ответы от API и возвращает контент в виде асинхронного генератора.

    Внутренние функции:
    - Отсутствуют

    ASCII flowchart:

    Форматирование запроса (prompt)
    │
    └─── Создание/использование session_hash
        │
        └─── Инициализация StreamSession
            │
            ├─── Получение API ключа и UUID (если необходимо)
            │   │   └─── get_zerogpu_token
            │   │
            └─── Создание/обновление JsonConversation
                │
                ├─── Загрузка медиафайлов (если необходимо)
                │   │   └─── POST запрос к /gradio_api/upload
                │   │
                └─── Выполнение API запросов
                    │
                    ├─── "predict": cls.run
                    │
                    ├─── "post": cls.run
                    │
                    └─── "get": cls.run
                        │
                        └─── Преобразование и возврат контента

    Примеры:
        # Пример создания async generator с минимальными параметрами
        >>> async for message in Microsoft_Phi_4.create_async_generator(model="phi-4-multimodal", messages=[{"role": "user", "content": "Hello"}]):
        ...     print(message)

        # Пример создания async generator с media
        >>> async for message in Microsoft_Phi_4.create_async_generator(model="phi-4-multimodal", messages=[{"role": "user", "content": "image"}], media=[("data", "image.jpg")]):
        ...     print(message)
    """
    prompt = format_prompt(messages) if prompt is None and conversation is None else prompt
    prompt = format_image_prompt(messages, prompt)

    session_hash = uuid.uuid4().hex if conversation is None else getattr(conversation, "session_hash", uuid.uuid4().hex)
    async with StreamSession(proxy=proxy, impersonate="chrome") as session:
        if api_key is None:
            zerogpu_uuid, api_key = await get_zerogpu_token(cls.space, session, conversation, cookies)
        if conversation is None or not hasattr(conversation, "session_hash"):
            conversation = JsonConversation(session_hash=session_hash, zerogpu_token=api_key, zerogpu_uuid=zerogpu_uuid)
        else:
            conversation.zerogpu_token = api_key
        if return_conversation:
            yield conversation

        if media is not None:
            data = FormData()
            mime_types = [None for i in range(len(media))]\
            for i in range(len(media)):
                mime_types[i] = is_data_an_audio(media[i][0], media[i][1])
                media[i] = (to_bytes(media[i][0]), media[i][1])
                mime_types[i] = is_accepted_format(media[i][0]) if mime_types[i] is None else mime_types[i]
            for image, image_name in media:
                data.add_field(f"files", to_bytes(image), filename=image_name)
            async with session.post(f"{cls.api_url}/gradio_api/upload", params={"upload_id": session_hash}, data=data) as response:
                await raise_for_status(response)
                image_files = await response.json()
            media = [{\
                "path": image_file,\
                "url": f"{cls.api_url}/gradio_api/file={image_file}",\
                "orig_name": media[i][1],\
                "size": len(media[i][0]),\
                "mime_type": mime_types[i],\
                "meta": {\
                    "_type": "gradio.FileData"\
                }\
            } for i, image_file in enumerate(image_files)]
        
        
        async with cls.run("predict", session, prompt, conversation, media) as response:
            await raise_for_status(response)

        async with cls.run("post", session, prompt, conversation, media) as response:
            await raise_for_status(response)

        async with cls.run("get", session, prompt, conversation) as response:
            response: StreamResponse = response
            async for line in response.iter_lines():
                if line.startswith(b'data: '):\
                    try:\
                        json_data = json.loads(line[6:])
                        if json_data.get('msg') == 'process_completed':
                            if 'output' in json_data and 'error' in json_data['output']:
                                raise ResponseError(json_data['output']['error'])
                            if 'output' in json_data and 'data' in json_data['output']:
                                yield json_data['output']['data'][0][-1]["content"]
                            break

                    except json.JSONDecodeError:\
                        debug.log("Could not parse JSON:", line.decode(errors="replace"))