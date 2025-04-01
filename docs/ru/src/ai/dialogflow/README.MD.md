# Модуль `src.ai.dialogflow`

## Обзор

Модуль `src.ai.dialogflow` предназначен для интеграции с платформой Dialogflow, обеспечивая возможности понимания естественного языка (NLU) и создания диалоговых AI-приложений. Он включает основные функции, такие как определение намерений, распознавание сущностей, управление контекстом, интеграции с различными платформами и поддержку webhook.

## Подробнее

Модуль предоставляет инструменты для работы с Dialogflow API, позволяя определять намерения пользователей на основе введенного текста, извлекать ключевые данные из фраз, управлять контекстом разговора, интегрироваться с различными платформами (Google Assistant, Facebook Messenger и др.) и поддерживать webhook для вызова внешних сервисов и API.

## Содержание

- [Описание модуля](#модуль-src.ai.dialogflow)
- [Основные возможности](#основные-возможности)
- [Пример использования](#пример-использования)

## Основные возможности

- **Определение намерений (Intent Detection):** Позволяет определить намерения пользователя на основе введенного текста.
- **Распознавание сущностей (Entity Recognition):** Позволяет извлекать ключевые данные из фраз пользователя.
- **Контексты (Contexts):** Управление контекстом разговора путем сохранения информации о текущем состоянии диалога.
- **Интеграции (Integrations):** Поддержка интеграции с различными платформами, такими как Google Assistant, Facebook Messenger, Slack, Telegram и другие.
- **Webhook:** Поддержка интеграций Webhook для вызова внешних сервисов и API.

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

# Удаление намерения (убедитесь, что intent_id заменен реальным ID)
# dialogflow_client.delete_intent("your-intent-id")