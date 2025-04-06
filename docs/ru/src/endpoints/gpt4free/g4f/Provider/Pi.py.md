# Модуль для работы с Pi.ai
===========================

Модуль предоставляет класс `Pi` для взаимодействия с AI-моделью Pi.ai. Он поддерживает асинхронный стриминг ответов и использует `StreamSession` для выполнения HTTP-запросов.

## Обзор

Этот модуль позволяет взаимодействовать с Pi.ai для получения ответов на основе предоставленных сообщений. Он поддерживает стриминг ответов в асинхронном режиме и использует `StreamSession` для управления HTTP-соединениями. Модуль также включает функции для начала разговора и получения истории чата.

## Классы

### `Pi`

**Описание**: Класс `Pi` является асинхронным генераторным провайдером для взаимодействия с AI-моделью Pi.ai.

**Наследует**: `AsyncGeneratorProvider`

**Атрибуты**:
- `url` (str): URL для взаимодействия с Pi.ai ("https://pi.ai/talk").
- `working` (bool): Указывает, работает ли провайдер (всегда `True`).
- `use_nodriver` (bool): Указывает, используется ли бездрайверный режим (всегда `True`).
- `supports_stream` (bool): Указывает, поддерживает ли провайдер стриминг (всегда `True`).
- `default_model` (str): Модель, используемая по умолчанию ("pi").
- `models` (List[str]): Список поддерживаемых моделей (только `default_model`).
- `_headers` (dict): Заголовки HTTP-запроса.
- `_cookies` (Cookies): Куки HTTP-запроса.

**Методы**:
- `create_async_generator()`: Создает асинхронный генератор для получения ответов от Pi.ai.
- `start_conversation()`: Начинает новый разговор с Pi.ai и возвращает идентификатор разговора.
- `get_chat_history()`: Получает историю чата по идентификатору разговора.
- `ask()`: Отправляет запрос в Pi.ai и возвращает асинхронный генератор для обработки стриминговых ответов.

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
        """Создает асинхронный генератор для получения ответов от Pi.ai.

        Args:
            model (str): Модель для использования (всегда "pi").
            messages (Messages): Список сообщений для отправки.
            stream (bool): Указывает, использовать ли стриминг (всегда `True`).
            proxy (str, optional): Прокси-сервер для использования. По умолчанию `None`.
            timeout (int, optional): Время ожидания запроса. По умолчанию 180.
            conversation_id (str, optional): Идентификатор существующего разговора. По умолчанию `None`.
            **kwargs: Дополнительные аргументы.

        Returns:
            AsyncResult: Асинхронный генератор, выдающий ответы от Pi.ai.

        Как работает функция:
        1. Проверяет, инициализированы ли заголовки HTTP-запроса (`cls._headers`). Если нет, получает их с использованием `get_args_from_nodriver`.
        2. Создает `StreamSession` с заголовками и куками.
        3. Если `conversation_id` не предоставлен, начинает новый разговор с помощью `start_conversation`.
        4. Форматирует сообщения с использованием `format_prompt`.
        5. Отправляет запрос с использованием `ask` и возвращает асинхронный генератор для обработки ответов.

        ASCII Flowchart:
        A: Проверка cls._headers
        |
        B: Получение args (headers, cookies)
        |
        C: Создание StreamSession
        |
        D: Проверка conversation_id
        |
        E1: start_conversation()
        E2: prompt = messages[-1]["content"]
        |
        F: answer = cls.ask()
        |
        G: yield line["text"]

        Примеры:
            >>> messages = [{"role": "user", "content": "Hello"}]
            >>> async def run():
            ...     async for message in Pi.create_async_generator(model="pi", messages=messages, stream=True):
            ...         print(message)
        """
```

### `start_conversation`

```python
    @classmethod
    async def start_conversation(cls, session: StreamSession) -> str:
        """Начинает новый разговор с Pi.ai и возвращает идентификатор разговора.

        Args:
            session (StreamSession): Асинхронная сессия для выполнения HTTP-запросов.

        Returns:
            str: Идентификатор нового разговора.

        Raises:
            Exception: Если возникает ошибка при выполнении запроса.

        Как работает функция:
        1. Выполняет POST-запрос к `https://pi.ai/api/chat/start` с пустыми данными JSON.
        2. Устанавливает заголовки `accept` и `x-api-version`.
        3. Извлекает идентификатор разговора (`sid`) из JSON-ответа.

        ASCII Flowchart:
        A: POST запрос к 'https://pi.ai/api/chat/start'
        |
        B: Извлечение sid из JSON-ответа
        |
        C: Возврат sid

        Примеры:
            >>> import asyncio
            >>> from aiohttp import ClientSession
            >>> async def run():
            ...     async with ClientSession() as client:
            ...         session = StreamSession(client=client)
            ...         conversation_id = await Pi.start_conversation(session)
            ...         print(conversation_id)
        """
```

### `get_chat_history`

```python
    async def get_chat_history(session: StreamSession, conversation_id: str):
        """Получает историю чата по идентификатору разговора.

        Args:
            session (StreamSession): Асинхронная сессия для выполнения HTTP-запросов.
            conversation_id (str): Идентификатор разговора.

        Returns:
            dict: JSON-ответ с историей чата.

        Raises:
            Exception: Если возникает ошибка при выполнении запроса.

        Как работает функция:
        1. Формирует параметры запроса с `conversation_id`.
        2. Выполняет GET-запрос к `https://pi.ai/api/chat/history` с параметрами.
        3. Возвращает JSON-ответ с историей чата.

        ASCII Flowchart:
        A: Формирование параметров запроса
        |
        B: GET запрос к 'https://pi.ai/api/chat/history'
        |
        C: Возврат JSON-ответа

        Примеры:
            >>> import asyncio
            >>> from aiohttp import ClientSession
            >>> async def run():
            ...     async with ClientSession() as client:
            ...         session = StreamSession(client=client)
            ...         conversation_id = "some_conversation_id"
            ...         history = await Pi.get_chat_history(session, conversation_id)
            ...         print(history)
        """
```

### `ask`

```python
    @classmethod
    async def ask(cls, session: StreamSession, prompt: str, conversation_id: str):
        """Отправляет запрос в Pi.ai и возвращает асинхронный генератор для обработки стриминговых ответов.

        Args:
            session (StreamSession): Асинхронная сессия для выполнения HTTP-запросов.
            prompt (str): Текст запроса.
            conversation_id (str): Идентификатор разговора.

        Yields:
            str: Части ответа от Pi.ai.

        Raises:
            Exception: Если возникает ошибка при выполнении запроса.

        Как работает функция:
        1. Формирует JSON-данные запроса с `prompt`, `conversation_id` и `mode`.
        2. Выполняет POST-запрос к `https://pi.ai/api/chat` с JSON-данными.
        3. Обновляет куки (`cls._cookies`) из ответа.
        4. Итерируется по строкам ответа и извлекает JSON-объекты, содержащие текст или заголовок.
        5. Возвращает текст или заголовок через `yield`.

        ASCII Flowchart:
        A: Формирование JSON-данных запроса
        |
        B: POST запрос к 'https://pi.ai/api/chat'
        |
        C: Обновление куки
        |
        D: Итерация по строкам ответа
        |
        E1: Извлечение текста
        E2: Извлечение заголовка
        |
        F: yield текст/заголовок

        Примеры:
            >>> import asyncio
            >>> from aiohttp import ClientSession
            >>> async def run():
            ...     async with ClientSession() as client:
            ...         session = StreamSession(client=client)
            ...         conversation_id = "some_conversation_id"
            ...         async for line in Pi.ask(session, "Hello", conversation_id):
            ...             print(line)
        """