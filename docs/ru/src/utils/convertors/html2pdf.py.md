# Модуль для конвертации HTML

## Обзор

Модуль `html2pdf.py` содержит утилиты для конвертации HTML в различные форматы, такие как escape-последовательности, словари и объекты SimpleNamespace. Также модуль предоставляет функциональность для конвертации HTML в PDF.

## Подробней

Этот модуль предоставляет набор функций для преобразования HTML в различные форматы данных. Включает функции для экранирования и деэкранирования HTML-тегов, преобразования HTML в словари и объекты SimpleNamespace, а также для генерации PDF-файлов из HTML. Модуль использует сторонние библиотеки, такие как `xhtml2pdf` и `weasyprint`, для конвертации HTML в PDF.

## Функции

### `html2escape`

```python
def html2escape(input_str: str) -> str:
    """
    Convert HTML to escape sequences.

    Args:
        input_str (str): The HTML code.

    Returns:
        str: HTML converted into escape sequences.

    Example:
        >>> html = "<p>Hello, world!</p>"
        >>> result = html2escape(html)
        >>> print(result)
        &lt;p&gt;Hello, world!&lt;/p&gt;
    """
    ...
```

**Назначение**: Преобразует HTML в escape-последовательности.

**Параметры**:
- `input_str` (str): HTML-код для преобразования.

**Возвращает**:
- `str`: HTML, преобразованный в escape-последовательности.

**Как работает функция**:
1. Функция `html2escape` принимает строку `input_str`, содержащую HTML-код.
2. Использует метод `StringFormatter.escape_html_tags(input_str)` для преобразования HTML в escape-последовательности.
3. Возвращает строку, содержащую HTML, преобразованный в escape-последовательности.

```ascii
Начало
   ↓
Преобразование HTML в escape-последовательности
   ↓
Конец
```

**Примеры**:

```python
html = "<p>Hello, world!</p>"
result = html2escape(html)
print(result)  # Вывод: &lt;p&gt;Hello, world!&lt;/p&gt;
```

### `escape2html`

```python
def escape2html(input_str: str) -> str:
    """
    Convert escape sequences to HTML.

    Args:
        input_str (str): The string with escape sequences.

    Returns:
        str: The escape sequences converted back into HTML.

    Example:
        >>> escaped = "&lt;p&gt;Hello, world!&lt;/p&gt;"
        >>> result = escape2html(escaped)
        >>> print(result)
        <p>Hello, world!</p>
    """
    ...
```

**Назначение**: Преобразует escape-последовательности обратно в HTML.

**Параметры**:
- `input_str` (str): Строка с escape-последовательностями.

**Возвращает**:
- `str`: Escape-последовательности, преобразованные обратно в HTML.

**Как работает функция**:
1. Функция `escape2html` принимает строку `input_str`, содержащую escape-последовательности.
2. Использует метод `StringFormatter.unescape_html_tags(input_str)` для преобразования escape-последовательностей обратно в HTML.
3. Возвращает строку, содержащую HTML.

```ascii
Начало
   ↓
Преобразование escape-последовательностей в HTML
   ↓
Конец
```

**Примеры**:

```python
escaped = "&lt;p&gt;Hello, world!&lt;/p&gt;"
result = escape2html(escaped)
print(result)  # Вывод: <p>Hello, world!</p>
```

### `html2dict`

```python
def html2dict(html_str: str) -> Dict[str, str]:
    """
    Convert HTML to a dictionary where tags are keys and content are values.

    Args:
        html_str (str): The HTML string to convert.

    Returns:
        dict: A dictionary with HTML tags as keys and their content as values.

    Example:
        >>> html = "<p>Hello</p><a href='link'>World</a>"
        >>> result = html2dict(html)
        >>> print(result)
        {'p': 'Hello', 'a': 'World'}
    """
    ...
```

**Назначение**: Преобразует HTML в словарь, где теги являются ключами, а содержимое - значениями.

**Параметры**:
- `html_str` (str): HTML-строка для преобразования.

**Возвращает**:
- `dict`: Словарь с HTML-тегами в качестве ключей и их содержимым в качестве значений.

**Как работает функция**:
1. Функция `html2dict` принимает строку `html_str`, содержащую HTML-код.
2. Определяет внутренний класс `HTMLToDictParser`, который наследует `HTMLParser` и переопределяет методы `handle_starttag`, `handle_endtag` и `handle_data`.
3. Создает экземпляр парсера `HTMLToDictParser`.
4. Вызывает метод `feed()` парсера, чтобы обработать HTML-строку.
5. Возвращает словарь, содержащий HTML-теги в качестве ключей и их содержимое в качестве значений.

```ascii
Начало
   ↓
Создание парсера HTMLToDictParser
   ↓
Обработка HTML-строки парсером
   ↓
Формирование словаря: тег -> содержимое
   ↓
Конец
```

**Внутренние функции**:

#### `HTMLToDictParser`

```python
class HTMLToDictParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.result = {}
        self.current_tag = None

    def handle_starttag(self, tag, attrs):
        self.current_tag = tag

    def handle_endtag(self, tag):
        self.current_tag = None

    def handle_data(self, data):
        if self.current_tag:
            self.result[self.current_tag] = data.strip()
```

**Описание**: Класс `HTMLToDictParser` наследует `HTMLParser` и используется для парсинга HTML и извлечения тегов и их содержимого.

**Атрибуты**:
- `result` (dict): Словарь для хранения результатов парсинга.
- `current_tag` (str): Текущий обрабатываемый тег.

**Методы**:
- `handle_starttag(self, tag, attrs)`: Обрабатывает начало тега, устанавливая текущий тег.
- `handle_endtag(self, tag)`: Обрабатывает конец тега, сбрасывая текущий тег.
- `handle_data(self, data)`: Обрабатывает данные между тегами, добавляя их в словарь результатов.

**Примеры**:

```python
html = "<p>Hello</p><a href='link'>World</a>"
result = html2dict(html)
print(result)  # Вывод: {'p': 'Hello', 'a': 'World'}
```

### `html2ns`

```python
def html2ns(html_str: str) -> SimpleNamespace:
    """
    Convert HTML to a SimpleNamespace object where tags are attributes and content are values.

    Args:
        html_str (str): The HTML string to convert.

    Returns:
        SimpleNamespace: A SimpleNamespace object with HTML tags as attributes and their content as values.

    Example:
        >>> html = "<p>Hello</p><a href='link'>World</a>"
        >>> result = html2ns(html)
        >>> print(result.p)
        Hello
        >>> print(result.a)
        World
    """
    ...
```

**Назначение**: Преобразует HTML в объект `SimpleNamespace`, где теги являются атрибутами, а содержимое - значениями.

**Параметры**:
- `html_str` (str): HTML-строка для преобразования.

**Возвращает**:
- `SimpleNamespace`: Объект `SimpleNamespace` с HTML-тегами в качестве атрибутов и их содержимым в качестве значений.

**Как работает функция**:
1. Функция `html2ns` принимает строку `html_str`, содержащую HTML-код.
2. Вызывает функцию `html2dict()` для преобразования HTML в словарь.
3. Создает объект `SimpleNamespace` из полученного словаря.
4. Возвращает объект `SimpleNamespace`.

```ascii
Начало
   ↓
Преобразование HTML в словарь (html2dict)
   ↓
Создание объекта SimpleNamespace из словаря
   ↓
Конец
```

**Примеры**:

```python
html = "<p>Hello</p><a href='link'>World</a>"
result = html2ns(html)
print(result.p)  # Вывод: Hello
print(result.a)  # Вывод: World
```

### `html2pdf`

```python
def html2pdf(html_str: str, pdf_file: str | Path) -> bool | None:
    """Converts HTML content to a PDF file using WeasyPrint."""
    try:
        HTML(string=html_str).write_pdf(pdf_file)
        return True
    except Exception as e:
        print(f"Error during PDF generation: {e}")
        return
```

**Назначение**: Преобразует HTML-контент в PDF-файл с использованием библиотеки `WeasyPrint`.

**Параметры**:
- `html_str` (str): HTML-контент в виде строки.
- `pdf_file` (str | Path): Путь к выходному PDF-файлу.

**Возвращает**:
- `bool | None`: Возвращает `True`, если генерация PDF прошла успешно; `None` в противном случае.

**Вызывает исключения**:
- `Exception`: Возникает при ошибке во время генерации PDF.

**Как работает функция**:
1. Функция `html2pdf` принимает HTML-контент в виде строки (`html_str`) и путь к выходному PDF-файлу (`pdf_file`).
2. Использует библиотеку `WeasyPrint` для конвертации HTML в PDF.
3. В блоке `try` пытается создать PDF-файл из HTML-контента и сохранить его по указанному пути.
4. Если PDF-файл успешно создан, функция возвращает `True`.
5. Если во время создания PDF возникает исключение, функция перехватывает его, логирует ошибку и возвращает `None`.

```ascii
Начало
   ↓
Попытка конвертации HTML в PDF с использованием WeasyPrint
   ↓
Успех?
  /   \
 Да    Нет
  ↓     ↓
Возврат True  Логирование ошибки
           ↓
      Возврат None
   ↓
Конец
```

**Примеры**:

```python
html_content = "<p>Hello, world!</p>"
pdf_filepath = "output.pdf"
result = html2pdf(html_content, pdf_filepath)
if result:
    print("PDF файл успешно создан")
else:
    print("Во время создания PDF возникла ошибка")