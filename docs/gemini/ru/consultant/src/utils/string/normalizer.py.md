# Анализ кода модуля `normalizer.py`

**Качество кода**
8
-  Плюсы
    - Код содержит docstring для каждой функции, что соответствует стандартам PEP 257.
    - Используется `logger` для логирования ошибок и отладочной информации, что помогает в траблшутинге.
    - Функции выполняют свою задачу по нормализации данных (строк, чисел, дат).
    - Есть обработки исключений для предотвращения падения программы.
-  Минусы
    - В некоторых местах есть избыточное использование `try-except` блоков, например, в `normalize_boolean`.
    - В функции `normalize_float` обработка `ValueError` и `TypeError` выполняется одинаково.
    - Функция `simplify_string` имеет устаревший формат документирования (`@param`, `@return`, `@code`, `@endcode`).
    - Не все функции используют явное указание типа `str`.

**Рекомендации по улучшению**

1.  **Упростить `try-except` блоки**: В функциях `normalize_boolean` и `normalize_int` можно убрать обработку исключений, заменив их на проверку типов и вызов `logger.error`.
2.  **Изменить форматирование документации**: Заменить `@param`, `@return`, `@code`, `@endcode` на RST в функции `simplify_string`.
3.  **Явное указание типа**: Добавить явное указание типа `str` в тех местах, где это необходимо.
4.  **Улучшить обработку ошибок**: В функции `normalize_float` можно разделить обработку `ValueError` и `TypeError` для более точного логирования.
5.  **Переписать комментарии в reStructuredText**: В соответствии с инструкцией все комментарии должны быть в формате reStructuredText.
6.  **Использовать более точные исключения**: Вместо `Exception` использовать более точные типы исключений.

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
import html
from datetime import datetime
from decimal import Decimal, InvalidOperation
from typing import Any, List, Union
from src.logger.logger import logger

MODE = 'dev'


def normalize_boolean(input_data: Any) -> bool:
    """
    Преобразует входные данные в логическое значение.

    :param input_data: Данные, которые могут быть представлены как логическое значение (например, bool, строка, целое число).
    :type input_data: Any
    :return: Логическое представление входных данных.
    :rtype: bool

    :Example:
        >>> normalize_boolean('yes')
        True
    """
    original_input = input_data
    if isinstance(input_data, bool):
        return input_data

    try:
        input_str = str(input_data).strip().lower()
        if input_str in {'true', '1', 'yes', 'y', 'on', 'true', 1}:
            return True
        if input_str in {'false', '0', 'no', 'n', 'off', 'false', 0}:
            return False
    except Exception as ex: # Код обрабатывает любое исключение
        logger.error(f'Ошибка при преобразовании в bool: {ex}')

    logger.debug(f'Неожиданное значение для преобразования в bool: {input_data}')
    return original_input


def normalize_string(input_data: Union[str, list]) -> str:
    """
    Нормализует строку или список строк.

    :param input_data: Строка или список строк для нормализации.
    :type input_data: Union[str, list]
    :return: Очищенная и нормализованная строка в формате UTF-8.
    :rtype: str
    :raises TypeError: Если `input_data` не является строкой или списком.

    :Example:
        >>> normalize_string(['Hello', '  World!  '])
        'Hello World!'
    """
    if not input_data:
        return ''
    original_input = input_data # Сохраняется исходное значение. В случае ошибки парсинга строки вернется это значение

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
    except Exception as ex: # Код обрабатывает любое исключение
        logger.error(f'Ошибка при нормализации строки: {ex}')
        return str(original_input).encode('utf-8').decode('utf-8')


def normalize_int(input_data: Union[str, int, float, Decimal]) -> int:
    """
    Преобразует входные данные в целое число.

    :param input_data: Данные для преобразования (строка, целое число, число с плавающей точкой, Decimal).
    :type input_data: Union[str, int, float, Decimal]
    :return: Целочисленное представление входных данных.
    :rtype: int

    :Example:
        >>> normalize_int('42')
        42
    """
    original_input = input_data # Сохраняется исходное значение
    try:
        if isinstance(input_data, Decimal):
            return int(input_data)
        return int(float(input_data))
    except (ValueError, TypeError, InvalidOperation) as ex: # Код обрабатывает исключения при преобразовании в int
        logger.error(f'Ошибка при преобразовании в int: {ex}')
        return original_input # Возвращается исходное значение


def normalize_float(value: Any) -> Union[float, None, list[float]]:
    """
    Безопасно преобразует входные данные в число с плавающей точкой или список чисел с плавающей точкой.

    :param value: Входное значение для преобразования. Может быть числом, строкой или итерируемым объектом (список/кортеж).
    :type value: Any
    :return: Число с плавающей точкой, список чисел с плавающей точкой или None, если преобразование не удалось.
    :rtype: Union[float, None, list[float]]

    :Example:
        >>> normalize_float("3.14")
        3.14
        >>> normalize_float([1, '2.5', 3])
        [1.0, 2.5, 3.0]
    """
    original_value = value # Сохраняется исходное значение
    if not value:
        return 0
    if isinstance(value, (list, tuple)):
        return [v for v in (normalize_float(v) for v in value) if v is not None]
    try:
        return float(value)
    except ValueError as ex: # Код обрабатывает ошибку преобразования в float
        logger.warning(f"Невозможно преобразовать '{value}' в float: {ex}")
        return original_value # Возвращается исходное значение
    except TypeError as ex: # Код обрабатывает ошибку типа данных при преобразовании в float
        logger.warning(f"Невозможно преобразовать '{value}' в float: {ex}")
        return original_value # Возвращается исходное значение

def normalize_sql_date(input_data: str) -> str:
    """
    Преобразует входные данные в формат SQL даты (YYYY-MM-DD).

    :param input_data: Данные, представляющие дату (например, строка, объект datetime).
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
                    normalized_date = datetime.strptime(input_data, date_format).date()
                    return normalized_date.isoformat() # Возвращаем дату в формате 'YYYY-MM-DD'
                except ValueError: # Код обрабатывает исключение неверного формата даты
                    continue
        # Если входные данные уже объект datetime
        if isinstance(input_data, datetime):
            return input_data.date().isoformat()

    except Exception as ex: # Код обрабатывает любое исключение
        logger.error(f'Ошибка при преобразовании даты в SQL формат: {ex}')

    logger.debug(f'Не удалось преобразовать в SQL дату: {input_data}')
    return original_input


def simplify_string(input_str: str) -> str:
    """
    Упрощает входную строку, оставляя только буквы, цифры и заменяя пробелы на подчеркивания.

    :param input_str: Строка для упрощения.
    :type input_str: str
    :return: Упрощенная строка.
    :rtype: str
    :Example:
        >>> example_str = "It's a test string with 'single quotes', numbers 123 and symbols!"
        >>> simplify_string(example_str)
        "Its_a_test_string_with_single_quotes_numbers_123_and_symbols"
    """
    try:
        # Удаление всех символов, кроме букв, цифр и пробелов
        cleaned_str = re.sub(r'[^a-zA-Z0-9\s]', '', input_str)
        # Замена пробелов на подчеркивания
        cleaned_str = cleaned_str.replace(' ', '_')
        # Удаление повторяющихся подчеркиваний
        cleaned_str = re.sub(r'_+', '_', cleaned_str)
        return cleaned_str
    except Exception as ex: # Код обрабатывает любое исключение
        logger.error("Ошибка при упрощении строки", ex)
        return input_str


def remove_line_breaks(input_str: str) -> str:
    """
    Удаляет переводы строк из входной строки.

    :param input_str: Входная строка.
    :type input_str: str
    :return: Строка без переводов строк.
    :rtype: str
    """
    return input_str.replace('\n', ' ').replace('\r', ' ').strip()


def remove_html_tags(input_html: str) -> str:
    """
    Удаляет HTML-теги из входной строки.

    :param input_html: Входная HTML-строка.
    :type input_html: str
    :return: Строка без HTML-тегов.
    :rtype: str
    """
    return re.sub(r'<.*?>', '', input_html).strip()


def remove_special_characters(input_str: Union[str, list], chars: list[str] = None) -> Union[str, list]:
    """
    Удаляет указанные специальные символы из строки или списка строк.

    :param input_str: Входная строка или список строк.
    :type input_str: Union[str, list]
    :param chars: Список символов для удаления. По умолчанию None.
    :type chars: list[str], optional
    :return: Обработанная строка или список с удаленными символами.
    :rtype: Union[str, list]
    """
    if chars is None:
        chars = ['#']  # Default list of characters to remove

    pattern = '[' + re.escape(''.join(chars)) + ']'

    if isinstance(input_str, list):
        return [re.sub(pattern, '', s) for s in input_str]
    return re.sub(pattern, '', input_str)
```