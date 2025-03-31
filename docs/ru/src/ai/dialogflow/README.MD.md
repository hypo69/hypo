# Модуль `src.ai.dialogflow`

## Обзор

Модуль `src.ai.dialogflow` предоставляет интеграцию с Dialogflow и содержит функциональность для понимания естественного языка (NLU) и создания разговорных AI-приложений. Он включает обнаружение намерений, распознавание сущностей, управление контекстом, интеграцию с различными платформами и поддержку веб-хуков для внешних сервисов и API.

## Подробнее

Этот модуль позволяет интегрировать приложение с платформой Dialogflow, предоставляя инструменты для создания и управления разговорными интерфейсами. Он упрощает взаимодействие с API Dialogflow, абстрагируя сложные детали реализации.

## Содержание

- [Обзор](#обзор)
- [Подробнее](#подробнее)
- [Функциональность](#функциональность)
- [Пример использования](#пример-использования)
- [Ссылки](#ссылки)

## Функциональность

- **Intent Detection (Обнаружение намерений):** Определяет намерения пользователя на основе входного текста.
- **Entity Recognition (Распознавание сущностей):** Извлекает ключевые данные из фраз пользователя.
- **Contexts (Контексты):** Управляет разговором, сохраняя информацию о текущем состоянии диалога.
- **Integrations (Интеграции):** Поддерживает интеграцию с различными платформами, такими как Google Assistant, Facebook Messenger, Slack, Telegram и другие.
- **Webhook (Веб-хуки):** Поддерживает интеграцию веб-хуков для вызова внешних сервисов и API.

## Пример использования

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

# Deleting an intent (make sure to replace intent_id with a real ID)
# dialogflow_client.delete_intent("your-intent-id")
```

## Ссылки

- [Root ↑](https://github.com/hypo69/hypo/blob/master/README.MD)
- [src](https://github.com/hypo69/hypo/blob/master/src/README.MD)
- [ai](https://github.com/hypo69/hypo/blob/master/src/ai/README.MD)
- [About dialogflow model](https://github.com/hypo69/hypo/blob/master/src/ai/dialogflow/about.md)
- [Русский](https://github.com/hypo69/hypo/blob/master/src/ai/dialogflow/readme.ru.md)
- [Dialogflow Documentation](https://dialogflow.com/docs/getting-started/basics)