# Модуль `FlowGpt.py`

## Обзор

Модуль предоставляет асинхронтный генератор для взаимодействия с FlowGPT. Он позволяет использовать различные модели, такие как `gpt-3.5-turbo`, `gpt-4-turbo` и другие, через асинхронные запросы. Поддерживает историю сообщений и системные сообщения.

## Подробней

Модуль предназначен для интеграции с FlowGPT для генерации текста на основе предоставленных сообщений и параметров модели. Он использует `aiohttp` для выполнения асинхронных запросов и предоставляет результаты в виде асинхронного генератора.

## Классы

### `FlowGpt`

**Описание**: Класс `FlowGpt` предоставляет функциональность для взаимодействия с FlowGPT. Он наследует `AsyncGeneratorProvider` и `ProviderModelMixin`, что позволяет ему использовать асинхронные генераторы и управлять моделями.

**Наследует**:
- `AsyncGeneratorProvider`: Обеспечивает базовую функциональность для асинхронных генераторов.
- `ProviderModelMixin`: Предоставляет методы для управления моделями.

**Атрибуты**:
- `url` (str): URL для взаимодействия с FlowGPT (`https://flowgpt.com/chat`).
- `working` (bool): Указывает, работает ли провайдер (по умолчанию `False`).
- `supports_message_history` (bool): Указывает, поддерживает ли провайдер историю сообщений (по умолчанию `True`).
- `supports_system_message` (bool): Указывает, поддерживает ли провайдер системные сообщения (по умолчанию `True`).
- `default_model` (str): Модель, используемая по умолчанию (`gpt-3.5-turbo`).
- `models` (List[str]): Список поддерживаемых моделей.
- `model_aliases` (Dict[str, str]): Алиасы для моделей (например, `"gemini": "google-gemini"`).

**Методы**:
- `create_async_generator`: Создает асинхронный генератор для получения ответов от FlowGPT.

## Функции

### `create_async_generator`

```python
@classmethod
async def create_async_generator(
    cls,
    model: str,
    messages: Messages,
    proxy: str = None,
    temperature: float = 0.7,
    **kwargs
) -> AsyncResult:
    """
    Создает асинхронный генератор для получения ответов от FlowGPT.

    Args:
        cls (FlowGpt): Класс FlowGpt.
        model (str): Название модели для использования.
        messages (Messages): Список сообщений для отправки.
        proxy (str, optional): URL прокси-сервера. По умолчанию `None`.
        temperature (float, optional): Температура генерации. По умолчанию `0.7`.
        **kwargs: Дополнительные аргументы.

    Returns:
        AsyncResult: Асинхронный генератор, выдающий ответы от FlowGPT.
    """
```

**Назначение**:
Создает и возвращает асинхронный генератор, который взаимодействует с FlowGPT для получения ответов на основе предоставленных сообщений и параметров модели.

**Параметры**:
- `cls`: Ссылка на класс `FlowGpt`.
- `model` (str): Имя модели, которую необходимо использовать для генерации ответа. Если указана модель с алиасом, происходит преобразование к полному названию модели.
- `messages (Messages)`: Список сообщений, отправляемых в FlowGPT. Каждое сообщение содержит роль (`user`, `assistant`, `system`) и содержимое (`content`).
- `proxy (str, optional)`: URL прокси-сервера, который будет использоваться для подключения к FlowGPT. По умолчанию `None`.
- `temperature (float, optional)`: Параметр, определяющий случайность генерации ответа. Значение по умолчанию: `0.7`. Чем выше температура, тем более случайным будет ответ.
- `**kwargs`: Дополнительные параметры, которые можно передать в функцию.

**Возвращает**:
- `AsyncResult`: Асинхронный генератор, который предоставляет ответы от FlowGPT. Генератор выдает фрагменты текста по мере их поступления от сервера.

**Как работает функция**:
1. **Подготовка параметров**:
   - Получает имя модели и преобразует его, если используется алиас.
   - Генерирует значения `timestamp`, `nonce` и `signature`, необходимые для аутентификации.

2. **Формирование заголовков**:
   - Создает словарь `headers` с необходимыми HTTP-заголовками, включая User-Agent, Referer, Content-Type и параметры аутентификации (`x-nonce`, `x-signature`, `x-timestamp`).

3. **Подготовка данных для запроса**:
   - Извлекает историю сообщений (все сообщения, кроме последнего и системных).
   - Формирует системное сообщение, объединяя содержимое всех сообщений с ролью `system`. Если системные сообщения отсутствуют, устанавливается сообщение по умолчанию.
   - Создает словарь `data` с данными для отправки, включая модель, вопрос (последнее сообщение), историю сообщений, системное сообщение, температуру и другие параметры.

4. **Отправка запроса и обработка ответа**:
   - Открывает асинхронную сессию с использованием `aiohttp.ClientSession` и отправляет POST-запрос к API FlowGPT (`https://prod-backend-k8s.flowgpt.com/v3/chat-anonymous`) с данными и заголовками.
   - Обрабатывает ответ от сервера по частям (chunks). Для каждой части:
     - Удаляет пробелы.
     - Преобразует JSON в объект Python.
     - Проверяет наличие события (`event`).
     - Если событие равно `text`, выдает данные (`data`) из сообщения.

```
    Начало
    ↓
    model = cls.get_model(model) - Получение имени модели
    ↓
    Генерация timestamp, nonce, signature
    ↓
    Формирование headers
    ↓
    history = [message ...] - Извлечение истории сообщений
    ↓
    system_message = "\\n".join(...) - Формирование системного сообщения
    ↓
    data = { ... } - Формирование данных для запроса
    ↓
    POST-запрос к FlowGPT
    ↓
    Обработка ответа по частям
    ↓
    Выдача данных из сообщения (если event == "text")
    ↓
    Конец
```

**Примеры**:

```python
# Пример вызова функции create_async_generator
import asyncio
from typing import AsyncGenerator, List, Dict

async def main():
    model = "gpt-3.5-turbo"
    messages: List[Dict[str, str]] = [
        {"role": "user", "content": "Hello, how are you?"}
    ]
    
    generator: AsyncGenerator[str, None] = await FlowGpt.create_async_generator(model=model, messages=messages)
    
    async for message in generator:
        print(message, end="")

if __name__ == "__main__":
    asyncio.run(main())
```
```python
# Пример с использованием прокси
import asyncio
from typing import AsyncGenerator, List, Dict

async def main():
    model = "gpt-4-turbo"
    messages: List[Dict[str, str]] = [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "What is the capital of France?"}
    ]
    proxy = "http://your_proxy_url:your_proxy_port"
    
    generator: AsyncGenerator[str, None] = await FlowGpt.create_async_generator(model=model, messages=messages, proxy=proxy)
    
    async for message in generator:
        print(message, end="")

if __name__ == "__main__":
    asyncio.run(main())
```
```python
# Пример с изменением температуры
import asyncio
from typing import AsyncGenerator, List, Dict

async def main():
    model = "google-gemini"
    messages: List[Dict[str, str]] = [
        {"role": "user", "content": "Tell me a joke."}
    ]
    temperature = 0.9
    
    generator: AsyncGenerator[str, None] = await FlowGpt.create_async_generator(model=model, messages=messages, temperature=temperature)
    
    async for message in generator:
        print(message, end="")

if __name__ == "__main__":
    asyncio.run(main())