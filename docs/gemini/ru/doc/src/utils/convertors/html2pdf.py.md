# Модуль для работы с HTML

## Обзор

Модуль `html2pdf.py` предоставляет набор утилит для работы с HTML, включая функции для конвертации HTML в escape-последовательности, обратно в HTML, в словари и объекты SimpleNamespace. Также включает функции для конвертации HTML в PDF.

## Подробней

Этот модуль предоставляет инструменты для преобразования HTML в различные форматы данных, что может быть полезно для обработки и анализа HTML-контента. В частности, модуль позволяет преобразовывать HTML в PDF.

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

**Назначение**: Преобразует HTML в escape-последовательности.

**Как работает функция**:
Функция `html2escape` принимает HTML-код в качестве входной строки и преобразует его в escape-последовательности, заменяя символы, такие как `<`, `>`, `&`, кавычки и апострофы, на соответствующие escape-последовательности (`&lt;`, `&gt;`, `&amp;` и т.д.).

**Параметры**:
- `input_str` (str): HTML-код, который необходимо преобразовать.

**Возвращает**:
- `str`: HTML, преобразованный в escape-последовательности.

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
    return StringFormatter.unescape_html_tags(input_str)
```

**Назначение**: Преобразует escape-последовательности обратно в HTML.

**Как работает функция**:
Функция `escape2html` принимает строку с escape-последовательностями и преобразует их обратно в HTML, заменяя escape-последовательности, такие как `&lt;`, `&gt;`, `&amp;`, на соответствующие символы `<`, `>`, `&`.

**Параметры**:
- `input_str` (str): Строка с escape-последовательностями.

**Возвращает**:
- `str`: Escape-последовательности, преобразованные обратно в HTML.

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

**Назначение**: Преобразует HTML в словарь, где теги являются ключами, а содержимое - значениями.

**Как работает функция**:
Функция `html2dict` использует класс `HTMLToDictParser`, который наследуется от `HTMLParser`. Этот класс анализирует HTML-строку и извлекает теги и их содержимое. Метод `handle_starttag` устанавливает текущий тег, а метод `handle_data` извлекает данные из текущего тега и сохраняет их в словаре `result`.

**Параметры**:
- `html_str` (str): HTML-строка для преобразования.

**Возвращает**:
- `dict`: Словарь, где ключами являются HTML-теги, а значениями - их содержимое.

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
    html_dict = html2dict(html_str)
    return SimpleNamespace(**html_dict)
```

**Назначение**: Преобразует HTML в объект SimpleNamespace, где теги являются атрибутами, а содержимое - значениями.

**Как работает функция**:
Функция `html2ns` сначала преобразует HTML-строку в словарь с помощью функции `html2dict`, а затем использует этот словарь для создания объекта `SimpleNamespace`.

**Параметры**:
- `html_str` (str): HTML-строка для преобразования.

**Возвращает**:
- `SimpleNamespace`: Объект SimpleNamespace с HTML-тегами в качестве атрибутов и их содержимым в качестве значений.

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

**Назначение**: Преобразует HTML-контент в PDF-файл, используя библиотеку `WeasyPrint`.

**Как работает функция**:
Функция `html2pdf` принимает HTML-строку и путь к PDF-файлу. Она использует библиотеку `WeasyPrint` для преобразования HTML в PDF. В случае возникновения ошибки во время генерации PDF, она выводит сообщение об ошибке.

**Параметры**:
- `html_str` (str): HTML-контент в виде строки.
- `pdf_file` (str | Path): Путь к выходному PDF-файлу.

**Возвращает**:
- `bool | None`: Возвращает `True`, если генерация PDF прошла успешно, и `None` в противном случае.

**Вызывает исключения**:
- `Exception`: Если возникает ошибка во время генерации PDF.

**Примеры**:
```python
html = "<p>Hello, world!</p>"
pdf_file = "output.pdf"
result = html2pdf(html, pdf_file)
if result:
    print("PDF generated successfully")
else:
    print("PDF generation failed")