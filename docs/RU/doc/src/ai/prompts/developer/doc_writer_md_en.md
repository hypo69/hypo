# Модуль: Помощник по программированию

Этот модуль содержит класс `CodeAssistant`, который используется для взаимодействия с различными моделями ИИ, такими как Google Gemini и OpenAI, для задач обработки кода.

## Примеры использования

Пример использования класса `CodeAssistant`:

```python
assistant = CodeAssistant(role='code_checker', lang='ru', model=['gemini'])
assistant.process_files()
```

## Платформы
Поддерживаются платформы, на которых работают модели ИИ, используемые `CodeAssistant`.

## Краткое описание
Модуль предоставляет инструменты для анализа и генерации документации кода с помощью моделей ИИ.

## Классы

### `CodeAssistant`

**Описание**: Класс `CodeAssistant` предназначен для взаимодействия с моделями ИИ, такими как Google Gemini, для обработки кода.

**Атрибуты**:
- `role`: Роль помощника (например, 'code_checker').
- `lang`: Язык, который будет использовать помощник (например, 'ru').
- `model`: Список используемых моделей ИИ (например, `['gemini']`).


**Методы**:

#### `process_files`

**Описание**: Метод для обработки файлов кода.

**Параметры**:
- `files` (list): Список файлов для обработки.
- `options` (dict, optional): Дополнительные параметры для настройки обработки. По умолчанию `None`.

**Возвращает**:
- `list`: Список результатов обработки, содержащий проанализированные данные.

**Вызывает исключения**:
- `FileNotFoundError`: Если файл не найден.
- `TypeError`: Если введены некорректные типы данных.


```
```
```python
# Обработка файлов кода
def process_files(self, files: list, options: dict = None) -> list:
    """
    Args:
        files (list): Список файлов для обработки.
        options (dict, optional): Дополнительные параметры для настройки обработки. По умолчанию None.

    Returns:
        list: Список результатов обработки, содержащий проанализированные данные.

    Raises:
        FileNotFoundError: Если файл не найден.
        TypeError: Если введены некорректные типы данных.
    """
    try:
        results = []
        for file in files:
            try:
                with open(file, 'r') as f:
                    code = f.read()
                    # Вызов модели ИИ для обработки кода
                    result = self.process_code(code)
                    results.append(result)
            except FileNotFoundError as ex:
                print(f"Ошибка: Файл {file} не найден.")
                # Обработка исключения и продолжение обработки
                results.append({"error": f"Файл {file} не найден."})

            except Exception as ex:
                print(f"Ошибка: Произошла ошибка при обработке файла {file}. {ex}")
                results.append({"error": f"Ошибка при обработке: {ex}"})
        return results
    except Exception as ex:
        raise TypeError(f"Неверный тип данных: {ex}") from ex
```
```
```
```
```
```
```
```
```
```


```