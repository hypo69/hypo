# Модуль: Programming Assistant

Этот модуль содержит класс `CodeAssistant`, предназначенный для взаимодействия с различными моделями ИИ, такими как Google Gemini и OpenAI, для обработки кода.

## Пример использования

Пример использования класса `CodeAssistant`:

```python
assistant = CodeAssistant(role='code_checker', lang='ru', model=['gemini'])
assistant.process_files()
```

## Функции

### `process_files`

**Описание**: Метод для обработки файлов кода.

**Параметры**:

- `files` (list): Список файлов для обработки.
- `options` (dict, optional): Дополнительные параметры для настройки обработки. По умолчанию `None`.

**Возвращает**:

- `list`: Список результатов обработки в виде анализированных данных.

**Вызывает исключения**:

- `FileNotFoundError`: Если файл не найден.
- `ValueError`: Если передан некорректный тип данных.
- `Exception`: Общее исключение, если произошла ошибка.


```