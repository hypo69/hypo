# Модуль Cromicle

## Обзор

Модуль `Cromicle` предоставляет асинхронный генератор для взаимодействия с сервисом `cromicle.top`. Он позволяет отправлять сообщения и получать ответы в потоковом режиме. Модуль поддерживает модель `gpt-3.5-turbo`.

## Подробнее

Этот модуль предназначен для асинхронного взаимодействия с API `cromicle.top`. Он использует `aiohttp` для выполнения асинхронных HTTP-запросов. Основная задача модуля - отправка сообщений и получение ответов от сервера в режиме реального времени.

## Классы

### `Cromicle`

**Описание**: Класс `Cromicle` является провайдером для асинхронной генерации ответов от сервиса `cromicle.top`.

**Наследует**: `AsyncGeneratorProvider`

**Аттрибуты**:

-   `url` (str): URL сервиса `cromicle.top`.
-   `working` (bool): Флаг, указывающий на работоспособность сервиса.
-   `supports_gpt_35_turbo` (bool): Флаг, указывающий на поддержку модели `gpt-3.5-turbo`.

**Методы**:

-   `create_async_generator`: Создает асинхронный генератор для получения ответов от сервиса.

## Функции

### `create_async_generator`

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
    Создает асинхронный генератор для получения ответов от сервиса cromicle.top.

    Args:
        model (str): Модель для генерации ответа.
        messages (Messages): Список сообщений для отправки.
        proxy (str, optional): Прокси-сервер для использования. По умолчанию `None`.
        **kwargs: Дополнительные аргументы.

    Returns:
        AsyncResult: Асинхронный генератор, возвращающий ответы от сервиса.
    """
```

**Назначение**: Создание асинхронного генератора для взаимодействия с API `cromicle.top`.

**Параметры**:

-   `cls`: Ссылка на класс `Cromicle`.
-   `model` (str): Модель для генерации ответа.
-   `messages` (Messages): Список сообщений для отправки.
-   `proxy` (str, optional): Прокси-сервер для использования. По умолчанию `None`.
-   `**kwargs`: Дополнительные аргументы.

**Возвращает**:

-   `AsyncResult`: Асинхронный генератор, возвращающий ответы от сервиса.

**Как работает функция**:

1.  **Инициализация**: Функция `create_async_generator` принимает параметры, необходимые для создания запроса к API `cromicle.top`, такие как модель, сообщения и прокси (если указан).
2.  **Создание сессии**: Создается асинхронная сессия с использованием `aiohttp.ClientSession` с заголовками, полученными из функции `_create_header`.
3.  **Выполнение POST-запроса**: Выполняется POST-запрос к эндпоинту `/chat` на сервере `cromicle.top`. Запрос включает JSON-payload, созданный функцией `_create_payload` на основе переформатированных сообщений.
4.  **Обработка ответа**: Функция итерируется по содержимому ответа, полученного от сервера, в виде потока байтов.
5.  **Генерация результата**: Каждый чанк байтов декодируется в строку и передается через генератор.

```
Начало
│
├─> Создание сессии aiohttp
│   │
│   └─> _create_header(): Создание заголовков запроса
│
│
├─> Выполнение POST-запроса к '/chat'
│   │
│   ├─> _create_payload(format_prompt(messages)): Создание JSON-payload
│   │   │
│   │   └─> format_prompt(messages): Форматирование сообщений
│   │   │
│   │   └─> sha256('abc'.encode() + message.encode()).hexdigest(): Создание hash
│   │
│   └─> Отправка запроса с прокси (если указан)
│
│
├─> Обработка потока ответа
│   │
│   └─> Итерация по stream в response.content.iter_any()
│   │
│   └─> Декодирование байтов в строку: stream.decode()
│
│
└─> Генерация строки ответа (yield)
│
Конец
```

**Примеры**:

```python
# Пример использования create_async_generator
import asyncio
from typing import List, Dict, AsyncGenerator, Optional

from aiohttp import ClientSession

Messages = List[Dict[str, str]]

class Cromicle:
    url: str = 'https://cromicle.top'
    working: bool = False
    supports_gpt_35_turbo: bool = True

    @classmethod
    async def create_async_generator(
        cls,
        model: str,
        messages: Messages,
        proxy: str = None,
        **kwargs
    ) -> AsyncGenerator[str, None]:
        """
        Создает асинхронный генератор для получения ответов от сервиса cromicle.top.

        Args:
            model (str): Модель для генерации ответа.
            messages (Messages): Список сообщений для отправки.
            proxy (str, optional): Прокси-сервер для использования. По умолчанию `None`.
            **kwargs: Дополнительные аргументы.

        Returns:
            AsyncGenerator[str, None]: Асинхронный генератор, возвращающий ответы от сервиса.
        """
        async with ClientSession(
            headers=_create_header()
        ) as session:
            async with session.post(
                f'{cls.url}/chat',
                proxy=proxy,
                json=_create_payload(format_prompt(messages))
            ) as response:
                response.raise_for_status()
                async for stream in response.content.iter_any():
                    if stream:
                        yield stream.decode()

def _create_header() -> Dict[str, str]:
    return {
        'accept': '*/*',
        'content-type': 'application/json',
    }

def _create_payload(message: str) -> Dict[str, str]:
    return {
        'message': message,
        'token': 'abc',
        'hash': sha256('abc'.encode() + message.encode()).hexdigest()
    }


async def main():
    messages: Messages = [{"role": "user", "content": "Hello, how are you?"}]
    generator = Cromicle.create_async_generator(model="gpt-3.5-turbo", messages=messages)
    async for message in await generator:
        print(message, end="")

if __name__ == "__main__":
    asyncio.run(main())
```

### `_create_header`

```python
def _create_header() -> Dict[str, str]:
    """
    Создает словарь с заголовками для HTTP-запроса.

    Returns:
        Dict[str, str]: Словарь с заголовками 'accept' и 'content-type'.
    """
```

**Назначение**: Создает словарь с заголовками для HTTP-запроса.

**Возвращает**:

-   `Dict[str, str]`: Словарь с заголовками `accept` и `content-type`.

**Как работает функция**:

Функция `_create_header` создает и возвращает словарь, содержащий заголовки HTTP-запроса. В частности, она устанавливает заголовок `accept` в значение `'*/*'` и заголовок `content-type` в значение `'application/json'`.

```
Начало
│
└─> Создание словаря с заголовками:
│   │
│   └─> 'accept': '*/*'
│   │
│   └─> 'content-type': 'application/json'
│
└─> Возврат словаря
│
Конец
```

**Примеры**:

```python
# Пример использования _create_header
def _create_header() -> Dict[str, str]:
    return {
        'accept': '*/*',
        'content-type': 'application/json',
    }

headers = _create_header()
print(headers)  # Вывод: {'accept': '*/*', 'content-type': 'application/json'}
```

### `_create_payload`

```python
def _create_payload(message: str) -> Dict[str, str]:
    """
    Создает словарь с данными для отправки в теле HTTP-запроса.

    Args:
        message (str): Сообщение для отправки.

    Returns:
        Dict[str, str]: Словарь с данными 'message', 'token' и 'hash'.
    """
```

**Назначение**: Создает словарь с данными для отправки в теле HTTP-запроса.

**Параметры**:

-   `message` (str): Сообщение для отправки.

**Возвращает**:

-   `Dict[str, str]`: Словарь с данными `message`, `token` и `hash`.

**Как работает функция**:

Функция `_create_payload` принимает сообщение в качестве аргумента и создает словарь, содержащий это сообщение, токен `'abc'` и хеш, вычисленный на основе сообщения и токена. Хеш вычисляется с использованием алгоритма SHA256.

```
Начало
│
├─> Получение message
│
├─> Создание словаря:
│   │
│   └─> 'message': message
│   │
│   └─> 'token': 'abc'
│   │
│   └─> 'hash': sha256('abc'.encode() + message.encode()).hexdigest()
│
└─> Возврат словаря
│
Конец
```

**Примеры**:

```python
# Пример использования _create_payload
import hashlib

def _create_payload(message: str) -> Dict[str, str]:
    return {
        'message': message,
        'token': 'abc',
        'hash': hashlib.sha256('abc'.encode() + message.encode()).hexdigest()
    }

message = "Hello, world!"
payload = _create_payload(message)
print(payload)