# Модуль для работы с помощником кода

## Обзор

Этот модуль предоставляет класс `CodeAssistant` для работы с различными моделями ИИ, такими как Google Gemini и OpenAI, для выполнения задач по обработке кода.  Он позволяет передавать файлы на обработку и получать результаты.

## Примеры использования

```python
from hypotez.src.ai.prompts.developer.doc_writer_rst_he import CodeAssistant

assistant = CodeAssistant(role='code_checker', lang='ru', model=['gemini'])
result = assistant.process_files(files=['file1.py', 'file2.py'], options={'max_tokens': 500})
print(result)
```

## Классы

### `CodeAssistant`

**Описание**: Класс для работы с помощником кода.

**Атрибуты**:

- `role` (str): Роль помощника (например, 'code_checker').
- `lang` (str): Язык, на котором будет работать помощник (например, 'ru').
- `model` (list): Список используемых моделей ИИ (например, ['gemini']).

**Методы**:

- `process_files(files: list[str], options: dict = {}) -> list[str]`: Обрабатывает список файлов.

    **Описание**: Метод обрабатывает список файлов, используя выбранные модели ИИ.

    **Параметры**:
    - `files` (list[str]): Список путей к файлам.
    - `options` (dict, optional): Словарь дополнительных параметров.

    **Возвращает**:
    - list[str]: Список результатов обработки файлов.

    **Обрабатываемые исключения**:
    - `ValueError`: Если не указаны файлы для обработки.
    - `FileNotFoundError`: Если файл не найден.
    - `Exception`: Общие исключения при обработке файлов.


## Функции

(Здесь будут функции, если они есть)


```