# Модуль `Aura`

## Обзор

Модуль предоставляет асинхронный генератор для взаимодействия с провайдером Aura (OpenChat Team). Он использует `aiohttp` для выполнения асинхронных HTTP-запросов и возвращает чанки данных, полученные от сервера. Модуль предназначен для интеграции с API OpenChat Team и поддерживает проксирование.

## Подробней

Этот модуль предназначен для обеспечения асинхронного взаимодействия с сервисом OpenChat Team. Он позволяет отправлять сообщения и получать ответы в виде асинхронного генератора, что позволяет обрабатывать большие объемы данных эффективно. Модуль использует `aiohttp` для выполнения HTTP-запросов и поддерживает проксирование, что делает его гибким для использования в различных сетевых конфигурациях.

## Классы

### `Aura`

**Описание**: Класс `Aura` предоставляет асинхронный генератор для взаимодействия с API OpenChat Team.

**Наследует**:
- `AsyncGeneratorProvider`: Класс наследует функциональность асинхронного генератора от `AsyncGeneratorProvider`.

**Атрибуты**:
- `url` (str): URL сервиса OpenChat Team (`https://openchat.team`).
- `working` (bool): Флаг, указывающий на работоспособность провайдера (в данном случае `False`).

**Методы**:
- `create_async_generator()`: Создает асинхронный генератор для взаимодействия с API OpenChat Team.

## Функции

### `create_async_generator`

```python
@classmethod
async def create_async_generator(
    cls,
    model: str,
    messages: Messages,
    proxy: str = None,
    temperature: float = 0.5,
    max_tokens: int = 8192,
    webdriver = None,
    **kwargs
) -> AsyncResult:
    """
    Создает асинхронный генератор для взаимодействия с API OpenChat Team.

    Args:
        model (str): Идентификатор модели, используемой для генерации ответа.
        messages (Messages): Список сообщений для отправки в API.
        proxy (str, optional): URL прокси-сервера для использования. По умолчанию `None`.
        temperature (float, optional): Температура для управления случайностью генерации. По умолчанию `0.5`.
        max_tokens (int, optional): Максимальное количество токенов в ответе. По умолчанию `8192`.
        webdriver: Selenium webdriver, используется для получения аргументов из браузера.
        **kwargs: Дополнительные именованные аргументы.

    Returns:
        AsyncResult: Асинхронный генератор, возвращающий чанки данных от API.

    Raises:
        Exception: Если возникает ошибка при выполнении запроса к API.
    """
```

**Назначение**: Создает асинхронный генератор для взаимодействия с API OpenChat Team.

**Параметры**:
- `cls`: Ссылка на класс.
- `model` (str): Идентификатор модели, используемой для генерации ответа.
- `messages` (Messages): Список сообщений для отправки в API.
- `proxy` (str, optional): URL прокси-сервера для использования. По умолчанию `None`.
- `temperature` (float, optional): Температура для управления случайностью генерации. По умолчанию `0.5`.
- `max_tokens` (int, optional): Максимальное количество токенов в ответе. По умолчанию `8192`.
- `webdriver`: Selenium webdriver, используется для получения аргументов из браузера.
- `**kwargs`: Дополнительные именованные аргументы.

**Возвращает**:
- `AsyncResult`: Асинхронный генератор, возвращающий чанки данных от API.

**Вызывает исключения**:
- `aiohttp.ClientError`: Если возникает ошибка при выполнении запроса к API.

**Как работает функция**:

1. **Получение аргументов из браузера**:
   - Используется функция `get_args_from_browser` для получения аргументов, необходимых для создания сессии `aiohttp.ClientSession`. Эта функция использует `webdriver` для взаимодействия с браузером и получения необходимых данных.

2. **Создание сессии `aiohttp.ClientSession`**:
   - Создается асинхронная сессия `aiohttp.ClientSession` с использованием полученных аргументов.

3. **Подготовка сообщений**:
   - Разделяются системные сообщения и сообщения пользователя. Системные сообщения добавляются в отдельный список `system_message`, а остальные сообщения добавляются в список `new_messages`.

4. **Формирование данных для запроса**:
   - Формируется словарь `data`, который включает в себя модель, сообщения, ключ, промпт и температуру.

5. **Выполнение POST-запроса к API**:
   - Выполняется асинхронный POST-запрос к API OpenChat Team по адресу `f"{cls.url}/api/chat"` с использованием сформированных данных и прокси (если указан).

6. **Обработка ответа**:
   - Для каждого чанка данных, полученного из ответа, выполняется декодирование в строку с игнорированием ошибок и возвращается через генератор.

```
A (Получение аргументов из браузера)
|
B (Создание сессии aiohttp.ClientSession)
|
C (Подготовка сообщений)
|
D (Формирование данных для запроса)
|
E (Выполнение POST-запроса к API)
|
F (Обработка ответа: декодирование и генерация чанков)
```

**Примеры**:

```python
# Пример использования create_async_generator
import asyncio
from typing import List, Dict, AsyncGenerator, Optional

# Допустим, есть функция get_args_from_browser и класс AsyncGeneratorProvider

class MockWebdriver:
    def __init__(self):
        pass

async def main():
    messages: List[Dict[str, str]] = [
        {"role": "user", "content": "Hello"},
        {"role": "system", "content": "You are a helpful assistant."}
    ]
    async def get_args_from_browser(url: str, webdriver, proxy: Optional[str] = None) -> dict:
        # Mock implementation for testing purposes
        return {}
    
    async def create_async_generator(
        model: str,
        messages: Messages,
        proxy: str = None,
        temperature: float = 0.5,
        max_tokens: int = 8192,
        webdriver = MockWebdriver(),
        **kwargs
    ) -> AsyncGenerator[str, None]:
        """
        Mock implementation of create_async_generator for demonstration purposes
        """
        yield "chunk1"
        yield "chunk2"
        yield "chunk3"
    
    async for chunk in create_async_generator(model="test_model", messages=messages, proxy="http://proxy.com"):
        print(chunk)

if __name__ == "__main__":
    asyncio.run(main())