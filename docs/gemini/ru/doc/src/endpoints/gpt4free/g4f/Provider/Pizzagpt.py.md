# Модуль Pizzagpt

## Обзор

Модуль `Pizzagpt` предназначен для взаимодействия с API сервиса pizzagpt.it. Он предоставляет асинхронный генератор, который отправляет запросы к API и возвращает ответы в виде текста. Этот модуль использует `aiohttp` для асинхронных HTTP-запросов и наследуется от `AsyncGeneratorProvider` и `ProviderModelMixin`.

## Подробней

Модуль позволяет отправлять текстовые запросы к API pizzagpt.it и получать ответы, имитируя поведение пользователя в браузере. Он включает в себя обработку ошибок и форматирование запросов для обеспечения совместимости с API. `Pizzagpt` используется для получения ответов от языковой модели, предоставляемой pizzagpt.it, и может быть интегрирован в другие части проекта `hypotez`, где требуется взаимодействие с этой моделью.

## Классы

### `Pizzagpt`

**Описание**: Класс `Pizzagpt` является асинхронным провайдером, который взаимодействует с API pizzagpt.it для генерации текста на основе предоставленных сообщений.

**Наследует**:
- `AsyncGeneratorProvider`: Обеспечивает базовую структуру для асинхронных генераторов.
- `ProviderModelMixin`: Предоставляет функциональность для работы с моделями.

**Атрибуты**:
- `url` (str): Базовый URL сервиса pizzagpt.it.
- `api_endpoint` (str): Конечная точка API для отправки запросов.
- `working` (bool): Флаг, указывающий на работоспособность провайдера (в данном случае `False`).
- `default_model` (str): Модель, используемая по умолчанию (`gpt-4o-mini`).
- `models` (List[str]): Список поддерживаемых моделей (содержит только `default_model`).

**Методы**:
- `create_async_generator`: Создает асинхронный генератор для получения ответов от API.

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
        Создает асинхронный генератор для взаимодействия с API pizzagpt.it.

        Args:
            model (str): Модель, используемая для генерации ответа.
            messages (Messages): Список сообщений для отправки в запросе.
            proxy (str, optional): URL прокси-сервера для использования. По умолчанию `None`.
            **kwargs: Дополнительные аргументы.

        Returns:
            AsyncResult: Асинхронный генератор, возвращающий текст ответа.

        Raises:
            ValueError: Если в ответе содержится сообщение о злоупотреблении.
            aiohttp.ClientResponseError: Если HTTP-запрос завершается с ошибкой.

        """
```

**Назначение**: Функция `create_async_generator` создает и возвращает асинхронный генератор, который отправляет запросы к API pizzagpt.it и возвращает ответы.

**Параметры**:
- `model` (str): Модель, используемая для генерации ответа.
- `messages` (Messages): Список сообщений для отправки в запросе.
- `proxy` (str, optional): URL прокси-сервера для использования. По умолчанию `None`.
- `**kwargs`: Дополнительные аргументы.

**Возвращает**:
- `AsyncResult`: Асинхронный генератор, возвращающий текст ответа.

**Вызывает исключения**:
- `ValueError`: Если в ответе содержится сообщение о злоупотреблении.
- `aiohttp.ClientResponseError`: Если HTTP-запрос завершается с ошибкой.

**Как работает функция**:

1. **Подготовка заголовков**: Функция создает заголовки HTTP-запроса, включая информацию о типе контента, User-Agent и секретный ключ `x-secret`.
2. **Создание сессии**: Используется `aiohttp.ClientSession` для управления HTTP-соединением.
3. **Форматирование запроса**: Список сообщений `messages` форматируется в строку `prompt` с использованием функции `format_prompt`.
4. **Отправка запроса**: Отправляется POST-запрос к API pizzagpt.it с использованием `session.post`. В теле запроса передается `prompt` в формате JSON.
5. **Обработка ответа**: Функция проверяет статус ответа и преобразует JSON-ответ в словарь. Извлекается содержимое ответа из ключа `answer.content`.
6. **Генерация результата**: Если содержимое присутствует, функция проверяет наличие сообщения о злоупотреблении. Если такого сообщения нет, функция генерирует текст ответа и признак завершения (`FinishReason("stop")`).
7. **Обработка ошибок**: Если возникает HTTP-ошибка, она обрабатывается с помощью `response.raise_for_status()`.

**ASCII Flowchart**:

```
A [Подготовка заголовков]
|
B [Создание сессии aiohttp.ClientSession]
|
C [Форматирование запроса format_prompt(messages)]
|
D [Отправка POST-запроса к API]
|
E [Обработка ответа JSON]
|
F [Извлечение содержимого ответа content]
|
G [Проверка на сообщение о злоупотреблении]
|
H [Генерация текста ответа и FinishReason]
```

**Примеры**:

```python
import asyncio
from typing import AsyncGenerator, List, Dict

from src.endpoints.gpt4free.g4f.Provider.Pizzagpt import Pizzagpt
from src.endpoints.gpt4free.g4f.typing import Messages

async def main():
    model = "gpt-4o-mini"
    messages: Messages = [{"role": "user", "content": "Привет, как дела?"}]
    proxy = None

    generator: AsyncGenerator = Pizzagpt.create_async_generator(model=model, messages=messages, proxy=proxy)
    async for message in generator:
        print(message)

if __name__ == "__main__":
    asyncio.run(main())
```

```python
import asyncio
from typing import AsyncGenerator, List, Dict

from src.endpoints.gpt4free.g4f.Provider.Pizzagpt import Pizzagpt
from src.endpoints.gpt4free.g4f.typing import Messages

async def main():
    model = "gpt-4o-mini"
    messages: Messages = [{"role": "user", "content": "Напиши небольшое стихотворение."}]
    proxy = "http://your_proxy:8080"  # Замените на ваш прокси-сервер

    generator: AsyncGenerator = Pizzagpt.create_async_generator(model=model, messages=messages, proxy=proxy)
    async for message in generator:
        print(message)

if __name__ == "__main__":
    asyncio.run(main())