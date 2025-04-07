# Модуль Bing

## Обзор

Модуль `Bing.py` предоставляет интерфейс для взаимодействия с чат-ботом Bing AI. Он использует веб-сокеты для потоковой передачи ответов и включает в себя функциональность для создания бесед, форматирования сообщений и управления контекстом.

## Подробней

Модуль предназначен для использования в проекте `hypotez` для обеспечения возможности взаимодействия с Bing AI через API. Он содержит классы для управления опциями, настройками по умолчанию и функциями для создания, форматирования сообщений и стриминга генерации ответов.

## Классы

### `optionsSets`

**Описание**: Класс, содержащий наборы опций для настройки поведения чат-бота Bing AI.

**Аттрибуты**:
- `optionSet` (dict): Словарь, определяющий структуру набора опций.
- `jailbreak` (dict): Словарь с набором опций, используемых для "взлома" (jailbreak) ограничений Bing AI.

### `Defaults`

**Описание**: Класс, содержащий значения по умолчанию для различных параметров и настроек, используемых при взаимодействии с Bing AI.

**Аттрибуты**:
- `delimiter` (str): Разделитель, используемый для разделения сообщений в потоке данных.
- `ip_address` (str): IP-адрес, используемый для обхода ограничений геолокации.
- `allowedMessageTypes` (list): Список разрешенных типов сообщений.
- `sliceIds` (list): Список идентификаторов срезов.
- `location` (dict): Информация о местоположении пользователя.

## Функции

### `_format`

```python
def _format(msg: dict) -> str:
    """
    Форматирует сообщение в JSON-формат и добавляет разделитель в конце.

    Args:
        msg (dict): Словарь с сообщением.

    Returns:
        str: JSON-представление сообщения с разделителем.

    Как работает функция:
    1. Преобразует входящий словарь `msg` в JSON-строку, используя `json.dumps` с отключением экранирования ASCII символов (ensure_ascii=False).
    2. Добавляет к полученной JSON-строке разделитель, хранящийся в атрибуте `delimiter` класса `Defaults`.
    3. Возвращает полученную строку.

    ASCII flowchart:
    msg (dict) --> JSON.dumps (ensure_ascii=False) --> JSON-строка + Defaults.delimiter --> str

    Примеры:
        >>> Defaults.delimiter = '\\x1e'
        >>> _format({'key': 'value'})
        '{"key": "value"}\\x1e'
    """
    ...
```

### `create_conversation`

```python
async def create_conversation():
    """
    Создает разговор с Bing AI и возвращает идентификатор разговора, идентификатор клиента и подпись разговора.

    Returns:
        tuple[str, str, str]: Кортеж, содержащий conversationId, clientId и conversationSignature.

    Raises:
        Exception: Если не удается создать разговор после нескольких попыток.

    Как работает функция:
    1. Выполняет до 5 попыток создания разговора с Bing AI.
    2. Отправляет GET-запрос к `https://www.bing.com/turing/conversation/create` с определенными заголовками, имитирующими запрос от браузера.
    3. Извлекает из JSON-ответа `conversationId`, `clientId` и `conversationSignature`.
    4. Если хотя бы один из параметров отсутствует после нескольких попыток, вызывает исключение.

    ASCII flowchart:
    Начало --> GET-запрос к Bing --> Извлечение conversationId, clientId, conversationSignature --> Возврат conversationId, clientId, conversationSignature

    Примеры:
        Функция не принимает аргументов, поэтому примеры вызова не требуются.
    """
    ...
```

### `stream_generate`

```python
async def stream_generate(prompt: str, mode: optionsSets.optionSet = optionsSets.jailbreak, context: bool | str = False):
    """
    Генерирует текст от Bing AI в потоковом режиме.

    Args:
        prompt (str): Текст запроса.
        mode (optionsSets.optionSet, optional): Набор опций для запроса. По умолчанию `optionsSets.jailbreak`.
        context (bool | str, optional): Контекст для запроса. По умолчанию `False`.

    Yields:
        str: Часть сгенерированного текста.

    Raises:
        Exception: Если возникает ошибка при обработке ответа от Bing AI.

    Как работает функция:
    1. Устанавливает таймаут для запроса.
    2. Создает сессию aiohttp.
    3. Получает conversationId, clientId и conversationSignature с помощью `create_conversation()`.
    4. Устанавливает соединение WebSocket с Bing AI.
    5. Отправляет начальное сообщение для установки протокола.
    6. Формирует структуру запроса с учетом параметров `prompt`, `mode` и `context`.
    7. Отправляет запрос Bing AI через WebSocket.
    8. Получает ответы от Bing AI, обрабатывает их и извлекает текст.
    9. Возвращает текст частями через yield.

    ASCII flowchart:
    Начало --> create_conversation() --> WebSocket-соединение --> Отправка запроса --> Получение ответа --> Извлечение текста --> yield текст

    Примеры:
        Функция является асинхронной и требует event loop для выполнения.
    """
    ...
```

### `run`

```python
def run(generator):
    """
    Запускает асинхронный генератор и возвращает значения.

    Args:
        generator: Асинхронный генератор.

    Yields:
        next_val: Значение, возвращаемое генератором.

    Как работает функция:
    1. Получает event loop.
    2. Преобразует переданный генератор в асинхронный итератор.
    3. В цикле пытается получить следующее значение из асинхронного итератора с помощью `loop.run_until_complete(gen.__anext__())`.
    4. Возвращает полученное значение через `yield`.
    5. Останавливает итерацию при возникновении исключения `StopAsyncIteration`.

    ASCII flowchart:
    generator --> __aiter__() --> gen --> loop.run_until_complete(gen.__anext__()) --> next_val --> yield next_val

    Примеры:
    Пример использования run с асинхронным генератором stream_generate:
        >>> async def my_generator():
        ...     yield "Hello"
        ...     yield "World"
        >>> generator = my_generator()
        >>> for value in run(generator):
        ...     print(value)
        Hello
        World
    """
    ...
```

### `convert`

```python
def convert(messages):
    """
    Преобразует список сообщений в строку контекста.

    Args:
        messages (list): Список сообщений, где каждое сообщение - словарь с ключами 'role' и 'content'.

    Returns:
        str: Строка контекста, сформированная из сообщений.

    Как работает функция:
    1. Инициализирует пустую строку `context`.
    2. Проходит по каждому сообщению в списке `messages`.
    3. Форматирует каждое сообщение в виде строки `"[роль](#message)\nсодержимое\n\n"` и добавляет его к строке `context`.

    ASCII flowchart:
    messages --> Цикл по сообщениям --> Форматирование сообщения --> Добавление сообщения в context --> str

    Примеры:
        >>> messages = [{'role': 'user', 'content': 'Привет'}, {'role': 'bot', 'content': 'Здравствуйте'}]
        >>> convert(messages)
        '[user](#message)\\nПривет\\n\\n[bot](#message)\\nЗдравствуйте\\n\\n'
    """
    ...
```

### `_create_completion`

```python
def _create_completion(model: str, messages: list, stream: bool, **kwargs):
    """
    Создает запрос к Bing AI и возвращает ответ в виде потока токенов.

    Args:
        model (str): Идентификатор модели.
        messages (list): Список сообщений для контекста.
        stream (bool): Флаг, указывающий на потоковую передачу данных.
        **kwargs: Дополнительные аргументы.

    Yields:
        str: Токен ответа от Bing AI.

    Как работает функция:
    1. Определяет `prompt` и `context` в зависимости от количества сообщений:
        - Если сообщение меньше двух, то первый элемент из `messages` присваивается переменной `prompt`, а `context` = `False`.
        - Иначе `prompt` - это последний элемент `messages`, а `context` - все сообщения, кроме последнего, преобразованные функцией `convert`.
    2. Запускает генерацию ответа с помощью `stream_generate` с параметрами `prompt`, `optionsSets.jailbreak` и `context`.
    3. Возвращает токены ответа через `yield`.

    ASCII flowchart:
    messages --> Определение prompt и context --> stream_generate() --> Цикл по токенам --> yield token

    Примеры:
        Функция использует `stream_generate`, примеры вызова зависят от асинхронной природы этой функции.
    """
    ...
```

### `params`

```python
params = f\'g4f.Providers.{os.path.basename(__file__)[:-3]} supports: \' + \'(%s)\' % \', \'.join( [f"{name}: {get_type_hints(_create_completion)[name].__name__}" for name in _create_completion.__code__.co_varnames[:_create_completion.__code__.co_argcount]])
```

**Описание**: Строка, содержащая информацию о поддерживаемых параметрах функцией `_create_completion`.

**Как работает функция**:
1. Формирует строку, содержащую имя файла модуля и информацию о поддерживаемых параметрах функции `_create_completion`.
2. Использует `get_type_hints` для получения аннотаций типов параметров функции `_create_completion`.
3. Извлекает имена параметров из `_create_completion.__code__.co_varnames`.
4. Объединяет информацию о параметрах в строку.