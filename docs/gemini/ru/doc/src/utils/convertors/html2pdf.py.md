# Модуль `html2pdf`

## Обзор

Модуль `html2pdf` предоставляет набор утилит для конвертации HTML в различные форматы, включая экранированные последовательности, словари, объекты `SimpleNamespace` и PDF-файлы. Модуль содержит функции для преобразования HTML в PDF с использованием библиотеки `WeasyPrint`, а также вспомогательные функции для обработки HTML и CSS.

## Подробней

Этот модуль предоставляет инструменты для работы с HTML-контентом, позволяя преобразовывать его в различные представления. Он включает функции для экранирования и восстановления HTML-тегов, преобразования HTML в словари и объекты `SimpleNamespace`, а также для генерации PDF-файлов из HTML. Модуль использует библиотеки `xhtml2pdf` и `weasyprint` для конвертации в PDF.

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

**Назначение**: Преобразует HTML-код в экранированные последовательности.

**Параметры**:
- `input_str` (str): HTML-код, который необходимо преобразовать.

**Возвращает**:
- `str`: HTML, преобразованный в экранированные последовательности.

**Как работает функция**:
1. Функция `html2escape` принимает строку `input_str`, содержащую HTML-код.
2. Вызывает метод `StringFormatter.escape_html_tags(input_str)` для преобразования HTML-кода в экранированные последовательности.
3. Возвращает экранированную строку.

```
    HTML-код
     |
     StringFormatter.escape_html_tags(input_str)
     |
    Экранированная строка
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
    return StringFormatter.unescape_html_tags(input_str)
```

**Назначение**: Преобразует экранированные последовательности обратно в HTML-код.

**Параметры**:
- `input_str` (str): Строка с экранированными последовательностями.

**Возвращает**:
- `str`: HTML-код, полученный из экранированных последовательностей.

**Как работает функция**:
1. Функция `escape2html` принимает строку `input_str`, содержащую экранированные последовательности.
2. Вызывает метод `StringFormatter.unescape_html_tags(input_str)` для преобразования экранированных последовательностей в HTML-код.
3. Возвращает HTML-код.

```
    Экранированная строка
     |
     StringFormatter.unescape_html_tags(input_str)
     |
    HTML-код
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

**Назначение**: Преобразует HTML-код в словарь, где ключами являются теги, а значениями — содержимое тегов.

**Параметры**:
- `html_str` (str): HTML-код для преобразования.

**Возвращает**:
- `dict`: Словарь, где ключи — это HTML-теги, а значения — содержимое этих тегов.

**Как работает функция**:
1. Функция `html2dict` определяет внутренний класс `HTMLToDictParser`, который наследуется от `HTMLParser`. Этот класс переопределяет методы `handle_starttag`, `handle_endtag` и `handle_data` для обработки HTML-тегов и данных.
2. Создается экземпляр `HTMLToDictParser`.
3. HTML-код передается в метод `feed` парсера.
4. Метод `handle_starttag` устанавливает текущий тег.
5. Метод `handle_endtag` сбрасывает текущий тег.
6. Метод `handle_data` извлекает данные из текущего тега и добавляет их в словарь `result`.
7. Функция возвращает словарь `result`.

**Внутренние функции**:

### `HTMLToDictParser`
**Описание**: Класс `HTMLToDictParser` наследуется от `HTMLParser` и используется для разбора HTML-кода и преобразования его в словарь.

**Методы**:

- `__init__(self)`: Инициализирует экземпляр класса, устанавливая атрибуты `result` (словарь для хранения результатов) и `current_tag` (текущий тег).
- `handle_starttag(self, tag, attrs)`: Обрабатывает начало тега, устанавливая `current_tag` равным текущему тегу.
- `handle_endtag(self, tag)`: Обрабатывает конец тега, сбрасывая `current_tag` в `None`.
- `handle_data(self, data)`: Обрабатывает данные, находящиеся между тегами. Если `current_tag` установлен, добавляет данные (очищенные от пробелов) в словарь `result` с ключом `current_tag`.

```
    HTML-код
     |
     Создание экземпляра HTMLToDictParser
     |
     parser.feed(html_str)
     |
     Разбор HTML-кода и заполнение словаря result
     |
    Словарь {тег: содержимое}
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
    html_dict = html2dict(html_str)
    return SimpleNamespace(**html_dict)
```

**Назначение**: Преобразует HTML-код в объект `SimpleNamespace`, где теги становятся атрибутами, а содержимое тегов — значениями атрибутов.

**Параметры**:
- `html_str` (str): HTML-код для преобразования.

**Возвращает**:
- `SimpleNamespace`: Объект `SimpleNamespace` с атрибутами, соответствующими HTML-тегам и их содержимому.

**Как работает функция**:
1. Функция `html2ns` вызывает функцию `html2dict` для преобразования HTML-кода в словарь.
2. Создает объект `SimpleNamespace` из полученного словаря, используя оператор `**` для передачи словаря в качестве именованных аргументов.
3. Возвращает объект `SimpleNamespace`.

```
    HTML-код
     |
     html2dict(html_str)
     |
    Словарь {тег: содержимое}
     |
     SimpleNamespace(**html_dict)
     |
    Объект SimpleNamespace
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

**Назначение**: Преобразует HTML-код в PDF-файл с использованием библиотеки `WeasyPrint`.

**Параметры**:
- `html_str` (str): HTML-код для преобразования.
- `pdf_file` (str | Path): Путь к выходному PDF-файлу.

**Возвращает**:
- `bool | None`: `True`, если PDF-файл успешно создан, `None` в случае ошибки.

**Вызывает исключения**:
- `Exception`: Если возникает ошибка при генерации PDF-файла.

**Как работает функция**:
1. Функция `html2pdf` принимает HTML-код и путь к PDF-файлу.
2. Пытается создать PDF-файл, используя библиотеку `WeasyPrint`.
3. В случае успеха возвращает `True`.
4. В случае ошибки логирует ошибку и возвращает `None`.

```
    HTML-код, путь к PDF-файлу
     |
     HTML(string=html_str).write_pdf(pdf_file)
     |
    Создание PDF-файла
     |
    Успех: True, Ошибка: None
```

**Примеры**:

```python
html = "<p>Hello, world!</p>"
pdf_file = "example.pdf"
result = html2pdf(html, pdf_file)
if result:
    print("PDF файл успешно создан.")
else:
    print("Ошибка при создании PDF файла.")