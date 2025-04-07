# Модуль для взаимодействия с API x.ai (Grok)

## Обзор

Модуль предоставляет класс `XAI` для взаимодействия с API x.ai, включая отправку запросов на завершение чата (chat completion) в потоковом и непотоковом режимах. Он предназначен для интеграции с сервисами, использующими API x.ai, например, для создания чат-ботов.

## Подробней

Модуль содержит класс `XAI`, который инкапсулирует логику взаимодействия с API x.ai. Класс инициализируется с использованием API-ключа, который используется для аутентификации при отправке запросов. Класс предоставляет методы для отправки запросов на завершение чата и потокового завершения чата. Класс использует библиотеку `requests` для отправки HTTP-запросов.

## Классы

### `XAI`

**Описание**: Класс для взаимодействия с API x.ai.

**Принцип работы**:
Класс инициализируется с использованием API-ключа, который используется для аутентификации при отправке запросов. Класс предоставляет методы для отправки запросов на завершение чата и потокового завершения чата. Класс использует библиотеку `requests` для отправки HTTP-запросов.

**Аттрибуты**:
- `api_key` (str): Ключ API для аутентификации.
- `base_url` (str): Базовый URL API ("https://api.x.ai/v1").
- `headers` (dict): Заголовки HTTP-запроса, включающие ключ API и тип контента.

**Методы**:
- `__init__(self, api_key)`: Инициализация класса `XAI`.
- `_send_request(self, method, endpoint, data=None)`: Отправка запроса к API x.ai.
- `chat_completion(self, messages, model="grok-beta", stream=False, temperature=0)`: Запрос на завершение чата.
- `stream_chat_completion(self, messages, model="grok-beta", temperature=0)`: Запрос на завершение чата с потоковой передачей.

### `__init__`

```python
def __init__(self, api_key):
    """
    Инициализация класса XAI.

    :param api_key: Ключ API для аутентификации.
    """
```

**Назначение**: Инициализация экземпляра класса `XAI`.

**Параметры**:
- `api_key` (str): Ключ API, используемый для аутентификации при запросах к API x.ai.

**Как работает функция**:
1. Присваивает переданный `api_key` атрибуту `self.api_key`.
2. Устанавливает базовый URL API x.ai в атрибуте `self.base_url`.
3. Определяет заголовки `self.headers` для HTTP-запросов, включая заголовок авторизации с использованием API-ключа и заголовок `Content-Type` для указания типа контента как JSON.

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

**Назначение**: Отправляет HTTP-запрос к API x.ai.

**Параметры**:
- `method` (str): HTTP-метод запроса (GET, POST, PUT, DELETE).
- `endpoint` (str): Конечная точка API.
- `data` (Optional[dict]): Данные для отправки в теле запроса (для POST и PUT). По умолчанию `None`.

**Возвращает**:
- `dict`: JSON-ответ от API.

**Вызывает исключения**:
- `requests.exceptions.HTTPError`: Если статус ответа не 2xx.

**Как работает функция**:

     Создание URL запроса
     │
     → Отправка запроса к API x.ai с использованием библиотеки requests
     │
     Обработка ответа: проверка статуса, преобразование в JSON
     │
     Возврат JSON-ответа

1. Формирует URL-адрес запроса, объединяя базовый URL (`self.base_url`) и указанную конечную точку (`endpoint`).
2. Отправляет HTTP-запрос с использованием библиотеки `requests`. Параметры запроса включают метод (`method`), URL, заголовки (`self.headers`) и данные (`data`).
3. Проверяет статус ответа. Если статус не 2xx (успешный), вызывает исключение `HTTPError`.
4. Преобразует JSON-ответ от API и возвращает его.

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

**Назначение**: Отправляет запрос на завершение чата к API x.ai.

**Параметры**:
- `messages` (list): Список сообщений для чата.
- `model` (str): Модель для использования. По умолчанию `"grok-beta"`.
- `stream` (bool): Флаг для включения потоковой передачи. По умолчанию `False`.
- `temperature` (int): Температура для генерации ответа. По умолчанию `0`.

**Возвращает**:
- `dict`: Ответ от API.

**Как работает функция**:

     Формирование данных запроса (messages, model, stream, temperature)
     │
     →  Определение конечной точки API
     │
     Отправка POST-запроса к API
     │
     Возврат ответа от API

1. Определяет конечную точку API как `"chat/completions"`.
2. Формирует данные запроса, включающие список сообщений (`messages`), модель (`model`), флаг потоковой передачи (`stream`) и температуру (`temperature`).
3. Отправляет POST-запрос к API с использованием метода `_send_request` и возвращает ответ.

**Примеры**:

```python
api_key = "your_api_key_here"
xai = XAI(api_key)
messages = [{"role": "user", "content": "What is the meaning of life?"}]
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

**Назначение**: Отправляет запрос на завершение чата с потоковой передачей к API x.ai.

**Параметры**:
- `messages` (list): Список сообщений для чата.
- `model` (str): Модель для использования. По умолчанию `"grok-beta"`.
- `temperature` (int): Температура для генерации ответа. По умолчанию `0`.

**Возвращает**:
- `Generator[str, None, None]`: Поток ответов от API.

**Как работает функция**:

     Формирование данных запроса (messages, model, stream=True, temperature)
     │
     →  Определение конечной точки API
     │
     Отправка POST-запроса к API с включенной потоковой передачей
     │
     Возврат потока ответов от API

1. Определяет конечную точку API как `"chat/completions"`.
2. Формирует данные запроса, включающие список сообщений (`messages`), модель (`model`), флаг потоковой передачи (`stream=True`) и температуру (`temperature`).
3. Отправляет POST-запрос к API с использованием библиотеки `requests` и параметром `stream=True` для включения потоковой передачи.
4. Возвращает итератор по строкам ответа, декодированным в Unicode.

**Примеры**:

```python
api_key = "your_api_key_here"
xai = XAI(api_key)
messages = [{"role": "user", "content": "Tell me a story."}]
stream_response = xai.stream_chat_completion(messages)
for line in stream_response:
    if line.strip():
        print(json.loads(line))
```