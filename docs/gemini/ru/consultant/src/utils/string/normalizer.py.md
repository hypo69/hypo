# Анализ кода модуля `normalizer.py`

**Качество кода**
    
    - **Соответствие требованиям по оформлению кода:** 8/10
   
    -  **Плюсы**
        *   Код содержит docstring для всех функций, что соответствует стандартам оформления документации.
        *   Используются `logger.error` и `logger.debug` для логирования ошибок и отладочной информации.
        *   Есть  обработка исключений для предотвращения сбоев программы.
        *   Присутствует подробное документирование параметров и возвращаемых значений функций.
        *   Большинство функций возвращают исходное значение при ошибке, что соответствует принципам обработки ошибок.
        *   Код хорошо структурирован и разделен на отдельные функции.
        *   Используются проверки типов входных данных.

    -  **Минусы**
        *   Некоторые комментарии `#` не соответствуют стандарту reStructuredText (RST).
        *   В некоторых местах используются `try-except` блоки без необходимости, можно упростить, используя `logger.error`.
        *   Некоторые docstring требуют уточнения.
        *   В `remove_special_characters` есть дефолтный параметр `chars`, который не документирован в docstring.
        *   Отсутствует обработка None в  `remove_special_characters`.
    
**Рекомендации по улучшению**
1.  **Документация в стиле RST**: Переписать все комментарии, используя RST, включая docstring и комментарии в коде.
2.  **Обработка ошибок**:  Удалить избыточные try-except блоки и использовать `logger.error` для логирования ошибок.
3.  **Уточнение документации**: Уточнить  docstring для функций, в которых есть неточности или отсутствие описания.
4.  **Обработка None**: Добавить обработку None в `remove_special_characters`.
5.  **Стиль кода**: Привести весь код к единому стилю, особенно в части кавычек (использовать одинарные).
6.  **Удалить не используемый импорт:**  Удалить не используемый импорт  `html`

**Оптимизированный код**
```python
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe
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
from datetime import datetime
from decimal import Decimal, InvalidOperation
from typing import Any, List, Union
from src.logger.logger import logger



def normalize_boolean(input_data: Any) -> bool:
    """
    Преобразует входные данные в булево значение.

    :param input_data: Данные, которые могут быть преобразованы в булево значение (например, bool, строка, целое число).
    :type input_data: Any
    :return: Булево представление входных данных.
    :rtype: bool
    
    :Example:
    
    >>> normalize_boolean('yes')
    True
    
    """
    original_input = input_data # Сохраняет исходное значение
    if isinstance(input_data, bool):
        return input_data

    try:
        input_str = str(input_data).strip().lower()
        if input_str in {'true', '1', 'yes', 'y', 'on', True, 1}:
            return True
        if input_str in {'false', '0', 'no', 'n', 'off', False, 0}:
            return False
    except Exception as ex:
        logger.error(f'Ошибка в normalize_boolean: {ex}')

    logger.debug(f'Неожиданное значение для преобразования в bool: {input_data}')
    return original_input # Возвращает исходное значение

def normalize_string(input_data: str | list) -> str:
    """
    Нормализует строку или список строк.

    :param input_data: Входные данные, строка или список строк.
    :type input_data: str | list
    :return: Очищенная и нормализованная строка в кодировке UTF-8.
    :rtype: str
    :raises TypeError: Если `input_data` не является строкой или списком.
    
    :Example:
    
    >>> normalize_string(['Hello', '  World!  '])
    'Hello World!'
    
    """
    if not input_data:
        return ''

    original_input = input_data # Сохраняет исходное значение. В случае ошибки парсинга строки вернется это значение

    if not isinstance(input_data, (str, list)):
        raise TypeError('Данные должны быть строкой или списком строк.')

    if isinstance(input_data, list):
        input_data = ' '.join(map(str, input_data))

    try:
        cleaned_str = remove_html_tags(input_data)
        cleaned_str = remove_line_breaks(cleaned_str)
        cleaned_str = remove_special_characters(cleaned_str)
        normalized_str = ' '.join(cleaned_str.split())
        return normalized_str.strip().encode('utf-8').decode('utf-8')
    except Exception as ex:
        logger.error(f'Ошибка в normalize_string: {ex}')
        return str(original_input).encode('utf-8').decode('utf-8')

def normalize_int(input_data: Union[str, int, float, Decimal]) -> int:
    """
    Преобразует входные данные в целое число.

    :param input_data: Входные данные, которые могут быть числом или строковым представлением числа.
    :type input_data: str | int | float | Decimal
    :return: Целочисленное представление входных данных.
    :rtype: int
    
    :Example:
    
    >>> normalize_int('42')
    42
    
    """
    original_input = input_data # Сохраняет исходное значение
    try:
        if isinstance(input_data, Decimal):
            return int(input_data)
        return int(float(input_data))
    except (ValueError, TypeError, InvalidOperation) as ex:
        logger.error(f'Ошибка в normalize_int: {ex}')
        return original_input # Возвращает исходное значение

def normalize_float(value: Any) -> float | None:
    """
    Безопасно преобразует входные значения в float или список float.

    :param value: Входное значение для преобразования. Может быть единичным значением (число или строка) или итерируемым (список/кортеж).
    :type value: Any
    :return: Значение float, список float или None, если преобразование не удалось.
    :rtype: float | List[float] | None
    
    :Example:
    
    >>> normalize_float("3.14")
    3.14
    >>> normalize_float([1, '2.5', 3])
    [1.0, 2.5, 3.0]
    
    """
    original_value = value # Сохраняет исходное значение
    if not value:
        return 0
    if isinstance(value, (list, tuple)):
         # Код преобразовывает каждый элемент в float и возвращает список, если элемент None, пропускаем
        return [v for v in (normalize_float(v) for v in value) if v is not None]
    try:
        return float(value)
    except (ValueError, TypeError):
        logger.warning(f"Невозможно преобразовать '{value}' в float.")
        return original_value # Возвращает исходное значение

def normalize_sql_date(input_data: str) -> str:
    """
    Нормализует данные в формат SQL даты (YYYY-MM-DD).

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
    original_input = input_data # Сохраняет исходное значение
    try:
         # Проверка и преобразование строки в формат даты
        if isinstance(input_data, str):
            # Попытка распарсить дату из строки
            for date_format in ['%Y-%m-%d', '%m/%d/%Y', '%d/%m/%Y']:
                try:
                     # Код преобразовывает дату в объект datetime
                    normalized_date = datetime.strptime(input_data, date_format).date()
                    return normalized_date.isoformat() # Возвращаем дату в формате 'YYYY-MM-DD'
                except ValueError:
                    continue
        # Если входные данные уже объект datetime
        if isinstance(input_data, datetime):
            return input_data.date().isoformat()
    except Exception as ex:
        logger.error(f'Ошибка в normalize_sql_date: {ex}')

    logger.debug(f'Не удалось преобразовать в SQL дату: {input_data}')
    return original_input # Возвращает исходное значение

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
        logger.error(f"Error simplifying the string: {ex}")
        return input_str

def remove_line_breaks(input_str: str) -> str:
    """
    Удаляет переносы строк из входной строки.

    :param input_str: Входная строка.
    :type input_str: str
    :return: Строка без переносов строк.
    :rtype: str
    """
    return input_str.replace('\n', ' ').replace('\r', ' ').strip()

def remove_html_tags(input_html: str) -> str:
    """
    Удаляет HTML-теги из входной строки.

    :param input_html: Входная HTML строка.
    :type input_html: str
    :return: Строка без HTML-тегов.
    :rtype: str
    """
    return re.sub(r'<.*?>', '', input_html).strip()

def remove_special_characters(input_str: str | list, chars: list[str] = None) -> str | list:
    """
    Удаляет указанные специальные символы из строки или списка строк.

    :param input_str: Входная строка или список строк.
    :type input_str: str | list
    :param chars: Список символов для удаления. По умолчанию None, что удаляет только #.
    :type chars: list[str], optional
    :return: Обработанная строка или список с удаленными символами.
    :rtype: str | list
    """
    if input_str is None: # Проверка на None
        return ''
    if chars is None:
        chars = ['#']  # Список символов для удаления по умолчанию

    pattern = '[' + re.escape(''.join(chars)) + ']'

    if isinstance(input_str, list):
         # Код удаляет специальные символы из каждой строки списка
        return [re.sub(pattern, '', s) for s in input_str]
    return re.sub(pattern, '', input_str) # Удаляет специальные символы из строки

def normalize_sku(input_str: str) -> str:
    """
    Нормализует артикул, удаляя определенные ивритские ключевые слова и любые не буквенно-цифровые символы.

    :param input_str: Входная строка, содержащая артикул.
    :type input_str: str
    :return: Нормализованная строка артикула.
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
        logger.error(f"Error normalizing SKU: {ex}")
        return input_str # Возвращает исходное значение при ошибке
```