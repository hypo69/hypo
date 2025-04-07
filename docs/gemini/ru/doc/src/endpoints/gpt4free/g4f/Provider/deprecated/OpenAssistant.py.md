# Модуль OpenAssistant

## Обзор

Модуль `OpenAssistant` предоставляет асинхронный генератор для взаимодействия с моделью Open Assistant. Он позволяет отправлять сообщения и получать ответы в режиме реального времени, используя API Open Assistant. Модуль предназначен для интеграции с другими частями проекта, требующими доступа к возможностям Open Assistant.

## Подробней

Этот модуль является устаревшим (`deprecated`). Он использует `aiohttp` для асинхронных запросов к API Open Assistant. Он получает куки, форматирует запросы и обрабатывает ответы, предоставляя их в виде асинхронного генератора.

## Классы

### `OpenAssistant`

**Описание**: Класс `OpenAssistant` предоставляет асинхронный генератор для взаимодействия с моделью Open Assistant.

**Наследует**:
- `AsyncGeneratorProvider`: Наследует функциональность асинхронного генератора от базового класса `AsyncGeneratorProvider`.

**Атрибуты**:
- `url` (str): URL для взаимодействия с Open Assistant ("https://open-assistant.io/chat").
- `needs_auth` (bool): Указывает, требуется ли аутентификация (True).
- `working` (bool): Указывает, работает ли провайдер (False).
- `model` (str): Название используемой модели ("OA_SFT_Llama_30B_6").

**Методы**:
- `create_async_generator`: Создает асинхронный генератор для обмена сообщениями с Open Assistant.

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
    Создает асинхронный генератор для взаимодействия с Open Assistant.

    Args:
        model (str): Название используемой модели.
        messages (Messages): Список сообщений для отправки.
        proxy (str, optional): Прокси-сервер для использования. По умолчанию `None`.
        cookies (dict, optional): Куки для аутентификации. По умолчанию `None`.
        **kwargs: Дополнительные параметры для передачи в API.

    Returns:
        AsyncResult: Асинхронный генератор, возвращающий текстовые ответы от Open Assistant.

    Raises:
        RuntimeError: Если в ответе от API содержится сообщение об ошибке.
        Exception: Если возникает ошибка при выполнении HTTP-запроса.

    """
```

**Назначение**:
Функция `create_async_generator` создает асинхронный генератор, который позволяет взаимодействовать с Open Assistant для получения ответов на сообщения.

**Параметры**:
- `cls`: Ссылка на класс `OpenAssistant`.
- `model` (str): Название используемой модели.
- `messages` (Messages): Список сообщений для отправки.
- `proxy` (str, optional): Прокси-сервер для использования. По умолчанию `None`.
- `cookies` (dict, optional): Куки для аутентификации. По умолчанию `None`.
- `**kwargs`: Дополнительные параметры для передачи в API.

**Возвращает**:
- `AsyncResult`: Асинхронный генератор, возвращающий текстовые ответы от Open Assistant.

**Вызывает исключения**:
- `RuntimeError`: Если в ответе от API содержится сообщение об ошибке.
- `Exception`: Если возникает ошибка при выполнении HTTP-запроса.

**Как работает функция**:

1.  **Получение куки**: Если куки не предоставлены, функция пытается получить их для домена "open-assistant.io".
2.  **Создание сессии**: Создается асинхронная клиентская сессия с использованием `aiohttp.ClientSession`.
3.  **Получение ID чата**: Отправляется POST-запрос к "https://open-assistant.io/api/chat" для получения ID чата.
4.  **Отправка сообщения пользователя**: Форматируется и отправляется сообщение пользователя с использованием `format_prompt` в API.
5.  **Отправка запроса ассистенту**: Отправляется запрос ассистенту с указанием ID чата, ID родительского сообщения, конфигурации модели и параметров выборки.
6.  **Получение ответа в реальном времени**: Отправляется POST-запрос к "https://open-assistant.io/api/chat/events" для получения ответа от ассистента в виде потока событий. Каждый полученный токен ответа возвращается через `yield`.
7.  **Удаление чата**: После завершения обмена сообщениями чат удаляется.

**ASCII Flowchart**:

```
    Начало
     ↓
    Получение куки (если отсутствуют)
     ↓
    Создание асинхронной сессии
     ↓
    Получение ID чата (POST запрос к /api/chat)
     ↓
    Отправка сообщения пользователя (POST запрос к /api/chat/prompter_message)
     ↓
    Отправка запроса ассистенту (POST запрос к /api/chat/assistant_message)
     ↓
    Получение ответа в реальном времени (POST запрос к /api/chat/events)
     │
     └──>  Извлечение токенов и отправка через yield
     ↓
    Удаление чата (DELETE запрос к /api/chat)
     ↓
    Конец
```

**Примеры**:

```python
# Пример использования create_async_generator
import asyncio
from typing import AsyncGenerator, List, Dict, Optional

from src.endpoints.gpt4free.g4f.typing import Messages
from src.endpoints.gpt4free.g4f.Provider.deprecated.OpenAssistant import OpenAssistant


async def main():
    model_name = "OA_SFT_Llama_30B_6"
    messages: Messages = [{"role": "user", "content": "Hello, how are you?"}]
    proxy: Optional[str] = None
    cookies: Optional[Dict] = None

    async def print_response(generator: AsyncGenerator[str, None]):
        async for token in generator:
            print(token, end="", flush=True)

    try:
        generator = await OpenAssistant.create_async_generator(
            model=model_name, messages=messages, proxy=proxy, cookies=cookies
        )
        await print_response(generator)
    except Exception as ex:
        print(f"Error: {ex}")

if __name__ == "__main__":
    asyncio.run(main())