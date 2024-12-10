# Модуль для работы с ассистентом программиста

## Обзор

Этот модуль предоставляет базовый класс `CodeAssistant` для работы с различными моделями ИИ (например, Google Gemini и OpenAI) для задач обработки кода.  Он предназначен для упрощения интеграции таких моделей в приложения.

## Пример использования

```python
from typing import List, Dict, Optional

class CodeAssistant:
    """
    Класс для работы с ассистентом программиста.

    Args:
        role (str): Роль ассистента (например, 'code_checker').
        lang (str): Язык, на котором будет работать ассистент (например, 'ru').
        model (List[str]): Список используемых моделей ИИ (например, ['gemini']).
    """
    def __init__(self, role: str, lang: str, model: List[str]):
        self.role = role
        self.lang = lang
        self.model = model


    def process_files(self, files: List[str], options: Optional[Dict] = None) -> List[Dict]:
        """
        Обрабатывает список файлов с кодом.

        Args:
            files (List[str]): Список путей к файлам.
            options (Optional[Dict], optional): Дополнительные параметры. Defaults to None.

        Returns:
            List[Dict]: Список словарей с результатами обработки. Возвращает пустой список, если вход пустой. Возможна обработка исключений.

        Raises:
            FileNotFoundError: Возникает, если один или несколько файлов не найдены.
            TypeError: Возникает, если тип аргумента `files` не соответствует ожиданиям.
        """
        if not files:
            return []
        if not isinstance(files, list):
            raise TypeError("Аргумент 'files' должен быть списком.")
        
        results = []
        for file in files:
            try:
                # Симулируем обработку файла
                result = {"file": file, "processed_data": f"Обработан файл {file}"}
                results.append(result)
            except FileNotFoundError as ex:
                raise FileNotFoundError(f"Файл {file} не найден") from ex


        return results


# Пример использования
assistant = CodeAssistant(role='code_checker', lang='ru', model=['gemini'])
try:
    results = assistant.process_files(files=['file1.py', 'file2.py'])
    for result in results:
        print(result)

    results_empty = assistant.process_files(files=[])
    print(results_empty)

    results_wrong_type = assistant.process_files(files="not a list")
except FileNotFoundError as ex:
    print(f"Ошибка: {ex}")
except TypeError as ex:
   print(f"Ошибка: {ex}")


```

## Классы

### `CodeAssistant`

**Описание**: Класс для работы с ассистентом программиста.

**Атрибуты**:
- `role` (str): Роль ассистента (например, 'code_checker').
- `lang` (str): Язык, на котором будет работать ассистент (например, 'ru').
- `model` (List[str]): Список используемых моделей ИИ (например, ['gemini']).


**Методы**:
- `process_files`: Метод для обработки файлов с кодом.  Подробное описание см. в разделе "Методы".


## Функции


## Методы

### `process_files`

**Описание**: Метод для обработки списка файлов с кодом.

**Параметры**:
- `files` (List[str]): Список путей к файлам.
- `options` (Optional[Dict], optional): Дополнительные параметры. По умолчанию `None`.

**Возвращает**:
- `List[Dict]`: Список словарей с результатами обработки. Возвращает пустой список, если вход пустой.

**Возможные исключения**:
- `FileNotFoundError`: Если один или несколько файлов не найдены.
- `TypeError`: Если тип аргумента `files` не соответствует ожиданиям.


**Примеры использования (см. пример в Обзоре).**


```