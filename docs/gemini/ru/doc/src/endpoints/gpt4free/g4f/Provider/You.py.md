# Модуль `You.py`

## Обзор

Модуль предоставляет асинхронный генератор для взаимодействия с сервисом You.com, позволяя использовать различные модели, включая GPT-4o, Grok-2 и другие, а также модели для генерации изображений, такие как DALL-E. Модуль поддерживает текстовые и визуальные запросы, а также загрузку изображений.

## Подробней

Этот модуль является частью проекта `hypotez` и предназначен для обеспечения интеграции с сервисом You.com для выполнения задач генерации текста и изображений. Он использует асинхронные запросы для взаимодействия с API You.com, поддерживая различные модели и режимы работы.

## Классы

### `You(AsyncGeneratorProvider, ProviderModelMixin)`

**Описание**: Класс `You` предоставляет функциональность для взаимодействия с сервисом You.com.

**Наследует**:
- `AsyncGeneratorProvider`: Обеспечивает базовую функциональность для асинхронных генераторов.
- `ProviderModelMixin`: Предоставляет методы для работы с моделями.

**Атрибуты**:
- `label` (str): Метка провайдера ("You.com").
- `url` (str): URL сервиса You.com ("https://you.com").
- `working` (bool): Флаг, указывающий на работоспособность провайдера (True).
- `default_model` (str): Модель, используемая по умолчанию ("gpt-4o-mini").
- `default_vision_model` (str): Модель для работы с изображениями по умолчанию ("agent").
- `image_models` (List[str]): Список моделей для генерации изображений (["dall-e"]).
- `models` (List[str]): Список поддерживаемых моделей.
- `_cookies` (Optional[Cookies]): Куки для авторизации.
- `_cookies_used` (int): Счетчик использованных куки.
- `_telemetry_ids` (List[str]): Список идентификаторов телеметрии.

**Методы**:
- `create_async_generator`: Создает асинхронный генератор для взаимодействия с You.com.
- `upload_file`: Загружает файл на сервер You.com.

## Функции

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
    Создает асинхронный генератор для взаимодействия с сервисом You.com.

    Args:
        model (str): Модель для использования.
        messages (Messages): Список сообщений для отправки.
        stream (bool, optional): Флаг, указывающий на использование потоковой передачи. По умолчанию True.
        image (ImageType, optional): Изображение для отправки. По умолчанию None.
        image_name (str, optional): Имя файла изображения. По умолчанию None.
        proxy (str, optional): Прокси-сервер для использования. По умолчанию None.
        timeout (int, optional): Время ожидания запроса. По умолчанию 240.
        chat_mode (str, optional): Режим чата. По умолчанию "default".
        cookies (Cookies, optional): Куки для авторизации. По умолчанию None.
        **kwargs: Дополнительные параметры.

    Returns:
        AsyncResult: Асинхронный генератор для получения ответов от сервиса You.com.

    Raises:
        MissingRequirementsError: Если отсутствуют необходимые куки и не удалось получить их автоматически.
        ResponseError: Если сервер возвращает ошибку.

    **Как работает функция**:

    1. **Определение режима чата**:
       - Определяет режим чата в зависимости от наличия изображения или выбранной модели. Если передано изображение или выбрана модель `default_vision_model`, устанавливается режим `agent`.
       - Если модель не указана или равна `default_model`, действия не выполняются.
       - Если модель начинается с `dall-e`, устанавливается режим `create` и извлекается последнее сообщение.
       - В остальных случаях устанавливается режим `custom` и получается модель с помощью `cls.get_model(model)`.

    2. **Получение куки**:
       - Если куки не переданы и режим чата не `default`, пытается получить куки из файла `.you.com`.
       - Если куки отсутствуют или не содержат `afUserId`, запускается браузер (через `get_nodriver`) для получения куки с сайта `cls.url`.

    3. **Создание сессии и отправка запроса**:
       - Создается асинхронная сессия с использованием `StreamSession` с заданными прокси и таймаутом.
       - Если передано изображение, оно загружается на сервер с помощью `cls.upload_file`.
       - Формируются заголовки и данные для запроса.
       - Отправляется GET-запрос к API `cls.url/api/streamingSearch` с параметрами и заголовками.

    4. **Обработка потока ответов**:
       - Читаются строки из ответа сервера.
       - Если строка начинается с `event:`, извлекается тип события.
       - Если строка начинается с `data:`, обрабатываются данные в зависимости от типа события:
         - `error`: Вызывается исключение `ResponseError`.
         - `youChatUpdate` или `youChatToken`: Данные загружаются из JSON.
         - `youChatToken`: Извлекается и возвращается содержимое токена.
         - `youChatUpdate`: Обрабатываются данные в зависимости от режима чата:
           - `create`: Извлекаются URL изображений из ответа и возвращаются как `ImagePreview` или `ImageResponse`.
           - В остальных случаях возвращается текст ответа.

    ```
    Определение режима чата
    │
    ├───► Получение куки
    │   │
    │   └───► Создание сессии и отправка запроса
    │       │
    │       └───► Обработка потока ответов
    │           │
    │           ├───► Обработка ошибок
    │           │
    │           ├───► Обработка обновлений чата
    │           │
    │           └───► Обработка токенов
    │
    ```

    """
    if image is not None or model == cls.default_vision_model:
        chat_mode = "agent"
    elif not model or model == cls.default_model:
        ...
    elif model.startswith("dall-e"):
        chat_mode = "create"
        messages = [messages[-1]]
    else:
        chat_mode = "custom"
        model = cls.get_model(model)
    if cookies is None and chat_mode != "default":
        try:
            cookies = get_cookies(".you.com")
        except MissingRequirementsError:
            pass
        if not cookies or "afUserId" not in cookies:
            browser, stop_browser = await get_nodriver(proxy=proxy)
            try:
                page = await browser.get(cls.url)
                await page.wait_for('[data-testid="user-profile-button"]', timeout=900)
                cookies = {}
                for c in await page.send(nodriver.cdp.network.get_cookies([cls.url])):\n                    cookies[c.name] = c.value
                await page.close()
            finally:
                stop_browser()
    async with StreamSession(
        proxy=proxy,
        impersonate="chrome",
        timeout=(30, timeout)
    ) as session:
        upload = ""
        if image is not None:
            upload_file = await cls.upload_file(
                session, cookies,
                to_bytes(image), image_name
            )
            upload = json.dumps([upload_file])
        headers = {
            "Accept": "text/event-stream",
            "Referer": f"{cls.url}/search?fromSearchBar=true&tbm=youchat",
        }
        data = {
            "userFiles": upload,
            "q": format_prompt(messages),
            "domain": "youchat",
            "selectedChatMode": chat_mode,
            "conversationTurnId": str(uuid.uuid4()),
            "chatId": str(uuid.uuid4()),
        }
        if chat_mode == "custom":
            if debug.logging:
                print(f"You model: {model}")
            data["selectedAiModel"] = model.replace("-", "_")

        async with session.get(
            f"{cls.url}/api/streamingSearch",
            params=data,
            headers=headers,
            cookies=cookies
        ) as response:
            await raise_for_status(response)
            async for line in response.iter_lines():
                if line.startswith(b'event: '):
                    event = line[7:].decode()
                elif line.startswith(b'data: '):
                    if event == "error":
                        raise ResponseError(line[6:])
                    if event in ["youChatUpdate", "youChatToken"]:
                        data = json.loads(line[6:])
                    if event == "youChatToken" and event in data and data[event]:
                        if data[event].startswith("#### You\\\'ve hit your free quota for the Model Agent. For more usage of the Model Agent, learn more at:"):\n                            continue
                        yield data[event]
                    elif event == "youChatUpdate" and "t" in data and data["t"]:
                        if chat_mode == "create":
                            match = re.search(r"!\\[(.+?)\\]\\((.+?)\\)", data["t"])
                            if match:
                                if match.group(1) == "fig":
                                    yield ImagePreview(match.group(2), messages[-1]["content"])
                                else:
                                    yield ImageResponse(match.group(2), match.group(1))
                            else:
                                yield data["t"]
                        else:
                            yield data["t"]
### `upload_file`

```python
    @classmethod
    async def upload_file(cls, client: StreamSession, cookies: Cookies, file: bytes, filename: str = None) -> dict:
        """
        Загружает файл на сервер You.com.

        Args:
            client (StreamSession): Асинхронная сессия для выполнения запросов.
            cookies (Cookies): Куки для авторизации.
            file (bytes): Файл для загрузки в виде байтов.
            filename (str, optional): Имя файла. По умолчанию None.

        Returns:
            dict: Словарь с результатами загрузки файла.

        Raises:
            ResponseError: Если сервер возвращает ошибку.

        **Как работает функция**:

        1. **Получение nonce**:
           - Отправляет GET-запрос к API `cls.url/api/get_nonce` для получения nonce (одноразового ключа) для загрузки файла.

        2. **Формирование данных для загрузки**:
           - Создает объект `FormData` для мультипарт-загрузки файла.
           - Определяет тип содержимого файла с помощью `is_accepted_format`.
           - Устанавливает имя файла, если оно не было передано.
           - Добавляет поле `file` в `FormData` с содержимым файла, типом содержимого и именем файла.

        3. **Отправка файла**:
           - Отправляет POST-запрос к API `cls.url/api/upload` с данными `FormData` и заголовком `X-Upload-Nonce`.

        4. **Обработка результата**:
           - Загружает JSON-ответ от сервера.
           - Добавляет поля `user_filename` и `size` в результат.

        ```
        Получение nonce
        ↓
        Формирование данных для загрузки
        ↓
        Отправка файла
        ↓
        Обработка результата
        ```
        """
        async with client.get(
            f"{cls.url}/api/get_nonce",
            cookies=cookies,
        ) as response:
            await raise_for_status(response)
            upload_nonce = await response.text()
        data = FormData()
        content_type = is_accepted_format(file)
        filename = f"image.{MEDIA_TYPE_MAP[content_type]}" if filename is None else filename
        data.add_field('file', file, content_type=content_type, filename=filename)
        async with client.post(
            f"{cls.url}/api/upload",
            data=data,
            headers={
                "X-Upload-Nonce": upload_nonce,
            },
            cookies=cookies
        ) as response:
            await raise_for_status(response)
            result = await response.json()
        result["user_filename"] = filename
        result["size"] = len(file)
        return result