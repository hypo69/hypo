# Модуль `html2pdf`

## Обзор

Модуль `html2pdf` предоставляет утилиты для конвертации HTML в различные форматы, такие как escape-последовательности, словари и объекты SimpleNamespace. Он также включает функциональность для конвертации HTML в PDF.

## Подробней

Этот модуль предназначен для обработки и преобразования HTML-контента. Он предоставляет функции для экранирования и восстановления HTML-тегов, преобразования HTML в словари и объекты SimpleNamespace, а также для генерации PDF-файлов из HTML. Модуль использует библиотеки `html.parser`, `xhtml2pdf` и `weasyprint` для выполнения этих задач. Расположение модуля в структуре проекта: `hypotez/src/utils/convertors/html2pdf.py`.

## Функции

### `html2escape`

```python
def html2escape(input_str: str) -> str:
    """
    Args:
        input_str (str): HTML-код.

    Returns:
        str: HTML, преобразованный в escape-последовательности.

    Example:
        >>> html = "<p>Hello, world!</p>"
        >>> result = html2escape(html)
        >>> print(result)
        &lt;p&gt;Hello, world!&lt;/p&gt;

     **Как работает функция**:
     Функция `html2escape` принимает строку `input_str`, содержащую HTML-код, и преобразует HTML-теги в соответствующие escape-последовательности.
     Это делается с использованием метода `StringFormatter.escape_html_tags(input_str)`.
     В результате все HTML-теги, такие как `<p>`, `<div>` и т.д., заменяются на их escape-эквиваленты, например, `&lt;p&gt;`, `&lt;div&gt;`.
     Это полезно для безопасного отображения HTML-кода в текстовом формате, например, в веб-интерфейсе или лог-файле.
    """
```

**Описание**: Преобразует HTML в escape-последовательности.

**Параметры**:
- `input_str` (str): HTML-код.

**Возвращает**:
- `str`: HTML, преобразованный в escape-последовательности.

**Примеры**:
```python
>>> html = "<p>Hello, world!</p>"
>>> result = html2escape(html)
>>> print(result)
&lt;p&gt;Hello, world!&lt;/p&gt;
```

### `escape2html`

```python
def escape2html(input_str: str) -> str:
    """
    Args:
        input_str (str): Строка с escape-последовательностями.

    Returns:
        str: Escape-последовательности, преобразованные обратно в HTML.

    Example:
        >>> escaped = "&lt;p&gt;Hello, world!&lt;/p&gt;"
        >>> result = escape2html(escaped)
        >>> print(result)
        <p>Hello, world!</p>

    **Как работает функция**:
     Функция `escape2html` принимает строку `input_str`, содержащую escape-последовательности, и преобразует их обратно в HTML-теги.
     Это делается с использованием метода `StringFormatter.unescape_html_tags(input_str)`.
     В результате escape-последовательности, такие как `&lt;p&gt;`, `&lt;div&gt;`, заменяются на соответствующие HTML-теги, например, `<p>`, `<div>`.
     Это полезно для восстановления HTML-кода из его escape-представления, например, при отображении данных, полученных из базы данных или другого источника, где HTML-теги были экранированы.
    """
```

**Описание**: Преобразует escape-последовательности в HTML.

**Параметры**:
- `input_str` (str): Строка с escape-последовательностями.

**Возвращает**:
- `str`: Escape-последовательности, преобразованные обратно в HTML.

**Примеры**:
```python
>>> escaped = "&lt;p&gt;Hello, world!</p>"
>>> result = escape2html(escaped)
>>> print(result)
<p>Hello, world!</p>
```

### `html2dict`

```python
def html2dict(html_str: str) -> Dict[str, str]:
    """
    Args:
        html_str (str): HTML-строка для конвертации.

    Returns:
        dict: Словарь, где ключи - HTML-теги, а значения - содержимое тегов.

    Example:
        >>> html = "<p>Hello</p><a href='link'>World</a>"
        >>> result = html2dict(html)
        >>> print(result)
        {'p': 'Hello', 'a': 'World'}

    **Как работает функция**:
     Функция `html2dict` преобразует HTML-строку в словарь, где ключами являются HTML-теги, а значениями - содержимое этих тегов.
     Для этого используется класс `HTMLToDictParser`, который наследуется от `HTMLParser`.
     Класс `HTMLToDictParser` переопределяет методы `handle_starttag`, `handle_endtag` и `handle_data` для обработки HTML-тегов и их содержимого.
     Метод `handle_starttag` вызывается при обнаружении открывающего тега, `handle_endtag` - при обнаружении закрывающего тега, а `handle_data` - при обнаружении содержимого тега.
     В результате формируется словарь, где ключами являются теги, а значениями - их содержимое.
    """
```

**Описание**: Преобразует HTML в словарь, где теги - ключи, а содержимое - значения.

**Параметры**:
- `html_str` (str): HTML-строка для конвертации.

**Возвращает**:
- `dict`: Словарь, где ключи - HTML-теги, а значения - содержимое тегов.

**Примеры**:
```python
>>> html = "<p>Hello</p><a href='link'>World</a>"
>>> result = html2dict(html)
>>> print(result)
{'p': 'Hello', 'a': 'World'}
```

### `html2ns`

```python
def html2ns(html_str: str) -> SimpleNamespace:
    """
    Args:
        html_str (str): HTML-строка для конвертации.

    Returns:
        SimpleNamespace: Объект SimpleNamespace, где атрибуты - HTML-теги, а значения - содержимое тегов.

    Example:
        >>> html = "<p>Hello</p><a href='link'>World</a>"
        >>> result = html2ns(html)
        >>> print(result.p)
        Hello
        >>> print(result.a)
        World

     **Как работает функция**:
     Функция `html2ns` преобразует HTML-строку в объект `SimpleNamespace`, где теги HTML становятся атрибутами объекта, а содержимое тегов - значениями этих атрибутов.
     Функция использует `html2dict` для преобразования HTML в словарь, а затем создает объект `SimpleNamespace` из этого словаря.
     Это позволяет обращаться к содержимому HTML-тегов как к атрибутам объекта, что упрощает доступ к данным.
    """
```

**Описание**: Преобразует HTML в объект SimpleNamespace, где теги - атрибуты, а содержимое - значения.

**Параметры**:
- `html_str` (str): HTML-строка для конвертации.

**Возвращает**:
- `SimpleNamespace`: Объект SimpleNamespace, где атрибуты - HTML-теги, а значения - содержимое тегов.

**Примеры**:
```python
>>> html = "<p>Hello</p><a href='link'>World</a>"
>>> result = html2ns(html)
>>> print(result.p)
Hello
>>> print(result.a)
World
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
- `Exception`: Возникает при ошибке во время генерации PDF.

**Как работает функция**:
     Функция `html2pdf` преобразует HTML-контент в PDF-файл, используя библиотеку WeasyPrint.
     Она принимает HTML-строку `html_str` и путь к PDF-файлу `pdf_file` в качестве аргументов.
     Внутри функции HTML-строка передается в конструктор `HTML` из WeasyPrint, а затем вызывается метод `write_pdf` для записи PDF-файла.
     Если в процессе возникают какие-либо исключения, они перехватываются, и функция возвращает `None`.
     В случае успешной генерации PDF функция возвращает `True`.