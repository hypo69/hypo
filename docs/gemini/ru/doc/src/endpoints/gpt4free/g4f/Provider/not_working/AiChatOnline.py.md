# Модуль AiChatOnline

## Обзор

Модуль `AiChatOnline` предоставляет асинхронный интерфейс для взаимодействия с сервисом AiChatOnline.org. Он позволяет генерировать ответы на основе предоставленных сообщений, используя асинхронные генераторы для эффективной обработки данных.

## Подробнее

Этот модуль является частью проекта `hypotez` и предназначен для интеграции с сервисом AiChatOnline.org. Он использует `aiohttp` для выполнения асинхронных HTTP-запросов и предоставляет методы для получения токена, необходимого для аутентификации, а также для создания асинхронного генератора, который возвращает ответы от сервиса.

## Классы

### `AiChatOnline`

**Описание**: Класс `AiChatOnline` является подклассом `AsyncGeneratorProvider` и `ProviderModelMixin`. Он предоставляет методы для взаимодействия с сервисом AiChatOnline.org.

**Принцип работы**:

Класс использует `aiohttp` для отправки асинхронных запросов к API AiChatOnline.org. Он реализует методы для получения уникального идентификатора пользователя (`grab_token`) и создания асинхронного генератора (`create_async_generator`), который возвращает ответы от сервиса.

**Атрибуты**:

- `site_url` (str): URL сайта AiChatOnline.org.
- `url` (str): Базовый URL для API запросов.
- `api_endpoint` (str): Конечная точка API для отправки сообщений.
- `working` (bool): Указывает, работает ли провайдер.
- `default_model` (str): Модель, используемая по умолчанию (`gpt-4o-mini`).

**Методы**:

- `grab_token(session: ClientSession, proxy: str)`: Получает уникальный идентификатор пользователя.
- `create_async_generator(model: str, messages: Messages, proxy: str = None, **kwargs)`: Создает асинхронный генератор для получения ответов от сервиса.

## Функции

### `grab_token`

```python
    @classmethod
    async def grab_token(
        cls,
        session: ClientSession,
        proxy: str
    ) -> str:
        """
        Получает уникальный идентификатор пользователя с использованием асинхронного HTTP-запроса.

        Args:
            session (ClientSession): Асинхровая HTTP-сессия для выполнения запроса.
            proxy (str): Адрес прокси-сервера для использования.

        Returns:
            str: Уникальный идентификатор пользователя.

        Raises:
            aiohttp.ClientResponseError: Если HTTP-запрос завершается с ошибкой.

        Example:
            >>> session = ClientSession()
            >>> token = await AiChatOnline.grab_token(session, 'http://proxy:8080')
            >>> print(token)
            'unique_id'
        """
        ...
```

**Назначение**: Получение уникального идентификатора пользователя для последующей аутентификации при запросах к API.

**Параметры**:

- `session` (ClientSession): Асинхровая HTTP-сессия для выполнения запроса.
- `proxy` (str): Адрес прокси-сервера для использования (если необходимо).

**Возвращает**:

- `str`: Уникальный идентификатор пользователя, полученный из ответа API.

**Вызывает исключения**:

- `aiohttp.ClientResponseError`: Если HTTP-запрос завершается с ошибкой.

**Как работает функция**:

1. **Формирование URL**: Формируется URL для запроса к API `getUniqueId`.
2. **Выполнение GET-запроса**: Выполняется асинхронный GET-запрос к API с использованием предоставленной сессии и прокси (если указан).
3. **Обработка ответа**: Извлекается `data` из JSON-ответа, который содержит уникальный идентификатор пользователя.

```
    A: Формирование URL
    |
    B: Выполнение GET-запроса с использованием ClientSession и прокси
    |
    C: Извлечение 'data' из JSON ответа
    |
    D: Возврат уникального идентификатора пользователя
```

**Примеры**:

```python
import asyncio
from aiohttp import ClientSession
from src.endpoints.gpt4free.g4f.Provider.not_working import AiChatOnline

async def main():
    session = ClientSession()
    try:
        token = await AiChatOnline.grab_token(session, proxy='http://proxy:8080')
        print(f"Token: {token}")
    except Exception as ex:
        print(f"Error: {ex}")
    finally:
        await session.close()

if __name__ == "__main__":
    asyncio.run(main())
```

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
        Создает асинхронный генератор для получения ответов от сервиса AiChatOnline.org.

        Args:
            model (str): Модель для генерации ответа.
            messages (Messages): Список сообщений для отправки в запросе.
            proxy (str, optional): Адрес прокси-сервера для использования. По умолчанию `None`.
            **kwargs: Дополнительные параметры.

        Yields:
            str: Части ответа, полученные от сервиса.

        Raises:
            aiohttp.ClientResponseError: Если HTTP-запрос завершается с ошибкой.

        Example:
            >>> messages = [{"role": "user", "content": "Hello, how are you?"}]
            >>> async for chunk in AiChatOnline.create_async_generator('gpt-4o-mini', messages, proxy='http://proxy:8080'):
            ...     print(chunk)
            'Hello'
            ', '
            'I'
            ' am'
            ' fine'
            '.'
        """
        ...
```

**Назначение**: Создание асинхронного генератора для получения ответов от API AiChatOnline.org.

**Параметры**:

- `model` (str): Модель, используемая для генерации ответа.
- `messages` (Messages): Список сообщений, отправляемых в запросе.
- `proxy` (str, optional): Адрес прокси-сервера для использования. По умолчанию `None`.
- `**kwargs`: Дополнительные параметры, которые могут быть переданы в функцию.

**Возвращает**:

- `AsyncResult`: Асинхронный генератор, который выдает части ответа, полученные от сервиса.

**Вызывает исключения**:

- `aiohttp.ClientResponseError`: Если HTTP-запрос завершается с ошибкой.

**Как работает функция**:

1. **Формирование заголовков**: Создаются заголовки для HTTP-запроса, включая User-Agent, Referer, Content-Type и Origin.
2. **Создание асинхронной сессии**: Создается асинхронная HTTP-сессия с использованием `aiohttp.ClientSession` и установленными заголовками.
3. **Формирование данных запроса**: Создается словарь с данными для отправки в запросе, включая `conversationId` и `prompt` (отформатированные сообщения).
4. **Получение токена**: Получается уникальный идентификатор пользователя с помощью метода `grab_token`.
5. **Выполнение POST-запроса**: Выполняется асинхронный POST-запрос к API с использованием предоставленной сессии, заголовков, данных и прокси (если указан).
6. **Обработка ответа**: Извлекаются части ответа из JSON-ответа и выдаются через генератор.

```
    A: Формирование заголовков запроса
    |
    B: Создание асинхронной сессии ClientSession
    |
    C: Формирование данных запроса (conversationId, prompt)
    |
    D: Получение токена пользователя
    |
    E: Выполнение POST-запроса к API
    |
    F: Извлечение и выдача частей ответа через генератор
```

**Примеры**:

```python
import asyncio
from aiohttp import ClientSession
from src.endpoints.gpt4free.g4f.Provider.not_working import AiChatOnline

async def main():
    messages = [{"role": "user", "content": "Hello, how are you?"}]
    try:
        async for chunk in AiChatOnline.create_async_generator(model='gpt-4o-mini', messages=messages, proxy='http://proxy:8080'):
            print(chunk, end='')
    except Exception as ex:
        print(f"Error: {ex}")

if __name__ == "__main__":
    asyncio.run(main())