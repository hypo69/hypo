# Модуль Bing

## Обзор

Модуль предоставляет класс и функции для взаимодействия с Bing Chat API. Он включает в себя создание бесед, генерацию ответов с использованием стриминга и форматирование сообщений. Модуль предназначен для использования в качестве поставщика (Provider) для G4F (Generic Function Framework) и поддерживает модель GPT-4.

## Подробней

Этот модуль предназначен для обеспечения взаимодействия с Bing Chat API, позволяя генерировать ответы на основе предоставленных подсказок (prompt). Он использует асинхронные запросы для стриминговой передачи данных, что позволяет получать ответы в реальном времени.

Модуль определяет несколько вспомогательных классов и функций:

*   `optionsSets`: Определяет структуру наборов опций, используемых для настройки поведения Bing Chat.
*   `Defaults`: Содержит значения по умолчанию, такие как разделитель сообщений, IP-адрес и список разрешенных типов сообщений.
*   `_format`: Форматирует сообщения в формат JSON с добавлением разделителя.
*   `create_conversation`: Создает новый разговор с Bing Chat API и возвращает идентификаторы разговора, клиента и подпись.
*   `stream_generate`: Генерирует ответы с использованием стриминга на основе предоставленной подсказки и контекста.
*   `run`: Запускает асинхронный генератор и возвращает значения.
*   `convert`: Преобразует список сообщений в контекст для Bing Chat API.
*   `_create_completion`: Создает запрос на завершение текста и возвращает ответ от Bing Chat API.

Модуль использует следующие библиотеки:

*   `os`: Для получения доступа к переменнам окружения, например `os.urandom(16).hex()`
*   `json`: Для работы с форматом JSON, например `json.dumps(msg, ensure_ascii=False)`
*   `random`: Для генерации случайных чисел, например `random.randint(104, 107)`
*   `ssl`: Для обеспечения безопасного соединения, например `ssl.create_default_context()`
*   `certifi`: Для проверки SSL сертификатов, например `certifi.where()`
*   `aiohttp`: Для асинхронных HTTP запросов, например `aiohttp.ClientSession(timeout=timeout)`
*   `asyncio`: Для асинхронного программирования, например `asyncio.get_event_loop()`
*   `requests`: Для выполнения HTTP запросов, например `requests.get('https://www.bing.com/turing/conversation/create'`
*   `uuid`: Для генерации уникальных идентификаторов, например `str(uuid.uuid4())`

## Классы

### `optionsSets`

**Описание**: Класс, определяющий структуру наборов опций для Bing Chat.

**Принцип работы**:
Класс `optionsSets` содержит два вложенных класса: `optionSet` и `jailbreak`.
*   `optionSet` используется для определения типа данных для набора параметров `tone` и `optionsSets`.
*   `jailbreak` содержит список опций `optionsSets`, используемых для "обхода" ограничений Bing Chat.

#### `optionSet`

**Описание**: Класс, определяющий типы данных для параметров `tone` и `optionsSets`.

#### `jailbreak`

**Описание**: Класс, содержащий список опций `optionsSets` для "обхода" ограничений Bing Chat.

### `Defaults`

**Описание**: Класс, содержащий значения по умолчанию для различных параметров Bing Chat.

**Принцип работы**:
Класс `Defaults` содержит значения по умолчанию, такие как разделитель сообщений (`delimiter`), IP-адрес (`ip_address`), список разрешенных типов сообщений (`allowedMessageTypes`), список идентификаторов срезов (`sliceIds`) и информацию о местоположении (`location`).

## Функции

### `_format`

```python
def _format(msg: dict) -> str:
    """Форматирует сообщение в JSON-формат и добавляет разделитель.

    Args:
        msg (dict): Словарь с сообщением.

    Returns:
        str: JSON-представление сообщения с добавленным разделителем.

    Как работает функция:
    1. Преобразует словарь `msg` в JSON-строку, используя `json.dumps` с параметром `ensure_ascii=False`, чтобы избежать экранирования символов Unicode.
    2. Добавляет к полученной JSON-строке разделитель `Defaults.delimiter`.

    Примеры:
    >>> Defaults.delimiter = '\\x1e'
    >>> _format({'text': 'Hello'})
    '{"text": "Hello"}\\x1e'
    """
```

### `create_conversation`

```python
async def create_conversation():
    """Создает новый разговор с Bing Chat API.

    Returns:
        tuple[str, str, str]: Кортеж, содержащий conversationId, clientId и conversationSignature.

    Raises:
        Exception: Если не удалось создать разговор после нескольких попыток.

    Как работает функция:

    Функция пытается создать разговор с сервером Bing, используя серию запросов.
    Если после нескольких попыток не удается получить нужные параметры, вызывается исключение.

    1.  Цикл `for _ in range(5)`: Повторяет попытки создания разговора до 5 раз.
    2.  `create = requests.get(...)`: Отправляет GET-запрос на URL для создания разговора, передавая необходимые заголовки.
        *   Заголовки содержат информацию о браузере, платформе и IP-адресе.
    3.  `conversationId = create.json().get('conversationId')`: Извлекает `conversationId` из JSON-ответа.
    4.  `clientId = create.json().get('clientId')`: Извлекает `clientId` из JSON-ответа.
    5.  `conversationSignature = create.json().get('conversationSignature')`: Извлекает `conversationSignature` из JSON-ответа.
    6.  `if not conversationId or not clientId or not conversationSignature and _ == 4`: Проверяет, все ли необходимые параметры были получены. Если хотя бы один из параметров отсутствует и это последняя попытка, вызывается исключение.

    Примеры:
    >>> # Для выполнения этого примера требуется реальный доступ к Bing API
    >>> # и корректная настройка заголовков и IP-адреса.
    >>> # В данном случае, просто покажем структуру возвращаемого значения.
    >>> async def example():
    ...     conversation_data = await create_conversation()
    ...     print(conversation_data)
    >>> # conversation_data может иметь вид: ('id_разговора', 'id_клиента', 'подпись_разговора')
    """
```

### `stream_generate`

```python
async def stream_generate(prompt: str, mode: optionsSets.optionSet = optionsSets.jailbreak, context: bool or str = False):
    """Генерирует ответы с использованием стриминга на основе предоставленной подсказки и контекста.

    Args:
        prompt (str): Подсказка для Bing Chat.
        mode (optionsSets.optionSet, optional): Набор опций для Bing Chat. По умолчанию optionsSets.jailbreak.
        context (bool | str, optional): Контекст для Bing Chat. По умолчанию False.

    Yields:
        str: Часть ответа от Bing Chat.

    Raises:
        Exception: Если произошла ошибка при генерации ответа.

    Как работает функция:
    Функция устанавливает соединение с Bing Chat API через WebSocket и обменивается сообщениями для генерации ответа на основе предоставленной подсказки и контекста.

    1.  `timeout = aiohttp.ClientTimeout(total=900)`: Устанавливает тайм-аут для HTTP-клиента.
    2.  `session = aiohttp.ClientSession(timeout=timeout)`: Создает асинхронную сессию HTTP-клиента.
    3.  `conversationId, clientId, conversationSignature = await create_conversation()`: Создает новый разговор и получает необходимые параметры.
    4.  `wss = await session.ws_connect(...)`: Устанавливает WebSocket-соединение с Bing Chat API.
        *   Передаются необходимые заголовки, включая `x-forwarded-for` с IP-адресом.
    5.  `await wss.send_str(_format({'protocol': 'json', 'version': 1}))`: Отправляет сообщение для установки протокола JSON.
    6.  `await wss.receive(timeout=900)`: Получает подтверждение установки протокола.
    7.  `struct = {...}`: Формирует структуру сообщения с аргументами для Bing Chat API.
        *   Включает подсказку, контекст, параметры разговора и другие необходимые данные.
    8.  `await wss.send_str(_format(struct))`: Отправляет сообщение с аргументами.
    9.  `while not final`: Цикл для получения сообщений от Bing Chat API до тех пор, пока не будет получен финальный ответ.
        *   `msg = await wss.receive(timeout=900)`: Получает сообщение.
        *   `objects = msg.data.split(Defaults.delimiter)`: Разбивает сообщение на объекты по разделителю.
        *   Обрабатывает каждый объект:
            *   Если `response.get('type') == 1`: Обрабатывает текстовое сообщение.
            *   Если `response.get('type') == 2`: Обрабатывает финальное сообщение с результатом.
        *   `yield (resp_txt.replace(cache_text, ''))`: Возвращает часть ответа.
    10. Закрывает WebSocket-соединение и HTTP-сессию.

    Примеры:
    >>> # Для выполнения этого примера требуется реальный доступ к Bing API
    >>> # и корректная настройка заголовков и IP-адреса.
    >>> async def example():
    ...     async for message in stream_generate("Как дела?"):
    ...         print(message)
    >>> # example() может выводить части ответа от Bing Chat API.
    """
```

### `run`

```python
def run(generator):
    """Запускает асинхронный генератор и возвращает значения.

    Args:
        generator: Асинхронный генератор.

    Yields:
        Any: Значения, возвращаемые генератором.

    Как работает функция:

    Функция запускает асинхронный генератор и возвращает значения, которые он генерирует.

    1.  `loop = asyncio.get_event_loop()`: Получает текущий event loop.
    2.  `gen = generator.__aiter__()`: Получает асинхронный итератор из генератора.
    3.  `while True`: Бесконечный цикл, который выполняется до тех пор, пока генератор не выбросит исключение `StopAsyncIteration`.
    4.  `next_val = loop.run_until_complete(gen.__anext__())`: Получает следующее значение из генератора, используя `loop.run_until_complete` для ожидания завершения асинхронной операции.
    5.  `yield next_val`: Возвращает полученное значение.
    6.  `except StopAsyncIteration`: Перехватывает исключение, когда генератор больше не имеет значений для возврата.
    7.  `break`: Выходит из цикла.

    Примеры:
    >>> async def my_generator():
    ...     yield "Hello"
    ...     yield "World"
    >>> for value in run(my_generator()):
    ...     print(value)
    Hello
    World
    """
```

### `convert`

```python
def convert(messages):
    """Преобразует список сообщений в контекст для Bing Chat API.

    Args:
        messages (list): Список словарей с сообщениями, где каждый словарь содержит ключи 'role' и 'content'.

    Returns:
        str: Строка, содержащая контекст для Bing Chat API.

    Как работает функция:

    Функция преобразует список сообщений в строку, которая может быть использована в качестве контекста для Bing Chat API.

    1.  `context = ""`: Инициализирует пустую строку для хранения контекста.
    2.  `for message in messages`: Перебирает каждое сообщение в списке `messages`.
    3.  `context += "[%s](#message)\\n%s\\n\\n" % (message['role'], message['content'])`: Форматирует каждое сообщение и добавляет его в строку контекста.
        *   `message['role']`: Роль отправителя сообщения (например, "user" или "assistant").
        *   `message['content']`: Содержание сообщения.
        *   `"[%s](#message)\\n%s\\n\\n"`: Формат строки, в которой роль и содержание сообщения разделяются символами новой строки.

    Примеры:
    >>> messages = [
    ...     {'role': 'user', 'content': 'Привет!'},
    ...     {'role': 'assistant', 'content': 'Здравствуйте!'}
    ... ]
    >>> convert(messages)
    '[user](#message)\\nПривет!\\n\\n[assistant](#message)\\nЗдравствуйте!\\n\\n'
    """
```

### `_create_completion`

```python
def _create_completion(model: str, messages: list, stream: bool, **kwargs):
    """Создает запрос на завершение текста и возвращает ответ от Bing Chat API.

    Args:
        model (str): Название модели.
        messages (list): Список сообщений для Bing Chat.
        stream (bool): Флаг, указывающий, использовать ли потоковую передачу.
        **kwargs: Дополнительные аргументы.

    Yields:
        str: Часть ответа от Bing Chat API.

    Как работает функция:

    Функция создает запрос к Bing Chat API для завершения текста на основе предоставленных сообщений и возвращает ответ в виде потока токенов.

    1.  `if len(messages) < 2`: Проверяет, содержит ли список сообщений менее двух элементов.
        *   Если да, то первый элемент считается подсказкой, а контекст отсутствует.
    2.  `prompt = messages[0]['content']`: Извлекает подсказку из первого сообщения.
    3.  `context = False`: Устанавливает контекст в `False`.
    4.  `else`: Если список сообщений содержит два или более элементов.
        *   `prompt = messages[-1]['content']`: Извлекает подсказку из последнего сообщения.
        *   `context = convert(messages[:-1])`: Преобразует все сообщения, кроме последнего, в контекст.
    5.  `response = run(stream_generate(prompt, optionsSets.jailbreak, context))`: Генерирует ответ с использованием потоковой передачи.
    6.  `for token in response`: Перебирает токены в ответе.
    7.  `yield (token)`: Возвращает каждый токен.

    Примеры:
    >>> # Для выполнения этого примера требуется реальный доступ к Bing API
    >>> # и корректная настройка заголовков и IP-адреса.
    >>> def example():
    ...     messages = [{'role': 'user', 'content': 'Как дела?'}]
    ...     for token in _create_completion('gpt-4', messages, True):
    ...         print(token, end='')
    >>> # example() может выводить части ответа от Bing Chat API.
    """