# Модуль `Free2GPT`

## Обзор

Модуль `Free2GPT` предоставляет класс `Free2GPT`, который является асинхронным провайдером для взаимодействия с моделью Gemini через API `chat10.free2gpt.xyz`. Он поддерживает историю сообщений и предоставляет функциональность для генерации подписи запросов.

## Подробней

Этот модуль позволяет использовать Gemini 1.5 Pro и Gemini 1.5 Flash для генерации текста. Он включает в себя методы для создания асинхронного генератора, который отправляет запросы к API и возвращает чанки текста. Модуль также содержит функцию для генерации подписи, необходимой для аутентификации запросов.

## Классы

### `Free2GPT`

**Описание**: Класс `Free2GPT` предоставляет функциональность для взаимодействия с API `chat10.free2gpt.xyz`. Он наследуется от `AsyncGeneratorProvider` и `ProviderModelMixin`.

   **Наследует**:
   - `AsyncGeneratorProvider`: Обеспечивает базовую структуру для асинхронных генераторов.
   - `ProviderModelMixin`: Предоставляет функциональность для работы с моделями.

   **Атрибуты**:
   - `url` (str): URL API (`https://chat10.free2gpt.xyz`).
   - `working` (bool): Указывает, что провайдер работает (`True`).
   - `supports_message_history` (bool): Указывает, что провайдер поддерживает историю сообщений (`True`).
   - `default_model` (str): Модель, используемая по умолчанию (`gemini-1.5-pro`).
   - `models` (List[str]): Список поддерживаемых моделей (`[default_model, 'gemini-1.5-flash']`).

   **Методы**:
   - `create_async_generator`: Создает асинхронный генератор для отправки запросов к API.

#### `create_async_generator`

```python
@classmethod
async def create_async_generator(
    cls,
    model: str,
    messages: Messages,
    proxy: str = None,
    connector: BaseConnector = None,
    **kwargs,
) -> AsyncResult:
    """Создает асинхронный генератор для отправки запросов к API.

    Args:
        model (str): Модель для использования.
        messages (Messages): Список сообщений для отправки.
        proxy (str, optional): Прокси-сервер для использования. По умолчанию `None`.
        connector (BaseConnector, optional): Aiohttp коннектор. По умолчанию `None`.
        **kwargs: Дополнительные параметры.

    Returns:
        AsyncResult: Асинхронный генератор, возвращающий чанки текста.

    Raises:
        RateLimitError: Если достигнут лимит запросов.
        Exception: Если произошла ошибка при отправке запроса.
    """
    ...
```

**Назначение**: Создает асинхронный генератор, который отправляет запросы к API `chat10.free2gpt.xyz` и возвращает чанки текста.

**Параметры**:
- `cls` (type[Free2GPT]): Ссылка на класс `Free2GPT`.
- `model` (str): Модель для использования (`gemini-1.5-pro` или `gemini-1.5-flash`).
- `messages` (Messages): Список сообщений для отправки в запросе.
- `proxy` (str, optional): Прокси-сервер для использования. По умолчанию `None`.
- `connector` (BaseConnector, optional): Aiohttp коннектор для использования. По умолчанию `None`.
- `**kwargs`: Дополнительные параметры.

**Возвращает**:
- `AsyncResult`: Асинхронный генератор, возвращающий чанки текста из ответа API.

**Вызывает исключения**:
- `RateLimitError`: Если получен ответ со статусом 500 и сообщением "Quota exceeded".
- `Exception`: Если произошла другая ошибка при отправке или обработке запроса.

**Как работает функция**:

1. **Определение заголовков**: Определяются заголовки запроса, включая `User-Agent`, `Accept`, `Accept-Language`, `Accept-Encoding`, `Content-Type`, `Referer` и `Origin`.
2. **Создание сессии**: Создается асинхронная сессия `ClientSession` с использованием предоставленного коннектора и заголовков.
3. **Подготовка данных**: Создается словарь `data`, содержащий сообщения, текущее время и подпись, сгенерированную на основе времени и содержимого последнего сообщения.
4. **Отправка запроса**: Отправляется `POST` запрос к API (`f"{cls.url}/api/generate"`) с данными в формате `JSON`.
5. **Обработка ответа**:
   - Если статус ответа равен 500 и содержит "Quota exceeded", вызывается исключение `RateLimitError`.
   - В противном случае, проверяется статус ответа с помощью `raise_for_status`.
   - Извлекаются чанки из ответа и декодируются, после чего возвращаются через асинхронный генератор.

**Внутренние функции**:

   В данной функции не используются внутренние функции.

**ASCII flowchart**:

```
A: Определение заголовков
|
B: Создание сессии ClientSession
|
C: Подготовка данных (timestamp, sign)
|
D: Отправка POST запроса к API
|
E: Обработка ответа
|
F: Генерация чанков текста
```

**Примеры**:

```python
# Пример использования create_async_generator
import asyncio
from aiohttp import TCPConnector

async def main():
    model = 'gemini-1.5-pro'
    messages = [{"role": "user", "content": "Hello, how are you?"}]
    proxy = None
    connector = TCPConnector(limit=50)

    generator = await Free2GPT.create_async_generator(model=model, messages=messages, proxy=proxy, connector=connector)
    
    async for chunk in generator:
        print(chunk, end="")

if __name__ == "__main__":
    asyncio.run(main())
```

## Функции

### `generate_signature`

```python
def generate_signature(time: int, text: str, secret: str = ""):
    """Генерирует подпись для запроса на основе времени, текста и секрета.

    Args:
        time (int): Timestamp запроса.
        text (str): Текст сообщения.
        secret (str, optional): Секретный ключ. По умолчанию "".

    Returns:
        str: SHA256 хэш, представляющий подпись.
    """
    ...
```

**Назначение**: Генерирует подпись для запроса на основе времени, текста и секретного ключа.

**Параметры**:
- `time` (int): Timestamp запроса.
- `text` (str): Текст сообщения.
- `secret` (str, optional): Секретный ключ. По умолчанию пустая строка.

**Возвращает**:
- `str`: SHA256 хэш, представляющий подпись.

**Вызывает исключения**:
- Отсутствуют.

**Как работает функция**:

1. **Формирование сообщения**: Формируется строка сообщения путем объединения времени, текста и секрета через двоеточие (`f"{time}:{text}:{secret}"`).
2. **Кодирование сообщения**: Сообщение кодируется в байты с использованием кодировки UTF-8.
3. **Хеширование сообщения**: Вычисляется SHA256 хэш закодированного сообщения.
4. **Возврат хэша**: Возвращается шестнадцатеричное представление SHA256 хэша.

**Внутренние функции**:

В данной функции не используются внутренние функции.

**ASCII flowchart**:

```
A: Формирование сообщения
|
B: Кодирование сообщения в байты
|
C: Вычисление SHA256 хэша
|
D: Возврат шестнадцатеричного представления хэша
```

**Примеры**:

```python
# Пример использования generate_signature
import time

timestamp = int(time.time() * 1e3)
text = "Hello, how are you?"
signature = generate_signature(timestamp, text)
print(f"Signature: {signature}")