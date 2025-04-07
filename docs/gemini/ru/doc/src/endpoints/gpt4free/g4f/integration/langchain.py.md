# Модуль интеграции G4F с Langchain

## Обзор

Модуль предназначен для интеграции библиотеки `g4f` (GPT4Free) с фреймворком `Langchain`. Он содержит класс `ChatAI`, который расширяет возможности `ChatOpenAI` из `langchain_community` для использования моделей, предоставляемых через `g4f`.

## Подробней

Этот модуль позволяет использовать модели, доступные через `g4f`, в приложениях `Langchain`. Он переопределяет функцию `convert_message_to_dict` для корректной обработки сообщений с вызовами инструментов (tool calls) и предоставляет класс `ChatAI` для удобной интеграции.

## Функции

### `new_convert_message_to_dict`

```python
def new_convert_message_to_dict(message: BaseMessage) -> dict:
    """Преобразует объект сообщения `BaseMessage` в словарь для использования в `OpenAI API`.

    Args:
        message (BaseMessage): Объект сообщения, который необходимо преобразовать.

    Returns:
        dict: Словарь, представляющий сообщение в формате, совместимом с `OpenAI API`.

    **Как работает функция**:

    1. **Проверка типа сообщения**: Определяет, является ли сообщение экземпляром `ChatCompletionMessage`.
    2. **Обработка `ChatCompletionMessage`**:
       - Если сообщение является `ChatCompletionMessage`, создает словарь с ключами `role` и `content` из атрибутов сообщения.
       - Обрабатывает `tool_calls`, если они присутствуют, преобразуя их в список словарей.
       - Если `content` пустой, устанавливает его в `None`.
    3. **Обработка других типов сообщений**: Если сообщение не является `ChatCompletionMessage`, использует стандартную функцию `convert_message_to_dict` из `langchain_community`.
    4. **Возврат результата**: Возвращает полученный словарь.

    ```
    A: Проверка типа сообщения
    |
    -- B: Обработка ChatCompletionMessage
    |  |
    |  -- C: Преобразование tool_calls
    |  |
    |  -- D: Установка content в None, если пустой
    |
    -- E: Обработка других типов сообщений (через convert_message_to_dict)
    |
    F: Возврат словаря
    ```
    Примеры:

    ```python
    from langchain_core.messages import BaseMessage, HumanMessage
    from g4f.client.stubs import ChatCompletionMessage
    from typing import List
    class ToolCall:
        def __init__(self, id: str, type: str, function: dict):
            self.id = id
            self.type = type
            self.function = function

    # Пример с ChatCompletionMessage и tool_calls
    tool_calls = [ToolCall(id='123', type='function', function={'name': 'test', 'arguments': 'args'})]
    message = ChatCompletionMessage(role='assistant', content='test content', tool_calls=tool_calls)
    result = new_convert_message_to_dict(message)
    assert result == {'role': 'assistant', 'content': 'test content', 'tool_calls': [{'id': '123', 'type': 'function', 'function': {'name': 'test', 'arguments': 'args'}}]}
    
    # Пример с HumanMessage
    message = HumanMessage(content='test content')
    result = new_convert_message_to_dict(message)
    assert result == {'content': 'test content', 'role': 'human'}
    """
```

## Классы

### `ChatAI`

**Описание**:
Класс `ChatAI` расширяет `ChatOpenAI` из `langchain_community` для интеграции с моделями, предоставляемыми через `g4f`.

**Наследует**:
- `ChatOpenAI`

**Атрибуты**:
- `model_name` (str): Имя модели, используемой для чата. По умолчанию "gpt-4o".

**Методы**:
- `validate_environment(cls, values: dict) -> dict`: Проверяет и настраивает окружение для использования `g4f` клиента.

### `validate_environment`

```python
    @classmethod
    def validate_environment(cls, values: dict) -> dict:
        """Проверяет и настраивает окружение для использования `g4f` клиента.

        Args:
            values (dict): Словарь с параметрами для настройки окружения.

        Returns:
            dict: Обновленный словарь с настроенным `g4f` клиентом.

        **Как работает функция**:

        1. **Извлечение параметров клиента**: Извлекает параметры `api_key` и `provider` из входного словаря `values`.
        2. **Создание экземпляров клиентов**: Создает синхронный и асинхронный экземпляры `g4f` клиента с использованием извлеченных параметров.
        3. **Обновление словаря значений**: Добавляет созданные клиенты в словарь `values` под ключами `client` и `async_client`.
        4. **Возврат результата**: Возвращает обновленный словарь `values`.

        ```
        A: Извлечение параметров клиента (api_key, provider)
        |
        -- B: Создание синхронного клиента
        |
        -- C: Создание асинхронного клиента
        |
        D: Обновление словаря values (добавление client и async_client)
        |
        E: Возврат обновленного словаря
        ```

        **Примеры**:

        ```python
        values = {"api_key": "test_key", "model_kwargs": {"provider": "test_provider"}}
        updated_values = ChatAI.validate_environment(values)
        assert "client" in updated_values
        assert "async_client" in updated_values
        ```
        """