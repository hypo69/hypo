# Модуль Acytoo

## Обзор

Модуль предоставляет асинхронный интерфейс для взаимодействия с провайдером Acytoo, который использует GPT-3.5-turbo. Он позволяет генерировать текст на основе предоставленных сообщений, поддерживая историю сообщений и работу через прокси.

## Подробней

Модуль предназначен для интеграции с gpt4free, обеспечивая возможность использования модели GPT-3.5-turbo через асинхронный генератор. Он включает функции для создания заголовков и полезной нагрузки запроса, необходимые для взаимодействия с API Acytoo.

## Классы

### `Acytoo`

**Описание**: Класс, представляющий провайдера Acytoo.

**Наследует**:
- `AsyncGeneratorProvider`: Наследует функциональность асинхронного генератора от базового класса `AsyncGeneratorProvider`.

**Атрибуты**:
- `url` (str): URL-адрес API Acytoo.
- `working` (bool): Флаг, указывающий на работоспособность провайдера (в данном случае `False`).
- `supports_message_history` (bool): Флаг, указывающий на поддержку истории сообщений (в данном случае `True`).
- `supports_gpt_35_turbo` (bool): Флаг, указывающий на поддержку модели GPT-3.5-turbo (в данном случае `True`).

**Методы**:
- `create_async_generator`: Асинхронный метод для создания генератора, который отправляет запросы к API Acytoo и возвращает сгенерированный текст.

#### `create_async_generator`

```python
@classmethod
async def create_async_generator(
    cls,
    model: str,
    messages: Messages,
    proxy: str = None,
    **kwargs
) -> AsyncResult:
    """
    Создает асинхронный генератор для взаимодействия с API Acytoo.

    Args:
        model (str): Модель для использования (в данном случае всегда 'gpt-3.5-turbo').
        messages (Messages): Список сообщений для отправки в API.
        proxy (str, optional): URL прокси-сервера. По умолчанию `None`.
        **kwargs: Дополнительные аргументы, передаваемые в API.

    Returns:
        AsyncResult: Асинхронный генератор, возвращающий сгенерированный текст.

    Raises:
        aiohttp.ClientResponseError: Если возникает ошибка при отправке запроса к API.

    """
```

**Как работает функция**:

1.  Функция `create_async_generator` создает асинхронный генератор, который взаимодействует с API Acytoo для генерации текста на основе предоставленных сообщений.

2.  Создание сессии:
    - Создается асинхронная сессия `aiohttp.ClientSession` с заголовками, полученными из функции `_create_header`.
    - Заголовки содержат информацию о типе контента и принимаемых данных (`accept`, `content-type`).

3.  Отправка POST-запроса:
    - Внутри асинхронной сессии отправляется POST-запрос к API Acytoo (`f'{cls.url}/api/completions'`).
    - В качестве параметров передаются:
        - `proxy`: Прокси-сервер, если указан.
        - `json`: Полезная нагрузка (payload), созданная с помощью функции `_create_payload`. Она содержит ключ API, модель, сообщения, температуру и пароль.

4.  Обработка ответа:
    - Функция `response.raise_for_status()` проверяет статус ответа и вызывает исключение, если статус указывает на ошибку.

5.  Генерация текста:
    - Асинхронно итерируется по содержимому ответа (`response.content.iter_any()`) в виде потока байтов.
    - Каждый полученный фрагмент (`stream`) декодируется в строку и передается через `yield`, делая функцию генератором.
    - Если фрагмент не пустой, он возвращается как часть сгенерированного текста.

```
    create_async_generator
    │
    ├── Создание асинхронной сессии (ClientSession)
    │   с заголовками (_create_header)
    │
    ├── Отправка POST-запроса к API Acytoo
    │   │
    │   ├── URL: f'{cls.url}/api/completions'
    │   ├── proxy: Прокси-сервер (если указан)
    │   └── json: Полезная нагрузка (_create_payload)
    │       │
    │       ├── key: ''
    │       ├── model: 'gpt-3.5-turbo'
    │       ├── messages: Список сообщений
    │       ├── temperature: Температура (по умолчанию 0.5)
    │       └── password: ''
    │
    ├── Проверка статуса ответа (response.raise_for_status())
    │
    └── Итерация по содержимому ответа (response.content.iter_any())
        │
        └── Декодирование фрагмента (stream.decode()) и передача через yield
```

**Примеры**:

```python
# Пример вызова create_async_generator
messages = [{"role": "user", "content": "Hello, how are you?"}]
async def main():
    async for message in Acytoo.create_async_generator(model='gpt-3.5-turbo', messages=messages):
        print(message)

# Пример с использованием прокси
messages = [{"role": "user", "content": "Привет, как дела?"}]
async def main():
    async for message in Acytoo.create_async_generator(model='gpt-3.5-turbo', messages=messages, proxy='http://proxy.example.com'):
        print(message)
```

## Функции

### `_create_header`

```python
def _create_header() -> dict:
    """
    Создает заголовки для HTTP-запроса.

    Returns:
        dict: Словарь с заголовками 'accept' и 'content-type'.
    """
```

**Как работает функция**:

1.  Функция `_create_header` создает словарь с HTTP-заголовками, необходимыми для запросов к API Acytoo.

2.  Определение заголовков:
    - `'accept': '*/*'`: Указывает, что клиент принимает любой тип контента.
    - `'content-type': 'application/json'`: Указывает, что тело запроса будет в формате JSON.

```
    _create_header
    │
    └── Создание словаря с HTTP-заголовками
        │
        ├── 'accept': '*/*'
        └── 'content-type': 'application/json'
```

**Примеры**:

```python
# Пример вызова _create_header
header = _create_header()
print(header)  # {'accept': '*/*', 'content-type': 'application/json'}
```

### `_create_payload`

```python
def _create_payload(messages: Messages, temperature: float = 0.5, **kwargs) -> dict:
    """
    Создает полезную нагрузку (payload) для отправки в API Acytoo.

    Args:
        messages (Messages): Список сообщений для отправки в API.
        temperature (float, optional): Температура генерации текста. По умолчанию 0.5.
        **kwargs: Дополнительные аргументы, которые могут быть переданы в API.

    Returns:
        dict: Словарь с данными для отправки в API.
    """
```

**Как работает функция**:

1.  Функция `_create_payload` создает полезную нагрузку (payload) в виде словаря, который будет отправлен в API Acytoo.

2.  Определение параметров:
    - `'key': ''`: Ключ API (в данном случае пустая строка).
    - `'model': 'gpt-3.5-turbo'`: Модель для использования.
    - `'messages': messages`: Список сообщений для отправки.
    - `'temperature': temperature`: Температура генерации текста.
    - `'password': ''`: Пароль (в данном случае пустая строка).

```
    _create_payload
    │
    └── Создание словаря с данными для отправки в API
        │
        ├── 'key': ''
        ├── 'model': 'gpt-3.5-turbo'
        ├── 'messages': Список сообщений
        ├── 'temperature': Температура
        └── 'password': ''
```

**Примеры**:

```python
# Пример вызова _create_payload
messages = [{"role": "user", "content": "Как дела?"}]
payload = _create_payload(messages=messages)
print(payload)
# {'key': '', 'model': 'gpt-3.5-turbo', 'messages': ..., 'temperature': 0.5, 'password': ''}

# Пример с указанием температуры
messages = [{"role": "user", "content": "What is the meaning of life?"}]
payload = _create_payload(messages=messages, temperature=0.7)
print(payload)
# {'key': '', 'model': 'gpt-3.5-turbo', 'messages': ..., 'temperature': 0.7, 'password': ''}