# Модуль CablyAI

## Обзор

Модуль `CablyAI` представляет собой реализацию класса `OpenaiTemplate` для взаимодействия с моделью CablyAI. Он определяет URL, базовый API, требования к аутентификации и поддержку потоковой передачи данных. Этот модуль предназначен для использования в проекте `hypotez` для обеспечения взаимодействия с CablyAI.

## Подробней

Модуль `CablyAI` используется для подключения к сервису CablyAI, который предоставляет доступ к языковым моделям через API. Он расширяет возможности `OpenaiTemplate`, добавляя специфичные для CablyAI параметры, такие как URL и заголовки запросов. Это позволяет унифицировать процесс взаимодействия с различными поставщиками AI-моделей в рамках проекта `hypotez`.

## Классы

### `CablyAI`

**Описание**: Класс `CablyAI` представляет собой шаблон для взаимодействия с API CablyAI.

**Наследует**:
- `OpenaiTemplate`: Класс наследует функциональность `OpenaiTemplate`, предоставляя базовые методы для работы с API OpenAI-подобных моделей.

**Атрибуты**:
- `url` (str): URL для взаимодействия с CablyAI (`"https://cablyai.com/chat"`).
- `login_url` (str): URL для аутентификации на CablyAI (`"https://cablyai.com"`).
- `api_base` (str): Базовый URL для API CablyAI (`"https://cablyai.com/v1"`).
- `working` (bool): Указывает, что модель CablyAI в рабочем состоянии (`True`).
- `needs_auth` (bool): Указывает, что для доступа к CablyAI требуется аутентификация (`True`).
- `supports_stream` (bool): Указывает, что CablyAI поддерживает потоковую передачу данных (`True`).
- `supports_system_message` (bool): Указывает, что CablyAI поддерживает системные сообщения (`True`).
- `supports_message_history` (bool): Указывает, что CablyAI поддерживает историю сообщений (`True`).

**Методы**:
- `create_async_generator`: Создает асинхронный генератор для взаимодействия с API CablyAI.

## Функции

### `create_async_generator`

```python
@classmethod
def create_async_generator(
    cls,
    model: str,
    messages: Messages,
    api_key: str = None,
    stream: bool = False,
    **kwargs
) -> AsyncResult:
    """
    Создает асинхронный генератор для взаимодействия с API CablyAI.

    Args:
        cls: Класс, для которого вызывается метод.
        model (str): Название модели, которую необходимо использовать.
        messages (Messages): Список сообщений для отправки в API.
        api_key (str, optional): API-ключ для аутентификации. По умолчанию `None`.
        stream (bool, optional): Флаг, указывающий, использовать ли потоковую передачу данных. По умолчанию `False`.
        **kwargs: Дополнительные аргументы, которые будут переданы в базовый метод.

    Returns:
        AsyncResult: Асинхронный генератор для получения ответов от API.

    Raises:
        ModelNotSupportedError: Если указанная модель не поддерживается.

    """
```

**Назначение**: Создает асинхронный генератор для взаимодействия с API CablyAI.

**Параметры**:
- `cls`: Класс, для которого вызывается метод.
- `model` (str): Название модели, которую необходимо использовать.
- `messages` (`Messages`): Список сообщений для отправки в API.
- `api_key` (str, optional): API-ключ для аутентификации. По умолчанию `None`.
- `stream` (bool, optional): Флаг, указывающий, использовать ли потоковую передачу данных. По умолчанию `False`.
- `**kwargs`: Дополнительные аргументы, которые будут переданы в базовый метод.

**Возвращает**:
- `AsyncResult`: Асинхронный генератор для получения ответов от API.

**Вызывает исключения**:
- `ModelNotSupportedError`: Если указанная модель не поддерживается.

**Как работает функция**:

1.  **Определение заголовков**: Функция определяет заголовки, необходимые для запроса к API CablyAI. Заголовки включают `Accept`, `Accept-Language`, `Authorization` (с использованием переданного `api_key`), `Content-Type`, `Origin`, `Referer` и `User-Agent`.

2.  **Вызов базового метода**: Функция вызывает метод `create_async_generator` из базового класса (`super()`) с передачей модели, сообщений, API-ключа, флага потоковой передачи и заголовков.

3.  **Возврат результата**: Функция возвращает результат вызова базового метода, который является асинхронным генератором для получения ответов от API.

**ASCII схема работы функции**:

```
Определение заголовков --> Вызов super().create_async_generator() --> Возврат AsyncResult
```

**Примеры**:

```python
# Пример вызова функции create_async_generator
from typing import List, Dict, AsyncGenerator, Any, Optional
from g4f.models import Model

class Messages:
    def __init__(self, messages: List[Dict[str, str]]):
        self.messages = messages

    def __iter__(self):
        return iter(self.messages)

    def __len__(self):
        return len(self.messages)

class AsyncResult:
    def __init__(self, generator: AsyncGenerator[str, None]):
        self.generator = generator

    async def __aiter__(self):
        return self.generator.__aiter__()
        
    async def __anext__(self):
        try:
            return await self.generator.__anext__()
        except StopAsyncIteration:
            raise StopAsyncIteration

async def example():
    model = "gpt-3.5-turbo"
    messages = Messages([{"role": "user", "content": "Hello, CablyAI!"}])
    api_key = "YOUR_API_KEY"  # Замените на ваш реальный API-ключ

    # Вызов create_async_generator
    result = CablyAI.create_async_generator(model=model, messages=messages, api_key=api_key, stream=True)

    # Пример использования асинхронного генератора
    async for response in result:
        print(response)

# Запуск примера
# import asyncio
# asyncio.run(example())