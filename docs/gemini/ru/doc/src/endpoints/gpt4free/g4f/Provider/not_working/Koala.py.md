# Модуль `Koala.py`

## Обзор

Модуль `Koala.py` предназначен для взаимодействия с API сервиса Koala (koala.sh) для генерации текста на основе предоставленных сообщений. Он использует асинхронные запросы для обмена данными с API и предоставляет функциональность для обработки потока событий, возвращаемого сервисом. Модуль поддерживает указание модели, прокси и истории сообщений.

## Подробней

Модуль `Koala.py` предоставляет асинхронный интерфейс для взаимодействия с сервисом Koala, позволяя генерировать текст на основе заданных входных данных. Он отправляет запросы к API `koala.sh` и обрабатывает ответы в формате потока событий.

## Классы

### `Koala`

**Описание**: Класс `Koala` является провайдером для асинхронной генерации текста с использованием API Koala. Он наследуется от `AsyncGeneratorProvider` и `ProviderModelMixin`, что позволяет ему использовать функциональность асинхронной генерации и поддержки различных моделей.

**Наследует**:

- `AsyncGeneratorProvider`: Обеспечивает базовую структуру для асинхронных провайдеров генерации.
- `ProviderModelMixin`: Предоставляет функциональность для работы с моделями, поддерживаемыми провайдером.

**Атрибуты**:

- `url` (str): URL сервиса Koala (`https://koala.sh/chat`).
- `api_endpoint` (str): URL API для взаимодействия (`https://koala.sh/api/gpt/`).
- `working` (bool): Указывает, работает ли провайдер в данный момент.
- `supports_message_history` (bool): Указывает, поддерживает ли провайдер историю сообщений.
- `default_model` (str): Модель, используемая по умолчанию (`gpt-4o-mini`).

**Методы**:

- `create_async_generator`: Создает асинхронный генератор для получения текстовых фрагментов от API Koala.
- `_parse_event_stream`: Разбирает поток событий, возвращаемый API, и извлекает полезные данные.

## Функции

### `create_async_generator`

```python
@classmethod
async def create_async_generator(
    cls,
    model: str,
    messages: Messages,
    proxy: Optional[str] = None,
    connector: Optional[BaseConnector] = None,
    **kwargs: Any
) -> AsyncGenerator[Dict[str, Union[str, int, float, List[Dict[str, Any]], None]], None]:
    """
    Создает асинхронный генератор для получения текстовых фрагментов от API Koala.

    Args:
        model (str): Модель для использования при генерации текста.
        messages (Messages): Список сообщений для отправки в API.
        proxy (Optional[str], optional): URL прокси-сервера для использования. По умолчанию `None`.
        connector (Optional[BaseConnector], optional): Объект коннектора aiohttp для использования. По умолчанию `None`.
        **kwargs (Any): Дополнительные параметры.

    Returns:
        AsyncGenerator[Dict[str, Union[str, int, float, List[Dict[str, Any]], None]], None]:
            Асинхронный генератор, возвращающий словарь с текстовыми фрагментами.

    Raises:
        Exception: Если возникает ошибка при взаимодействии с API.
    """
```

**Назначение**: Создает асинхронный генератор, который отправляет запросы к API Koala и возвращает текстовые фрагменты в виде словарей.

**Параметры**:

- `model` (str): Модель для использования при генерации текста.
- `messages` (Messages): Список сообщений, отправляемых в API. Каждое сообщение содержит роль (`user`, `assistant`, `system`) и содержимое.
- `proxy` (Optional[str], optional): URL прокси-сервера для использования. По умолчанию `None`.
- `connector` (Optional[BaseConnector], optional): Объект коннектора aiohttp для использования. По умолчанию `None`.
- `**kwargs` (Any): Дополнительные параметры, которые могут быть переданы в функцию.

**Возвращает**:

- `AsyncGenerator[Dict[str, Union[str, int, float, List[Dict[str, Any]], None]], None]`: Асинхронный генератор, который выдает словари, содержащие текстовые фрагменты от API Koala.

**Как работает функция**:

1. **Определение модели**: Если модель не указана, используется модель по умолчанию (`gpt-4o-mini`).
2. **Подготовка заголовков**: Создаются заголовки HTTP-запроса, включающие User-Agent, Accept, Referer и другие необходимые параметры.
3. **Создание сессии**: Создается асинхронная сессия `aiohttp.ClientSession` с заданными заголовками и коннектором.
4. **Подготовка данных**: Извлекается входной текст из последнего сообщения в списке `messages`. Также извлекаются системные сообщения и добавляются к входному тексту. Формируются данные для отправки в API, включающие входной текст, историю сообщений пользователя и ассистента, а также модель.
5. **Отправка запроса**: Отправляется POST-запрос к API `koala.sh` с подготовленными данными.
6. **Обработка потока событий**: Полученный ответ разбирается с использованием асинхронного генератора `_parse_event_stream`, который извлекает текстовые фрагменты из потока событий.
7. **Возврат генератора**: Возвращается асинхронный генератор, который выдает словари с текстовыми фрагментами.

**Внутренние функции**: Нет.

**Примеры**:

```python
# Пример использования create_async_generator
import asyncio
from typing import List, Dict, Union, Any, AsyncGenerator

async def main():
    model = "gpt-4o-mini"
    messages: List[Dict[str, str]] = [
        {"role": "user", "content": "Привет, как дела?"},
        {"role": "assistant", "content": "Привет! У меня все хорошо, спасибо."},
        {"role": "user", "content": "Что ты умеешь?"}
    ]

    async def print_chunks(generator: AsyncGenerator[Dict[str, Union[str, int, float, List[Dict[str, Any]], None]], None]):
        async for chunk in generator:
            print(chunk)

    generator = await Koala.create_async_generator(model=model, messages=messages)
    await print_chunks(generator)

if __name__ == "__main__":
    asyncio.run(main())
```

### `_parse_event_stream`

```python
@staticmethod
async def _parse_event_stream(response: ClientResponse) -> AsyncGenerator[Dict[str, Any], None]:
    """
    Разбирает поток событий, возвращаемый API, и извлекает полезные данные.

    Args:
        response (ClientResponse): Объект ответа от API.

    Returns:
        AsyncGenerator[Dict[str, Any], None]: Асинхронный генератор, возвращающий словари с данными из потока событий.
    """
```

**Назначение**: Разбирает поток событий, возвращаемый API Koala, и извлекает данные, содержащиеся в каждом событии.

**Параметры**:

- `response` (ClientResponse): Объект ответа от API Koala, содержащий поток событий.

**Возвращает**:

- `AsyncGenerator[Dict[str, Any], None]`: Асинхронный генератор, который выдает словари с данными, извлеченными из каждого события в потоке.

**Как работает функция**:

1. **Итерация по чанкам**: Функция асинхронно итерируется по чанкам в содержимом ответа (`response.content`).
2. **Проверка префикса**: Для каждого чанка проверяется, начинается ли он с префикса `b"data: "`.
3. **Извлечение данных**: Если чанк начинается с указанного префикса, извлекаются данные, находящиеся после префикса (начиная с 6-го байта).
4. **Декодирование JSON**: Извлеченные данные декодируются из JSON-формата в словарь.
5. **Выдача данных**: Полученный словарь выдается через асинхронный генератор.

**Внутренние функции**: Нет.

**Примеры**:

```python
# Пример использования _parse_event_stream
import asyncio
from aiohttp import ClientSession
from typing import AsyncGenerator, Dict, Any

async def main():
    url = "https://koala.sh/api/gpt/"  # Замените на фактический URL, если необходимо
    data = {"input": "Hello"}  # Замените на фактические данные

    async with ClientSession() as session:
        async with session.post(url, json=data) as response:
            async def print_chunks(generator: AsyncGenerator[Dict[str, Any], None]):
                async for chunk in generator:
                    print(chunk)

            generator = Koala._parse_event_stream(response)
            await print_chunks(generator)

if __name__ == "__main__":
    asyncio.run(main())