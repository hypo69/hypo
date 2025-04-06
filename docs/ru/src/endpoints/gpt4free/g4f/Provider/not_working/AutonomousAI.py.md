# Модуль для работы с AutonomousAI
====================================

Модуль предоставляет класс `AutonomousAI`, который является асинхронным генератором для взаимодействия с API AutonomousAI.
Он поддерживает потоковую передачу сообщений и предоставляет методы для отправки запросов к различным моделям,
таким как llama, qwen_coder, hermes, vision и summary.

## Обзор

Модуль `AutonomousAI` предназначен для асинхронного взаимодействия с API AutonomousAI. Он включает в себя:

- Поддержку потоковой передачи данных.
- Поддержку системных сообщений.
- Поддержку истории сообщений.
- Возможность выбора различных моделей AI.

## Подробнее

Этот модуль позволяет отправлять запросы к API AutonomousAI для получения ответов от различных моделей искусственного интеллекта.
Он использует библиотеку `aiohttp` для выполнения асинхронных HTTP-запросов.
Кодирует сообщения в формате JSON и base64 для передачи в API.
Поддерживает потоковую передачу ответов от сервера.

## Классы

### `AutonomousAI`

**Описание**: Класс для взаимодействия с API AutonomousAI. Явлется асинхронным генератором.

**Наследует**:
- `AsyncGeneratorProvider`: Обеспечивает базовую функциональность для асинхронных генераторов.
- `ProviderModelMixin`: Предоставляет функциональность для работы с моделями.

**Аттрибуты**:
- `url` (str): URL для AutonomousAI.
- `api_endpoints` (dict): Словарь с конечными точками API для различных моделей.
- `working` (bool): Флаг, указывающий, работает ли провайдер.
- `supports_stream` (bool): Флаг, указывающий, поддерживает ли провайдер потоковую передачу.
- `supports_system_message` (bool): Флаг, указывающий, поддерживает ли провайдер системные сообщения.
- `supports_message_history` (bool): Флаг, указывающий, поддерживает ли провайдер историю сообщений.
- `default_model` (str): Модель, используемая по умолчанию.
- `models` (list): Список поддерживаемых моделей.
- `model_aliases` (dict): Словарь псевдонимов моделей.

### `AutonomousAI.create_async_generator`

```python
@classmethod
async def create_async_generator(
    cls,
    model: str,
    messages: Messages,
    proxy: str = None,
    stream: bool = False,
    **kwargs
) -> AsyncResult:
    """
    Создает асинхронный генератор для взаимодействия с API AutonomousAI.

    Args:
        model (str): Название модели для использования.
        messages (Messages): Список сообщений для отправки.
        proxy (str, optional): Адрес прокси-сервера. По умолчанию `None`.
        stream (bool, optional): Флаг, указывающий, использовать ли потоковую передачу. По умолчанию `False`.
        **kwargs: Дополнительные аргументы.

    Returns:
        AsyncResult: Асинхронный генератор, выдающий ответы от API.

    Raises:
        Exception: В случае ошибки при взаимодействии с API.
    """
```

**Назначение**: Создает асинхронный генератор для взаимодействия с API AutonomousAI.

**Параметры**:
- `cls` (class): Ссылка на класс `AutonomousAI`.
- `model` (str): Название модели для использования.
- `messages` (Messages): Список сообщений для отправки.
- `proxy` (str, optional): Адрес прокси-сервера. По умолчанию `None`.
- `stream` (bool, optional): Флаг, указывающий, использовать ли потоковую передачу. По умолчанию `False`.
- `**kwargs`: Дополнительные аргументы.

**Возвращает**:
- `AsyncResult`: Асинхронный генератор, выдающий ответы от API.

**Вызывает исключения**:
- `Exception`: В случае ошибки при взаимодействии с API.

**Как работает функция**:

1. **Определение конечной точки API**: Определяется конечная точка API на основе выбранной модели (`api_endpoint = cls.api_endpoints[model]`).
2. **Формирование заголовков**: Формируются заголовки HTTP-запроса (`headers`).
3. **Асинхронный HTTP-запрос**:
   - Открывается асинхронная сессия с использованием `aiohttp.ClientSession`.
   - Кодируются сообщения в JSON и base64 (`message_json`, `encoded_message`).
   - Формируются данные для отправки (`data`).
   - Отправляется POST-запрос к API (`session.post`).
   - Обрабатывается ответ от сервера по частям (`response.content`).
   - Декодируются и анализируются полученные чанки данных.
   - Извлекается содержимое (`delta["content"]`) и причина завершения (`finish_reason`) из JSON-ответа.
   - Генерируются результаты с использованием `yield`.
4. **Обработка ошибок JSON**: Если происходит ошибка при декодировании JSON, она игнорируется.

**ASCII схема работы функции**:

```
Определение api_endpoint
│
Формирование заголовков headers
│
Создание асинхронной сессии ClientSession
│
Кодирование messages в JSON и base64 (message_json, encoded_message)
│
Формирование данных запроса data
│
Отправка POST-запроса в api_endpoint
│
Обработка ответа по частям (response.content)
│
Декодирование чанков (chunk.decode())
│
Проверка на "data: [DONE]"
│
Декодирование JSON (json.loads)
│
Извлечение delta["content"] и finish_reason
│
Генерация результатов (yield)
│
Обработка ошибок JSONDecodeError
```

**Примеры**:

```python
import asyncio
from typing import AsyncGenerator, List

# Для того, чтобы примеры заработали, нужно убрать AsyncGenerator и List из typing
# так как они уже импортированы в файле

# Пример 1: Использование create_async_generator с минимальными параметрами
async def example_1():
    model = "llama"
    messages = [{"role": "user", "content": "Hello, world!"}]
    generator = AutonomousAI.create_async_generator(model=model, messages=messages)
    async for item in generator:
        print(item, end="")

# Пример 2: Использование create_async_generator с прокси и потоковой передачей
async def example_2():
    model = "llama"
    messages = [{"role": "user", "content": "Tell me a story."}]
    proxy = "http://your_proxy:8080"
    generator = AutonomousAI.create_async_generator(model=model, messages=messages, proxy=proxy, stream=True)
    async for item in generator:
        print(item, end="")

# Пример 3: Использование create_async_generator с различными моделями
async def example_3():
    models = ["llama", "qwen_coder", "hermes"]
    messages = [{"role": "user", "content": "Write a short code snippet."}]
    for model in models:
        print(f"Model: {model}")
        generator = AutonomousAI.create_async_generator(model=model, messages=messages)
        async for item in generator:
            print(item, end="")
        print("\n---")

# Запуск примеров (необходимо запустить в асинхронном контексте)
# asyncio.run(example_1())
# asyncio.run(example_2())
# asyncio.run(example_3())
```