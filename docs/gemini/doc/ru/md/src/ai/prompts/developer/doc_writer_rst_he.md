# Документация модуля CodeAssistant

## Обзор

Модуль `CodeAssistant` предназначен для работы с различными моделями ИИ, такими как Google Gemini и OpenAI, для выполнения задач обработки кода. Модуль предоставляет класс `CodeAssistant`, позволяющий взаимодействовать с выбранной моделью ИИ.

## Примеры использования

```python
from hypotez.ai.prompts.developer.doc_writer_rst_he import CodeAssistant

assistant = CodeAssistant(role='code_checker', lang='ru', model=['gemini'])
assistant.process_files()
```

## Классы

### `CodeAssistant`

**Описание**: Класс `CodeAssistant` служит для взаимодействия с моделями ИИ, предоставляя методы для анализа и генерации кода.

**Атрибуты**:

- `role` (str): Роль помощника (например, 'code_checker').
- `lang` (str): Язык, на котором будет работать помощник (например, 'ru').
- `model` (list): Список используемых моделей ИИ (например, ['gemini']).


**Методы**:

#### `process_files()`

**Описание**: Метод для обработки списка файлов.


**Параметры**:

- `files` (list): Список путей к файлам для обработки.
- `options` (dict, optional): Дополнительные параметры обработки. По умолчанию пустое значение.


**Возвращает**:

- list: Список обработанных файлов (в данном случае, просто возвращается тот же самый список файлов).


**Обрабатываемые исключения**:

- `FileNotFoundError`: Если один из файлов в списке не найден.
- `Exception`: Другие исключения, которые могут возникнуть во время выполнения.


**Пример использования**:

```python
from hypotez.ai.prompts.developer.doc_writer_rst_he import CodeAssistant

assistant = CodeAssistant(role='code_checker', lang='ru', model=['gemini'])
files_to_process = ['file1.py', 'file2.py']
try:
    result = assistant.process_files(files=files_to_process, options={})
    print(result)
except FileNotFoundError as ex:
    print(f"Ошибка: {ex}")
```


## Функции

(Нет функций в данном коде)


```