# Модуль для работы с помощником по программированию

## Обзор

Данный модуль содержит класс `CodeAssistant`, предназначенный для взаимодействия с различными моделями ИИ, такими как Google Gemini и OpenAI, для задач обработки кода.  Модуль позволяет анализировать и генерировать документацию для кода.

**Пример использования**

```python
from ai.prompts.developer.code_assistant import CodeAssistant

assistant = CodeAssistant(role='code_checker', lang='ru', model=['gemini'])
result = assistant.process_files(files=['file1.py', 'file2.py'], options={})
print(result)
```

**Платформы**:
- Python 3.x

**Синопсис**:
- Обработка файлов кода с использованием моделей ИИ.
- Генерирование документации по коду.


## Классы

### `CodeAssistant`

**Описание**: Класс для взаимодействия с помощником по программированию.

**Атрибуты**

- `role` (str): Роль помощника (например, 'code_checker').
- `lang` (str): Язык, который будет использовать помощник (например, 'ru').
- `model` (list): Список используемых моделей ИИ (например, ['gemini']).

**Методы**

#### `process_files`

**Описание**: Метод для обработки файлов кода.

**Параметры**:
- `files` (list): Список файлов для обработки.
- `options` (dict, опционально): Дополнительные параметры для настройки обработки. По умолчанию `{}`.

**Возвращает**:
- `list`: Список результатов обработки (анализированные данные).

**Вызывает исключения**:
- `FileNotFoundError`: Если файл не найден.
- `Exception`: В случае возникновения других ошибок во время обработки.

**Пример использования**

```python
from ai.prompts.developer.code_assistant import CodeAssistant

assistant = CodeAssistant(role='code_checker', lang='ru', model=['gemini'])
result = assistant.process_files(files=['file1.py', 'file2.py'], options={})
print(result)
```
```