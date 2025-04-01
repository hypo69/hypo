# Модуль интеграции g4f с Langchain

## Обзор

Модуль предоставляет интеграцию между библиотекой `g4f` (библиотека для доступа к различным моделям ИИ) и фреймворком `Langchain`. Он включает в себя переопределение функции преобразования сообщений и класс `ChatAI`, который расширяет возможности `ChatOpenAI` из `Langchain` для использования с `g4f`.

## Подробнее

Этот модуль позволяет использовать модели, доступные через `g4f`, в цепочках `Langchain`. Это достигается путем переопределения способа преобразования сообщений и создания класса `ChatAI`, который настраивает клиент `g4f` для взаимодействия с этими моделями. Расположение файла в проекте указывает на то, что он предназначен для расширения возможностей `Langchain` за счет интеграции с различными моделями ИИ, доступными через `g4f`.

## Функции

### `new_convert_message_to_dict`

```python
def new_convert_message_to_dict(message: BaseMessage) -> dict:
    """Преобразует объект сообщения (BaseMessage) в словарь.

    Args:
        message (BaseMessage): Объект сообщения для преобразования.

    Returns:
        dict: Словарь, представляющий сообщение.

    Как работает функция:
     1. **Проверка типа сообщения**: Функция проверяет, является ли входное сообщение экземпляром `ChatCompletionMessage`.
     2. **Обработка ChatCompletionMessage**: Если сообщение является экземпляром `ChatCompletionMessage`, создается словарь `message_dict` со следующими ключами:
        - `"role"`: Роль сообщения (например, "user", "assistant").
        - `"content"`: Содержимое сообщения.
        - `"tool_calls"`: Список вызовов инструментов, если они есть в сообщении. Каждый вызов инструмента преобразуется в словарь с ключами `"id"`, `"type"` и `"function"`.
        Если содержимое сообщения пустое, оно устанавливается в `None`.
     3. **Обработка других типов сообщений**: Если сообщение не является экземпляром `ChatCompletionMessage`, используется стандартная функция `convert_message_to_dict` из модуля `openai` для преобразования сообщения в словарь.
     4. **Возврат результата**: Функция возвращает словарь, представляющий сообщение.

     ASCII-схема работы функции:

     Начало
     ↓
     isinstance(message, ChatCompletionMessage)?
     ├── Да → Создать message_dict с данными из message, преобразовать tool_calls
     │       Если message_dict["content"] == "": message_dict["content"] = None
     └── Нет → message_dict = convert_message_to_dict(message)
     ↓
     Возврат message_dict

    Example:
        >>> from langchain_community.messages import HumanMessage
        >>> message = HumanMessage(content="Hello")
        >>> new_convert_message_to_dict(message)
        {'content': 'Hello', 'additional_kwargs': {}, 'type': 'human'}

        >>> from g4f.client.stubs import ChatCompletionMessage, ToolCall
        >>> tool_call = ToolCall(id='123', type='function', function={'name': 'my_function', 'arguments': '{"arg1": "value1"}'})
        >>> message = ChatCompletionMessage(role="assistant", content="Tool call", tool_calls=[tool_call])
        >>> new_convert_message_to_dict(message)
        {'role': 'assistant', 'content': 'Tool call', 'tool_calls': [{'id': '123', 'type': 'function', 'function': {'name': 'my_function', 'arguments': '{"arg1": "value1"}'}}]}
    """
    message_dict: Dict[str, Any]
    if isinstance(message, ChatCompletionMessage):
        message_dict = {"role": message.role, "content": message.content}
        if message.tool_calls is not None:
            message_dict["tool_calls"] = [{
                "id": tool_call.id,
                "type": tool_call.type,
                "function": tool_call.function
            } for tool_call in message.tool_calls]
            if message_dict["content"] == "":
                message_dict["content"] = None
    else:
        message_dict = convert_message_to_dict(message)
    return message_dict
```

## Классы

### `ChatAI`

```python
class ChatAI(ChatOpenAI):
    """Наследует ChatOpenAI и расширяет его функциональность для работы с моделями g4f.

    Inherits:
        ChatOpenAI: Базовый класс для работы с моделями OpenAI.

    Attributes:
        model_name (str): Имя модели, по умолчанию "gpt-4o".
        client: Клиент для выполнения запросов к моделям g4f.
        async_client: Асинхронный клиент для выполнения асинхронных запросов к моделям g4f.

    Methods:
        validate_environment(cls, values: dict) -> dict: Проверяет и настраивает окружение для работы с g4f.
    """

    model_name: str = Field(default="gpt-4o", alias="model")

    @classmethod
    def validate_environment(cls, values: dict) -> dict:
        """Проверяет и настраивает окружение для работы с g4f.

        Args:
            values (dict): Словарь с параметрами для настройки окружения.

        Returns:
            dict: Обновленный словарь с настроенным окружением.

        Как работает функция:
        1. **Извлечение параметров клиента**: Функция извлекает параметры для инициализации клиента `g4f` из входного словаря `values`. Это включает в себя `api_key` и `provider` (если они указаны).
        2. **Создание клиентов**: На основе извлеченных параметров создаются два клиента: синхронный (`Client`) и асинхронный (`AsyncClient`). Эти клиенты используются для выполнения запросов к моделям `g4f`.
        3. **Сохранение клиентов в values**: Созданные клиенты сохраняются в словаре `values` под ключами `"client"` и `"async_client"`.
        4. **Возврат обновленного словаря**: Функция возвращает обновленный словарь `values` с настроенными клиентами.

        ASCII-схема работы функции:

        Начало
        ↓
        Извлечение api_key и provider из values
        ↓
        Создание синхронного клиента Client(**client_params)
        ↓
        Создание асинхронного клиента AsyncClient(**client_params)
        ↓
        Сохранение клиентов в values
        ↓
        Возврат values

        Example:
            >>> ChatAI.validate_environment({"api_key": "test_key", "model_kwargs": {"provider": "test_provider"}})
            {'api_key': 'test_key', 'model_kwargs': {'provider': 'test_provider'}, 'client': <g4f.client.chat.completions object at 0x...>, 'async_client': <g4f.client.chat.completions object at 0x...>}
        """
        client_params = {
            "api_key": values["api_key"] if "api_key" in values else None,
            "provider": values["model_kwargs"]["provider"] if "provider" in values["model_kwargs"] else None,
        }
        values["client"] = Client(**client_params).chat.completions
        values["async_client"] = AsyncClient(
            **client_params
        ).chat.completions
        return values