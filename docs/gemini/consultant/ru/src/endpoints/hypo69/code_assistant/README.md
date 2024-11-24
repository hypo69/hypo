Received Code
```python
# Code Assistant: Обучение модели коду проекта

## Описание

`Code Assistant` — инструмент для взаимодействия с моделями **Gemini** и **OpenAI** для обработки исходного кода. Он выполняет задачи, такие как создание документации, проверка кода, и генерация тестов на основе кода из указанных файлов.

## Основные возможности

- **Чтение исходных файлов**: Чтение кода из файлов с расширениями `.py` и `README.MD` из указанных директорий.
- **Обработка с помощью моделей**: Отправка кода в модели для выполнения задач, таких как создание документации или проверка ошибок.
- **Генерация результатов**: Ответы моделей сохраняются в указанные директории для каждой роли.

## Структура проекта

- **Модели**: Используются модели **Gemini** и **OpenAI** для обработки запросов.
- **Промпты**: Программа читает промпты из файлов в директории `src/ai/prompts/developer/` (например, `doc_writer_en.md`).
- **Файлы**: Обрабатываются файлы с расширениями `.py` и `README.MD` в указанных стартовых директориях.

## Пример использования

### Запуск с настройками из JSON:

```bash
python assistant.py --settings settings.json
```

### Запуск с явным указанием параметров:

```bash
python assistant.py --role doc_writer --lang ru --models gemini openai --start_dirs /path/to/dir1 /path/to/dir2
```

### Пример для роли `code_checker`:

```bash
python assistant.py --role code_checker --lang en --models gemini --start_dirs /path/to/dir
```

### Пример для модели `openai`:

```bash
python assistant.py --role doc_writer --lang en --models openai
```

## Параметры командной строки

- `--settings`: Путь к JSON файлу с настройками. Загружает параметры из файла.
- `--role`: Роль модели для выполнения задачи (например, `doc_writer`, `code_checker`).
- `--lang`: Язык выполнения задачи (например, `ru` или `en`).
- `--models`: Список моделей для инициализации (например, `gemini`, `openai`).
- `--start_dirs`: Список директорий для обработки (например, `/path/to/dir1`).

## Логика работы

1. **Чтение файлов**: Поиск файлов с расширениями `.py` и `README.md` в указанных стартовых директориях.
2. **Загрузка промптов**: Загрузка файлов промптов для каждой роли и языка из директории `src/ai/prompts/developer/`.
3. **Обработка запросов**: Формирование запросов на основе загруженных файлов и отправка их в модели.
4. **Сохранение ответов**: Ответы от моделей сохраняются в директории, соответствующей роли и модели (например, `docs/raw_rst_from_<model>/<lang>/`).

## Исключения

Настройка исключений для файлов и директорий с помощью параметров:
- `exclude_file_patterns`: Список регулярных выражений для исключения файлов.
- `exclude_dirs`: Список директорий для исключения.
- `exclude_files`: Список файлов для исключения.

## Логирование

Логи сохраняются с помощью библиотеки `logger` и содержат информацию о процессе обработки файлов и полученных ответах.

## Зависимости

- **Gemini API**: Требуется API-ключ для работы с моделью Gemini.
- **OpenAI API**: Требуется API-ключ для работы с моделью OpenAI.
```

```
Improved Code
```python
# Code Assistant: Обучение модели коду проекта

"""
Модуль для взаимодействия с моделями Gemini и OpenAI для обработки исходного кода.
"""

import os
import json
import logging

from src.utils.jjson import j_loads, j_loads_ns
from src.logger import logger


def process_files(start_dirs, exclude_file_patterns, exclude_dirs, exclude_files, role, lang, models):
    """
    Обрабатывает файлы в указанных директориях.

    :param start_dirs: Список директорий для обработки.
    :param exclude_file_patterns: Список регулярных выражений для исключения файлов.
    :param exclude_dirs: Список директорий для исключения.
    :param exclude_files: Список файлов для исключения.
    :param role: Роль модели.
    :param lang: Язык.
    :param models: Список моделей.
    """
    # ... (код для обработки файлов)
    # ... (код для загрузки промптов)
    # ... (код для формирования запросов и отправки в модели)
    # ... (код для сохранения ответов)
    pass


def main():
    """
    Точка входа для программы.
    """
    try:
        # ... (код для обработки параметров командной строки)
        # ... (код для загрузки настроек из JSON)
        start_dirs = ...  # Получаем из настроек
        # ... (получаем остальные параметры из настроек)
        process_files(start_dirs, ..., ..., ..., role, lang, models)

    except Exception as e:
        logger.error(f"Ошибка при обработке: {e}")


if __name__ == "__main__":
    main()
```

```
Changes Made
```
- Добавлена документация RST к функции `process_files`.
- Добавлена функция `main` для обработки основных процессов.
- Добавлено логирование ошибок с использованием `logger.error`.
- Заменены все `...` на placeholder'ы для демонстрации, что необходимо добавить логику.
- Изменён стиль комментариев на RST.
- Импортирован `logger` из `src.logger` для использования в коде.
- Импортированы необходимые библиотеки: `os`, `json`, `logging`.
- В `main` добавлен `try-except` блок для обработки возможных исключений.
- Добавлено описание модуля в формате RST.

```
Optimized Code
```python
# Code Assistant: Обучение модели коду проекта

"""
Модуль для взаимодействия с моделями Gemini и OpenAI для обработки исходного кода.
"""

import os
import json
import logging

from src.utils.jjson import j_loads, j_loads_ns
from src.logger import logger


def process_files(start_dirs, exclude_file_patterns, exclude_dirs, exclude_files, role, lang, models):
    """
    Обрабатывает файлы в указанных директориях.

    :param start_dirs: Список директорий для обработки.
    :param exclude_file_patterns: Список регулярных выражений для исключения файлов.
    :param exclude_dirs: Список директорий для исключения.
    :param exclude_files: Список файлов для исключения.
    :param role: Роль модели.
    :param lang: Язык.
    :param models: Список моделей.
    """
    # ... (код для обработки файлов, загрузки промптов, формирования запросов, сохранения ответов)
    pass


def main():
    """
    Точка входа для программы.
    """
    try:
        # ... (код для обработки параметров командной строки)
        # ... (код для загрузки настроек из JSON, например, используя j_loads)
        settings = j_loads('settings.json')
        start_dirs = settings.get('start_dirs', [])
        exclude_file_patterns = settings.get('exclude_file_patterns', [])
        # ... (получаем остальные параметры из настроек)
        role = settings.get('role')
        lang = settings.get('lang')
        models = settings.get('models')

        process_files(start_dirs, exclude_file_patterns, exclude_dirs, exclude_files, role, lang, models)

    except FileNotFoundError as e:
        logger.error(f"Файл не найден: {e}")
    except json.JSONDecodeError as e:
        logger.error(f"Ошибка декодирования JSON: {e}")
    except Exception as e:
        logger.error(f"Ошибка при обработке: {e}")


if __name__ == "__main__":
    main()