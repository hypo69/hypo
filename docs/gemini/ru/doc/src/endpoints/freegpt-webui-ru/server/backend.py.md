# Модуль backend.py

## Обзор

Модуль `backend.py` предоставляет API для взаимодействия с различными языковыми моделями (например, ChatGPT) через веб-интерфейс. Он включает в себя обработку запросов, формирование сообщений для модели, выполнение поисковых запросов и генерацию ответов.

## Подробней

Этот модуль является частью серверной части приложения и отвечает за обработку входящих запросов, формирование контекста для языковой модели и возврат сгенерированных ответов. Он использует библиотеки `g4f`, `googletrans` и `requests` для взаимодействия с внешними сервисами и API. Также в модуле реализована поддержка автоматического использования прокси для обхода ограничений доступа к API.

## Классы

### `Backend_Api`

**Описание**: Класс `Backend_Api` инкапсулирует API для взаимодействия с языковой моделью.

**Принцип работы**: Класс инициализируется с Flask-приложением и конфигурацией, включающей информацию об использовании автоматических прокси. Он определяет маршруты для обработки входящих запросов и запускает отдельный поток для обновления списка рабочих прокси, если это необходимо.

**Атрибуты**:

- `app`: Flask-приложение.
- `use_auto_proxy` (bool): Флаг, указывающий на использование автоматических прокси.
- `routes` (dict): Словарь, содержащий маршруты API и соответствующие функции для их обработки.

**Методы**:

- `__init__(self, app, config: dict) -> None`: Инициализирует экземпляр класса `Backend_Api`.
- `_conversation(self)`: Обрабатывает запрос на разговор с языковой моделью.

#### `Backend_Api.__init__`

```python
def __init__(self, app, config: dict) -> None:
    """Инициализирует экземпляр класса Backend_Api.

    Args:
        app: Flask-приложение.
        config (dict): Конфигурация приложения.

    Returns:
        None
    """
```

#### `Backend_Api._conversation`

```python
def _conversation(self):
    """Обрабатывает запрос на разговор с языковой моделью.

    Извлекает параметры из запроса, такие как streaming, jailbreak, model и messages.
    Использует ChatCompletion.create для генерации ответа от языковой модели.
    Возвращает ответ в формате streaming, если это указано в запросе.
    В случае возникновения исключения, возвращает сообщение об ошибке с кодом 400.

    Returns:
        Flask.response_class: Сгенерированный ответ от языковой модели в формате streaming,
                              если параметр 'stream' установлен в True.
        dict: В случае ошибки возвращает словарь с информацией об ошибке и кодом 400.

    Raises:
        Exception as ex: Если возникает ошибка при обработке запроса или взаимодействии с языковой моделью.
                         В этом случае, информация об ошибке логируется.
    """
```

**Как работает функция**:

1. Извлекает параметры из запроса: `streaming`, `jailbreak`, `model`, `messages`.
2. Использует `ChatCompletion.create` для получения ответа от языковой модели.
3. Возвращает ответ в формате потока (`text/event-stream`), если `streaming` равен `True`.
4. Обрабатывает исключения, логирует ошибки и возвращает сообщение об ошибке в формате JSON с кодом 400.

```
Начало --> Извлечение параметров из запроса (streaming, jailbreak, model, messages)
     |
     --> Вызов ChatCompletion.create(model=model, messages=messages)
     |
     --> Генерация ответа в формате streaming (если streaming=True) или в формате JSON (если streaming=False)
     |
     --> Обработка исключений (логирование ошибки, возврат сообщения об ошибке)
     |
Конец
```

**Примеры**:

Пример успешного вызова:
```python
# request.json = {'stream': True, 'jailbreak': 'Default', 'model': 'gpt-3.5-turbo', 'meta': {'content': {'conversation': [], 'internet_access': False, 'parts': [{'content': 'Hello', 'role': 'user'}]}}}
response = Backend_Api(app, config)._conversation()
```
Пример вызова с ошибкой:
```python
# request.json = {'stream': True, 'jailbreak': 'Default', 'model': 'invalid-model', 'meta': {'content': {'conversation': [], 'internet_access': False, 'parts': [{'content': 'Hello', 'role': 'user'}]}}}
response = Backend_Api(app, config)._conversation()
# response будет содержать словарь с информацией об ошибке и кодом 400
```

## Функции

### `build_messages`

```python
def build_messages(jailbreak):
    """Создает список сообщений для отправки в языковую модель.

    Формирует системное сообщение, добавляет историю разговора, результаты поиска в интернете (если разрешено) и инструкции jailbreak (если разрешено).

    Args:
        jailbreak: Имя jailbreak-инструкции.

    Returns:
        list: Список сообщений для отправки в языковую модель.

    Raises:
        Нет исключений.
    """
```

**Как работает функция**:

1. Извлекает данные из `request.json`: `_conversation`, `internet_access`, `prompt`.
2. Формирует системное сообщение, включающее текущую дату и язык ответа.
3. Добавляет историю разговора (`_conversation`).
4. Добавляет результаты поиска в интернете, если `internet_access` равен `True`.
5. Добавляет jailbreak-инструкции, если `jailbreak` не равен `"Default"`.
6. Добавляет пользовательский запрос (`prompt`).
7. Ограничивает размер разговора до 13 последних сообщений.

```
Начало --> Извлечение данных из request.json (_conversation, internet_access, prompt)
     |
     --> Формирование системного сообщения (current_date, set_response_language)
     |
     --> Добавление истории разговора (_conversation)
     |
     --> Добавление результатов поиска (fetch_search_results), если internet_access=True
     |
     --> Добавление jailbreak-инструкций (isJailbreak), если jailbreak != "Default"
     |
     --> Добавление пользовательского запроса (prompt)
     |
     --> Ограничение размера разговора (conversation[-13:])
     |
Конец
```

**Примеры**:

Пример вызова без jailbreak и с доступом в интернет:
```python
# request.json = {'meta': {'content': {'conversation': [], 'internet_access': True, 'parts': [{'content': 'Hello', 'role': 'user'}]}}, 'jailbreak': 'Default'}
messages = build_messages('Default')
```

Пример вызова с jailbreak и без доступа в интернет:
```python
# request.json = {'meta': {'content': {'conversation': [], 'internet_access': False, 'parts': [{'content': 'Hello', 'role': 'user'}]}}, 'jailbreak': 'Custom'}
messages = build_messages('Custom')
```

### `fetch_search_results`

```python
def fetch_search_results(query):
    """Выполняет поиск в интернете и возвращает результаты.

    Использует DuckDuckGo API для поиска информации в интернете по заданному запросу.

    Args:
        query (str): Поисковой запрос.

    Returns:
        list: Список результатов поиска в формате сообщений для языковой модели.

    Raises:
        Нет исключений.
    """
```

**Как работает функция**:

1. Выполняет GET-запрос к DuckDuckGo API с поисковым запросом и ограничением на 5 результатов.
2. Формирует список результатов, добавляя сниппет и URL каждого результата.
3. Возвращает список результатов в формате сообщений для языковой модели.

```
Начало --> GET-запрос к DuckDuckGo API (query, limit=5)
     |
     --> Формирование списка результатов (snippet, URL)
     |
     --> Возврат списка результатов
     |
Конец
```

**Примеры**:

Пример вызова:
```python
results = fetch_search_results('What is the capital of France?')
```

### `generate_stream`

```python
def generate_stream(response, jailbreak):
    """Генерирует поток сообщений в зависимости от jailbreak-инструкций.

    В зависимости от того, используется ли jailbreak, функция генерирует поток сообщений, проверяя, успешно ли выполнена jailbreak-инструкция.

    Args:
        response: Ответ от языковой модели.
        jailbreak: Имя jailbreak-инструкции.

    Yields:
        str: Сообщения из ответа языковой модели.

    Raises:
        Нет исключений.
    """
```

**Как работает функция**:

1. Проверяет, используется ли jailbreak.
2. Если jailbreak используется, итерируется по сообщениям ответа, проверяя, выполнена ли jailbreak-инструкция успешно или нет.
3. Если jailbreak не используется, возвращает поток сообщений ответа без изменений.

```
Начало --> Проверка, используется ли jailbreak (isJailbreak)
     |
     --> Если jailbreak используется:
     |    --> Итерация по сообщениям ответа
     |    --> Проверка успешности jailbreak (response_jailbroken_success)
     |    --> Проверка неудачи jailbreak (response_jailbroken_failed)
     |    --> Возврат сообщений
     |
     --> Если jailbreak не используется:
     |    --> Возврат потока сообщений ответа
     |
Конец
```

**Примеры**:

Пример вызова с jailbreak:
```python
# response = ['ACT: Hello', ' how are you?']
# jailbreak = 'Custom'
stream = generate_stream(response, 'Custom')
# stream будет содержать сообщения ответа после успешной проверки jailbreak
```

Пример вызова без jailbreak:
```python
# response = ['Hello', ' how are you?']
# jailbreak = 'Default'
stream = generate_stream(response, 'Default')
# stream будет содержать все сообщения ответа
```

### `response_jailbroken_success`

```python
def response_jailbroken_success(response: str) -> bool:
    """Проверяет, успешно ли выполнена jailbreak-инструкция.

    Ищет в ответе языковой модели маркер "ACT:", указывающий на успешное выполнение jailbreak-инструкции.

    Args:
        response (str): Ответ от языковой модели.

    Returns:
        bool: True, если jailbreak-инструкция выполнена успешно, False в противном случае.

    Raises:
        Нет исключений.
    """
```

**Как работает функция**:

1. Ищет в ответе маркер `"ACT:"`.
2. Возвращает `True`, если маркер найден, `False` в противном случае.

```
Начало --> Поиск маркера "ACT:" в ответе
     |
     --> Возврат True, если маркер найден, False в противном случае
     |
Конец
```

**Примеры**:

Пример успешного выполнения jailbreak:
```python
response = 'ACT: Hello, how are you?'
success = response_jailbroken_success(response)  # success будет True
```

Пример неуспешного выполнения jailbreak:
```python
response = 'Hello, how are you?'
success = response_jailbroken_success(response)  # success будет False
```

### `response_jailbroken_failed`

```python
def response_jailbroken_failed(response):
    """Проверяет, не произошла ли ошибка при выполнении jailbreak-инструкции.

    Проверяет, начинается ли ответ с "GPT:" или "ACT:". Если нет, значит, произошла ошибка.

    Args:
        response: Ответ от языковой модели.

    Returns:
        bool: False, если длина ответа меньше 4 символов. True, если ответ не начинается с "GPT:" или "ACT:".

    Raises:
        Нет исключений.
    """
```

**Как работает функция**:

1. Проверяет длину ответа. Если длина ответа меньше 4 символов, возвращает `False`.
2. Проверяет, начинается ли ответ с `"GPT:"` или `"ACT:"`.
3. Возвращает `False`, если ответ начинается с `"GPT:"` или `"ACT:"`, в противном случае возвращает `True`.

```
Начало --> Проверка длины ответа (len(response) < 4)
     |
     --> Проверка начала ответа (response.startswith("GPT:") or response.startswith("ACT:"))
     |
     --> Возврат False, если длина ответа меньше 4 символов или ответ начинается с "GPT:" или "ACT:", в противном случае возврат True
     |
Конец
```

**Примеры**:

Пример ошибки при выполнении jailbreak:
```python
response = 'Error'
failed = response_jailbroken_failed(response)  # failed будет True
```

Пример успешного выполнения jailbreak:
```python
response = 'ACT: Hello'
failed = response_jailbroken_failed(response)  # failed будет False
```

### `set_response_language`

```python
def set_response_language(prompt):
    """Определяет язык запроса и возвращает инструкцию для языковой модели.

    Использует Google Translate API для определения языка запроса и формирует инструкцию для языковой модели, чтобы она отвечала на этом языке.

    Args:
        prompt: Текст запроса.

    Returns:
        str: Инструкция для языковой модели.

    Raises:
        Нет исключений.
    """
```

**Как работает функция**:

1. Использует `Translator` из библиотеки `googletrans` для определения языка запроса.
2. Формирует инструкцию для языковой модели, чтобы она отвечала на определенном языке.
3. Возвращает инструкцию.

```
Начало --> Определение языка запроса (translator.detect(prompt['content']).lang)
     |
     --> Формирование инструкции для языковой модели
     |
     --> Возврат инструкции
     |
Конец
```

**Примеры**:

Пример вызова:
```python
prompt = {'content': 'Hello, how are you?'}
instruction = set_response_language(prompt)
# instruction будет 'You will respond in the language: en. '
```

### `isJailbreak`

```python
def isJailbreak(jailbreak):
    """Проверяет, используется ли jailbreak, и возвращает соответствующие инструкции.

    Args:
        jailbreak: Имя jailbreak-инструкции.

    Returns:
        list | None: Список инструкций, если jailbreak используется и найден в `special_instructions`. None в противном случае.

    Raises:
        Нет исключений.
    """
```

**Как работает функция**:

1. Проверяет, не равен ли `jailbreak` `"Default"`.
2. Если `jailbreak` не равен `"Default"`, проверяет, есть ли `jailbreak` в `special_instructions`.
3. Если `jailbreak` есть в `special_instructions`, возвращает соответствующие инструкции.
4. Если `jailbreak` нет в `special_instructions` или равен `"Default"`, возвращает `None`.

```
Начало --> Проверка jailbreak != "Default"
     |
     --> Проверка jailbreak in special_instructions
     |
     --> Возврат special_instructions[jailbreak], если jailbreak in special_instructions, None в противном случае
     |
Конец
```

**Примеры**:

Пример использования jailbreak:
```python
jailbreak = 'Custom'
instructions = isJailbreak(jailbreak)
# Если 'Custom' есть в special_instructions, instructions будет списком инструкций, иначе None
```

Пример без использования jailbreak:
```python
jailbreak = 'Default'
instructions = isJailbreak(jailbreak)  # instructions будет None