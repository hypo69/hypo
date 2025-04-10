# Модуль `AIChatFree`

## Обзор

Модуль `AIChatFree` предоставляет асинхронный интерфейс для взаимодействия с сервисом AIChatFree. Он позволяет генерировать текст на основе предоставленных сообщений, используя модель `gemini-1.5-pro` по умолчанию. Модуль поддерживает потоковую передачу данных и сохранение истории сообщений.

## Подробнее

Модуль предназначен для интеграции с другими компонентами проекта `hypotez`, требующими функциональности генерации текста с использованием AI. Он использует асинхронные запросы для обеспечения неблокирующей работы и эффективного использования ресурсов. В частности, модуль применяется для обхода ограничений, связанных с бесплатным доступом к API, а также предоставляет удобный интерфейс для работы с моделью `gemini-1.5-pro`.

## Классы

### `AIChatFree`

**Описание**: Класс `AIChatFree` является провайдером для работы с сервисом AIChatFree. Он наследует функциональность от `AsyncGeneratorProvider` и `ProviderModelMixin`, что обеспечивает поддержку асинхронной генерации и выбора моделей.

**Принцип работы**:
1.  При инициализации класса задаются параметры подключения к сервису, включая URL, заголовки и флаги поддержки потоковой передачи и истории сообщений.
2.  Метод `create_async_generator` создает асинхронный генератор, который отправляет запросы к API AIChatFree и возвращает чанки сгенерированного текста.
3.  Для каждого запроса генерируется цифровая подпись, которая обеспечивает безопасность и целостность передаваемых данных.
4.  Полученные чанки декодируются и передаются вызывающей стороне через асинхронный генератор.

**Методы**:

*   `create_async_generator`: Создает асинхронный генератор для получения сгенерированного текста от AIChatFree.

**Параметры**:

*   `url` (str): URL сервиса AIChatFree.
*   `working` (bool): Указывает, работает ли провайдер в данный момент.
*   `supports_stream` (bool): Указывает, поддерживает ли провайдер потоковую передачу данных.
*   `supports_message_history` (bool): Указывает, поддерживает ли провайдер историю сообщений.
*   `default_model` (str): Модель, используемая по умолчанию (`gemini-1.5-pro`).

## Функции

### `create_async_generator`

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
    """
    Создает асинхронный генератор для получения сгенерированного текста от AIChatFree.

    Args:
        model (str): Имя используемой модели.
        messages (Messages): Список сообщений для генерации текста.
        proxy (Optional[str], optional): URL прокси-сервера. По умолчанию `None`.
        connector (Optional[BaseConnector], optional): Aiohttp коннектор. По умолчанию `None`.

    Returns:
        AsyncResult: Асинхронный генератор, выдающий чанки сгенерированного текста.

    Raises:
        RateLimitError: Если достигнут лимит запросов.
        Exception: Если произошла ошибка при выполнении запроса.
    """
```

**Назначение**: Функция `create_async_generator` создает асинхронный генератор, который отправляет запросы к API AIChatFree и возвращает чанки сгенерированного текста.

**Параметры**:

*   `cls`: Ссылка на класс `AIChatFree`.
*   `model` (str): Имя используемой модели.
*   `messages` (Messages): Список сообщений для генерации текста.
*   `proxy` (Optional[str], optional): URL прокси-сервера. По умолчанию `None`.
*   `connector` (Optional[BaseConnector], optional): Aiohttp коннектор. По умолчанию `None`.
*   `**kwargs`: Дополнительные аргументы.

**Возвращает**:

*   `AsyncResult`: Асинхронный генератор, выдающий чанки сгенерированного текста.

**Вызывает исключения**:

*   `RateLimitError`: Если достигнут лимит запросов.
*   `Exception`: Если произошла ошибка при выполнении запроса.

**Как работает функция**:

1.  **Подготовка заголовков**: Функция создает заголовки HTTP-запроса, включая User-Agent, Accept, Accept-Language, Accept-Encoding, Content-Type, Referer и Origin.
2.  **Создание сессии**: Создается асинхронная сессия с использованием `ClientSession` и переданного коннектора (или коннектора по умолчанию).
3.  **Формирование данных**: Формируются данные для отправки в теле запроса, включая список сообщений, временную метку и подпись. Сообщения преобразуются в формат, ожидаемый API AIChatFree.
4.  **Отправка запроса**: Отправляется POST-запрос к API AIChatFree по адресу `f"{cls.url}/api/generate"` с использованием созданной сессии.
5.  **Обработка ответа**:
    *   Проверяется статус ответа. Если статус равен 500 и в тексте ответа содержится "Quota exceeded", выбрасывается исключение `RateLimitError`.
    *   Если статус ответа не указывает на ошибку, начинается чтение данных из ответа чанками.
    *   Каждый чанк декодируется и возвращается через асинхронный генератор.
6.  **Обработка ошибок**: В случае возникновения ошибок при выполнении запроса или обработке ответа, выбрасывается исключение `Exception`.

**Внутренние функции**: Отсутствуют.

**ASCII flowchart**:

```
    Заголовки HTTP   Данные запроса    Отправка запроса  Обработка ответа
    │                 │                 │                  │
    User-Agent,       Сообщения,        POST to           Чтение чанков,
    Accept, ...       Временная метка,  AIChatFree API    Декодирование,
    │                 Подпись           │                  Выдача через генератор
    Создание сессии   │                 Проверка статуса │
    │                 │                 │                  │
    ClientSession     └──>              └──>               └──>
```

**Примеры**:

```python
import asyncio
from src.endpoints.gpt4free.g4f.Provider.not_working.AIChatFree import AIChatFree
from src.logger import logger

async def main():
    messages = [
        {"role": "user", "content": "Привет, как дела?"},
        {"role": "assistant", "content": "Привет! У меня все хорошо, спасибо. Как я могу тебе помочь?"}
    ]
    try:
        async for chunk in AIChatFree.create_async_generator(model="gemini-1.5-pro", messages=messages):
            print(chunk, end="")
    except Exception as ex:
        logger.error(f"Error occurred: {ex}", exc_info=True)

if __name__ == "__main__":
    asyncio.run(main())
```

### `generate_signature`

```python
def generate_signature(time: int, text: str, secret: str = ""):
    """
    Генерирует подпись для запроса к API AIChatFree.

    Args:
        time (int): Временная метка.
        text (str): Текст сообщения.
        secret (str, optional): Секретный ключ. По умолчанию "".

    Returns:
        str: Сгенерированная подпись.
    """
```

**Назначение**: Функция `generate_signature` генерирует подпись для запроса к API AIChatFree. Подпись используется для проверки целостности и подлинности запроса.

**Параметры**:

*   `time` (int): Временная метка.
*   `text` (str): Текст сообщения.
*   `secret` (str, optional): Секретный ключ. По умолчанию "".

**Возвращает**:

*   `str`: Сгенерированная подпись.

**Вызывает исключения**:

*   Нет.

**Как работает функция**:

1.  **Формирование сообщения**: Функция формирует строку сообщения, объединяя временную метку, текст сообщения и секретный ключ через двоеточие.
2.  **Вычисление хеша**: Вычисляется SHA256 хеш от сформированной строки сообщения.
3.  **Возврат подписи**: Функция возвращает вычисленный хеш в виде шестнадцатеричной строки.

**Внутренние функции**: Отсутствуют.

**ASCII flowchart**:

```
    Входные данные    Формирование сообщения    Вычисление хеша    Возврат подписи
    │                 │                         │                  │
    time, text,       time:text:secret          SHA256(message)    hex(hash)
    secret            │                         │                  │
    │                 └──>                      └──>               └──>
```

**Примеры**:

```python
from src.endpoints.gpt4free.g4f.Provider.not_working.AIChatFree import generate_signature
import time

timestamp = int(time.time() * 1e3)
text = "Привет, как дела?"
signature = generate_signature(timestamp, text)
print(f"Signature: {signature}")