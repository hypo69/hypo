# Модуль для нормализации строк и числовых данных

## Обзор

Модуль предоставляет функции для нормализации строк, булевых значений, целых и чисел с плавающей точкой.
Он также содержит вспомогательные методы для обработки текста, включая удаление HTML-тегов и специальных символов.
Расположен в `src/utils/string/normalizer.py` и предназначен для подготовки данных к дальнейшей обработке,
обеспечивая единообразное представление строк и чисел.

## Подробнее

Этот модуль играет важную роль в проекте, обеспечивая стандартизацию входных данных.
Он используется для очистки и преобразования строк, чисел и булевых значений в удобный и консистентный формат.
Нормализация данных важна для обеспечения корректной работы различных компонентов системы,
таких как валидаторы, поисковые движки и инструменты анализа данных.

## Функции

### `normalize_boolean`

```python
def normalize_boolean(input_data: Any) -> bool:
    """
    Args:
        input_data (Any): Data that can represent a boolean (e.g., bool, string, integer).

    Returns:
        bool: Boolean representation of the input.

    Example:
        >>> normalize_boolean('yes')
        True
    """
```

**Описание**: Преобразует входные данные в булево значение. Поддерживает различные типы входных данных, такие как строки (например, 'yes', 'true', '1'), числа (1, 0) и булевы значения.

**Параметры**:
- `input_data` (Any): Входные данные, которые могут быть представлены как булево значение.

**Возвращает**:
- `bool`: Булево представление входных данных.

**Примеры**:
```python
normalize_boolean('yes')
```

### `normalize_string`

```python
def normalize_string(input_data: str | list) -> str:
    """
    Args:
        input_data (str | list): Input data that can be either a string or a list of strings.

    Returns:
        str: Cleaned and normalized string in UTF-8 encoded format.

    Raises:
        TypeError: If `input_data` is not of type `str` or `list`.

    Example:
        >>> normalize_string(['Hello', '  World!  '])
        'Hello World!'
    """
```

**Описание**: Нормализует строку или список строк. Выполняет очистку от HTML-тегов, лишних пробелов, специальных символов и приводит строку к кодировке UTF-8.

**Параметры**:
- `input_data` (str | list): Входная строка или список строк.

**Возвращает**:
- `str`: Очищенная и нормализованная строка в формате UTF-8.

**Вызывает исключения**:
- `TypeError`: Если `input_data` не является строкой или списком.

**Примеры**:
```python
normalize_string(['Hello', '  World!  '])
```

### `normalize_int`

```python
def normalize_int(input_data: Union[str, int, float, Decimal]) -> int:
    """
    Args:
        input_data (str | int | float | Decimal): Input data that can be a number or its string representation.

    Returns:
        int: Integer representation of the input.

    Example:
        >>> normalize_int('42')
        42
    """
```

**Описание**: Преобразует входные данные в целое число. Поддерживает различные типы входных данных, такие как строки, целые числа, числа с плавающей точкой и Decimal.

**Параметры**:
- `input_data` (str | int | float | Decimal): Входные данные, которые могут быть представлены как число или его строковое представление.

**Возвращает**:
- `int`: Целое представление входных данных.

**Примеры**:
```python
normalize_int('42')
```

### `normalize_float`

```python
def normalize_float(value: Any) -> float | None:
    """
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

**Описание**: Преобразует входные данные в число с плавающей точкой. Поддерживает различные типы входных данных, такие как строки и числа.

**Параметры**:
- `value` (Any): Входные данные, которые могут быть представлены как число с плавающей точкой. Может быть как одиночным значением, так и списком/кортежем.

**Возвращает**:
- `float | List[float] | None`: Представление входных данных в виде числа с плавающей точкой или список чисел с плавающей точкой. Возвращает `None`, если преобразование не удалось.

**Примеры**:
```python
normalize_float("3.14")
normalize_float([1, '2.5', 3])
```

### `normalize_sql_date`

```python
def normalize_sql_date(input_data: str) -> str:
    """
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

**Описание**: Преобразует входные данные в формат даты SQL (YYYY-MM-DD). Поддерживает различные типы входных данных, такие как строки и объекты datetime.

**Параметры**:
- `input_data` (str): Входные данные, которые могут быть представлены как дата.

**Возвращает**:
- `str`: Нормализованная дата в формате SQL (YYYY-MM-DD) или исходное значение, если преобразование не удалось.

**Примеры**:
```python
normalize_sql_date('2024-12-06')
normalize_sql_date('12/06/2024')
```

### `simplify_string`

```python
def simplify_string(input_str: str) -> str:
    """
    Args:
        input_str: The string to be simplified.

    Returns:
        The simplified string.
    """
```

**Описание**: Упрощает входную строку, оставляя только буквы и цифры, заменяя пробелы на подчеркивания.

**Параметры**:
- `input_str` (str): Строка для упрощения.

**Возвращает**:
- `str`: Упрощенная строка.

**Примеры**:
```python
example_str = "It's a test string with 'single quotes', numbers 123 and symbols!"
simplified_str = StringNormalizer.simplify_string(example_str)
print(simplified_str)  # Output: Its_a_test_string_with_single_quotes_numbers_123_and_symbols
```

### `remove_line_breaks`

```python
def remove_line_breaks(input_str: str) -> str:
    """
    Args:
        input_str (str): Input string.

    Returns:
        str: String without line breaks.
    """
```

**Описание**: Удаляет символы переноса строки из входной строки.

**Параметры**:
- `input_str` (str): Входная строка.

**Возвращает**:
- `str`: Строка без символов переноса строки.

### `remove_html_tags`

```python
def remove_html_tags(input_html: str) -> str:
    """
    Args:
        input_html (str): Input HTML string.

    Returns:
        str: String without HTML tags.
    """
```

**Описание**: Удаляет HTML-теги из входной строки.

**Параметры**:
- `input_html` (str): Входная HTML-строка.

**Возвращает**:
- `str`: Строка без HTML-тегов.

### `remove_special_characters`

```python
def remove_special_characters(input_str: str | list, chars: list[str] = None) -> str | list:
    """
    Args:
        input_str (str | list): Input string or list of strings.
        chars (list[str], optional): List of characters to remove. Defaults to None.

    Returns:
        str | list: Processed string or list with specified characters removed.
    """
```

**Описание**: Удаляет указанные специальные символы из строки или списка строк.

**Параметры**:
- `input_str` (str | list): Входная строка или список строк.
- `chars` (list[str], optional): Список символов для удаления. По умолчанию `None`.

**Возвращает**:
- `str | list`: Обработанная строка или список строк с удаленными символами.

### `normalize_sku`

```python
def normalize_sku(input_str: str) -> str:
    """
    Args:
        input_str (str): The input string containing the SKU.

    Returns:
        str: The normalized SKU string.

    Example:
        >>> normalize_sku("מקט: 303235-A")
        '303235-A'
        >>> normalize_sku("מק''ט: 12345-B")
        '12345-B'
        >>> normalize_sku("Some text מקט: 123-456-789 other text")
        'Some text 123-456-789 other text' # Important: It now keeps the hyphens and spaces between texts
    """
```

**Описание**: Нормализует SKU, удаляя специфичные ключевые слова на иврите и любые не-буквенно-цифровые символы, за исключением дефисов.

**Параметры**:
- `input_str` (str): Входная строка, содержащая SKU.

**Возвращает**:
- `str`: Нормализованная строка SKU.

**Примеры**:
```python
normalize_sku("מקט: 303235-A")
normalize_sku("מק''ט: 12345-B")
normalize_sku("Some text מקט: 123-456-789 other text")
```