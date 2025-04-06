# Модуль для работы с провайдером Aibn (Deprecated)

## Обзор

Модуль `Aibn` предоставляет асинхронный генератор для взаимодействия с сервисом `aibn.cc`. Он поддерживает историю сообщений и модель `gpt-3.5-turbo`. Модуль предназначен для использования в устаревших (deprecated) версиях и может быть заменен более актуальными решениями.

## Подробнее

Этот модуль реализует класс `Aibn`, который наследуется от `AsyncGeneratorProvider`. Он использует `StreamSession` для асинхронной отправки запросов к API `aibn.cc`.

## Классы

### `Aibn`

**Описание**: Класс для взаимодействия с сервисом `aibn.cc`.

**Наследует**: `AsyncGeneratorProvider`

**Атрибуты**:
- `url` (str): URL сервиса `aibn.cc`.
- `working` (bool): Флаг, указывающий на работоспособность сервиса (в данном случае `False`).
- `supports_message_history` (bool): Флаг, указывающий на поддержку истории сообщений (в данном случае `True`).
- `supports_gpt_35_turbo` (bool): Флаг, указывающий на поддержку модели `gpt-3.5-turbo` (в данном случае `True`).

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
    proxy: str = None,
    timeout: int = 120,
    **kwargs
) -> AsyncResult:
    """Создает асинхронный генератор для получения ответов от сервиса Aibn.

    Args:
        model (str): Имя модели для использования.
        messages (Messages): Список сообщений для отправки.
        proxy (str, optional): Прокси-сервер для использования. По умолчанию `None`.
        timeout (int, optional): Время ожидания ответа в секундах. По умолчанию `120`.
        **kwargs: Дополнительные параметры.

    Returns:
        AsyncResult: Асинхронный генератор, выдающий ответы от сервиса.

    Как работает функция:
    1.  Функция `create_async_generator` принимает параметры, необходимые для создания асинхронного генератора, который будет взаимодействовать с API `aibn.cc`.
    2.  Используется `StreamSession` для асинхронной отправки запросов. `StreamSession` позволяет отправлять запросы и получать ответы в потоковом режиме.
    3.  Формируются данные для отправки, включая сообщения, временную метку и подпись.
    4.  Отправляется POST-запрос к API `aibn.cc` с сформированными данными.
    5.  Полученные чанки данных декодируются и выдаются через генератор.

    create_async_generator
    │
    ├───StreamSession (Создание сессии)
    │   │
    │   └───Формирование данных (timestamp, sign)
    │   │
    │   └───POST запрос к API (отправка данных)
    │   │
    │   └───Чтение ответа по частям (chunk.decode())
    │
    Вывод: AsyncResult

    Примеры:
        >>> model = "gpt-3.5-turbo"
        >>> messages = [{"role": "user", "content": "Hello"}]
        >>> async def run_generator():
        ...     async for chunk in Aibn.create_async_generator(model=model, messages=messages):
        ...         print(chunk, end="")
        >>> import asyncio
        >>> asyncio.run(run_generator())
    """
```

### `generate_signature`

```python
def generate_signature(timestamp: int, message: str, secret: str = "undefined"):
    """Генерирует подпись для запроса к API.

    Args:
        timestamp (int): Временная метка.
        message (str): Сообщение.
        secret (str, optional): Секретный ключ. По умолчанию "undefined".

    Returns:
        str: Сгенерированная подпись в формате SHA256.

    Как работает функция:
    1.  Функция `generate_signature` принимает временную метку, сообщение и секретный ключ (по умолчанию "undefined").
    2.  Формируется строка данных, объединяющая временную метку, сообщение и секретный ключ через двоеточие.
    3.  Вычисляется SHA256-хеш от полученной строки.
    4.  Возвращается шестнадцатеричное представление хеша.

    generate_signature
    │
    ├───Формирование данных (timestamp:message:secret)
    │   │
    │   └───SHA256 хеширование
    │
    Вывод: hex digest

    Примеры:
        >>> timestamp = int(time.time())
        >>> message = "Hello"
        >>> signature = generate_signature(timestamp, message)
        >>> print(signature)
        <example_signature>
    """