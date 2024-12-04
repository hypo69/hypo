# Модуль: Ассистент программиста

Этот модуль содержит класс `CodeAssistant`, который используется для взаимодействия с различными AI-моделями (такими как Google Gemini и OpenAI) для выполнения задач по обработке кода.  Модуль предназначен для документирования кода в формате RST и обеспечивает поддержку различных языков.

## Пример использования

```python
assistant = CodeAssistant(role='code_checker', lang='ru', model=['gemini'])
result = assistant.process_files(files=['file1.py', 'file2.py'], options={})
print(result)
```

## Поддерживаемые платформы
- Python 3.9+


# Класс: CodeAssistant

Класс `CodeAssistant` используется для взаимодействия с различными AI-моделями и предоставляет методы для анализа и генерации документации для кода.

## Атрибуты

- `role`: Роль ассистента (например, 'code_checker').
- `lang`: Язык, который будет использовать ассистент (например, 'ru').
- `model`: Список используемых AI-моделей (например, ['gemini']).

## Методы

### `process_files`

Метод для обработки списка файлов кода.

#### Параметры

- `files`: Список путей к файлам для обработки.  Ожидается список строк.
- `options`: Словарь с дополнительными параметрами для настройки обработки.  По умолчанию пустое значение.

#### Возвращаемое значение

- Возвращает список словарей, где каждый словарь содержит информацию об обработанном файле. Возвращает `None`, если произошла ошибка или файлы не были найдены.

#### Пример использования

```python
assistant = CodeAssistant(role='code_checker', lang='ru', model=['gemini'])
result = assistant.process_files(files=['file1.py', 'file2.py'], options={})
if result:
    for file_data in result:
        print(f"Обработанный файл: {file_data['filename']}, результат: {file_data['result']}")
else:
    print("Ошибка при обработке файлов.")
```

#### Возможные исключения

- `FileNotFoundError`: Если один или несколько файлов из списка `files` не найдены.
- `TypeError`: Если в качестве входных данных передан неверный тип данных.
- `ValueError`: Если параметры options содержат неверные значения.
- `Exception`:  Для других необработанных ошибок.

```
```

```python
#Пример реализации (заглушка)
import os
class CodeAssistant:
    def __init__(self, role, lang, model):
        self.role = role
        self.lang = lang
        self.model = model

    def process_files(self, files, options=None):
        if options is None:
            options = {}
        results = []
        for file in files:
            try:
                with open(file, 'r') as f:
                    code = f.read()
                    # Симулируем обработку с помощью AI модели
                    processed_data = {"filename": file, "result": f"Обработан файл {file}"}
                    results.append(processed_data)
            except FileNotFoundError:
                print(f"Файл {file} не найден.")
                return None
            except Exception as e:
                print(f"Ошибка при обработке файла {file}: {e}")
                return None
        return results
```
```
```
```python
# Пример pytest теста для функции process_files
import pytest

# Файлы в тестовой папке (для имитации)
test_file_1 = "test_file1.txt"
test_file_2 = "test_file2.txt"

def create_test_file(filename, content):
    with open(filename, "w") as f:
        f.write(content)

@pytest.fixture
def assistant_instance():
    return CodeAssistant(role='code_checker', lang='ru', model=['gemini'])

def test_process_files_valid_input(assistant_instance):
    create_test_file(test_file_1, "test content")
    create_test_file(test_file_2, "test content 2")
    result = assistant_instance.process_files([test_file_1, test_file_2])
    assert result is not None
    assert len(result) == 2

def test_process_files_file_not_found(assistant_instance):
    result = assistant_instance.process_files([test_file_1])
    assert result is None


```
```
```

```