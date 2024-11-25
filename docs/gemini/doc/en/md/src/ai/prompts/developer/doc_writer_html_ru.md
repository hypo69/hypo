# Модуль: Ассистент Программирования

Этот модуль содержит класс `CodeAssistant`, который используется для взаимодействия с различными моделями ИИ, такими как Google Gemini и OpenAI, для задач обработки кода.

## Описание

Этот модуль предоставляет инструменты для обработки файлов кода с использованием моделей ИИ.

## Примеры использования

```python
assistant = CodeAssistant(role='code_checker', lang='ru', model=['gemini'])
assistant.process_files()
```

```python
try:
    assistant = CodeAssistant(role='code_formatter', lang='ru', model=['gemini'])
    result = assistant.format_code(file_path='my_file.py')
    print(result)
except FileNotFoundError as ex:
    print(f"Ошибка: {ex}")
```

## Платформы
- Python 3.x

## СинOPSIS

Модуль позволяет обрабатывать файлы кода и форматировать их с помощью моделей ИИ.

## Классы

### `CodeAssistant`

**Описание**: Класс `CodeAssistant` используется для взаимодействия с различными моделями ИИ, такими как Google Gemini, и предоставляет методы для анализа и генерации документации для кода.

**Атрибуты**
- `role` (str): Роль ассистента (например, 'code_checker').
- `lang` (str): Язык, на котором будет работать ассистент (например, 'ru').
- `model` (list): Список используемых ИИ моделей (например, ['gemini']).

**Методы**

#### `process_files`

**Описание**: Метод для обработки файлов кода.

**Параметры**:
- `files` (list): Список путей к файлам для обработки.
- `options` (dict, optional): Дополнительные параметры для настройки обработки.


**Возвращаемое значение**:
- `list`: Список результатов обработки файлов.

**Примеры**:

```python
assistant = CodeAssistant(role='code_checker', lang='ru', model=['gemini'])
result = assistant.process_files(files=['file1.py', 'file2.py'], options={})
```

#### `format_code`

**Описание**: Метод для форматирования кода в указанном файле.

**Параметры**:
- `file_path` (str): Путь к файлу, который необходимо отформатировать.

**Возвращаемое значение**:
- `str`: Отформатированный код. Возвращает `None`, если файл не найден.

**Исключения**:
- `FileNotFoundError`: Файл не найден.


```python
assistant = CodeAssistant(role='code_formatter', lang='ru', model=['gemini'])
formatted_code = assistant.format_code(file_path='my_code.py')
```

**Примечание**: Документация для методов `process_files` и `format_code` может быть дополнена деталями, например, детальным описанием дополнительных параметров в `options`, описанием структуры возвращаемого списка `result`, и т.д.