# Модуль `src.ai.dialogflow`

## Обзор

Модуль `src.ai.dialogflow` предназначен для интеграции с Google Dialogflow. Он предоставляет возможности для обработки естественного языка (NLU) и создания разговорных ИИ-приложений. Модуль включает в себя функции для определения намерений, работы с сущностями, контекстами, интеграции с различными платформами и Webhook.

## Оглавление

1.  [Обзор](#обзор)
2.  [Классы](#классы)
    *   [`Dialogflow`](#dialogflow)
3.  [Функции](#функции)
    *   [`detect_intent`](#detect_intent)
    *  [`list_intents`](#list_intents)
    *  [`create_intent`](#create_intent)
    *  [`delete_intent`](#delete_intent)


## Классы

### `Dialogflow`

**Описание**: Класс для взаимодействия с Google Dialogflow API.

**Методы**:
   - [`__init__`](#__init__): Инициализирует клиент Dialogflow.
   - [`detect_intent`](#detect_intent): Определяет намерение пользователя на основе введенного текста.
   - [`list_intents`](#list_intents): Получает список всех намерений.
   - [`create_intent`](#create_intent): Создает новое намерение.
   - [`delete_intent`](#delete_intent): Удаляет намерение.

#### `__init__`
```python
def __init__(project_id: str, session_id: str) -> None:
    """
    Args:
        project_id (str): ID проекта Dialogflow.
        session_id (str): ID сессии.

    Returns:
        None
    """
```
**Описание**: Инициализирует клиент Dialogflow.

**Параметры**:
- `project_id` (str): ID проекта Dialogflow.
- `session_id` (str): ID сессии.

**Возвращает**:
- `None`

## Функции

### `detect_intent`
```python
def detect_intent(self, text: str, language_code: str = "ru-RU") -> dict:
    """
    Args:
        text (str): Текст запроса пользователя.
        language_code (str, optional): Языковой код. По умолчанию "ru-RU".

    Returns:
        dict: Ответ от Dialogflow API в формате словаря.

    Raises:
        Exception: В случае ошибки при взаимодействии с Dialogflow API.
    """
```

**Описание**: Определяет намерение пользователя на основе введенного текста.

**Параметры**:
- `text` (str): Текст запроса пользователя.
- `language_code` (str, optional): Языковой код. По умолчанию `"ru-RU"`.

**Возвращает**:
- `dict`: Ответ от Dialogflow API в формате словаря.

**Вызывает исключения**:
- `Exception`: В случае ошибки при взаимодействии с Dialogflow API.

### `list_intents`
```python
def list_intents(self) -> list:
    """
    Args:
        None

    Returns:
        list: Список всех намерений в проекте.

    Raises:
        Exception: В случае ошибки при взаимодействии с Dialogflow API.
    """
```

**Описание**: Получает список всех намерений в проекте Dialogflow.

**Параметры**:
- `None`

**Возвращает**:
- `list`: Список всех намерений в проекте.

**Вызывает исключения**:
- `Exception`: В случае ошибки при взаимодействии с Dialogflow API.

### `create_intent`
```python
def create_intent(self, display_name: str, training_phrases_parts: list, message_texts: list) -> dict:
    """
    Args:
        display_name (str): Отображаемое имя нового намерения.
        training_phrases_parts (list): Список фраз для обучения модели.
        message_texts (list): Список текстовых ответов.

    Returns:
        dict: Информация о созданном намерении.

    Raises:
         Exception: В случае ошибки при взаимодействии с Dialogflow API.
    """
```

**Описание**: Создает новое намерение в Dialogflow.

**Параметры**:
- `display_name` (str): Отображаемое имя нового намерения.
- `training_phrases_parts` (list): Список фраз для обучения модели.
- `message_texts` (list): Список текстовых ответов.

**Возвращает**:
- `dict`: Информация о созданном намерении.

**Вызывает исключения**:
- `Exception`: В случае ошибки при взаимодействии с Dialogflow API.

### `delete_intent`
```python
def delete_intent(self, intent_id: str) -> None:
    """
    Args:
        intent_id (str): ID намерения для удаления.

    Returns:
        None

    Raises:
         Exception: В случае ошибки при взаимодействии с Dialogflow API.
    """
```

**Описание**: Удаляет намерение из Dialogflow.

**Параметры**:
- `intent_id` (str): ID намерения для удаления.

**Возвращает**:
- `None`

**Вызывает исключения**:
- `Exception`: В случае ошибки при взаимодействии с Dialogflow API.