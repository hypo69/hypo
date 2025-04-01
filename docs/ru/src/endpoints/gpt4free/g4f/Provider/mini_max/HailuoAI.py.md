# Модуль HailuoAI
## Обзор

Модуль `HailuoAI` предоставляет асинхронный интерфейс для взаимодействия с AI-сервисом Hailuo AI. Он включает в себя функциональность аутентификации, создания бесед и обмена сообщениями, поддерживает потоковую передачу данных и интеграцию с другими компонентами проекта `hypotez`.

## Подробней

Модуль предназначен для упрощения интеграции с сервисом Hailuo AI, предоставляя удобные методы для аутентификации, создания и управления беседами. Он использует асинхронные запросы для обеспечения высокой производительности и поддерживает потоковую передачу данных для эффективной обработки больших объемов информации.

## Классы

### `Conversation`

**Описание**: Класс представляет собой структуру данных для хранения информации о беседе с Hailuo AI.

**Аттрибуты**:

- `token` (str): Токен аутентификации для доступа к API Hailuo AI.
- `chatID` (str): Идентификатор чата.
- `characterID` (str, optional): Идентификатор персонажа. По умолчанию равен 1.

### `HailuoAI`

**Описание**: Класс `HailuoAI` предоставляет интерфейс для взаимодействия с AI-сервисом Hailuo AI. Он включает методы для аутентификации, создания бесед и обмена сообщениями.

**Наследует**:

- `AsyncAuthedProvider`: Обеспечивает асинхронную аутентификацию.
- `ProviderModelMixin`: Предоставляет функциональность для работы с моделями.

**Аттрибуты**:

- `label` (str): Метка провайдера ("Hailuo AI").
- `url` (str): URL сервиса Hailuo AI ("https://www.hailuo.ai").
- `working` (bool): Флаг, указывающий на работоспособность провайдера (True).
- `use_nodriver` (bool): Флаг, указывающий на использование без драйвера (True).
- `supports_stream` (bool): Флаг, указывающий на поддержку потоковой передачи данных (True).
- `default_model` (str): Модель по умолчанию ("MiniMax").

**Методы**:

- `on_auth_async`: Метод для асинхронной аутентификации.
- `create_authed`: Метод для создания аутентифицированного запроса.

## Функции

### `on_auth_async`

```python
@classmethod
async def on_auth_async(cls, proxy: str = None, **kwargs) -> AsyncIterator:
    """
    Асинхронно аутентифицирует пользователя, используя либо предоставленный `login_url` из переменных окружения,
    либо выполняя автоматическую аутентификацию через браузер.

    Args:
        proxy (str, optional): Прокси-сервер для использования при подключении. По умолчанию `None`.
        **kwargs: Дополнительные аргументы.

    Returns:
        AsyncIterator: Асинхронный итератор, возвращающий результаты аутентификации.

    Yields:
        RequestLogin: Если `login_url` найден, возвращает запрос на вход через URL.
        AuthResult: Результат аутентификации, содержащий все необходимые данные для дальнейшей работы.

    Как работает функция:
    1. **Проверяет наличие `login_url`:** Пытается получить URL для входа из переменной окружения `G4F_LOGIN_URL`.
    2. **Если `login_url` найден:** Генерирует объект `RequestLogin` с `login_url` и передает его.
    3. **Инициализирует `CallbackResults`:** Создает экземпляр класса `CallbackResults` для сбора результатов обратного вызова из браузера.
    4. **Выполняет автоматическую аутентификацию:** Использует `get_args_from_nodriver` для автоматической аутентификации через браузер, передавая URL сервиса и обратный вызов.
    5. **Возвращает `AuthResult`:** Генерирует объект `AuthResult` с результатами аутентификации, включая данные, полученные из браузера и собранные `CallbackResults`.

    Блок-схема:

    Проверка login_url -> Если да -> RequestLogin
        |
        Нет
        |
    Инициализация CallbackResults -> get_args_from_nodriver -> AuthResult

    Примеры:
        Пример 1: Использование без `login_url` (автоматическая аутентификация через браузер).
        >>> async for result in HailuoAI.on_auth_async():
        ...     print(result)

        Пример 2: Использование с `login_url` (запрос на вход через URL).
        >>> import os
        >>> os.environ["G4F_LOGIN_URL"] = "https://example.com/login"
        >>> async for result in HailuoAI.on_auth_async():
        ...     print(result)
    """
    login_url = os.environ.get("G4F_LOGIN_URL")
    if login_url:
        yield RequestLogin(cls.label, login_url)
    callback_results = CallbackResults()
    yield AuthResult(
        **await get_args_from_nodriver(
            cls.url,
            proxy=proxy,
            callback=await get_browser_callback(callback_results)
        ),
        **callback_results.get_dict()
    )
```

### `create_authed`

```python
@classmethod
async def create_authed(
    cls,
    model: str,
    messages: Messages,
    auth_result: AuthResult,
    return_conversation: bool = False,
    conversation: Conversation = None,
    **kwargs
) -> AsyncResult:
    """
    Создает аутентифицированный запрос к Hailuo AI для получения ответа на основе предоставленных сообщений.

    Args:
        model (str): Модель для использования.
        messages (Messages): Список сообщений для отправки.
        auth_result (AuthResult): Результат аутентификации, содержащий необходимые данные для запроса.
        return_conversation (bool, optional): Флаг, указывающий, нужно ли возвращать объект Conversation. По умолчанию `False`.
        conversation (Conversation, optional): Объект Conversation для продолжения существующей беседы. По умолчанию `None`.
        **kwargs: Дополнительные аргументы.

    Returns:
        AsyncResult: Асинхронный генератор, возвращающий ответ от Hailuo AI.

    Yields:
        TitleGeneration: Если в ответе есть заголовок чата, возвращает объект TitleGeneration.
        Conversation: Если `return_conversation` равен `True` и в ответе есть идентификатор чата, возвращает объект Conversation.
        str: Части контента сообщения.

    Как работает функция:
    1. **Извлекает данные из `auth_result`:** Копирует данные аутентификации из `auth_result` и удаляет ненужные поля.
    2. **Создает сессию `ClientSession`:** Использует `ClientSession` для выполнения асинхронных HTTP-запросов.
    3. **Проверяет и обновляет `conversation`:** Если предоставлен объект `conversation`, проверяет его токен и, при необходимости, создает новый объект `conversation`.
    4. **Формирует данные формы `form_data`:** Создает словарь `form_data` с данными для отправки, включая идентификатор персонажа, контент сообщения и идентификатор чата.
    5. **Преобразует данные в `FormData`:** Преобразует словарь `form_data` в объект `FormData` для отправки в теле запроса.
    6. **Генерирует заголовки `headers`:** Создает словарь `headers` с токеном и подписью `yy`.
    7. **Отправляет POST-запрос:** Отправляет асинхронный POST-запрос к сервису Hailuo AI с данными формы и заголовками.
    8. **Обрабатывает ответ:** Читает ответ построчно, обрабатывает события `close_chunk`, `send_result` и `message_result`, и генерирует соответствующие объекты `TitleGeneration`, `Conversation` и части контента сообщения.

    Блок-схема:

    Извлечение данных из auth_result -> Создание ClientSession
        |
        Проверка conversation -> Формирование form_data -> Преобразование в FormData
        |
        Генерация headers -> Отправка POST-запроса -> Обработка ответа

    Примеры:
        Пример 1: Создание запроса без существующей беседы.
        >>> auth_result = AuthResult(token="test_token", path_and_query="/api/chat", timestamp="1234567890", impersonate=True)
        >>> messages = [{"role": "user", "content": "Hello"}]
        >>> async for result in HailuoAI.create_authed(model="MiniMax", messages=messages, auth_result=auth_result):
        ...     print(result)

        Пример 2: Создание запроса с существующей беседой.
        >>> auth_result = AuthResult(token="test_token", path_and_query="/api/chat", timestamp="1234567890", impersonate=True)
        >>> messages = [{"role": "user", "content": "Hello"}]
        >>> conversation = Conversation(token="test_token", chatID="123")
        >>> async for result in HailuoAI.create_authed(model="MiniMax", messages=messages, auth_result=auth_result, conversation=conversation):
        ...     print(result)
    """
    args = auth_result.get_dict().copy()
    args.pop("impersonate")
    token = args.pop("token")
    path_and_query = args.pop("path_and_query")
    timestamp = args.pop("timestamp")

    async with ClientSession(**args) as session:
        if conversation is not None and conversation.token != token:
            conversation = None
        form_data = {
            "characterID": 1 if conversation is None else getattr(conversation, "characterID", 1),
            "msgContent": format_prompt(messages) if conversation is None else get_last_user_message(messages),
            "chatID": 0 if conversation is None else getattr(conversation, "chatID", 0),
            "searchMode": 0
        }
        data = FormData(default_to_multipart=True)
        for name, value in form_data.items():
            form_data[name] = str(value)
            data.add_field(name, str(value))
        headers = {
            "token": token,
            "yy": generate_yy_header(auth_result.path_and_query, get_body_to_yy(form_data), timestamp)
        }
        async with session.post(f"{cls.url}{path_and_query}", data=data, headers=headers) as response:
            await raise_for_status(response)
            event = None
            yield_content_len = 0
            async for line in response.content:
                if not line:
                    continue
                if line.startswith(b"event:") :
                    event = line[6:].decode(errors="replace").strip()
                    if event == "close_chunk":
                        break
                if line.startswith(b"data:"):
                    try:
                        data = json.loads(line[5:])
                    except json.JSONDecodeError as e:
                        debug.log(f"Failed to decode JSON: {line}, error: {e}")
                        continue
                    if event == "send_result":
                        send_result = data["data"]["sendResult"]
                        if "chatTitle" in send_result:
                            yield TitleGeneration(send_result["chatTitle"])
                        if "chatID" in send_result and return_conversation:
                            yield Conversation(token, send_result["chatID"])
                    elif event == "message_result":
                        message_result = data["data"]["messageResult"]
                        if "content" in message_result:
                            yield message_result["content"][yield_content_len:]
                            yield_content_len = len(message_result["content"])