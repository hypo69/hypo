# Модуль Yqcloud
## Обзор

Модуль предоставляет класс `Yqcloud`, который является асинхронным провайдером для взаимодействия с API Yqcloud (https://chat9.yqcloud.top). Он позволяет генерировать текст на основе предоставленных сообщений с использованием модели GPT-4. Модуль поддерживает потоковую передачу данных, системные сообщения и историю сообщений.

## Подробней

Модуль `Yqcloud` предназначен для асинхронного взаимодействия с API Yqcloud для генерации текста. Он использует `aiohttp` для выполнения HTTP-запросов. Класс `Yqcloud` наследуется от `AsyncGeneratorProvider` и `ProviderModelMixin`, что позволяет ему предоставлять асинхронные генераторы для обработки ответов от API. Модуль также включает класс `Conversation` для управления историей сообщений и идентификатором пользователя.

## Классы

### `Conversation`

**Описание**: Класс для хранения истории сообщений и идентификатора пользователя в рамках одного диалога.
   
**Наследует**: `JsonConversation`

**Атрибуты**:
- `userId` (str): Уникальный идентификатор пользователя.
- `message_history` (Messages): Список сообщений в формате `typing.Messages`.

**Методы**:
- `__init__(self, model: str)`: Инициализирует объект `Conversation` с указанной моделью и генерирует уникальный `userId`.

### `Yqcloud`

**Описание**: Класс, предоставляющий функциональность для взаимодействия с API Yqcloud.

**Наследует**: `AsyncGeneratorProvider`, `ProviderModelMixin`

**Атрибуты**:
- `url` (str): URL сервиса Yqcloud.
- `api_endpoint` (str): URL API для генерации текста.
- `working` (bool): Флаг, указывающий, работает ли провайдер.
- `supports_stream` (bool): Флаг, указывающий, поддерживает ли провайдер потоковую передачу данных.
- `supports_system_message` (bool): Флаг, указывающий, поддерживает ли провайдер системные сообщения.
- `supports_message_history` (bool): Флаг, указывающий, поддерживает ли провайдер историю сообщений.
- `default_model` (str): Модель, используемая по умолчанию ("gpt-4").
- `models` (list[str]): Список поддерживаемых моделей (в данном случае только "gpt-4").

**Методы**:
- `create_async_generator(model: str, messages: Messages, stream: bool = True, proxy: str = None, conversation: Conversation = None, return_conversation: bool = False, **kwargs) -> AsyncResult`: Создает асинхронный генератор для получения ответов от API Yqcloud.

## Функции

### `create_async_generator`

```python
@classmethod
async def create_async_generator(
    cls,
    model: str,
    messages: Messages,
    stream: bool = True,
    proxy: str = None,
    conversation: Conversation = None,
    return_conversation: bool = False,
    **kwargs
) -> AsyncResult:
    """
    Создает асинхронный генератор для получения ответов от API Yqcloud.

    Args:
        model (str): Имя используемой модели.
        messages (Messages): Список сообщений для отправки в API.
        stream (bool): Флаг, указывающий, использовать ли потоковую передачу данных. По умолчанию `True`.
        proxy (str): Адрес прокси-сервера для использования при подключении к API. По умолчанию `None`.
        conversation (Conversation): Объект `Conversation` для хранения истории сообщений. По умолчанию `None`.
        return_conversation (bool): Флаг, указывающий, возвращать ли объект `Conversation` вместе с результатом. По умолчанию `False`.
        **kwargs: Дополнительные аргументы.

    Returns:
        AsyncResult: Асинхронный генератор, возвращающий ответы от API.

    Raises:
        Exception: Если возникает ошибка при выполнении запроса к API.
    """
    ...
```

**Назначение**: Создание асинхронного генератора для взаимодействия с API Yqcloud и получения ответов на основе предоставленных сообщений.

**Параметры**:
- `cls`: Ссылка на класс `Yqcloud`.
- `model` (str): Имя модели, которую необходимо использовать.
- `messages` (Messages): Список сообщений, отправляемых в API.
- `stream` (bool, optional): Флаг, указывающий, использовать ли потоковую передачу данных. По умолчанию `True`.
- `proxy` (str, optional): Адрес прокси-сервера. По умолчанию `None`.
- `conversation` (Conversation, optional): Объект `Conversation` для хранения истории сообщений. По умолчанию `None`.
- `return_conversation` (bool, optional): Флаг, указывающий, возвращать ли объект `Conversation` вместе с результатом. По умолчанию `False`.
- `**kwargs`: Дополнительные параметры.

**Возвращает**:
- `AsyncResult`: Асинхронный генератор, который возвращает ответы от API.

**Вызывает исключения**:
- `aiohttp.ClientResponseError`: Если возникает HTTP ошибка при запросе.

**Как работает функция**:
1. **Подготовка**:
   - Извлекает модель, приводя ее к допустимому значению.
   - Формирует заголовки запроса, включая `accept`, `accept-language`, `content-type`, `origin`, `referer` и `user-agent`.
   - Если объект `conversation` не предоставлен, создает новый экземпляр `Conversation`.
   - Обновляет историю сообщений в объекте `conversation`.
   - Извлекает системное сообщение из истории сообщений, если оно присутствует.

2. **Выполнение запроса**:
   - Использует `aiohttp.ClientSession` для выполнения асинхронного POST-запроса к `cls.api_endpoint`.
   - Формирует JSON-данные для запроса, включая `prompt`, `userId`, `network`, `system`, `withoutContext` и `stream`.

3. **Обработка ответа**:
   - Итерируется по чанкам в ответе, декодирует каждый чанк и передает его в генератор.
   - Собирает все чанки в `full_message`.

4. **Завершение**:
   - Если `return_conversation` установлен в `True`, добавляет ответ ассистента в историю сообщений и передает объект `conversation` в генератор.
   - Передает `FinishReason("stop")` в генератор, сигнализируя о завершении работы.

```text
    Начало
    │
    ├──►  Извлечение модели
    │
    ├──►  Формирование заголовков
    │
    ├──►  Создание/обновление conversation
    │
    ├──►  Извлечение системного сообщения (если есть)
    │
    ├──►  Создание сессии aiohttp
    │   │
    │   └──► Формирование данных запроса
    │   │
    │   └──► POST запрос к API
    │       │
    │       └──► Обработка чанков ответа
    │           │
    │           └──► Сборка полного сообщения
    │
    └──►  Возврат conversation (если return_conversation)
    │
    └──►  Завершение
```

**Примеры**:

```python
# Пример 1: Использование с минимальными параметрами
async for message in Yqcloud.create_async_generator(model="gpt-4", messages=[{"role": "user", "content": "Hello"}]):
    print(message)

# Пример 2: Использование с прокси и возвратом conversation
conversation = None
async for message in Yqcloud.create_async_generator(model="gpt-4", messages=[{"role": "user", "content": "Как дела?"}], proxy="http://proxy.example.com", return_conversation=True, conversation=conversation):
    if isinstance(message, Conversation):
        conversation = message
    else:
        print(message)

if conversation:
    print(conversation.message_history)

# Пример 3: Использование с системным сообщением
async for message in Yqcloud.create_async_generator(model="gpt-4", messages=[{"role": "system", "content": "Ты полезный ассистент"}, {"role": "user", "content": "Hello"}]):
    print(message)