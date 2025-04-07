# Модуль `backend.py`

## Обзор

Модуль предоставляет API для обработки запросов к серверу, включая ведение диалогов, настройку прокси и обработку специальных инструкций (jailbreak). Он содержит класс `Backend_Api`, который управляет маршрутами и обработкой запросов, а также набор функций для построения сообщений, получения результатов поиска, генерации потока ответов и определения языка ответа.

## Подробнее

Этот модуль является частью серверной логики и отвечает за обработку входящих запросов, взаимодействие с внешними API (например, Google Translate и DuckDuckGo API), а также управление диалогами и прокси-серверами. Модуль использует библиотеку `flask` для создания API и `googletrans` для определения языка запроса.

## Классы

### `Backend_Api`

**Описание**: Класс `Backend_Api` инициализирует API-сервер Flask, настраивает маршруты для обработки запросов и управляет прокси-серверами.

**Принцип работы**:
Класс инициализируется с приложением Flask и конфигурацией. Он определяет маршруты для API, такие как `/backend-api/v2/conversation`, и связывает их с соответствующими функциями обработки. Если включено автоматическое использование прокси, класс запускает отдельный поток для обновления списка рабочих прокси.

**Атрибуты**:
- `app`: Экземпляр приложения Flask.
- `use_auto_proxy`: Флаг, указывающий, следует ли использовать автоматическое обновление прокси.
- `routes`: Словарь, содержащий маршруты API и связанные с ними функции и методы.

**Методы**:

- `__init__(self, app, config: dict) -> None`:
    ```python
    def __init__(self, app, config: dict) -> None:
        """Инициализирует экземпляр класса `Backend_Api`.

        Args:
            app: Экземпляр приложения Flask.
            config (dict): Словарь конфигурации, содержащий параметры `use_auto_proxy`.

        Returns:
            None
        """
    ```
- `_conversation(self)`:
    ```python
    def _conversation(self):
        """Обрабатывает запрос на ведение диалога.

        Извлекает параметры из запроса, такие как `stream`, `jailbreak`, `model` и `messages`,
        использует их для генерации ответа с помощью `ChatCompletion.create`.
        В случае ошибки возвращает сообщение об ошибке.

        Returns:
            app.response_class: Сгенерированный поток данных (stream) или словарь с ошибкой.
            int: HTTP-код ответа.

        Raises:
            Exception: Если возникает ошибка при обработке запроса.
        """
    ```

## Функции

### `build_messages(jailbreak)`

```python
def build_messages(jailbreak):
    """Строит сообщение для запроса к API, используя информацию из запроса и системные настройки.

    Извлекает данные из JSON-запроса (`meta`, `content`, `conversation`, `internet_access`, `parts`),
    генерирует системное сообщение на основе текущей даты и языка запроса,
    добавляет историю разговоров, результаты поиска (если разрешено) и инструкции jailbreak (если включено).
    Ограничивает размер разговора для избежания ошибок, связанных с количеством токенов.

    Args:
        jailbreak: Идентификатор или название jailbreak-инструкции.

    Returns:
        list: Список сообщений, представляющих собой историю разговоров,
              дополненную системными сообщениями и результатами поиска.
    """
```

**Как работает функция**:

1. **Извлечение данных из запроса**: Извлекает необходимые данные из JSON-запроса, такие как история разговоров, параметры доступа в интернет и содержимое запроса.
2. **Генерация системного сообщения**: Формирует системное сообщение, включающее текущую дату и язык ответа.
3. **Построение истории разговоров**: Добавляет существующую историю разговоров к системному сообщению.
4. **Добавление результатов поиска (если разрешено)**: Если включен доступ в интернет, выполняет поиск и добавляет результаты к истории разговоров.
5. **Добавление инструкций jailbreak (если включено)**: Если включены инструкции jailbreak, добавляет их к истории разговоров.
6. **Ограничение размера разговора**: Ограничивает размер истории разговоров, чтобы избежать ошибок, связанных с количеством токенов.

**ASII flowchart**:

```
Начало
    ↓
A (Извлечение данных из запроса)
    ↓
B (Генерация системного сообщения)
    ↓
C (Построение истории разговоров)
    ↓
D (Добавление результатов поиска, если разрешено)
    ↓
E (Добавление инструкций jailbreak, если включено)
    ↓
F (Ограничение размера разговора)
    ↓
Конец (Возврат списка сообщений)
```

**Примеры**:

Пример 1: Без jailbreak и доступа в интернет

```python
request.json = {
    'meta': {
        'content': {
            'conversation': [],
            'internet_access': False,
            'parts': [{'role': 'user', 'content': 'Hello'}]
        }
    },
    'jailbreak': 'Default'
}
messages = build_messages('Default')
print(messages)
```

Пример 2: С jailbreak и доступом в интернет

```python
request.json = {
    'meta': {
        'content': {
            'conversation': [],
            'internet_access': True,
            'parts': [{'role': 'user', 'content': 'Search for something'}]
        }
    },
    'jailbreak': 'Custom'
}
special_instructions = {'Custom': [{'role': 'system', 'content': 'Custom instructions'}]}
messages = build_messages('Custom')
print(messages)
```

### `fetch_search_results(query)`

```python
def fetch_search_results(query):
    """Получает результаты поиска из DuckDuckGo API.

    Выполняет запрос к API с заданным запросом, ограничивает количество результатов,
    формирует сниппеты с информацией о каждом результате и возвращает их в виде списка сообщений.

    Args:
        query (str): Поисковой запрос.

    Returns:
        list: Список сообщений, содержащих результаты поиска.
    """
```

**Как работает функция**:

1. **Выполнение запроса к API**: Выполняет GET-запрос к DuckDuckGo API с заданным поисковым запросом и ограничением на количество результатов.
2. **Формирование сниппетов**: Для каждого результата формирует сниппет, содержащий краткое описание и URL.
3. **Создание сообщения**: Объединяет все сниппеты в одно сообщение и добавляет его в список результатов.

**ASII flowchart**:

```
Начало
    ↓
A (Выполнение запроса к API)
    ↓
B (Формирование сниппетов)
    ↓
C (Создание сообщения)
    ↓
Конец (Возврат списка сообщений)
```

**Примеры**:

Пример 1: Успешный поиск

```python
import requests
def mock_get(*args, **kwargs):
    class MockResponse:
        def __init__(self, json_data):
            self.json_data = json_data
        def json(self):
            return self.json_data
    return MockResponse([{'snippet': 'Snippet 1', 'link': 'Link 1'}, {'snippet': 'Snippet 2', 'link': 'Link 2'}])

requests.get = mock_get
query = 'test query'
results = fetch_search_results(query)
print(results)
```

Пример 2: Пустой результат поиска

```python
import requests
def mock_get(*args, **kwargs):
    class MockResponse:
        def __init__(self, json_data):
            self.json_data = json_data
        def json(self):
            return self.json_data
    return MockResponse([])

requests.get = mock_get
query = 'test query'
results = fetch_search_results(query)
print(results)
```

### `generate_stream(response, jailbreak)`

```python
def generate_stream(response, jailbreak):
    """Генерирует поток данных на основе ответа от API.

    Если включены инструкции jailbreak, проверяет ответ на соответствие критериям успешного или неуспешного jailbreak,
    и возвращает поток данных с учетом этих критериев.
    В противном случае просто возвращает поток данных ответа.

    Args:
        response: Ответ от API.
        jailbreak: Идентификатор или название jailbreak-инструкции.

    Yields:
        str: Часть ответа API.
    """
```

**Как работает функция**:

1. **Проверка наличия инструкций jailbreak**: Проверяет, включены ли инструкции jailbreak.
2. **Обработка ответа с jailbreak**: Если инструкции jailbreak включены, проверяет каждую часть ответа на соответствие критериям успешного или неуспешного jailbreak.
3. **Генерация потока данных**: Возвращает поток данных с учетом результатов проверки на jailbreak.

**ASII flowchart**:

```
Начало
    ↓
A (Проверка наличия инструкций jailbreak)
    ↓
B (Обработка ответа с jailbreak, если включены)
    ↓
C (Генерация потока данных)
    ↓
Конец (Возврат потока данных)
```

**Примеры**:

Пример 1: Без jailbreak

```python
def mock_response():
    yield "GPT: Hello"
    yield " world!"

response = mock_response()
jailbreak = "Default"
stream = generate_stream(response, jailbreak)
print(list(stream))
```

Пример 2: С jailbreak (успешный)

```python
def mock_response():
    yield "ACT: Hello"
    yield " world!"

response = mock_response()
special_instructions = {'Custom': [{'role': 'system', 'content': 'Custom instructions'}]}
jailbreak = "Custom"
stream = generate_stream(response, jailbreak)
print(list(stream))
```

### `response_jailbroken_success(response: str) -> bool`

```python
def response_jailbroken_success(response: str) -> bool:
    """Проверяет, содержит ли ответ признак успешного выполнения jailbreak (наличие "ACT:").

    Args:
        response (str): Ответ от API.

    Returns:
        bool: True, если ответ содержит "ACT:", иначе False.
    """
```

**Как работает функция**:

Функция использует регулярное выражение для поиска подстроки "ACT:" в ответе. Если подстрока найдена, функция возвращает `True`, иначе `False`.

**ASII flowchart**:

```
Начало
    ↓
A (Поиск "ACT:" в ответе)
    ↓
B (Возврат True, если найдено, иначе False)
    ↓
Конец
```

**Примеры**:

Пример 1: Успешный jailbreak

```python
response = "ACT: Hello world!"
success = response_jailbroken_success(response)
print(success)
```

Пример 2: Неуспешный jailbreak

```python
response = "GPT: Hello world!"
success = response_jailbroken_success(response)
print(success)
```

### `response_jailbroken_failed(response)`

```python
def response_jailbroken_failed(response):
    """Проверяет, является ли ответ неудачной попыткой jailbreak.

    Args:
        response: Ответ от API.

    Returns:
        bool: False, если длина ответа менее 4 символов или ответ начинается с "GPT:" или "ACT:", иначе True.
    """
```

**Как работает функция**:

Функция проверяет, является ли ответ неудачной попыткой jailbreak. Она возвращает `False`, если длина ответа менее 4 символов или ответ начинается с "GPT:" или "ACT:", в противном случае возвращает `True`.

**ASII flowchart**:

```
Начало
    ↓
A (Проверка длины ответа)
    ↓
B (Проверка начала ответа на "GPT:" или "ACT:")
    ↓
C (Возврат False, если длина < 4 или начинается с "GPT:"/"ACT:", иначе True)
    ↓
Конец
```

**Примеры**:

Пример 1: Короткий ответ

```python
response = "Hi"
failed = response_jailbroken_failed(response)
print(failed)
```

Пример 2: Ответ GPT

```python
response = "GPT: Hello"
failed = response_jailbroken_failed(response)
print(failed)
```

Пример 3: Ответ ACT

```python
response = "ACT: Hello"
failed = response_jailbroken_failed(response)
print(failed)
```

Пример 4: Неудачная попытка jailbreak

```python
response = "Hello"
failed = response_jailbroken_failed(response)
print(failed)
```

### `set_response_language(prompt)`

```python
def set_response_language(prompt):
    """Определяет язык запроса и возвращает строку с инструкцией для ответа на этом языке.

    Args:
        prompt (dict): Словарь, содержащий текст запроса в ключе 'content'.

    Returns:
        str: Строка с инструкцией для ответа на определенном языке.
    """
```

**Как работает функция**:

1. **Определение языка**: Использует `googletrans.Translator` для определения языка текста запроса.
2. **Формирование инструкции**: Формирует строку с инструкцией для ответа на определенном языке.

**ASII flowchart**:

```
Начало
    ↓
A (Определение языка текста запроса)
    ↓
B (Формирование инструкции для ответа на определенном языке)
    ↓
Конец
```

**Примеры**:

Пример 1: Английский язык

```python
import googletrans
def mock_detect(text):
    class MockDetection:
        def __init__(self, lang):
            self.lang = lang
    return MockDetection('en')

googletrans.Translator.detect = mock_detect
prompt = {'content': 'Hello'}
instruction = set_response_language(prompt)
print(instruction)
```

Пример 2: Русский язык

```python
import googletrans
def mock_detect(text):
    class MockDetection:
        def __init__(self, lang):
            self.lang = lang
    return MockDetection('ru')

googletrans.Translator.detect = mock_detect
prompt = {'content': 'Привет'}
instruction = set_response_language(prompt)
print(instruction)
```

### `isJailbreak(jailbreak)`

```python
def isJailbreak(jailbreak):
    """Проверяет, является ли переданный jailbreak специальной инструкцией.

    Args:
        jailbreak: Идентификатор или название jailbreak-инструкции.

    Returns:
        list | None: Список инструкций, если jailbreak найден в `special_instructions`, иначе None.
    """
```

**Как работает функция**:

Функция проверяет, является ли переданный jailbreak специальной инструкцией. Если jailbreak не является "Default" и присутствует в словаре `special_instructions`, функция возвращает соответствующий список инструкций. В противном случае возвращает `None`.

**ASII flowchart**:

```
Начало
    ↓
A (Проверка jailbreak на "Default")
    ↓
B (Проверка наличия jailbreak в special_instructions)
    ↓
C (Возврат инструкций или None)
    ↓
Конец
```

**Примеры**:

Пример 1: Jailbreak "Default"

```python
jailbreak = "Default"
instructions = isJailbreak(jailbreak)
print(instructions)
```

Пример 2: Jailbreak найден в `special_instructions`

```python
special_instructions = {'Custom': [{'role': 'system', 'content': 'Custom instructions'}]}
jailbreak = "Custom"
instructions = isJailbreak(jailbreak)
print(instructions)
```

Пример 3: Jailbreak не найден в `special_instructions`

```python
special_instructions = {'Custom': [{'role': 'system', 'content': 'Custom instructions'}]}
jailbreak = "NonExistent"
instructions = isJailbreak(jailbreak)
print(instructions)