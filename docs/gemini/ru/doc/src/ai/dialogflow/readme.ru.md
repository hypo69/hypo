# Модуль `src.ai.dialogflow`

## Обзор

Модуль `src.ai.dialogflow` предназначен для интеграции с Google Dialogflow, предоставляя инструменты для обработки естественного языка (NLU) и создания разговорных ИИ-приложений. 

## Подробней

Этот модуль обеспечивает взаимодействие с Google Dialogflow API, упрощая задачи определения намерений пользователя, извлечения сущностей, управления контекстами и интеграции с различными платформами и сервисами. Он позволяет создавать, читать, обновлять и удалять намерения (intents) в Dialogflow.

## Содержание

- [Классы](#классы)
- [Функции](#функции)

## Классы

### `Dialogflow`

**Описание**: Класс `Dialogflow` предоставляет интерфейс для взаимодействия с Google Dialogflow API. Он позволяет выполнять операции, такие как определение намерений пользователя на основе текста, получение списка всех доступных намерений, создание новых намерений с заданными параметрами и удаление существующих намерений.

**Принцип работы**:

1.  Класс инициализируется с идентификатором проекта (project ID) и идентификатором сессии (session ID), необходимыми для аутентификации и взаимодействия с Dialogflow API.
2.  Для выполнения операций, таких как определение намерения или создание нового намерения, класс использует клиент Dialogflow API.
3.  Методы класса позволяют абстрагироваться от низкоуровневых деталей взаимодействия с API, предоставляя удобный интерфейс для выполнения основных задач.

**Аттрибуты**:

-   `project_id` (str): Идентификатор проекта в Google Cloud Platform.
-   `session_id` (str): Уникальный идентификатор сессии для Dialogflow.
-   `language_code` (str): Код языка, используемый в Dialogflow (по умолчанию 'ru-RU').
-   `session_client` (google.cloud.dialogflow_v2.SessionsClient): Клиент для управления сессиями Dialogflow.
-   `intents_client` (google.cloud.dialogflow_v2.IntentsClient): Клиент для управления намерениями Dialogflow.
-   `session` (str): Полное имя сессии в формате `projects/<project_id>/agent/sessions/<session_id>`.
-   `agent_path` (str): Путь к агенту Dialogflow.

**Методы**:

-   `__init__(project_id: str, session_id: str, language_code: str = 'ru-RU')`: Инициализирует экземпляр класса `Dialogflow`.
-   `detect_intent(text: str) -> str`: Определяет намерение пользователя на основе введенного текста.
-   `list_intents() -> list`: Возвращает список всех доступных намерений.
-   `create_intent(display_name: str, training_phrases_parts: list, message_texts: list) -> google.cloud.dialogflow_v2.Intent`: Создает новое намерение с заданными параметрами.
-   `delete_intent(intent_id: str) -> None`: Удаляет существующее намерение по его ID.

## Функции

### `detect_intent`

**Назначение**: Функция определяет намерение пользователя на основе введенного текста, используя Dialogflow API.

**Параметры**:

*   `text` (str): Текст, который необходимо проанализировать для определения намерения.

**Возвращает**:

*   `str`: Ответ от Dialogflow, содержащий информацию об определенном намерении.

**Вызывает исключения**:

*   Исключения, возникающие при взаимодействии с Dialogflow API, например, при отсутствии доступа к сервису или неправильной конфигурации.

**Как работает функция**:

1.  Функция принимает текст в качестве входных данных.
2.  Создает запрос к Dialogflow API для определения намерения на основе этого текста.
3.  Возвращает ответ от Dialogflow, который содержит информацию об определенном намерении.

**ASCII flowchart**:

```
Text input
     ↓
Create DetectIntentRequest
     ↓
Send request to Dialogflow API
     ↓
Receive response from Dialogflow
     ↓
Return response
```

**Примеры**:

```python
from src.ai.dialogflow import Dialogflow

project_id = "your-project-id"
session_id = "unique-session-id"

dialogflow_client = Dialogflow(project_id, session_id)

# Пример использования
intent_response = dialogflow_client.detect_intent("Привет")
print("Detected Intent:", intent_response)
```

### `list_intents`

**Назначение**: Функция возвращает список всех доступных намерений в Dialogflow.

**Параметры**:

*   Нет.

**Возвращает**:

*   `list`: Список всех доступных намерений.

**Вызывает исключения**:

*   Исключения, возникающие при взаимодействии с Dialogflow API, например, при отсутствии доступа к сервису или неправильной конфигурации.

**Как работает функция**:

1.  Функция отправляет запрос к Dialogflow API для получения списка всех доступных намерений.
2.  Возвращает список полученных намерений.

**ASCII flowchart**:

```
Start
     ↓
Send request to Dialogflow API to list intents
     ↓
Receive list of intents from Dialogflow
     ↓
Return list of intents
```

**Примеры**:

```python
from src.ai.dialogflow import Dialogflow

project_id = "your-project-id"
session_id = "unique-session-id"

dialogflow_client = Dialogflow(project_id, session_id)

# Пример использования
intents = dialogflow_client.list_intents()
print("List of Intents:", intents)
```

### `create_intent`

**Назначение**: Функция создает новое намерение с заданными параметрами в Dialogflow.

**Параметры**:

*   `display_name` (str): Отображаемое имя нового намерения.
*   `training_phrases_parts` (list): Список фраз для обучения модели распознавания намерений.
*   `message_texts` (list): Список текстовых сообщений, которые будут отправлены в ответ на распознанное намерение.

**Возвращает**:

*   `google.cloud.dialogflow_v2.Intent`: Объект, представляющий созданное намерение.

**Вызывает исключения**:

*   Исключения, возникающие при взаимодействии с Dialogflow API, например, при отсутствии доступа к сервису или неправильной конфигурации.

**Как работает функция**:

1.  Функция принимает имя намерения, список фраз для обучения и список текстовых сообщений в качестве входных данных.
2.  Создает запрос к Dialogflow API для создания нового намерения с этими параметрами.
3.  Возвращает объект, представляющий созданное намерение.

**ASCII flowchart**:

```
Start
     ↓
Prepare intent data
     ↓
Send request to Dialogflow API to create intent
     ↓
Receive created intent from Dialogflow
     ↓
Return created intent
```

**Примеры**:

```python
from src.ai.dialogflow import Dialogflow

project_id = "your-project-id"
session_id = "unique-session-id"

dialogflow_client = Dialogflow(project_id, session_id)

# Пример использования
new_intent = dialogflow_client.create_intent(
    display_name="NewIntent",
    training_phrases_parts=["new phrase", "another phrase"],
    message_texts=["This is a new intent"]
)
print("Created Intent:", new_intent)
```

### `delete_intent`

**Назначение**: Функция удаляет существующее намерение по его ID в Dialogflow.

**Параметры**:

*   `intent_id` (str): ID намерения, которое необходимо удалить.

**Возвращает**:

*   `None`: Функция ничего не возвращает.

**Вызывает исключения**:

*   Исключения, возникающие при взаимодействии с Dialogflow API, например, при отсутствии доступа к сервису, неправильной конфигурации или если намерение с указанным ID не существует.

**Как работает функция**:

1.  Функция принимает ID намерения, которое необходимо удалить.
2.  Создает запрос к Dialogflow API для удаления намерения с этим ID.
3.  Выполняет удаление намерения.

**ASCII flowchart**:

```
Start
     ↓
Get intent ID
     ↓
Send request to Dialogflow API to delete intent
     ↓
Delete intent
     ↓
End
```

**Примеры**:

```python
from src.ai.dialogflow import Dialogflow

project_id = "your-project-id"
session_id = "unique-session-id"

dialogflow_client = Dialogflow(project_id, session_id)

# Пример использования (не забудьте заменить intent_id на реальный ID)
# dialogflow_client.delete_intent("your-intent-id")
```