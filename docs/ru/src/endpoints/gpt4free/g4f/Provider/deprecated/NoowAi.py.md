# Модуль `NoowAi`

## Обзор

Модуль `NoowAi` предоставляет асинхронный генератор для взаимодействия с сервисом NoowAI. Он поддерживает ведение истории сообщений и использование модели `gpt-3.5-turbo`. Модуль предназначен для получения ответов от AI-модели NoowAI через асинхронные запросы.

## Подробнее

Модуль использует `aiohttp` для выполнения асинхронных HTTP-запросов к API NoowAI. Он формирует JSON-запрос с историей сообщений и отправляет его на сервер. Ответ от сервера приходит в виде потока данных, который модуль обрабатывает и выдает в виде асинхронного генератора.

## Классы

### `NoowAi`

**Описание**: Класс `NoowAi` является провайдером асинхронного генератора для взаимодействия с сервисом NoowAI.

**Наследует**:

-   `AsyncGeneratorProvider`: Наследует функциональность асинхронного генератора от базового класса `AsyncGeneratorProvider`.

**Атрибуты**:

-   `url` (str): URL сервиса NoowAI (`"https://noowai.com"`).
-   `supports_message_history` (bool): Поддержка истории сообщений (всегда `True`).
-   `supports_gpt_35_turbo` (bool): Поддержка модели `gpt-3.5-turbo` (всегда `True`).
-   `working` (bool): Индикатор работоспособности (всегда `False`).

**Методы**:

-   `create_async_generator()`: Создает асинхронный генератор для получения ответов от NoowAI.

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
    Создает асинхронный генератор для получения ответов от NoowAI.

    Args:
        model (str): Модель для использования (например, `gpt-3.5-turbo`).
        messages (Messages): Список сообщений для отправки в запросе.
        proxy (str, optional): Прокси-сервер для использования. По умолчанию `None`.
        **kwargs: Дополнительные параметры.

    Returns:
        AsyncResult: Асинхронный генератор, выдающий ответы от NoowAI.

    Raises:
        RuntimeError: Если приходит сломанная строка или возникает ошибка в данных ответа.
    """
```

**Назначение**: Функция `create_async_generator` создает асинхронный генератор, который отправляет сообщения в NoowAI и возвращает ответы в асинхронном режиме.

**Параметры**:

-   `cls`: Ссылка на класс `NoowAi`.
-   `model` (str): Имя используемой модели.
-   `messages` (Messages): Список сообщений, отправляемых в запросе.
-   `proxy` (str, optional): Адрес прокси-сервера (если необходимо). По умолчанию `None`.
-   `**kwargs`: Дополнительные именованные аргументы.

**Возвращает**:

-   `AsyncResult`: Асинхронный генератор, выдающий ответы от NoowAI.

**Вызывает исключения**:

-   `RuntimeError`: Вызывается, если приходит некорректный ответ от сервера или если в данных ответа содержится ошибка.

**Как работает функция**:

1.  **Формирование заголовков**: Создаются заголовки HTTP-запроса, включая User-Agent, Referer и Content-Type.
2.  **Создание сессии**: Создается асинхронная HTTP-сессия с использованием `aiohttp.ClientSession`.
3.  **Формирование данных запроса**: Создается словарь `data`, содержащий параметры запроса, такие как `botId`, `customId`, `session`, `chatId`, `contextId`, `messages`, `newMessage` и `stream`.
4.  **Отправка запроса**: Отправляется POST-запрос к API NoowAI (`{cls.url}/wp-json/mwai-ui/v1/chats/submit`) с использованием созданной сессии и JSON-данных.
5.  **Обработка ответа**:
    -   Читаются строки из ответа сервера.
    -   Если строка начинается с `b"data: "`:
        -   Извлекается JSON из строки.
        -   Проверяется наличие ключа `"type"` в JSON.
        -   Если `line["type"] == "live"`, то выдается `line["data"]`.
        -   Если `line["type"] == "end"`, то цикл завершается.
        -   Если `line["type"] == "error"`, то вызывается исключение `RuntimeError`.

```
Формирование заголовков и данных запроса
│
Создание асинхронной сессии (aiohttp.ClientSession)
│
Отправка POST-запроса к API NoowAI
│
Начало обработки потока данных из ответа
│
Проверка каждой строки на начало с "data: "
│
Извлечение JSON из строки
│
Проверка типа сообщения (line["type"])
├── "live": Выдача данных (yield line["data"])
├── "end": Завершение цикла
└── "error": Вызов исключения RuntimeError
```

**Примеры**:

```python
# Пример использования асинхронного генератора NoowAi
import asyncio
from typing import AsyncGenerator, List, Dict, Any

async def process_noowai_response(generator: AsyncGenerator[str, None]) -> None:
    """
    Асинхронно обрабатывает ответы от NoowAi.
    """
    async for message in generator:
        print(f"NoowAi: {message}")

async def main():
    messages: List[Dict[str, str]] = [
        {"role": "user", "content": "Hello, NoowAI!"},
        {"role": "assistant", "content": "Hello! How can I assist you today?"}
    ]
    
    # Создание асинхронного генератора
    generator: AsyncGenerator[str, None] = NoowAi.create_async_generator(model="gpt-3.5-turbo", messages=messages)
    
    # Обработка ответов от генератора
    await process_noowai_response(generator)

if __name__ == "__main__":
    asyncio.run(main())