# Модуль `AI365VIP`

## Обзор

Модуль `AI365VIP` предоставляет асинхронный генератор для взаимодействия с API AI365VIP. Он позволяет отправлять запросы к различным моделям, таким как `gpt-3.5-turbo` и `gpt-4o`, и получать ответы в виде асинхронного генератора. Этот модуль является частью проекта `hypotez` и предназначен для использования в задачах, требующих асинхронного взаимодействия с AI365VIP.

## Подробней

Модуль содержит класс `AI365VIP`, который наследуется от `AsyncGeneratorProvider` и `ProviderModelMixin`. Он определяет URL, API endpoint, список поддерживаемых моделей и алиасы для моделей. Основной функциональностью является метод `create_async_generator`, который отправляет запрос к API AI365VIP и возвращает асинхронный генератор, выдающий чанки данных из ответа.

## Классы

### `AI365VIP`

**Описание**: Класс для взаимодействия с API AI365VIP.

**Наследует**:
- `AsyncGeneratorProvider`: Обеспечивает функциональность асинхронного генератора.
- `ProviderModelMixin`: Предоставляет миксин для работы с моделями.

**Аттрибуты**:
- `url` (str): URL API AI365VIP.
- `api_endpoint` (str): Endpoint API для чата.
- `working` (bool): Указывает, работает ли провайдер в данный момент.
- `default_model` (str): Модель, используемая по умолчанию (`gpt-3.5-turbo`).
- `models` (List[str]): Список поддерживаемых моделей.
- `model_aliases` (Dict[str, str]): Алиасы для моделей.

**Методы**:
- `create_async_generator`: Создает асинхронный генератор для получения ответов от API AI365VIP.

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
    Создает асинхронный генератор для получения ответов от API AI365VIP.

    Args:
        model (str): Название модели для использования.
        messages (Messages): Список сообщений для отправки в API.
        proxy (str, optional): Прокси-сервер для использования. По умолчанию `None`.
        **kwargs: Дополнительные аргументы.

    Returns:
        AsyncResult: Асинхронный генератор, выдающий чанки данных из ответа API.

    Raises:
        aiohttp.ClientResponseError: Если возникает HTTP ошибка при запросе к API.

    """
    ...
```

**Назначение**: Создает асинхронный генератор для взаимодействия с API AI365VIP.

**Параметры**:
- `cls` (AI365VIP): Ссылка на класс.
- `model` (str): Название модели для использования.
- `messages` (Messages): Список сообщений для отправки в API.
- `proxy` (str, optional): Прокси-сервер для использования. По умолчанию `None`.
- `**kwargs`: Дополнительные аргументы.

**Возвращает**:
- `AsyncResult`: Асинхронный генератор, выдающий чанки данных из ответа API.

**Вызывает исключения**:
- `aiohttp.ClientResponseError`: Если возникает HTTP ошибка при запросе к API.

**Как работает функция**:

1. **Определение заголовков**: Функция начинает с определения необходимых HTTP-заголовков для запроса. Эти заголовки включают информацию о типе контента, User-Agent и другие метаданные, которые помогают серверу правильно обработать запрос.
2. **Создание сессии**: Используется `aiohttp.ClientSession` для асинхронного выполнения HTTP-запросов. Сессия позволяет повторно использовать соединение для нескольких запросов, что повышает эффективность.
3. **Формирование данных**: Функция формирует JSON-данные, которые будут отправлены в теле POST-запроса. Эти данные включают:
   - `model`: Идентификатор модели, имя, максимальную длину и лимит токенов.
   - `messages`: Список сообщений, где каждое сообщение имеет роль (например, "user") и контент, отформатированный с использованием `format_prompt(messages)`.
   - `key`, `prompt`, `temperature`: Дополнительные параметры для запроса.
4. **Выполнение POST-запроса**: С помощью `session.post` отправляется POST-запрос к API endpoint (`cls.url}{cls.api_endpoint`) с JSON-данными и прокси-сервером (если указан).
5. **Обработка ответа**: Функция проверяет статус ответа с помощью `response.raise_for_status()`, чтобы убедиться, что запрос выполнен успешно (код 200 OK).
6. **Генерация чанков**: Асинхронно читает содержимое ответа чанками и декодирует каждый чанк в строку. Затем каждый чанк передается через `yield`, что делает функцию генератором.

**ASCII flowchart**:

```
Заголовки  ->  Создание сессии -> Формирование данных -> POST-запрос -> Проверка статуса -> Генерация чанков -> Выход
```

**Примеры**:

```python
# Пример вызова функции
import asyncio
from typing import List, Dict, AsyncGenerator, Optional

async def main():
    model = "gpt-3.5-turbo"
    messages: List[Dict[str, str]] = [{"role": "user", "content": "Hello, how are you?"}]
    proxy: Optional[str] = None

    async def consume_generator(generator: AsyncGenerator[str, None]) -> None:
        async for chunk in generator:
            print(chunk, end="")

    generator = AI365VIP.create_async_generator(model=model, messages=messages, proxy=proxy)
    if generator:
        await consume_generator(generator)

if __name__ == "__main__":
    asyncio.run(main())
```
```python
# Пример вызова функции с прокси
import asyncio
from typing import List, Dict, AsyncGenerator, Optional

async def main():
    model = "gpt-3.5-turbo"
    messages: List[Dict[str, str]] = [{"role": "user", "content": "Translate to french: Hello, how are you?"}]
    proxy: Optional[str] = "http://your.proxy:8080"  # Замените на ваш прокси

    async def consume_generator(generator: AsyncGenerator[str, None]) -> None:
        async for chunk in generator:
            print(chunk, end="")

    generator = AI365VIP.create_async_generator(model=model, messages=messages, proxy=proxy)
    if generator:
        await consume_generator(generator)

if __name__ == "__main__":
    asyncio.run(main())