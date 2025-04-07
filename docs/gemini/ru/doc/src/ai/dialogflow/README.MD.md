# Документация для модуля `src.ai.dialogflow`

## Обзор

Этот модуль предназначен для интеграции с платформой Dialogflow и предоставляет возможности для понимания естественного языка (NLU) и создания разговорных AI-приложений. Он включает в себя основные функции, такие как определение намерений, распознавание сущностей, управление контекстами, интеграции с различными платформами и поддержку вебхуков.

## Подробнее

Модуль `src.ai.dialogflow` позволяет взаимодействовать с Dialogflow API для создания и управления разговорными агентами. Он предоставляет классы и функции для определения намерений пользователя, извлечения ключевых данных из фраз, управления контекстом разговора и интеграции с различными платформами. Этот модуль упрощает разработку чат-ботов и голосовых помощников, позволяя разработчикам сосредоточиться на логике приложения, а не на деталях взаимодействия с NLU-платформой.

## Содержание

1. [Обзор](#обзор)
2. [Подробнее](#подробнее)
3. [Функциональность](#функциональность)
4. [Пример использования](#пример-использования)

## Функциональность

### **Основные возможности**

- **Определение намерений:** Определяет намерения пользователя на основе введенного текста.
- **Распознавание сущностей:** Извлекает ключевые данные из фраз пользователя.
- **Контексты:** Управляет разговором, сохраняя информацию о текущем состоянии диалога.
- **Интеграции:** Поддерживает интеграцию с различными платформами, такими как Google Assistant, Facebook Messenger, Slack, Telegram и другие.
- **Вебхуки:** Поддерживает интеграцию вебхуков для вызова внешних сервисов и API.

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

# Deleting an intent (make sure to replace intent_id with a real ID)
# dialogflow_client.delete_intent("your-intent-id")