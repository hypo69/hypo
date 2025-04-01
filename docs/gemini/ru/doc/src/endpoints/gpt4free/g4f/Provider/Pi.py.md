# Модуль `Pi`

## Обзор

Модуль `Pi` предоставляет асинхронный генератор для взаимодействия с сервисом Pi.ai. Он позволяет вести беседы, отправлять запросы и получать ответы в асинхронном режиме. Модуль использует `StreamSession` для асинхронных HTTP-запросов и поддерживает потоковую передачу данных.

## Подробнее

Этот модуль является частью проекта `hypotez` и предназначен для интеграции с сервисом Pi.ai, предоставляя удобный интерфейс для асинхронного обмена сообщениями. Он использует асинхронные генераторы для обработки потоковых данных, что позволяет эффективно работать с большими объемами информации.
Модуль определяет методы для начала разговора, отправки сообщений и получения истории чата, обеспечивая полный цикл взаимодействия с API Pi.ai.

## Классы

### `Pi`

**Описание**: Класс `Pi` является асинхронным генератором провайдером для взаимодействия с API Pi.ai.

**Принцип работы**:
1.  **Инициализация**: При первом обращении к классу, если `_headers` не установлены, происходит получение аргументов (включая cookies и headers) с использованием `get_args_from_nodriver`.
2.  **Начало разговора**: Метод `start_conversation` начинает новый разговор с Pi.ai и возвращает идентификатор разговора.
3.  **Отправка запроса**: Метод `ask` отправляет запрос к Pi.ai и возвращает асинхронный генератор, который выдает ответы по мере их поступления.
4.  **Обработка ответов**: В процессе работы, ответы от Pi.ai обрабатываются и извлекаются из потока данных. Cookies обновляются для поддержания сессии.

**Атрибуты:**

*   `url` (str): URL для взаимодействия с Pi.ai ("https://pi.ai/talk").
*   `working` (bool): Указывает, что провайдер работает (True).
*   `use_nodriver` (bool): Указывает на использование без драйвера (True).
*   `supports_stream` (bool): Указывает на поддержку потоковой передачи (True).
*   `default_model` (str): Модель по умолчанию ("pi").
*   `models` (list): Список поддерживаемых моделей (["pi"]).
*   `_headers` (dict): Заголовки HTTP-запроса (инициализируется как None).
*   `_cookies` (Cookies): Cookies для HTTP-запроса (инициализируется как пустой словарь).

**Методы**:

*   `create_async_generator`: Создает асинхронный генератор для взаимодействия с Pi.ai.
*   `start_conversation`: Начинает новый разговор с Pi.ai.
*   `get_chat_history`: Получает историю чата.
*   `ask`: Отправляет запрос к Pi.ai и возвращает асинхронный генератор ответов.

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
    """Создает асинхронный генератор для взаимодействия с Pi.ai.

    Args:
        model (str): Модель для использования.
        messages (Messages): Список сообщений для отправки.
        stream (bool): Флаг, указывающий, использовать ли потоковую передачу.
        proxy (str, optional): Адрес прокси-сервера. По умолчанию `None`.
        timeout (int, optional): Время ожидания запроса в секундах. По умолчанию 180.
        conversation_id (str, optional): Идентификатор разговора. По умолчанию `None`.
        **kwargs: Дополнительные параметры.

    Returns:
        AsyncResult: Асинхронный генератор, выдающий ответы от Pi.ai.

    Как работает функция:
    1. Проверяет, инициализированы ли заголовки (`cls._headers`). Если нет, то получает их и cookies с помощью `get_args_from_nodriver`.
    2. Создает асинхронную сессию `StreamSession` с полученными заголовками и cookies.
    3. Если `conversation_id` не предоставлен, начинает новый разговор, получая `conversation_id` от Pi.ai.
    4. Форматирует запрос с использованием `format_prompt` или берет последнее сообщение из списка.
    5. Вызывает метод `ask` для отправки запроса и получения ответов.
    6. Итерируется по ответам, извлекая текст из каждого ответа и передавая его через `yield`.

    Внутри функции происходят следующие действия и преобразования:
    A. Проверка инициализации заголовков и получение их при необходимости.
    |
    B. Создание асинхронной сессии.
    |
    C. Получение или использование существующего `conversation_id`.
    |
    D. Форматирование запроса.
    |
    E. Отправка запроса и получение ответов.
    |
    F. Извлечение текста из ответов и передача через `yield`.
    """
    ...
```

**Примеры**:

```python
# Пример использования create_async_generator
model = "pi"
messages = [{"role": "user", "content": "Hello, Pi!"}]
stream = True
# result = Pi.create_async_generator(model=model, messages=messages, stream=stream)
```

### `start_conversation`

```python
@classmethod
async def start_conversation(cls, session: StreamSession) -> str:
    """Начинает новый разговор с Pi.ai.

    Args:
        session (StreamSession): Асинхронная сессия для выполнения запроса.

    Returns:
        str: Идентификатор нового разговора.

    Raises:
        Exception: Если возникает ошибка при выполнении запроса.

    Как работает функция:
    1. Отправляет POST-запрос к `https://pi.ai/api/chat/start` с заголовками, необходимыми для начала разговора.
    2. Проверяет статус ответа с помощью `raise_for_status`.
    3. Извлекает `conversation_id` из JSON-ответа.

    Внутри функции происходят следующие действия и преобразования:
    A. Отправка POST-запроса.
    |
    B. Проверка статуса ответа.
    |
    C. Извлечение `conversation_id`.
    """
    ...
```

**Примеры**:

```python
# Пример использования start_conversation
# async def example():
#     session = StreamSession()
#     conversation_id = await Pi.start_conversation(session)
#     print(f"Conversation ID: {conversation_id}")
# asyncio.run(example())
```

### `get_chat_history`

```python
async def get_chat_history(session: StreamSession, conversation_id: str):
    """Получает историю чата.

    Args:
        session (StreamSession): Асинхронная сессия для выполнения запроса.
        conversation_id (str): Идентификатор разговора.

    Returns:
        dict: JSON-ответ с историей чата.

    Raises:
        Exception: Если возникает ошибка при выполнении запроса.

    Как работает функция:
    1. Определяет параметры запроса, включая `conversation_id`.
    2. Отправляет GET-запрос к `https://pi.ai/api/chat/history` с параметрами.
    3. Проверяет статус ответа с помощью `raise_for_status`.
    4. Возвращает JSON-ответ с историей чата.

    Внутри функции происходят следующие действия и преобразования:
    A. Определение параметров запроса.
    |
    B. Отправка GET-запроса.
    |
    C. Проверка статуса ответа.
    |
    D. Возврат JSON-ответа.
    """
    ...
```

**Примеры**:

```python
# Пример использования get_chat_history
# async def example():
#     session = StreamSession()
#     conversation_id = "some_conversation_id"
#     history = await Pi.get_chat_history(session, conversation_id)
#     print(f"Chat history: {history}")
# asyncio.run(example())
```

### `ask`

```python
@classmethod
async def ask(cls, session: StreamSession, prompt: str, conversation_id: str):
    """Отправляет запрос к Pi.ai и возвращает асинхронный генератор ответов.

    Args:
        session (StreamSession): Асинхронная сессия для выполнения запроса.
        prompt (str): Текст запроса.
        conversation_id (str): Идентификатор разговора.

    Yields:
        dict: Части ответа от Pi.ai.

    Raises:
        Exception: Если возникает ошибка при выполнении запроса.

    Как работает функция:
    1. Формирует JSON-данные для отправки запроса, включая текст запроса, `conversation_id` и режим.
    2. Отправляет POST-запрос к `https://pi.ai/api/chat` с JSON-данными.
    3. Проверяет статус ответа с помощью `raise_for_status`.
    4. Обновляет cookies с помощью `merge_cookies`.
    5. Итерируется по строкам ответа, извлекая JSON-части, начинающиеся с `data: {"text":` или `data: {"title":`.
    6. Возвращает извлеченные JSON-части через `yield`.

    Внутри функции происходят следующие действия и преобразования:
    A. Формирование JSON-данных.
    |
    B. Отправка POST-запроса.
    |
    C. Проверка статуса ответа.
    |
    D. Обновление cookies.
    |
    E. Итерация по строкам ответа.
    |
    F. Извлечение JSON-частей и передача через `yield`.
    """
    ...
```

**Примеры**:

```python
# Пример использования ask
# async def example():
#     session = StreamSession()
#     prompt = "Tell me a story."
#     conversation_id = "some_conversation_id"
#     async for line in Pi.ask(session, prompt, conversation_id):
#         print(f"Response line: {line}")
# asyncio.run(example())