# Документация для модуля `src.ai.dialogflow`

## Обзор

Модуль `src.ai.dialogflow` предназначен для интеграции с Google Dialogflow. Он предоставляет инструменты для обработки естественного языка (NLU) и создания разговорных ИИ-приложений.

## Подробней

Этот модуль позволяет определять намерения пользователя, извлекать ключевые данные из фраз, управлять контекстом диалога и интегрироваться с различными платформами, такими как Google Assistant, Facebook Messenger, Slack и Telegram. Он также поддерживает Webhook-интеграции для вызова внешних сервисов и API.

## Содержание

- [Обзор](#обзор)
- [Подробней](#подробней)
- [Основные функции](#основные-функции)
- [Пример использования](#пример-использования)

## Основные функции

- **Определение намерений (Intent Detection):** Определяет намерения пользователя на основе введенного текста.
- **Работа с сущностями (Entity Recognition):** Извлекает ключевые данные из пользовательских фраз.
- **Контексты (Contexts):** Управляет диалогом, сохраняя информацию о текущем состоянии разговора.
- **Интеграции:** Поддерживает интеграцию с различными платформами, такими как Google Assistant, Facebook Messenger, Slack, Telegram, и другими.
- **Webhook:** Поддерживает Webhook-интеграции для вызова внешних сервисов и API.

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