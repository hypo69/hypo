# Модуль: Programming Assistant

Этот модуль содержит класс `CodeAssistant`, который используется для взаимодействия с различными моделями ИИ, такими как Google Gemini и OpenAI, для задач обработки кода.

## Пример использования

Пример использования класса `CodeAssistant`:

```python
assistant = CodeAssistant(role='code_checker', lang='ru', model=['gemini'])
assistant.process_files()
```

## Платформы
Поддерживается выполнение на платформах с установленным Python.

## Краткое описание
Модуль предназначен для обработки файлов кода с помощью ИИ-моделей.  Он предоставляет методы для анализа кода, генерации документации и других задач.

## Атрибуты
- `role`: Роль помощника (например, 'code_checker').
- `lang`: Язык, который будет использовать помощник (например, 'ru').
- `model`: Список используемых ИИ-моделей (например, `['gemini']`).

## Методы
### `process_files`

Метод для обработки файлов кода.

**Описание**: Анализирует переданные файлы кода с помощью выбранных моделей ИИ и выполняет заданные действия.

**Параметры**:
- `files` (list[str]): Список путей к файлам кода.
- `options` (dict, optional): Дополнительные параметры для настройки обработки. По умолчанию `{}`.

**Возвращает**:
- `list[dict]`: Список словарей, содержащих результаты анализа для каждого файла.  Возвращает `None` в случае ошибки.

**Вызывает исключения**:
- `FileNotFoundError`: Если файл с заданным путем не найден.
- `ValueError`: Если передан некорректный тип данных или значение параметров.


```python
# Пример использования
assistant = CodeAssistant(role='code_checker', lang='ru', model=['gemini'])
try:
    result = assistant.process_files(files=['file1.py', 'file2.py'], options={'output_format': 'markdown'})
    print(result)
except FileNotFoundError as ex:
    print(f"Ошибка: {ex}")
except ValueError as ex:
    print(f"Ошибка: {ex}")
```

```python
# Пример обработки результата
for file_result in result:
    print(f"Результат для файла {file_result['filename']}:")
    print(file_result['analysis'])

```


```python
# Пример с дополнительными опциями
result = assistant.process_files(files=['file1.py', 'file2.py'], options={'max_tokens': 1000, 'temperature': 0.5})
```
```python
class CodeAssistant:
    def __init__(self, role: str, lang: str, model: list) -> None:
        """
        Args:
            role (str): Роль помощника (например, 'code_checker').
            lang (str): Язык, который будет использовать помощник (например, 'ru').
            model (list): Список используемых ИИ-моделей (например, ['gemini']).
        """
        self.role = role
        self.lang = lang
        self.model = model

    def process_files(self, files: list[str], options: dict = {}) -> list[dict] | None:
        """
        Метод для обработки файлов кода.

        Args:
            files (list[str]): Список путей к файлам кода.
            options (dict, optional): Дополнительные параметры для настройки обработки. По умолчанию {}.

        Returns:
            list[dict]: Список словарей, содержащих результаты анализа для каждого файла. Возвращает None в случае ошибки.

        Raises:
            FileNotFoundError: Если файл с заданным путем не найден.
            ValueError: Если передан некорректный тип данных или значение параметров.
        """
        # Логика обработки файлов здесь
        pass
```