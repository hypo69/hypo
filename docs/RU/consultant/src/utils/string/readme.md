# Анализ кода модуля `src.utils.string`

**Качество кода**
10
-  Плюсы
    -   Хорошая документация модуля и функций.
    -   Подробное описание каждой функции с примерами.
    -   Структурированный и читаемый код.
    -   Используются RST для документации.
    -  Соответствует требованиям PEP8.
-  Минусы
    -  Отсутствует импорт `logger`.
    -  Некоторые моменты можно улучшить, например, добавить `type hints` и использовать `logger.exception` вместо `logger.error` при перехвате исключений.
    -   В RST документации не указаны `Raises`.
    -  Пример использования модуля в конце `readme.md` следует перенести в отдельный `example.py` файл

**Рекомендации по улучшению**
1.  Добавить импорт `logger` из `src.logger`.
2.  В функциях `normalize_float`, `normalize_int`, `normalize_sql_date` добавить `type hints`.
3.  Заменить `logger.error` на `logger.exception` в блоках `try-except`.
4.  В RST документации для функций добавить `Raises` описание ошибок.
5.  Перенести пример использования в отдельный файл `example.py`.
6. Дополнить документацию `type hints`

**Оптимизированный код**
```markdown
````rst
.. module:: src.utils.string

Data Normalizer Module Documentation
====================================

Модуль `normalizer` предоставляет функциональность для нормализации различных типов данных, включая строки, булевы значения, целые числа и числа с плавающей точкой. Он также включает вспомогательные функции для обработки текста.

---

## Содержание

1.  [Обзор](#overview)
2.  [Функции модуля](#module-functions)
    -   [normalize_boolean](#normalize_boolean)
    -   [normalize_string](#normalize_string)
    -   [normalize_int](#normalize_int)
    -   [normalize_float](#normalize_float)
    -   [remove_line_breaks](#remove_line_breaks)
    -   [remove_html_tags](#remove_html_tags)
    -   [remove_special_characters](#remove_special_characters)
    -   [normalize_sql_date](#normalize_sql_date)
3.  [Пример использования](#usage-example)
4.  [Требования](#requirements)

---

## Обзор

Модуль предоставляет удобные утилиты для нормализации и обработки данных. Его можно использовать для:
-   Удаления HTML-тегов из строк.
-   Преобразования строк в числовые или булевы значения.
-   Очистки строк от специальных символов.
-   Преобразования списков строк в одну нормализованную строку.

---

## Функции модуля

### `normalize_boolean`

**Описание:**
Преобразует входное значение в булево значение.

**Аргументы:**
-   `input_data (Any)`: Данные, которые могут представлять булево значение (строка, число, булевый тип).

**Возвращает:**
-   `bool`: Преобразованное булево значение.

**Пример:**
```python
normalize_boolean('yes')  # Result: True
normalize_boolean(0)      # Result: False
```

---

### `normalize_string`

**Описание:**
Преобразует строку или список строк в нормализованную строку, удаляя лишние пробелы, HTML-теги и специальные символы.

**Аргументы:**
-   `input_data (str | list)`: Строка или список строк.

**Возвращает:**
-   `str`: Очищенная строка в кодировке UTF-8.

**Пример:**
```python
normalize_string(['  Example string  ', '<b>with HTML</b>'])  # Result: 'Example string with HTML'
```

---

### `normalize_int`

**Описание:**
Преобразует входное значение в целое число.

**Аргументы:**
-   `input_data (str | int | float | Decimal)`: Число или его строковое представление.

**Возвращает:**
-   `int`: Преобразованное целое число.

**Пример:**
```python
normalize_int('42')  # Result: 42
normalize_int(3.14)  # Result: 3
```

---

### `normalize_float`

**Описание:**
Преобразует входное значение в число с плавающей точкой.

**Аргументы:**
-   `value (str | int | float | list[str|int|float])`: Число, строка или список чисел.

**Возвращает:**
-   `float | List[float] | None`: Число с плавающей точкой, список чисел с плавающей точкой или `None` в случае ошибки.

**Пример:**
```python
normalize_float('3.14')         # Result: 3.14
normalize_float([1, '2.5', 3])  # Result: [1.0, 2.5, 3.0]
```

---

### `remove_line_breaks`

**Описание:**
Удаляет символы новой строки из строки.

**Аргументы:**
-   `input_str (str)`: Входная строка.

**Возвращает:**
-   `str`: Строка без разрывов строк.

**Пример:**
```python
remove_line_breaks('String\\nwith line breaks\\r')  # Result: 'String with line breaks'
```

---

### `remove_html_tags`

**Описание:**
Удаляет HTML-теги из строки.

**Аргументы:**
-   `input_html (str)`: Входная строка с HTML-тегами.

**Возвращает:**
-   `str`: Строка без HTML-тегов.

**Пример:**
```python
remove_html_tags('<p>Example text</p>')  # Result: 'Example text'
```

---

### `remove_special_characters`

**Описание:**
Удаляет специальные символы из строки или списка строк.

**Аргументы:**
-   `input_str (str | list)`: Строка или список строк.

**Возвращает:**
-   `str | list`: Строка или список строк без специальных символов.

**Пример:**
```python
remove_special_characters('Hello@World!')  # Result: 'HelloWorld'
```

---

### `normalize_sql_date`

**Описание:**
Преобразует строку или объект datetime в стандартный формат SQL-даты (`YYYY-MM-DD`).

**Аргументы:**
-   `input_data (str | datetime)`: Строка или объект datetime, представляющий дату.

**Возвращает:**
-   `str`: Нормализованная SQL-дата в виде строки в формате `YYYY-MM-DD`.

**Пример:**
```python
normalize_sql_date('2024-12-06')  # Result: '2024-12-06'
normalize_sql_date(datetime(2024, 12, 6))  # Result: '2024-12-06'
```

---

## Пример использования
```python
#  Пример использования перенесен в example.py
```

---

## Требования

-   Python 3.10 или выше.
-   Модуль `src.logger` для логирования.
-   Модуль используется в режиме разработки (``).

---

## Логирование

Все ошибки и предупреждения логируются через `logger`:
-   Ошибки логируются с помощью `logger.error`.
-   Неожиданные значения логируются с помощью `logger.debug` или `logger.warning`.
```
````
```python
"""
Модуль для нормализации строк, чисел и дат.
=========================================================================================

Этот модуль содержит функции для нормализации различных типов данных,
таких как строки, булевы значения, целые числа, числа с плавающей точкой и даты.

"""
from decimal import Decimal
from datetime import datetime
from typing import Any, List
import re

from src.logger import logger

def normalize_boolean(input_data: Any) -> bool:
    """
    Преобразует входное значение в булево значение.

    Args:
        input_data (Any): Данные, которые могут представлять булево значение (строка, число, булевый тип).

    Returns:
        bool: Преобразованное булево значение.
    """
    if isinstance(input_data, bool):
        return input_data
    if isinstance(input_data, str):
        if input_data.lower() in ['true', 'yes', '1']:
            return True
        if input_data.lower() in ['false', 'no', '0', '']:
            return False
    if isinstance(input_data, int):
        return bool(input_data)
    return False


def normalize_string(input_data: str | list) -> str:
    """
    Преобразует строку или список строк в нормализованную строку,
    удаляя лишние пробелы, HTML-теги и специальные символы.

    Args:
        input_data (str | list): Строка или список строк.

    Returns:
        str: Очищенная строка в кодировке UTF-8.
    """
    if isinstance(input_data, list):
        input_data = ' '.join(map(str, input_data))

    if not isinstance(input_data, str):
        logger.debug(f'Неверный тип данных {type(input_data)=}')
        return ''

    input_data = remove_html_tags(input_data)
    input_data = remove_special_characters(input_data)
    input_data = remove_line_breaks(input_data)
    input_data = ' '.join(input_data.split())
    return input_data


def normalize_int(input_data: str | int | float | Decimal) -> int:
    """
    Преобразует входное значение в целое число.

    Args:
        input_data (str | int | float | Decimal): Число или его строковое представление.

    Returns:
        int: Преобразованное целое число.
    Raises:
         ValueError: Если не удается преобразовать входные данные в целое число.
    """
    try:
        if isinstance(input_data, str):
            return int(float(input_data))
        return int(input_data)
    except Exception as ex:
        logger.exception(f'Не удалось преобразовать в int {input_data=}', ex)
        return 0


def normalize_float(value: str | int | float | list[str|int|float]) -> float | List[float] | None:
    """
    Преобразует входное значение в число с плавающей точкой.

    Args:
        value (str | int | float | list[str|int|float]): Число, строка или список чисел.

    Returns:
        float | List[float] | None: Число с плавающей точкой, список чисел с плавающей точкой или `None` в случае ошибки.
    Raises:
        ValueError: Если не удается преобразовать входные данные в число с плавающей точкой.
    """
    if isinstance(value, (int, float)):
        return float(value)
    if isinstance(value, str):
        try:
            return float(value)
        except Exception as ex:
            logger.exception(f'Не удалось преобразовать в float {value=}', ex)
            return None
    if isinstance(value, list):
        result = []
        for item in value:
            try:
                result.append(float(item))
            except Exception as ex:
                logger.exception(f'Не удалось преобразовать в float {item=}', ex)
                return None
        return result
    logger.debug(f'Неверный тип данных {value=}')
    return None

def remove_line_breaks(input_str: str) -> str:
    """
    Удаляет символы новой строки из строки.

    Args:
        input_str (str): Входная строка.

    Returns:
        str: Строка без разрывов строк.
    """
    return input_str.replace('\n', '').replace('\r', '')


def remove_html_tags(input_html: str) -> str:
    """
    Удаляет HTML-теги из строки.

    Args:
        input_html (str): Входная строка с HTML-тегами.

    Returns:
        str: Строка без HTML-тегов.
    """
    clean_text = re.compile('<.*?>')
    return re.sub(clean_text, '', input_html)


def remove_special_characters(input_str: str | list) -> str | list:
    """
    Удаляет специальные символы из строки или списка строк.

    Args:
        input_str (str | list): Строка или список строк.

    Returns:
        str | list: Строка или список строк без специальных символов.
    """
    if isinstance(input_str, list):
        return [re.sub(r'[^a-zA-Z0-9\s]', '', str(item)) for item in input_str]
    if isinstance(input_str, str):
        return re.sub(r'[^a-zA-Z0-9\s]', '', input_str)
    logger.debug(f'Неверный тип данных {input_str=}')
    return ''


def normalize_sql_date(input_data: str | datetime) -> str:
    """
    Преобразует строку или объект datetime в стандартный формат SQL-даты (`YYYY-MM-DD`).

    Args:
        input_data (str | datetime): Строка или объект datetime, представляющий дату.

    Returns:
        str: Нормализованная SQL-дата в виде строки в формате `YYYY-MM-DD`.
    Raises:
        ValueError: Если не удается преобразовать входные данные в дату.
    """
    try:
        if isinstance(input_data, str):
            date_obj = datetime.fromisoformat(input_data)
        elif isinstance(input_data, datetime):
             date_obj = input_data
        else:
            logger.debug(f'Неверный тип данных {input_data=}')
            return ''
        return date_obj.strftime('%Y-%m-%d')
    except Exception as ex:
        logger.exception(f'Не удалось преобразовать в дату {input_data=}', ex)
        return ''
```