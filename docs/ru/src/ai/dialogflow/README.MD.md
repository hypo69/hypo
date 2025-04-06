# Документация для модуля `src.ai.dialogflow`

## Обзор

Этот модуль предоставляет интеграцию с Dialogflow и обеспечивает возможности для понимания естественного языка (NLU) и создания диалоговых AI-приложений. Он включает следующие основные функции:

- **Определение намерений:** Определяет намерения пользователя на основе введенного текста.
- **Распознавание сущностей:** Извлекает ключевые данные из фраз пользователя.
- **Контексты:** Управляет разговором, сохраняя информацию о текущем состоянии диалога.
- **Интеграции:** Поддерживает интеграцию с различными платформами, такими как Google Assistant, Facebook Messenger, Slack, Telegram и другие.
- **Webhook:** Поддерживает интеграции Webhook для вызова внешних сервисов и API.

## Подробней

Модуль `src.ai.dialogflow` предназначен для упрощения взаимодействия с Dialogflow API. Он позволяет создавать, читать, обновлять и удалять намерения, а также обнаруживать намерения на основе входных данных пользователя. Этот модуль упрощает интеграцию Dialogflow в проект `hypotez`, обеспечивая унифицированный интерфейс для работы с функциями Dialogflow.

## Содержание

1.  [Классы](#Классы)
2.  [Пример использования](#Пример-использования)

## Классы

### `Dialogflow`

**Описание**: Класс для взаимодействия с Dialogflow API.

**Принцип работы**: Класс инициализируется с project_id и session_id, необходимыми для аутентификации и идентификации сессии в Dialogflow. Он предоставляет методы для создания, чтения, обновления и удаления намерений, а также для обнаружения намерений на основе входных данных пользователя.

**Аттрибуты**:

*   `project_id` (str): Идентификатор проекта Dialogflow.
*   `session_id` (str): Уникальный идентификатор сессии Dialogflow.
*   `client` (google.cloud.dialogflow_v2.IntentsClient): Клиент для работы с Intents API.
*   `session_client` (google.cloud.dialogflow_v2.SessionsClient): Клиент для работы с Sessions API.
*   `language_code` (str): Код языка для запросов Dialogflow.

**Методы**:

*   `__init__(project_id: str, session_id: str)`: Инициализирует экземпляр класса `Dialogflow`.
*   `detect_intent(text: str) -> str`: Определяет намерение пользователя на основе введенного текста.
*   `list_intents() -> list`: Возвращает список всех намерений в проекте.
*   `create_intent(display_name: str, training_phrases_parts: list, message_texts: list) -> google.cloud.dialogflow_v2.intent.Intent`: Создает новое намерение.
*   `delete_intent(intent_id: str) -> None`: Удаляет намерение по его идентификатору.

## Функции

### `detect_intent`

```python
def detect_intent(text: str) -> str:
    """Определяет намерение пользователя на основе введенного текста.
    Args:
        text (str): Входной текст пользователя.

    Returns:
        str: Ответ от Dialogflow.
    """
    ...
```

**Назначение**: Определяет намерение пользователя на основе предоставленного текста, используя Dialogflow API.

**Параметры**:

*   `text` (str): Входной текст пользователя, который нужно проанализировать.

**Возвращает**:

*   `str`: Ответ от Dialogflow, содержащий информацию о распознанном намерении.

**Как работает функция**:

1.  Формируется имя сессии на основе `project_id` и `session_id`.
2.  Создается текстовый ввод (`text_input`) с указанием языка.
3.  Формируется запрос (`query_input`) на основе текстового ввода.
4.  Вызывается метод `detect_intent` клиента сессий Dialogflow для определения намерения.
5.  Извлекается и возвращается ответ от Dialogflow.

**ASCII flowchart**:

```
Начало
    ↓
Формирование имени сессии
    ↓
Создание текстового ввода (text_input)
    ↓
Формирование запроса (query_input)
    ↓
Вызов detect_intent клиента сессий Dialogflow
    ↓
Извлечение ответа от Dialogflow
    ↓
Конец
```

**Примеры**:

```python
from src.ai.dialogflow import Dialogflow

project_id = "your-project-id"
session_id = "unique-session-id"
dialogflow_client = Dialogflow(project_id, session_id)

intent_response = dialogflow_client.detect_intent("Hello")
print("Detected Intent:", intent_response)
```

### `list_intents`

```python
def list_intents() -> list:
    """Возвращает список всех намерений в проекте.
    Returns:
        list: Список всех намерений в проекте.
    """
    ...
```

**Назначение**: Получает список всех намерений, определенных в проекте Dialogflow.

**Возвращает**:

*   `list`: Список всех намерений в проекте Dialogflow.

**Как работает функция**:

1.  Формируется имя родителя (project name) для запроса списка намерений.
2.  Вызывается метод `list_intents` клиента намерений Dialogflow для получения списка.
3.  Возвращается список всех намерений.

**ASCII flowchart**:

```
Начало
    ↓
Формирование имени родителя (project name)
    ↓
Вызов list_intents клиента намерений Dialogflow
    ↓
Возврат списка всех намерений
    ↓
Конец
```

**Примеры**:

```python
from src.ai.dialogflow import Dialogflow

project_id = "your-project-id"
session_id = "unique-session-id"
dialogflow_client = Dialogflow(project_id, session_id)

intents = dialogflow_client.list_intents()
print("List of Intents:", intents)
```

### `create_intent`

```python
def create_intent(display_name: str, training_phrases_parts: list, message_texts: list) -> google.cloud.dialogflow_v2.intent.Intent:
    """Создает новое намерение.
    Args:
        display_name (str): Отображаемое имя нового намерения.
        training_phrases_parts (list): Список фраз для обучения.
        message_texts (list): Список текстовых сообщений для ответа.

    Returns:
        google.cloud.dialogflow_v2.intent.Intent: Созданное намерение.
    """
    ...
```

**Назначение**: Создает новое намерение в проекте Dialogflow с указанным отображаемым именем, обучающими фразами и текстовыми сообщениями для ответа.

**Параметры**:

*   `display_name` (str): Отображаемое имя нового намерения.
*   `training_phrases_parts` (list): Список фраз, которые будут использоваться для обучения модели распознавания намерений.
*   `message_texts` (list): Список текстовых сообщений, которые будут отправлены в качестве ответа, когда намерение будет распознано.

**Возвращает**:

*   `google.cloud.dialogflow_v2.intent.Intent`: Созданное намерение.

**Как работает функция**:

1.  Формируется имя родителя (project name) для создания намерения.
2.  Создаются обучающие фразы (`training_phrases`) на основе предоставленных частей фраз.
3.  Создается текстовое сообщение (`message`) на основе предоставленных текстовых сообщений.
4.  Создается ответное сообщение (`response_message`) на основе текстового сообщения.
5.  Формируется намерение (`intent`) с указанным отображаемым именем, обучающими фразами и ответным сообщением.
6.  Вызывается метод `create_intent` клиента намерений Dialogflow для создания нового намерения.
7.  Возвращается созданное намерение.

**ASCII flowchart**:

```
Начало
    ↓
Формирование имени родителя (project name)
    ↓
Создание обучающих фраз (training_phrases)
    ↓
Создание текстового сообщения (message)
    ↓
Создание ответного сообщения (response_message)
    ↓
Формирование намерения (intent)
    ↓
Вызов create_intent клиента намерений Dialogflow
    ↓
Возврат созданного намерения
    ↓
Конец
```

**Примеры**:

```python
from src.ai.dialogflow import Dialogflow

project_id = "your-project-id"
session_id = "unique-session-id"
dialogflow_client = Dialogflow(project_id, session_id)

new_intent = dialogflow_client.create_intent(
    display_name="NewIntent",
    training_phrases_parts=["new phrase", "another phrase"],
    message_texts=["This is a new intent"]
)
print("Created Intent:", new_intent)
```

### `delete_intent`

```python
def delete_intent(intent_id: str) -> None:
    """Удаляет намерение по его идентификатору.
    Args:
        intent_id (str): Идентификатор намерения, которое нужно удалить.
    """
    ...
```

**Назначение**: Удаляет указанное намерение из проекта Dialogflow по его идентификатору.

**Параметры**:

*   `intent_id` (str): Идентификатор намерения, которое необходимо удалить.

**Как работает функция**:

1.  Формируется имя намерения на основе `project_id` и `intent_id`.
2.  Вызывается метод `delete_intent` клиента намерений Dialogflow для удаления указанного намерения.

**ASCII flowchart**:

```
Начало
    ↓
Формирование имени намерения
    ↓
Вызов delete_intent клиента намерений Dialogflow
    ↓
Конец
```

**Примеры**:

```python
from src.ai.dialogflow import Dialogflow

project_id = "your-project-id"
session_id = "unique-session-id"
dialogflow_client = Dialogflow(project_id, session_id)

# Deleting an intent (make sure to replace intent_id with a real ID)
# dialogflow_client.delete_intent("your-intent-id")
```

## Пример использования

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