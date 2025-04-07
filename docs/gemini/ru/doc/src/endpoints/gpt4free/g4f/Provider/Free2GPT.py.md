# Модуль для работы с провайдером Free2GPT
================================================

Модуль содержит класс `Free2GPT`, который используется для взаимодействия с сервисом Free2GPT для генерации текста.
Он поддерживает асинхронную генерацию текста и предоставляет методы для создания запросов к API Free2GPT.

## Обзор

Модуль предоставляет асинхронный класс `Free2GPT` для взаимодействия с API Free2GPT. Этот класс поддерживает указание модели, прокси и может использоваться для получения ответов в виде асинхронного генератора.

## Подробнее

Этот модуль предназначен для интеграции с сервисом Free2GPT, предоставляющим API для генерации текста на основе различных моделей, включая `gemini-1.5-pro` и `gemini-1.5-flash`. Класс `Free2GPT` асинхронно взаимодействует с API, обрабатывает ответы и обеспечивает удобный интерфейс для получения сгенерированного текста.

## Классы

### `Free2GPT`

**Описание**: Класс для взаимодействия с API Free2GPT. Позволяет генерировать текст асинхронно, поддерживая различные модели и прокси.

**Наследует**:
- `AsyncGeneratorProvider`: Обеспечивает поддержку асинхронной генерации.
- `ProviderModelMixin`: Предоставляет методы для работы с моделями.

**Атрибуты**:
- `url` (str): URL API Free2GPT.
- `working` (bool): Флаг, указывающий, что провайдер работает.
- `supports_message_history` (bool): Флаг, указывающий, что провайдер поддерживает историю сообщений.
- `default_model` (str): Модель, используемая по умолчанию (`gemini-1.5-pro`).
- `models` (List[str]): Список поддерживаемых моделей (`gemini-1.5-pro`, `gemini-1.5-flash`).

**Методы**:
- `create_async_generator`: Создает асинхронный генератор для генерации текста.

### `create_async_generator`

**Описание**: Создает асинхронный генератор для генерации текста с использованием API Free2GPT.

```python
@classmethod
async def create_async_generator(
    cls,
    model: str,
    messages: Messages,
    proxy: str = None,
    connector: BaseConnector = None,
    **kwargs,
) -> AsyncResult:
    """
    Создает асинхронный генератор для генерации текста с использованием API Free2GPT.

    Args:
        model (str): Модель для генерации текста.
        messages (Messages): Список сообщений для отправки в API.
        proxy (str, optional): Прокси-сервер для использования. По умолчанию `None`.
        connector (BaseConnector, optional): Aiohttp connector. По умолчанию `None`.

    Returns:
        AsyncResult: Асинхронный генератор, возвращающий текст чанками.

    Raises:
        RateLimitError: Если достигнут лимит запросов.
        Exception: При других ошибках во время запроса.
    """
```

**Параметры**:
- `cls`: Ссылка на класс.
- `model` (str): Модель для генерации текста.
- `messages` (Messages): Список сообщений для отправки в API.
- `proxy` (str, optional): Прокси-сервер для использования. По умолчанию `None`.
- `connector (BaseConnector, optional)`: Aiohttp connector. По умолчанию `None`.
- `**kwargs`: Дополнительные аргументы.

**Возвращает**:
- `AsyncResult`: Асинхронный генератор, возвращающий текст чанками.

**Вызывает исключения**:
- `RateLimitError`: Если достигнут лимит запросов.
- `Exception`: При других ошибках во время запроса.

**Как работает функция**:

1. **Подготовка заголовков**: Формируются заголовки запроса, включая `User-Agent`, `Accept`, `Content-Type`, `Referer` и `Origin`.
2. **Создание сессии**: Создается асинхронная сессия `aiohttp` с использованием переданного или созданного коннектора и заголовков.
3. **Подготовка данных**: Формируются данные для отправки в API, включая сообщения, текущее время и подпись.
4. **Отправка запроса**: Отправляется POST-запрос к API Free2GPT с данными в формате JSON.
5. **Обработка ответа**:
   - Если статус ответа `500` и текст содержит "Quota exceeded", выбрасывается исключение `RateLimitError`.
   - В противном случае проверяется статус ответа на наличие ошибок.
   - Полученный контент ответа итерируется по чанкам, каждый чанк декодируется и возвращается через генератор.

```
Подготовка запроса
│
└───> Создание сессии aiohttp
│
└───> Формирование данных (messages, timestamp, sign)
│
└───> Отправка POST-запроса к API
│
└───> Обработка ответа
    │
    ├───> Проверка на RateLimitError (статус 500 и "Quota exceeded")
    │   │
    │   └───> Выброс RateLimitError
    │
    └───> Проверка статуса ответа на ошибки
    │   │
    │   └───> Итерация по чанкам ответа
    │       │
    │       └───> Декодирование чанка
    │           │
    │           └───> Возврат чанка через генератор
    │
    └───> Завершение
```

**Примеры**:

```python
# Пример использования create_async_generator
import asyncio
from typing import AsyncGenerator, List, Dict

from aiohttp import BaseConnector

async def main():
    model: str = "gemini-1.5-pro"
    messages: List[Dict[str, str]] = [{"role": "user", "content": "Hello, how are you?"}]
    proxy: str = None
    connector: BaseConnector = None

    async def consume_generator(generator: AsyncGenerator[str, None]) -> None:
        async for chunk in generator:
            print(chunk, end="")

    generator = await Free2GPT.create_async_generator(model=model, messages=messages, proxy=proxy, connector=connector)
    await consume_generator(generator)

if __name__ == "__main__":
    asyncio.run(main())
```

## Функции

### `generate_signature`

**Описание**: Генерирует подпись для запроса к API Free2GPT.

```python
def generate_signature(time: int, text: str, secret: str = ""):
    """
    Генерирует подпись для запроса к API Free2GPT.

    Args:
        time (int): Временная метка.
        text (str): Текст сообщения.
        secret (str, optional): Секретный ключ. По умолчанию "".

    Returns:
        str: SHA256 хеш сообщения в шестнадцатеричном формате.
    """
```

**Параметры**:
- `time` (int): Временная метка.
- `text` (str): Текст сообщения.
- `secret` (str, optional): Секретный ключ. По умолчанию "".

**Возвращает**:
- `str`: SHA256 хеш сообщения в шестнадцатеричном формате.

**Как работает функция**:

1. **Формирование сообщения**: Создается строка сообщения, объединяющая временную метку, текст и секретный ключ (если он предоставлен) через двоеточие.
2. **Кодирование сообщения**: Сообщение кодируется в байты с использованием кодировки UTF-8.
3. **Хеширование сообщения**: Вычисляется SHA256 хеш закодированного сообщения.
4. **Форматирование хеша**: Хеш преобразуется в шестнадцатеричный формат.

```
Формирование сообщения (time:text:secret)
│
└───> Кодирование сообщения в байты (UTF-8)
│
└───> Вычисление SHA256 хеша
│
└───> Преобразование хеша в шестнадцатеричный формат
│
└───> Возврат хеша
```

**Примеры**:

```python
# Пример использования generate_signature
import time
from hashlib import sha256

timestamp = int(time.time() * 1e3)
text = "Hello, how are you?"
signature = generate_signature(timestamp, text)
print(signature)