# Модуль интеграции g4f с Langchain

## Обзор

Модуль предоставляет интеграцию между библиотекой `g4f` (для работы с различными моделями чат-ботов) и фреймворком `Langchain`. Он включает в себя переопределение функции преобразования сообщений и класс `ChatAI`, расширяющий возможности `ChatOpenAI` для использования с `g4f`.

## Подробней

Этот модуль позволяет использовать модели, доступные через `g4f`, в приложениях, построенных на базе `Langchain`. Он содержит функции для преобразования сообщений в формат, совместимый с `g4f`, и класс `ChatAI`, который упрощает использование моделей `g4f` как альтернативы моделям OpenAI в `Langchain`.

## Функции

### `new_convert_message_to_dict`

```python
def new_convert_message_to_dict(message: BaseMessage) -> dict:
    """
    Преобразует объект сообщения `BaseMessage` в словарь.

    Args:
        message (BaseMessage): Объект сообщения для преобразования.

    Returns:
        dict: Словарь, представляющий сообщение.

    Как работает функция:
    1. Проверяет, является ли сообщение экземпляром класса `ChatCompletionMessage`.
    2. Если сообщение является экземпляром `ChatCompletionMessage`, то извлекает информацию о роли, содержании и вызовах инструментов (`tool_calls`) из сообщения и формирует словарь.
    3. Если `tool_calls` не `None`, преобразует информацию о каждом вызове инструмента в формат словаря и добавляет в результирующий словарь.
    4. Если `content` сообщения пустое, устанавливает значение `None` для ключа `content` в словаре.
    5. Если сообщение не является экземпляром `ChatCompletionMessage`, использует стандартную функцию `convert_message_to_dict` для преобразования сообщения в словарь.
    6. Возвращает полученный словарь.

    Внутренние функции:
    - Отсутствуют.

    ASCII flowchart:
    Проверка типа сообщения --> Извлечение информации из сообщения --> Преобразование tool_calls (если есть) --> Возврат словаря

    Примеры:
    >>> from langchain_core.messages import BaseMessage
    >>> from g4f.client.stubs import ChatCompletionMessage, ToolCall
    >>> message = ChatCompletionMessage(role='assistant', content='Привет', tool_calls=[ToolCall(id='123', type='function', function={'name': 'test', 'arguments': 'args'})])
    >>> new_convert_message_to_dict(message)
    {'role': 'assistant', 'content': 'Привет', 'tool_calls': [{'id': '123', 'type': 'function', 'function': {'name': 'test', 'arguments': 'args'}}]}
    """
    ...
```

### Внутренние функции:
 Отсутствуют.

#### `openai.convert_message_to_dict = new_convert_message_to_dict`

Заменяет стандартную функцию `convert_message_to_dict` в модуле `openai` на новую функцию `new_convert_message_to_dict`.

## Классы

### `ChatAI`

```python
class ChatAI(ChatOpenAI):
    """
    Класс для взаимодействия с моделями чат-ботов через g4f.

    Inherits:
        ChatOpenAI: Наследует от класса ChatOpenAI из langchain_community.

    Attributes:
        model_name (str): Название модели, по умолчанию "gpt-4o".

    Methods:
        validate_environment(cls, values: dict) -> dict: Проверяет и подготавливает окружение для работы с g4f.
    """
    ...
```

**Описание**:
Класс `ChatAI` расширяет класс `ChatOpenAI` из библиотеки `langchain_community` для обеспечения совместимости с моделями, предоставляемыми через `g4f`.

**Принцип работы**:
Класс `ChatAI` позволяет использовать модели, доступные через `g4f`, в качестве альтернативы моделям OpenAI в приложениях, построенных на базе `Langchain`. Он включает метод `validate_environment`, который устанавливает параметры клиента `g4f` для выполнения запросов к моделям.

#### Методы:

- `validate_environment`

```python
@classmethod
def validate_environment(cls, values: dict) -> dict:
    """
    Проверяет и подготавливает окружение для работы с g4f.

    Args:
        values (dict): Словарь с параметрами конфигурации.

    Returns:
        dict: Обновленный словарь с параметрами конфигурации.

    Как работает функция:
    1. Извлекает параметры `api_key` и `provider` из словаря `values`.
    2. Создает экземпляры `Client` и `AsyncClient` из библиотеки `g4f` с переданными параметрами.
    3. Устанавливает атрибуты `client` и `async_client` в словаре `values`, используя созданные экземпляры `Client` и `AsyncClient`.
    4. Возвращает обновленный словарь `values`.

    Внутренние функции:
    - Отсутствуют.

    ASCII flowchart:
    Извлечение параметров --> Создание экземпляров Client и AsyncClient --> Установка атрибутов в словаре --> Возврат словаря

    Примеры:
    >>> values = {'api_key': 'test_key', 'model_kwargs': {'provider': 'test_provider'}}
    >>> ChatAI.validate_environment(values)
    {'api_key': 'test_key', 'model_kwargs': {'provider': 'test_provider'}, 'client': <g4f.client.chat.completions object at ...>, 'async_client': <g4f.client.chat.completions object at ...>}
    """
    ...
```

- `model_name`

```python
model_name: str = Field(default="gpt-4o", alias="model")
```

**Параметры**:
- `values` (dict): Словарь, содержащий параметры конфигурации.

**Как работает функция**:
1. Извлекает `api_key` и `provider` из входного словаря `values`.
2. Создает экземпляры `Client` и `AsyncClient` из библиотеки `g4f` с использованием извлеченных параметров.
3. Устанавливает атрибуты `client` и `async_client` в словаре `values`, присваивая им созданные экземпляры `Client` и `AsyncClient`.
4. Возвращает обновленный словарь `values`.

**Примеры**:
```python
values = {"api_key": "test_key", "model_kwargs": {"provider": "test_provider"}}
result = ChatAI.validate_environment(values)
print(result)