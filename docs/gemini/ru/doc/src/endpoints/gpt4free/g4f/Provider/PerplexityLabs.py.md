# Модуль для работы с Perplexity Labs API
## Обзор

Модуль `PerplexityLabs` предоставляет асинхронный интерфейс для взаимодействия с API Perplexity Labs. Он позволяет отправлять сообщения и получать ответы от различных моделей, предоставляемых Perplexity Labs, таких как `r1-1776`, `sonar-pro`, `sonar` и другие. Модуль использует вебсокеты для потоковой передачи данных, что позволяет получать ответы в режиме реального времени.

## Подробнее

Этот модуль является частью проекта `hypotez` и предназначен для интеграции с другими компонентами, требующими взаимодействия с AI-моделями Perplexity Labs. Он предоставляет удобный способ отправки запросов и обработки ответов в асинхронном режиме.

## Классы

### `PerplexityLabs`

**Описание**: Класс `PerplexityLabs` является асинхронным генератором, который позволяет взаимодействовать с API Perplexity Labs.

**Наследует**:
- `AsyncGeneratorProvider`: Обеспечивает базовую функциональность для асинхронных генераторов.
- `ProviderModelMixin`: Предоставляет методы для работы с моделями.

**Атрибуты**:
- `url` (str): URL главной страницы Perplexity Labs.
- `working` (bool): Указывает, работает ли провайдер.
- `default_model` (str): Модель, используемая по умолчанию (`r1-1776`).
- `models` (List[str]): Список поддерживаемых моделей.

**Методы**:
- `create_async_generator()`: Создает асинхронный генератор для получения ответов от API Perplexity Labs.

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
    Создает асинхронный генератор для взаимодействия с API Perplexity Labs.

    Args:
        cls: Класс, для которого вызывается метод.
        model (str): Имя используемой модели.
        messages (Messages): Список сообщений для отправки.
        proxy (str, optional): Прокси-сервер для использования. По умолчанию `None`.
        **kwargs: Дополнительные параметры.

    Returns:
        AsyncResult: Асинхронный генератор, возвращающий ответы от API Perplexity Labs.

    Raises:
        ResponseError: Если возникает ошибка при получении ответа от API.
        RuntimeError: Если возникает неизвестная ошибка.

    """
```

**Назначение**: Функция `create_async_generator` создает и возвращает асинхронный генератор, который отправляет сообщения в API Perplexity Labs и возвращает ответы.

**Параметры**:
- `cls`: Ссылка на класс `PerplexityLabs`.
- `model` (str): Имя модели, которую нужно использовать для генерации ответа.
- `messages` (Messages): Список сообщений, которые нужно отправить в API.
- `proxy` (str, optional): Адрес прокси-сервера, если необходимо использовать прокси для подключения к API. По умолчанию `None`.
- `**kwargs`: Дополнительные параметры, которые могут быть переданы в API.

**Возвращает**:
- `AsyncResult`: Асинхронный генератор, который выдает части ответа от API Perplexity Labs.

**Вызывает исключения**:
- `ResponseError`: Если возникает ошибка при обработке ответа от API.
- `RuntimeError`: Если возникает неизвестная ошибка во время обмена сообщениями с сервером.

**Как работает функция**:

1. **Инициализация**:
   - Устанавливаются заголовки запроса, включая `Origin` и `Referer`.
   - Открывается асинхронная сессия с использованием `StreamSession` для поддержки потоковой передачи данных.

2. **Получение SID (Session ID)**:
   - Отправляется GET-запрос к API для получения идентификатора сессии (SID).
   - Проверяется, что ответ начинается с "0", и извлекается SID из JSON-ответа.

3. **Аутентификация**:
   - Отправляется POST-запрос для аутентификации с использованием JWT.
   - Проверяется, что ответ равен "OK".

4. **Подключение к WebSocket**:
   - Устанавливается WebSocket-соединение с сервером Perplexity Labs.
   - Отправляются probe-сообщения для установления соединения.

5. **Отправка сообщений и получение ответов**:
   - Формируется JSON-сообщение с данными для отправки, включая версию, источник, модель и список сообщений.
   - Отправляется сообщение через WebSocket.
   - В цикле ожидаются ответы от сервера.
   - Обрабатываются различные типы сообщений:
     - "2": Отправляется ответное сообщение "3".
     - Данные с ответом: Извлекаются данные из JSON, и извлекается полезная нагрузка `data["output"][last_message:]`.
     - Если `data["final"]` равно `True`, извлекаются цитаты (`data["citations"]`), и генератор завершается.

6. **Обработка ошибок**:
   - Если происходит ошибка при обработке сообщения, выбрасывается исключение `ResponseError`.
   - Если происходит неизвестная ошибка, выбрасывается исключение `RuntimeError`.

**ASCII Flowchart**:

```
Начало
  ↓
Установка заголовков и открытие сессии
  ↓
Получение SID через GET-запрос
  ↓
Аутентификация через POST-запрос
  ↓
Установка WebSocket-соединения
  ↓
Отправка probe-сообщений
  ↓
Отправка данных сообщений через WebSocket
  ↓
Начало цикла получения ответов
  ↓
Получение сообщения
  ↓
Обработка сообщения:
  ├── "2" -> Отправка "3"
  └── Данные -> Извлечение данных и выдача ответа
  ↓
Проверка data["final"]
  ├── True -> Извлечение цитат и завершение
  └── False -> Продолжение цикла
  ↓
Обработка ошибок (ResponseError, RuntimeError)
  ↓
Конец
```

**Примеры**:

```python
import asyncio
from src.endpoints.gpt4free.g4f.Provider.PerplexityLabs import PerplexityLabs
from src.endpoints.gpt4free.g4f.typing import Messages

async def main():
    model = "r1-1776"
    messages: Messages = [{"role": "user", "content": "Hello, how are you?"}]

    async for message in PerplexityLabs.create_async_generator(model=model, messages=messages):
        print(message, end="")

if __name__ == "__main__":
    asyncio.run(main())
```
```python
import asyncio
from src.endpoints.gpt4free.g4f.Provider.PerplexityLabs import PerplexityLabs
from src.endpoints.gpt4free.g4f.typing import Messages

async def main():
    model = "sonar-pro"
    messages: Messages = [{"role": "user", "content": "Tell me a joke"}]

    async for message in PerplexityLabs.create_async_generator(model=model, messages=messages):
        print(message, end="")

if __name__ == "__main__":
    asyncio.run(main())
```
```python
import asyncio
from src.endpoints.gpt4free.g4f.Provider.PerplexityLabs import PerplexityLabs
from src.endpoints.gpt4free.g4f.typing import Messages

async def main():
    model = "sonar"
    messages: Messages = [{"role": "user", "content": "Write a short poem about the sea"}]

    async for message in PerplexityLabs.create_async_generator(model=model, messages=messages):
        print(message, end="")

if __name__ == "__main__":
    asyncio.run(main())
```
```python
import asyncio
from src.endpoints.gpt4free.g4f.Provider.PerplexityLabs import PerplexityLabs
from src.endpoints.gpt4free.g4f.typing import Messages

async def main():
    model = "sonar-reasoning"
    messages: Messages = [{"role": "user", "content": "What is the capital of France?"}]

    async for message in PerplexityLabs.create_async_generator(model=model, messages=messages):
        print(message, end="")

if __name__ == "__main__":
    asyncio.run(main())
```
```python
import asyncio
from src.endpoints.gpt4free.g4f.Provider.PerplexityLabs import PerplexityLabs
from src.endpoints.gpt4free.g4f.typing import Messages

async def main():
    model = "sonar-reasoning-pro"
    messages: Messages = [{"role": "user", "content": "Explain the theory of relativity"}]

    async for message in PerplexityLabs.create_async_generator(model=model, messages=messages):
        print(message, end="")

if __name__ == "__main__":
    asyncio.run(main())