# Модуль `dialogflow`

## Обзор

Модуль `dialogflow` предоставляет интеграцию с платформой Dialogflow для обработки естественного языка и создания чат-ботов. Он обеспечивает возможности распознавания намерений пользователей, извлечения сущностей из фраз, управления контекстом диалога и интеграцию с различными платформами.

## Функции

### `Dialogflow`

**Описание**: Класс `Dialogflow` отвечает за взаимодействие с сервисом Dialogflow.

**Параметры**:
- `project_id` (str): Идентификатор проекта Dialogflow.
- `session_id` (str): Идентификатор сессии.

**Методы**:

#### `detect_intent(text: str) -> dict | None`

**Описание**: Обнаруживает намерение пользователя на основе входного текста.

**Параметры**:
- `text` (str): Входной текст от пользователя.

**Возвращает**:
- `dict | None`: Словарь с результатами распознавания намерения. Возвращает `None` при ошибке.

**Вызывает исключения**:
- `ValueError`: Если входной параметр `text` не является строкой.
- `DialogflowError`: При возникновении ошибки Dialogflow.


#### `list_intents() -> list | None`

**Описание**: Возвращает список намерений из Dialogflow.

**Возвращает**:
- `list | None`: Список намерений. Возвращает `None` при ошибке.

**Вызывает исключения**:
- `DialogflowError`: При возникновении ошибки Dialogflow.


#### `create_intent(display_name: str, training_phrases_parts: list[str], message_texts: list[str]) -> dict | None`

**Описание**: Создаёт новое намерение в Dialogflow.

**Параметры**:
- `display_name` (str): Отображаемое имя намерения.
- `training_phrases_parts` (list[str]): Список фрагментов фраз для обучения.
- `message_texts` (list[str]): Список текстов ответов на это намерение.

**Возвращает**:
- `dict | None`: Словарь с результатами создания намерения. Возвращает `None` при ошибке.

**Вызывает исключения**:
- `ValueError`: Если любой из входных параметров имеет неверный тип.
- `DialogflowError`: При возникновении ошибки Dialogflow.


#### `delete_intent(intent_id: str) -> bool | None`

**Описание**: Удаляет намерение из Dialogflow.

**Параметры**:
- `intent_id` (str): Идентификатор намерения для удаления.

**Возвращает**:
- `bool | None`: `True`, если намерение удалено успешно, `None` при ошибке.

**Вызывает исключения**:
- `ValueError`: Если `intent_id` не является строкой.
- `DialogflowError`: При возникновении ошибки Dialogflow.


## Пример использования

```python
from src.ai.dialogflow import Dialogflow

project_id = "ваш-идентификатор-проекта"
session_id = "ваш-идентификатор-сессии"

dialogflow_client = Dialogflow(project_id, session_id)

try:
    intent_response = dialogflow_client.detect_intent("Привет!")
    print("Detected Intent:", intent_response)

    intents = dialogflow_client.list_intents()
    print("List of Intents:", intents)
except DialogflowError as ex:
    print(f"Произошла ошибка Dialogflow: {ex}")
```

**Примечание**: Замените `"ваш-идентификатор-проекта"` и `"ваш-идентификатор-сессии"` на ваши реальные значения. Обратите внимание на обработку исключения `DialogflowError`.