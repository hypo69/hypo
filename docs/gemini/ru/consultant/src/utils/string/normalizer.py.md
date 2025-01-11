# Анализ кода модуля normalizer

**Качество кода**
7
- Плюсы
    - Код хорошо структурирован и разбит на отдельные функции для нормализации различных типов данных.
    - Используется `logger` для записи ошибок и отладочной информации.
    - Присутствуют примеры использования для большинства функций.
    -  Есть подробные docstring, описывающие назначение, аргументы и возвращаемые значения функций.
- Минусы
    -  Не все функции имеют docstring в формате RST.
    -  В некоторых функциях логика обработки ошибок могла бы быть более последовательной (например, возвращение исходного значения при ошибке).
    -   Не везде используется `from src.logger.logger import logger` для импорта logger.
    -   Есть `try-except` без `...` для остановки.

**Рекомендации по улучшению**

1.  **Импорты:** Добавьте `from src.logger.logger import logger` для единообразия.
2.  **Форматирование**: Привести все docstring к стандарту RST.
3.  **Обработка ошибок**: Упростить `try-except` блоки, где это возможно, используя `logger.error` с последующим возвратом исходного значения.
4.  **Комментарии:** Добавить комментарии, описывающие логику работы отдельных блоков кода.
5.  **Унификация**: Привести к одному виду обработку ошибок, где необходимо возвращать исходное значение, в случае возникновения ошибки.
6. **Удаление HTML тегов** : Улучшить удаление HTML тегов, добавив обработку экранированных символов.

**Оптимизированный код**

```python
# -*- coding: utf-8 -*-

#! venv/bin/python/python3.12

"""
Модуль для нормализации строк и числовых данных
=========================================================================================

Этот модуль предоставляет функции для нормализации строк, булевых значений, целых и чисел с плавающей точкой.
Он также содержит вспомогательные методы для обработки текста, включая удаление HTML-тегов и специальных символов.

Пример использования
--------------------

.. code-block:: python

    from src.utils.string.normalizer import normalize_string, normalize_boolean

    normalized_str = normalize_string(" Пример строки <b>с HTML</b> ")
    normalized_bool = normalize_boolean("yes")
"""

import re
import html
from datetime import datetime
from decimal import Decimal, InvalidOperation
from typing import Any, List, Union
# Импорт logger из src.logger.logger
from src.logger.logger import logger


def normalize_boolean(input_data: Any) -> bool:
    """
    Нормализует входные данные в логическое значение.

    :param input_data: Данные, которые могут представлять логическое значение (например, bool, string, integer).
    :type input_data: Any
    :return: Логическое представление входных данных.
    :rtype: bool

    :Example:
        >>> normalize_boolean('yes')
        True
    """
    original_input = input_data  # Сохраняется исходное значение
    if isinstance(input_data, bool):
        return input_data

    try:
        # Преобразует входные данные в строку, удаляет пробелы и приводит к нижнему регистру
        input_str = str(input_data).strip().lower()
        # Проверяет, является ли строка одним из истинных значений
        if input_str in {'true', '1', 'yes', 'y', 'on', True, 1}:
            return True
        # Проверяет, является ли строка одним из ложных значений
        if input_str in {'false', '0', 'no', 'n', 'off', False, 0}:
            return False
    except Exception as ex:
        logger.error('Ошибка в normalize_boolean: ', ex)
        # ...
    # Логирование ошибки и возврат исходного значения, если преобразование не удалось
    logger.debug(f'Неожиданное значение для преобразования в bool: {input_data}')
    return original_input  # Возвращается исходное значение


def normalize_string(input_data: str | list) -> str:
    """
    Нормализует строку или список строк.

    :param input_data: Входные данные, которые могут быть строкой или списком строк.
    :type input_data: str | list
    :return: Очищенная и нормализованная строка в кодировке UTF-8.
    :rtype: str
    :raises TypeError: Если `input_data` не является строкой или списком.
    :Example:
        >>> normalize_string(['Hello', '  World!  '])
        'Hello World!'
    """
    # Проверка, что входные данные не пусты
    if not input_data:
        return ''

    original_input = input_data  # Сохраняется исходное значение. В случае ошибки парсинга строки вернется это значение

    # Проверка типа входных данных
    if not isinstance(input_data, (str, list)):
        raise TypeError('Данные должны быть строкой или списком строк.')

    # Преобразует список строк в одну строку
    if isinstance(input_data, list):
        input_data = ' '.join(map(str, input_data))
    
    try:
        # Удаляет HTML теги, переносы строк и специальные символы
        cleaned_str = remove_html_tags(input_data)
        cleaned_str = remove_line_breaks(cleaned_str)
        cleaned_str = remove_special_characters(cleaned_str)
        # Удаляет лишние пробелы
        normalized_str = ' '.join(cleaned_str.split())

        # Возвращает нормализованную строку в кодировке UTF-8
        return normalized_str.strip().encode('utf-8').decode('utf-8')
    except Exception as ex:
        logger.error('Ошибка в normalize_string: ', ex)
        # Возвращает исходное значение, если преобразование не удалось
        return str(original_input).encode('utf-8').decode('utf-8')


def normalize_int(input_data: Union[str, int, float, Decimal]) -> int:
    """
    Нормализует входные данные в целое число.

    :param input_data: Входные данные, которые могут быть числом или его строковым представлением.
    :type input_data: str | int | float | Decimal
    :return: Целое представление входных данных.
    :rtype: int
    :Example:
        >>> normalize_int('42')
        42
    """
    original_input = input_data  # Сохраняется исходное значение
    try:
         # Проверка типа данных и преобразование в целое число
        if isinstance(input_data, Decimal):
            return int(input_data)
        return int(float(input_data))
    except (ValueError, TypeError, InvalidOperation) as ex:
         # Логирование ошибки и возврат исходного значения, если преобразование не удалось
        logger.error('Ошибка в normalize_int: ', ex)
        return original_input  # Возвращается исходное значение


def normalize_float(value: Any) -> float | None:
    """
    Безопасно преобразует входные значения в float или список float.

    :param value: Входное значение для преобразования. Может быть числом, строкой или итерируемым объектом (list/tuple).
    :type value: Any
    :return: Значение float, список float или None, если преобразование не удалось.
    :rtype: float | List[float] | None

    :Example:
        >>> normalize_float("3.14")
        3.14
        >>> normalize_float([1, '2.5', 3])
        [1.0, 2.5, 3.0]
    """
    original_value = value  # Сохраняется исходное значение
    if not value:
        return 0
    # Рекурсивно обрабатывает список или кортеж
    if isinstance(value, (list, tuple)):
        return [v for v in (normalize_float(v) for v in value) if v is not None]
    try:
        # Пытается преобразовать значение в float
        return float(value)
    except (ValueError, TypeError):
        # Логирование предупреждения и возврат исходного значения, если преобразование не удалось
        logger.warning(f"Невозможно преобразовать '{value}' в float.")
        return original_value  # Возвращается исходное значение


def normalize_sql_date(input_data: str) -> str:
    """
    Нормализует входные данные в формат даты SQL (YYYY-MM-DD).

    :param input_data: Данные, которые могут представлять дату (например, строка, объект datetime).
    :type input_data: str
    :return: Нормализованная дата в формате SQL (YYYY-MM-DD) или исходное значение, если преобразование не удалось.
    :rtype: str

    :Example:
        >>> normalize_sql_date('2024-12-06')
        '2024-12-06'
        >>> normalize_sql_date('12/06/2024')
        '2024-12-06'
    """
    original_input = input_data  # Сохраняется исходное значение

    try:
        # Проверка и преобразование строки в формат даты
        if isinstance(input_data, str):
            # Попытка распарсить дату из строки
            for date_format in ['%Y-%m-%d', '%m/%d/%Y', '%d/%m/%Y']:
                try:
                    # Преобразует строку в объект datetime
                    normalized_date = datetime.strptime(input_data, date_format).date()
                    # Возвращает дату в формате 'YYYY-MM-DD'
                    return normalized_date.isoformat()
                except ValueError:
                    continue
        # Если входные данные уже объект datetime
        if isinstance(input_data, datetime):
             # Возвращает дату в формате 'YYYY-MM-DD'
            return input_data.date().isoformat()

    except Exception as ex:
        logger.error('Ошибка в normalize_sql_date: ', ex)
        # ...

    # Логирование ошибки и возврат исходного значения, если преобразование не удалось
    logger.debug(f'Не удалось преобразовать в SQL дату: {input_data}')
    return original_input  # Возвращается исходное значение

def simplify_string(input_str: str) -> str:
    """
    Упрощает входную строку, оставляя только буквы, цифры и заменяя пробелы на подчеркивания.

    :param input_str: Строка для упрощения.
    :type input_str: str
    :return: Упрощенная строка.
    :rtype: str
        
    :Example:
        >>> example_str = "It's a test string with 'single quotes', numbers 123 and symbols!"
        >>> simplified_str = simplify_string(example_str)
        >>> print(simplified_str)
        Its_a_test_string_with_single_quotes_numbers_123_and_symbols
    """
    try:
        # Удаляет все символы, кроме букв, цифр и пробелов
        cleaned_str = re.sub(r'[^a-zA-Z0-9\s]', '', input_str)
        # Заменяет пробелы на подчеркивания
        cleaned_str = cleaned_str.replace(' ', '_')
        # Удаляет последовательные подчеркивания
        cleaned_str = re.sub(r'_+', '_', cleaned_str)
        return cleaned_str
    except Exception as ex:
        logger.error("Error simplifying the string", ex)
        # Возвращает исходное значение, если преобразование не удалось
        return input_str


def remove_line_breaks(input_str: str) -> str:
    """
    Удаляет переносы строк из входной строки.

    :param input_str: Входная строка.
    :type input_str: str
    :return: Строка без переносов строк.
    :rtype: str
    """
    # Заменяет переносы строк и возвраты каретки на пробелы
    return input_str.replace('\n', ' ').replace('\r', ' ').strip()


def remove_html_tags(input_html: str) -> str:
    """
    Удаляет HTML теги из входной строки.

    :param input_html: Входная HTML строка.
    :type input_html: str
    :return: Строка без HTML тегов.
    :rtype: str
    """
    # Удаляет HTML теги, а также обрабатывает html сущности
    return re.sub(r'<.*?>', '', html.unescape(input_html)).strip()


def remove_special_characters(input_str: str | list, chars: list[str] = None) -> str | list:
    """
    Удаляет указанные специальные символы из строки или списка строк.

    :param input_str: Входная строка или список строк.
    :type input_str: str | list
    :param chars: Список символов для удаления. По умолчанию None.
    :type chars: list[str], optional
    :return: Обработанная строка или список строк с удаленными символами.
    :rtype: str | list
    """
    if chars is None:
        chars = ['#']  # Default list of characters to remove
    
    # Формируем шаблон регулярного выражения для удаления символов
    pattern = '[' + re.escape(''.join(chars)) + ']'

    # Если входные данные - список, обрабатываем каждый элемент
    if isinstance(input_str, list):
        return [re.sub(pattern, '', s) for s in input_str]
     # Если входные данные - строка, применяем регулярное выражение
    return re.sub(pattern, '', input_str)

def normalize_sku(input_str: str) -> str:
    """
    Нормализует SKU, удаляя специфические ивритские ключевые слова и любые не буквенно-цифровые символы.

    :param input_str: Входная строка, содержащая SKU.
    :type input_str: str
    :return: Нормализованная строка SKU.
    :rtype: str
        
    :Example:
        >>> normalize_sku("מקט: 303235")
        '303235'
        >>> normalize_sku("מק''ט: 12345")
        '12345'
    """
    try:
        # Удаляет ивритские ключевые слова
        input_str = re.sub(r'מקט|מק\'\'ט', '', input_str, flags=re.IGNORECASE)
        # Удаляет не буквенно-цифровые символы
        normalized_sku = re.sub(r'\W+', '', input_str)
        return normalized_sku
    except Exception as ex:
        # Логирование ошибки и возврат исходного значения, если преобразование не удалось
        logger.error(f"Error normalizing SKU: {ex}")
        return input_str  # Return the original input in case of error
```