# Модуль `html2pdf`

## Обзор

Модуль `html2pdf` предоставляет утилиты для преобразования HTML в различные форматы, включая экранированные последовательности, словари, пространства имен и PDF-файлы. Он содержит функции для преобразования HTML в экранированные последовательности и обратно, преобразования HTML в словари и объекты SimpleNamespace, а также для преобразования HTML в PDF-файлы.

## Подробнее

Этот модуль предназначен для обработки и преобразования HTML-контента. Он включает функции для экранирования и восстановления HTML-тегов, преобразования HTML в структурированные данные (словари и пространства имен), а также для генерации PDF-файлов на основе HTML. Модуль использует сторонние библиотеки, такие как `xhtml2pdf` и `weasyprint`, для преобразования HTML в PDF.

## Функции

### `html2escape`

```python
def html2escape(input_str: str) -> str:
    """
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
```

**Описание**: Преобразует HTML в экранированные последовательности.

**Параметры**:
- `input_str` (str): HTML-код для преобразования.

**Возвращает**:
- `str`: HTML, преобразованный в экранированные последовательности.

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
```

**Описание**: Преобразует экранированные последовательности обратно в HTML.

**Параметры**:
- `input_str` (str): Строка с экранированными последовательностями.

**Возвращает**:
- `str`: Экранированные последовательности, преобразованные обратно в HTML.

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
```

**Описание**: Преобразует HTML в словарь, где теги являются ключами, а содержимое - значениями.

**Параметры**:
- `html_str` (str): HTML-строка для преобразования.

**Возвращает**:
- `dict`: Словарь, где ключи - HTML-теги, а значения - содержимое тегов.

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
```

**Описание**: Преобразует HTML в объект SimpleNamespace, где теги являются атрибутами, а содержимое - значениями.

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

**Описание**: Преобразует HTML-контент в PDF-файл с использованием WeasyPrint.

**Параметры**:
- `html_str` (str): HTML-контент в виде строки.
- `pdf_file` (str | Path): Путь к выходному PDF-файлу.

**Возвращает**:
- `bool | None`: Возвращает `True`, если генерация PDF прошла успешно; `None` в противном случае.

**Вызывает исключения**:
- `Exception`: Выводит информацию об ошибке в случае неудачи при генерации PDF.

**Примеры**:
```python
html_content = "<p>Hello, world!</p>"
pdf_file_path = "output.pdf"
result = html2pdf(html_content, pdf_file_path)
if result:
    print(f"PDF успешно создан: {pdf_file_path}")
else:
    print("Не удалось создать PDF.")