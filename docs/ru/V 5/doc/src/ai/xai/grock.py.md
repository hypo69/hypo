# Модуль для взаимодействия с API XAI (Grok)

## Обзор

Модуль `grock.py` предоставляет класс `XAI`, предназначенный для взаимодействия с API XAI (Grok). Он включает в себя функциональность для отправки запросов на завершение чата как в обычном, так и в потоковом режимах. Модуль обеспечивает аутентификацию через API-ключ и обрабатывает ответы от API.

## Подробней

Этот модуль упрощает интеграцию с API XAI, предоставляя удобный интерфейс для отправки запросов и получения ответов. Он позволяет использовать различные модели, управлять параметрами запросов, такими как температура, и обрабатывать ответы в реальном времени через потоковую передачу. `XAI` используется для получения ответов от модели Grok на основе предоставленных сообщений.

## Классы

### `XAI`

**Описание**: Класс для взаимодействия с API XAI.

**Как работает класс**:
Класс инициализируется с использованием API-ключа, который используется для аутентификации при каждом запросе к API. Он определяет базовый URL API и заголовки, необходимые для взаимодействия. Методы класса позволяют отправлять запросы на завершение чата и обрабатывать ответы, включая потоковую передачу.

**Методы**:
- `__init__`: Инициализация экземпляра класса `XAI`.
- `_send_request`: Отправка HTTP-запроса к API XAI.
- `chat_completion`: Запрос на завершение чата без потоковой передачи.
- `stream_chat_completion`: Запрос на завершение чата с потоковой передачей.

**Примеры**:
```python
api_key = "your_api_key_here"  # Замените на ваш реальный API-ключ
xai = XAI(api_key)

messages = [
    {
        "role": "system",
        "content": "You are Grok, a chatbot inspired by the Hitchhikers Guide to the Galaxy."
    },
    {
        "role": "user",
        "content": "What is the answer to life and universe?"
    }
]

# Непотоковый запрос
completion_response = xai.chat_completion(messages)
print("Non-streaming response:", completion_response)

# Потоковый запрос
stream_response = xai.stream_chat_completion(messages)
print("Streaming response:")
for line in stream_response:
    if line.strip():
        print(json.loads(line))
```

### `__init__`

```python
def __init__(self, api_key):
    """
    Инициализация класса XAI.

    :param api_key: Ключ API для аутентификации.
    """
```

**Описание**: Инициализирует экземпляр класса `XAI` с использованием API-ключа.

**Как работает функция**:
Функция инициализирует экземпляр класса `XAI`, устанавливая API-ключ, базовый URL и заголовки для будущих запросов. Ключ API используется для аутентификации при каждом запросе.

**Параметры**:
- `api_key` (str): Ключ API для аутентификации.

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

**Описание**: Отправляет HTTP-запрос к API XAI.

**Как работает функция**:
Функция принимает метод HTTP, конечную точку API и данные (если необходимо) и отправляет запрос к API XAI. Она обрабатывает ответ, проверяя статус код и возвращая JSON-ответ.

**Параметры**:
- `method` (str): Метод HTTP (GET, POST, PUT, DELETE).
- `endpoint` (str): Конечная точка API.
- `data` (Optional[dict], optional): Данные для отправки в теле запроса (для POST и PUT). По умолчанию `None`.

**Возвращает**:
- `dict`: Ответ от API в формате JSON.

**Вызывает исключения**:
- `requests.exceptions.HTTPError`: Если статус ответа не 2xx.

**Примеры**:
```python
api_key = "your_api_key_here"
xai = XAI(api_key)
endpoint = "chat/completions"
data = {"messages": [{"role": "user", "content": "Hello"}]}
response = xai._send_request("POST", endpoint, data)
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

**Описание**: Отправляет запрос на завершение чата.

**Как работает функция**:
Функция принимает список сообщений, модель, флаг потоковой передачи и температуру и отправляет запрос на завершение чата к API XAI. Она возвращает ответ от API в формате JSON.

**Параметры**:
- `messages` (list[dict]): Список сообщений для чата.
- `model` (str, optional): Модель для использования. По умолчанию `"grok-beta"`.
- `stream` (bool, optional): Флаг для включения потоковой передачи. По умолчанию `False`.
- `temperature` (int, optional): Температура для генерации ответа. По умолчанию `0`.

**Возвращает**:
- `dict`: Ответ от API в формате JSON.

**Примеры**:
```python
api_key = "your_api_key_here"
xai = XAI(api_key)
messages = [{"role": "user", "content": "Hello"}]
response = xai.chat_completion(messages)
print(response)
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

**Описание**: Отправляет запрос на завершение чата с потоковой передачей.

**Как работает функция**:
Функция принимает список сообщений, модель и температуру и отправляет запрос на завершение чата с потоковой передачей к API XAI. Она возвращает поток ответов от API, который можно итерировать для получения каждого сообщения.

**Параметры**:
- `messages` (list[dict]): Список сообщений для чата.
- `model` (str, optional): Модель для использования. По умолчанию `"grok-beta"`.
- `temperature` (int, optional): Температура для генерации ответа. По умолчанию `0`.

**Возвращает**:
- `Generator[str, None, None]`: Поток ответов от API.

**Примеры**:
```python
api_key = "your_api_key_here"
xai = XAI(api_key)
messages = [{"role": "user", "content": "Hello"}]
stream_response = xai.stream_chat_completion(messages)
for line in stream_response:
    if line.strip():
        print(json.loads(line))
```