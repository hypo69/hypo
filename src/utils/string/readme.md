```rst
.. module:: src.utils.string
```

Data Normalizer Module Documentation
=====================================

The `normalizer` module provides functionality for normalizing various data types, including strings, booleans, integers, and floating-point numbers. It also includes helper functions for text processing.

---

## Table of Contents

1. [Overview](#overview)
2. [Module Functions](#module-functions)
   - [normalize_boolean](#normalize_boolean)
   - [normalize_string](#normalize_string)
   - [normalize_int](#normalize_int)
   - [normalize_float](#normalize_float)
   - [remove_line_breaks](#remove_line_breaks)
   - [remove_html_tags](#remove_html_tags)
   - [remove_special_characters](#remove_special_characters)
   - [normalize_sql_date](#normalize_sql_date)
3. [Usage Example](#usage-example)
4. [Requirements](#requirements)

---

## Overview

The module provides convenient data normalization and processing utilities. It can be used to:
- Remove HTML tags from strings.
- Convert strings to numeric or boolean values.
- Clean strings from special characters.
- Convert lists of strings into a single normalized string.

---

## Module Functions

### `normalize_boolean`

**Description:**  
Converts the input value into a boolean.

**Arguments:**  
- `input_data (Any)`: The data that can represent a boolean value (string, number, boolean type).

**Returns:**  
- `bool`: The converted boolean value.

**Example:**  
```python
normalize_boolean('yes')  # Result: True
normalize_boolean(0)      # Result: False
```

---

### `normalize_string`

**Description:**  
Converts a string or a list of strings into a normalized string by removing extra spaces, HTML tags, and special characters.

**Arguments:**  
- `input_data (str | list)`: A string or list of strings.

**Returns:**  
- `str`: A cleaned UTF-8 string.

**Example:**  
```python
normalize_string(['  Example string  ', '<b>with HTML</b>'])  # Result: 'Example string with HTML'
```

---

### `normalize_int`

**Description:**  
Converts the input value into an integer.

**Arguments:**  
- `input_data (str | int | float | Decimal)`: A number or its string representation.

**Returns:**  
- `int`: The converted integer value.

**Example:**  
```python
normalize_int('42')  # Result: 42
normalize_int(3.14)  # Result: 3
```

---

### `normalize_float`

**Description:**  
Converts the input value into a floating-point number.

**Arguments:**  
- `value (Any)`: A number, string, or list of numbers.

**Returns:**  
- `float | List[float] | None`: A floating-point number, a list of floating-point numbers, or `None` in case of error.

**Example:**  
```python
normalize_float('3.14')         # Result: 3.14
normalize_float([1, '2.5', 3])  # Result: [1.0, 2.5, 3.0]
```

---

### `remove_line_breaks`

**Description:**  
Removes newline characters from a string.

**Arguments:**  
- `input_str (str)`: The input string.

**Returns:**  
- `str`: The string without line breaks.

**Example:**  
```python
remove_line_breaks('String\nwith line breaks\r')  # Result: 'String with line breaks'
```

---

### `remove_html_tags`

**Description:**  
Removes HTML tags from a string.

**Arguments:**  
- `input_html (str)`: The input string with HTML tags.

**Returns:**  
- `str`: The string without HTML tags.

**Example:**  
```python
remove_html_tags('<p>Example text</p>')  # Result: 'Example text'
```

---

### `remove_special_characters`

**Description:**  
Removes special characters from a string or a list of strings.

**Arguments:**  
- `input_str (str | list)`: A string or list of strings.

**Returns:**  
- `str | list`: A string or list of strings without special characters.

**Example:**  
```python
remove_special_characters('Hello@World!')  # Result: 'HelloWorld'
```

---

### `normalize_sql_date`

**Description:**  
Converts a string or datetime object into a standard SQL date format (`YYYY-MM-DD`).

**Arguments:**  
- `input_data (str | datetime)`: A string or datetime object representing a date.

**Returns:**  
- `str`: The normalized SQL date as a string in `YYYY-MM-DD` format.

**Example:**  
```python
normalize_sql_date('2024-12-06')  # Result: '2024-12-06'
normalize_sql_date(datetime(2024, 12, 6))  # Result: '2024-12-06'
```

---

## Usage Example

```python
from src.utils.string.normalizer import normalize_string, normalize_boolean, normalize_int, normalize_float, normalize_sql_date

# Normalizing a string
clean_str = normalize_string(['<h1>Header</h1>', '  text with spaces  '])
print(clean_str)  # 'Header text with spaces'

# Normalizing a boolean value
is_active = normalize_boolean('Yes')
print(is_active)  # True

# Normalizing an integer
integer_value = normalize_int('42')
print(integer_value)  # 42

# Normalizing a floating-point number
float_value = normalize_float('3.14159')
print(float_value)  # 3.14159

# Normalizing a SQL date
sql_date = normalize_sql_date('2024-12-06')
print(sql_date)  # '2024-12-06'
```

---

## Requirements

- Python 3.10 or higher.
- The `src.logger` module for logging.
- The module is used in development mode (``).

---

## Logging

All errors and warnings are logged via `logger`:
- Errors are logged using `logger.error`.
- Unexpected values are logged using `logger.debug` or `logger.warning`.
