# Модуль OpenAssistant

## Обзор

Модуль `OpenAssistant` предоставляет асинхронный генератор для взаимодействия с Open Assistant API. Он позволяет создавать чаты и получать ответы от модели `OA_SFT_Llama_30B_6`.
Модуль использует `aiohttp` для асинхронных HTTP-запросов. Этот файл содержит класс `OpenAssistant`, который является производным от `AsyncGeneratorProvider` и предназначен для асинхронной генерации ответов от модели Open Assistant.

## Подробней

Этот модуль используется для интеграции с сервисом Open Assistant, предоставляя возможность отправлять запросы и получать ответы в асинхронном режиме. Он включает в себя создание сессии, отправку сообщений, получение событий и удаление чата.

## Классы

### `OpenAssistant`

**Описание**: Класс для взаимодействия с Open Assistant API.
**Наследует**: `AsyncGeneratorProvider`

**Атрибуты**:
- `url` (str): URL для чата Open Assistant.
- `needs_auth` (bool): Указывает, требуется ли аутентификация.
- `working` (bool): Указывает, работает ли провайдер.
- `model` (str): Используемая модель (по умолчанию `"OA_SFT_Llama_30B_6"`).

**Методы**:
- `create_async_generator`: Создает асинхронный генератор для получения ответов от Open Assistant.

## Функции

### `create_async_generator`

```python
@classmethod
async def create_async_generator(
    cls,
    model: str,
    messages: Messages,
    proxy: str = None,
    cookies: dict = None,
    **kwargs
) -> AsyncResult:
    """
    Создает асинхронный генератор для получения ответов от Open Assistant.

    Args:
        model (str): Имя используемой модели.
        messages (Messages): Список сообщений для отправки.
        proxy (str, optional): URL прокси-сервера. По умолчанию `None`.
        cookies (dict, optional): Cookie для аутентификации. По умолчанию `None`.
        **kwargs: Дополнительные параметры для модели.

    Returns:
        AsyncResult: Асинхронный генератор, выдающий текстовые ответы.

    Raises:
        RuntimeError: Если в ответе от сервера содержится сообщение об ошибке.
        Exception: Если возникает ошибка при выполнении HTTP-запросов.
    """
```

**Назначение**: Создает асинхронный генератор, который взаимодействует с Open Assistant API для получения ответов на основе предоставленных сообщений.

**Параметры**:
- `cls` (class): Ссылка на класс `OpenAssistant`.
- `model` (str): Имя используемой модели.
- `messages` (Messages): Список сообщений для отправки.
- `proxy` (str, optional): URL прокси-сервера. По умолчанию `None`.
- `cookies` (dict, optional): Cookie для аутентификации. По умолчанию `None`.
- `**kwargs`: Дополнительные параметры для модели.

**Возвращает**:
- `AsyncResult`: Асинхронный генератор, выдающий текстовые ответы.

**Вызывает исключения**:
- `RuntimeError`: Если в ответе от сервера содержится сообщение об ошибке.
- `Exception`: Если возникает ошибка при выполнении HTTP-запросов.

**Как работает функция**:

1. **Инициализация**:
   - Проверяет наличие `cookies`, если их нет, пытается получить их с домена `"open-assistant.io"`.
   - Определяет `headers` для HTTP-запросов, включая `User-Agent`.
   - Создает асинхронную сессию `ClientSession` с использованием `cookies` и `headers`.

2. **Создание чата**:
   - Отправляет `POST` запрос на `"https://open-assistant.io/api/chat"` для создания нового чата.
   - Извлекает `chat_id` из JSON-ответа.

3. **Отправка сообщения пользователя**:
   - Форматирует входные `messages` с использованием `format_prompt` и оборачивает их в формат `<s>[INST]\n{formatted_messages}\n[/INST]`.
   - Создает данные `data` для отправки сообщения пользователя (`prompter_message`), включающие `chat_id`, форматированный `content` и `parent_id` (в данном случае `None`).
   - Отправляет `POST` запрос на `"https://open-assistant.io/api/chat/prompter_message"` с данными сообщения.
   - Извлекает `parent_id` из JSON-ответа.

4. **Отправка сообщения ассистента**:
   - Создает данные `data` для отправки сообщения ассистента (`assistant_message`), включающие `chat_id`, `parent_id`, имя модели (`model_config_name`), параметры выборки (`sampling_parameters`) и плагины (`plugins`).
   - Параметры выборки включают `top_k`, `temperature`, `repetition_penalty`, `max_new_tokens` и дополнительные параметры из `kwargs`.
   - Отправляет `POST` запрос на `"https://open-assistant.io/api/chat/assistant_message"` с данными сообщения.
   - Извлекает `message_id` из JSON-ответа. Если в ответе содержится поле `"message"`, выбрасывает исключение `RuntimeError` с текстом ошибки.

5. **Получение событий чата**:
   - Определяет параметры `params` для запроса событий, включающие `chat_id` и `message_id`.
   - Отправляет `POST` запрос на `"https://open-assistant.io/api/chat/events"` с параметрами запроса.
   - Асинхронно итерирует по строкам в ответе:
     - Декодирует строку из байтов в UTF-8.
     - Проверяет, начинается ли строка с `"data: "`.
     - Загружает JSON из остатка строки после `"data: "`.
     - Если `event_type` равен `"token"`, извлекает текст (`line["text"]`) и выдает его через `yield`.

6. **Удаление чата**:
   - Определяет параметры `params` для запроса удаления, включающие `chat_id`.
   - Отправляет `DELETE` запрос на `"https://open-assistant.io/api/chat"` с параметрами запроса.
   - Вызывает `response.raise_for_status()` для проверки успешности запроса.

```
A: Проверка наличия cookies
|
B: Получение cookies, если отсутствуют
|
C: Создание асинхронной сессии
|
D: Создание чата (POST /api/chat) -> chat_id
|
E: Форматирование сообщения пользователя
|
F: Отправка сообщения пользователя (POST /api/chat/prompter_message) -> parent_id
|
G: Отправка сообщения ассистента (POST /api/chat/assistant_message) -> message_id
|
H: Получение событий чата (POST /api/chat/events) -> генерация токенов
|
I: Удаление чата (DELETE /api/chat)
```

**Примеры**:

```python
# Пример использования функции create_async_generator
import asyncio
from typing import AsyncGenerator, List, Dict, Optional

from aiohttp import ClientSession

from g4f.Provider.deprecated.OpenAssistant import OpenAssistant

async def main():
    messages = [{"role": "user", "content": "Hello, how are you?"}]
    model = "OA_SFT_Llama_30B_6"
    proxy = None
    cookies = {}  # Replace with actual cookies if needed

    async def consume_generator(generator: AsyncGenerator[str, None]) -> None:
        async for item in generator:
            print(item, end="")

    generator = await OpenAssistant.create_async_generator(
        model=model,
        messages=messages,
        proxy=proxy,
        cookies=cookies
    )

    await consume_generator(generator)

if __name__ == "__main__":
    asyncio.run(main())