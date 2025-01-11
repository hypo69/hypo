# Модуль `dialogflow`

## Обзор

Модуль интеграции с Dialogflow. Предоставляет возможности для понимания естественного языка (NLU) и создания разговорных AI-приложений. Он включает в себя следующие основные функции:

- **Определение намерений (Intent Detection):** Определяет намерения пользователя на основе введенного текста.
- **Распознавание сущностей (Entity Recognition):** Извлекает ключевые данные из фраз пользователя.
- **Контексты (Contexts):** Управляет разговором, сохраняя информацию о текущем состоянии диалога.
- **Интеграции (Integrations):** Поддерживает интеграцию с различными платформами, такими как Google Assistant, Facebook Messenger, Slack, Telegram и другими.
- **Вебхуки (Webhook):** Поддерживает интеграцию с вебхуками для вызова внешних сервисов и API.

## Оглавление

- [Обзор](#обзор)
- [Примеры использования](#примеры-использования)

## Примеры использования

Пример использования подмодуля `dialogflow`:

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

# Удаление интента (необходимо заменить intent_id на реальный ID)
# dialogflow_client.delete_intent("your-intent-id")
```