# Модуль интеграции Langchain с g4f
## Обзор

Модуль предоставляет интеграцию между библиотекой Langchain и g4f (GenerativeForFree), позволяя использовать модели g4f в качестве чат-моделей Langchain. В частности, он переопределяет функции преобразования сообщений и создает класс `ChatAI`, который расширяет `ChatOpenAI` из Langchain для работы с моделями g4f.

## Подробней

Этот модуль позволяет использовать модели, предоставляемые g4f, в пайплайнах Langchain. Это достигается путем замены стандартной функции преобразования сообщений Langchain и создания класса `ChatAI`, который адаптирован для работы с g4f. Модуль обеспечивает совместимость между Langchain и g4f, упрощая использование различных моделей в Langchain.

## Функции

### `new_convert_message_to_dict`

```python
def new_convert_message_to_dict(message: BaseMessage) -> dict:
    """Преобразует объект сообщения (BaseMessage) в словарь, пригодный для использования в API чат-моделей.

    Args:
        message (BaseMessage): Объект сообщения, который необходимо преобразовать.

    Returns:
        dict: Словарь, представляющий сообщение. Содержит ключи 'role' (роль отправителя), 'content' (содержимое сообщения) и, при наличии, 'tool_calls' (информация о вызовах инструментов).

    Как работает функция:
    1. Проверяет, является ли сообщение экземпляром класса `ChatCompletionMessage`.
    2. Если да, то создает словарь `message_dict` с ключами 'role' и 'content', взятыми из атрибутов объекта `message`.
    3. Если в `message` присутствует атрибут `tool_calls`, то добавляет в `message_dict` ключ 'tool_calls', значением которого является список словарей, описывающих каждый вызов инструмента. Каждый словарь содержит ключи 'id', 'type' и 'function', соответствующие атрибутам объекта `tool_call`.
    4. Если `message_dict["content"]` равно пустой строке, то устанавливает значение `message_dict["content"]` в `None`.
    5. Если сообщение не является экземпляром `ChatCompletionMessage`, то использует стандартную функцию `convert_message_to_dict` из модуля `openai` для преобразования сообщения в словарь.

    Внутри функции происходят следующие действия и преобразования:
    A. **Проверка типа сообщения:** Определяется, является ли входящее сообщение типом `ChatCompletionMessage`.
    |
    B. **Обработка ChatCompletionMessage:** Если сообщение является `ChatCompletionMessage`, извлекаются роль, содержимое и, при наличии, вызовы инструментов.
    |
    C. **Преобразование вызовов инструментов:** Если есть вызовы инструментов, они преобразуются в формат словаря.
    |
    D. **Обработка пустого содержимого:** Если содержимое сообщения пустое, оно устанавливается в `None`.
    |
    E. **Обработка других типов сообщений:** Если сообщение не является `ChatCompletionMessage`, используется стандартный метод преобразования.
    |
    F. **Возврат результата:** Возвращается преобразованный словарь.
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

**Примеры:**

```python
from langchain_core.messages import BaseMessage, HumanMessage
from g4f.client.stubs import ChatCompletionMessage, ToolCall
# Пример 1: Преобразование ChatCompletionMessage без tool_calls
message = ChatCompletionMessage(role="assistant", content="Hello!")
result = new_convert_message_to_dict(message)
print(result)  # {'role': 'assistant', 'content': 'Hello!'}

# Пример 2: Преобразование ChatCompletionMessage с tool_calls
tool_calls = [ToolCall(id="1", type="function", function={"name": "get_weather", "arguments": "{location: 'Moscow'}"})]
message = ChatCompletionMessage(role="assistant", content="Calling tool", tool_calls=tool_calls)
result = new_convert_message_to_dict(message)
print(result)
# {'role': 'assistant', 'content': 'Calling tool', 'tool_calls': [{'id': '1', 'type': 'function', 'function': {'name': 'get_weather', 'arguments': "{location: 'Moscow'}"}}]}

# Пример 3: Преобразование HumanMessage
message = HumanMessage(content="Hi there!")
result = new_convert_message_to_dict(message)
print(result)  # {'content': 'Hi there!', 'role': 'human'}
```

## Классы

### `ChatAI`

**Описание**:
Класс `ChatAI` расширяет класс `ChatOpenAI` из библиотеки Langchain для интеграции с моделями g4f. Он позволяет использовать модели g4f в качестве чат-моделей Langchain.

**Принцип работы**:
Класс `ChatAI` наследует от `ChatOpenAI` и переопределяет метод `validate_environment`, чтобы настроить клиент g4f для использования с Langchain. Он также устанавливает `model_name` по умолчанию в "gpt-4o".

**Методы**:

- `validate_environment(cls, values: dict) -> dict`:
    ```python
    @classmethod
    def validate_environment(cls, values: dict) -> dict:
        """Проверяет и настраивает окружение для использования g4f в качестве чат-модели Langchain.

        Args:
            values (dict): Словарь с параметрами конфигурации.

        Returns:
            dict: Обновленный словарь с параметрами конфигурации, включающий настроенный клиент g4f.

        Как работает функция:
        1. Извлекает параметры `api_key` и `provider` из словаря `values` (при их наличии).
        2. Создает клиент `Client` и асинхронный клиент `AsyncClient` из библиотеки `g4f.client`, передавая им параметры `api_key` и `provider`.
        3. Присваивает клиенты `chat.completions` атрибутам `client` и `async_client` словаря `values`.
        4. Возвращает обновленный словарь `values`.

        Внутри функции происходят следующие действия и преобразования:
        A. **Извлечение параметров:** Извлекаются параметры `api_key` и `provider` из входного словаря.
        |
        B. **Создание клиентов g4f:** Создаются синхронный и асинхронный клиенты `g4f` с использованием извлеченных параметров.
        |
        C. **Настройка параметров Langchain:** В словарь `values` добавляются настроенные клиенты для использования с Langchain.
        |
        D. **Возврат результата:** Возвращается обновленный словарь конфигурации.
        """
    ```
    **Назначение**: Проверяет и настраивает окружение, создавая клиентов `Client` и `AsyncClient` из библиотеки `g4f.client`. Эти клиенты используются для взаимодействия с моделями g4f.
    **Параметры**:
        - `values` (dict): Словарь, содержащий параметры конфигурации.
    **Возвращает**:
        - `dict`: Обновленный словарь `values`, включающий настроенные клиенты `client` и `async_client`.

**Примеры**:

```python
from typing import Dict

# Пример 1: Создание экземпляра ChatAI с минимальной конфигурацией
config: Dict[str, Any] = {}
validated_config = ChatAI.validate_environment(config)
print(validated_config.keys())
#dict_keys(['client', 'async_client'])

# Пример 2: Создание экземпляра ChatAI с указанием провайдера
config: Dict[str, Any] = {"model_kwargs": {"provider": "g4f.models.gpt_4"}}
validated_config = ChatAI.validate_environment(config)
print(validated_config.keys())
#dict_keys(['model_kwargs', 'client', 'async_client'])
```