# Модуль: Programming Assistant

Этот модуль содержит класс `CodeAssistant`, предназначенный для взаимодействия с различными моделями ИИ, такими как Google Gemini и OpenAI, для обработки задач, связанных с кодом. Модуль предоставляет методы для анализа кода и генерации документации.

## Примеры использования

Пример использования класса `CodeAssistant`:

```python
assistant = CodeAssistant(role='code_checker', lang='ru', model=['gemini'])
result = assistant.process_files(files=['file1.py', 'file2.py'], options={'verbose': True})
print(result)
```

## Поддерживаемые платформы

- Linux
- macOS
- Windows

## Краткое описание

Модуль `Programming Assistant` позволяет обрабатывать файлы кода, анализировать их структуру и генерировать документацию.


## Классы

### `CodeAssistant`

**Описание**:  Класс `CodeAssistant` взаимодействует с моделями ИИ для обработки файлов кода.

**Атрибуты**:
- `role`: Роль помощника (например, 'code_checker').
- `lang`: Язык, используемый помощником (например, 'ru').
- `model`: Список используемых моделей ИИ (например, `['gemini']`).


**Методы**:

#### `process_files`

**Описание**: Метод для обработки файлов кода.

**Параметры**:
- `files` (list): Список путей к файлам кода.
- `options` (dict, optional): Дополнительные параметры для настройки обработки. По умолчанию `{}`.

**Возвращает**:
- `list`: Список результатов обработки. Возвращает `None`, если произошла ошибка.


**Примеры использования**:

```python
assistant = CodeAssistant(role='code_checker', lang='ru', model=['gemini'])
result = assistant.process_files(files=['file1.py', 'file2.py'], options={'verbose': True})
if result:
  for item in result:
      print(item)
else:
  print("Ошибка при обработке файлов.")
```

**Возможные исключения**:
- `FileNotFoundError`: Если указанный файл не найден.
- `ValueError`: Если передан некорректный тип данных.
- `Exception`: В случае других непредвиденных ошибок.


```
```
```
```
```