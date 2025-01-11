# Анализ кода модуля `normalizer`

**Качество кода**
9
-  Плюсы
    - Хорошая и полная документация в формате RST.
    - Код хорошо структурирован и понятен.
    - Присутствуют примеры использования функций.
    - Все функции имеют четкое описание и примеры.
    - Используется `logger` для логирования ошибок и предупреждений.
-  Минусы
    - Не указаны импорты для `datetime`, `Decimal` и `re` хотя они используются в коде.
    -  Необходима проверка типов `input_data` в функциях.
    - В блоках кода отсутствует обработка исключений.
    - Не используется `j_loads` или `j_loads_ns` для загрузки json файлов (если это требуется в данном модуле)

**Рекомендации по улучшению**
1. Добавить импорты для `datetime`, `Decimal` и `re`.
2. Добавить проверку типов `input_data` во всех функциях для предотвращения ошибок.
3. Реализовать обработку исключений в функциях `normalize_int`, `normalize_float` и `remove_special_characters`.
4. Избегать избыточного использования стандартных блоков `try-except`, предпочитая обработку ошибок с помощью `logger.error`.
5. Использовать `j_loads` или `j_loads_ns` из `src.utils.jjson` для загрузки json (если это необходимо в данном модуле).
6.  Добавить более подробные описания типов для параметров и возвращаемых значений в docstrings.
7. Улучшить обработку ошибок при преобразовании данных.

**Оптимизированный код**
```python
"""
Модуль для нормализации различных типов данных.
=========================================================================================

Модуль `normalizer` предоставляет функциональность для нормализации различных типов данных,
включая строки, булевы значения, целые числа и числа с плавающей запятой.
Он также включает вспомогательные функции для обработки текста.

Пример использования
--------------------

Пример использования функций `normalizer`:

.. code-block:: python

    from src.utils.string.normalizer import normalize_string, normalize_boolean, normalize_int, normalize_float, normalize_sql_date

    # Нормализация строки
    clean_str = normalize_string(['<h1>Header</h1>', '  text with spaces  '])
    print(clean_str)

    # Нормализация булевого значения
    is_active = normalize_boolean('Yes')
    print(is_active)

    # Нормализация целого числа
    integer_value = normalize_int('42')
    print(integer_value)

    # Нормализация числа с плавающей запятой
    float_value = normalize_float('3.14159')
    print(float_value)

    # Нормализация SQL даты
    sql_date = normalize_sql_date('2024-12-06')
    print(sql_date)
"""
import re
from datetime import datetime
from decimal import Decimal
from typing import Any, List, Union
from src.logger.logger import logger


def normalize_boolean(input_data: Any) -> bool:
    """Преобразует входное значение в булево значение.

    :param input_data: Данные, которые могут представлять булево значение (строка, число, булев тип).
    :type input_data: Any
    :return: Преобразованное булево значение.
    :rtype: bool

    Пример:
        >>> normalize_boolean('yes')
        True
        >>> normalize_boolean(0)
        False
    """
    if isinstance(input_data, bool):
        return input_data
    if isinstance(input_data, str):
        return input_data.lower() in ['true', 'yes', '1']
    if isinstance(input_data, int):
        return bool(input_data)
    return False


def normalize_string(input_data: Union[str, List[str]]) -> str:
    """Преобразует строку или список строк в нормализованную строку.

    Удаляет лишние пробелы, HTML теги и специальные символы.

    :param input_data: Строка или список строк для нормализации.
    :type input_data: Union[str, List[str]]
    :return: Очищенная строка в кодировке UTF-8.
    :rtype: str

    Пример:
        >>> normalize_string(['  Example string  ', '<b>with HTML</b>'])
        'Example string with HTML'
    """
    if isinstance(input_data, list):
        input_data = ' '.join(map(str, input_data))

    if not isinstance(input_data, str):
         logger.error(f'Неверный тип данных {input_data=}, ожидалась строка или список строк')
         return ''

    input_data = remove_html_tags(input_data)
    input_data = remove_line_breaks(input_data)
    input_data = remove_special_characters(input_data)
    return " ".join(input_data.split()).strip()


def normalize_int(input_data: Union[str, int, float, Decimal]) -> int:
    """Преобразует входное значение в целое число.

    :param input_data: Число или его строковое представление.
    :type input_data: Union[str, int, float, Decimal]
    :return: Преобразованное целое число.
    :rtype: int

    Пример:
        >>> normalize_int('42')
        42
        >>> normalize_int(3.14)
        3
    """
    try:
        if isinstance(input_data, str):
            return int(float(input_data))
        if isinstance(input_data, (int, float, Decimal)):
            return int(input_data)
        logger.error(f'Неверный тип данных {input_data=}, ожидалась строка, int, float или Decimal')
        return 0
    except (ValueError, TypeError) as ex:
        logger.error(f'Ошибка приведения к int {input_data=}', ex)
        return 0



def normalize_float(value: Any) -> Union[float, List[float], None]:
    """Преобразует входное значение в число с плавающей запятой.

    :param value: Число, строка или список чисел для преобразования.
    :type value: Any
    :return: Число с плавающей запятой, список чисел с плавающей запятой или `None` в случае ошибки.
    :rtype: Union[float, List[float], None]

    Пример:
        >>> normalize_float('3.14')
        3.14
        >>> normalize_float([1, '2.5', 3])
        [1.0, 2.5, 3.0]
    """
    try:
        if isinstance(value, str):
            return float(value)
        if isinstance(value, (int, float)):
            return float(value)
        if isinstance(value, list):
            return [float(normalize_float(item)) for item in value]
        logger.error(f'Неверный тип данных {value=}, ожидалась строка, int, float или list')
        return None
    except (ValueError, TypeError) as ex:
        logger.error(f'Ошибка приведения к float {value=}', ex)
        return None


def remove_line_breaks(input_str: str) -> str:
    """Удаляет символы новой строки из строки.

    :param input_str: Входная строка.
    :type input_str: str
    :return: Строка без символов новой строки.
    :rtype: str

    Пример:
        >>> remove_line_breaks('String\\nwith line breaks\\r')
        'String with line breaks'
    """
    return input_str.replace('\n', '').replace('\r', '')


def remove_html_tags(input_html: str) -> str:
    """Удаляет HTML теги из строки.

    :param input_html: Входная строка с HTML тегами.
    :type input_html: str
    :return: Строка без HTML тегов.
    :rtype: str

    Пример:
        >>> remove_html_tags('<p>Example text</p>')
        'Example text'
    """
    clean_text = re.compile('<.*?>')
    return re.sub(clean_text, '', input_html)


def remove_special_characters(input_str: Union[str, List[str]]) -> Union[str, List[str]]:
    """Удаляет специальные символы из строки или списка строк.

    :param input_str: Строка или список строк.
    :type input_str: Union[str, List[str]]
    :return: Строка или список строк без специальных символов.
    :rtype: Union[str, List[str]]

    Пример:
        >>> remove_special_characters('Hello@World!')
        'HelloWorld'
    """
    try:
        if isinstance(input_str, str):
            return re.sub(r'[^a-zA-Zа-яА-Я0-9\s]', '', input_str)
        if isinstance(input_str, list):
            return [re.sub(r'[^a-zA-Zа-яА-Я0-9\s]', '', item) for item in input_str]
        logger.error(f'Неверный тип данных {input_str=}, ожидалась строка или список строк')
        return ''
    except Exception as ex:
        logger.error(f'Ошибка при удалении спец символов {input_str=}', ex)
        return ''



def normalize_sql_date(input_data: Union[str, datetime]) -> str:
    """Преобразует строку или объект `datetime` в стандартный формат SQL даты (`YYYY-MM-DD`).

    :param input_data: Строка или объект `datetime`, представляющий дату.
    :type input_data: Union[str, datetime]
    :return: Нормализованная дата в формате строки `YYYY-MM-DD`.
    :rtype: str

    Пример:
        >>> normalize_sql_date('2024-12-06')
        '2024-12-06'
        >>> normalize_sql_date(datetime(2024, 12, 6))
        '2024-12-06'
    """
    if isinstance(input_data, str):
        try:
            date_obj = datetime.strptime(input_data, '%Y-%m-%d')
            return date_obj.strftime('%Y-%m-%d')
        except ValueError as ex:
           logger.error(f'Неверный формат даты {input_data=}', ex)
           return ''
    elif isinstance(input_data, datetime):
        return input_data.strftime('%Y-%m-%d')
    else:
        logger.error(f'Неверный тип данных {input_data=}, ожидалась строка или datetime')
        return ''
```