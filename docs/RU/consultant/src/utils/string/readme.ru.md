# Анализ кода модуля `normalizer`

**Качество кода**
7
- Плюсы
    - Документация хорошо структурирована и охватывает большинство аспектов модуля.
    - Приведены примеры использования функций.
    - Описание каждой функции достаточно подробное.

- Минусы
    -  Не хватает документации в формате reStructuredText (RST) для корректного отображения в Sphinx.
    -  Отсутствуют docstring для функций.
    -  Не указаны импорты необходимые для работы кода, и из какого модуля нужно импортировать `logger`.
    -  Некоторые формулировки в описаниях могут быть более конкретными.

**Рекомендации по улучшению**

1.  Добавить docstring в формате RST для каждой функции, включая описание аргументов, возвращаемых значений и примеры использования.
2.  Использовать `from src.logger.logger import logger` для импорта логгера.
3.  Уточнить формулировки в описании функций, избегая слов вроде "получаем" или "делаем".
4.  Добавить информацию о том, что модуль работает с кодировкой UTF-8.
5.  Добавить проверку на типы входных данных.
6.  В разделе "Требования" указать, что требуется модуль `datetime`.

**Оптимизированный код**

```markdown
``````rst
.. module:: src.utils.string.normalizer

Модуль нормализации данных
========================================

Модуль `normalizer` предоставляет функциональность для нормализации различных типов данных,
включая строки, булевы значения, целые числа и числа с плавающей запятой.
Он также включает вспомогательные функции для обработки текста.

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
- Работает с кодировкой UTF-8.

---

## Функции модуля

### `normalize_boolean`

.. function:: normalize_boolean(input_data: Any) -> bool

   Преобразует входное значение в булево значение.

   :param input_data: Данные, которые могут представлять булево значение (строка, число, булев тип).
   :type input_data: Any
   :raises TypeError: Если input_data не строка, число, или булево значение.
   :return: Преобразованное булево значение.
   :rtype: bool

   **Пример:**

   .. code-block:: python

      normalize_boolean('yes')  # Результат: True
      normalize_boolean(0)      # Результат: False

---

### `normalize_string`

.. function:: normalize_string(input_data: str | list) -> str

   Преобразует строку или список строк в нормализованную строку, удаляя лишние пробелы, HTML теги и специальные символы.

   :param input_data: Строка или список строк.
   :type input_data: str | list
   :raises TypeError: Если input_data не строка или список.
   :return: Очищенная строка в кодировке UTF-8.
   :rtype: str

   **Пример:**

   .. code-block:: python

      normalize_string(['  Example string  ', '<b>with HTML</b>'])  # Результат: 'Example string with HTML'

---

### `normalize_int`

.. function:: normalize_int(input_data: str | int | float | Decimal) -> int

   Преобразует входное значение в целое число.

   :param input_data: Число или его строковое представление.
   :type input_data: str | int | float | Decimal
   :raises TypeError: Если input_data не строка, целое число, число с плавающей точкой, или Decimal.
   :return: Преобразованное целое число.
   :rtype: int

   **Пример:**

   .. code-block:: python

      normalize_int('42')  # Результат: 42
      normalize_int(3.14)  # Результат: 3

---

### `normalize_float`

.. function:: normalize_float(value: Any) -> float | List[float] | None

   Преобразует входное значение в число с плавающей запятой.

   :param value: Число, строка или список чисел.
   :type value: Any
   :raises TypeError: Если value не строка, число, или список.
   :return: Число с плавающей запятой, список чисел с плавающей запятой или `None` в случае ошибки.
   :rtype: float | List[float] | None

   **Пример:**

   .. code-block:: python

      normalize_float('3.14')         # Результат: 3.14
      normalize_float([1, '2.5', 3])  # Результат: [1.0, 2.5, 3.0]

---

### `remove_line_breaks`

.. function:: remove_line_breaks(input_str: str) -> str

   Удаляет символы новой строки из строки.

   :param input_str: Входная строка.
   :type input_str: str
   :raises TypeError: Если input_str не строка.
   :return: Строка без символов новой строки.
   :rtype: str

   **Пример:**

   .. code-block:: python

      remove_line_breaks('String\\nwith line breaks\\r')  # Результат: 'String with line breaks'

---

### `remove_html_tags`

.. function:: remove_html_tags(input_html: str) -> str

   Удаляет HTML теги из строки.

   :param input_html: Входная строка с HTML тегами.
   :type input_html: str
    :raises TypeError: Если input_html не строка.
   :return: Строка без HTML тегов.
   :rtype: str

   **Пример:**

   .. code-block:: python

      remove_html_tags('<p>Example text</p>')  # Результат: 'Example text'

---

### `remove_special_characters`

.. function:: remove_special_characters(input_str: str | list) -> str | list

   Удаляет специальные символы из строки или списка строк.

   :param input_str: Строка или список строк.
   :type input_str: str | list
   :raises TypeError: Если input_str не строка или список.
   :return: Строка или список строк без специальных символов.
   :rtype: str | list

   **Пример:**

   .. code-block:: python

      remove_special_characters('Hello@World!')  # Результат: 'HelloWorld'

---

### `normalize_sql_date`

.. function:: normalize_sql_date(input_data: str | datetime) -> str

   Преобразует строку или объект `datetime` в стандартный формат SQL даты (`YYYY-MM-DD`).

   :param input_data: Строка или объект `datetime`, представляющий дату.
   :type input_data: str | datetime
   :raises TypeError: Если input_data не строка или объект datetime.
   :return: Нормализованная дата в формате строки `YYYY-MM-DD`.
   :rtype: str

   **Пример:**

   .. code-block:: python

      normalize_sql_date('2024-12-06')  # Результат: '2024-12-06'
      normalize_sql_date(datetime(2024, 12, 6))  # Результат: '2024-12-06'

---

## Пример использования

```python
from src.utils.string.normalizer import normalize_string, normalize_boolean, normalize_int, normalize_float, normalize_sql_date
from datetime import datetime # добавлены импорты
from src.logger.logger import logger # импорт logger

# Нормализация строки
clean_str = normalize_string(['<h1>Header</h1>', '  text with spaces  '])
print(clean_str)  # 'Header text with spaces'

# Нормализация булевого значения
is_active = normalize_boolean('Yes')
print(is_active)  # True

# Нормализация целого числа
integer_value = normalize_int('42')
print(integer_value)  # 42

# Нормализация числа с плавающей запятой
float_value = normalize_float('3.14159')
print(float_value)  # 3.14159

# Нормализация SQL даты
sql_date = normalize_sql_date('2024-12-06')
print(sql_date)  # '2024-12-06'
```

---

## Требования

- Python 3.10 или выше.
- Модуль `src.logger` для логирования.
- Модуль `datetime` для работы с датами.
- Модуль используется в режиме разработки (``).

---

## Логирование

Все ошибки и предупреждения записываются через `logger`:\n
- Ошибки записываются с использованием `logger.error`.
- Неожиданные значения записываются с использованием `logger.debug` или `logger.warning`.
``````
```