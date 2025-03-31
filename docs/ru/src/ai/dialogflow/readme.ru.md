# Документация модуля `src.ai.dialogflow`

## Обзор

Модуль `src.ai.dialogflow` предоставляет интеграцию с Google Dialogflow, обеспечивая возможности обработки естественного языка (NLU) и создания разговорных ИИ-приложений. Он включает в себя определение намерений, работу с сущностями, контексты и интеграции с различными платформами.

## Подробней

Этот модуль позволяет интегрировать ваш проект с Google Dialogflow, что упрощает создание чат-ботов и других разговорных интерфейсов. С помощью этого модуля можно определять намерения пользователя, извлекать ключевые данные из фраз, управлять диалогом и интегрироваться с различными платформами, такими как Google Assistant, Facebook Messenger, Slack, Telegram и другие.

## dialogflow

### **Описание**

Модуль интеграции с Google Dialogflow.

Предоставляет возможности для обработки естественного языка (NLU)
и создания разговорных ИИ-приложений. Он включает в себя следующие основные функции:

- **Определение намерений (Intent Detection):** Определяет намерения пользователя на основе введенного текста.
- **Работа с сущностями (Entity Recognition):** Извлекает ключевые данные из пользовательских фраз.
- **Контексты (Contexts):** Управляет диалогом, сохраняя информацию о текущем состоянии разговора.
- **Интеграции:** Поддерживает интеграцию с различными платформами, такими как Google Assistant, Facebook Messenger, Slack, Telegram, и другими.
- **Webhook:** Поддерживает Webhook-интеграции для вызова внешних сервисов и API.

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
```