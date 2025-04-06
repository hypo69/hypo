# Модуль AIUncensored

## Обзор

Модуль предоставляет асинхронный интерфейс для взаимодействия с AIUncensored, сервисом, предоставляющим доступ к различным моделям LLM. Он включает в себя функции для формирования запросов, вычисления подписи безопасности и обработки потоковых ответов.

## Подробней

Модуль предназначен для интеграции с AIUncensored, позволяя пользователям получать ответы от LLM в асинхронном режиме. Он поддерживает потоковую передачу данных и может использоваться с прокси-серверами. Для обеспечения безопасности запросов используется механизм подписи на основе HMAC.

## Классы

### `AIUncensored`

**Описание**: Класс `AIUncensored` реализует асинхронного провайдера, который взаимодействует с сервисом AIUncensored. Он наследует функциональность от `AsyncGeneratorProvider` и `ProviderModelMixin`, предоставляя методы для создания асинхронных генераторов и управления моделями.

**Наследует**:

-   `AsyncGeneratorProvider`: Обеспечивает базовую функциональность для асинхронных генераторов.
-   `ProviderModelMixin`: Предоставляет методы для работы с моделями провайдера.

**Атрибуты**:

-   `url` (str): URL-адрес сервиса AIUncensored.
-   `api_key` (str): Ключ API для аутентификации на сервисе AIUncensored.
-   `working` (bool): Флаг, указывающий на работоспособность провайдера.
-   `supports_stream` (bool): Флаг, указывающий на поддержку потоковой передачи данных.
-   `supports_system_message` (bool): Флаг, указывающий на поддержку системных сообщений.
-   `supports_message_history` (bool): Флаг, указывающий на поддержку истории сообщений.
-   `default_model` (str): Модель, используемая по умолчанию.
-   `models` (list[str]): Список поддерживаемых моделей.
-   `model_aliases` (dict[str, str]): Словарь псевдонимов моделей.

**Методы**:

-   `calculate_signature(timestamp: str, json_dict: dict) -> str`: Вычисляет подпись безопасности для запроса.
-   `get_server_url() -> str`: Возвращает случайный URL-адрес сервера из списка доступных.
-   `create_async_generator(model: str, messages: Messages, stream: bool = False, proxy: str = None, api_key: str = None, **kwargs) -> AsyncResult`: Создает асинхронный генератор для взаимодействия с AIUncensored.

## Функции

### `calculate_signature`

```python
@staticmethod
def calculate_signature(timestamp: str, json_dict: dict) -> str:
    """Вычисляет подпись безопасности для запроса.

    Args:
        timestamp (str): Временная метка запроса.
        json_dict (dict): Словарь с данными запроса в формате JSON.

    Returns:
        str: Подпись безопасности.

    Как работает функция:
    1. Формирует сообщение, объединяя временную метку и JSON-представление данных запроса.
    2. Использует секретный ключ для вычисления HMAC-SHA256 подписи сообщения.
    3. Возвращает вычисленную подпись в шестнадцатеричном формате.

    ASCII flowchart:
    A [timestamp, json_dict]
    |
    B [message = timestamp + json.dumps(json_dict)]
    |
    C [signature = hmac.new(secret_key, message.encode('utf-8'), hashlib.sha256).hexdigest()]
    |
    D [return signature]
    """
    ...
```

**Назначение**: Вычисление подписи безопасности для запроса к AIUncensored.

**Параметры**:

-   `timestamp` (str): Временная метка запроса.
-   `json_dict` (dict): Словарь с данными запроса в формате JSON.

**Возвращает**:

-   `str`: Подпись безопасности.

**Как работает функция**:

1.  **Формирование сообщения**: Объединяет временную метку и JSON-представление данных запроса.
2.  **Вычисление подписи**: Использует секретный ключ для вычисления HMAC-SHA256 подписи сообщения.
3.  **Возврат подписи**: Возвращает вычисленную подпись в шестнадцатеричном формате.

**ASCII flowchart**:

```
A [Вход: timestamp, json_dict]
|
B [message = timestamp + json.dumps(json_dict)]
|
C [signature = hmac.new(secret_key, message.encode('utf-8'), hashlib.sha256).hexdigest()]
|
D [Выход: signature]
```

**Примеры**:

```python
timestamp = "1678886400"
json_dict = {"messages": [{"role": "user", "content": "Hello"}]}
signature = AIUncensored.calculate_signature(timestamp, json_dict)
print(signature)
```

### `get_server_url`

```python
@staticmethod
def get_server_url() -> str:
    """Возвращает случайный URL-адрес сервера из списка доступных.

    Returns:
        str: URL-адрес сервера.

    Как работает функция:
    1. Определяет список доступных серверов.
    2. Случайным образом выбирает один из серверов.
    3. Возвращает URL-адрес выбранного сервера.

    ASCII flowchart:
    A [servers = [...]]
    |
    B [server_url = random.choice(servers)]
    |
    C [return server_url]
    """
    ...
```

**Назначение**: Возвращает случайный URL-адрес сервера из списка доступных.

**Возвращает**:

-   `str`: URL-адрес сервера.

**Как работает функция**:

1.  **Определение серверов**: Определяет список доступных серверов.
2.  **Выбор сервера**: Случайным образом выбирает один из серверов.
3.  **Возврат URL**: Возвращает URL-адрес выбранного сервера.

**ASCII flowchart**:

```
A [servers = [...]]
|
B [server_url = random.choice(servers)]
|
C [Выход: server_url]
```

**Примеры**:

```python
server_url = AIUncensored.get_server_url()
print(server_url)
```

### `create_async_generator`

```python
@classmethod
async def create_async_generator(
    cls,
    model: str,
    messages: Messages,
    stream: bool = False,
    proxy: str = None,
    api_key: str = None,
    **kwargs
) -> AsyncResult:
    """Создает асинхронный генератор для взаимодействия с AIUncensored.

    Args:
        model (str): Модель для использования.
        messages (Messages): Список сообщений для отправки.
        stream (bool, optional): Флаг, указывающий на использование потоковой передачи данных. По умолчанию False.
        proxy (str, optional): URL-адрес прокси-сервера. По умолчанию None.
        api_key (str, optional): Ключ API. По умолчанию None.
        **kwargs: Дополнительные параметры.

    Returns:
        AsyncResult: Асинхронный генератор.

    Raises:
        Exception: В случае ошибки при выполнении запроса.

    Как работает функция:
    1. Получает модель для использования.
    2. Формирует временную метку.
    3. Создает словарь с данными запроса в формате JSON.
    4. Вычисляет подпись безопасности.
    5. Формирует заголовки запроса.
    6. Отправляет POST-запрос к AIUncensored.
    7. Обрабатывает потоковые и не потоковые ответы.

    ASCII flowchart:
    A [Вход: model, messages, stream, proxy, api_key, kwargs]
    |
    B [model = cls.get_model(model)]
    |
    C [timestamp = str(int(time.time()))]
    |
    D [json_dict = {"messages": ..., "model": model, "stream": stream}]
    |
    E [signature = cls.calculate_signature(timestamp, json_dict)]
    |
    F [headers = {...}]
    |
    G [url = f"{cls.get_server_url()}/api/chat"]
    |
    H [async with ClientSession(headers=headers) as session:
        async with session.post(url, json=json_dict, proxy=proxy) as response:]
    |
    I [Обработка потокового ответа (stream=True) или не потокового ответа (stream=False)]
    |
    J [Выход: AsyncResult]
    """
    ...
```

**Назначение**: Создает асинхронный генератор для взаимодействия с AIUncensored.

**Параметры**:

-   `model` (str): Модель для использования.
-   `messages` (Messages): Список сообщений для отправки.
-   `stream` (bool, optional): Флаг, указывающий на использование потоковой передачи данных. По умолчанию `False`.
-   `proxy` (str, optional): URL-адрес прокси-сервера. По умолчанию `None`.
-   `api_key` (str, optional): Ключ API. По умолчанию `None`.
-   `**kwargs`: Дополнительные параметры.

**Возвращает**:

-   `AsyncResult`: Асинхронный генератор.

**Вызывает исключения**:

-   `Exception`: В случае ошибки при выполнении запроса.

**Как работает функция**:

1.  **Получение модели**: Получает модель для использования.
2.  **Формирование временной метки**: Формирует временную метку.
3.  **Создание словаря**: Создает словарь с данными запроса в формате JSON.
4.  **Вычисление подписи**: Вычисляет подпись безопасности.
5.  **Формирование заголовков**: Формирует заголовки запроса.
6.  **Отправка запроса**: Отправляет POST-запрос к AIUncensored.
7.  **Обработка ответа**: Обрабатывает потоковые и не потоковые ответы.

**ASCII flowchart**:

```
A [Вход: model, messages, stream, proxy, api_key, kwargs]
|
B [model = cls.get_model(model)]
|
C [timestamp = str(int(time.time()))]
|
D [json_dict = {"messages": ..., "model": model, "stream": stream}]
|
E [signature = cls.calculate_signature(timestamp, json_dict)]
|
F [headers = {...}]
|
G [url = f"{cls.get_server_url()}/api/chat"]
|
H [async with ClientSession(headers=headers) as session:
    async with session.post(url, json=json_dict, proxy=proxy) as response:]
|
I [Обработка потокового ответа (stream=True) или не потокового ответа (stream=False)]
|
J [Выход: AsyncResult]
```

**Примеры**:

```python
async def main():
    model = "hermes3-70b"
    messages = [{"role": "user", "content": "Hello"}]
    async for message in AIUncensored.create_async_generator(model, messages, stream=True):
        print(message)

import asyncio
asyncio.run(main())