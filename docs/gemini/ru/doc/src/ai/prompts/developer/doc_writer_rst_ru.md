# Модуль для работы с ассистентом программиста

## Обзор

Этот модуль содержит класс `CodeAssistant`, предназначенный для взаимодействия с моделями ИИ (например, Google Gemini и OpenAI) для выполнения задач по обработке кода.  Класс предоставляет методы для анализа и создания документации кода.

## Примеры использования

.. code-block:: python

    from hypotez.src.ai.prompts.developer.code_assistant import CodeAssistant

    assistant = CodeAssistant(role='code_checker', lang='ru', model=['gemini'])
    result = assistant.process_files(['file1.py', 'file2.py'])
    print(result)

## Классы

### `CodeAssistant`

**Описание**:  Класс для взаимодействия с моделями ИИ, такими как Google Gemini, для анализа и генерации информации о коде.

**Атрибуты**:

- `role` (str): Роль ассистента (например, 'code_checker').
- `lang` (str): Язык, на котором будет работать ассистент (например, 'ru').
- `model` (list): Список используемых моделей ИИ (например, ['gemini']).

**Методы**:

#### `process_files`

**Описание**: Метод для обработки файлов с кодом.

**Параметры**:

- `files` (list): Список путей к файлам для обработки.
- `options` (dict, optional): Словарь с дополнительными параметрами для настройки обработки.

**Возвращает**:

- list: Список результатов обработки файлов (с описанием ошибок или информации). Возвращает None при ошибке.

**Пример использования**:

.. code-block:: python

    from hypotez.src.ai.prompts.developer.code_assistant import CodeAssistant

    assistant = CodeAssistant(role='code_checker', lang='ru', model=['gemini'])
    try:
        result = assistant.process_files(['file1.py', 'file2.py'])
        print(result)  # Обработка результата
    except Exception as ex:
        print(f"Ошибка при обработке файлов: {ex}")



## Функции

(В данном модуле нет отдельных функций, только методы класса.)


## Обработка исключений

Этот модуль обрабатывает исключения, связанные с работой с файлами и моделями ИИ.  В методе `process_files` предусмотрен блок `try...except`, позволяющий обрабатывать потенциальные ошибки при чтении файлов, запросах к моделям и других операциях.

**Примеры обработки исключений**:

.. code-block:: python

    try:
        # Код, который может вызвать исключение
        assistant.process_files(['file1.py', 'file2.py'])
    except FileNotFoundError as ex:
        print(f"Ошибка: Файл не найден - {ex}")
    except Exception as ex:  # Обработка других ошибок
        print(f"Непредвиденная ошибка: {ex}")

```
**Примечание:**  Этот шаблон предполагает, что в файле `hypotez/src/ai/prompts/developer/code_assistant.py` определён класс `CodeAssistant` с методом `process_files`. Для более полной документации потребуется код этого файла.  Также добавлены примеры обработки исключений, которые могут быть полезны в реальных сценариях.  Вместо `file1.py` и `file2.py` необходимо подставить реальные пути к файлам.