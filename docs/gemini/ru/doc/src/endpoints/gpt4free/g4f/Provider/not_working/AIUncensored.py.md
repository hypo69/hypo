# Модуль AIUncensored

## Обзор

Модуль `AIUncensored` предоставляет асинхронный интерфейс для взаимодействия с сервисом AIUncensored.info. Он позволяет отправлять запросы к моделям AI и получать ответы в режиме потока или полной выдачи. Модуль поддерживает настройку прокси и передачу истории сообщений.

## Подробнее

Этот модуль является частью проекта `hypotez` и предназначен для интеграции с различными AI-моделями через асинхронные запросы. Он использует `aiohttp` для выполнения HTTP-запросов и предоставляет методы для форматирования запросов и обработки ответов, включая потоковую передачу данных.

## Классы

### `AIUncensored`

**Описание**: Класс `AIUncensored` предоставляет асинхронный интерфейс для взаимодействия с моделями AIUncensored.

**Принцип работы**: Класс отправляет запросы к серверам AIUncensored, используя асинхронные HTTP-запросы через библиотеку `aiohttp`. Он поддерживает потоковую передачу ответов и полную выдачу. Поддерживается передача истории сообщений и настройка прокси.

**Наследует**:

- `AsyncGeneratorProvider`: Обеспечивает асинхронную генерацию ответов.
- `ProviderModelMixin`: Предоставляет функциональность для работы с моделями.

**Атрибуты**:
- `url` (str): URL-адрес сервиса AIUncensored.
- `api_key` (str): Ключ API для доступа к сервису.
- `working` (bool): Указывает, работает ли провайдер.
- `supports_stream` (bool): Указывает, поддерживает ли провайдер потоковую передачу.
- `supports_system_message` (bool): Указывает, поддерживает ли провайдер системные сообщения.
- `supports_message_history` (bool): Указывает, поддерживает ли провайдер историю сообщений.
- `default_model` (str): Модель, используемая по умолчанию.
- `models` (List[str]): Список поддерживаемых моделей.
- `model_aliases` (dict): Псевдонимы моделей.

**Методы**:
- `calculate_signature(timestamp: str, json_dict: dict) -> str`: Вычисляет подпись запроса.
- `get_server_url() -> str`: Возвращает случайный URL-адрес сервера из списка доступных.
- `create_async_generator(model: str, messages: Messages, stream: bool = False, proxy: str = None, api_key: str = None, **kwargs) -> AsyncResult`: Создает асинхронный генератор для получения ответов от модели.

## Функции

### `calculate_signature`

```python
    @staticmethod
    def calculate_signature(timestamp: str, json_dict: dict) -> str:
        """
        Вычисляет подпись запроса на основе временной метки и JSON-словаря.

        Args:
            timestamp (str): Временная метка запроса.
            json_dict (dict): JSON-словарь с данными запроса.

        Returns:
            str: Вычисленная подпись запроса.
        """
```

**Назначение**: Вычисляет подпись запроса для обеспечения безопасности.

**Параметры**:
- `timestamp` (str): Временная метка запроса.
- `json_dict` (dict): JSON-словарь, содержащий данные запроса.

**Возвращает**:
- `str`: Вычисленная подпись запроса в виде шестнадцатеричной строки.

**Как работает функция**:

1. Формируется сообщение путем объединения временной метки и JSON-представления данных запроса.
2. Используется секретный ключ для создания HMAC-подписи с использованием алгоритма SHA256.
3. Возвращается вычисленная подпись в виде шестнадцатеричной строки.

```
    timestamp + json_dict
     |
     V
    message.encode('utf-8')
     |
     V
    hmac.new(secret_key, message, hashlib.sha256).hexdigest()
     |
     V
    signature
```

**Примеры**:

```python
timestamp = "1678886400"
json_data = {"messages": [{"role": "user", "content": "Hello"}]}
signature = AIUncensored.calculate_signature(timestamp, json_data)
print(signature)
```

### `get_server_url`

```python
    @staticmethod
    def get_server_url() -> str:
        """
        Возвращает случайный URL-адрес сервера из списка доступных серверов.

        Returns:
            str: URL-адрес выбранного сервера.
        """
```

**Назначение**: Возвращает случайный URL-адрес сервера для балансировки нагрузки.

**Возвращает**:
- `str`: URL-адрес выбранного сервера.

**Как работает функция**:

1. Определяется список доступных URL-адресов серверов.
2. Случайно выбирается один из URL-адресов.
3. Возвращается выбранный URL-адрес.

```
    servers
     |
     V
    random.choice(servers)
     |
     V
    server_url
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
        """
        Создает асинхронный генератор для получения ответов от модели AIUncensored.

        Args:
            model (str): Имя используемой модели.
            messages (Messages): Список сообщений для отправки.
            stream (bool, optional): Флаг, указывающий на использование потоковой передачи. По умолчанию `False`.
            proxy (str, optional): URL-адрес прокси-сервера. По умолчанию `None`.
            api_key (str, optional): API-ключ для аутентификации. По умолчанию `None`.
            **kwargs: Дополнительные аргументы.

        Returns:
            AsyncResult: Асинхронный генератор, возвращающий ответы от модели.
        """
```

**Назначение**: Создает асинхронный генератор для получения ответов от AIUncensored.

**Параметры**:
- `model` (str): Имя используемой модели.
- `messages` (Messages): Список сообщений для отправки.
- `stream` (bool, optional): Флаг, указывающий на использование потоковой передачи. По умолчанию `False`.
- `proxy` (str, optional): URL-адрес прокси-сервера. По умолчанию `None`.
- `api_key` (str, optional): API-ключ для аутентификации. По умолчанию `None`.
- `**kwargs`: Дополнительные аргументы.

**Возвращает**:
- `AsyncResult`: Асинхронный генератор, возвращающий ответы от модели.

**Как работает функция**:

1. Получает имя модели, используя `cls.get_model(model)`.
2. Генерирует временную метку.
3. Формирует JSON-словарь с данными запроса, включая сообщения, модель и флаг потоковой передачи.
4. Вычисляет подпись запроса с использованием `cls.calculate_signature(timestamp, json_dict)`.
5. Формирует заголовки запроса, включая API-ключ, временную метку и подпись.
6. Отправляет асинхронный POST-запрос к серверу AIUncensored.
7. Если включена потоковая передача, обрабатывает ответы построчно и генерирует результаты.
8. Если потоковая передача выключена, получает JSON-ответ и генерирует результат.

```
    model, messages, stream, proxy, api_key, kwargs
     |
     V
    timestamp = str(int(time.time()))
     |
     V
    json_dict = {"messages": [...], "model": model, "stream": stream}
     |
     V
    signature = cls.calculate_signature(timestamp, json_dict)
     |
     V
    headers = {..., "x-api-key": api_key, "x-timestamp": timestamp, "x-signature": signature}
     |
     V
    async with ClientSession(headers=headers) as session:
        async with session.post(url, json=json_dict, proxy=proxy) as response:
            await raise_for_status(response)
            if stream:
                # Обработка потоковой передачи
            else:
                # Обработка полной выдачи
     |
     V
    yield result
```

**Примеры**:

```python
model = "hermes3-70b"
messages = [{"role": "user", "content": "Hello, how are you?"}]
async for response in AIUncensored.create_async_generator(model=model, messages=messages, stream=True):
    print(response)