# Модуль `FreeGpt`

## Обзор

Модуль `FreeGpt` предоставляет асинхронтный генератор для взаимодействия с сервисом FreeGpt. Он поддерживает работу с историей сообщений и системными сообщениями, а также предоставляет возможность выбора модели.

## Подробней

Модуль предназначен для отправки запросов к API FreeGpt и получения ответов в виде асинхронного генератора. Он включает в себя функции для создания запросов, обработки ответов и генерации подписи для обеспечения безопасности.

## Классы

### `FreeGpt`

**Описание**: Класс `FreeGpt` является асинхронным провайдером генератора, который взаимодействует с API FreeGpt для генерации текста на основе предоставленных сообщений.

**Наследует**:

- `AsyncGeneratorProvider`: Обеспечивает базовую функциональность для асинхронных провайдеров генераторов.
- `ProviderModelMixin`: Предоставляет методы для работы с моделями.

**Атрибуты**:

- `url` (str): URL для доступа к сервису FreeGpt.
- `working` (bool): Флаг, указывающий, работает ли провайдер.
- `supports_message_history` (bool): Флаг, указывающий, поддерживает ли провайдер историю сообщений.
- `supports_system_message` (bool): Флаг, указывающий, поддерживает ли провайдер системные сообщения.
- `default_model` (str): Модель, используемая по умолчанию (`gemini-1.5-pro`).
- `models` (List[str]): Список поддерживаемых моделей (`gemini-1.5-pro`, `gemini-1.5-flash`).

**Методы**:

- `create_async_generator()`: Создает асинхронный генератор для получения ответов от API FreeGpt.
- `_build_request_data()`: Статический метод для создания данных запроса.

### `create_async_generator`

```python
@classmethod
async def create_async_generator(
    cls,
    model: str,
    messages: Messages,
    proxy: Optional[str] = None,
    timeout: int = 120,
    **kwargs: Any
) -> AsyncGenerator[str, None]:
    """
    Создает асинхронный генератор для получения ответов от API FreeGpt.

    Args:
        model (str): Название используемой модели.
        messages (Messages): Список сообщений для отправки в API.
        proxy (Optional[str], optional): Прокси-сервер для использования. По умолчанию `None`.
        timeout (int, optional): Время ожидания ответа от сервера. По умолчанию 120.
        **kwargs (Any): Дополнительные аргументы.

    Returns:
        AsyncGenerator[str, None]: Асинхронный генератор, возвращающий части ответа от API.

    Raises:
        RateLimitError: Если достигнут лимит запросов.

    """
```

**Назначение**: Создает асинхронный генератор, который отправляет запросы к API FreeGpt и возвращает ответы в виде потока чанков текста.

**Параметры**:

- `model` (str): Название модели, которую нужно использовать для генерации ответа.
- `messages` (Messages): Список сообщений, которые нужно отправить в API.
- `proxy` (Optional[str], optional): Прокси-сервер, который нужно использовать для подключения к API. По умолчанию `None`.
- `timeout` (int, optional): Максимальное время ожидания ответа от API в секундах. По умолчанию 120.
- `**kwargs (Any)`: Дополнительные параметры, которые можно передать в API.

**Возвращает**:

- `AsyncGenerator[str, None]`: Асинхронный генератор, который выдает части ответа от API в виде строк.

**Вызывает исключения**:

- `RateLimitError`: Вызывается, если достигнут лимит запросов к API.

**Как работает функция**:

1. **Извлечение промпта и текущего времени**: Извлекается последнее сообщение пользователя (промпт) и текущее время в формате timestamp.
2. **Построение данных запроса**: Вызывается метод `_build_request_data` для создания данных запроса, включая сообщения, timestamp и подпись.
3. **Выбор домена**: Случайно выбирается один из доступных доменов из списка `DOMAINS`.
4. **Отправка запроса и обработка ответа**:
   - Открывается асинхронная сессия с использованием `StreamSession`.
   - Отправляется POST-запрос к API с использованием выбранного домена и данных запроса.
   - Проверяется статус ответа с помощью `raise_for_status`.
   - Итерируется по чанкам ответа, декодируя каждый чанк и проверяя на наличие сообщения об ошибке `RATE_LIMIT_ERROR_MESSAGE`.
   - Если обнаружено сообщение об ошибке, вызывается исключение `RateLimitError`.
   - Каждый декодированный чанк выдается через генератор.

```
    Начало
    │
    ├── prompt, timestamp = messages[-1]["content"], int(time.time())
    │
    ├── data = cls._build_request_data(messages, prompt, timestamp)
    │
    ├── domain = random.choice(DOMAINS)
    │
    ├── async with StreamSession() as session
    │   │
    │   ├── async with session.post(f"{domain}/api/generate", json=data) as response
    │   │   │
    │   │   ├── await raise_for_status(response)
    │   │   │
    │   │   ├── async for chunk in response.iter_content()
    │   │   │   │
    │   │   │   ├── chunk_decoded = chunk.decode(errors="ignore")
    │   │   │   │
    │   │   │   ├── if chunk_decoded == RATE_LIMIT_ERROR_MESSAGE: raise RateLimitError("Rate limit reached")
    │   │   │   │
    │   │   │   └── yield chunk_decoded
    │   │   │
    │   │   └── Конец цикла по чанкам
    │   │
    │   └── Конец POST-запроса
    │
    └── Конец сессии
```

**Примеры**:

```python
# Пример использования create_async_generator
messages = [{"role": "user", "content": "Напиши короткий рассказ."}]
async def main():
    generator = await FreeGpt.create_async_generator(model="gemini-1.5-pro", messages=messages)
    async for chunk in generator:
        print(chunk, end="")

# Запуск примера (только в асинхронной среде)
# import asyncio
# asyncio.run(main())
```

### `_build_request_data`

```python
    @staticmethod
    def _build_request_data(messages: Messages, prompt: str, timestamp: int, secret: str = "") -> Dict[str, Any]:
        """
        Создает словарь с данными запроса для отправки в API.

        Args:
            messages (Messages): Список сообщений для отправки.
            prompt (str): Последнее сообщение пользователя (промпт).
            timestamp (int): Timestamp запроса.
            secret (str, optional): Секретный ключ для подписи. По умолчанию "".

        Returns:
            Dict[str, Any]: Словарь с данными запроса.
        """
```

**Назначение**: Создает словарь с данными запроса, который будет отправлен в API FreeGpt.

**Параметры**:

- `messages` (Messages): Список сообщений, которые нужно отправить в API.
- `prompt` (str): Последнее сообщение пользователя (промпт).
- `timestamp` (int): Timestamp запроса.
- `secret` (str, optional): Секретный ключ для подписи запроса. По умолчанию "".

**Возвращает**:

- `Dict[str, Any]`: Словарь с данными запроса, который включает сообщения, timestamp, параметр `pass` (установлен в `None`) и подпись.

**Как работает функция**:

1. **Создание данных для подписи**: Формируется строка данных для создания подписи, включающая timestamp, сообщение и секретный ключ.
2. **Создание словаря данных**: Создается словарь, содержащий сообщения, timestamp, `pass` (установлен в `None`) и подпись.
3. **Возврат словаря**: Возвращается словарь с данными запроса.

```
    Начало
    │
    ├── Формирование данных для подписи: f"{timestamp}:{message}:{secret}"
    │
    ├── Создание подписи: generate_signature(timestamp, prompt, secret)
    │
    ├── Создание словаря данных запроса: {"messages": messages, "time": timestamp, "pass": None, "sign": signature}
    │
    └── Возврат словаря данных запроса
```

**Примеры**:

```python
# Пример использования _build_request_data
messages = [{"role": "user", "content": "Напиши короткий рассказ."}]
timestamp = int(time.time())
data = FreeGpt._build_request_data(messages, "Напиши короткий рассказ.", timestamp)
print(data)
```

## Функции

### `generate_signature`

```python
def generate_signature(timestamp: int, message: str, secret: str = "") -> str:
    """
    Генерирует подпись для запроса.

    Args:
        timestamp (int): Timestamp запроса.
        message (str): Сообщение для подписи.
        secret (str, optional): Секретный ключ. По умолчанию "".

    Returns:
        str: Подпись запроса.
    """
```

**Назначение**: Генерирует подпись для запроса к API, используя алгоритм SHA256.

**Параметры**:

- `timestamp` (int): Timestamp запроса.
- `message` (str): Сообщение, которое нужно подписать.
- `secret` (str, optional): Секретный ключ для подписи. По умолчанию "".

**Возвращает**:

- `str`: Подпись запроса в виде шестнадцатеричной строки.

**Как работает функция**:

1. **Формирование строки данных**: Формируется строка данных, включающая timestamp, сообщение и секретный ключ, разделенные двоеточиями.
2. **Кодирование строки**: Строка данных кодируется в байты с использованием кодировки UTF-8.
3. **Вычисление хеша SHA256**: Вычисляется хеш SHA256 от закодированной строки.
4. **Преобразование в шестнадцатеричную строку**: Хеш преобразуется в шестнадцатеричную строку.
5. **Возврат подписи**: Возвращается подпись в виде шестнадцатеричной строки.

```
    Начало
    │
    ├── Формирование строки данных: f"{timestamp}:{message}:{secret}"
    │
    ├── Кодирование строки в байты
    │
    ├── Вычисление хеша SHA256
    │
    ├── Преобразование хеша в шестнадцатеричную строку
    │
    └── Возврат подписи
```

**Примеры**:

```python
# Пример использования generate_signature
timestamp = int(time.time())
message = "Напиши короткий рассказ."
signature = generate_signature(timestamp, message)
print(signature)