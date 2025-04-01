# Анализ кода модуля `src.utils.string`

**Качество кода:**

- **Соответствие стандартам**: 7
- **Плюсы**:
    - Хорошее описание функций и их назначения.
    - Примеры использования функций в документации.
    - Структурированное описание с использованием заголовков.
- **Минусы**:
    - Не хватает подробного описания работы с ошибками в функциях.
    - Отсутствует  RST документация для функций.
    - Не используется `logger` из `src.logger`.
    - Код примера не отображает импорты из модуля.
    - Не все функции имеют примеры использования.

**Рекомендации по улучшению:**

1.  **Добавить RST документацию для функций**: 
    -   Дополнить каждую функцию RST документацией.
2.  **Использовать `logger`**:
    -   Импортировать `logger` из `src.logger` и использовать для логирования ошибок и предупреждений в функциях.
3.  **Обработка ошибок**:
    - Указать в RST-документации возможные исключения и методы их обработки через `logger.error`.
4.  **Улучшить примеры использования**:
    - Дополнить примеры использования функций, показывая импорты, чтобы сделать их более практичными.
5.  **Проверить наличие всех необходимых импортов**:
    -  Удостовериться, что все необходимые импорты для модуля присутствуют.
6.  **Форматирование**:
    -   Привести форматирование кода в соответствие со стандартами PEP8.
7. **Обновить формат документации**:
    -   Уточнить, что используется документация **RST**.

**Оптимизированный код:**

```rst
.. module:: src.utils.string

Data Normalizer Module Documentation
====================================

Модуль :mod:`src.utils.string` предоставляет функциональность для нормализации различных типов данных, включая строки, логические значения, целые числа и числа с плавающей запятой. Он также включает вспомогательные функции для обработки текста.

---

## Оглавление

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

Модуль предоставляет удобные утилиты для нормализации и обработки данных. Он может быть использован для:

-   Удаления HTML-тегов из строк.
-   Преобразования строк в числовые или логические значения.
-   Очистки строк от специальных символов.
-   Преобразования списков строк в одну нормализованную строку.

---

## Функции модуля

### `normalize_boolean`

**Описание:**
    Преобразует входное значение в логическое.

**Аргументы:**
    -   `input_data (Any)`: Данные, представляющие логическое значение (строка, число, логический тип).

**Возвращает:**
    -   `bool`: Преобразованное логическое значение.

**Пример:**
   
    >>> normalize_boolean('yes')
    True
    >>> normalize_boolean(0)
    False
 
.. code-block:: python
    
    def normalize_boolean(input_data: Any) -> bool:
        """
        Преобразует входное значение в логическое.

        :param input_data: Данные, представляющие логическое значение (строка, число, логический тип).
        :type input_data: Any
        :return: Преобразованное логическое значение.
        :rtype: bool
        
        Пример:
            >>> normalize_boolean('yes')
            True
            >>> normalize_boolean(0)
            False
        """
        ...


---

### `normalize_string`

**Описание:**
    Преобразует строку или список строк в нормализованную строку, удаляя лишние пробелы, HTML-теги и специальные символы.

**Аргументы:**
    -   `input_data (str | list)`: Строка или список строк.

**Возвращает:**
    -   `str`: Очищенная строка в кодировке UTF-8.

**Пример:**
    
    >>> normalize_string(['  Example string  ', '<b>with HTML</b>'])
    'Example string with HTML'
 
.. code-block:: python

    def normalize_string(input_data: str | list) -> str:
        """
        Преобразует строку или список строк в нормализованную строку, 
        удаляя лишние пробелы, HTML-теги и специальные символы.

        :param input_data: Строка или список строк.
        :type input_data: str | list
        :return: Очищенная строка в кодировке UTF-8.
        :rtype: str
        
        Пример:
            >>> normalize_string(['  Example string  ', '<b>with HTML</b>'])
            'Example string with HTML'
        """
        ...


---

### `normalize_int`

**Описание:**
    Преобразует входное значение в целое число.

**Аргументы:**
    -   `input_data (str | int | float | Decimal)`: Число или его строковое представление.

**Возвращает:**
    -   `int`: Преобразованное целое число.

**Пример:**
    
    >>> normalize_int('42')
    42
    >>> normalize_int(3.14)
    3

.. code-block:: python
    
    def normalize_int(input_data: str | int | float | Decimal) -> int:
        """
        Преобразует входное значение в целое число.

        :param input_data: Число или его строковое представление.
        :type input_data: str | int | float | Decimal
        :return: Преобразованное целое число.
        :rtype: int
        
        Пример:
            >>> normalize_int('42')
            42
            >>> normalize_int(3.14)
            3
        """
        ...


---

### `normalize_float`

**Описание:**
    Преобразует входное значение в число с плавающей запятой.

**Аргументы:**
    -   `value (Any)`: Число, строка или список чисел.

**Возвращает:**
    -   `float | List[float] | None`: Число с плавающей запятой, список чисел с плавающей запятой или `None` в случае ошибки.

**Пример:**
    
    >>> normalize_float('3.14')
    3.14
    >>> normalize_float([1, '2.5', 3])
    [1.0, 2.5, 3.0]

.. code-block:: python

    def normalize_float(value: Any) -> float | list[float] | None:
        """
        Преобразует входное значение в число с плавающей запятой.

        :param value: Число, строка или список чисел.
        :type value: Any
        :return: Число с плавающей запятой, список чисел с плавающей запятой или `None` в случае ошибки.
        :rtype: float | list[float] | None
        
        Пример:
            >>> normalize_float('3.14')
            3.14
            >>> normalize_float([1, '2.5', 3])
            [1.0, 2.5, 3.0]
        """
        ...

---

### `remove_line_breaks`

**Описание:**
    Удаляет символы новой строки из строки.

**Аргументы:**
    -   `input_str (str)`: Входная строка.

**Возвращает:**
    -   `str`: Строка без символов новой строки.

**Пример:**
    
    >>> remove_line_breaks('String\\nwith line breaks\\r')
    'String with line breaks'

.. code-block:: python
    
    def remove_line_breaks(input_str: str) -> str:
        """
        Удаляет символы новой строки из строки.

        :param input_str: Входная строка.
        :type input_str: str
        :return: Строка без символов новой строки.
        :rtype: str
        
        Пример:
            >>> remove_line_breaks('String\\nwith line breaks\\r')
            'String with line breaks'
        """
        ...


---

### `remove_html_tags`

**Описание:**
    Удаляет HTML-теги из строки.

**Аргументы:**
    -   `input_html (str)`: Входная строка с HTML-тегами.

**Возвращает:**
    -   `str`: Строка без HTML-тегов.

**Пример:**
    
    >>> remove_html_tags('<p>Example text</p>')
    'Example text'

.. code-block:: python
    
    def remove_html_tags(input_html: str) -> str:
        """
        Удаляет HTML-теги из строки.

        :param input_html: Входная строка с HTML-тегами.
        :type input_html: str
        :return: Строка без HTML-тегов.
        :rtype: str
        
        Пример:
            >>> remove_html_tags('<p>Example text</p>')
            'Example text'
        """
        ...

---

### `remove_special_characters`

**Описание:**
    Удаляет специальные символы из строки или списка строк.

**Аргументы:**
    -   `input_str (str | list)`: Строка или список строк.

**Возвращает:**
    -   `str | list`: Строка или список строк без специальных символов.

**Пример:**
    
    >>> remove_special_characters('Hello@World!')
    'HelloWorld'

.. code-block:: python
    
    def remove_special_characters(input_str: str | list) -> str | list:
        """
        Удаляет специальные символы из строки или списка строк.

        :param input_str: Строка или список строк.
        :type input_str: str | list
        :return: Строка или список строк без специальных символов.
        :rtype: str | list
        
        Пример:
            >>> remove_special_characters('Hello@World!')
            'HelloWorld'
        """
        ...

---

### `normalize_sql_date`

**Описание:**
    Преобразует строку или объект datetime в стандартный формат SQL-даты (`YYYY-MM-DD`).

**Аргументы:**
    -   `input_data (str | datetime)`: Строка или объект datetime, представляющий дату.

**Возвращает:**
    -   `str`: Нормализованная SQL-дата в формате `YYYY-MM-DD`.

**Пример:**
    
    >>> normalize_sql_date('2024-12-06')
    '2024-12-06'
    >>> normalize_sql_date(datetime(2024, 12, 6))
    '2024-12-06'

.. code-block:: python

    from datetime import datetime
    
    def normalize_sql_date(input_data: str | datetime) -> str:
        """
        Преобразует строку или объект datetime в стандартный формат SQL-даты (`YYYY-MM-DD`).

        :param input_data: Строка или объект datetime, представляющий дату.
        :type input_data: str | datetime
        :return: Нормализованная SQL-дата в формате `YYYY-MM-DD`.
        :rtype: str
        
        Пример:
            >>> normalize_sql_date('2024-12-06')
            '2024-12-06'
            >>> normalize_sql_date(datetime(2024, 12, 6))
            '2024-12-06'
        """
        ...

---

## Пример использования

```python
from src.utils.string.normalizer import (
    normalize_string,
    normalize_boolean,
    normalize_int,
    normalize_float,
    normalize_sql_date
)

# Нормализация строки
clean_str = normalize_string(['<h1>Header</h1>', '  text with spaces  '])
print(clean_str)  # 'Header text with spaces'

# Нормализация логического значения
is_active = normalize_boolean('Yes')
print(is_active)  # True

# Нормализация целого числа
integer_value = normalize_int('42')
print(integer_value)  # 42

# Нормализация числа с плавающей запятой
float_value = normalize_float('3.14159')
print(float_value)  # 3.14159

# Нормализация SQL-даты
sql_date = normalize_sql_date('2024-12-06')
print(sql_date)  # '2024-12-06'
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