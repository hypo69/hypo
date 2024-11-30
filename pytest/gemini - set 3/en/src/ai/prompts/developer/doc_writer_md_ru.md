```python
import pytest

class CodeAssistant:
    """
    Класс CodeAssistant для взаимодействия с AI-моделями для обработки кода.

    Атрибуты:
    - role: Роль ассистента.
    - lang: Язык работы.
    - model: Список используемых AI-моделей.

    Методы:
    - process_files: Обрабатывает список файлов кода.
    """

    def __init__(self, role, lang, model):
        """
        Инициализирует объект CodeAssistant.

        Параметры:
        - role: Роль ассистента.
        - lang: Язык работы.
        - model: Список используемых AI-моделей.
        """
        self.role = role
        self.lang = lang
        self.model = model

    def process_files(self, files, options={}):
        """
        Обрабатывает список файлов.

        Параметры:
        - files: Список путей к файлам.
        - options: Словарь с дополнительными параметрами.

        Возвращаемое значение:
        - Список результатов обработки файлов. Возвращает пустой список, если файлы не переданы.
        Возможные исключения:
        - ValueError: Если тип данных files не список.
        """

        if not isinstance(files, list):
            raise ValueError("Files must be a list.")
        
        if not files:
            return []  # Возвращает пустой список, если files пустой

        results = []
        for file in files:
            try:
                # Здесь должна быть реализация обработки файла.
                # Замените это на вашу логику работы с файлами
                # Используя AI-модель.
                results.append(f"Processed file: {file}")
            except FileNotFoundError as e:
                print(f"Error processing {file}: {e}")
                # Обрабатываем исключение, чтобы не останавливать обработку остальных файлов.
                continue  # Пропускаем текущий файл и переходим к следующему.
            except Exception as e:
                print(f"An unexpected error occurred while processing {file}: {e}")
                return None  # Возвращаем None при непредвиденной ошибке.


        return results
```

```python
import pytest

def test_process_files_valid_input():
    """Тест для process_files с валидными данными."""
    assistant = CodeAssistant(role='code_checker', lang='ru', model=['gemini'])
    files = ['file1.py', 'file2.py']
    result = assistant.process_files(files)
    assert isinstance(result, list), "Result should be a list."
    assert len(result) == 2, "Length of the result list should be equal to the number of files."


def test_process_files_empty_input():
  """Тест для process_files с пустым списком файлов."""
  assistant = CodeAssistant(role='code_checker', lang='ru', model=['gemini'])
  files = []
  result = assistant.process_files(files)
  assert result == [], "Result should be an empty list for an empty input."


def test_process_files_invalid_input_type():
    """Тест для process_files с невалидным типом данных files."""
    assistant = CodeAssistant(role='code_checker', lang='ru', model=['gemini'])
    files = 'not_a_list'
    with pytest.raises(ValueError):
        assistant.process_files(files)



def test_process_files_file_not_found():
    """Тест для process_files с несуществующим файлом (исключение FileNotFoundError)."""
    assistant = CodeAssistant(role='code_checker', lang='ru', model=['gemini'])
    files = ['nonexistent_file.txt']
    result = assistant.process_files(files)
    assert result is not None, "Function should not return None in case of a single error."
```