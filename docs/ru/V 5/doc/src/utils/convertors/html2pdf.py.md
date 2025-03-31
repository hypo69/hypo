# Модуль `html2pdf`

## Обзор

Модуль `html2pdf` предоставляет набор утилит для преобразования HTML в различные форматы, включая экранированные последовательности, словари, объекты `SimpleNamespace` и PDF-файлы.

## Подробней

Этот модуль содержит функции для преобразования HTML в различные форматы данных, такие как экранированные строки, словари и объекты `SimpleNamespace`. Он также включает функцию для преобразования HTML-контента в PDF-файл с использованием библиотеки `weasyprint`. Модуль обрабатывает исключения, возникающие при преобразовании, и использует логирование для записи ошибок.

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
    return StringFormatter.escape_html_tags(input_str)
```

**Описание**: Преобразует HTML в экранированные последовательности.

**Как работает функция**:
Функция `html2escape` принимает строку HTML-кода в качестве входных данных и использует метод `escape_html_tags` из класса `StringFormatter` для преобразования HTML-тегов в экранированные последовательности. Это полезно для безопасного отображения HTML-кода в текстовом формате, например, в веб-интерфейсах или при передаче данных.

**Параметры**:
- `input_str` (str): Строка HTML-кода, которую необходимо преобразовать.

**Возвращает**:
- `str`: Строка, содержащая HTML-код, преобразованный в экранированные последовательности.

**Примеры**:

```python
html = "<p>Hello, world!</p>"
result = html2escape(html)
print(result)
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
    return StringFormatter.unescape_html_tags(input_str)
```

**Описание**: Преобразует экранированные последовательности обратно в HTML.

**Как работает функция**:
Функция `escape2html` принимает строку с экранированными последовательностями в качестве входных данных и использует метод `unescape_html_tags` из класса `StringFormatter` для преобразования экранированных последовательностей обратно в HTML-теги. Это полезно для восстановления HTML-кода из экранированного представления.

**Параметры**:
- `input_str` (str): Строка, содержащая экранированные последовательности.

**Возвращает**:
- `str`: Строка, содержащая HTML-код, полученный из экранированных последовательностей.

**Примеры**:

```python
escaped = "&lt;p&gt;Hello, world!</p>"
result = escape2html(escaped)
print(result)
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

    parser = HTMLToDictParser()
    parser.feed(html_str)
    return parser.result
```

**Описание**: Преобразует HTML в словарь, где теги являются ключами, а содержимое - значениями.

**Как работает функция**:
Функция `html2dict` принимает строку HTML-кода в качестве входных данных и использует внутренний класс `HTMLToDictParser`, который наследуется от `HTMLParser`, для разбора HTML-кода. Класс `HTMLToDictParser` переопределяет методы `handle_starttag`, `handle_endtag` и `handle_data` для обработки HTML-тегов и содержимого. Функция создает экземпляр парсера, передает ему HTML-код для обработки и возвращает словарь, содержащий теги и их содержимое.

**Параметры**:
- `html_str` (str): Строка HTML-кода, которую необходимо преобразовать.

**Возвращает**:
- `dict`: Словарь, где ключами являются HTML-теги, а значениями - их содержимое.

**Примеры**:

```python
html = "<p>Hello</p><a href='link'>World</a>"
result = html2dict(html)
print(result)
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
    html_dict = html2dict(html_str)
    return SimpleNamespace(**html_dict)
```

**Описание**: Преобразует HTML в объект `SimpleNamespace`, где теги являются атрибутами, а содержимое - значениями.

**Как работает функция**:
Функция `html2ns` принимает строку HTML-кода в качестве входных данных и использует функцию `html2dict` для преобразования HTML-кода в словарь. Затем она создает объект `SimpleNamespace` из полученного словаря, где ключи словаря становятся атрибутами объекта `SimpleNamespace`, а значения словаря становятся значениями атрибутов.

**Параметры**:
- `html_str` (str): Строка HTML-кода, которую необходимо преобразовать.

**Возвращает**:
- `SimpleNamespace`: Объект `SimpleNamespace` с HTML-тегами в качестве атрибутов и их содержимым в качестве значений.

**Примеры**:

```python
html = "<p>Hello</p><a href='link'>World</a>"
result = html2ns(html)
print(result.p)
print(result.a)
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

**Описание**: Преобразует HTML-контент в PDF-файл с использованием библиотеки `WeasyPrint`.

**Как работает функция**:
Функция `html2pdf` принимает строку HTML-кода и путь к PDF-файлу в качестве входных данных. Она использует библиотеку `WeasyPrint` для преобразования HTML-кода в PDF-файл. В случае возникновения ошибки во время преобразования, она выводит сообщение об ошибке.

**Параметры**:
- `html_str` (str): Строка HTML-кода, которую необходимо преобразовать в PDF.
- `pdf_file` (str | Path): Путь к PDF-файлу, в который будет записан результат.

**Возвращает**:
- `bool | None`: Возвращает `True`, если преобразование прошло успешно, и `None` в случае ошибки.

**Вызывает исключения**:
- `Exception`: Возникает при ошибке в процессе генерации PDF.

**Примеры**:

```python
html_content = "<p>Hello, world!</p>"
pdf_file_path = "output.pdf"
result = html2pdf(html_content, pdf_file_path)
if result:
    print("PDF generated successfully!")
else:
    print("Failed to generate PDF.")
```