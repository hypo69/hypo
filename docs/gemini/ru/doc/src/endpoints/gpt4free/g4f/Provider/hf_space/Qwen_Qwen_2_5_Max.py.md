# Модуль для работы с Qwen Qwen-2.5-Max

## Обзор

Модуль предоставляет асинхронный генератор для взаимодействия с моделью Qwen Qwen-2.5-Max через API. Он включает в себя функциональность для подготовки запросов, отправки их к API и обработки потоковых ответов.

## Подробнее

Этот модуль позволяет взаимодействовать с моделью Qwen Qwen-2.5-Max, предоставляя асинхронный генератор для обработки запросов и получения потоковых ответов. Он поддерживает настройку прокси и форматирование запросов.

## Классы

### `Qwen_Qwen_2_5_Max`

**Описание**: Класс для взаимодействия с моделью Qwen Qwen-2.5-Max.

**Наследует**:
- `AsyncGeneratorProvider`: Предоставляет базовую функциональность для асинхронных генераторов.
- `ProviderModelMixin`: Предоставляет функциональность для работы с моделями.

**Атрибуты**:
- `label` (str): Метка провайдера ("Qwen Qwen-2.5-Max").
- `url` (str): URL для API ("https://qwen-qwen2-5-max-demo.hf.space").
- `api_endpoint` (str): Конечная точка API для отправки запросов ("https://qwen-qwen2-5-max-demo.hf.space/gradio_api/queue/join?").
- `working` (bool): Указывает, работает ли провайдер (True).
- `supports_stream` (bool): Указывает, поддерживает ли провайдер потоковую передачу данных (True).
- `supports_system_message` (bool): Указывает, поддерживает ли провайдер системные сообщения (True).
- `supports_message_history` (bool): Указывает, поддерживает ли провайдер историю сообщений (False).
- `default_model` (str): Модель по умолчанию ("qwen-qwen2-5-max").
- `model_aliases` (dict): Псевдонимы моделей ({"qwen-2-5-max": default_model}).
- `models` (list): Список моделей (ключи из model_aliases).

**Методы**:
- `create_async_generator`: Создает асинхронный генератор для получения ответов от модели.

## Функции

### `create_async_generator`

```python
@classmethod
async def create_async_generator(
    cls,
    model: str,
    messages: Messages,
    proxy: str = None,
    **kwargs
) -> AsyncResult:
    """
    Создает асинхронный генератор для получения ответов от модели Qwen Qwen-2.5-Max.

    Args:
        model (str): Модель для использования.
        messages (Messages): Список сообщений для отправки.
        proxy (str, optional): URL прокси-сервера. По умолчанию `None`.
        **kwargs: Дополнительные аргументы.

    Returns:
        AsyncResult: Асинхронный генератор, возвращающий ответы от модели.
    """
    def generate_session_hash() -> str:
        """
        Генерирует уникальный hash сессии.

        Returns:
            str: Уникальный hash сессии.
        """
        ...

    # Генерация уникального session hash
    session_hash = generate_session_hash()

    headers_join = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:136.0) Gecko/20100101 Firefox/136.0',
        'Accept': '*/*',
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate, br, zstd',
        'Referer': f'{cls.url}/?__theme=system',
        'content-type': 'application/json',
        'Origin': cls.url,
        'Connection': 'keep-alive',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'Pragma': 'no-cache',
        'Cache-Control': 'no-cache',
    }

    # Подготовка prompt
    system_prompt = "\n".join([message["content"] for message in messages if message["role"] == "system"])
    if not system_prompt:
        system_prompt = "You are a helpful assistant."
    messages = [message for message in messages if message["role"] != "system"]
    prompt = format_prompt(messages)

    payload_join = {
        "data": [prompt, [], system_prompt],
        "event_data": None,
        "fn_index": 0,
        "trigger_id": 11,
        "session_hash": session_hash
    }

    async with aiohttp.ClientSession() as session:
        # Отправка join request
        async with session.post(cls.api_endpoint, headers=headers_join, json=payload_join) as response:
            event_id = (await response.json())['event_id']

        # Подготовка data stream request
        url_data = f'{cls.url}/gradio_api/queue/data'

        headers_data = {
            'Accept': 'text/event-stream',
            'Accept-Language': 'en-US,en;q=0.5',
            'Referer': f'{cls.url}/?__theme=system',
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:136.0) Gecko/20100101 Firefox/136.0',
        }

        params_data = {
            'session_hash': session_hash
        }

        # Отправка data stream request
        async with session.get(url_data, headers=headers_data, params=params_data) as response:
            full_response = ""
            final_full_response = ""
            async for line in response.content:
                decoded_line = line.decode('utf-8')
                if decoded_line.startswith('data: '):
                    try:
                        json_data = json.loads(decoded_line[6:])

                        # Поиск generation stages
                        if json_data.get('msg') == 'process_generating':
                            if 'output' in json_data and 'data' in json_data['output']:
                                output_data = json_data['output']['data']
                                if len(output_data) > 1 and len(output_data[1]) > 0:
                                    for item in output_data[1]:
                                        if isinstance(item, list) and len(item) > 1:
                                            fragment = str(item[1])
                                            # Игнорировать [0, 1] type fragments и дубликаты
                                            if not re.match(r'^\\[.*\\]$', fragment) and not full_response.endswith(fragment):
                                                full_response += fragment
                                                yield fragment

                        # Проверка completion
                        if json_data.get('msg') == 'process_completed':
                            # Финальная проверка для получения полного ответа
                            if 'output' in json_data and 'data' in json_data['output']:
                                output_data = json_data['output']['data']
                                if len(output_data) > 1 and len(output_data[1]) > 0:
                                    final_full_response = output_data[1][0][1]
                                    
                                    # Очистка final response
                                    if final_full_response.startswith(full_response):
                                        final_full_response = final_full_response[len(full_response):]
                                    
                                    # Возврат оставшейся части final response
                                    if final_full_response:
                                        yield final_full_response
                            break

                    except json.JSONDecodeError as ex:
                        debug.log("Could not parse JSON:", decoded_line)

    """Генерирует асинхронный генератор для получения ответов от модели.

    Args:
        model (str): Модель для использования.
        messages (Messages): Список сообщений для отправки.
        proxy (str, optional): URL прокси-сервера. По умолчанию `None`.
        **kwargs: Дополнительные аргументы.

    Returns:
        AsyncResult: Асинхронный генератор, возвращающий ответы от модели.
    """

    def generate_session_hash() -> str:
        """Генерирует уникальный hash сессии.

        Returns:
            str: Уникальный hash сессии.
        """
        return str(uuid.uuid4()).replace('-', '')[:8] + str(uuid.uuid4()).replace('-', '')[:4]

    # 1. Генерация уникального session hash
    session_hash = generate_session_hash()

    headers_join = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:136.0) Gecko/20100101 Firefox/136.0',
        'Accept': '*/*',
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate, br, zstd',
        'Referer': f'{cls.url}/?__theme=system',
        'content-type': 'application/json',
        'Origin': cls.url,
        'Connection': 'keep-alive',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'Pragma': 'no-cache',
        'Cache-Control': 'no-cache',
    }

    # 2. Подготовка prompt
    system_prompt = "\n".join([message["content"] for message in messages if message["role"] == "system"])
    if not system_prompt:
        system_prompt = "You are a helpful assistant."
    messages = [message for message in messages if message["role"] != "system"]
    prompt = format_prompt(messages)

    payload_join = {
        "data": [prompt, [], system_prompt],
        "event_data": None,
        "fn_index": 0,
        "trigger_id": 11,
        "session_hash": session_hash
    }

    async with aiohttp.ClientSession() as session:
        # 3. Отправка join request
        async with session.post(cls.api_endpoint, headers=headers_join, json=payload_join) as response:
            event_id = (await response.json())['event_id']

        # 4. Подготовка data stream request
        url_data = f'{cls.url}/gradio_api/queue/data'

        headers_data = {
            'Accept': 'text/event-stream',
            'Accept-Language': 'en-US,en;q=0.5',
            'Referer': f'{cls.url}/?__theme=system',
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:136.0) Gecko/20100101 Firefox/136.0',
        }

        params_data = {
            'session_hash': session_hash
        }

        # 5. Отправка data stream request
        async with session.get(url_data, headers=headers_data, params=params_data) as response:
            full_response = ""
            final_full_response = ""
            async for line in response.content:
                decoded_line = line.decode('utf-8')
                if decoded_line.startswith('data: '):
                    try:
                        json_data = json.loads(decoded_line[6:])

                        # 6. Поиск generation stages
                        if json_data.get('msg') == 'process_generating':
                            if 'output' in json_data and 'data' in json_data['output']:
                                output_data = json_data['output']['data']
                                if len(output_data) > 1 and len(output_data[1]) > 0:
                                    for item in output_data[1]:
                                        if isinstance(item, list) and len(item) > 1:
                                            fragment = str(item[1])
                                            # Игнорировать [0, 1] type fragments и дубликаты
                                            if not re.match(r'^\\[.*\\]$', fragment) and not full_response.endswith(fragment):
                                                full_response += fragment
                                                yield fragment

                        # 7. Проверка completion
                        if json_data.get('msg') == 'process_completed':
                            # Финальная проверка для получения полного ответа
                            if 'output' in json_data and 'data' in json_data['output']:
                                output_data = json_data['output']['data']
                                if len(output_data) > 1 and len(output_data[1]) > 0:
                                    final_full_response = output_data[1][0][1]
                                    
                                    # Очистка final response
                                    if final_full_response.startswith(full_response):
                                        final_full_response = final_full_response[len(full_response):]
                                    
                                    # Возврат оставшейся части final response
                                    if final_full_response:
                                        yield final_full_response
                            break

                    except json.JSONDecodeError as ex:
                        debug.log("Could not parse JSON:", decoded_line)
    """
    Функция `create_async_generator` создает асинхронный генератор для взаимодействия с моделью Qwen Qwen-2.5-Max.
    Она выполняет несколько шагов, чтобы отправить запрос к API и получить потоковые ответы.

    Args:
        cls (type): Класс, для которого вызывается метод.
        model (str): Модель для использования.
        messages (Messages): Список сообщений для отправки.
        proxy (str, optional): URL прокси-сервера. По умолчанию `None`.
        **kwargs: Дополнительные аргументы.

    Returns:
        AsyncResult: Асинхронный генератор, возвращающий ответы от модели.

    Raises:
        JSONDecodeError: Если не удается распарсить JSON из ответа API.
    """

    def generate_session_hash() -> str:
        """
        Внутренняя функция `generate_session_hash` генерирует уникальный hash сессии.

        Returns:
            str: Уникальный hash сессии.
        """
        return str(uuid.uuid4()).replace('-', '')[:8] + str(uuid.uuid4()).replace('-', '')[:4]

    # 1. Генерация уникального session hash
    session_hash = generate_session_hash()

    headers_join = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:136.0) Gecko/20100101 Firefox/136.0',
        'Accept': '*/*',
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate, br, zstd',
        'Referer': f'{cls.url}/?__theme=system',
        'content-type': 'application/json',
        'Origin': cls.url,
        'Connection': 'keep-alive',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'Pragma': 'no-cache',
        'Cache-Control': 'no-cache',
    }

    # 2. Подготовка prompt
    system_prompt = "\n".join([message["content"] for message in messages if message["role"] == "system"])
    if not system_prompt:
        system_prompt = "You are a helpful assistant."
    messages = [message for message in messages if message["role"] != "system"]
    prompt = format_prompt(messages)

    payload_join = {
        "data": [prompt, [], system_prompt],
        "event_data": None,
        "fn_index": 0,
        "trigger_id": 11,
        "session_hash": session_hash
    }

    async with aiohttp.ClientSession() as session:
        # 3. Отправка join request
        async with session.post(cls.api_endpoint, headers=headers_join, json=payload_join) as response:
            event_id = (await response.json())['event_id']

        # 4. Подготовка data stream request
        url_data = f'{cls.url}/gradio_api/queue/data'

        headers_data = {
            'Accept': 'text/event-stream',
            'Accept-Language': 'en-US,en;q=0.5',
            'Referer': f'{cls.url}/?__theme=system',
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:136.0) Gecko/20100101 Firefox/136.0',
        }

        params_data = {
            'session_hash': session_hash
        }

        # 5. Отправка data stream request
        async with session.get(url_data, headers=headers_data, params=params_data) as response:
            full_response = ""
            final_full_response = ""
            async for line in response.content:
                decoded_line = line.decode('utf-8')
                if decoded_line.startswith('data: '):
                    try:
                        json_data = json.loads(decoded_line[6:])

                        # 6. Поиск generation stages
                        if json_data.get('msg') == 'process_generating':
                            if 'output' in json_data and 'data' in json_data['output']:
                                output_data = json_data['output']['data']
                                if len(output_data) > 1 and len(output_data[1]) > 0:
                                    for item in output_data[1]:
                                        if isinstance(item, list) and len(item) > 1:
                                            fragment = str(item[1])
                                            # Игнорировать [0, 1] type fragments и дубликаты
                                            if not re.match(r'^\\[.*\\]$', fragment) and not full_response.endswith(fragment):
                                                full_response += fragment
                                                yield fragment

                        # 7. Проверка completion
                        if json_data.get('msg') == 'process_completed':
                            # Финальная проверка для получения полного ответа
                            if 'output' in json_data and 'data' in json_data['output']:
                                output_data = json_data['output']['data']
                                if len(output_data) > 1 and len(output_data[1]) > 0:
                                    final_full_response = output_data[1][0][1]
                                    
                                    # Очистка final response
                                    if final_full_response.startswith(full_response):
                                        final_full_response = final_full_response[len(full_response):]
                                    
                                    # Возврат оставшейся части final response
                                    if final_full_response:
                                        yield final_full_response
                            break

                    except json.JSONDecodeError as ex:
                        debug.log("Could not parse JSON:", decoded_line)

    """
    Функция `create_async_generator` создает асинхронный генератор для взаимодействия с моделью Qwen Qwen-2.5-Max.
    Она выполняет несколько шагов, чтобы отправить запрос к API и получить потоковые ответы.

    **Как работает функция**:

    1.  **Генерация уникального идентификатора сессии**:
        -   Вызывается внутренняя функция `generate_session_hash` для создания уникального идентификатора сессии (session_hash), который используется для дальнейшего взаимодействия с API.

    2.  **Подготовка заголовков для запроса на присоединение**:
        -   Определяются заголовки (`headers_join`), которые будут отправлены с запросом на присоединение к очереди API. Эти заголовки включают информацию о User-Agent, типах принимаемого контента, языке и другие метаданные.

    3.  **Подготовка данных запроса (payload) на присоединение**:
        -   Формируется полезная нагрузка (`payload_join`) для запроса на присоединение к API. Она включает в себя:
            -   `prompt`: Отформатированный запрос, содержащий сообщения от пользователя и системные инструкции.
            -   `system_prompt`: Системные инструкции, если они есть. Если системные инструкции отсутствуют, устанавливается значение по умолчанию "You are a helpful assistant.".
            -   `session_hash`: Уникальный идентификатор сессии, сгенерированный ранее.

    4.  **Отправка запроса на присоединение и получение идентификатора события**:
        -   Используется асинхронная сессия `aiohttp.ClientSession` для отправки POST-запроса к API (`cls.api_endpoint`) с заголовками `headers_join` и полезной нагрузкой `payload_join`.
        -   Полученный ответ преобразуется в JSON, и из него извлекается идентификатор события (`event_id`), который будет использоваться для дальнейших запросов.

    5.  **Подготовка заголовков и параметров для запроса потока данных**:
        -   Определяются URL (`url_data`), заголовки (`headers_data`) и параметры (`params_data`) для запроса потока данных.
        -   Заголовки включают информацию о типе принимаемого контента (text/event-stream), языке и User-Agent.
        -   Параметры включают идентификатор сессии (`session_hash`).

    6.  **Отправка запроса потока данных и обработка ответов**:
        -   Отправляется GET-запрос к API (`url_data`) с заголовками `headers_data` и параметрами `params_data`.
        -   Полученный ответ обрабатывается построчно в асинхронном режиме. Каждая строка декодируется из UTF-8.
        -   Если строка начинается с "data: ", она считается содержащей JSON-данные.

    7.  **Обработка JSON-данных**:
        -   JSON-данные извлекаются из строки и десериализуются.
        -   Если сообщение (`msg`) равно "process_generating", извлекаются данные о генерации (`output_data`).
        -   Извлекаются фрагменты текста из `output_data` и возвращаются как часть асинхронного генератора.

    8.  **Проверка завершения процесса**:
        -   Если сообщение (`msg`) равно "process_completed", извлекаются финальные данные (`output_data`).
        -   Извлекается полный текст ответа, очищается от предыдущих фрагментов и возвращается как финальная часть асинхронного генератора.

    9.  **Обработка ошибок**:
        -   Если происходит ошибка при десериализации JSON, она логируется с использованием `debug.log`.

    **Внутренние функции**:
        -   `generate_session_hash()`:
            -   **Назначение**: Генерация уникального идентификатора сессии.
            -   **Как работает функция**:
                -   Генерирует UUID, удаляет дефисы и берет первые 8 и 4 символа.
                -   Конкатенирует полученные строки и возвращает результат.

    **ASCII схема работы функции**:

    ```
    generate_session_hash
    ↓
    HeadersJoinPreparation
    ↓
    PromptPreparation
    ↓
    SendJoinRequest -→ GetEventId
    ↓
    HeadersDataPreparation
    ↓
    SendDataStreamRequest
    ↓
    ProcessGenerating? -→ ExtractFragment -→ ReturnFragment
    ↓
    ProcessCompleted?  -→ ExtractFullResponse -→ ReturnFullResponse
    ↓
    End
    ```

    **Примеры**:

    ```python
    # Пример 1: Создание асинхронного генератора с минимальными параметрами
    model = "qwen-2-5-max"
    messages = [{"role": "user", "content": "Hello, how are you?"}]
    generator = await Qwen_Qwen_2_5_Max.create_async_generator(model=model, messages=messages)

    # Пример 2: Создание асинхронного генератора с указанием прокси
    model = "qwen-2-5-max"
    messages = [{"role": "user", "content": "Translate 'hello' to French."}]
    proxy = "http://your_proxy:8080"
    generator = await Qwen_Qwen_2_5_Max.create_async_generator(model=model, messages=messages, proxy=proxy)

    # Пример 3: Использование асинхронного генератора для получения ответа
    model = "qwen-2-5-max"
    messages = [{"role": "user", "content": "Tell me a joke."}]
    generator = await Qwen_Qwen_2_5_Max.create_async_generator(model=model, messages=messages)
    async for fragment in generator:
        print(fragment, end="")
    ```