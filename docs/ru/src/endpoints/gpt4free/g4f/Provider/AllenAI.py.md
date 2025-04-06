# Модуль для работы с AllenAI Playground
## Обзор

Модуль `AllenAI` предоставляет асинхронный интерфейс для взаимодействия с сервисом AllenAI Playground. Он позволяет генерировать текст на основе предоставленных сообщений, используя различные модели, поддерживаемые AllenAI. Модуль поддерживает потоковую передачу ответов и сохранение истории разговоров.

## Подробнее

Модуль предназначен для интеграции с другими частями проекта `hypotez`, где требуется использование AI-моделей для генерации текста. Он предоставляет удобный интерфейс для отправки запросов к AllenAI Playground и получения ответов в асинхронном режиме.

## Классы

### `Conversation`

**Описание**: Класс `Conversation` представляет собой структуру для хранения истории разговора с AI-моделью.

**Наследует**:
- `JsonConversation`: Класс наследует функциональность для сериализации и десериализации истории разговора в формате JSON.

**Атрибуты**:
- `parent` (str, optional): Идентификатор родительского сообщения в истории разговора. По умолчанию `None`.
- `x_anonymous_user_id` (str, optional): Анонимный идентификатор пользователя. Генерируется случайным образом, если не задан.
- `model` (str): Используемая модель AI.
- `messages` (List[dict]): Список сообщений в истории разговора, где каждое сообщение представлено словарем с ключами "role" и "content".

**Методы**:
- `__init__(self, model: str)`: Инициализирует новый экземпляр класса `Conversation`.

### `AllenAI`

**Описание**: Класс `AllenAI` предоставляет асинхронный интерфейс для взаимодействия с сервисом AllenAI Playground.

**Наследует**:
- `AsyncGeneratorProvider`: Класс наследует функциональность для асинхронной генерации данных.
- `ProviderModelMixin`: Класс наследует функциональность для работы с моделями.

**Атрибуты**:
- `label` (str): Метка провайдера, используемая для идентификации ("Ai2 Playground").
- `url` (str): URL сервиса AllenAI Playground ("https://playground.allenai.org").
- `login_url` (str): URL для входа в систему (в данном случае `None`, так как аутентификация не требуется).
- `api_endpoint` (str): URL API для отправки запросов ("https://olmo-api.allen.ai/v4/message/stream").
- `working` (bool): Указывает, работает ли провайдер (в данном случае `True`).
- `needs_auth` (bool): Указывает, требуется ли аутентификация (в данном случае `False`).
- `use_nodriver` (bool): Указывает, используется ли драйвер браузера (в данном случае `False`).
- `supports_stream` (bool): Указывает, поддерживает ли провайдер потоковую передачу данных (в данном случае `True`).
- `supports_system_message` (bool): Указывает, поддерживает ли провайдер системные сообщения (в данном случае `False`).
- `supports_message_history` (bool): Указывает, поддерживает ли провайдер историю сообщений (в данном случае `True`).
- `default_model` (str): Модель, используемая по умолчанию ("tulu3-405b").
- `models` (List[str]): Список поддерживаемых моделей.
- `model_aliases` (Dict[str, str]): Словарь псевдонимов моделей для удобства использования.

**Методы**:
- `create_async_generator(cls, model: str, messages: Messages, proxy: str = None, host: str = "inferd", private: bool = True, top_p: float = None, temperature: float = None, conversation: Conversation = None, return_conversation: bool = False, **kwargs) -> AsyncResult`: Асинхронно генерирует текст на основе предоставленных сообщений, используя указанную модель AllenAI.

## Функции

### `create_async_generator`

```python
@classmethod
async def create_async_generator(
    cls,
    model: str,
    messages: Messages,
    proxy: str = None,
    host: str = "inferd",
    private: bool = True,
    top_p: float = None,
    temperature: float = None,
    conversation: Conversation = None,
    return_conversation: bool = False,
    **kwargs
) -> AsyncResult:
    """
    Асинхронно генерирует текст на основе предоставленных сообщений, используя указанную модель AllenAI.

    Args:
        cls (AllenAI): Класс AllenAI.
        model (str): Модель для использования.
        messages (Messages): Список сообщений для отправки в модель.
        proxy (str, optional): URL прокси-сервера. По умолчанию `None`.
        host (str, optional): Хост для отправки запроса. По умолчанию "inferd".
        private (bool, optional): Указывает, является ли разговор приватным. По умолчанию `True`.
        top_p (float, optional): Параметр top_p для управления случайностью генерации. По умолчанию `None`.
        temperature (float, optional): Параметр temperature для управления случайностью генерации. По умолчанию `None`.
        conversation (Conversation, optional): Объект разговора для сохранения истории. По умолчанию `None`.
        return_conversation (bool, optional): Указывает, следует ли возвращать объект разговора. По умолчанию `False`.
        **kwargs: Дополнительные параметры.

    Returns:
        AsyncResult: Асинхронный генератор текста.

    Raises:
        Exception: Если возникает ошибка при отправке запроса или обработке ответа.
    """
```

**Назначение**: Генерация текста асинхронно на основе предоставленных сообщений с использованием указанной AI-модели AllenAI.

**Параметры**:
- `cls` (AllenAI): Класс AllenAI.
- `model` (str): Модель для использования при генерации ответа.
- `messages` (Messages): Список сообщений для отправки в модель.
- `proxy` (str, optional): URL прокси-сервера для использования при отправке запроса. По умолчанию `None`.
- `host` (str, optional): Хост для отправки запроса. По умолчанию "inferd".
- `private` (bool, optional): Указывает, является ли разговор приватным. По умолчанию `True`.
- `top_p` (float, optional): Параметр top_p для управления случайностью генерации. По умолчанию `None`.
- `temperature` (float, optional): Параметр temperature для управления случайностью генерации. По умолчанию `None`.
- `conversation` (Conversation, optional): Объект разговора для сохранения истории. По умолчанию `None`.
- `return_conversation` (bool, optional): Указывает, следует ли возвращать объект разговора. По умолчанию `False`.
- `**kwargs`: Дополнительные параметры, которые могут быть переданы в функцию.

**Возвращает**:
- `AsyncResult`: Асинхронный генератор текста.

**Вызывает исключения**:
- `Exception`: Если возникает ошибка при отправке запроса или обработке ответа.

**Как работает функция**:

1.  **Подготовка промпта**: Функция подготавливает промт для отправки в модель. Если объект `conversation` не передан, формируется полный промт из всех сообщений. В противном случае используется только последнее сообщение пользователя.
2.  **Инициализация/обновление разговора**: Если объект `conversation` не передан, создается новый экземпляр класса `Conversation`.
3.  **Генерация разделителя**: Генерируется уникальный разделитель для формирования multipart/form-data запроса.
4.  **Формирование заголовков**: Формируются заголовки запроса, включая Content-Type с уникальным разделителем, User-Agent и идентификатор пользователя.
5.  **Формирование тела запроса**: Формируется тело запроса в формате multipart/form-data, включающее модель, хост, контент (промт), флаг приватности и, при наличии, идентификатор родительского сообщения, параметры temperature и top_p.
6.  **Отправка запроса**: Отправляется POST-запрос к API AllenAI с использованием `aiohttp.ClientSession`.
7.  **Обработка потока ответов**: Полученный ответ обрабатывается по частям (chunks). Каждая часть декодируется, разделяется на строки, и каждая строка парсится как JSON.
8.  **Извлечение контента**: Из JSON-ответа извлекается контент, сгенерированный ассистентом.
9.  **Обработка завершения**: При получении финального сообщения или при достижении `finish_reason == "stop"`, извлекается идентификатор родительского сообщения, добавляется сообщение в историю разговора и, если требуется, возвращается объект разговора.

```
    Начало
    │
    ├───> Форматирование промпта (format_prompt или get_last_user_message)
    │
    ├───> Создание/обновление объекта Conversation
    │
    ├───> Генерация уникального boundary
    │
    ├───> Формирование заголовков запроса
    │
    ├───> Формирование тела запроса (multipart/form-data)
    │
    ├───> Отправка POST-запроса к API AllenAI
    │
    ├───> Обработка потока ответов (chunks)
    │   │
    │   └───> Декодирование и разделение на строки
    │   │
    │   └───> Парсинг JSON
    │   │
    │   └───> Извлечение контента ассистента
    │   │
    │   └───> Обработка завершения (final или finish_reason == "stop")
    │
    └───> Конец
```

**Примеры**:

```python
# Пример использования функции create_async_generator
import asyncio
from typing import AsyncGenerator, List, Dict

async def main():
    model = "tulu3-405b"
    messages: List[Dict[str, str]] = [
        {"role": "user", "content": "Hello, AllenAI!"}
    ]

    async def print_response(generator: AsyncGenerator[str, None]):
        async for chunk in generator:
            print(chunk, end="")

    response_generator = AllenAI.create_async_generator(model=model, messages=messages)
    await print_response(await response_generator)

if __name__ == "__main__":
    asyncio.run(main())
```

```python
# Пример использования с conversation
import asyncio
from typing import AsyncGenerator, List, Dict
from src.endpoints.gpt4free.g4f.Provider.AllenAI import Conversation

async def main():
    model = "tulu3-405b"
    messages: List[Dict[str, str]] = [
        {"role": "user", "content": "Hello, AllenAI!"}
    ]
    conversation = Conversation(model=model)

    async def print_response(generator: AsyncGenerator[str, None]):
        async for chunk in generator:
            print(chunk, end="")

    response_generator = AllenAI.create_async_generator(model=model, messages=messages, conversation=conversation, return_conversation=True)
    await print_response(await response_generator)

if __name__ == "__main__":
    asyncio.run(main())