# Модуль `Yqcloud.py`

## Обзор

Модуль предоставляет асинхронный класс `Yqcloud`, который используется для взаимодействия с сервисом `chat9.yqcloud.top`. Он позволяет генерировать ответы на основе предоставленных сообщений, поддерживая стриминг, системные сообщения и историю сообщений.

## Подробнее

Этот модуль является частью провайдеров для работы с различными языковыми моделями в проекте `hypotez`. Класс `Yqcloud` наследуется от `AsyncGeneratorProvider` и `ProviderModelMixin`, что позволяет ему асинхронно генерировать ответы и управлять моделями. Модуль использует `aiohttp` для асинхронных HTTP-запросов и форматирует запросы для соответствия требованиям API `Yqcloud`.

## Классы

### `Conversation`

**Описание**: Класс `Conversation` предназначен для хранения истории сообщений и идентификатора пользователя в рамках одного диалога.

**Наследует**:
- `JsonConversation`: Класс, обеспечивающий функциональность для работы с JSON-форматом истории сообщений.

**Атрибуты**:
- `userId` (str): Уникальный идентификатор пользователя, используемый для отслеживания диалога. По умолчанию `None`.
- `message_history` (Messages): Список сообщений, составляющих историю диалога. По умолчанию `[]`.
- `model` (str): Модель, используемая в диалоге.

**Методы**:
- `__init__(self, model: str)`: Инициализирует новый экземпляр класса `Conversation`.

### `Yqcloud`

**Описание**: Класс `Yqcloud` предоставляет интерфейс для взаимодействия с API `chat9.yqcloud.top`.

**Наследует**:
- `AsyncGeneratorProvider`: Класс для асинхронной генерации ответов.
- `ProviderModelMixin`: Класс, предоставляющий функциональность для выбора и управления моделями.

**Атрибуты**:
- `url` (str): Базовый URL сервиса `chat9.yqcloud.top`.
- `api_endpoint` (str): URL API для генерации ответов.
- `working` (bool): Флаг, указывающий на работоспособность провайдера.
- `supports_stream` (bool): Флаг, указывающий на поддержку стриминга ответов.
- `supports_system_message` (bool): Флаг, указывающий на поддержку системных сообщений.
- `supports_message_history` (bool): Флаг, указывающий на поддержку истории сообщений.
- `default_model` (str): Модель, используемая по умолчанию.
- `models` (List[str]): Список поддерживаемых моделей.

**Методы**:
- `create_async_generator(cls, model: str, messages: Messages, stream: bool = True, proxy: str = None, conversation: Conversation = None, return_conversation: bool = False, **kwargs) -> AsyncResult`: Асинхронно генерирует ответы на основе предоставленных сообщений.

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
    Асинхронно генерирует ответы на основе предоставленных сообщений.

    Args:
        model (str): Имя используемой модели.
        messages (Messages): Список сообщений для генерации ответа.
        stream (bool, optional): Флаг, указывающий на использование стриминга. По умолчанию `True`.
        proxy (str, optional): URL прокси-сервера. По умолчанию `None`.
        conversation (Conversation, optional): Объект `Conversation` для хранения истории сообщений. По умолчанию `None`.
        return_conversation (bool, optional): Флаг, указывающий на необходимость возврата объекта `Conversation`. По умолчанию `False`.
        **kwargs: Дополнительные аргументы.

    Returns:
        AsyncResult: Асинхронный генератор, возвращающий части ответа.

    Raises:
        Exception: Если возникает ошибка при запросе к API.

    """
```

**Назначение**: Генерация ответа от Yqcloud на основе предоставленных сообщений. Функция отвечает за взаимодействие с API `chat9.yqcloud.top`, отправку запросов и обработку ответов.

**Параметры**:
- `cls` (type): Ссылка на класс `Yqcloud`.
- `model` (str): Имя используемой модели.
- `messages` (Messages): Список сообщений для генерации ответа.
- `stream` (bool, optional): Флаг, указывающий на использование стриминга. По умолчанию `True`.
- `proxy` (str, optional): URL прокси-сервера. По умолчанию `None`.
- `conversation` (Conversation, optional): Объект `Conversation` для хранения истории сообщений. По умолчанию `None`.
- `return_conversation` (bool, optional): Флаг, указывающий на необходимость возврата объекта `Conversation`. По умолчанию `False`.
- `**kwargs`: Дополнительные аргументы.

**Возвращает**:
- `AsyncResult`: Асинхронный генератор, возвращающий части ответа.

**Вызывает исключения**:
- `Exception`: Если возникает ошибка при запросе к API.

**Как работает функция**:

1.  **Подготовка**:
    *   Извлекается имя модели.
    *   Формируются заголовки запроса, включающие `accept`, `accept-language`, `content-type`, `origin`, `referer` и `user-agent`.
    *   Проверяется, передан ли объект `conversation`. Если нет, создается новый экземпляр `Conversation`.

2.  **Обработка истории сообщений**:
    *   Если передан объект `conversation`, последнее сообщение добавляется в историю.
    *   Извлекается системное сообщение, если оно присутствует в начале истории сообщений.

3.  **Формирование запроса**:
    *   Форматируется запрос с использованием функции `format_prompt`.
    *   Формируются данные запроса, включающие `prompt`, `userId`, `network`, `system`, `withoutContext` и `stream`.

4.  **Отправка запроса и обработка ответа**:
    *   Отправляется POST-запрос к `cls.api_endpoint` с использованием `aiohttp.ClientSession`.
    *   Обрабатывается ответ по частям (chunks) с использованием асинхронного генератора.
    *   Каждая часть декодируется и возвращается через `yield`.
    *   Полное сообщение накапливается в переменной `full_message`.

5.  **Возврат результата**:
    *   Если `return_conversation` установлен в `True`, полное сообщение добавляется в историю `conversation`, и объект `conversation` возвращается через `yield`.
    *   В конце возвращается `FinishReason("stop")`, чтобы указать на завершение генерации.

**ASCII flowchart**:

```
    Начало
     ↓
  Подготовка данных (модель, заголовки, conversation)
     ↓
  Обработка истории сообщений (системное сообщение)
     ↓
  Формирование запроса (prompt, userId, network, system, withoutContext, stream)
     ↓
  Отправка POST-запроса к API
     ↓
  Обработка ответа по частям (декодирование, yield message, накопление full_message)
     ↓
  Условие: return_conversation == True?
     ├── Да → Добавление full_message в conversation и yield conversation
     └── Нет
     ↓
  Yield FinishReason("stop")
     ↓
    Конец
```

**Примеры**:

```python
# Пример 1: Генерация ответа с использованием стриминга и без прокси
messages = [{"role": "user", "content": "Hello, how are you?"}]
async for message in Yqcloud.create_async_generator(model="gpt-4", messages=messages):
    print(message)

# Пример 2: Генерация ответа с использованием прокси и возвратом conversation
messages = [{"role": "user", "content": "Tell me a joke."}]
async for message in Yqcloud.create_async_generator(model="gpt-4", messages=messages, proxy="http://your-proxy:8080", return_conversation=True):
    print(message)

# Пример 3: Генерация ответа с использованием существующего conversation
conversation = Conversation(model="gpt-4")
conversation.message_history = [{"role": "user", "content": "Hi!"}]
messages = [{"role": "user", "content": "What is your name?"}]
async for message in Yqcloud.create_async_generator(model="gpt-4", messages=messages, conversation=conversation, return_conversation=True):
    print(message)