# Анализ кода модуля `normalizer`

## Качество кода:

- **Соответствие стандартам**: 7
- **Плюсы**:
    - Код достаточно хорошо структурирован и разбит на отдельные функции, что облегчает его понимание и поддержку.
    - Используются аннотации типов, что повышает читаемость и позволяет обнаруживать ошибки на ранних стадиях разработки.
    - Присутствует базовая документация для каждой функции с примерами.
    - Код обрабатывает различные типы данных, включая строки, числа, даты и логические значения.
    - Для обработки ошибок используется `logger.error`, что позволяет отслеживать возникающие проблемы.
- **Минусы**:
    - Некоторые функции имеют чрезмерно усложненную логику обработки ошибок.
    - Не все функции документированы в формате RST.
    - Используются как двойные, так и одинарные кавычки, что не соответствует стандартам.
    - Некоторые комментарии являются неинформативными.
    - Присутствует избыточное использование `try-except`.
    - В некоторых случаях возвращается исходное значение при ошибке, что может скрывать проблемы.

## Рекомендации по улучшению:

- Привести все строки в коде к единому стандарту, используя только одинарные кавычки (`'`). Двойные кавычки (`"`) использовать только для вывода в консоль.
- Переписать документацию к функциям в формате RST, как показано в примере, включая более подробные описания параметров, возвращаемых значений и возможных исключений.
- Избегать  `try-except` в случаях, когда можно обработать ошибку более явно, например, через `if` или проверку типов.
- Логировать ошибки через `logger.error` с указанием контекста и типа ошибки.
- Убрать избыточные комментарии, такие как `# Сохраняется исходное значение`, так как их смысл понятен из кода.
- Использовать `from src.logger.logger import logger` для импорта логгера.
- Стандартизировать обработку ошибок, например, возвращать `None` или бросать исключение, вместо возврата исходного значения.
- В функции `remove_special_characters` добавить проверку на пустой список `chars`.
- В `normalize_string` добавить проверку на None, а не только на пустую строку.
- В `normalize_float`  возвращать `None` в случае ошибки, если необходимо.
- Избавиться от дублирования кода, когда результат кодируется и декодируется в utf-8.
- Улучшить документацию функции `simplify_string` с учетом RST стандарта.
- Добавить проверки типов для `input_data` в `normalize_sql_date`.
- В `normalize_sku` убрать try-except и предоставить более понятную обработку ошибок.

## Оптимизированный код:

```python
"""
Модуль для нормализации строк и числовых данных
=========================================================================================

Этот модуль предоставляет функции для нормализации строк, булевых значений, целых и чисел с плавающей точкой.
Он также содержит вспомогательные методы для обработки текста, включая удаление HTML-тегов и специальных символов.

Пример использования
--------------------

.. code-block:: python

    from src.utils.string.normalizer import normalize_string, normalize_boolean

    normalized_str = normalize_string(' Пример строки <b>с HTML</b> ')
    normalized_bool = normalize_boolean('yes')
"""

import re
import html
from datetime import datetime
from decimal import Decimal, InvalidOperation
from typing import Any, List, Union
from src.logger.logger import logger


def normalize_boolean(input_data: Any) -> bool | None:
    """
    Нормализует входные данные в булево значение.

    :param input_data: Данные, которые могут быть представлены в виде булевого значения (например, bool, строка, целое число).
    :type input_data: Any
    :return: Булево представление входных данных. Возвращает None, если преобразование невозможно.
    :rtype: bool | None

    :Example:
        >>> normalize_boolean('yes')
        True
        >>> normalize_boolean('no')
        False
        >>> normalize_boolean(1)
        True
        >>> normalize_boolean(0)
        False
        >>> normalize_boolean(None)
        None
    """
    if isinstance(input_data, bool):
        return input_data

    try:
        input_str = str(input_data).strip().lower()
        if input_str in {'true', '1', 'yes', 'y', 'on'}:
            return True
        if input_str in {'false', '0', 'no', 'n', 'off'}:
            return False
    except Exception as ex:
        logger.error(f'Ошибка в normalize_boolean: {ex}')
        return None

    logger.debug(f'Неожиданное значение для преобразования в bool: {input_data}')
    return None


def normalize_string(input_data: str | list | None) -> str:
    """
    Нормализует строку или список строк.

    :param input_data: Строка или список строк для нормализации.
    :type input_data: str | list | None
    :return: Очищенная и нормализованная строка в кодировке UTF-8. Возвращает пустую строку если input_data None.
    :rtype: str
    :raises TypeError: Если `input_data` не является строкой, списком или None.

    :Example:
        >>> normalize_string(['Hello', '  World!  '])
        'Hello World!'
        >>> normalize_string('  Hello  World!  ')
        'Hello World!'
        >>> normalize_string(None)
        ''
    """
    if input_data is None:
        return ''

    if not isinstance(input_data, (str, list)):
        raise TypeError('Данные должны быть строкой или списком строк.')

    if isinstance(input_data, list):
        input_data = ' '.join(map(str, input_data))

    try:
        cleaned_str = remove_html_tags(input_data)
        cleaned_str = remove_line_breaks(cleaned_str)
        cleaned_str = remove_special_characters(cleaned_str)
        normalized_str = ' '.join(cleaned_str.split())
        return normalized_str.strip()
    except Exception as ex:
        logger.error(f'Ошибка в normalize_string: {ex}')
        return str(input_data)


def normalize_int(input_data: Union[str, int, float, Decimal]) -> int | None:
    """
    Нормализует данные в целое число.

    :param input_data: Данные, которые могут быть представлены в виде числа или его строкового представления.
    :type input_data: str | int | float | Decimal
    :return: Целочисленное представление входных данных. Возвращает None, если преобразование невозможно.
    :rtype: int | None

    :Example:
        >>> normalize_int('42')
        42
        >>> normalize_int(42.5)
        42
        >>> normalize_int(Decimal('42'))
        42
        >>> normalize_int('abc')
        None
    """
    try:
        if isinstance(input_data, Decimal):
            return int(input_data)
        return int(float(input_data))
    except (ValueError, TypeError, InvalidOperation) as ex:
        logger.error(f'Ошибка в normalize_int: {ex}')
        return None


def normalize_float(value: Any) -> float | list[float] | None:
    """
    Безопасно преобразует входные значения в float или список float.

    :param value: Входное значение для преобразования. Может быть одиночным значением (число или строка) или итерируемым объектом (список/кортеж).
    :type value: Any
    :return: Значение float, список значений float или None, если преобразование не удалось.
    :rtype: float | list[float] | None

    :Example:
        >>> normalize_float("3.14")
        3.14
        >>> normalize_float([1, '2.5', 3])
        [1.0, 2.5, 3.0]
        >>> normalize_float('abc')
        None
    """
    if not value:
        return 0
    if isinstance(value, (list, tuple)):
        return [v for v in (normalize_float(v) for v in value) if v is not None]

    try:
        return float(value)
    except (ValueError, TypeError):
        logger.warning(f'Невозможно преобразовать \'{value}\' в float.')
        return None


def normalize_sql_date(input_data: str | datetime) -> str | None:
    """
    Нормализует данные в формат SQL даты (YYYY-MM-DD).

    :param input_data: Данные, которые могут представлять дату (например, строка, объект datetime).
    :type input_data: str | datetime
    :return: Нормализованная дата в формате SQL (YYYY-MM-DD) или None, если преобразование не удалось.
    :rtype: str | None

    :Example:
        >>> normalize_sql_date('2024-12-06')
        '2024-12-06'
        >>> normalize_sql_date('12/06/2024')
        '2024-12-06'
        >>> normalize_sql_date(datetime(2024, 12, 6))
        '2024-12-06'
    """
    if not isinstance(input_data, (str, datetime)):
        logger.error(f'Неверный тип данных для преобразования в SQL дату: {type(input_data)}')
        return None

    try:
        if isinstance(input_data, str):
            for date_format in ['%Y-%m-%d', '%m/%d/%Y', '%d/%m/%Y']:
                try:
                    normalized_date = datetime.strptime(input_data, date_format).date()
                    return normalized_date.isoformat()
                except ValueError:
                    continue
        if isinstance(input_data, datetime):
            return input_data.date().isoformat()
    except Exception as ex:
        logger.error(f'Ошибка в normalize_sql_date: {ex}')
        return None

    logger.debug(f'Не удалось преобразовать в SQL дату: {input_data}')
    return None


def simplify_string(input_str: str) -> str:
    """
     Упрощает входную строку, оставляя только буквы и цифры, и заменяет пробелы на подчеркивания.

    :param input_str: Строка для упрощения.
    :type input_str: str
    :return: Упрощенная строка.
    :rtype: str

    :Example:
         >>> example_str = "It's a test string with 'single quotes', numbers 123 and symbols!"
         >>> simplify_string(example_str)
         'Its_a_test_string_with_single_quotes_numbers_123_and_symbols'
     """
    try:
        cleaned_str = re.sub(r'[^a-zA-Z0-9\s]', '', input_str)
        cleaned_str = cleaned_str.replace(' ', '_')
        cleaned_str = re.sub(r'_+', '_', cleaned_str)
        return cleaned_str
    except Exception as ex:
        logger.error(f'Ошибка при упрощении строки: {ex}')
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
    Удаляет HTML теги из входной строки.

    :param input_html: Входная HTML строка.
    :type input_html: str
    :return: Строка без HTML тегов.
    :rtype: str
    """
    return re.sub(r'<.*?>', '', input_html).strip()


def remove_special_characters(input_str: str | list, chars: list[str] = None) -> str | list:
    """
    Удаляет указанные специальные символы из строки или списка строк.

    :param input_str: Входная строка или список строк.
    :type input_str: str | list
    :param chars: Список символов для удаления. Если None, используется список по умолчанию ['#'].
    :type chars: list[str], optional
    :return: Обработанная строка или список строк с удаленными символами.
    :rtype: str | list
    """
    if chars is None:
        chars = ['#']
    if not chars:
        return input_str

    pattern = '[' + re.escape(''.join(chars)) + ']'
    if isinstance(input_str, list):
        return [re.sub(pattern, '', s) for s in input_str]
    return re.sub(pattern, '', input_str)


def normalize_sku(input_str: str) -> str | None:
    """
    Нормализует артикул (SKU), удаляя специфические ивритские ключевые слова и любые не буквенно-цифровые символы.

    :param input_str: Входная строка, содержащая артикул.
    :type input_str: str
    :return: Нормализованная строка артикула или None если произошла ошибка.
    :rtype: str | None

    :Example:
        >>> normalize_sku("מקט: 303235")
        '303235'
        >>> normalize_sku("מק''ט: 12345")
        '12345'
    """
    if not isinstance(input_str, str):
        logger.error(f'Неверный тип данных для нормализации SKU: {type(input_str)}')
        return None

    try:
        input_str = re.sub(r'מקט|מק\'\'ט', '', input_str, flags=re.IGNORECASE)
        normalized_sku = re.sub(r'\W+', '', input_str)
        return normalized_sku
    except Exception as ex:
        logger.error(f'Ошибка нормализации SKU: {ex}')
        return None
```