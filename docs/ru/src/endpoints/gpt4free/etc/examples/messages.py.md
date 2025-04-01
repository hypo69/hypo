# Модуль для обработки диалогов с использованием g4f

## Обзор

Модуль содержит класс `ConversationHandler`, который упрощает взаимодействие с моделями GPT через библиотеку `g4f`. Он предоставляет функциональность для хранения истории диалогов и получения ответов от модели.

## Подробнее

Этот модуль предоставляет простой способ ведения диалогов с AI-моделями, используя библиотеку `g4f`. Класс `ConversationHandler` инициализирует клиента `g4f`, хранит историю сообщений и предоставляет метод для получения ответа от модели на основе истории сообщений.

## Классы

### `ConversationHandler`

**Описание**: Класс для управления диалогом с AI-моделью.

**Принцип работы**:

1.  Инициализируется с указанием модели (по умолчанию "gpt-4").
2.  Создает экземпляр клиента `g4f`.
3.  Хранит историю диалога в списке `conversation_history`.
4.  Метод `add_user_message` добавляет сообщение пользователя в историю.
5.  Метод `get_response` отправляет историю диалога модели и возвращает ответ ассистента, а также добавляет ответ ассистента в историю.

**Методы**:

*   `__init__(model="gpt-4")`: Инициализирует объект `ConversationHandler`.
*   `add_user_message(content: str)`: Добавляет сообщение пользователя в историю диалога.
*   `get_response() -> str`: Получает ответ от модели на основе истории диалога.

### `__init__`

```python
    def __init__(self, model="gpt-4"):
        self.client = Client()
        self.model = model
        self.conversation_history = []
```

**Назначение**: Инициализирует объект `ConversationHandler`.

**Параметры**:

*   `model` (str): Название модели, используемой для диалога. По умолчанию `"gpt-4"`.

**Как работает функция**:

1.  Создает экземпляр класса `Client` из библиотеки `g4f`.
2.  Инициализирует атрибут `model` значением переданного параметра `model`.
3.  Создает пустой список `conversation_history` для хранения истории диалога.

```
Инициализация -> Создание клиента g4f ->  Инициализация атрибута model -> Создание списка истории
```

**Примеры**:

```python
conversation = ConversationHandler()
conversation = ConversationHandler(model="gpt-3.5-turbo")
```

### `add_user_message`

```python
    def add_user_message(self, content: str):
        self.conversation_history.append({
            "role": "user",
            "content": content
        })
```

**Назначение**: Добавляет сообщение пользователя в историю диалога.

**Параметры**:

*   `content` (str): Текст сообщения пользователя.

**Как работает функция**:

1.  Создает словарь, содержащий роль `"user"` и контент сообщения.
2.  Добавляет этот словарь в список `conversation_history`.

```
Получение контента -> Создание словаря с ролью и контентом -> Добавление словаря в историю диалога
```

**Примеры**:

```python
conversation = ConversationHandler()
conversation.add_user_message("Hello!")
conversation.add_user_message("How are you?")
```

### `get_response`

```python
    def get_response(self) -> str:
        response = self.client.chat.completions.create(
            model=self.model,
            messages=self.conversation_history
        )
        assistant_message = {
            "role": response.choices[0].message.role,
            "content": response.choices[0].message.content
        }
        self.conversation_history.append(assistant_message)
        return assistant_message["content"]
```

**Назначение**: Получает ответ от модели на основе истории диалога.

**Возвращает**:

*   `str`: Текст ответа ассистента.

**Как работает функция**:

1.  Отправляет запрос к модели через `client.chat.completions.create`, передавая историю диалога.
2.  Извлекает роль и контент сообщения ассистента из ответа.
3.  Создает словарь с ролью и контентом ассистента.
4.  Добавляет сообщение ассистента в историю диалога.
5.  Возвращает контент сообщения ассистента.

```
Отправка запроса к модели -> Извлечение данных из ответа -> Создание словаря с сообщением ассистента -> Добавление сообщения ассистента в историю -> Возврат контента сообщения ассистента
```

**Примеры**:

```python
conversation = ConversationHandler()
conversation.add_user_message("Hello!")
assistant_response = conversation.get_response()
print("Assistant:", assistant_response)
```
```python
from g4f.client import Client

class ConversationHandler:
    def __init__(self, model="gpt-4"):
        """
        Инициализирует обработчик диалогов.

        Args:
            model (str): Модель для использования в диалоге. По умолчанию "gpt-4".

        Примеры:
            >>> conversation = ConversationHandler(model="gpt-4")
        """
        self.client = Client()
        self.model = model
        self.conversation_history = []
        
    def add_user_message(self, content: str):
        """
        Добавляет сообщение пользователя в историю диалога.

        Args:
            content (str): Содержание сообщения пользователя.

        Примеры:
            >>> conversation = ConversationHandler()
            >>> conversation.add_user_message("Hello!")
        """
        self.conversation_history.append({
            "role": "user",
            "content": content
        })
        
    def get_response(self) -> str:
        """
        Получает ответ от модели на основе истории диалога.

        Returns:
            str: Ответ модели.

        Примеры:
            >>> conversation = ConversationHandler()
            >>> conversation.add_user_message("Hello!")
            >>> response = conversation.get_response()
            >>> print(response)
        """
        response = self.client.chat.completions.create(
            model=self.model,
            messages=self.conversation_history
        )
        assistant_message = {
            "role": response.choices[0].message.role,
            "content": response.choices[0].message.content
        }
        self.conversation_history.append(assistant_message)
        return assistant_message["content"]

# Примеры использования
conversation = ConversationHandler()
conversation.add_user_message("Hello!")
print("Assistant:", conversation.get_response())

conversation.add_user_message("How are you?")
print("Assistant:", conversation.get_response())