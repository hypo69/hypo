# Модуль Opchatgpts

## Обзор

Модуль `Opchatgpts` предоставляет асинхронный генератор для взаимодействия с сервисом opchatgpts.net.
Он поддерживает работу с историей сообщений и моделью `gpt-3.5-turbo`.
Этот модуль предназначен для использования в асинхронных приложениях и предоставляет возможность получения ответов от чат-бота в режиме реального времени.

## Подробней

Модуль использует библиотеку `aiohttp` для выполнения асинхронных HTTP-запросов. Он отправляет сообщения пользователя на сервер `opchatgpts.net` и получает ответы в формате потока данных, который затем обрабатывается для извлечения полезной информации. Модуль также включает поддержку прокси-серверов для обеспечения анонимности и обхода географических ограничений.

## Классы

### `Opchatgpts`

**Описание**: Класс `Opchatgpts` является асинхронным генератором провайдера, который взаимодействует с сервисом `opchatgpts.net`.

**Принцип работы**:
Класс отправляет POST-запросы на сервер `opchatgpts.net` с использованием библиотеки `aiohttp`. Запросы содержат сообщения пользователя, а также метаданные, такие как идентификатор бота, идентификатор чата и контекст. Ответ от сервера приходит в виде потока данных, который обрабатывается для извлечения содержимого сообщений.

**Аттрибуты**:
- `url` (str): URL сервиса `opchatgpts.net`.
- `working` (bool): Флаг, указывающий на работоспособность провайдера.
- `supports_message_history` (bool): Флаг, указывающий на поддержку истории сообщений.
- `supports_gpt_35_turbo` (bool): Флаг, указывающий на поддержку модели `gpt-3.5-turbo`.

**Методы**:
- `create_async_generator`: Создает асинхронный генератор для получения ответов от сервиса.

## Функции

### `create_async_generator`

```python
@classmethod
async def create_async_generator(
    cls,
    model: str,
    messages: Messages,
    proxy: str = None, **kwargs) -> AsyncResult:
    """
    Создает асинхронный генератор для получения ответов от сервиса opchatgpts.net.

    Args:
        model (str): Название используемой модели (например, `gpt-3.5-turbo`).
        messages (Messages): Список сообщений для отправки на сервер.
        proxy (str, optional): URL прокси-сервера. По умолчанию `None`.
        **kwargs: Дополнительные аргументы.

    Returns:
        AsyncResult: Асинхронный генератор, возвращающий ответы от сервиса.

    Raises:
        RuntimeError: Если полученная строка данных имеет неправильный формат.
        aiohttp.ClientResponseError: Если HTTP-запрос завершается с ошибкой.

    Example:
        Пример использования асинхронного генератора:

        ```python
        async for message in Opchatgpts.create_async_generator(model="gpt-3.5-turbo", messages=[{"role": "user", "content": "Hello"}], proxy="http://proxy.example.com"):
            print(message)
        ```
    """
```

**Назначение**: Создает асинхронный генератор для взаимодействия с сервисом `opchatgpts.net`.

**Параметры**:
- `cls`: Ссылка на класс `Opchatgpts`.
- `model` (str): Название используемой модели (например, `gpt-3.5-turbo`).
- `messages` (Messages): Список сообщений для отправки на сервер.
- `proxy` (str, optional): URL прокси-сервера. По умолчанию `None`.
- `**kwargs`: Дополнительные аргументы.

**Возвращает**:
- `AsyncResult`: Асинхронный генератор, возвращающий ответы от сервиса.

**Вызывает исключения**:
- `RuntimeError`: Если полученная строка данных имеет неправильный формат.
- `aiohttp.ClientResponseError`: Если HTTP-запрос завершается с ошибкой.

**Как работает функция**:

1. Функция создает заголовки HTTP-запроса, включая `User-Agent`, `Accept`, `Origin` и другие необходимые параметры.
2. Создается сессия `aiohttp.ClientSession` с заданными заголовками. Если указан прокси-сервер, он также используется в сессии.
3. Формируется словарь `data` с параметрами запроса, такими как `botId`, `chatId`, `contextId`, `messages` и `newMessage`.
4. Отправляется POST-запрос на URL `f"{cls.url}/wp-json/mwai-ui/v1/chats/submit"` с использованием сессии `aiohttp.ClientSession`.
5. Функция итерируется по строкам ответа, полученного от сервера.
6. Для каждой строки, начинающейся с `b"data: "`, извлекается JSON-данные и проверяется наличие ключа `"type"`.
7. Если `"type"` имеет значение `"live"`, возвращается значение `"data"`. Если `"type"` имеет значение `"end"`, генератор завершает работу.
8. В случае возникновения ошибок при обработке ответа, выбрасывается исключение `RuntimeError`.

```
                                     Начало
                                        ↓
         Создание заголовков HTTP-запроса и сессии aiohttp.ClientSession
                                        ↓
                Формирование данных запроса (botId, chatId, contextId, messages, и т.д.)
                                        ↓
    Отправка POST-запроса на сервер opchatgpts.net с данными и заголовками
                                        ↓
          Итерация по строкам ответа от сервера (response.content)
                                        ↓
    Проверка, начинается ли строка с b"data: " → [Да] : Извлечение JSON из строки
            [Нет] : Пропуск строки                                 
                                        ↓
  Проверка наличия ключа "type" в JSON → [Да] : Проверка значения "type"
            [Нет] : Выбрасывание RuntimeError                      
                                        ↓
        "type" == "live"  → [Да] : Выдача значения "data"
                            [Нет] : Проверка "type" == "end"
                                        ↓
            "type" == "end" → [Да] : Завершение генератора
                                [Нет] : Продолжение итерации
                                        ↓
                                      Конец
```

**Примеры**:

- Пример вызова функции без использования прокси:

```python
async for message in Opchatgpts.create_async_generator(model="gpt-3.5-turbo", messages=[{"role": "user", "content": "Hello"}]):
    print(message)
```

- Пример вызова функции с использованием прокси:

```python
async for message in Opchatgpts.create_async_generator(model="gpt-3.5-turbo", messages=[{"role": "user", "content": "Hello"}], proxy="http://proxy.example.com"):
    print(message)
```

- Пример вызова функции с дополнительными аргументами:

```python
async for message in Opchatgpts.create_async_generator(model="gpt-3.5-turbo", messages=[{"role": "user", "content": "Hello"}], temperature=0.7):
    print(message)