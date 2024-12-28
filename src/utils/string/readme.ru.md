```rst
.. module:: src.utils.string.normalizer
```
Документация модуля нормализации данных
=========================================

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

**Описание:**  
Преобразует входное значение в булево значение.

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

**Описание:**  
Преобразует строку или список строк в нормализованную строку, удаляя лишние пробелы, HTML теги и специальные символы.

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

**Описание:**  
Преобразует входное значение в целое число.

**Аргументы:**  
- `input_data (str | int | float | Decimal)`: Число или его строковое представление.

**Возвращает:**  
- `int`: Преобразованное целое число.

**Пример:**  
```python
normalize_int('42')  # Результат: 42
normalize_int(3.14)  # Результат: 3
```

---

### `normalize_float`

**Описание:**  
Преобразует входное значение в число с плавающей запятой.

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

**Описание:**  
Удаляет символы новой строки из строки.

**Аргументы:**  
- `input_str (str)`: Входная строка.

**Возвращает:**  
- `str`: Строка без символов новой строки.

**Пример:**  
```python
remove_line_breaks('String\nwith line breaks\r')  # Результат: 'String with line breaks'
```

---

### `remove_html_tags`

**Описание:**  
Удаляет HTML теги из строки.

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

**Описание:**  
Удаляет специальные символы из строки или списка строк.

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

**Описание:**  
Преобразует строку или объект `datetime` в стандартный формат SQL даты (`YYYY-MM-DD`).

**Аргументы:**  
- `input_data (str | datetime)`: Строка или объект `datetime`, представляющий дату.

**Возвращает:**  
- `str`: Нормализованная дата в формате строки `YYYY-MM-DD`.

**Пример:**  
```python
normalize_sql_date('2024-12-06')  # Результат: '2024-12-06'
normalize_sql_date(datetime(2024, 12, 6))  # Результат: '2024-12-06'
```

---

## Пример использования

```python
from src.utils.string.normalizer import normalize_string, normalize_boolean, normalize_int, normalize_float, normalize_sql_date

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
- Модуль используется в режиме разработки (``).

---

## Логирование

Все ошибки и предупреждения записываются через `logger`:
- Ошибки записываются с использованием `logger.error`.
- Неожиданные значения записываются с использованием `logger.debug` или `logger.warning`.
