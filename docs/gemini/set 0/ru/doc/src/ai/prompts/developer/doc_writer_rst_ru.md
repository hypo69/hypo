# Модуль для работы с ассистентом программиста

## Обзор

Этот модуль предоставляет класс `CodeAssistant` для взаимодействия с моделями ИИ (такими как Google Gemini и OpenAI) для выполнения задач по обработке кода.  Класс предназначен для анализа и создания документации Python-кода.

## Примеры использования

.. code-block:: python

    from hypotez.src.ai.prompts.developer.code_assistant import CodeAssistant

    assistant = CodeAssistant(role='code_checker', lang='ru', model=['gemini'])
    result = assistant.process_files(['file1.py', 'file2.py'])
    print(result)

## Классы

### `CodeAssistant`

**Описание**: Класс для работы с ассистентом программиста.  Позволяет взаимодействовать с различными моделями ИИ для обработки задач по коду.

**Атрибуты**

- `role` (str): Роль ассистента (например, 'code_checker').
- `lang` (str): Язык, на котором работает ассистент.
- `model` (list): Список используемых моделей ИИ.

**Методы**

#### `process_files`

**Описание**: Метод для обработки файлов с кодом.

**Параметры**

- `files` (list): Список путей к файлам для обработки.

**Возвращает**

- `dict`: Результат обработки файлов в виде словаря.

**Примеры использования**

.. code-block:: python

    assistant = CodeAssistant(role='code_checker', lang='ru', model=['gemini'])
    result = assistant.process_files(['file1.py', 'file2.py'])
    # Обработка результата

## Функции

(Список функций отсутствует в входных данных)

## Исключения

(Список исключений отсутствует в входных данных)


## Платформы

(Данные о платформах отсутствуют в входных данных)

## Синопсис

(Данные о синопсисе отсутствуют в входных данных)