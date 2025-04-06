# Модуль Bing.py
## Обзор

Модуль предоставляет класс для взаимодействия с Bing AI через веб-сокеты для генерации текста. 
Модуль включает в себя функции для создания диалога, отправки запросов и получения потоковых ответов.

## Подробнее

Этот модуль предназначен для работы с Bing AI. Он использует веб-сокеты для установления соединения, отправки запросов и получения ответов в режиме реального времени. 
В модуле реализована поддержка потоковой передачи данных, что позволяет получать ответы по частям, а не ждать завершения всей генерации.

Модуль содержит следующие компоненты:

-   Настройки SSL для безопасного соединения.
-   Классы для определения наборов опций и значений по умолчанию.
-   Функции для создания и форматирования сообщений, установления соединения и обмена данными через веб-сокеты.

## Классы

### `optionsSets`

**Описание**: Класс, предназначенный для хранения различных наборов опций, используемых при взаимодействии с Bing AI.

**Принцип работы**:
Класс содержит два атрибута: `optionSet` и `jailbreak`. 
`optionSet` представляет собой словарь, определяющий структуру набора опций с указанием типа данных для каждой опции. 
`jailbreak` содержит список опций, используемых для "обхода" ограничений Bing AI.

**Атрибуты**:

-   `optionSet` (dict): Словарь, определяющий структуру набора опций.
    -   `tone` (str): Тип данных для опции "tone".
    -   `optionsSets` (list): Тип данных для опции "optionsSets".
-   `jailbreak` (dict): Словарь, содержащий список опций для "обхода" ограничений Bing AI.
    -   `optionsSets` (list): Список строк, представляющих опции для "обхода" ограничений.

### `Defaults`

**Описание**: Класс, предназначенный для хранения значений по умолчанию, используемых при взаимодействии с Bing AI.

**Принцип работы**:
Класс содержит статические атрибуты, определяющие значения по умолчанию для различных параметров, таких как разделитель сообщений, IP-адрес, разрешенные типы сообщений, идентификаторы срезов и информация о местоположении.

**Атрибуты**:

-   `delimiter` (str): Разделитель сообщений, используемый при обмене данными с Bing AI.
-   `ip_address` (str): IP-адрес, используемый для запросов к Bing AI.
-   `allowedMessageTypes` (list): Список разрешенных типов сообщений.
-   `sliceIds` (list): Список идентификаторов срезов.
-   `location` (dict): Словарь, содержащий информацию о местоположении пользователя.

## Функции

### `_format`

```python
def _format(msg: dict) -> str:
    """ Функция форматирует сообщение в JSON-формат и добавляет разделитель.
    Args:
        msg (dict): Сообщение для форматирования.

    Returns:
        str: JSON-представление сообщения с добавленным разделителем.

    Как работает функция:
    1. Преобразует входящий словарь `msg` в JSON-строку с помощью `json.dumps`,
       гарантируя, что не-ASCII символы будут корректно обработаны.
    2. Добавляет к полученной JSON-строке разделитель `Defaults.delimiter`.
    3. Возвращает отформатированную строку.
    """
```

**Назначение**: Форматирование сообщения в JSON-формат с добавлением разделителя.

**Параметры**:

-   `msg` (dict): Сообщение для форматирования.

**Возвращает**:

-   `str`: JSON-представление сообщения с добавленным разделителем.

**Как работает функция**:

```
      msg (dict)
        |
        V
    json.dumps (ensure_ascii=False)
        |
        V
    JSON-string + Defaults.delimiter
        |
        V
    return string
```

**Примеры**:

```python
message = {"text": "Hello, Bing!"}
formatted_message = _format(message)
print(formatted_message)  # Пример вывода: {"text": "Hello, Bing!"}\x1e
```

### `create_conversation`

```python
async def create_conversation():
    """ Функция создает диалог с Bing AI и возвращает идентификаторы и сигнатуру.

    Returns:
        tuple[str, str, str]: Кортеж, содержащий conversationId, clientId и conversationSignature.

    Raises:
        Exception: Если не удалось создать диалог после нескольких попыток.

    Как работает функция:
    1. Пытается создать диалог с Bing AI, отправляя GET-запрос к `https://www.bing.com/turing/conversation/create`.
    2. Извлекает из ответа `conversationId`, `clientId` и `conversationSignature`.
    3. Если не удалось получить все необходимые идентификаторы после нескольких попыток, выбрасывает исключение.
    """
```

**Назначение**: Создание диалога с Bing AI и получение идентификаторов и сигнатуры.

**Возвращает**:

-   `tuple[str, str, str]`: Кортеж, содержащий `conversationId`, `clientId` и `conversationSignature`.

**Вызывает исключения**:

-   `Exception`: Если не удалось создать диалог после нескольких попыток.

**Как работает функция**:

```
    loop (5 times)
        |
        V
    GET request to Bing API
        |
        V
    Extract conversationId, clientId, conversationSignature
        |
        V
    Check if all IDs are present
        |
        V
    return conversationId, clientId, conversationSignature
```

**Примеры**:

```python
conversation_id, client_id, conversation_signature = await create_conversation()
print(f"Conversation ID: {conversation_id}")
print(f"Client ID: {client_id}")
print(f"Conversation Signature: {conversation_signature}")
```

### `stream_generate`

```python
async def stream_generate(prompt: str, mode: optionsSets.optionSet = optionsSets.jailbreak, context: bool or str = False):
    """ Функция генерирует текст с использованием Bing AI и возвращает потоковый ответ.

    Args:
        prompt (str): Текст запроса.
        mode (optionsSets.optionSet): Набор опций. По умолчанию `optionsSets.jailbreak`.
        context (bool or str): Контекст запроса. По умолчанию `False`.

    Yields:
        str: Часть сгенерированного текста.

    Raises:
        Exception: Если произошла ошибка при генерации текста.
    """
```

**Назначение**: Генерация текста с использованием Bing AI и получение потокового ответа.

**Параметры**:

-   `prompt` (str): Текст запроса.
-   `mode` (optionsSets.optionSet): Набор опций. По умолчанию `optionsSets.jailbreak`.
-   `context` (bool or str): Контекст запроса. По умолчанию `False`.

**Yields**:

-   `str`: Часть сгенерированного текста.

**Вызывает исключения**:

-   `Exception`: Если произошла ошибка при генерации текста.

**Как работает функция**:

```
    create_conversation()
        |
        V
    ws_connect to Bing API
        |
        V
    Send initial messages
        |
        V
    Send prompt with context
        |
        V
    Receive messages
        |
        V
    Process messages to extract text
        |
        V
    Yield text
        |
        V
    Close connection
```

**Примеры**:

```python
async for token in stream_generate("Tell me a story."):
    print(token, end="")
```

### `run`

```python
def run(generator):
    """ Функция запускает асинхронный генератор и возвращает его значения.

    Args:
        generator: Асинхронный генератор.

    Yields:
        Any: Значение, возвращаемое генератором.

    Raises:
        StopAsyncIteration: Когда генератор завершает работу.

    Как работает функция:
    1. Получает event loop.
    2. Преобразует асинхронный генератор в асинхронный итератор.
    3. Итерируется по асинхронному итератору, получая значения.
    4. Возвращает значения, полученные от асинхронного итератора.
    5. Завершает работу, когда асинхронный итератор выбрасывает исключение StopAsyncIteration.
    """
```

**Назначение**: Запуск асинхронного генератора и возврат его значений.

**Параметры**:

-   `generator`: Асинхронный генератор.

**Yields**:

-   `Any`: Значение, возвращаемое генератором.

**Вызывает исключения**:

-   `StopAsyncIteration`: Когда генератор завершает работу.

**Как работает функция**:

```
    Get event loop
        |
        V
    Convert async generator to async iterator
        |
        V
    Iterate over async iterator
        |
        V
    Return values from async iterator
        |
        V
    Stop when StopAsyncIteration is raised
```

**Примеры**:

```python
def my_generator():
    yield 1
    yield 2
    yield 3

for value in run(my_generator()):
    print(value)
```

### `convert`

```python
def convert(messages):
    """ Функция преобразует список сообщений в контекст для Bing AI.

    Args:
        messages (list): Список сообщений для преобразования.

    Returns:
        str: Контекст, отформатированный для Bing AI.

    Как работает функция:
    1. Итерируется по списку сообщений.
    2. Форматирует каждое сообщение в строку с использованием роли и содержимого.
    3. Объединяет отформатированные строки в одну строку, разделяя их символами новой строки.
    4. Возвращает полученную строку.
    """
```

**Назначение**: Преобразование списка сообщений в контекст для Bing AI.

**Параметры**:

-   `messages` (list): Список сообщений для преобразования.

**Возвращает**:

-   `str`: Контекст, отформатированный для Bing AI.

**Как работает функция**:

```
    messages (list)
        |
        V
    Iterate over messages
        |
        V
    Format each message as a string
        |
        V
    Concatenate formatted strings
        |
        V
    Return context string
```

**Примеры**:

```python
messages = [
    {"role": "user", "content": "Hello"},
    {"role": "assistant", "content": "Hi there"}
]
context = convert(messages)
print(context)
```

### `_create_completion`

```python
def _create_completion(model: str, messages: list, stream: bool, **kwargs):
    """ Функция создает запрос к Bing AI и возвращает ответ.

    Args:
        model (str): Модель для использования.
        messages (list): Список сообщений для отправки.
        stream (bool): Флаг, указывающий, использовать ли потоковый режим.
        **kwargs: Дополнительные аргументы.

    Yields:
        str: Часть ответа от Bing AI.

    Как работает функция:
    1. Извлекает текст запроса и контекст из списка сообщений.
    2. Запускает генерацию текста с использованием функции stream_generate.
    3. Возвращает части ответа, полученные от Bing AI.
    """
```

**Назначение**: Создание запроса к Bing AI и возврат ответа.

**Параметры**:

-   `model` (str): Модель для использования.
-   `messages` (list): Список сообщений для отправки.
-   `stream` (bool): Флаг, указывающий, использовать ли потоковый режим.
-   `**kwargs`: Дополнительные аргументы.

**Yields**:

-   `str`: Часть ответа от Bing AI.

**Как работает функция**:

```
    messages (list)
        |
        V
    Extract prompt and context
        |
        V
    stream_generate()
        |
        V
    Yield tokens from response
```

**Примеры**:

```python
messages = [
    {"role": "user", "content": "Tell me a joke."}
]
for token in _create_completion("gpt-4", messages, True):
    print(token, end="")
```

### params

```python
params = f\'g4f.Providers.{os.path.basename(__file__)[:-3]} supports: \' + \\\n    \'(%s)\' % \', \'.join(\n        [f"{name}: {get_type_hints(_create_completion)[name].__name__}" for name in _create_completion.__code__.co_varnames[:_create_completion.__code__.co_argcount]])
```

**Описание**: Строка, содержащая информацию о поддерживаемых параметрах функции `_create_completion`.

**Назначение**: Формирование строки с информацией о поддерживаемых параметрах функции `_create_completion`.

**Как работает**:

1.  `os.path.basename(__file__)[:-3]`: Извлекает имя файла модуля без расширения `.py`.
2.  `get_type_hints(_create_completion)`: Получает аннотации типов для параметров функции `_create_completion`.
3.  `_create_completion.__code__.co_varnames[:_create_completion.__code__.co_argcount]`: Получает имена параметров функции `_create_completion`.
4.  Формирует строку, содержащую информацию о поддерживаемых параметрах и их типах.