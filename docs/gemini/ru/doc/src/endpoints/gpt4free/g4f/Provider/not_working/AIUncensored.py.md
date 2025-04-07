# Модуль AIUncensored
## Обзор

Модуль `AIUncensored` предоставляет асинхронный интерфейс для взаимодействия с AI Uncensored API. Он позволяет генерировать текст на основе предоставленных сообщений, поддерживая потоковую передачу данных и использование системных сообщений. Модуль также включает в себя функциональность для расчета подписи запросов, обеспечивая безопасное взаимодействие с API.

## Подробней

Модуль предназначен для использования в проекте `hypotez` в качестве одного из провайдеров API для генерации текста. Он реализует асинхронный генератор для обработки ответов от API, что позволяет эффективно обрабатывать большие объемы данных.

## Классы

### `AIUncensored`

**Описание**: Класс `AIUncensored` является асинхронным провайдером, реализующим взаимодействие с API AI Uncensored.

**Наследует**:
- `AsyncGeneratorProvider`: Обеспечивает асинхронную генерацию результатов.
- `ProviderModelMixin`: Добавляет функциональность для работы с моделями.

**Атрибуты**:
- `url` (str): URL для взаимодействия с API AI Uncensored.
- `api_key` (str): API ключ для аутентификации.
- `working` (bool): Указывает, работает ли провайдер.
- `supports_stream` (bool): Поддержка потоковой передачи данных.
- `supports_system_message` (bool): Поддержка системных сообщений.
- `supports_message_history` (bool): Поддержка истории сообщений.
- `default_model` (str): Модель, используемая по умолчанию.
- `models` (List[str]): Список поддерживаемых моделей.
- `model_aliases` (Dict[str, str]): Псевдонимы моделей.

**Методы**:
- `calculate_signature(timestamp: str, json_dict: dict) -> str`: Вычисляет подпись запроса.
- `get_server_url() -> str`: Возвращает случайный URL сервера из списка доступных.
- `create_async_generator(model: str, messages: Messages, stream: bool = False, proxy: str = None, api_key: str = None, **kwargs) -> AsyncResult`: Создает асинхронный генератор для получения ответов от API.

## Функции

### `calculate_signature`

```python
@staticmethod
def calculate_signature(timestamp: str, json_dict: dict) -> str:
    """
    Вычисляет подпись запроса на основе временной метки и данных запроса.

    Args:
        timestamp (str): Временная метка запроса.
        json_dict (dict): Данные запроса в формате JSON.

    Returns:
        str: Вычисленная подпись запроса.
    """
```

**Назначение**:
Функция `calculate_signature` вычисляет подпись запроса, используя алгоритм HMAC-SHA256. Это необходимо для обеспечения безопасности при взаимодействии с API.

**Параметры**:
- `timestamp` (str): Временная метка запроса в виде строки.
- `json_dict` (dict): Словарь, содержащий данные запроса, которые будут отправлены на сервер.

**Возвращает**:
- `str`: Строка, представляющая собой вычисленную подпись запроса в шестнадцатеричном формате.

**Как работает функция**:

1.  Формируется сообщение для подписи путем конкатенации временной метки и JSON-представления данных запроса.
2.  В качестве секретного ключа используется `your-super-secret-key-replace-in-production`. **Важно**: Этот ключ должен быть заменен на реальный секретный ключ в production-среде.
3.  Вычисляется HMAC-SHA256 подпись с использованием секретного ключа и сообщения.
4.  Подпись возвращается в виде шестнадцатеричной строки.

```
    timestamp + json_dict
        ↓
    message.encode('utf-8')
        ↓
    hmac.new(secret_key, message, hashlib.sha256)
        ↓
    signature.hexdigest()
```

**Примеры**:
```python
timestamp = "1678886400"
json_data = {"messages": [{"role": "user", "content": "Hello"}], "model": "hermes3-70b", "stream": False}
signature = AIUncensored.calculate_signature(timestamp, json_data)
print(signature)
```

### `get_server_url`

```python
@staticmethod
def get_server_url() -> str:
    """
    Возвращает случайный URL сервера из списка доступных серверов.

    Returns:
        str: URL сервера.
    """
```

**Назначение**:
Функция `get_server_url` выбирает случайный URL сервера из списка доступных серверов. Это позволяет распределить нагрузку между серверами и повысить отказоустойчивость.

**Возвращает**:
- `str`: Строка, представляющая собой URL выбранного сервера.

**Как работает функция**:

1.  Определяется список серверов.
2.  Случайным образом выбирается один из серверов из списка.
3.  Возвращается URL выбранного сервера.

```
    servers
        ↓
    random.choice(servers)
        ↓
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
    Создает асинхронный генератор для получения ответов от API.

    Args:
        model (str): Модель для использования.
        messages (Messages): Список сообщений для отправки.
        stream (bool, optional): Использовать ли потоковую передачу данных. По умолчанию `False`.
        proxy (str, optional): Прокси-сервер для использования. По умолчанию `None`.
        api_key (str, optional): API ключ для аутентификации. По умолчанию `None`.
        **kwargs: Дополнительные параметры.

    Returns:
        AsyncResult: Асинхронный генератор для получения ответов от API.
    """
```

**Назначение**:
Функция `create_async_generator` создает асинхронный генератор, который используется для получения ответов от API AI Uncensored. Она формирует запрос к API, подписывает его и обрабатывает ответ, возвращая результаты в виде асинхронного генератора.

**Параметры**:
- `model` (str): Имя модели, которую необходимо использовать для генерации ответа.
- `messages` (Messages): Список сообщений, которые будут отправлены в API для получения ответа.
- `stream` (bool, optional): Флаг, указывающий, следует ли использовать потоковую передачу данных. По умолчанию `False`.
- `proxy` (str, optional): URL прокси-сервера, если необходимо использовать прокси для подключения к API. По умолчанию `None`.
- `api_key` (str, optional): API ключ для аутентификации. По умолчанию `None`.
- `**kwargs`: Дополнительные параметры, которые могут быть переданы в API.

**Возвращает**:
- `AsyncResult`: Асинхронный генератор, который выдает части ответа от API.

**Как работает функция**:

1.  Получает имя модели, приводя его к нужному формату с помощью `cls.get_model(model)`.
2.  Генерирует временную метку, которая будет использоваться для подписи запроса.
3.  Формирует словарь `json_dict`, содержащий сообщения, модель и флаг потоковой передачи.
4.  Вычисляет подпись запроса с помощью `cls.calculate_signature(timestamp, json_dict)`.
5.  Формирует заголовок запроса, включая API ключ, временную метку и подпись.
6.  Определяет URL для запроса к API с помощью `cls.get_server_url()`.
7.  Использует `ClientSession` из библиотеки `aiohttp` для отправки асинхронного POST запроса к API.
8.  Обрабатывает ответ от API:
    - Если включена потоковая передача (`stream=True`):
        - Читает ответ построчно.
        - Декодирует каждую строку из UTF-8.
        - Извлекает данные из JSON.
        - Выдает данные с помощью `yield`.
    - Если потоковая передача выключена (`stream=False`):
        - Читает весь ответ как JSON.
        - Извлекает содержимое ответа.
        - Выдает содержимое с помощью `yield`.

```
    model, messages, stream, proxy, api_key, kwargs
        ↓
    model = cls.get_model(model)
        ↓
    timestamp = str(int(time.time()))
        ↓
    json_dict = {"messages": [...], "model": model, "stream": stream}
        ↓
    signature = cls.calculate_signature(timestamp, json_dict)
        ↓
    headers = {..., "x-api-key": cls.api_key, "x-timestamp": timestamp, "x-signature": signature}
        ↓
    url = f"{cls.get_server_url()}/api/chat"
        ↓
    ClientSession.post(url, json=json_dict, proxy=proxy)
        ↓
    response processing (stream=True or stream=False)
        ↓
    yield data
```

**Примеры**:

Пример использования с потоковой передачей:

```python
async for part in AIUncensored.create_async_generator(model="hermes3-70b", messages=[{"role": "user", "content": "Hello"}], stream=True):
    print(part)
```

Пример использования без потоковой передачи:

```python
result = AIUncensored.create_async_generator(model="hermes3-70b", messages=[{"role": "user", "content": "Hello"}], stream=False)
async for item in result:
    print(item)