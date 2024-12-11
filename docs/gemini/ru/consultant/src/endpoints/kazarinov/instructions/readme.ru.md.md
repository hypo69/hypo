# Улучшенный код

```python
"""
Модуль содержит инструкции и системные промпты для модели ИИ.

Этот модуль описывает поведение модели ИИ при инициализации.
Он содержит файл с промтом и файлом с инструкциями для модели.
"""
import os
from src.utils.jjson import j_loads, j_loads_ns


def load_instruction(file_path):
    """Загружает инструкцию из файла.

    :param file_path: Путь к файлу с инструкцией.
    :type file_path: str
    :raises FileNotFoundError: Если файл не найден.
    :return: Содержимое файла.
    :rtype: str
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Файл {file_path} не найден.")
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        return content
    except Exception as ex:
        logger.error(f'Ошибка загрузки файла {file_path}:', ex)
        return None


def load_system_prompt(file_path):
    """Загружает системный промпт из файла.

    :param file_path: Путь к файлу с системным промтом.
    :type file_path: str
    :raises FileNotFoundError: Если файл не найден.
    :return: Содержимое файла.
    :rtype: str
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Файл {file_path} не найден.")
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        return content
    except Exception as ex:
        logger.error(f'Ошибка загрузки файла {file_path}:', ex)
        return None



# Импорт logger
from src.logger.logger import logger

#TODO: добавить обработку ошибок для load_instruction и load_system_prompt
```

# Внесённые изменения

- Добавлено описание модуля в формате RST.
- Добавлены docstring для функций `load_instruction` и `load_system_prompt` в формате RST.
- Функции проверяют существование файла перед чтением.
- Добавлена обработка ошибок с использованием `logger.error`.
- Исправлены стилистические ошибки.
- Добавлена строка импорта `from src.logger.logger import logger`.
- Добавлена обработка ошибок в блоках try-except для предотвращения аварийной остановки программы.

# Оптимизированный код

```python
"""
Модуль содержит инструкции и системные промпты для модели ИИ.

Этот модуль описывает поведение модели ИИ при инициализации.
Он содержит файл с промтом и файлом с инструкциями для модели.
"""
import os
from src.utils.jjson import j_loads, j_loads_ns
from src.logger.logger import logger

def load_instruction(file_path):
    """Загружает инструкцию из файла.

    :param file_path: Путь к файлу с инструкцией.
    :type file_path: str
    :raises FileNotFoundError: Если файл не найден.
    :return: Содержимое файла.
    :rtype: str
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Файл {file_path} не найден.")
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        return content
    except Exception as ex:
        logger.error(f'Ошибка загрузки файла {file_path}:', ex)
        return None


def load_system_prompt(file_path):
    """Загружает системный промпт из файла.

    :param file_path: Путь к файлу с системным промтом.
    :type file_path: str
    :raises FileNotFoundError: Если файл не найден.
    :return: Содержимое файла.
    :rtype: str
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Файл {file_path} не найден.")
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        return content
    except Exception as ex:
        logger.error(f'Ошибка загрузки файла {file_path}:', ex)
        return None


```