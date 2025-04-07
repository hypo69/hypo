# Модуль `Pi`

## Обзор

Модуль `Pi` предоставляет асинхронный интерфейс для взаимодействия с AI-моделью Pi.ai. Он позволяет начать разговор, отправлять запросы и получать ответы в потоковом режиме. Модуль использует `StreamSession` для асинхронных HTTP-запросов и поддерживает работу через прокси.

## Подробнее

Модуль предназначен для интеграции с другими частями проекта `hypotez`, обеспечивая возможность использования AI-модели Pi.ai для обработки текстовых запросов и генерации ответов. Он включает в себя функции для установления соединения, поддержания контекста разговора и обработки потоковых данных.

## Классы

### `Pi`

**Описание**: Класс `Pi` является асинхронным провайдером, который реализует взаимодействие с AI-моделью Pi.ai.

**Наследует**:

- `AsyncGeneratorProvider`: Обеспечивает базовую функциональность для асинхронных провайдеров, генерирующих данные.

**Атрибуты**:

- `url` (str): URL для взаимодействия с Pi.ai ("https://pi.ai/talk").
- `working` (bool): Указывает, работает ли провайдер (True).
- `use_nodriver` (bool): Указывает, используется ли бездрайверный режим (True).
- `supports_stream` (bool): Указывает, поддерживает ли провайдер потоковую передачу данных (True).
- `default_model` (str): Модель, используемая по умолчанию ("pi").
- `models` (list[str]): Список поддерживаемых моделей (["pi"]).
- `_headers` (dict | None): Заголовки HTTP-запросов (изначально None).
- `_cookies` (Cookies): Куки для HTTP-запросов (изначально пустой словарь).

**Методы**:

- `create_async_generator`: Создает асинхронный генератор для взаимодействия с моделью.
- `start_conversation`: Начинает новый разговор с AI-моделью.
- `get_chat_history`: Получает историю чата по идентификатору разговора.
- `ask`: Отправляет запрос AI-модели и возвращает ответ в потоковом режиме.

## Функции

### `create_async_generator`

```python
@classmethod
async def create_async_generator(
    cls,
    model: str,
    messages: Messages,
    stream: bool,
    proxy: str = None,
    timeout: int = 180,
    conversation_id: str = None,
    **kwargs
) -> AsyncResult:
    """Создает асинхронный генератор для взаимодействия с AI-моделью Pi.ai.

    Args:
        model (str): Название модели.
        messages (Messages): Список сообщений для отправки.
        stream (bool): Флаг, указывающий на использование потокового режима.
        proxy (str, optional): Адрес прокси-сервера. По умолчанию None.
        timeout (int, optional): Время ожидания запроса в секундах. По умолчанию 180.
        conversation_id (str, optional): Идентификатор существующего разговора. По умолчанию None.
        **kwargs: Дополнительные аргументы.

    Returns:
        AsyncResult: Асинхронный генератор, возвращающий ответы от AI-модели.

    Как работает функция:
    1. Проверяет, инициализированы ли заголовки запроса `cls._headers`. Если нет, то запрашивает их и куки из `cls.url`.
    2. Открывает асинхронную сессию с помощью `StreamSession`, используя заголовки и куки.
    3. Если `conversation_id` не передан, начинает новый разговор, используя метод `start_conversation`, и форматирует сообщения для отправки.
    4. Если `conversation_id` передан, использует его и отправляет последнее сообщение из списка `messages`.
    5. Вызывает метод `ask` для отправки запроса в AI-модель и получает ответы в потоковом режиме.

    A -- Проверка инициализации заголовков
    |
    B -- Получение заголовков и куки (если не инициализированы)
    |
    C -- Открытие асинхронной сессии
    |
    D -- Проверка наличия conversation_id
    |
    E -- Запуск нового разговора (если conversation_id отсутствует)
    |
    F -- Форматирование сообщений
    |
    G -- Отправка запроса в AI-модель и получение ответов в потоковом режиме

    Примеры:
    - Создание асинхронного генератора для нового разговора:
        ```python
        messages = [{"role": "user", "content": "Hello, how are you?"}]
        generator = await Pi.create_async_generator(model="pi", messages=messages, stream=True)
        ```
    - Создание асинхронного генератора для продолжения существующего разговора:
        ```python
        messages = [{"role": "user", "content": "What is the weather like today?"}]
        generator = await Pi.create_async_generator(model="pi", messages=messages, stream=True, conversation_id="12345")
        ```
    """
    if cls._headers is None:
        args = await get_args_from_nodriver(cls.url, proxy=proxy, timeout=timeout)
        cls._cookies = args.get("cookies", {})
        cls._headers = args.get("headers")
    async with StreamSession(headers=cls._headers, cookies=cls._cookies, proxy=proxy) as session:
        if not conversation_id:
            conversation_id = await cls.start_conversation(session)
            prompt = format_prompt(messages)
        else:
            prompt = messages[-1]["content"]
        answer = cls.ask(session, prompt, conversation_id)
        async for line in answer:
            if "text" in line:
                yield line["text"]
```

### `start_conversation`

```python
@classmethod
async def start_conversation(cls, session: StreamSession) -> str:
    """Начинает новый разговор с AI-моделью Pi.ai.

    Args:
        session (StreamSession): Асинхронная сессия для выполнения HTTP-запросов.

    Returns:
        str: Идентификатор нового разговора.

    Как работает функция:
    1. Отправляет POST-запрос на URL 'https://pi.ai/api/chat/start' с пустыми данными и заголовками, указывающими на ожидание JSON в ответе.
    2. Проверяет статус ответа и вызывает исключение, если произошла ошибка.
    3. Извлекает идентификатор разговора (`sid`) из JSON-ответа.

    A -- Отправка POST-запроса на URL начала разговора
    |
    B -- Проверка статуса ответа
    |
    C -- Извлечение идентификатора разговора из JSON-ответа

    Примеры:
    - Запуск нового разговора:
        ```python
        session = StreamSession()
        conversation_id = await Pi.start_conversation(session)
        print(f"Conversation ID: {conversation_id}")
        ```
    """
    async with session.post('https://pi.ai/api/chat/start', data="{}", headers={
        'accept': 'application/json',
        'x-api-version': '3'
    }) as response:
        await raise_for_status(response)
        return (await response.json())['conversations'][0]['sid']
```

### `get_chat_history`

```python
async def get_chat_history(session: StreamSession, conversation_id: str):
    """Получает историю чата по идентификатору разговора.

    Args:
        session (StreamSession): Асинхронная сессия для выполнения HTTP-запросов.
        conversation_id (str): Идентификатор разговора.

    Returns:
        json: История разговора в формате JSON.

    Как работает функция:
    1. Подготавливает параметры запроса, включая `conversation_id`.
    2. Отправляет GET-запрос на URL 'https://pi.ai/api/chat/history' с указанными параметрами.
    3. Проверяет статус ответа и вызывает исключение, если произошла ошибка.
    4. Возвращает историю разговора в формате JSON.

    A -- Подготовка параметров запроса
    |
    B -- Отправка GET-запроса на URL истории чата
    |
    C -- Проверка статуса ответа
    |
    D -- Возврат истории разговора в формате JSON

    Примеры:
    - Получение истории чата:
        ```python
        session = StreamSession()
        conversation_id = "12345"
        history = await Pi.get_chat_history(session, conversation_id)
        print(history)
        ```
    """
    params = {
        'conversation': conversation_id,
    }
    async with session.get('https://pi.ai/api/chat/history', params=params) as response:
        await raise_for_status(response)
        return await response.json()
```

### `ask`

```python
@classmethod
async def ask(cls, session: StreamSession, prompt: str, conversation_id: str):
    """Отправляет запрос AI-модели и возвращает ответ в потоковом режиме.

    Args:
        session (StreamSession): Асинхронная сессия для выполнения HTTP-запросов.
        prompt (str): Текст запроса.
        conversation_id (str): Идентификатор разговора.

    Yields:
        str: Части ответа от AI-модели.

    Как работает функция:
    1. Формирует JSON-данные для отправки запроса, включая текст запроса, идентификатор разговора и режим работы.
    2. Отправляет POST-запрос на URL 'https://pi.ai/api/chat' с сформированными JSON-данными.
    3. Проверяет статус ответа и вызывает исключение, если произошла ошибка.
    4. Обновляет куки сессии, объединяя текущие куки с куками из ответа.
    5. Итерируется по строкам в ответе и извлекает текст ответа из строк, начинающихся с 'data: {"text":' или 'data: {"title":'.

    A -- Формирование JSON-данных для запроса
    |
    B -- Отправка POST-запроса на URL чата
    |
    C -- Проверка статуса ответа
    |
    D -- Обновление куки сессии
    |
    E -- Итерация по строкам в ответе
    |
    F -- Извлечение текста ответа из строк, начинающихся с 'data: {"text":' или 'data: {"title":'

    Примеры:
    - Отправка запроса и получение ответа в потоковом режиме:
        ```python
        session = StreamSession()
        conversation_id = "12345"
        prompt = "What is the capital of France?"
        async for line in Pi.ask(session, prompt, conversation_id):
            print(line)
        ```
    """
    json_data = {
        'text': prompt,
        'conversation': conversation_id,
        'mode': 'BASE',
    }
    async with session.post('https://pi.ai/api/chat', json=json_data) as response:
        await raise_for_status(response)
        cls._cookies = merge_cookies(cls._cookies, response)
        async for line in response.iter_lines():
            if line.startswith(b'data: {"text":'):
                yield json.loads(line.split(b'data: ')[1])
            elif line.startswith(b'data: {"title":'):
                yield json.loads(line.split(b'data: ')[1])