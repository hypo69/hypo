# Модуль Acytoo

## Обзор

Модуль `Acytoo` предоставляет асинхронный генератор для взаимодействия с сервисом чата Acytoo. Он реализует класс `Acytoo`, который наследуется от `AsyncGeneratorProvider` и предназначен для работы с моделью `gpt-3.5-turbo`. Модуль поддерживает историю сообщений.

## Подробнее

Этот модуль используется для отправки запросов к API Acytoo и получения ответов в виде асинхронного потока данных. Он включает функции для создания заголовков и полезной нагрузки запроса.
Модуль определяет, как взаимодействовать с Acytoo в асинхронном режиме.

## Классы

### `Acytoo`

**Описание**: Класс `Acytoo` предназначен для асинхронного взаимодействия с сервисом чата Acytoo.

**Наследует**:
- `AsyncGeneratorProvider`: Этот класс наследует функциональность асинхронного генератора от базового класса `AsyncGeneratorProvider`.

**Атрибуты**:
- `url` (str): URL сервиса Acytoo (`'https://chat.acytoo.com'`).
- `working` (bool): Флаг, указывающий на работоспособность сервиса (всегда `False`).
- `supports_message_history` (bool): Флаг, указывающий на поддержку истории сообщений (всегда `True`).
- `supports_gpt_35_turbo` (bool): Флаг, указывающий на поддержку модели `gpt-3.5-turbo` (всегда `True`).

**Методы**:
- `create_async_generator`: Асинхронный генератор для отправки запросов и получения ответов от Acytoo.

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
    """Асинхронный генератор для отправки запросов и получения ответов от Acytoo.

    Args:
        cls (Type[Acytoo]): Ссылка на класс `Acytoo`.
        model (str): Название модели, используемой для генерации ответов.
        messages (Messages): Список сообщений для отправки в запросе.
        proxy (str, optional): URL прокси-сервера. По умолчанию `None`.
        **kwargs: Дополнительные параметры.

    Returns:
        AsyncResult: Асинхронный генератор, возвращающий части ответа от Acytoo.

    Raises:
        aiohttp.ClientResponseError: Если HTTP-запрос завершается с ошибкой.

    """
```

**Назначение**: Функция `create_async_generator` создает асинхронный генератор, который отправляет запросы к API Acytoo и возвращает ответы в виде потока данных.

**Параметры**:
- `cls`: Ссылка на класс `Acytoo`.
- `model` (str): Название модели, используемой для генерации ответов.
- `messages` (Messages): Список сообщений для отправки в запросе.
- `proxy` (str, optional): URL прокси-сервера. По умолчанию `None`.
- `**kwargs`: Дополнительные параметры, передаваемые в полезной нагрузке запроса.

**Возвращает**:
- `AsyncResult`: Асинхронный генератор, возвращающий части ответа от Acytoo.

**Вызывает исключения**:
- `aiohttp.ClientResponseError`: Возникает, если HTTP-запрос завершается с ошибкой.

**Как работает функция**:
1.  Функция создает асинхронную сессию `aiohttp.ClientSession` с заголовками, полученными из функции `_create_header`.
2.  Внутри сессии выполняется POST-запрос к адресу `f'{cls.url}/api/completions'` с использованием указанного прокси и JSON-данных, полученных из функции `_create_payload`.
3.  Если запрос успешен, функция итерируется по содержимому ответа как по потоку данных и декодирует каждый чанк, возвращая его как часть асинхронного генератора.

```text
create_async_generator
│
├── Создание асинхронной сессии (session) с headers
│   │
│   └── _create_header() -> headers
│
├── Создание payload
│   │
│   └── _create_payload(messages, **kwargs) -> payload
│
├── POST-запрос к API Acytoo
│   │
│   └── session.post(url, proxy, json=payload) -> response
│
├── Обработка потока данных из ответа
│   │
│   └── response.content.iter_any() -> stream
│       │
│       └── Декодирование чанка: stream.decode()
│
└── Выдача декодированного чанка через yield
```

**Примеры**:

```python
# Пример использования функции create_async_generator
messages = [{"role": "user", "content": "Hello, Acytoo!"}]
async def example():
    async for message in Acytoo.create_async_generator(model='gpt-3.5-turbo', messages=messages):
        print(message, end="")

# Запуск примера (требуется асинхронная среда)
# import asyncio
# asyncio.run(example())
```

### `_create_header`

```python
def _create_header():
    """Создает словарь с HTTP-заголовками.

    Returns:
        dict: Словарь с HTTP-заголовками 'accept' и 'content-type'.
    """
```

**Назначение**: Функция `_create_header` создает словарь с HTTP-заголовками, необходимыми для запроса к API Acytoo.

**Возвращает**:
- `dict`: Словарь с HTTP-заголовками `accept` и `content-type`.

**Как работает функция**:
1.  Функция создает и возвращает словарь, содержащий заголовки `accept` и `content-type`.

**Примеры**:

```python
# Пример использования функции _create_header
headers = _create_header()
print(headers)
```

### `_create_payload`

```python
def _create_payload(messages: Messages, temperature: float = 0.5, **kwargs):
    """Создает словарь с полезной нагрузкой для запроса к API Acytoo.

    Args:
        messages (Messages): Список сообщений для отправки.
        temperature (float, optional): Температура для генерации ответов. По умолчанию 0.5.
        **kwargs: Дополнительные параметры.

    Returns:
        dict: Словарь с полезной нагрузкой для запроса.
    """
```

**Назначение**: Функция `_create_payload` создает словарь с полезной нагрузкой (payload) для запроса к API Acytoo.

**Параметры**:
- `messages` (Messages): Список сообщений для отправки.
- `temperature` (float, optional): Температура для генерации ответов. По умолчанию `0.5`.
- `**kwargs`: Дополнительные параметры, которые будут включены в полезную нагрузку.

**Возвращает**:
- `dict`: Словарь с полезной нагрузкой для запроса.

**Как работает функция**:
1.  Функция создает словарь, содержащий параметры `key`, `model`, `messages`, `temperature` и `password`.
2.  Значения этих параметров устанавливаются на основе входных аргументов и констант.
3.  Возвращается созданный словарь.

**Примеры**:

```python
# Пример использования функции _create_payload
messages = [{"role": "user", "content": "Hello, Acytoo!"}]
payload = _create_payload(messages=messages, temperature=0.7)
print(payload)