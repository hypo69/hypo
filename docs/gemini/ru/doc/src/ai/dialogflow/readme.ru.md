# Документация для `src.ai.dialogflow`

## Обзор

Этот модуль предназначен для интеграции с Google Dialogflow и предоставляет инструменты для создания разговорных ИИ-приложений. Он обеспечивает определение намерений пользователя, работу с сущностями, управление контекстами и интеграцию с различными платформами.

## Подробней

Модуль `src.ai.dialogflow` позволяет взаимодействовать с Google Dialogflow API для обработки естественного языка (NLU) и создания разговорных интерфейсов. Он используется для определения намерений пользователя, извлечения ключевых данных из фраз, управления диалогом и интеграции с различными платформами.

## Классы

### `Dialogflow`

**Описание**: Класс для взаимодействия с Google Dialogflow API.

**Методы**:
- `detect_intent`: Определяет намерение пользователя на основе введенного текста.
- `list_intents`: Получает список всех намерений в проекте Dialogflow.
- `create_intent`: Создает новое намерение с указанными параметрами.
- `delete_intent`: Удаляет указанное намерение.

**Параметры**:
- `project_id` (str): Идентификатор проекта в Google Cloud.
- `session_id` (str): Уникальный идентификатор сессии.

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
```

## Функции

### `detect_intent`

```python
   def detect_intent(self, text: str, language_code: str = "ru") -> str:
       """
       Args:
           text (str): _description_
           language_code (str, optional): _description_. Defaults to "ru".

       Returns:
           str: _description_
       """
```

**Описание**: Определяет намерение пользователя на основе введенного текста.

**Параметры**:
- `text` (str): Текст для анализа.
- `language_code` (str, optional): Код языка текста. По умолчанию "ru".

**Возвращает**:
- `str`: Ответ Dialogflow API с информацией о распознанном намерении.

**Примеры**:

Примеры вызовов

### `list_intents`

```python
def list_intents(self, language_code: str = "ru") -> list[str]:
    """
    Args:
        language_code (str, optional): _description_. Defaults to "ru".

    Returns:
        list[str]: _description_
    """
```

**Описание**: Получает список всех намерений в проекте Dialogflow.

**Параметры**:
- `language_code` (str, optional): Код языка для возвращаемых намерений. По умолчанию "ru".

**Возвращает**:
- `list[str]`: Список всех намерений в проекте Dialogflow.

**Примеры**:

Примеры вызовов

### `create_intent`

```python
 def create_intent(
        self,
        display_name: str,
        training_phrases_parts: list[str],
        message_texts: list[str],
        language_code: str = "ru",
    ) -> str:
        """
        Args:
            display_name (str): _description_
            training_phrases_parts (list[str]): _description_
            message_texts (list[str]): _description_
            language_code (str, optional): _description_. Defaults to "ru".

        Returns:
            str: _description_
        """
```

**Описание**: Создает новое намерение с указанными параметрами.

**Параметры**:
- `display_name` (str): Отображаемое имя намерения.
- `training_phrases_parts` (list[str]): Список фраз для обучения модели.
- `message_texts` (list[str]): Список ответов, которые будут возвращаться при срабатывании намерения.
- `language_code` (str, optional): Код языка для намерения. По умолчанию "ru".

**Возвращает**:
- `str`: Ответ Dialogflow API с информацией о созданном намерении.

**Примеры**:

Примеры вызовов

### `delete_intent`

```python
def delete_intent(self, intent_id: str) -> None:
    """
    Args:
        intent_id (str): _description_
    """
```

**Описание**: Удаляет указанное намерение.

**Параметры**:
- `intent_id` (str): Идентификатор намерения для удаления.

**Примеры**:

Примеры вызовов