# Модуль для нормализации строк и числовых данных

## Обзор

Модуль предоставляет функции для нормализации строк, булевых значений, целых чисел и чисел с плавающей точкой. Он также содержит вспомогательные методы для обработки текста, включая удаление HTML-тегов и специальных символов.

## Подробней

Этот модуль предназначен для предобработки данных, поступающих из различных источников, чтобы привести их к единообразному и удобному для дальнейшей обработки виду. Он используется для очистки строк от лишних символов, приведения числовых значений к нужным типам и форматам, а также для нормализации булевых значений.

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

**Назначение**: Преобразует входные данные в булево значение.

**Параметры**:
- `input_data` (Any): Данные, которые могут быть представлены как булево значение (например, bool, строка, целое число).

**Возвращает**:
- `bool`: Булево представление входных данных.

**Как работает функция**:

1. Функция сначала проверяет, является ли входное значение уже булевым типом. Если да, оно возвращается без изменений.
2. Если входное значение не является булевым, оно преобразуется в строку, удаляются начальные и конечные пробелы, и приводится к нижнему регистру.
3. Затем функция проверяет, входит ли полученная строка в множество значений, которые считаются истинными (`'true'`, `'1'`, `'yes'`, `'y'`, `'on'`, `True`, `1`). Если да, возвращается `True`.
4. Аналогично, функция проверяет, входит ли строка в множество значений, которые считаются ложными (`'false'`, `'0'`, `'no'`, `'n'`, `'off'`, `False`, `0`). Если да, возвращается `False`.
5. Если строка не соответствует ни одному из известных булевых значений, в лог записывается отладочное сообщение, и возвращается исходное значение без изменений.
6. Если в процессе преобразования возникает исключение, оно логируется как ошибка, и возвращается исходное значение.

**Примеры**:

```python
normalize_boolean('yes')  # Возвращает: True
normalize_boolean('No')   # Возвращает: False
normalize_boolean(1)      # Возвращает: True
normalize_boolean(0)      # Возвращает: False
normalize_boolean('unknown') # Возвращает: 'unknown'
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

**Назначение**: Нормализует строку или список строк.

**Параметры**:
- `input_data` (str | list): Входные данные, которые могут быть строкой или списком строк.

**Возвращает**:
- `str`: Очищенная и нормализованная строка в формате UTF-8.

**Вызывает исключения**:
- `TypeError`: Если `input_data` не является строкой или списком.

**Как работает функция**:

1. Функция проверяет, является ли входное значение пустой строкой. Если это так, она возвращает пустую строку.
2. Сохраняет исходное значение во временную переменную `original_input`.
3. Затем функция проверяет, является ли входное значение строкой или списком. Если нет, вызывается исключение `TypeError`.
4. Если входное значение является списком, он объединяется в одну строку, разделенную пробелами.
5. Далее, строка проходит через следующие этапы очистки:
   - Удаляются HTML-теги с использованием функции `remove_html_tags`.
   - Удаляются переносы строк с использованием функции `remove_line_breaks`.
   - Удаляются специальные символы с использованием функции `remove_special_characters`.
   - Нормализуются пробелы, удаляются лишние пробелы между словами и в начале/конце строки.
6. Наконец, строка кодируется в формат UTF-8 и декодируется обратно для обеспечения совместимости.
7. Если в процессе нормализации возникает исключение, оно логируется как ошибка, и возвращается исходное значение, также закодированное в UTF-8.

**Внутренние функции**:
   - `remove_html_tags(input_html: str) -> str:`:
      **Назначение**: Удаляет HTML-теги из входной строки.

      **Параметры**:
         - `input_html (str)`: Входная HTML-строка.

      **Возвращает**:
         - `str`: Строка без HTML-тегов.

   - `remove_line_breaks(input_str: str) -> str`:
      **Назначение**: Удаляет переносы строк из входной строки.

      **Параметры**:
         - `input_str (str)`: Входная строка.

      **Возвращает**:
         - `str`: Строка без переносов строк.

   - `remove_special_characters(input_str: str | list, chars: list[str] = None) -> str | list`:
      **Назначение**: Удаляет указанные специальные символы из строки или списка строк.

      **Параметры**:
         - `input_str (str | list)`: Входная строка или список строк.
         - `chars (list[str], optional)`: Список символов для удаления. По умолчанию `None`.

      **Возвращает**:
         - `str | list`: Обработанная строка или список с удаленными указанными символами.

**Примеры**:

```python
normalize_string(['Hello', '  World!  '])  # Возвращает: 'Hello World!'
normalize_string(' Пример строки <b>с HTML</b> ')  # Возвращает: 'Пример строки с HTML'
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

**Назначение**: Преобразует входные данные в целое число.

**Параметры**:
- `input_data` (str | int | float | Decimal): Входные данные, которые могут быть числом или его строковым представлением.

**Возвращает**:
- `int`: Целочисленное представление входных данных.

**Как работает функция**:

1. Функция сначала сохраняет исходное значение во временную переменную `original_input`.
2. Затем функция пытается преобразовать входное значение в целое число. Если входное значение является типом `Decimal`, оно сначала преобразуется в `int`. В противном случае входное значение сначала преобразуется в `float`, а затем в `int`.
3. Если в процессе преобразования возникает исключение (`ValueError`, `TypeError`, `InvalidOperation`), оно логируется как ошибка, и возвращается исходное значение без изменений.

**Примеры**:

```python
normalize_int('42')   # Возвращает: 42
normalize_int(3.14)  # Возвращает: 3
normalize_int(Decimal('123.45')) # Возвращает: 123
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

**Назначение**: Безопасное преобразование входных значений в тип float или список float.

**Параметры**:
- `value` (Any): Входное значение для преобразования. Это может быть одиночное значение (число или строка) или итерируемый объект (список/кортеж).

**Возвращает**:
- `float | List[float] | None`: Значение типа float, список значений типа float или None, если преобразование не удалось.

**Как работает функция**:

1. Функция сохраняет исходное значение во временную переменную `original_value`.
2. Если входное значение пустое, функция возвращает 0.
3. Если входное значение является списком или кортежем, функция применяет `normalize_float` к каждому элементу списка/кортежа и возвращает список значений float, исключая те, которые не удалось преобразовать (None).
4. Если входное значение не является списком или кортежем, функция пытается преобразовать его в тип float.
5. Если в процессе преобразования возникает исключение (`ValueError`, `TypeError`), оно логируется как предупреждение, и возвращается исходное значение без изменений.

**Примеры**:

```python
normalize_float("3.14")  # Возвращает: 3.14
normalize_float([1, '2.5', 3])  # Возвращает: [1.0, 2.5, 3.0]
normalize_float('abc') # Возвращает: "abc"
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

**Назначение**: Преобразует входные данные в формат даты SQL (YYYY-MM-DD).

**Параметры**:
- `input_data` (str): Данные, которые могут быть представлены как дата (например, строка, объект datetime).

**Возвращает**:
- `str`: Нормализованная дата в формате SQL (YYYY-MM-DD) или исходное значение, если преобразование не удалось.

**Как работает функция**:

1. Функция сохраняет исходное значение во временную переменную `original_input`.
2. Если входные данные - строка, функция пытается распарсить дату из строки, используя различные форматы (`'%Y-%m-%d'`, `'%m/%d/%Y'`, `'%d/%m/%Y'`).
3. Если входные данные уже являются объектом `datetime`, функция преобразует их в дату и форматирует в формат ISO (`YYYY-MM-DD`).
4. Если в процессе преобразования возникает исключение, оно логируется как ошибка, и возвращается исходное значение без изменений.
5. Если строка не соответствует ни одному из известных форматов даты, в лог записывается отладочное сообщение, и возвращается исходное значение без изменений.

**Примеры**:

```python
normalize_sql_date('2024-12-06')  # Возвращает: '2024-12-06'
normalize_sql_date('12/06/2024')  # Возвращает: '2024-12-06'
normalize_sql_date('invalid date') # Возвращает: 'invalid date'
```

### `simplify_string`

```python
def simplify_string(input_str: str) -> str:
    """ Simplifies the input string by keeping only letters, digits, and replacing spaces with underscores.

    @param input_str: The string to be simplified.
    @return: The simplified string.
    @code
        example_str = "It\'s a test string with \'single quotes\', numbers 123 and symbols!"
        simplified_str = StringNormalizer.simplify_string(example_str)
        print(simplified_str)  # Output: Its_a_test_string_with_single_quotes_numbers_123_and_symbols
    @endcode
    """
```

**Назначение**: Упрощает входную строку, оставляя только буквы и цифры, заменяя пробелы на символы подчеркивания.

**Параметры**:
- `input_str` (str): Строка для упрощения.

**Возвращает**:
- `str`: Упрощенная строка.

**Как работает функция**:

1. Функция удаляет из входной строки все символы, кроме букв, цифр и пробелов.
2. Заменяет пробелы на символы подчеркивания.
3. Удаляет последовательные символы подчеркивания, оставляя только один.
4. Если в процессе упрощения возникает исключение, оно логируется как ошибка, и возвращается исходная строка.

**Примеры**:

```python
example_str = "It's a test string with 'single quotes', numbers 123 and symbols!"
simplified_str = simplify_string(example_str)
print(simplified_str)  # Output: Its_a_test_string_with_single_quotes_numbers_123_and_symbols
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

**Назначение**: Удаляет переносы строк из входной строки.

**Параметры**:
- `input_str` (str): Входная строка.

**Возвращает**:
- `str`: Строка без переносов строк.

**Как работает функция**:

1.  Функция заменяет все символы новой строки (`\n`) и возврата каретки (`\r`) на пробелы.
2.  Удаляет начальные и конечные пробелы.

**Примеры**:

```python
remove_line_breaks("Hello\nWorld!\r")  # Возвращает: 'Hello World!'
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

**Назначение**: Удаляет HTML-теги из входной строки.

**Параметры**:
- `input_html` (str): Входная HTML-строка.

**Возвращает**:
- `str`: Строка без HTML-тегов.

**Как работает функция**:

1. Использует регулярное выражение для поиска и удаления всех HTML-тегов из входной строки.
2. Удаляет начальные и конечные пробелы.

**Примеры**:

```python
remove_html_tags(" Пример строки <b>с HTML</b> ")  # Возвращает: 'Пример строки с HTML'
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

**Назначение**: Удаляет указанные специальные символы из строки или списка строк.

**Параметры**:
- `input_str` (str | list): Входная строка или список строк.
- `chars` (list[str], optional): Список символов для удаления. По умолчанию `None`.

**Возвращает**:
- `str | list`: Обработанная строка или список с удаленными указанными символами.

**Как работает функция**:

1. Если список символов для удаления не указан, используется список по умолчанию, содержащий символ `#`.
2. Формируется регулярное выражение для поиска указанных символов.
3. Если входные данные - список, функция применяет регулярное выражение к каждой строке в списке.
4. Если входные данные - строка, функция применяет регулярное выражение к строке.

**Примеры**:

```python
remove_special_characters("Hello#World!", chars=['#', '!'])  # Возвращает: 'HelloWorld'
remove_special_characters(['Hello#', 'World!'], chars=['#', '!'])  # Возвращает: ['Hello', 'World']
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

**Назначение**: Нормализует SKU (Stock Keeping Unit), удаляя определенные ключевые слова на иврите и все не буквенно-цифровые символы, за исключением дефисов.

**Параметры**:
- `input_str` (str): Входная строка, содержащая SKU.

**Возвращает**:
- `str`: Нормализованная строка SKU.

**Как работает функция**:

1. Функция пытается удалить ключевые слова на иврите ("מקט" и "מק''ט") из входной строки, используя регулярное выражение с игнорированием регистра.
2. Затем функция удаляет все не буквенно-цифровые символы, за исключением дефисов, используя регулярное выражение.
3. Если в процессе нормализации возникает исключение, оно логируется как ошибка с информацией об исключении, и возвращается исходная строка.

**Примеры**:

```python
normalize_sku("מקט: 303235-A")  # Возвращает: '303235-A'
normalize_sku("מק''ט: 12345-B")  # Возвращает: '12345-B'
normalize_sku("Some text מקט: 123-456-789 other text")  # Возвращает: 'Some text 123-456-789 other text'
```