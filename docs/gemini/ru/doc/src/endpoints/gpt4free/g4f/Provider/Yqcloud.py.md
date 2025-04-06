# Модуль Yqcloud

## Обзор

Модуль `Yqcloud` предоставляет асинхронный генератор для взаимодействия с сервисом `chat9.yqcloud.top`. 
Он позволяет генерировать текст на основе предоставленных сообщений, поддерживая потоковую передачу данных, системные сообщения и историю сообщений.

## Подробней

Модуль предназначен для интеграции с API `binjie.fun` через асинхронные запросы. Он использует `aiohttp` для выполнения HTTP-запросов и предоставляет возможность работы через прокси. Поддерживает сохранение истории разговоров и возвращает её при необходимости.

## Классы

### `Conversation`

**Описание**: Класс для хранения информации о разговоре.

**Наследует**:

- `JsonConversation`: Предоставляет функциональность для сериализации и десериализации разговора в JSON.

**Атрибуты**:

- `userId` (str): Уникальный идентификатор пользователя. По умолчанию `None`.
- `message_history` (Messages): Список сообщений в истории разговора. По умолчанию `[]`.
- `model` (str): Модель, используемая в разговоре.

**Методы**:

- `__init__(self, model: str)`: Инициализирует новый экземпляр класса `Conversation`.
    - `model` (str): Модель, используемая в разговоре.
    - Устанавливает `self.model` в переданное значение `model`.
    - Генерирует уникальный `userId` на основе текущего времени.

### `Yqcloud`

**Описание**: Класс, реализующий асинхронный генератор для взаимодействия с API `Yqcloud`.

**Наследует**:

- `AsyncGeneratorProvider`: Предоставляет базовую функциональность для асинхронных генераторов.
- `ProviderModelMixin`: Добавляет функциональность для работы с моделями.

**Атрибуты**:

- `url` (str): Базовый URL сервиса `chat9.yqcloud.top`.
- `api_endpoint` (str): URL API для генерации текста `api.binjie.fun/api/generateStream`.
- `working` (bool): Указывает, работает ли провайдер. Всегда `True`.
- `supports_stream` (bool): Указывает, поддерживает ли провайдер потоковую передачу данных. Всегда `True`.
- `supports_system_message` (bool): Указывает, поддерживает ли провайдер системные сообщения. Всегда `True`.
- `supports_message_history` (bool): Указывает, поддерживает ли провайдер историю сообщений. Всегда `True`.
- `default_model` (str): Модель, используемая по умолчанию `"gpt-4"`.
- `models` (list): Список поддерживаемых моделей `[default_model]`.

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
    """Создает асинхронный генератор для генерации текста с использованием API Yqcloud.

    Args:
        model (str): Модель для генерации текста.
        messages (Messages): Список сообщений для отправки в API.
        stream (bool, optional): Флаг, указывающий, использовать ли потоковую передачу данных. По умолчанию `True`.
        proxy (str, optional): URL прокси-сервера для использования. По умолчанию `None`.
        conversation (Conversation, optional): Объект разговора для сохранения истории. По умолчанию `None`.
        return_conversation (bool, optional): Флаг, указывающий, возвращать ли объект разговора после завершения. По умолчанию `False`.
        **kwargs: Дополнительные параметры.

    Returns:
        AsyncResult: Асинхронный генератор, возвращающий текст от API.

    Как работает функция:
     1. **Инициализация**:
        - Получает модель, используя `cls.get_model(model)`.
        - Определяет заголовки запроса, включая `accept`, `accept-language`, `content-type`, `origin`, `referer` и `user-agent`.
     2. **Обработка истории разговора**:
        - Если `conversation` не предоставлен, создает новый экземпляр `Conversation(model)`.
        - Если `conversation` предоставлен, добавляет последнее сообщение из `messages` в историю разговора.
     3. **Извлечение системного сообщения**:
        - Проверяет, есть ли системное сообщение в начале списка сообщений. Если есть, извлекает его содержимое и удаляет из списка.
     4. **Формирование запроса**:
        - Форматирует сообщения с помощью `format_prompt(current_messages)`.
        - Формирует данные для отправки в API, включая `prompt`, `userId`, `network`, `system`, `withoutContext` и `stream`.
     5. **Отправка запроса и обработка ответа**:
        - Использует `aiohttp.ClientSession` для отправки POST-запроса к `cls.api_endpoint` с данными и заголовками.
        - Обрабатывает ответ от API по частям (chunks) и декодирует каждую часть.
        - Передает декодированные части через генератор.
     6. **Сохранение истории и завершение**:
        - Если `return_conversation` установлен в `True`, добавляет ответ ассистента в историю разговора и передает объект разговора через генератор.
        - Завершает генератор, передавая `FinishReason("stop")`.

    ASCII flowchart:

    ```
    Начало
    │
    Получение модели
    │
    Определение заголовков
    │
    Обработка истории разговора
    │
    Извлечение системного сообщения
    │
    Формирование запроса
    │
    Отправка POST-запроса
    │
    Обработка ответа по частям
    │
    Сохранение истории (если нужно)
    │
    Завершение
    │
    Конец
    ```

    Примеры:
    ```python
    # Пример вызова функции с минимальными параметрами
    async for message in Yqcloud.create_async_generator(model="gpt-4", messages=[{"role": "user", "content": "Hello"}]):
        print(message)

    # Пример вызова функции с использованием прокси и возвратом истории разговора
    async for message in Yqcloud.create_async_generator(model="gpt-4", messages=[{"role": "user", "content": "Hello"}], proxy="http://proxy.example.com", return_conversation=True):
        print(message)

    # Пример с указанием conversation
    conversation = Conversation(model="gpt-4")
    async for message in Yqcloud.create_async_generator(model="gpt-4", messages=[{"role": "user", "content": "Hello"}], conversation=conversation):
        print(message)
    ```
    """
    model = cls.get_model(model)
    headers = {
        "accept": "application/json, text/plain, */*",
        "accept-language": "en-US,en;q=0.9",
        "content-type": "application/json",
        "origin": f"{cls.url}",
        "referer": f"{cls.url}/",
        "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"
    }
    
    if conversation is None:
        conversation = Conversation(model)
        conversation.message_history = messages
    else:
        conversation.message_history.append(messages[-1])

    # Extract system message if present
    system_message = ""
    current_messages = conversation.message_history
    if current_messages and current_messages[0]["role"] == "system":
        system_message = current_messages[0]["content"]
        current_messages = current_messages[1:]
    
    async with ClientSession(headers=headers) as session:
        prompt = format_prompt(current_messages)
        data = {
            "prompt": prompt,
            "userId": conversation.userId,
            "network": True,
            "system": system_message,
            "withoutContext": False,
            "stream": stream
        }
        
        async with session.post(cls.api_endpoint, json=data, proxy=proxy) as response:
            await raise_for_status(response)
            full_message = ""
            async for chunk in response.content:
                if chunk:
                    message = chunk.decode()
                    yield message
                    full_message += message

            if return_conversation:
                conversation.message_history.append({"role": "assistant", "content": full_message})
                yield conversation
            
            yield FinishReason("stop")