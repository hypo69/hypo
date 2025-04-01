# Модуль DeepseekAI_JanusPro7b

## Обзор

Модуль `DeepseekAI_JanusPro7b` предназначен для взаимодействия с моделью DeepseekAI Janus-Pro-7B, размещенной на платформе Hugging Face Spaces. Он обеспечивает асинхронную генерацию текста и изображений с использованием API Hugging Face. Модуль поддерживает потоковую передачу данных, системные сообщения и историю сообщений.

## Подробней

Модуль использует классы `AsyncGeneratorProvider` и `ProviderModelMixin` для реализации асинхронного взаимодействия с API. Он поддерживает как текстовые, так и графические запросы к модели Janus-Pro-7B. Для аутентификации используется токен `zerogpu`, который получается динамически.

## Классы

### `DeepseekAI_JanusPro7b`

**Описание**: Класс реализует взаимодействие с моделью DeepseekAI Janus-Pro-7B.

**Наследует**:
- `AsyncGeneratorProvider`: Обеспечивает асинхронную генерацию данных.
- `ProviderModelMixin`: Предоставляет общие методы для работы с моделями.

**Атрибуты**:
- `label` (str): Метка провайдера "DeepseekAI Janus-Pro-7B".
- `space` (str): Имя пространства Hugging Face "deepseek-ai/Janus-Pro-7B".
- `url` (str): URL пространства Hugging Face.
- `api_url` (str): URL API Hugging Face Space.
- `referer` (str): Referer для HTTP-запросов.
- `working` (bool): Флаг, указывающий на работоспособность провайдера.
- `supports_stream` (bool): Флаг, указывающий на поддержку потоковой передачи данных.
- `supports_system_message` (bool): Флаг, указывающий на поддержку системных сообщений.
- `supports_message_history` (bool): Флаг, указывающий на поддержку истории сообщений.
- `default_model` (str): Модель по умолчанию "janus-pro-7b".
- `default_image_model` (str): Модель для генерации изображений по умолчанию "janus-pro-7b-image".
- `default_vision_model` (str): Модель для обработки изображений по умолчанию.
- `image_models` (list[str]): Список моделей для генерации изображений.
- `vision_models` (list[str]): Список моделей для обработки изображений.
- `models` (list[str]): Список всех поддерживаемых моделей.

**Методы**:
- `run`: Выполняет HTTP-запрос к API Hugging Face Space.
- `create_async_generator`: Создает асинхронный генератор для получения ответов от модели.

## Функции

### `run`

```python
    @classmethod
    def run(cls, method: str, session: StreamSession, prompt: str, conversation: JsonConversation, image: dict = None, seed: int = 0):
        """
        Выполняет HTTP-запрос к API Hugging Face Space.

        Args:
            method (str): HTTP-метод ("post" или "image" или "get").
            session (StreamSession): Асинхронная сессия для выполнения запросов.
            prompt (str): Текст запроса.
            conversation (JsonConversation): Объект, содержащий информацию о текущем диалоге.
            image (dict, optional): Данные изображения для запроса. По умолчанию `None`.
            seed (int, optional): Зерно для генерации случайных чисел. По умолчанию `0`.

        Returns:
            StreamResponse: Объект ответа от API.

        Как работает функция:
        1.  Функция `run` выполняет HTTP-запросы к API Hugging Face Space для взаимодействия с моделью DeepseekAI Janus-Pro-7B.
        2.  В зависимости от значения параметра `method`, функция отправляет `POST` или `GET` запросы.
        3.  При `method == "post"` формируется `POST` запрос с данными для генерации текста, включающими промпт, seed, параметры генерации и метаданные сессии.
        4.  При `method == "image"` формируется `POST` запрос с данными для генерации изображения, включающими промпт, seed и параметры.
        5.  При `method == "get"` формируется `GET` запрос для получения потока данных с результатами генерации.
        6.  Заголовки запроса содержат информацию о типе контента, токене `zerogpu`, UUID и referer.

        ASCII flowchart:

        Начало --> Проверка метода
        Проверка метода --> (метод == "post") ? POST запрос для генерации текста : Далее
        Далее --> (метод == "image") ? POST запрос для генерации изображения : Далее
        Далее --> (метод == "get") ? GET запрос для получения данных : Конец
        POST запрос для генерации текста --> Отправка запроса
        POST запрос для генерации изображения --> Отправка запроса
        GET запрос для получения данных --> Отправка запроса
        Отправка запроса --> Конец

        """
        headers = {
            "content-type": "application/json",
            "x-zerogpu-token": conversation.zerogpu_token,
            "x-zerogpu-uuid": conversation.zerogpu_uuid,
            "referer": cls.referer,
        }
        if method == "post":
            return session.post(f"{cls.api_url}/gradio_api/queue/join?__theme=light", **{
                "headers": {k: v for k, v in headers.items() if v is not None},
                "json": {"data":[image,prompt,seed,0.95,0.1],"event_data":None,"fn_index":2,"trigger_id":10,"session_hash":conversation.session_hash},
            })
        elif method == "image":
            return session.post(f"{cls.api_url}/gradio_api/queue/join?__theme=light", **{
                "headers": {k: v for k, v in headers.items() if v is not None},
                "json": {"data":[prompt,seed,5,1],"event_data":None,"fn_index":3,"trigger_id":20,"session_hash":conversation.session_hash},
            })
        return session.get(f"{cls.api_url}/gradio_api/queue/data?session_hash={conversation.session_hash}", **{
            "headers": {
                "accept": "text/event-stream",
                "content-type": "application/json",
                "referer": cls.referer,
            }
        })
```

**Примеры**:

```python
# Пример вызова функции run для отправки текстового запроса
# session = StreamSession()
# conversation = JsonConversation(session_hash="some_hash", zerogpu_token="some_token", zerogpu_uuid="some_uuid")
# response = DeepseekAI_JanusPro7b.run("post", session, "Hello", conversation)

# Пример вызова функции run для отправки запроса на генерацию изображения
# session = StreamSession()
# conversation = JsonConversation(session_hash="some_hash", zerogpu_token="some_token", zerogpu_uuid="some_uuid")
# response = DeepseekAI_JanusPro7b.run("image", session, "A cat", conversation)

# Пример вызова функции run для получения данных
# session = StreamSession()
# conversation = JsonConversation(session_hash="some_hash", zerogpu_token="some_token", zerogpu_uuid="some_uuid")
# response = DeepseekAI_JanusPro7b.run("get", session, "Hello", conversation)
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
        Создает асинхронный генератор для получения ответов от модели.

        Args:
            model (str): Имя модели.
            messages (Messages): Список сообщений для отправки.
            media (MediaListType, optional): Список медиафайлов для отправки. По умолчанию `None`.
            prompt (str, optional): Текст запроса. По умолчанию `None`.
            proxy (str, optional): URL прокси-сервера. По умолчанию `None`.
            cookies (Cookies, optional): HTTP-куки. По умолчанию `None`.
            api_key (str, optional): API-ключ. По умолчанию `None`.
            zerogpu_uuid (str, optional): UUID для zerogpu. По умолчанию "[object Object]".
            return_conversation (bool, optional): Флаг, указывающий, нужно ли возвращать объект conversation. По умолчанию `False`.
            conversation (JsonConversation, optional): Объект, содержащий информацию о текущем диалоге. По умолчанию `None`.
            seed (int, optional): Зерно для генерации случайных чисел. По умолчанию `None`.
            **kwargs: Дополнительные аргументы.

        Returns:
            AsyncResult: Асинхронный генератор, возвращающий результаты от модели.

        Как работает функция:
        1.  Функция `create_async_generator` создает асинхронный генератор для взаимодействия с моделью DeepseekAI Janus-Pro-7B.
        2.  Определяется метод запроса (`"post"` или `"image"`) в зависимости от типа запроса (текстовый или графический).
        3.  Формируется промпт на основе переданных сообщений или используется переданный промпт напрямую.
        4.  Создается или используется существующая сессия `StreamSession` для выполнения запросов.
        5.  Получается токен `zerogpu` и UUID, если они не были переданы.
        6.  Создается или используется существующий объект `JsonConversation` для хранения информации о диалоге.
        7.  Если переданы медиафайлы, они загружаются на сервер.
        8.  Вызывается функция `run` для отправки запроса к API.
        9.  Асинхронно обрабатывается поток данных, возвращаемый API, и извлекаются результаты.
        10. Результаты передаются через генератор в виде объектов `Reasoning` (для статуса) и `ImageResponse` (для изображений) или текста.

        ASCII flowchart:

        Начало --> Определение метода запроса
        Определение метода запроса --> Формирование промпта
        Формирование промпта --> Создание/использование сессии StreamSession
        Создание/использование сессии StreamSession --> Получение токена zerogpu и UUID (если необходимо)
        Получение токена zerogpu и UUID (если необходимо) --> Создание/использование объекта JsonConversation
        Создание/использование объекта JsonConversation --> Загрузка медиафайлов (если переданы)
        Загрузка медиафайлов (если переданы) --> Вызов функции run для отправки запроса к API
        Вызов функции run для отправки запроса к API --> Асинхронная обработка потока данных
        Асинхронная обработка потока данных --> Извлечение результатов
        Извлечение результатов --> Передача результатов через генератор
        Передача результатов через генератор --> Конец
        """
        method = "post"
        if model == cls.default_image_model or prompt is not None:
            method = "image"
        prompt = format_prompt(messages) if prompt is None and conversation is None else prompt
        prompt = format_image_prompt(messages, prompt)
        if seed is None:
            seed = random.randint(1000, 999999)

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
                for i in range(len(media)):
                    media[i] = (to_bytes(media[i][0]), media[i][1])
                for image, image_name in media:
                    data.add_field(f"files", image, filename=image_name)
                async with session.post(f"{cls.api_url}/gradio_api/upload", params={"upload_id": session_hash}, data=data) as response:
                    await raise_for_status(response)
                    image_files = await response.json()
                media = [{\
                    "path": image_file,
                    "url": f"{cls.api_url}/gradio_api/file={image_file}",
                    "orig_name": media[i][1],\
                    "size": len(media[i][0]),\
                    "mime_type": is_accepted_format(media[i][0]),
                    "meta": {
                        "_type": "gradio.FileData"
                    }
                } for i, image_file in enumerate(image_files)]

            async with cls.run(method, session, prompt, conversation, None if media is None else media.pop(), seed) as response:
                await raise_for_status(response)

            async with cls.run("get", session, prompt, conversation, None, seed) as response:
                response: StreamResponse = response
                counter = 3
                async for line in response.iter_lines():
                    decoded_line = line.decode(errors="replace")
                    if decoded_line.startswith('data: '):
                        try:
                            json_data = json.loads(decoded_line[6:])
                            if json_data.get('msg') == 'log':
                                yield Reasoning(status=json_data["log"])

                            if json_data.get('msg') == 'progress':
                                if 'progress_data' in json_data:
                                    if json_data['progress_data']:
                                        progress = json_data['progress_data'][0]
                                        yield Reasoning(status=f"{progress['desc']} {progress['index']}/{progress['length']}")
                                    else:
                                        yield Reasoning(status=f"Generating")

                            elif json_data.get('msg') == 'heartbeat':
                                yield Reasoning(status=f"Generating{''.join(['.' for i in range(counter)])}")
                                counter  += 1

                            elif json_data.get('msg') == 'process_completed':
                                if 'output' in json_data and 'error' in json_data['output']:
                                    json_data['output']['error'] = json_data['output']['error'].split(" <a ")[0]
                                    raise ResponseError("Missing images input" if json_data['output']['error'] and "AttributeError" in json_data['output']['error'] else json_data['output']['error'])
                                if 'output' in json_data and 'data' in json_data['output']:
                                    yield Reasoning(status="Finished")
                                    if "image" in json_data['output']['data'][0][0]:
                                        yield ImageResponse([image["image"]["url"] for image in json_data['output']['data'][0]], prompt)
                                    else:
                                        yield json_data['output']['data'][0]
                                break

                        except json.JSONDecodeError as ex:
                            debug.log("Could not parse JSON:", decoded_line)
```

**Примеры**:

```python
# Пример вызова функции create_async_generator для генерации текста
# messages = [{"role": "user", "content": "Hello"}]
# async for result in DeepseekAI_JanusPro7b.create_async_generator(model="janus-pro-7b", messages=messages):
#     print(result)

# Пример вызова функции create_async_generator для генерации изображения
# messages = [{"role": "user", "content": "A cat"}]
# async for result in DeepseekAI_JanusPro7b.create_async_generator(model="janus-pro-7b-image", messages=messages):
#     print(result)
```

### `get_zerogpu_token`

```python
async def get_zerogpu_token(space: str, session: StreamSession, conversation: JsonConversation, cookies: Cookies = None):
    """
    Получает токен zerogpu и UUID из Hugging Face Space.

    Args:
        space (str): Имя пространства Hugging Face.
        session (StreamSession): Асинхронная сессия для выполнения запросов.
        conversation (JsonConversation): Объект, содержащий информацию о текущем диалоге.
        cookies (Cookies, optional): HTTP-куки. По умолчанию `None`.

    Returns:
        tuple[str | None, str]: Кортеж, содержащий UUID и токен zerogpu.

    Как работает функция:
    1.  Функция `get_zerogpu_token` получает токен `zerogpu` и UUID, необходимые для аутентификации в Hugging Face Space.
    2.  Если UUID уже существует в объекте `conversation`, он используется.
    3.  Если UUID отсутствует, функция выполняет `GET` запрос к странице Hugging Face Space и извлекает токен и UUID из HTML-кода страницы с использованием регулярных выражений.
    4.  Если переданы куки, функция также отправляет `GET` запрос к API Hugging Face для получения токена, используя текущее время UTC + 10 минут в качестве параметра expiration.

    ASCII flowchart:

    Начало --> Проверка наличия UUID в conversation
    Проверка наличия UUID в conversation --> (UUID есть) ? Использовать существующий UUID : Далее
    Далее --> GET запрос к странице Hugging Face Space
    GET запрос к странице Hugging Face Space --> Извлечение токена и UUID из HTML
    Извлечение токена и UUID из HTML --> GET запрос к API Hugging Face (если есть куки)
    GET запрос к API Hugging Face (если есть куки) --> Получение токена из API
    Получение токена из API --> Конец
    """
    zerogpu_uuid = None if conversation is None else getattr(conversation, "zerogpu_uuid", None)
    zerogpu_token = "[object Object]"

    cookies = get_cookies("huggingface.co", raise_requirements_error=False) if cookies is None else cookies
    if zerogpu_uuid is None:
        async with session.get(f"https://huggingface.co/spaces/{space}", cookies=cookies) as response:
            match = re.search(r"&quot;token&quot;:&quot;([^&]+?)&quot;", await response.text())
            if match:
                zerogpu_token = match.group(1)
            match = re.search(r"&quot;sessionUuid&quot;:&quot;([^&]+?)&quot;", await response.text())
            if match:
                zerogpu_uuid = match.group(1)
    if cookies:
        # Get current UTC time + 10 minutes
        dt = (datetime.now(timezone.utc) + timedelta(minutes=10)).isoformat(timespec='milliseconds')
        encoded_dt = urllib.parse.quote(dt)
        async with session.get(f"https://huggingface.co/api/spaces/{space}/jwt?expiration={encoded_dt}&include_pro_status=true", cookies=cookies) as response:
            response_data = (await response.json())
            if "token" in response_data:
                zerogpu_token = response_data["token"]

    return zerogpu_uuid, zerogpu_token
```

**Примеры**:

```python
# Пример вызова функции get_zerogpu_token
# session = StreamSession()
# space = "deepseek-ai/Janus-Pro-7B"
# conversation = JsonConversation()
# uuid, token = await get_zerogpu_token(space, session, conversation)
# print(f"UUID: {uuid}, Token: {token}")