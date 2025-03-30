# Модуль для работы с XAI Grok

## Обзор

Модуль предоставляет класс `XAI` для взаимодействия с API x.ai, в частности, для выполнения запросов на завершение чата с использованием модели Grok. Он включает в себя функциональность для отправки запросов как в непотоковом, так и в потоковом режимах.

## Подробней

Этот модуль предназначен для упрощения работы с API x.ai. Класс `XAI` инкапсулирует логику аутентификации и отправки запросов, предоставляя удобные методы для запроса завершения чата. Модуль использует библиотеку `requests` для отправки HTTP-запросов и библиотеку `json` для обработки данных в формате JSON.

## Классы

### `XAI`

**Описание**: Класс для взаимодействия с API x.ai.

**Методы**:
- `__init__`: Инициализация класса XAI.
- `_send_request`: Отправка запроса к API x.ai.
- `chat_completion`: Запрос на завершение чата.
- `stream_chat_completion`: Запрос на завершение чата с потоковой передачей.

**Параметры**:
- `api_key` (str): Ключ API для аутентификации.

**Примеры**
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

## Функции

### `__init__`

```python
def __init__(self, api_key: str):
    """
    Args:
        api_key (str): Ключ API для аутентификации.
    """
```

**Описание**: Инициализирует экземпляр класса `XAI` с использованием предоставленного ключа API.

**Параметры**:
- `api_key` (str): Ключ API для аутентификации.

**Примеры**:
```python
api_key = "your_api_key"
xai = XAI(api_key)
```

### `_send_request`

```python
def _send_request(self, method: str, endpoint: str, data: Optional[dict] = None) -> dict:
    """
    Args:
        method (str): Метод HTTP (GET, POST, PUT, DELETE).
        endpoint (str): Конечная точка API.
        data (Optional[dict], optional): Данные для отправки в теле запроса (для POST и PUT). По умолчанию `None`.

    Returns:
        dict: Ответ от API.

    Raises:
        requests.exceptions.HTTPError: Если статус ответа не 2xx.
    """
```

**Описание**: Отправляет HTTP-запрос к API x.ai.

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
api_key = "your_api_key"
xai = XAI(api_key)
endpoint = "chat/completions"
data = {"messages": [{"role": "user", "content": "Hello"}]}
response = xai._send_request("POST", endpoint, data)
print(response)
```

### `chat_completion`

```python
def chat_completion(self, messages: list[dict], model: str = "grok-beta", stream: bool = False, temperature: int = 0) -> dict:
    """
    Args:
        messages (list[dict]): Список сообщений для чата.
        model (str, optional): Модель для использования. По умолчанию "grok-beta".
        stream (bool, optional): Флаг для включения потоковой передачи. По умолчанию `False`.
        temperature (int, optional): Температура для генерации ответа. По умолчанию 0.

    Returns:
        dict: Ответ от API.
    """
```

**Описание**: Отправляет запрос на завершение чата.

**Параметры**:
- `messages` (list[dict]): Список сообщений для чата.
- `model` (str, optional): Модель для использования. По умолчанию "grok-beta".
- `stream` (bool, optional): Флаг для включения потоковой передачи. По умолчанию `False`.
- `temperature` (int, optional): Температура для генерации ответа. По умолчанию 0.

**Возвращает**:
- `dict`: Ответ от API.

**Примеры**:
```python
api_key = "your_api_key"
xai = XAI(api_key)
messages = [{"role": "user", "content": "Hello"}]
response = xai.chat_completion(messages)
print(response)
```

### `stream_chat_completion`

```python
def stream_chat_completion(self, messages: list[dict], model: str = "grok-beta", temperature: int = 0) -> Generator[str, None, None]:
    """
    Args:
        messages (list[dict]): Список сообщений для чата.
        model (str, optional): Модель для использования. По умолчанию "grok-beta".
        temperature (int, optional): Температура для генерации ответа. По умолчанию 0.

    Returns:
        Generator[str, None, None]: Поток ответов от API.
    """
```

**Описание**: Отправляет запрос на завершение чата с потоковой передачей.

**Параметры**:
- `messages` (list[dict]): Список сообщений для чата.
- `model` (str, optional): Модель для использования. По умолчанию "grok-beta".
- `temperature` (int, optional): Температура для генерации ответа. По умолчанию 0.

**Возвращает**:
- `Generator[str, None, None]`: Поток ответов от API.

**Примеры**:
```python
api_key = "your_api_key"
xai = XAI(api_key)
messages = [{"role": "user", "content": "Hello"}]
response = xai.stream_chat_completion(messages)
for line in response:
    if line.strip():
        print(json.loads(line))