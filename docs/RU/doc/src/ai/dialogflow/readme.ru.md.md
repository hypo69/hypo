# Модуль интеграции с Google Dialogflow

## Обзор

Модуль `dialogflow` предоставляет возможности для интеграции с Google Dialogflow, обеспечивая обработку естественного языка (NLU) и создание разговорных ИИ-приложений. Он включает в себя функции определения намерений, работы с сущностями, управления контекстами и интеграции с различными платформами.

## Оглавление

1. [Обзор](#обзор)
2. [Классы](#классы)
   - [`Dialogflow`](#dialogflow)
3. [Пример использования](#пример-использования)

## Классы

### `Dialogflow`

**Описание**: Класс для взаимодействия с Google Dialogflow API.

**Методы**:

- `__init__`: Инициализирует экземпляр класса Dialogflow.
- `detect_intent`: Определяет намерение пользователя на основе введенного текста.
- `list_intents`: Возвращает список всех доступных намерений.
- `create_intent`: Создает новое намерение.
- `delete_intent`: Удаляет намерение.

#### `__init__`

**Описание**: Инициализирует экземпляр класса Dialogflow.

**Параметры**:
- `project_id` (str): Идентификатор проекта Google Cloud.
- `session_id` (str): Идентификатор сессии пользователя.

**Возвращает**:
- `None`: Ничего не возвращает.

#### `detect_intent`

**Описание**: Определяет намерение пользователя на основе введенного текста.

**Параметры**:
- `text` (str): Текст для анализа.
- `language_code` (str, optional): Код языка. По умолчанию `'ru-RU'`.

**Возвращает**:
- `dict`: Ответ от Dialogflow API.

**Вызывает исключения**:
- `Exception`:  Возникает в случае ошибки при взаимодействии с Dialogflow API.

#### `list_intents`

**Описание**: Возвращает список всех доступных намерений.

**Параметры**:
- `language_code` (str, optional): Код языка. По умолчанию `'ru-RU'`.

**Возвращает**:
- `list[dict]`: Список словарей, представляющих намерения.

**Вызывает исключения**:
- `Exception`:  Возникает в случае ошибки при взаимодействии с Dialogflow API.

#### `create_intent`

**Описание**: Создает новое намерение.

**Параметры**:
- `display_name` (str): Имя намерения.
- `training_phrases_parts` (list[str]): Список фраз для обучения.
- `message_texts` (list[str]): Список ответов на намерение.
- `language_code` (str, optional): Код языка. По умолчанию `'ru-RU'`.

**Возвращает**:
- `dict`: Ответ от Dialogflow API.

**Вызывает исключения**:
- `Exception`:  Возникает в случае ошибки при взаимодействии с Dialogflow API.

#### `delete_intent`

**Описание**: Удаляет намерение.

**Параметры**:
- `intent_id` (str): Идентификатор намерения.

**Возвращает**:
- `None`: Ничего не возвращает.

**Вызывает исключения**:
- `Exception`: Возникает в случае ошибки при взаимодействии с Dialogflow API.

## Пример использования

Пример использования подмодуля **dialogflow**:

```python
from src.ai.dialogflow import Dialogflow

project_id = "your-project-id"
session_id = "unique-session-id"

dialogflow_client = Dialogflow(project_id, session_id)

# Пример использования методов
intent_response = dialogflow_client.detect_intent("Hello")
print("Detected Intent:", intent_response)

intents = dialogflow_client.list_intents()
print("List of Intents:", intents)

new_intent = dialogflow_client.create_intent(
    display_name="NewIntent",
    training_phrases_parts=["new phrase", "another phrase"],
    message_texts=["This is a new intent"]
)
print("Created Intent:", new_intent)

# Удаление намерения (не забудьте заменить intent_id на реальный ID)
# dialogflow_client.delete_intent("your-intent-id")
```