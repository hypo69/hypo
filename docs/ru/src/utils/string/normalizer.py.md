# Модуль `normalizer`

## Обзор

Модуль `normalizer` предоставляет функции для нормализации строк, булевых значений, целых чисел и чисел с плавающей точкой. Он также содержит вспомогательные методы для обработки текста, включая удаление HTML-тегов и специальных символов.

## Подробней

Этот модуль предназначен для стандартизации данных, поступающих из различных источников, чтобы обеспечить их консистентность и пригодность для дальнейшей обработки. Он полезен, когда необходимо привести данные к определенному формату перед сохранением в базе данных или использованием в других частях приложения.

## Классы

В данном модуле классы отсутствуют.

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

**Описание**:
Преобразует входные данные в логический тип. Функция анализирует входные данные различных типов (строки, числа, логические значения) и возвращает соответствующее логическое значение.

**Как работает функция**:
1. Сохраняет исходное значение входных данных.
2. Проверяет, является ли входное значение уже логическим. Если да, возвращает его без изменений.
3. Преобразует входное значение в строку, приводит к нижнему регистру и удаляет пробелы в начале и конце строки.
4. Проверяет, соответствует ли строка одному из значений, представляющих `True` (`'true'`, `'1'`, `'yes'`, `'y'`, `'on'`, `True`, `1`).
5. Если строка не соответствует значениям `True`, проверяет, соответствует ли она одному из значений, представляющих `False` (`'false'`, `'0'`, `'no'`, `'n'`, `'off'`, `False`, `0`).
6. В случае ошибки логирования возвращает исходное значение.

**Параметры**:
- `input_data` (Any): Входные данные, которые могут быть представлены в виде логического значения (например, логический тип, строка, целое число).

**Возвращает**:
- `bool`: Логическое представление входных данных.

**Вызывает исключения**:
- Отсутствуют.

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

**Описание**:
Нормализует строку или список строк. Функция выполняет очистку и нормализацию входных данных, удаляя HTML-теги, переносы строк и специальные символы, а также приводит строку к кодировке UTF-8.

**Как работает функция**:
1. Проверяет, является ли входное значение пустым. Если да, возвращает пустую строку.
2. Сохраняет исходное значение входных данных для возврата в случае ошибки.
3. Проверяет, является ли входное значение строкой или списком. Если нет, вызывает исключение `TypeError`.
4. Если входное значение является списком, объединяет элементы списка в одну строку, разделяя их пробелами.
5. Удаляет HTML-теги, переносы строк и специальные символы из строки.
6. Удаляет лишние пробелы и приводит строку к кодировке UTF-8.
7. В случае ошибки возвращает исходное значение.

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

**Описание**:
Преобразует входные данные в целое число. Функция анализирует входные данные различных типов (строки, целые числа, числа с плавающей точкой, Decimal) и возвращает их целочисленное представление.

**Как работает функция**:
1. Сохраняет исходное значение входных данных.
2. Проверяет, является ли входное значение типом `Decimal`. Если да, преобразует его в целое число.
3. Преобразует входное значение в число с плавающей точкой, а затем в целое число.
4. В случае ошибки логирования возвращает исходное значение.

**Параметры**:
- `input_data` (str | int | float | Decimal): Входные данные, которые могут быть числом или его строковым представлением.

**Возвращает**:
- `int`: Целочисленное представление входных данных.

**Вызывает исключения**:
- Отсутствуют.

**Примеры**:

```python
>>> normalize_int('42')
42
>>> normalize_int(42.5)
42
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

**Описание**:
Преобразует входные данные в число с плавающей точкой или список чисел с плавающей точкой. Функция анализирует входные данные различных типов (числа, строки, списки, кортежи) и возвращает их представление в виде числа с плавающей точкой.

**Как работает функция**:
1. Сохраняет исходное значение входных данных.
2. Проверяет, является ли входное значение пустым. Если да, возвращает 0.
3. Проверяет, является ли входное значение списком или кортежем. Если да, рекурсивно вызывает `normalize_float` для каждого элемента и возвращает список чисел с плавающей точкой.
4. Пытается преобразовать входное значение в число с плавающей точкой.
5. В случае ошибки логирования возвращает исходное значение.

**Параметры**:
- `value` (Any): Входные данные для преобразования. Может быть числом, строкой, списком или кортежем.

**Возвращает**:
- `float | List[float] | None`: Число с плавающей точкой, список чисел с плавающей точкой или `None`, если преобразование не удалось.

**Вызывает исключения**:
- Отсутствуют.

**Примеры**:

```python
>>> normalize_float("3.14")
3.14
>>> normalize_float([1, '2.5', 3])
[1.0, 2.5, 3.0]
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

**Описание**:
Преобразует входные данные в формат даты SQL (YYYY-MM-DD). Функция анализирует входные данные различных типов (строки, объекты datetime) и возвращает дату в формате SQL.

**Как работает функция**:
1. Сохраняет исходное значение входных данных.
2. Проверяет, является ли входное значение строкой. Если да, пытается распарсить дату из строки, используя различные форматы (`'%Y-%m-%d'`, `'%m/%d/%Y'`, `'%d/%m/%Y'`).
3. Если входные данные уже являются объектом `datetime`, преобразует их в формат даты SQL.
4. В случае ошибки логирования возвращает исходное значение.

**Параметры**:
- `input_data` (str): Входные данные, которые могут быть представлены в виде даты (например, строка, объект datetime).

**Возвращает**:
- `str`: Нормализованная дата в формате SQL (YYYY-MM-DD) или исходное значение, если преобразование не удалось.

**Вызывает исключения**:
- Отсутствуют.

**Примеры**:

```python
>>> normalize_sql_date('2024-12-06')
'2024-12-06'
>>> normalize_sql_date('12/06/2024')
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

**Описание**:
Упрощает входную строку, оставляя только буквы, цифры и заменяя пробелы на подчеркивания.

**Как работает функция**:
1. Удаляет все символы, кроме букв, цифр и пробелов.
2. Заменяет пробелы на подчеркивания.
3. Удаляет последовательные подчеркивания.
4. В случае ошибки логирования возвращает исходное значение.

**Параметры**:
- `input_str` (str): Строка для упрощения.

**Возвращает**:
- `str`: Упрощенная строка.

**Вызывает исключения**:
- Отсутствуют.

**Примеры**:

```python
>>> simplify_string("It's a test string with 'single quotes', numbers 123 and symbols!")
"Its_a_test_string_with_single_quotes_numbers_123_and_symbols"
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

**Описание**:
Удаляет переносы строк из входной строки.

**Как работает функция**:
1. Заменяет символы `\n` и `\r` на пробелы.
2. Удаляет пробелы в начале и конце строки.

**Параметры**:
- `input_str` (str): Входная строка.

**Возвращает**:
- `str`: Строка без переносов строк.

**Вызывает исключения**:
- Отсутствуют.

**Примеры**:

```python
>>> remove_line_breaks("Hello\nWorld!")
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

**Описание**:
Удаляет HTML-теги из входной строки.

**Как работает функция**:
1. Использует регулярное выражение для удаления всех HTML-тегов.
2. Удаляет пробелы в начале и конце строки.

**Параметры**:
- `input_html` (str): Входная HTML-строка.

**Возвращает**:
- `str`: Строка без HTML-тегов.

**Вызывает исключения**:
- Отсутствуют.

**Примеры**:

```python
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

**Описание**:
Удаляет указанные специальные символы из строки или списка строк.

**Как работает функция**:
1. Если список символов для удаления не указан, используется список по умолчанию (`['#']`).
2. Формирует регулярное выражение на основе списка символов для удаления.
3. Если входные данные являются списком, применяет регулярное выражение к каждому элементу списка.
4. Если входные данные являются строкой, применяет регулярное выражение к строке.

**Параметры**:
- `input_str` (str | list): Входная строка или список строк.
- `chars` (list[str], optional): Список символов для удаления. По умолчанию `None`.

**Возвращает**:
- `str | list`: Обработанная строка или список с удаленными символами.

**Вызывает исключения**:
- Отсутствуют.

**Примеры**:

```python
>>> remove_special_characters("Hello#World!", chars=['#', '!'])
'HelloWorld'
>>> remove_special_characters(['Hello#', 'World!'], chars=['#', '!'])
['Hello', 'World']
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

**Описание**:
Нормализует артикул (SKU), удаляя определенные ключевые слова на иврите и все не-буквенно-цифровые символы, кроме дефисов.

**Как работает функция**:
1. Удаляет ключевые слова на иврите (`מקט`, `מק''ט`).
2. Удаляет все не-буквенно-цифровые символы, кроме дефисов.
3. В случае ошибки логирования возвращает исходное значение.

**Параметры**:
- `input_str` (str): Входная строка, содержащая артикул.

**Возвращает**:
- `str`: Нормализованная строка артикула.

**Вызывает исключения**:
- Отсутствуют.

**Примеры**:

```python
>>> normalize_sku("מקט: 303235-A")
'303235-A'
>>> normalize_sku("מק\'\'ט: 12345-B")
'12345-B'
>>> normalize_sku("Some text מקט: 123-456-789 other text")
'Some text 123-456-789 other text'
```