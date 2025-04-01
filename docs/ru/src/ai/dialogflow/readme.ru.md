# Модуль `src.ai.dialogflow`

## Обзор

Модуль `src.ai.dialogflow` предназначен для интеграции с Google Dialogflow. Он предоставляет возможности для обработки естественного языка (NLU) и создания разговорных ИИ-приложений.

## Подробней

Этот модуль позволяет взаимодействовать с Google Dialogflow для определения намерений пользователя, извлечения ключевых данных, управления контекстами и интеграции с различными платформами. Он облегчает создание разговорных ИИ-приложений, поддерживающих интеграцию с Google Assistant, Facebook Messenger, Slack, Telegram и другими сервисами.

## Функциональность

- **Определение намерений (Intent Detection):** Определяет намерения пользователя на основе введенного текста.
- **Работа с сущностями (Entity Recognition):** Извлекает ключевые данные из пользовательских фраз.
- **Контексты (Contexts):** Управляет диалогом, сохраняя информацию о текущем состоянии разговора.
- **Интеграции:** Поддерживает интеграцию с различными платформами, такими как Google Assistant, Facebook Messenger, Slack, Telegram, и другими.
- **Webhook:** Поддерживает Webhook-интеграции для вызова внешних сервисов и API.

## Классы

### `Dialogflow`

**Описание**: Класс `Dialogflow` предоставляет интерфейс для взаимодействия с API Google Dialogflow.

**Принцип работы**:
Класс инициализируется с использованием идентификатора проекта и идентификатора сессии. Он содержит методы для обнаружения намерений, получения списка намерений, создания и удаления намерений.

**Методы**:
- `__init__(self, project_id: str, session_id: str)`: Инициализирует клиент Dialogflow с указанным project_id и session_id.
- `detect_intent(self, text: str, language_code: str = "ru-RU") -> str`: Определяет намерение пользователя на основе введенного текста.
- `list_intents(self) -> list`: Получает список всех намерений, определенных в проекте Dialogflow.
- `create_intent(self, display_name: str, training_phrases_parts: list, message_texts: list) -> str`: Создает новое намерение в проекте Dialogflow.
- `delete_intent(self, intent_id: str) -> None`: Удаляет указанное намерение из проекта Dialogflow.

**Параметры**:
- `project_id` (str): Идентификатор проекта в Google Cloud Platform.
- `session_id` (str): Уникальный идентификатор сессии.
- `text` (str): Текст запроса пользователя.
- `language_code` (str): Языковой код запроса (по умолчанию "ru-RU").
- `display_name` (str): Отображаемое имя создаваемого намерения.
- `training_phrases_parts` (list): Список фраз для обучения намерения.
- `message_texts` (list): Список текстовых ответов для намерения.
- `intent_id` (str): Идентификатор намерения для удаления.

**Примеры**
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