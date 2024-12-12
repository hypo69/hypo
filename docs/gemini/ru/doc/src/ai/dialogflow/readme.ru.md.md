# Модуль `src.ai.dialogflow`

## Обзор

Модуль `src.ai.dialogflow` предоставляет интеграцию с Google Dialogflow, обеспечивая возможности обработки естественного языка (NLU) и создания разговорных ИИ-приложений. Он включает в себя функции определения намерений, работы с сущностями, контекстами, интеграции с различными платформами и Webhook-интеграции.

## Оглавление

1. [Обзор](#обзор)
2. [Функции](#функции)
   - [`detect_intent`](#detect_intent)
   - [`list_intents`](#list_intents)
   - [`create_intent`](#create_intent)
   - [`delete_intent`](#delete_intent)
3. [Класс `Dialogflow`](#класс-dialogflow)
   - [Метод `__init__`](#__init__)
   - [Метод `detect_intent`](#detect_intent-1)
   - [Метод `list_intents`](#list_intents-1)
   - [Метод `create_intent`](#create_intent-1)
   - [Метод `delete_intent`](#delete_intent-1)

## Функции

### `detect_intent`

**Описание**:
   Эта функция отправляет запрос на обнаружение намерения в Dialogflow.

**Параметры**:
- `text` (str): Текст, который нужно проанализировать.

**Возвращает**:
- `dict | None`: Ответ от Dialogflow в виде словаря или `None` в случае ошибки.

**Вызывает исключения**:
- `google.api_core.exceptions.GoogleAPIError`: Если произошла ошибка при вызове API Dialogflow.
- `Exception`: Если возникла любая другая ошибка.

### `list_intents`

**Описание**:
   Эта функция извлекает список доступных интентов из Dialogflow.

**Параметры**:
   - Нет

**Возвращает**:
   - `list[dict] | None`: Список интентов в виде словаря или `None`, если не удалось получить список интентов.

**Вызывает исключения**:
   - `google.api_core.exceptions.GoogleAPIError`: Если произошла ошибка при вызове API Dialogflow.
   - `Exception`: Если возникла любая другая ошибка.

### `create_intent`

**Описание**:
   Эта функция создает новый интент в Dialogflow.

**Параметры**:
   - `display_name` (str): Отображаемое имя интента.
   - `training_phrases_parts` (list[str]): Список фраз для обучения модели.
   - `message_texts` (list[str]): Список текстовых ответов для интента.

**Возвращает**:
   - `dict | None`: Словарь с данными созданного интента или `None` в случае ошибки.

**Вызывает исключения**:
   - `google.api_core.exceptions.GoogleAPIError`: Если произошла ошибка при вызове API Dialogflow.
   - `Exception`: Если возникла любая другая ошибка.

### `delete_intent`

**Описание**:
   Эта функция удаляет интент из Dialogflow по его идентификатору.

**Параметры**:
   - `intent_id` (str): Идентификатор удаляемого интента.

**Возвращает**:
   - `None`: Ничего не возвращает.

**Вызывает исключения**:
   - `google.api_core.exceptions.GoogleAPIError`: Если произошла ошибка при вызове API Dialogflow.
   - `Exception`: Если возникла любая другая ошибка.

## Класс `Dialogflow`

### `__init__`

**Описание**:
   Конструктор класса `Dialogflow`. Инициализирует клиента Dialogflow.

**Параметры**:
   - `project_id` (str): Идентификатор проекта Dialogflow.
   - `session_id` (str): Идентификатор сессии Dialogflow.

**Возвращает**:
   - `None`: Ничего не возвращает.

### `detect_intent`

**Описание**:
   Отправляет запрос на обнаружение намерения в Dialogflow.

**Параметры**:
   - `text` (str): Текст, который нужно проанализировать.

**Возвращает**:
   - `dict | None`: Ответ от Dialogflow в виде словаря или `None` в случае ошибки.

**Вызывает исключения**:
- `google.api_core.exceptions.GoogleAPIError`: Если произошла ошибка при вызове API Dialogflow.
- `Exception`: Если возникла любая другая ошибка.

### `list_intents`

**Описание**:
   Извлекает список доступных интентов из Dialogflow.

**Параметры**:
   - Нет.

**Возвращает**:
   - `list[dict] | None`: Список интентов в виде словаря или `None`, если не удалось получить список интентов.

**Вызывает исключения**:
   - `google.api_core.exceptions.GoogleAPIError`: Если произошла ошибка при вызове API Dialogflow.
   - `Exception`: Если возникла любая другая ошибка.

### `create_intent`

**Описание**:
   Создает новый интент в Dialogflow.

**Параметры**:
   - `display_name` (str): Отображаемое имя интента.
   - `training_phrases_parts` (list[str]): Список фраз для обучения модели.
   - `message_texts` (list[str]): Список текстовых ответов для интента.

**Возвращает**:
   - `dict | None`: Словарь с данными созданного интента или `None` в случае ошибки.

**Вызывает исключения**:
   - `google.api_core.exceptions.GoogleAPIError`: Если произошла ошибка при вызове API Dialogflow.
   - `Exception`: Если возникла любая другая ошибка.

### `delete_intent`

**Описание**:
   Удаляет интент из Dialogflow по его идентификатору.

**Параметры**:
   - `intent_id` (str): Идентификатор удаляемого интента.

**Возвращает**:
   - `None`: Ничего не возвращает.

**Вызывает исключения**:
   - `google.api_core.exceptions.GoogleAPIError`: Если произошла ошибка при вызове API Dialogflow.
   - `Exception`: Если возникла любая другая ошибка.