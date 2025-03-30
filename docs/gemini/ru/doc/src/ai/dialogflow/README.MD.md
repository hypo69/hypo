# Документация модуля `src.ai.dialogflow`

## Обзор

Этот модуль предоставляет интеграцию с Dialogflow и обеспечивает возможности для понимания естественного языка (NLU) и создания диалоговых AI-приложений. Он включает в себя основные функции, такие как определение намерений, распознавание сущностей, управление контекстами и интеграцию с различными платформами.

## Подорбней

Модуль `src.ai.dialogflow` предназначен для упрощения взаимодействия с Dialogflow API. Он позволяет определять намерения пользователя на основе введенного текста, извлекать ключевые данные из фраз, управлять контекстом разговора и интегрироваться с различными платформами, такими как Google Assistant, Facebook Messenger, Slack, Telegram и другие. Также поддерживается интеграция с Webhook для вызова внешних сервисов и API. Этот модуль является ключевым компонентом для создания чат-ботов и других приложений, использующих NLU.

## Функции

### `Dialogflow`

**Описание**: Класс для взаимодействия с Dialogflow API.

**Методы**:
- `detect_intent`: Определяет намерения пользователя на основе введенного текста.
- `list_intents`: Возвращает список всех определенных намерений.
- `create_intent`: Создает новое намерение.
- `delete_intent`: Удаляет существующее намерение.

**Параметры**:
- `project_id` (str): Идентификатор проекта Dialogflow.
- `session_id` (str): Уникальный идентификатор сессии.

**Примеры**

Пример использования класса `Dialogflow`:

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
```