# Модуль `dialogflow`

## Обзор

Модуль `dialogflow` предназначен для интеграции с сервисом Dialogflow. Он предоставляет возможности для понимания естественного языка (NLU) и создания диалоговых AI-приложений. Модуль включает следующие основные функции:

- **Определение намерений:** Определяет намерения пользователя на основе введенного текста.
- **Распознавание сущностей:** Извлекает ключевые данные из фраз пользователя.
- **Контексты:** Управляет разговором, сохраняя информацию о текущем состоянии диалога.
- **Интеграции:** Поддерживает интеграцию с различными платформами, такими как Google Assistant, Facebook Messenger, Slack, Telegram и другие.
- **Webhook:** Поддерживает интеграции с Webhook для вызова внешних сервисов и API.

## Оглавление

1. [Обзор](#обзор)
2. [Пример использования](#пример-использования)

## Пример использования

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

# Удаление намерения (обязательно замените intent_id на реальный ID)
# dialogflow_client.delete_intent("your-intent-id")
```