# Модуль для нормализации строк и числовых данных

## Обзор

Модуль `normalizer.py` предоставляет набор функций для нормализации строк, булевых значений, целых чисел и чисел с плавающей точкой. Он также включает вспомогательные методы для обработки текста, такие как удаление HTML-тегов и специальных символов.

## Подробнее

Этот модуль предназначен для очистки и стандартизации данных, что особенно полезно при обработке пользовательского ввода или данных из внешних источников. Он обеспечивает консистентность данных, упрощает сравнение и хранение.

## Оглавление

- [Функции](#Функции)
    - [`normalize_boolean`](#normalize_boolean)
    - [`normalize_string`](#normalize_string)
    - [`normalize_int`](#normalize_int)
    - [`normalize_float`](#normalize_float)
    - [`normalize_sql_date`](#normalize_sql_date)
    - [`simplify_string`](#simplify_string)
    - [`remove_line_breaks`](#remove_line_breaks)
    - [`remove_html_tags`](#remove_html_tags)
    - [`remove_special_characters`](#remove_special_characters)
    - [`normalize_sku`](#normalize_sku)

## Функции

### `normalize_boolean`

```python
def normalize_boolean(input_data: Any) -> bool:
    """Normalize data into a boolean.

    Args:
        input_data (Any): Data that can represent a boolean (e.g., bool, string, integer).

    Returns:
        bool: Boolean representation of the input.

    Example:
        >>> normalize_boolean('yes')
        True
    """
```

**Назначение**:
Преобразует входные данные в булево значение.

**Как работает функция**:
Функция принимает входные данные любого типа и пытается преобразовать их в булево значение. Сначала проверяется, является ли входное значение уже булевым. Если нет, оно преобразуется в строку, удаляются начальные и конечные пробелы, и строка приводится к нижнему регистру. Затем проверяется, соответствует ли строка одному из предопределенных строковых представлений `True` или `False`. Если преобразование не удаётся, возвращается исходное значение.

**Параметры**:
- `input_data` (Any): Входные данные, которые могут быть представлены в виде булева значения (например, `bool`, `string`, `integer`).

**Возвращает**:
- `bool`: Булево представление входных данных.

**Примеры**:

```python
>>> normalize_boolean('yes')
True
>>> normalize_boolean(1)
True
>>> normalize_boolean('no')
False
>>> normalize_boolean(0)
False
```

### `normalize_string`

```python
def normalize_string(input_data: str | list) -> str:
    """Normalize a string or a list of strings.

    Args:
        input_data (str | list): Input data that can be either a string or a list of strings.

    Returns:
        str: Cleaned and normalized string in UTF-8 encoded format.

    Example:
        >>> normalize_string(['Hello', '  World!  '])
        'Hello World!'

    Raises:
        TypeError: If `input_data` is not of type `str` or `list`.
    """
```

**Назначение**:
Нормализует строку или список строк.

**Как работает функция**:
Функция принимает строку или список строк в качестве входных данных. Если входные данные являются списком, они объединяются в одну строку с пробелами между элементами. Затем из строки удаляются HTML-теги, переносы строк и специальные символы. После этого строка разбивается на слова, из которых формируется новая строка, где слова разделены одним пробелом. В завершение строка кодируется в формат UTF-8.

**Параметры**:
- `input_data` (str | list): Входные данные, которые могут быть строкой или списком строк.

**Возвращает**:
- `str`: Очищенная и нормализованная строка в формате UTF-8.

**Вызывает исключения**:
- `TypeError`: Если `input_data` не является строкой или списком.

**Примеры**:

```python
>>> normalize_string(['Hello', '  World!  '])
'Hello World!'
>>> normalize_string(' Пример строки <b>с HTML</b> ')
'Пример строки с HTML'
```

### `normalize_int`

```python
def normalize_int(input_data: Union[str, int, float, Decimal]) -> int:
    """Normalize data into an integer.

    Args:
        input_data (str | int | float | Decimal): Input data that can be a number or its string representation.

    Returns:
        int: Integer representation of the input.

    Example:
        >>> normalize_int('42')
        42
    """
```

**Назначение**:
Преобразует входные данные в целое число.

**Как работает функция**:
Функция принимает входные данные, которые могут быть числом или его строковым представлением, и пытается преобразовать их в целое число. Если входные данные являются типом `Decimal`, они сначала преобразуются в `int`. В противном случае они преобразуются во временный `float`, который потом преобразуется в `int`. Если преобразование не удаётся, возвращается исходное значение.

**Параметры**:
- `input_data` (str | int | float | Decimal): Входные данные, которые могут быть числом или его строковым представлением.

**Возвращает**:
- `int`: Целое представление входных данных.

**Примеры**:

```python
>>> normalize_int('42')
42
>>> normalize_int(3.14)
3
>>> normalize_int(Decimal('123.45'))
123
```

### `normalize_float`

```python
def normalize_float(value: Any) -> float | None:
    """Safely convert input values to float or list of floats.

    Args:
        value (Any): The input value to be converted. 
                     It can be a single value (number or string) or an iterable (list/tuple).

    Returns:
        float | List[float] | None: A float value, a list of floats, or None if conversion fails.

    Example:
        >>> normalize_float("3.14")
        3.14
        >>> normalize_float([1, '2.5', 3])
        [1.0, 2.5, 3.0]
    """
```

**Назначение**:
Преобразует входные данные в число с плавающей точкой или список чисел с плавающей точкой.

**Как работает функция**:
Функция принимает входные данные любого типа и пытается преобразовать их в число с плавающей точкой. Если входные данные являются списком или кортежем, функция рекурсивно применяет себя к каждому элементу и возвращает список чисел с плавающей точкой. Если преобразование не удаётся, возвращается `None`.

**Параметры**:
- `value` (Any): Входные данные для преобразования, которые могут быть числом, строкой или итерируемым объектом (список/кортеж).

**Возвращает**:
- `float | List[float] | None`: Число с плавающей точкой, список чисел с плавающей точкой или `None`, если преобразование не удалось.

**Примеры**:

```python
>>> normalize_float("3.14")
3.14
>>> normalize_float([1, '2.5', 3])
[1.0, 2.5, 3.0]
>>> normalize_float('abc')
0
```

### `normalize_sql_date`

```python
def normalize_sql_date(input_data: str) -> str:
    """Normalize data into SQL date format (YYYY-MM-DD).

    Args:
        input_data (str): Data that can represent a date (e.g., string, datetime object).

    Returns:
        str: Normalized date in SQL format (YYYY-MM-DD) or original value if conversion fails.

    Example:
        >>> normalize_sql_date('2024-12-06')
        '2024-12-06'
        >>> normalize_sql_date('12/06/2024')
        '2024-12-06'
    """
```

**Назначение**:
Преобразует входные данные в формат даты SQL (`YYYY-MM-DD`).

**Как работает функция**:
Функция принимает входные данные, которые могут быть строкой или объектом `datetime`, и пытается преобразовать их в формат даты SQL (`YYYY-MM-DD`). Если входные данные являются строкой, функция пытается распарсить дату, используя различные форматы (`%Y-%m-%d`, `%m/%d/%Y`, `%d/%m/%Y`). Если входные данные являются объектом `datetime`, функция преобразует их в строку в формате `YYYY-MM-DD`. Если преобразование не удаётся, возвращается исходное значение.

**Параметры**:
- `input_data` (str): Входные данные, которые могут быть представлены в виде даты (например, строка или объект `datetime`).

**Возвращает**:
- `str`: Нормализованная дата в формате SQL (`YYYY-MM-DD`) или исходное значение, если преобразование не удалось.

**Примеры**:

```python
>>> normalize_sql_date('2024-12-06')
'2024-12-06'
>>> normalize_sql_date('12/06/2024')
'2024-12-06'
>>> normalize_sql_date('06/12/2024')
'2024-12-06'
```

### `simplify_string`

```python
def simplify_string(input_str: str) -> str:
    """ Simplifies the input string by keeping only letters, digits, and replacing spaces with underscores.

    @param input_str: The string to be simplified.
    @return: The simplified string.
    @code
        example_str = "It's a test string with 'single quotes', numbers 123 and symbols!"
        simplified_str = StringNormalizer.simplify_string(example_str)
        print(simplified_str)  # Output: Its_a_test_string_with_single_quotes_numbers_123_and_symbols
    @endcode
    """
```

**Назначение**:
Упрощает входную строку, оставляя только буквы и цифры, заменяя пробелы на символы подчеркивания.

**Как работает функция**:
Функция принимает строку и удаляет из неё все символы, кроме букв, цифр и пробелов. Затем заменяет пробелы на символы подчеркивания. Наконец, удаляет последовательные символы подчеркивания, оставляя только один.

**Параметры**:
- `input_str` (str): Строка для упрощения.

**Возвращает**:
- `str`: Упрощенная строка.

**Примеры**:

```python
>>> simplify_string("It's a test string with 'single quotes', numbers 123 and symbols!")
'Its_a_test_string_with_single_quotes_numbers_123_and_symbols'
>>> simplify_string("  Hello   World!  ")
'Hello_World_'
```

### `remove_line_breaks`

```python
def remove_line_breaks(input_str: str) -> str:
    """Remove line breaks from the input string.

    Args:
        input_str (str): Input string.

    Returns:
        str: String without line breaks.
    """
```

**Назначение**:
Удаляет переносы строк из входной строки.

**Как работает функция**:
Функция принимает строку и заменяет все символы переноса строки (`\n`) и возврата каретки (`\r`) на пробелы. Затем удаляет начальные и конечные пробелы.

**Параметры**:
- `input_str` (str): Входная строка.

**Возвращает**:
- `str`: Строка без переносов строк.

**Примеры**:

```python
>>> remove_line_breaks("Hello\nWorld!\r")
'Hello World!'
>>> remove_line_breaks("  Hello\nWorld!  ")
'Hello World!'
```

### `remove_html_tags`

```python
def remove_html_tags(input_html: str) -> str:
    """Remove HTML tags from the input string.

    Args:
        input_html (str): Input HTML string.

    Returns:
        str: String without HTML tags.
    """
```

**Назначение**:
Удаляет HTML-теги из входной строки.

**Как работает функция**:
Функция принимает строку, содержащую HTML-теги, и удаляет все теги, используя регулярное выражение. Затем удаляет начальные и конечные пробелы.

**Параметры**:
- `input_html` (str): Входная HTML-строка.

**Возвращает**:
- `str`: Строка без HTML-тегов.

**Примеры**:

```python
>>> remove_html_tags("<b>Hello</b> <i>World</i>!")
'Hello World!'
>>> remove_html_tags("<p>Hello</p>")
'Hello'
```

### `remove_special_characters`

```python
def remove_special_characters(input_str: str | list, chars: list[str] = None) -> str | list:
    """Remove specified special characters from a string or list of strings.

    Args:
        input_str (str | list): Input string or list of strings.
        chars (list[str], optional): List of characters to remove. Defaults to None.

    Returns:
        str | list: Processed string or list with specified characters removed.
    """
```

**Назначение**:
Удаляет указанные специальные символы из строки или списка строк.

**Как работает функция**:
Функция принимает строку или список строк и удаляет из них указанные специальные символы. Если список символов для удаления не указан, используется список по умолчанию, содержащий символ `#`.

**Параметры**:
- `input_str` (str | list): Входная строка или список строк.
- `chars` (list[str], optional): Список символов для удаления. По умолчанию `None`.

**Возвращает**:
- `str | list`: Обработанная строка или список строк с удаленными символами.

**Примеры**:

```python
>>> remove_special_characters("Hello#World!", chars=['#', '!'])
'HelloWorld'
>>> remove_special_characters(['Hello#', 'World!'], chars=['#', '!'])
['Hello', 'World']
>>> remove_special_characters("Hello#World!")
'HelloWorld!'
```

### `normalize_sku`

```python
def normalize_sku(input_str: str) -> str:
    """
    Normalizes the SKU by removing specific Hebrew keywords and any non-alphanumeric characters, 
    except for hyphens.

    Args:
        input_str (str): The input string containing the SKU.

    Returns:
        str: The normalized SKU string.

    Example:
        >>> normalize_sku("מקט: 303235-A")
        '303235-A'
        >>> normalize_sku("מק\'\'ט: 12345-B")
        '12345-B'
        >>> normalize_sku("Some text מקט: 123-456-789 other text")
        'Some text 123-456-789 other text' # Important: It now keeps the hyphens and spaces between texts
    """
```

**Назначение**:
Нормализует SKU, удаляя определенные ключевые слова на иврите и все не буквенно-цифровые символы, кроме дефисов.

**Как работает функция**:
Функция принимает строку, содержащую SKU, и выполняет следующие действия:
1. Удаляет ключевые слова на иврите "מקט" и "מק''ט" (независимо от регистра).
2. Удаляет все не буквенно-цифровые символы, кроме дефисов.

**Параметры**:
- `input_str` (str): Входная строка, содержащая SKU.

**Возвращает**:
- `str`: Нормализованная строка SKU.

**Примеры**:

```python
>>> normalize_sku("מקט: 303235-A")
'303235-A'
>>> normalize_sku("מק''ט: 12345-B")
'12345-B'
>>> normalize_sku("Some text מקט: 123-456-789 other text")
'Some text 123-456-789 other text'
```