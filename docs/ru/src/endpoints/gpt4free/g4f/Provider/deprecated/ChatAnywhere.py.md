# Модуль `ChatAnywhere`

## Обзор

Модуль `ChatAnywhere` предоставляет асинхронный генератор для взаимодействия с сервисом `chatanywhere.cn`.
Он поддерживает модель `gpt-3.5-turbo` и сохранение истории сообщений. Модуль предназначен для использования в асинхронных приложениях.

## Подробнее

Модуль реализует класс `ChatAnywhere`, который наследуется от `AsyncGeneratorProvider`.
Этот класс использует `aiohttp` для выполнения асинхронных HTTP-запросов к API `chatanywhere.cn`.

## Классы

### `ChatAnywhere`

**Описание**: Класс для взаимодействия с сервисом `chatanywhere.cn`.

**Наследует**: `AsyncGeneratorProvider`

**Атрибуты**:
- `url` (str): URL сервиса `chatanywhere.cn`.
- `supports_gpt_35_turbo` (bool): Указывает, поддерживает ли провайдер модель `gpt-3.5-turbo`.
- `supports_message_history` (bool): Указывает, поддерживает ли провайдер историю сообщений.
- `working` (bool): Указывает, работает ли провайдер в данный момент.

**Методы**:
- `create_async_generator`: Создает асинхронный генератор для обмена сообщениями с сервисом.

## Функции

### `create_async_generator`

```python
@classmethod
async def create_async_generator(
    cls,
    model: str,
    messages: Messages,
    proxy: str = None,
    timeout: int = 120,
    temperature: float = 0.5,
    **kwargs
) -> AsyncResult:
    """Создает асинхронный генератор для обмена сообщениями с сервисом chatanywhere.cn.

    Args:
        model (str): Модель для использования (например, "gpt-3.5-turbo").
        messages (Messages): Список сообщений для отправки.
        proxy (str, optional): Прокси-сервер для использования. По умолчанию `None`.
        timeout (int, optional): Время ожидания ответа в секундах. По умолчанию 120.
        temperature (float, optional): Температура генерации текста. По умолчанию 0.5.
        **kwargs: Дополнительные параметры.

    Returns:
        AsyncResult: Асинхронный генератор, выдающий чанки текста.

    Raises:
        aiohttp.ClientResponseError: Если HTTP-запрос завершается с ошибкой.

    """
```

**Назначение**: Создание асинхронного генератора для взаимодействия с API `chatanywhere.cn`.

**Параметры**:
- `cls` (class): Ссылка на класс `ChatAnywhere`.
- `model` (str): Имя модели для использования.
- `messages` (Messages): Список сообщений для отправки в формате списка словарей, где каждый словарь содержит ключи `role` и `content`.
- `proxy` (str, optional): Адрес прокси-сервера для использования при отправке запроса. По умолчанию `None`.
- `timeout` (int, optional): Максимальное время ожидания ответа от сервера в секундах. По умолчанию 120.
- `temperature` (float, optional): Параметр, контролирующий случайность генерации текста. Чем выше значение, тем более случайным будет результат. По умолчанию 0.5.
- `**kwargs`: Дополнительные параметры, которые могут быть переданы в функцию.

**Возвращает**:
- `AsyncResult`: Асинхронный генератор, который выдает чанки текста, полученные от API.

**Вызывает исключения**:
- `aiohttp.ClientResponseError`: Вызывается, если HTTP-запрос завершается с ошибкой.

**Как работает функция**:

1.  **Определение заголовков**: Функция начинает с определения заголовков HTTP-запроса, включая `User-Agent`, `Accept`, `Content-Type` и другие необходимые параметры.
2.  **Создание сессии `aiohttp`**:  Создается асинхронная сессия `aiohttp` с заданными заголовками и таймаутом.
3.  **Подготовка данных для запроса**: Формируются данные для отправки в теле запроса, включая список сообщений, идентификатор, заголовок, температуру и другие параметры.
4.  **Выполнение POST-запроса**: Отправляется POST-запрос к API `chatanywhere.cn` с использованием асинхронной сессии.
5.  **Обработка ответа**: Функция асинхронно перебирает чанки данных из ответа и декодирует их, передавая каждый чанк как результат генератора.
6.  **Обработка ошибок**: В случае возникновения HTTP-ошибки, функция вызывает исключение `aiohttp.ClientResponseError`.

```
    Начало
    │
    ├── Заголовки запроса (Определение заголовков HTTP-запроса)
    │
    ├── Создание сессии (Создание асинхронной сессии aiohttp)
    │
    ├── Подготовка данных (Формирование данных для отправки)
    │
    ├── Отправка запроса (POST-запрос к API chatanywhere.cn)
    │
    ├── Обработка ответа (Асинхронный перебор чанков данных)
    │
    └── Конец
```

**Примеры**:

```python
import asyncio

async def main():
    model = "gpt-3.5-turbo"
    messages = [{"role": "user", "content": "Hello, how are you?"}]
    proxy = None
    timeout = 120
    temperature = 0.5

    generator = await ChatAnywhere.create_async_generator(
        model=model,
        messages=messages,
        proxy=proxy,
        timeout=timeout,
        temperature=temperature
    )

    async for chunk in generator:
        print(chunk, end="")

if __name__ == "__main__":
    asyncio.run(main())
```
```python
import asyncio

async def main():
    model = "gpt-3.5-turbo"
    messages = [{"role": "user", "content": "Как дела?"}]
    proxy = 'http://user:password@host:port'
    timeout = 60
    temperature = 0.7

    generator = await ChatAnywhere.create_async_generator(
        model=model,
        messages=messages,
        proxy=proxy,
        timeout=timeout,
        temperature=temperature
    )

    async for chunk in generator:
        print(chunk, end="")

if __name__ == "__main__":
    asyncio.run(main())
```
```python
import asyncio

async def main():
    model = "gpt-3.5-turbo"
    messages = [{"role": "user", "content": "Как написать API на python?"}]
    timeout = 300

    generator = await ChatAnywhere.create_async_generator(
        model=model,
        messages=messages,
        timeout=timeout,
    )

    async for chunk in generator:
        print(chunk, end="")

if __name__ == "__main__":
    asyncio.run(main())