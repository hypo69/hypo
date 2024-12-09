# Модуль нормализации данных

## Обзор

Модуль `normalizer` предоставляет функциональность для нормализации различных типов данных, включая строки, булевы значения, целые числа и числа с плавающей точкой. Он также содержит вспомогательные функции для обработки текста.

## Оглавление

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


## Функции модуля

### `normalize_boolean`

**Описание:** Преобразует входное значение в булево значение.

**Аргументы:**
- `input_data (Any)`: Данные, которые могут представлять булево значение (строка, число, тип bool).

**Возвращает:**
- `bool`: Преобразованное булево значение.

**Примеры:**
```python
normalize_boolean('yes')  # Результат: True
normalize_boolean(0)      # Результат: False
```

### `normalize_string`

**Описание:** Преобразует строку или список строк в нормализованную строку, удаляя лишние пробелы, HTML-теги и специальные символы.

**Аргументы:**
- `input_data (str | list)`: Строка или список строк.

**Возвращает:**
- `str`: Очищенная строка UTF-8.

**Примеры:**
```python
normalize_string(['  Пример строки  ', '<b>с HTML</b>'])  # Результат: 'Пример строки с HTML'
```

### `normalize_int`

**Описание:** Преобразует входное значение в целое число.

**Аргументы:**
- `input_data (str | int | float | Decimal)`: Число или его строковое представление.

**Возвращает:**
- `int`: Преобразованное целое число.

**Примеры:**
```python
normalize_int('42')  # Результат: 42
normalize_int(3.14)  # Результат: 3
```

### `normalize_float`

**Описание:** Преобразует входное значение в число с плавающей точкой.

**Аргументы:**
- `value (Any)`: Число, строка или список чисел.

**Возвращает:**
- `float | List[float] | None`: Число с плавающей точкой, список чисел с плавающей точкой или `None` в случае ошибки.

**Примеры:**
```python
normalize_float('3.14')         # Результат: 3.14
normalize_float([1, '2.5', 3])  # Результат: [1.0, 2.5, 3.0]
```

### `remove_line_breaks`

**Описание:** Удаляет символы новой строки из строки.

**Аргументы:**
- `input_str (str)`: Входная строка.

**Возвращает:**
- `str`: Строка без символов новой строки.

**Примеры:**
```python
remove_line_breaks('Строка\\nс переносами\\r')  # Результат: 'Строка с переносами'
```

### `remove_html_tags`

**Описание:** Удаляет HTML-теги из строки.

**Аргументы:**
- `input_html (str)`: Входная строка с HTML-тегами.

**Возвращает:**
- `str`: Строка без HTML-тегов.

**Примеры:**
```python
remove_html_tags('<p>Пример текста</p>')  # Результат: 'Пример текста'
```

### `remove_special_characters`

**Описание:** Удаляет специальные символы из строки или списка строк.

**Аргументы:**
- `input_str (str | list)`: Строка или список строк.

**Возвращает:**
- `str | list`: Строка или список строк без специальных символов.

**Примеры:**
```python
remove_special_characters('Привет@мир!')  # Результат: 'Приветмир!'
```

### `normalize_sql_date`

**Описание:** Преобразует строку или объект datetime в стандартный формат даты SQL (`YYYY-MM-DD`).

**Аргументы:**
- `input_data (str | datetime)`: Строка или объект datetime, представляющий дату.

**Возвращает:**
- `str`: Нормализованная дата SQL в формате `YYYY-MM-DD`.

**Примеры:**
```python
normalize_sql_date('2024-12-06')  # Результат: '2024-12-06'
normalize_sql_date(datetime(2024, 12, 6))  # Результат: '2024-12-06'
```

## Пример использования

```python
from src.utils.string.normalizer import normalize_string, normalize_boolean, normalize_int, normalize_float, normalize_sql_date
from datetime import datetime

# Нормализация строки
clean_str = normalize_string(['<h1>Заголовок</h1>', '  текст с пробелами  '])
print(clean_str)  # 'Заголовок текст с пробелами'

# Нормализация булева значения
is_active = normalize_boolean('Да')
print(is_active)  # True

# Нормализация целого числа
integer_value = normalize_int('42')
print(integer_value)  # 42

# Нормализация числа с плавающей точкой
float_value = normalize_float('3.14159')
print(float_value)  # 3.14159

# Нормализация SQL даты
sql_date = normalize_sql_date('2024-12-06')
print(sql_date)  # '2024-12-06'
```

## Требования

- Python 3.10 или выше.
- Модуль `src.logger` для ведения журнала.
- Модуль используется в режиме разработки (`MODE = 'dev'`).


## Ведение журнала

Все ошибки и предупреждения записываются в `logger`:
- Ошибки записываются с помощью `logger.error`.
- Неожиданные значения записываются с помощью `logger.debug` или `logger.warning`.
```