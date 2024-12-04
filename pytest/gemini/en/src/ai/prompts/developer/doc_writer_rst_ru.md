```python
import pytest


class CodeAssistant:
    """
    Класс для работы с ассистентом программиста, использующим модели ИИ.

    :param role: Роль ассистента (например, 'code_checker').
    :type role: str
    :param lang: Язык, на котором будет работать ассистент (например, 'ru').
    :type lang: str
    :param model: Список используемых моделей ИИ (например, ['gemini']).
    :type model: list
    """

    def __init__(self, role, lang, model):
        """
        Инициализация ассистента с указанием роли, языка и моделей ИИ.
        """
        self.role = role
        self.lang = lang
        self.model = model

    def process_files(self, files, options=None):
        """
        Метод для обработки файлов с кодом.

        :param files: Список путей к файлам для обработки.
        :type files: list
        :param options: Словарь с дополнительными параметрами.
        :type options: dict
        :raises FileNotFoundError: Если файл не найден.
        :return: Список результатов обработки файлов. Возвращает пустой список, если входные данные пустые или некорректные.
        :rtype: list
        """
        if not files:
            return []
        results = []
        for file in files:
            try:
                # Пример симуляции обработки файла.  В реальном коде здесь должен быть вызов API или другой механизм обработки.
                result = f"Обработка файла {file} завершена."
                results.append(result)
            except FileNotFoundError as e:
                raise FileNotFoundError(f"Файл {file} не найден.") from e
        return results


# Тестовые функции для класса CodeAssistant
def test_process_files_valid_input():
    """Проверяет корректную обработку списка файлов."""
    assistant = CodeAssistant(role='code_checker', lang='ru', model=['gemini'])
    files = ['file1.py', 'file2.py']
    results = assistant.process_files(files)
    assert len(results) == 2
    for result in results:
        assert isinstance(result, str)
  
def test_process_files_empty_input():
    """Проверяет работу с пустым списком файлов."""
    assistant = CodeAssistant(role='code_checker', lang='ru', model=['gemini'])
    files = []
    results = assistant.process_files(files)
    assert results == []


def test_process_files_file_not_found():
    """Проверяет обработку случая, когда файл не найден."""
    assistant = CodeAssistant(role='code_checker', lang='ru', model=['gemini'])
    files = ['nonexistent_file.py']
    with pytest.raises(FileNotFoundError, match="Файл nonexistent_file.py не найден."):
        assistant.process_files(files)
```