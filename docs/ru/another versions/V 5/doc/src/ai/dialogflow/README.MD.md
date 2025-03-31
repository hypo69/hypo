# Модуль `src.ai.dialogflow`

## Обзор

Этот модуль предназначен для интеграции с Dialogflow, обеспечивая возможности понимания естественного языка (NLU) и создания разговорных AI-приложений. Он включает в себя основные функции, такие как определение намерений, распознавание сущностей, управление контекстами и интеграцию с различными платформами.

## Подробней

Модуль `src.ai.dialogflow` предоставляет инструменты для работы с Dialogflow API, позволяя определять намерения пользователей на основе введенного текста, извлекать ключевые данные из фраз, управлять контекстом диалога и интегрироваться с различными платформами, такими как Google Assistant, Facebook Messenger, Slack и Telegram. Также поддерживаются интеграции Webhook для вызова внешних сервисов и API.

## Классы

### `Dialogflow`

**Описание**: Класс для взаимодействия с Dialogflow API.

**Как работает класс**:
Класс `Dialogflow` инициализируется с использованием идентификатора проекта и идентификатора сессии. Он предоставляет методы для определения намерений, создания, чтения и удаления намерений в Dialogflow. Класс использует клиент `IntentsClient` для взаимодействия с Dialogflow API.

**Методы**:
- `__init__`: Инициализирует клиент Dialogflow с использованием идентификатора проекта и идентификатора сессии.
- `detect_intent`: Определяет намерение пользователя на основе введенного текста.
- `list_intents`: Возвращает список всех доступных намерений.
- `create_intent`: Создает новое намерение с заданными параметрами.
- `delete_intent`: Удаляет указанное намерение.

**Параметры**:
- `project_id` (str): Идентификатор проекта Dialogflow.
- `session_id` (str): Уникальный идентификатор сессии.
- `display_name` (str): Отображаемое имя нового намерения.
- `training_phrases_parts` (list[str]): Список фраз для обучения нового намерения.
- `message_texts` (list[str]): Список текстовых сообщений для нового намерения.
- `intent_id` (str): Идентификатор намерения для удаления.

**Примеры**:

```python
from src.ai.dialogflow import Dialogflow

project_id = "your-project-id"
session_id = "unique-session-id"

dialogflow_client = Dialogflow(project_id, session_id)

# Example usage of methods
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

# Deleting an intent (make sure to replace intent_id with a real ID)
# dialogflow_client.delete_intent("your-intent-id")