# Модуль для работы с Qwen Qwen-2.5M через HF Space
## Обзор

Модуль `Qwen_Qwen_2_5M` предоставляет асинхронный интерфейс для взаимодействия с моделью Qwen Qwen-2.5M, размещенной на HF Space. Он поддерживает потоковую передачу данных и системные сообщения, позволяя использовать модель для генерации текста в реальном времени. Модуль использует `aiohttp` для выполнения асинхронных HTTP-запросов к API HF Space.

## Подробнее

Этот модуль предназначен для интеграции в проекты, требующие взаимодействия с моделью Qwen Qwen-2.5M. Он обеспечивает удобный способ отправки запросов и получения ответов в асинхронном режиме, что позволяет эффективно использовать ресурсы и обеспечивает высокую производительность.

## Классы

### `Qwen_Qwen_2_5M`

**Описание**: Класс `Qwen_Qwen_2_5M` реализует асинхронный генератор, который взаимодействует с моделью Qwen Qwen-2.5M через API HF Space.

**Принцип работы**:
1.  Класс наследуется от `AsyncGeneratorProvider` и `ProviderModelMixin`, что обеспечивает поддержку асинхронной генерации и управления моделями.
2.  Определяются статические атрибуты, такие как `label`, `url`, `api_endpoint`, `working`, `supports_stream`, `supports_system_message`, `supports_message_history`, `default_model`, `model_aliases` и `models`, которые задают параметры и настройки для взаимодействия с API.
3.  Метод `create_async_generator` создает асинхронный генератор, который отправляет запросы к API и возвращает сгенерированный текст.

**Атрибуты**:

*   `label` (str): Метка провайдера, `"Qwen Qwen-2.5M"`.
*   `url` (str): URL HF Space, `"https://qwen-qwen2-5-1m-demo.hf.space"`.
*   `api_endpoint` (str): URL API для отправки запросов, формируется из `url`.
*   `working` (bool): Указывает, работает ли провайдер, `True`.
*   `supports_stream` (bool): Указывает, поддерживает ли провайдер потоковую передачу, `True`.
*   `supports_system_message` (bool): Указывает, поддерживает ли провайдер системные сообщения, `True`.
*   `supports_message_history` (bool): Указывает, поддерживает ли провайдер историю сообщений, `False`.
*   `default_model` (str): Модель по умолчанию, `"qwen-2.5-1m-demo"`.
*   `model_aliases` (dict): Алиасы моделей, `{"qwen-2.5-1m": default_model}`.
*   `models` (list): Список моделей, формируется из ключей `model_aliases`.

**Методы**:

*   `create_async_generator`: Создает асинхронный генератор для взаимодействия с моделью.

## Функции

### `create_async_generator`

```python
@classmethod
async def create_async_generator(
    cls,
    model: str,
    messages: Messages,
    proxy: str = None,
    return_conversation: bool = False,
    conversation: JsonConversation = None,
    **kwargs
) -> AsyncResult:
    """
    Создает асинхронный генератор для взаимодействия с моделью Qwen Qwen-2.5M.

    Args:
        model (str): Имя модели для использования.
        messages (Messages): Список сообщений для отправки модели.
        proxy (str, optional): Прокси-сервер для использования. По умолчанию `None`.
        return_conversation (bool, optional): Указывает, следует ли возвращать объект `JsonConversation`. По умолчанию `False`.
        conversation (JsonConversation, optional): Объект `JsonConversation` для продолжения беседы. По умолчанию `None`.

    Returns:
        AsyncResult: Асинхронный генератор, возвращающий текст, сгенерированный моделью.

    Raises:
        aiohttp.ClientError: Если возникает ошибка при выполнении HTTP-запроса.
        json.JSONDecodeError: Если не удается декодировать JSON-ответ.

    Внутренние функции:
        generate_session_hash(): Генерирует уникальный хэш сессии.
    """
```

**Назначение**: Создает асинхронный генератор для взаимодействия с моделью Qwen Qwen-2.5M.

**Параметры**:

*   `model` (str): Имя модели для использования.
*   `messages` (Messages): Список сообщений для отправки модели.
*   `proxy` (str, optional): Прокси-сервер для использования. По умолчанию `None`.
*   `return_conversation` (bool, optional): Указывает, следует ли возвращать объект `JsonConversation`. По умолчанию `False`.
*   `conversation` (JsonConversation, optional): Объект `JsonConversation` для продолжения беседы. По умолчанию `None`.
*   `**kwargs`: Дополнительные аргументы.

**Возвращает**:

*   `AsyncResult`: Асинхронный генератор, возвращающий текст, сгенерированный моделью.

**Вызывает исключения**:

*   `aiohttp.ClientError`: Если возникает ошибка при выполнении HTTP-запроса.
*   `json.JSONDecodeError`: Если не удается декодировать JSON-ответ.

**Как работает функция**:

1.  Функция генерирует уникальный хэш сессии с помощью внутренней функции `generate_session_hash`. Если передан объект `conversation`, используется его хэш сессии.
2.  Если `return_conversation` имеет значение `True`, функция возвращает объект `JsonConversation` с хэшем сессии.
3.  Форматирует запрос, используя `format_prompt(messages)` если нет объекта `conversation` или получает последнее сообщение пользователя `get_last_user_message(messages)` если объект `conversation` передан в функцию.
4.  Определяет заголовки HTTP-запроса, включая `accept`, `accept-language`, `content-type`, `origin`, `referer` и `user-agent`.
5.  Создает полезную нагрузку (payload) для отправки запроса к API, включая `data`, `event_data`, `fn_index`, `trigger_id` и `session_hash`.
6.  Использует `aiohttp.ClientSession` для выполнения асинхронных HTTP-запросов.
7.  Отправляет POST-запрос к `cls.api_endpoint` с заголовками и полезной нагрузкой.
8.  Получает данные из ответа и отправляет POST-запрос к `join_url` для присоединения к очереди.
9.  Получает `event_id` из ответа.
10. Подготавливает запрос потока данных, определяя `url_data` и `headers_data`.
11. Отправляет GET-запрос к `url_data` с заголовками `headers_data` и обрабатывает ответ потоково.
12. Декодирует каждую строку ответа, проверяет, начинается ли строка с `'data: '`, и пытается декодировать JSON из строки.
13. Если `json_data` содержит сообщение `'process_generating'`, извлекает сгенерированный текст и возвращает его.
14. Если `json_data` содержит сообщение `'process_completed'`, извлекает полный ответ и завершает генерацию.
15. Обрабатывает исключение `json.JSONDecodeError`, если не удается декодировать JSON, и логирует ошибку.

**Внутренние функции**:

### `generate_session_hash`

```python
def generate_session_hash():
    """Generate a unique session hash."""
    return str(uuid.uuid4()).replace(\'-\', \'\')[:12]
```

**Назначение**: Генерирует уникальный хэш сессии.

**Параметры**:

*   Нет.

**Возвращает**:

*   `str`: Уникальный хэш сессии.

**Как работает функция**:

1.  Генерирует UUID (Universally Unique Identifier) с помощью `uuid.uuid4()`.
2.  Преобразует UUID в строку и удаляет все дефисы (`-`).
3.  Возвращает первые 12 символов полученной строки.

**ASCII flowchart**:

```
[Generate UUID] --> [Remove hyphens] --> [Take first 12 chars] --> [Return hash]
```

**Примеры**:

```python
import asyncio
from src.endpoints.gpt4free.g4f.Provider.hf_space.Qwen_Qwen_2_5M import Qwen_Qwen_2_5M
from src.endpoints.gpt4free.g4f.typing import Messages

async def main():
    model = "qwen-2.5-1m-demo"
    messages: Messages = [{"role": "user", "content": "Translate to french: Hello, how are you?"}]
    generator = Qwen_Qwen_2_5M.create_async_generator(model=model, messages=messages)
    async for message in await generator:
        print(message)

if __name__ == "__main__":
    asyncio.run(main())
```

```python
import asyncio
from src.endpoints.gpt4free.g4f.Provider.hf_space.Qwen_Qwen_2_5M import Qwen_Qwen_2_5M
from src.endpoints.gpt4free.g4f.typing import Messages
from src.endpoints.gpt4free.g4f.providers.response import JsonConversation

async def main():
    model = "qwen-2.5-1m-demo"
    messages: Messages = [{"role": "user", "content": "Translate to french: Hello, how are you?"}]
    conversation = JsonConversation(session_hash="1234567890ab")  # Пример хэша сессии
    generator = Qwen_Qwen_2_5M.create_async_generator(model=model, messages=messages, return_conversation=True, conversation=conversation)
    async for message in await generator:
        print(message)

if __name__ == "__main__":
    asyncio.run(main())
```