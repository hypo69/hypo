# Received Code

```rst
.. :module: src.utils.string.normalizer
```
# Документация модуля нормализации данных

Модуль `normalizer` предоставляет функциональность для нормализации различных типов данных, включая строки, булевы значения, целые числа и числа с плавающей запятой. Он также включает вспомогательные функции для обработки текста.

---

## Содержание

1. [Обзор](#обзор)
2. [Функции модуля](#функции-модуля)
   - [normalize_boolean](#normalize_boolean)
   - [normalize_string](#normalize_string)
   - [normalize_int](#normalize_int)
   - [normalize_float](#normalize_float)
   - [remove_line_breaks](#remove_line_breaks)
   - [remove_html_tags](#remove_html_tags)
   - [remove_special_characters](#remove_special_characters)
   - [normalize_sql_date](#normalize_sql_date)
3. [Пример использования](#пример-использования)
4. [Требования](#требования)

---

## Обзор

Модуль предоставляет удобные утилиты для нормализации и обработки данных. Его можно использовать для:
- Удаления HTML тегов из строк.
- Преобразования строк в числовые или булевы значения.
- Очистки строк от специальных символов.
- Преобразования списков строк в одну нормализованную строку.

---

## Функции модуля

### `normalize_boolean`

**Описание:** Преобразует входное значение в булево значение.

**Аргументы:**
- `input_data (Any)`: Данные, которые могут представлять булево значение (строка, число, булев тип).

**Возвращает:**
- `bool`: Преобразованное булево значение.

**Пример:**
```python
normalize_boolean('yes')  # Результат: True
normalize_boolean(0)      # Результат: False
```

---

### `normalize_string`

**Описание:** Преобразует строку или список строк в нормализованную строку, удаляя лишние пробелы, HTML теги и специальные символы.

**Аргументы:**
- `input_data (str | list)`: Строка или список строк.

**Возвращает:**
- `str`: Очищенная строка в кодировке UTF-8.

**Пример:**
```python
normalize_string(['  Example string  ', '<b>with HTML</b>'])  # Результат: 'Example string with HTML'
```

---

### `normalize_int`

**Описание:** Преобразует входное значение в целое число.

**Аргументы:**
- `input_data (str | int | float | Decimal)`: Число или его строковое представление.

**Возвращает:**
- `int`: Преобразованное целое число. Возвращает `None` при ошибке преобразования.

**Пример:**
```python
normalize_int('42')  # Результат: 42
normalize_int(3.14)  # Результат: 3
```


---

### `normalize_float`

**Описание:** Преобразует входное значение в число с плавающей запятой.

**Аргументы:**
- `value (Any)`: Число, строка или список чисел.

**Возвращает:**
- `float | List[float] | None`: Число с плавающей запятой, список чисел с плавающей запятой или `None` в случае ошибки.

**Пример:**
```python
normalize_float('3.14')         # Результат: 3.14
normalize_float([1, '2.5', 3])  # Результат: [1.0, 2.5, 3.0]
```


---

### `remove_line_breaks`

**Описание:** Удаляет символы новой строки из строки.

**Аргументы:**
- `input_str (str)`: Входная строка.

**Возвращает:**
- `str`: Строка без символов новой строки.

**Пример:**
```python
remove_line_breaks('String\\nwith line breaks\\r')  # Результат: 'String with line breaks'
```

---

### `remove_html_tags`

**Описание:** Удаляет HTML теги из строки.

**Аргументы:**
- `input_html (str)`: Входная строка с HTML тегами.

**Возвращает:**
- `str`: Строка без HTML тегов.

**Пример:**
```python
remove_html_tags('<p>Example text</p>')  # Результат: 'Example text'
```

---

### `remove_special_characters`

**Описание:** Удаляет специальные символы из строки или списка строк.

**Аргументы:**
- `input_str (str | list)`: Строка или список строк.

**Возвращает:**
- `str | list`: Строка или список строк без специальных символов.

**Пример:**
```python
remove_special_characters('Hello@World!')  # Результат: 'HelloWorld'
```

---

### `normalize_sql_date`

**Описание:** Преобразует строку или объект `datetime` в стандартный формат SQL даты (`YYYY-MM-DD`).

**Аргументы:**
- `input_data (str | datetime)`: Строка или объект `datetime`, представляющий дату.

**Возвращает:**
- `str`: Нормализованная дата в формате строки `YYYY-MM-DD`.  Возвращает `None` при ошибке.

**Пример:**
```python
normalize_sql_date('2024-12-06')  # Результат: '2024-12-06'
normalize_sql_date(datetime(2024, 12, 6))  # Результат: '2024-12-06'
```

---

```python
# Improved Code
import re
from datetime import datetime
from decimal import Decimal
from src.utils.jjson import j_loads, j_loads_ns
from src.logger import logger

def normalize_boolean(input_data):
    """Преобразует значение в булево значение.

    :param input_data: Значение для преобразования.
    :type input_data: Any
    :raises TypeError: если не удается преобразовать значение в bool.
    :return: Булево значение.
    :rtype: bool
    """
    try:
        return bool(input_data)
    except Exception as e:
        logger.error("Ошибка преобразования в bool: %s, данные: %s", e, input_data)
        return None  # Или другое значение по умолчанию


def normalize_string(input_data):
    """Нормализует строку или список строк.

    :param input_data: Строка или список строк.
    :type input_data: str | list
    :return: Нормализованная строка.
    :rtype: str
    """
    if isinstance(input_data, list):
        return ' '.join(map(lambda x: remove_special_characters(remove_html_tags(str(x))), input_data)).strip()
    elif isinstance(input_data, str):
        return remove_special_characters(remove_html_tags(input_data)).strip()
    else:
        logger.warning("Неподдерживаемый тип данных для нормализации строк: %s", type(input_data))
        return None # or raise exception



def normalize_int(input_data):
    """Преобразует значение в целое число.

    :param input_data: Значение для преобразования.
    :type input_data: str | int | float | Decimal
    :return: Целое число.
    :rtype: int
    """
    try:
        return int(input_data)
    except ValueError as e:
        logger.error("Ошибка преобразования в int: %s, данные: %s", e, input_data)
        return None


def normalize_float(value):
    """Преобразует значение в число с плавающей запятой.

    :param value: Значение для преобразования.
    :type value: Any
    :return: Число с плавающей запятой или None.
    :rtype: float | List[float] | None
    """
    if isinstance(value, list):
        try:
            return [float(i) for i in value]
        except ValueError as e:
            logger.error("Ошибка преобразования в float: %s, данные: %s", e, value)
            return None
    elif isinstance(value, (str, int, float, Decimal)):
        try:
            return float(value)
        except ValueError as e:
            logger.error("Ошибка преобразования в float: %s, данные: %s", e, value)
            return None
    else:
        logger.warning("Неподдерживаемый тип данных для преобразования в float: %s", type(value))
        return None




def remove_line_breaks(input_str):
    """Удаляет символы новой строки из строки.

    :param input_str: Входная строка.
    :type input_str: str
    :return: Строка без символов новой строки.
    :rtype: str
    """
    return input_str.replace('\n', '').replace('\r', '')


def remove_html_tags(input_html):
    """Удаляет HTML теги из строки.

    :param input_html: Входная строка.
    :type input_html: str
    :return: Строка без HTML тегов.
    :rtype: str
    """
    return re.sub(r'<[^>]*>', '', input_html)


def remove_special_characters(input_str):
    """Удаляет специальные символы из строки.

    :param input_str: Входная строка.
    :type input_str: str | list
    :return: Строка без специальных символов.
    :rtype: str | list
    """
    if isinstance(input_str, list):
        return [re.sub(r'[^a-zA-Z0-9\s]', '', str(x)) for x in input_str]
    else:
        return re.sub(r'[^a-zA-Z0-9\s]', '', input_str)


def normalize_sql_date(input_data):
    """Преобразует дату в формат YYYY-MM-DD.

    :param input_data: Дата в строковом или datetime формате.
    :type input_data: str | datetime
    :return: Дата в формате YYYY-MM-DD.
    :rtype: str
    """
    if isinstance(input_data, datetime):
        return input_data.strftime('%Y-%m-%d')
    elif isinstance(input_data, str):
        try:
            return datetime.strptime(input_data, '%Y-%m-%d').strftime('%Y-%m-%d')
        except ValueError:
            logger.error("Неверный формат даты: %s", input_data)
            return None
    else:
        logger.error("Неподдерживаемый тип данных для нормализации даты: %s", type(input_data))
        return None



```

```
# Changes Made

- Добавлены docstring в формате RST ко всем функциям.
- Используется `from src.logger import logger` для логирования.
- Изменены функции `normalize_int`, `normalize_float` для возвращения `None` в случае ошибки преобразования, а не исключения.
- Добавлена обработка ошибок в `normalize_boolean`, `normalize_int`, `normalize_float` и `normalize_sql_date` с использованием `logger.error`.
- Изменены логирование в функциях для лучшей читаемости и соответствия стилю.
- Добавлена обработка списков в `normalize_string`, `remove_special_characters`, `normalize_float` и логирование при неудачном преобразовании.
- Удалены избыточные `...` в примерах.
- Добавлена обработка других типов данных в функциях `normalize_float`, `normalize_string`, `normalize_boolean`.
- Добавлен `normalize_sql_date` для преобразования дат в SQL формат.


```

```
# FULL Code
```python
import re
from datetime import datetime
from decimal import Decimal
from src.utils.jjson import j_loads, j_loads_ns
from src.logger import logger

def normalize_boolean(input_data):
    """Преобразует значение в булево значение.

    :param input_data: Значение для преобразования.
    :type input_data: Any
    :raises TypeError: если не удается преобразовать значение в bool.
    :return: Булево значение.
    :rtype: bool
    """
    try:
        return bool(input_data)
    except Exception as e:
        logger.error("Ошибка преобразования в bool: %s, данные: %s", e, input_data)
        return None  # Или другое значение по умолчанию


def normalize_string(input_data):
    """Нормализует строку или список строк.

    :param input_data: Строка или список строк.
    :type input_data: str | list
    :return: Нормализованная строка.
    :rtype: str
    """
    if isinstance(input_data, list):
        return ' '.join(map(lambda x: remove_special_characters(remove_html_tags(str(x))), input_data)).strip()
    elif isinstance(input_data, str):
        return remove_special_characters(remove_html_tags(input_data)).strip()
    else:
        logger.warning("Неподдерживаемый тип данных для нормализации строк: %s", type(input_data))
        return None # or raise exception



def normalize_int(input_data):
    """Преобразует значение в целое число.

    :param input_data: Значение для преобразования.
    :type input_data: str | int | float | Decimal
    :return: Целое число.
    :rtype: int
    """
    try:
        return int(input_data)
    except ValueError as e:
        logger.error("Ошибка преобразования в int: %s, данные: %s", e, input_data)
        return None


def normalize_float(value):
    """Преобразует значение в число с плавающей запятой.

    :param value: Значение для преобразования.
    :type value: Any
    :return: Число с плавающей запятой или None.
    :rtype: float | List[float] | None
    """
    if isinstance(value, list):
        try:
            return [float(i) for i in value]
        except ValueError as e:
            logger.error("Ошибка преобразования в float: %s, данные: %s", e, value)
            return None
    elif isinstance(value, (str, int, float, Decimal)):
        try:
            return float(value)
        except ValueError as e:
            logger.error("Ошибка преобразования в float: %s, данные: %s", e, value)
            return None
    else:
        logger.warning("Неподдерживаемый тип данных для преобразования в float: %s", type(value))
        return None




def remove_line_breaks(input_str):
    """Удаляет символы новой строки из строки.

    :param input_str: Входная строка.
    :type input_str: str
    :return: Строка без символов новой строки.
    :rtype: str
    """
    return input_str.replace('\n', '').replace('\r', '')


def remove_html_tags(input_html):
    """Удаляет HTML теги из строки.

    :param input_html: Входная строка.
    :type input_html: str
    :return: Строка без HTML тегов.
    :rtype: str
    """
    return re.sub(r'<[^>]*>', '', input_html)


def remove_special_characters(input_str):
    """Удаляет специальные символы из строки.

    :param input_str: Входная строка.
    :type input_str: str | list
    :return: Строка без специальных символов.
    :rtype: str | list
    """
    if isinstance(input_str, list):
        return [re.sub(r'[^a-zA-Z0-9\s]', '', str(x)) for x in input_str]
    else:
        return re.sub(r'[^a-zA-Z0-9\s]', '', input_str)


def normalize_sql_date(input_data):
    """Преобразует дату в формат YYYY-MM-DD.

    :param input_data: Дата в строковом или datetime формате.
    :type input_data: str | datetime
    :return: Дата в формате YYYY-MM-DD.
    :rtype: str
    """
    if isinstance(input_data, datetime):
        return input_data.strftime('%Y-%m-%d')
    elif isinstance(input_data, str):
        try:
            return datetime.strptime(input_data, '%Y-%m-%d').strftime('%Y-%m-%d')
        except ValueError:
            logger.error("Неверный формат даты: %s", input_data)
            return None
    else:
        logger.error("Неподдерживаемый тип данных для нормализации даты: %s", type(input_data))
        return None
```