# Модуль для конвертации HTML

## Обзор

Модуль `html2pdf.py` предоставляет набор утилит для конвертации HTML в различные форматы, включая экранированные последовательности, словари, объекты SimpleNamespace и PDF-файлы. Он включает функции для экранирования и деэкранирования HTML-тегов, преобразования HTML в словари и объекты SimpleNamespace, а также для конвертации HTML в PDF с использованием библиотеки `weasyprint`.

## Подробнее

Этот модуль содержит функции для работы с HTML, включая преобразование HTML в экранированные последовательности, преобразование экранированных последовательностей обратно в HTML, преобразование HTML в словари и объекты SimpleNamespace, а также преобразование HTML в PDF. Он использует библиотеки `html.parser`, `xhtml2pdf` и `weasyprint` для выполнения этих задач.
Внутри проекта модуль используется для преобразования  различной информации в удобный формат. Например, для генерации отчетов в формате PDF.

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

**Назначение**: Преобразует HTML в экранированные последовательности.

**Параметры**:
- `input_str` (str): HTML-код для преобразования.

**Возвращает**:
- `str`: HTML, преобразованный в экранированные последовательности.

**Как работает функция**:
1. Функция принимает HTML-код в качестве входных данных.
2. Она вызывает метод `StringFormatter.escape_html_tags(input_str)` для преобразования HTML в экранированные последовательности.
3. Возвращает преобразованный HTML.

```ascii
HTML-код --> Преобразование в экранированные последовательности --> Экранированный HTML
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

**Назначение**: Преобразует экранированные последовательности обратно в HTML.

**Параметры**:
- `input_str` (str): Строка с экранированными последовательностями.

**Возвращает**:
- `str`: Экранированные последовательности, преобразованные обратно в HTML.

**Как работает функция**:
1. Функция принимает строку с экранированными последовательностями в качестве входных данных.
2. Она вызывает метод `StringFormatter.unescape_html_tags(input_str)` для преобразования экранированных последовательностей обратно в HTML.
3. Возвращает преобразованный HTML.

```ascii
Строка с экранированными последовательностями --> Преобразование в HTML --> HTML
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
- `dict`: Словарь, где HTML-теги являются ключами, а их содержимое - значениями.

**Как работает функция**:
1. Функция определяет внутренний класс `HTMLToDictParser`, который наследуется от `HTMLParser`.
2. Класс `HTMLToDictParser` переопределяет методы `handle_starttag`, `handle_endtag` и `handle_data` для извлечения тегов и содержимого.
3. Создается экземпляр `HTMLToDictParser`.
4. HTML-строка передается в метод `feed` парсера.
5. Результат парсинга (словарь) возвращается.

**Внутренние функции**:

#### `HTMLToDictParser`
```python
class HTMLToDictParser(HTMLParser):
    """
    Преобразует HTML в словарь, где теги являются ключами, а содержимое - значениями.

    Inherits:
        HTMLParser: Наследуется от класса HTMLParser.

    Attributes:
        result (dict): Словарь для хранения результатов парсинга.
        current_tag (str): Текущий обрабатываемый тег.

    Methods:
        handle_starttag(tag, attrs): Обрабатывает начало тега.
        handle_endtag(tag): Обрабатывает конец тега.
        handle_data(data): Обрабатывает данные внутри тега.
    """

    def __init__(self):
        """
        Инициализирует парсер HTML.
        """
        super().__init__()
        self.result = {}
        self.current_tag = None

    def handle_starttag(self, tag, attrs):
        """
        Обрабатывает начало тега.

        Args:
            tag (str): Тег HTML.
            attrs (list): Атрибуты тега.
        """
        self.current_tag = tag

    def handle_endtag(self, tag):
        """
        Обрабатывает конец тега.

        Args:
            tag (str): Тег HTML.
        """
        self.current_tag = None

    def handle_data(self, data):
        """
        Обрабатывает данные внутри тега.

        Args:
            data (str): Данные внутри тега.
        """
        if self.current_tag:
            self.result[self.current_tag] = data.strip()
```

```ascii
HTML-строка --> Создание HTMLToDictParser --> Парсинг HTML --> Словарь (тег: содержимое)
```

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

**Назначение**: Преобразует HTML в объект SimpleNamespace, где теги являются атрибутами, а содержимое - значениями.

**Параметры**:
- `html_str` (str): HTML-строка для преобразования.

**Возвращает**:
- `SimpleNamespace`: Объект SimpleNamespace, где HTML-теги являются атрибутами, а их содержимое - значениями.

**Как работает функция**:
1. Функция вызывает функцию `html2dict` для преобразования HTML в словарь.
2. Создается объект `SimpleNamespace` из словаря.
3. Возвращается объект `SimpleNamespace`.

```ascii
HTML-строка --> Преобразование в словарь (html2dict) --> Создание SimpleNamespace --> SimpleNamespace
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
    ...
```

**Назначение**: Преобразует HTML-контент в PDF-файл с использованием библиотеки `weasyprint`.

**Параметры**:
- `html_str` (str): HTML-контент в виде строки.
- `pdf_file` (str | Path): Путь к выходному PDF-файлу.

**Возвращает**:
- `bool | None`: Возвращает `True`, если генерация PDF прошла успешно; `None` в противном случае.

**Вызывает исключения**:
- `Exception`: Если во время генерации PDF произошла ошибка.

**Как работает функция**:
1. Пытается преобразовать HTML-контент в PDF-файл, используя библиотеку `weasyprint`.
2. В случае успеха возвращает `True`.
3. Если во время генерации PDF произошла ошибка, печатает сообщение об ошибке и возвращает `None`.

```ascii
HTML-строка --> Генерация PDF (weasyprint) --> PDF-файл
```

**Примеры**:

```python
html = "<p>Hello, world!</p>"
pdf_file = "example.pdf"
result = html2pdf(html, pdf_file)
if result:
    print("PDF generated successfully!")
else:
    print("PDF generation failed.")