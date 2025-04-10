# Модуль `ChatGptt`

## Обзор

Модуль `ChatGptt` предоставляет асинхронный генератор для взаимодействия с сервисом `chatgptt.me`. Он позволяет отправлять запросы к API этого сервиса и получать ответы в потоковом режиме. Модуль поддерживает указание модели, прокси и другие параметры запроса.

## Подробней

Модуль предназначен для интеграции с `chatgptt.me`, предоставляя удобный интерфейс для отправки сообщений и получения ответов в асинхронном режиме. Он использует `aiohttp` для выполнения HTTP-запросов и поддерживает потоковую передачу данных. Поддерживается как системные сообщения, так и история сообщений.

## Классы

### `ChatGptt`

**Описание**: Класс `ChatGptt` является асинхронным генератором провайдером и предоставляет методы для взаимодействия с API `chatgptt.me`.

**Наследует**:
- `AsyncGeneratorProvider`: Обеспечивает базовую функциональность для асинхронных генераторов провайдеров.
- `ProviderModelMixin`: Добавляет поддержку выбора моделей.

**Атрибуты**:
- `url` (str): URL сервиса `chatgptt.me`.
- `api_endpoint` (str): URL API для отправки сообщений.
- `working` (bool): Флаг, указывающий на работоспособность провайдера.
- `supports_stream` (bool): Флаг, указывающий на поддержку потоковой передачи данных.
- `supports_system_message` (bool): Флаг, указывающий на поддержку системных сообщений.
- `supports_message_history` (bool): Флаг, указывающий на поддержку истории сообщений.
- `default_model` (str): Модель, используемая по умолчанию (`gpt-4o`).
- `models` (List[str]): Список поддерживаемых моделей.

**Методы**:
- `create_async_generator`: Создает асинхронный генератор для отправки запросов к API.

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
    Создает асинхронный генератор для отправки запросов к API chatgptt.me.

    Args:
        cls (ChatGptt): Класс `ChatGptt`.
        model (str): Модель, используемая для генерации ответа.
        messages (Messages): Список сообщений для отправки.
        proxy (str, optional): URL прокси-сервера. По умолчанию `None`.
        **kwargs: Дополнительные параметры.

    Returns:
        AsyncResult: Асинхронный генератор, возвращающий результаты запроса.

    Raises:
        RuntimeError: Если не удалось извлечь токены аутентификации из HTML-страницы.
    """
```

**Назначение**: Создает асинхронный генератор для взаимодействия с API `chatgptt.me`.

**Параметры**:
- `cls`: Класс `ChatGptt`.
- `model` (str): Модель, используемая для генерации ответа.
- `messages` (Messages): Список сообщений для отправки.
- `proxy` (str, optional): URL прокси-сервера. По умолчанию `None`.
- `**kwargs`: Дополнительные параметры.

**Возвращает**:
- `AsyncResult`: Асинхронный генератор, возвращающий результаты запроса.

**Вызывает исключения**:
- `RuntimeError`: Если не удалось извлечь токены аутентификации из HTML-страницы.

**Как работает функция**:

1. **Выбор модели**: Функция `create_async_generator` сначала выбирает модель, используя метод `cls.get_model(model)`.
2. **Подготовка заголовков**: Подготавливаются заголовки HTTP-запроса, включая информацию о браузере и источнике запроса.
3. **Создание сессии**: Создается асинхронная сессия `ClientSession` с заданными заголовками.
4. **Получение начальной страницы**: Функция отправляет GET-запрос к `cls.url` для получения начальной HTML-страницы.
5. **Извлечение токенов**: Из HTML-страницы извлекаются токены `nonce_` и `post_id` с использованием регулярных выражений. В случае неудачи извлечения токенов, выбрасывается исключение `RuntimeError`.
6. **Подготовка полезной нагрузки**: Формируется полезная нагрузка (payload) для POST-запроса, включающая токены, сообщения и другие необходимые параметры.
7. **Отправка POST-запроса**: Отправляется POST-запрос к `cls.api_endpoint` с заголовками, полезной нагрузкой и прокси (если указан).
8. **Обработка ответа**: Полученный JSON-ответ обрабатывается, и из него извлекаются данные (`result['data']`), которые затем передаются в генератор.

**ASCII flowchart**:

```
A [Выбор модели]
|
B [Подготовка заголовков]
|
C [Создание сессии]
|
D [Получение HTML страницы]
|
E [Извлечение токенов]
|
F [Подготовка payload]
|
G [Отправка POST запроса]
|
H [Обработка ответа и передача данных в генератор]
```

**Примеры**:

```python
# Пример вызова create_async_generator
model = "gpt-4"
messages = [{"role": "user", "content": "Hello, how are you?"}]
proxy = "http://your-proxy:8080"

async def example():
    async for response in ChatGptt.create_async_generator(model=model, messages=messages, proxy=proxy):
        print(response)

# Запуск примера (необходимо находиться в асинхронном контексте)
# import asyncio
# asyncio.run(example())