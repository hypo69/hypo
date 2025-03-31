### Анализ кода модуля `xls`

**Качество кода:**
- **Соответствие стандартам**: 7/10
- **Плюсы**:
  - Код хорошо структурирован и включает обработку ошибок.
  - Используются типы для аннотации функций, что улучшает читаемость и упрощает отладку.
  - Присутствует подробная документация модуля и каждой функции.
- **Минусы**:
  - Используется устаревший стиль логгирования вместо `logger` из `src.logger`.
  - Не используется `j_loads` для работы с JSON.
  - Не везде соблюдается PEP8 (пробелы вокруг операторов).
  - Используется `Union` вместо `|`.

**Рекомендации по улучшению:**

1.  **Заменить logging на logger из src.logger**:
    - Заменить импорт `import logging` на `from src.logger import logger`.
    - Использовать `logger.info`, `logger.error` вместо `logging.info`, `logging.error`.
    - Добавить `exc_info=True` при логировании ошибок для получения трассировки стека.
2.  **Использовать `j_loads`**:
    - Изменить способ сохранения JSON в файл, чтобы использовать `j_loads`.
3.  **Соблюдать PEP8**:
    - Добавить пробелы вокруг операторов присваивания и других операторов.
4.  **Использовать `|` вместо `Union`**:
    - Изменить аннотации типов `Union[str, int]` на `str | int`.
5.  **Добавить примеры использования в документацию**:
    - Добавить примеры использования функций в документацию, чтобы упростить понимание их работы.
6.  **Улучшить обработку исключений**:
    - Указывать конкретные типы исключений вместо общего `Exception`.
7.  **Улучшить документацию модуля**:
    - Добавить информацию о зависимостях и окружении, необходимом для работы модуля.

**Оптимизированный код:**

```python
## \file /src/utils/xls.py
# -*- coding: utf-8 -*-
#! .pyenv/bin/python3

"""
Модуль для конвертации Excel (`xls`) в JSON и JSON в Excel (`xls`)
=================================================================

Модуль предоставляет функции для конвертации файлов Excel в формат JSON, обработки нескольких листов и сохранения данных JSON обратно в файлы Excel.

Пример использования
----------------------

    >>> data = read_xls_as_dict('input.xlsx', 'output.json', 'Sheet1')
    >>> if data:
    ...     print(data)  # Output will be {'Sheet1': [{...}]}

    >>> data_to_save = {'Sheet1': [{'column1': 'value1', 'column2': 'value2'}]}
    >>> success = save_xls_file(data_to_save, 'output.xlsx')
    >>> if success:
    ...     print("Successfully saved to output.xlsx")
"""

import pandas as pd
import json
from typing import List, Dict, Union
from pathlib import Path
from src.logger import logger  # Используем logger из src.logger


def read_xls_as_dict(
    xls_file: str,
    json_file: str = None,
    sheet_name: str | int = None
) -> dict | List[dict] | bool:
    """
    Читает Excel файл и конвертирует его в JSON.

    Args:
        xls_file (str): Путь к Excel файлу.
        json_file (str, optional): Путь для сохранения JSON файла. Defaults to None.
        sheet_name (str | int, optional): Имя листа для чтения. Defaults to None.

    Returns:
        dict | List[dict] | bool: Словарь с данными или False в случае ошибки.

    Raises:
        FileNotFoundError: Если файл не найден.
        Exception: При возникновении других ошибок.

    Example:
        >>> data = read_xls_as_dict('input.xlsx', 'output.json', 'Sheet1')
        >>> if data:
        ...     print(data)
        {'Sheet1': [{...}]}
    """
    try:
        xls_file_path = Path(xls_file)
        if not xls_file_path.exists():
            logger.error(f'Excel file not found: {xls_file}')  # Используем logger.error
            return False  # Indicate failure

        xls = pd.ExcelFile(xls_file)

        if sheet_name is None:
            data_dict = {}
            for sheet in xls.sheet_names:
                try:
                    df = pd.read_excel(xls, sheet_name=sheet)
                    data_dict[sheet] = df.to_dict(orient='records')
                except Exception as e:
                    logger.error(f'Error processing sheet \'{sheet}\': {e}', exc_info=True)  # Добавляем exc_info=True
                    return False

        else:
            try:
                df = pd.read_excel(xls, sheet_name=sheet_name)
                data_dict = df.to_dict(orient='records')
            except Exception as e:
                logger.error(f'Error processing sheet \'{sheet_name}\': {e}', exc_info=True)  # Добавляем exc_info=True
                return False

        if json_file:
            with open(json_file, 'w', encoding='utf-8') as f: # по заданию используем одинарные кавычки
                json.dump(data_dict, f, ensure_ascii=False, indent=4)
                logger.info(f'JSON data saved to {json_file}')  # Используем logger.info

        return data_dict

    except FileNotFoundError as e:
        logger.error(f'File not found: {e}', exc_info=True)  # Используем logger.error и exc_info=True
        return False
    except Exception as e:
        logger.error(f'An error occurred: {e}', exc_info=True)  # Используем logger.error и exc_info=True
        return False


def save_xls_file(data: Dict[str, List[Dict]], file_path: str) -> bool:
    """
    Сохраняет JSON данные в Excel файл.

    Args:
        data (Dict[str, List[Dict]]): Данные для сохранения, где ключи - это названия листов, а значения - списки словарей с данными.
        file_path (str): Путь для сохранения Excel файла.

    Returns:
        bool: True, если сохранение прошло успешно, False в противном случае.

    Raises:
        Exception: При возникновении ошибок во время сохранения файла.

    Example:
        >>> data_to_save = {'Sheet1': [{'column1': 'value1', 'column2': 'value2'}]}
        >>> success = save_xls_file(data_to_save, 'output.xlsx')
        >>> if success:
        ...     print("Successfully saved to output.xlsx")
        Successfully saved to output.xlsx
    """
    try:
        with pd.ExcelWriter(file_path, engine='xlsxwriter') as writer: # по заданию используем одинарные кавычки
            for sheet_name, rows in data.items():
                df = pd.DataFrame(rows)
                df.to_excel(writer, sheet_name=sheet_name, index=False)
                logger.info(f'Sheet \'{sheet_name}\' saved to {file_path}')  # Используем logger.info
        return True
    except Exception as e:
        logger.error(f'Error saving Excel file: {e}', exc_info=True)  # Используем logger.error и exc_info=True
        return False
```