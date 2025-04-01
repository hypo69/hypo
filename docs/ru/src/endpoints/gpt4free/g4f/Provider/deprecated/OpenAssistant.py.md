# Модуль OpenAssistant

## Обзор

Модуль `OpenAssistant` предоставляет асинхронный класс `OpenAssistant`, который позволяет взаимодействовать с сервисом Open Assistant для генерации текста. Он использует `aiohttp` для асинхронных HTTP-запросов и поддерживает установку прокси и cookies. Модуль предназначен для работы с устаревшей версией API Open Assistant.

## Подробней

Этот модуль предоставляет функциональность для подключения и взаимодействия с Open Assistant API. Он автоматизирует процесс создания чата, отправки запросов и получения ответов, используя асинхронные вызовы. Класс `OpenAssistant` предназначен для использования в асинхронных приложениях, требующих интеграции с Open Assistant.

## Классы

### `OpenAssistant`

**Описание**:
Асинхронный класс для взаимодействия с Open Assistant API.

**Наследует**:
- `AsyncGeneratorProvider`: Наследует от базового класса `AsyncGeneratorProvider`, который предоставляет общую структуру для асинхронных провайдеров генерации текста.

**Атрибуты**:
- `url` (str): URL для взаимодействия с Open Assistant API ("https://open-assistant.io/chat").
- `needs_auth` (bool): Указывает, требуется ли аутентификация (True).
- `working` (bool): Указывает, находится ли провайдер в рабочем состоянии (False).
- `model` (str): Используемая модель ("OA_SFT_Llama_30B_6").

**Методы**:
- `create_async_generator`: Создает асинхронный генератор для получения ответов от Open Assistant API.

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
    Создает асинхронный генератор для получения ответов от Open Assistant API.

    Args:
        cls: Ссылка на класс.
        model (str): Название модели, которую нужно использовать.
        messages (Messages): Список сообщений для отправки в Open Assistant.
        proxy (str, optional): URL прокси-сервера. По умолчанию `None`.
        cookies (dict, optional): Словарь cookies для аутентификации. По умолчанию `None`.
        **kwargs: Дополнительные параметры для настройки генерации.

    Returns:
        AsyncResult: Асинхронный генератор, возвращающий текст от Open Assistant.

    Raises:
        RuntimeError: Если в ответе от Open Assistant содержится сообщение об ошибке.
        Exception: Если при выполнении запроса возникает HTTP-ошибка.
    """
```

**Назначение**:
Создание асинхронного генератора для взаимодействия с Open Assistant API, отправки сообщений и получения ответов.

**Параметры**:
- `cls`: Ссылка на класс.
- `model` (str): Название модели, которую нужно использовать для генерации текста.
- `messages` (Messages): Список сообщений для отправки в Open Assistant.
- `proxy` (str, optional): URL прокси-сервера для выполнения запросов. По умолчанию `None`.
- `cookies` (dict, optional): Словарь cookies для аутентификации. Если не указаны, используются cookies, полученные с сайта open-assistant.io. По умолчанию `None`.
- `**kwargs`: Дополнительные параметры конфигурации для генерации текста, такие как `top_k`, `top_p`, `temperature` и `max_new_tokens`.

**Возвращает**:
- `AsyncResult`: Асинхронный генератор, выдающий текстовые фрагменты ответа от Open Assistant.

**Вызывает исключения**:
- `RuntimeError`: Вызывается, если API возвращает сообщение об ошибке.
- `Exception`: Вызывается, если при выполнении HTTP-запроса возникает ошибка.

**Как работает функция**:

1. **Инициализация**:
   - Если `cookies` не предоставлены, функция пытается получить их, используя `get_cookies("open-assistant.io")`.
   - Определяются заголовки User-Agent для имитации запроса от браузера.

2. **Создание сессии `aiohttp`**:
   - Создается асинхронная сессия `ClientSession` с использованием переданных `cookies` и `headers`.

3. **Создание чата**:
   - Отправляется POST-запрос к `https://open-assistant.io/api/chat` для создания нового чата.
   - Из ответа извлекается `chat_id`, который будет использоваться для дальнейших запросов.

4. **Отправка сообщения пользователя**:
   - Форматируется сообщение пользователя из списка `messages` с использованием функции `format_prompt`.
   - Отправляется POST-запрос к `https://open-assistant.io/api/chat/prompter_message` с `chat_id` и форматированным сообщением.
   - Из ответа извлекается `parent_id`, который будет использоваться как `parent_id` для сообщения ассистента.

5. **Отправка запроса ассистенту**:
   - Формируются данные для запроса к ассистенту, включая `chat_id`, `parent_id`, название модели и параметры генерации.
   - Отправляется POST-запрос к `https://open-assistant.io/api/chat/assistant_message` с этими данными.
   - Если в ответе содержится `id`, он сохраняется как `message_id`. Если в ответе содержится сообщение об ошибке, вызывается исключение `RuntimeError`.

6. **Получение событий чата**:
   - Отправляется POST-запрос к `https://open-assistant.io/api/chat/events` с `chat_id` и `message_id` для получения событий чата.
   - Функция перебирает строки в ответе, декодирует их и извлекает текстовые фрагменты (`token`), которые затем выдаются через `yield`.

7. **Удаление чата**:
   - После завершения получения событий чата отправляется DELETE-запрос к `https://open-assistant.io/api/chat` для удаления чата.

```text
Инициализация Cookies и Headers
↓
Создание асинхронной сессии aiohttp
│
Создание чата (POST /api/chat) → chat_id
│
Отправка сообщения пользователя (POST /api/chat/prompter_message) → parent_id
│
Отправка запроса ассистенту (POST /api/chat/assistant_message) → message_id
│
Получение событий чата (POST /api/chat/events) → Текстовые фрагменты ответа (yield)
│
Удаление чата (DELETE /api/chat)
↓
Завершение
```

**Примеры**:

```python
# Пример использования create_async_generator
import asyncio
from typing import AsyncGenerator, List, Dict, Any

async def main():
    messages = [{"role": "user", "content": "Hello, Open Assistant!"}]
    model = "OA_SFT_Llama_30B_6"
    proxy = None
    cookies = {}
    kwargs = {}

    generator: AsyncGenerator[str, None] = await OpenAssistant.create_async_generator(
        model=model, messages=messages, proxy=proxy, cookies=cookies, **kwargs
    )

    async for text in generator:
        print(text, end="")

if __name__ == "__main__":
    asyncio.run(main())