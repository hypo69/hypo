# Модуль `dialogflow`

## Обзор

Модуль `dialogflow` предназначен для интеграции с Dialogflow, предоставляя возможности для понимания естественного языка (NLU) и создания разговорных приложений с использованием искусственного интеллекта. Он включает в себя следующие основные функции:

- **Определение намерений:** Определяет намерения пользователя на основе введенного текста.
- **Распознавание сущностей:** Извлекает ключевые данные из фраз пользователя.
- **Контексты:** Управляет разговором, сохраняя информацию о текущем состоянии диалога.
- **Интеграции:** Поддерживает интеграцию с различными платформами, такими как Google Assistant, Facebook Messenger, Slack, Telegram и другими.
- **Webhook:** Поддерживает интеграции Webhook для вызова внешних сервисов и API.

## Оглавление

1. [Обзор](#обзор)
2. [Пример использования](#пример-использования)

## Пример использования

Пример использования подмодуля `dialogflow`:

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