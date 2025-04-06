# Модуль Pizzagpt

## Обзор

Модуль `Pizzagpt` предоставляет асинхронный генератор для взаимодействия с API pizzagpt.it. Он позволяет отправлять запросы к API и получать ответы в виде асинхронного генератора текста.

## Подробней

Этот модуль предназначен для интеграции с сервисом pizzagpt.it, предоставляющим API для генерации текста. Он использует асинхронные запросы для взаимодействия с API и возвращает результаты в виде генератора, что позволяет эффективно обрабатывать большие объемы данных. Модуль также обрабатывает возможные ошибки, возвращаемые API, и предоставляет информацию о причине завершения генерации.

## Классы

### `Pizzagpt`

**Описание**: Класс `Pizzagpt` является асинхронным провайдером и миксином моделей. Он наследует от `AsyncGeneratorProvider` и `ProviderModelMixin`.

**Наследует**:
- `AsyncGeneratorProvider`: Обеспечивает асинхронную генерацию данных.
- `ProviderModelMixin`: Предоставляет функциональность для работы с моделями.

**Атрибуты**:
- `url` (str): URL сервиса pizzagpt.it.
- `api_endpoint` (str): Endpoint API для отправки запросов.
- `working` (bool): Указывает, работает ли провайдер в данный момент.
- `default_model` (str): Модель, используемая по умолчанию (`gpt-4o-mini`).
- `models` (list[str]): Список поддерживаемых моделей.

**Методы**:
- `create_async_generator()`: Создает асинхронный генератор для получения ответов от API.

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
    Создает асинхронный генератор для получения ответов от API pizzagpt.it.

    Args:
        model (str): Модель для использования.
        messages (Messages): Список сообщений для отправки в API.
        proxy (str, optional): Прокси-сервер для использования. По умолчанию `None`.
        **kwargs: Дополнительные аргументы.

    Returns:
        AsyncResult: Асинхронный генератор, возвращающий текст от API.

    Raises:
        ValueError: Если API возвращает сообщение об обнаружении злоупотребления.

    """
```

**Назначение**:
Функция `create_async_generator` создает асинхронный генератор, который взаимодействует с API pizzagpt.it для получения ответов на основе предоставленных сообщений. Она отправляет POST-запрос к API и возвращает текст ответа в виде асинхронного генератора.

**Параметры**:
- `cls`: Ссылка на класс `Pizzagpt`.
- `model` (str): Модель, которую следует использовать для генерации ответа.
- `messages` (Messages): Список сообщений, которые нужно отправить в API для получения ответа.
- `proxy` (str, optional): Прокси-сервер для использования при отправке запроса. По умолчанию `None`.
- `**kwargs`: Дополнительные параметры, которые могут быть переданы в API.

**Возвращает**:
- `AsyncResult`: Асинхронный генератор, который возвращает текст от API.

**Вызывает исключения**:
- `ValueError`: Если API возвращает сообщение об обнаружении злоупотребления.

**Как работает функция**:
1. **Подготовка заголовков**: Функция начинает с подготовки заголовков для HTTP-запроса, включая User-Agent, Content-Type и другие необходимые параметры.
2. **Создание сессии**: Затем создается асинхронная сессия `ClientSession` с заданными заголовками.
3. **Форматирование запроса**: Функция форматирует сообщения, используя функцию `format_prompt`, чтобы подготовить данные для отправки в API.
4. **Отправка запроса**: POST-запрос отправляется на endpoint API с использованием асинхронной сессии.
5. **Обработка ответа**: Функция обрабатывает ответ от API, извлекая содержимое ответа в формате JSON и проверяя наличие ошибок.
6. **Генерация результата**: Если содержимое успешно извлечено, функция генерирует текст ответа и причину завершения (FinishReason).
7. **Обработка ошибок**: В случае обнаружения сообщения о злоупотреблении, функция вызывает исключение `ValueError`.

**Внутренние функции**:

Внутри функции `create_async_generator` используется асинхронный контекстный менеджер `async with ClientSession(headers=headers) as session:` для создания сессии и `async with session.post(f"{cls.url}{cls.api_endpoint}", json=data, proxy=proxy) as response:` для отправки POST-запроса.

```
A: Подготовка заголовков и данных для запроса
|
B: Создание асинхронной сессии
|
C: Отправка POST-запроса к API
|
D: Обработка ответа от API
|
E: Генерация текста ответа или обработка ошибки
```

**Примеры**:

```python
import asyncio
from typing import AsyncGenerator, List, Dict

from src.endpoints.gpt4free.g4f.Provider.Pizzagpt import Pizzagpt
from src.endpoints.gpt4free.g4f.typing import Messages, FinishReason


async def main():
    model = "gpt-4o-mini"
    messages: Messages = [{"role": "user", "content": "Привет, как дела?"}]
    proxy = None
    kwargs = {}

    async def consume_generator(generator: AsyncGenerator[str | FinishReason, None]):
        async for item in generator:
            print(item, end="")

    try:
        generator = await Pizzagpt.create_async_generator(model=model, messages=messages, proxy=proxy, **kwargs)
        await consume_generator(generator)
    except ValueError as ex:
        print(f"Ошибка: {ex}")

if __name__ == "__main__":
    asyncio.run(main())
```

```python
import asyncio
from typing import AsyncGenerator, List, Dict

from src.endpoints.gpt4free.g4f.Provider.Pizzagpt import Pizzagpt
from src.endpoints.gpt4free.g4f.typing import Messages, FinishReason


async def main():
    model = "gpt-4o-mini"
    messages: Messages = [
        {"role": "user", "content": "Напиши короткий стих о лете."},
        {"role": "assistant", "content": "Солнце светит ярко, птички поют,\nЛето наступило, радость вокруг!"}
    ]
    proxy = None
    kwargs = {}

    async def consume_generator(generator: AsyncGenerator[str | FinishReason, None]):
        async for item in generator:
            print(item, end="")

    try:
        generator = await Pizzagpt.create_async_generator(model=model, messages=messages, proxy=proxy, **kwargs)
        await consume_generator(generator)
    except ValueError as ex:
        print(f"Ошибка: {ex}")

if __name__ == "__main__":
    asyncio.run(main())