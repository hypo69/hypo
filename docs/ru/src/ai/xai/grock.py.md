# Модуль для работы с API x.ai (Grok)

## Обзор

Модуль `grock.py` предоставляет класс `XAI` для взаимодействия с API x.ai, в частности, для получения ответов от чат-бота Grok. Он включает в себя методы для отправки запросов на завершение чата как в потоковом, так и в непотоковом режимах.

## Подробнее

Этот модуль позволяет интегрировать функциональность чат-бота Grok в ваши приложения, предоставляя удобный интерфейс для отправки сообщений и получения ответов. Класс `XAI` инкапсулирует детали аутентификации и отправки запросов к API x.ai.

## Классы

### `XAI`

**Описание**: Класс для взаимодействия с API x.ai.

**Принцип работы**:
1.  При инициализации класса `XAI` требуется передать ключ API, который используется для аутентификации при каждом запросе к API x.ai.
2.  Класс предоставляет методы `chat_completion` и `stream_chat_completion` для отправки запросов на завершение чата в непотоковом и потоковом режимах соответственно.
3.  Метод `_send_request` используется для отправки HTTP-запросов к API x.ai.

**Атрибуты**:

*   `api_key` (str): Ключ API для аутентификации.
*   `base_url` (str): Базовый URL API x.ai.
*   `headers` (dict): Заголовки HTTP-запроса, включающие ключ API и тип контента.

**Методы**:

*   `__init__(self, api_key)`: Инициализация класса `XAI`.
*   `_send_request(self, method, endpoint, data=None)`: Отправка запроса к API x.ai.
*   `chat_completion(self, messages, model="grok-beta", stream=False, temperature=0)`: Запрос на завершение чата.
*   `stream_chat_completion(self, messages, model="grok-beta", temperature=0)`: Запрос на завершение чата с потоковой передачей.

## Функции

### `__init__`

```python
def __init__(self, api_key):
    """
    Инициализация класса XAI.

    :param api_key: Ключ API для аутентификации.
    """
```

**Назначение**: Инициализация экземпляра класса `XAI` с заданным ключом API.

**Параметры**:

*   `api_key` (str): Ключ API для аутентификации.

**Как работает функция**:

1.  Сохраняет переданный `api_key` в атрибуте `self.api_key`.
2.  Устанавливает базовый URL API x.ai в атрибуте `self.base_url`.
3.  Создает словарь `self.headers`, содержащий заголовок `Authorization` с ключом API и заголовок `Content-Type` для JSON.

**Примеры**:

```python
api_key = "your_api_key_here"
xai = XAI(api_key)
```

### `_send_request`

```python
def _send_request(self, method, endpoint, data=None):
    """
    Отправка запроса к API x.ai.

    :param method: Метод HTTP (GET, POST, PUT, DELETE).
    :param endpoint: Конечная точка API.
    :param data: Данные для отправки в теле запроса (для POST и PUT).
    :return: Ответ от API.
    """
```

**Назначение**: Отправка HTTP-запроса к API x.ai с заданными параметрами.

**Параметры**:

*   `method` (str): Метод HTTP (GET, POST, PUT, DELETE).
*   `endpoint` (str): Конечная точка API.
*   `data` (Optional[dict]): Данные для отправки в теле запроса (для POST и PUT). По умолчанию `None`.

**Возвращает**:

*   `dict`: Ответ от API в формате JSON.

**Вызывает исключения**:

*   `requests.exceptions.HTTPError`: Если статус ответа не 2xx.

**Как работает функция**:

1.  Формирует URL-адрес запроса, объединяя `self.base_url` и `endpoint`.
2.  Выполняет HTTP-запрос с использованием библиотеки `requests`.
3.  Проверяет статус ответа и вызывает исключение `HTTPError`, если статус не 2xx.
4.  Возвращает JSON-ответ от API.

```
A: Формирование URL запроса
|
B: Отправка HTTP запроса (requests.request)
|
C: Проверка статуса ответа
|
D: Возврат JSON ответа
```

**Примеры**:

```python
api_key = "your_api_key_here"
xai = XAI(api_key)
messages = [
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "Hello!"}
]
response = xai._send_request("POST", "chat/completions", data={"messages": messages})
print(response)
```

### `chat_completion`

```python
def chat_completion(self, messages, model="grok-beta", stream=False, temperature=0):
    """
    Запрос на завершение чата.

    :param messages: Список сообщений для чата.
    :param model: Модель для использования.
    :param stream: Флаг для включения потоковой передачи.
    :param temperature: Температура для генерации ответа.
    :return: Ответ от API.
    """
```

**Назначение**: Отправка запроса на завершение чата к API x.ai.

**Параметры**:

*   `messages` (list): Список сообщений для чата.
*   `model` (str): Модель для использования. По умолчанию `"grok-beta"`.
*   `stream` (bool): Флаг для включения потоковой передачи. По умолчанию `False`.
*   `temperature` (int): Температура для генерации ответа. По умолчанию `0`.

**Возвращает**:

*   `dict`: Ответ от API.

**Как работает функция**:

1.  Устанавливает конечную точку API как `"chat/completions"`.
2.  Формирует данные запроса, включающие сообщения, модель, флаг потоковой передачи и температуру.
3.  Вызывает метод `_send_request` для отправки POST-запроса к API.
4.  Возвращает ответ от API.

```
A: Установка endpoint
|
B: Формирование данных запроса
|
C: Вызов метода _send_request
|
D: Возврат ответа API
```

**Примеры**:

```python
api_key = "your_api_key_here"
xai = XAI(api_key)
messages = [
    {"role": "system", "content": "You are Grok."},
    {"role": "user", "content": "What is the meaning of life?"}
]
completion_response = xai.chat_completion(messages)
print(completion_response)
```

### `stream_chat_completion`

```python
def stream_chat_completion(self, messages, model="grok-beta", temperature=0):
    """
    Запрос на завершение чата с потоковой передачей.

    :param messages: Список сообщений для чата.
    :param model: Модель для использования.
    :param temperature: Температура для генерации ответа.
    :return: Поток ответов от API.
    """
```

**Назначение**: Отправка запроса на завершение чата с потоковой передачей к API x.ai.

**Параметры**:

*   `messages` (list): Список сообщений для чата.
*   `model` (str): Модель для использования. По умолчанию `"grok-beta"`.
*   `temperature` (int): Температура для генерации ответа. По умолчанию `0`.

**Возвращает**:

*   `Generator[str, None, None]`: Поток ответов от API.

**Как работает функция**:

1.  Устанавливает конечную точку API как `"chat/completions"`.
2.  Формирует данные запроса, включающие сообщения, модель, флаг потоковой передачи (установлен в `True`) и температуру.
3.  Формирует URL-адрес запроса, объединяя `self.base_url` и `endpoint`.
4.  Отправляет POST-запрос с использованием библиотеки `requests` и параметром `stream=True`.
5.  Проверяет статус ответа и вызывает исключение, если статус не 2xx.
6.  Возвращает итератор по строкам ответа, декодированным в Unicode.

```
A: Установка endpoint
|
B: Формирование данных запроса (stream=True)
|
C: Формирование URL запроса
|
D: Отправка POST запроса (requests.post, stream=True)
|
E: Проверка статуса ответа
|
F: Возврат потока ответов
```

**Примеры**:

```python
api_key = "your_api_key_here"
xai = XAI(api_key)
messages = [
    {"role": "system", "content": "You are Grok."},
    {"role": "user", "content": "Tell me a joke."}
]
stream_response = xai.stream_chat_completion(messages)
for line in stream_response:
    if line.strip():
        print(json.loads(line))