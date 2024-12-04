# Модуль для работы с помощником по программированию

## Обзор

Данный модуль содержит класс `CodeAssistant`, предназначенный для взаимодействия с различными моделями ИИ, такими как Google Gemini и OpenAI, для задач обработки кода.  Модуль предоставляет методы для анализа и генерации документации по коду.

## Примеры использования

```python
from hypotez.src.ai.prompts.developer.code_assistant import CodeAssistant

assistant = CodeAssistant(role='code_checker', lang='ru', model=['gemini'])
result = assistant.process_files(files=['file1.py', 'file2.py'], options={})
print(result)
```

## Классы

### `CodeAssistant`

**Описание**: Класс для работы с помощником по программированию.  Он предоставляет интерфейс для взаимодействия с моделями ИИ и выполнения задач анализа и генерации документации.

**Атрибуты**:

- `role` (str): Роль помощника (например, 'code_checker').
- `lang` (str): Язык, который будет использовать помощник (например, 'ru').
- `model` (list): Список используемых моделей ИИ (например, ['gemini']).


**Методы**:

#### `process_files`

**Описание**: Метод для обработки файлов кода.

**Параметры**:
- `files` (list): Список файлов для обработки.
- `options` (dict, optional): Дополнительные параметры для настройки обработки. По умолчанию пустой словарь.


**Возвращает**:
- list: Список результатов обработки, содержащий проанализированные данные.


**Вызывает исключения**:
- `FileNotFoundError`: Если какой-либо из файлов в списке `files` не найден.
- `ValueError`: Если передан некорректный тип данных или значение для параметров `files` или `options`.
- `Exception`: В случае возникновения других ошибок во время обработки.


```python
# Пример использования
assistant = CodeAssistant(role='code_checker', lang='ru', model=['gemini'])
try:
    result = assistant.process_files(files=['file1.py', 'file2.py'], options={})
    print(result)
except FileNotFoundError as ex:
    print(f"Ошибка: {ex}")
except ValueError as ex:
    print(f"Ошибка: {ex}")
except Exception as ex:
    print(f"Произошла непредвиденная ошибка: {ex}")

```


## Функции

(Здесь будут описаны функции, если они есть в исходном коде.)


## Обработка исключений

(Здесь будут описаны все типы исключений, которые могут быть возбуждены методами.)