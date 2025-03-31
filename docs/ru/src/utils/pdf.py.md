# Модуль `src.utils.pdf`

## Обзор

Модуль предоставляет инструменты для преобразования HTML-контента или файлов в формат PDF с использованием различных библиотек, таких как `pdfkit`, `FPDF`, `WeasyPrint` и `xhtml2pdf`. Он также включает функции для конвертации PDF-файлов в HTML и сохранения данных словаря в PDF.

## Подробней

Этот модуль предназначен для обеспечения гибкости при работе с PDF-файлами, позволяя выбирать наиболее подходящую библиотеку в зависимости от конкретных требований проекта. Он включает функции для конвертации HTML в PDF, текста в PDF, а также PDF в HTML. Модуль также предоставляет возможность сохранения данных из словаря в PDF-файл.

## Классы

### `PDFUtils`

**Описание**: Класс, предоставляющий статические методы для работы с PDF-файлами.

**Как работает класс**:
Класс `PDFUtils` содержит несколько статических методов, каждый из которых использует определенную библиотеку для преобразования данных в PDF-формат или из PDF-формата. Методы охватывают различные подходы к генерации PDF, включая использование HTML, текста и данных из словаря.

**Методы**:
- `save_pdf_pdfkit`: Сохраняет HTML-контент или файл в PDF с использованием библиотеки `pdfkit`.
- `save_pdf_fpdf`: Сохраняет текст в PDF с использованием библиотеки `FPDF`.
- `save_pdf_weasyprint`: Сохраняет HTML-контент или файл в PDF с использованием библиотеки `WeasyPrint`.
- `save_pdf_xhtml2pdf`: Сохраняет HTML-контент или файл в PDF с использованием библиотеки `xhtml2pdf`.
- `html2pdf`: Конвертирует HTML-контент в PDF-файл, используя WeasyPrint.
- `pdf_to_html`: Конвертирует PDF-файл в HTML-файл.
- `dict2pdf`: Сохраняет данные словаря в PDF-файл.

## Функции

### `save_pdf_pdfkit`

```python
def save_pdf_pdfkit(data: str | Path, pdf_file: str | Path) -> bool:
    """
    Сохранить HTML-контент или файл в PDF с использованием библиотеки `pdfkit`.

    Args:
        data (str | Path): HTML-контент или путь к HTML-файлу.
        pdf_file (str | Path): Путь к сохраняемому PDF-файлу.

    Returns:
        bool: `True` если PDF успешно сохранен, иначе `False`.

    Raises:
        pdfkit.PDFKitError: Ошибка генерации PDF через `pdfkit`.
        OSError: Ошибка доступа к файлу.
    """
```

**Описание**: Сохраняет HTML-контент или HTML-файл в PDF, используя библиотеку `pdfkit`.

**Как работает функция**:
Функция `save_pdf_pdfkit` принимает HTML-контент (в виде строки) или путь к HTML-файлу, а также путь к PDF-файлу, в который нужно сохранить результат. Она использует библиотеку `pdfkit` для преобразования HTML в PDF. Функция проверяет наличие исполняемого файла `wkhtmltopdf.exe`, необходимого для работы `pdfkit`, и настраивает параметры конфигурации.

**Параметры**:
- `data` (str | Path): HTML-контент в виде строки или путь к HTML-файлу.
- `pdf_file` (str | Path): Путь к сохраняемому PDF-файлу.

**Возвращает**:
- `bool`: `True`, если PDF успешно сохранен, иначе `False`.

**Вызывает исключения**:
- `pdfkit.PDFKitError`: Если происходит ошибка во время генерации PDF с использованием `pdfkit`.
- `OSError`: Если возникают проблемы с доступом к файлам.

**Примеры**:

```python
from pathlib import Path
from src.utils.pdf import PDFUtils

html_content = "<html><body><h1>Hello, PDF!</h1></body></html>"
pdf_file = "example.pdf"
result = PDFUtils.save_pdf_pdfkit(html_content, pdf_file)
print(f"PDF saved successfully: {result}")

html_file_path = Path("example.html")
with open(html_file_path, "w", encoding="utf-8") as f:
    f.write(html_content)
pdf_file = "example_from_file.pdf"
result = PDFUtils.save_pdf_pdfkit(html_file_path, pdf_file)
print(f"PDF saved successfully from file: {result}")
```

### `save_pdf_fpdf`

```python
def save_pdf_fpdf(data: str, pdf_file: str | Path) -> bool:
    """
    Сохранить текст в PDF с использованием библиотеки FPDF.

    Args:
        data (str): Текст, который необходимо сохранить в PDF.
        pdf_file (str | Path): Путь к сохраняемому PDF-файлу.

    Returns:
        bool: `True`, если PDF успешно сохранен, иначе `False`.
    """
```

**Описание**: Сохраняет текст в PDF-файл с использованием библиотеки `FPDF`.

**Как работает функция**:
Функция `save_pdf_fpdf` принимает строку текста и путь к PDF-файлу. Она использует библиотеку `FPDF` для создания PDF-документа и добавления текста в него. Функция также выполняет настройку шрифтов, загружая их из JSON-файла конфигурации.

**Параметры**:
- `data` (str): Текст, который необходимо сохранить в PDF.
- `pdf_file` (str | Path): Путь к сохраняемому PDF-файлу.

**Возвращает**:
- `bool`: `True`, если PDF успешно сохранен, иначе `False`.

**Вызывает исключения**:
- `FileNotFoundError`: Если файл шрифта не найден.
- Любые исключения, которые могут возникнуть при работе с библиотекой `FPDF`.

**Примеры**:

```python
from src.utils.pdf import PDFUtils

text_data = "Hello, PDF! This is a test."
pdf_file = "example_fpdf.pdf"
result = PDFUtils.save_pdf_fpdf(text_data, pdf_file)
print(f"PDF saved successfully: {result}")
```

### `save_pdf_weasyprint`

```python
def save_pdf_weasyprint(data: str | Path, pdf_file: str | Path) -> bool:
    """
    Сохранить HTML-контент или файл в PDF с использованием библиотеки `WeasyPrint`.

    Args:
        data (str | Path): HTML-контент или путь к HTML-файлу.
        pdf_file (str | Path): Путь к сохраняемому PDF-файлу.

    Returns:
        bool: `True` если PDF успешно сохранен, иначе `False`.
    """
```

**Описание**: Сохраняет HTML-контент или HTML-файл в PDF, используя библиотеку `WeasyPrint`.

**Как работает функция**:
Функция `save_pdf_weasyprint` принимает HTML-контент (в виде строки) или путь к HTML-файлу, а также путь к PDF-файлу, в который нужно сохранить результат. Она использует библиотеку `WeasyPrint` для преобразования HTML в PDF.

**Параметры**:
- `data` (str | Path): HTML-контент в виде строки или путь к HTML-файлу.
- `pdf_file` (str | Path): Путь к сохраняемому PDF-файлу.

**Возвращает**:
- `bool`: `True`, если PDF успешно сохранен, иначе `False`.

**Вызывает исключения**:
- Любые исключения, которые могут возникнуть при работе с библиотекой `WeasyPrint`.

**Примеры**:

```python
from pathlib import Path
from src.utils.pdf import PDFUtils

html_content = "<html><body><h1>Hello, PDF!</h1></body></html>"
pdf_file = "example_weasyprint.pdf"
result = PDFUtils.save_pdf_weasyprint(html_content, pdf_file)
print(f"PDF saved successfully: {result}")

html_file_path = Path("example.html")
with open(html_file_path, "w", encoding="utf-8") as f:
    f.write(html_content)
pdf_file = "example_from_file_weasyprint.pdf"
result = PDFUtils.save_pdf_weasyprint(html_file_path, pdf_file)
print(f"PDF saved successfully from file: {result}")
```

### `save_pdf_xhtml2pdf`

```python
def save_pdf_xhtml2pdf(data: str | Path, pdf_file: str | Path) -> bool:
    """
    Сохранить HTML-контент или файл в PDF с использованием библиотеки `xhtml2pdf`.

    Args:
        data (str | Path): HTML-контент или путь к HTML-файлу.
        pdf_file (str | Path): Путь к сохраняемому PDF-файлу.

    Returns:
        bool: `True` если PDF успешно сохранен, иначе `False`.
    """
```

**Описание**: Сохраняет HTML-контент или HTML-файл в PDF, используя библиотеку `xhtml2pdf`.

**Как работает функция**:
Функция `save_pdf_xhtml2pdf` принимает HTML-контент (в виде строки) или путь к HTML-файлу, а также путь к PDF-файлу, в который нужно сохранить результат. Она использует библиотеку `xhtml2pdf` для преобразования HTML в PDF. Функция обрабатывает кодировку UTF-8 для обеспечения правильного отображения текста.

**Параметры**:
- `data` (str | Path): HTML-контент в виде строки или путь к HTML-файлу.
- `pdf_file` (str | Path): Путь к сохраняемому PDF-файлу.

**Возвращает**:
- `bool`: `True`, если PDF успешно сохранен, иначе `False`.

**Вызывает исключения**:
- Любые исключения, которые могут возникнуть при работе с библиотекой `xhtml2pdf`.

**Примеры**:

```python
from pathlib import Path
from src.utils.pdf import PDFUtils

html_content = "<html><body><h1>Hello, PDF!</h1></body></html>"
pdf_file = "example_xhtml2pdf.pdf"
result = PDFUtils.save_pdf_xhtml2pdf(html_content, pdf_file)
print(f"PDF saved successfully: {result}")

html_file_path = Path("example.html")
with open(html_file_path, "w", encoding="utf-8") as f:
    f.write(html_content)
pdf_file = "example_from_file_xhtml2pdf.pdf"
result = PDFUtils.save_pdf_xhtml2pdf(html_file_path, pdf_file)
print(f"PDF saved successfully from file: {result}")
```

### `html2pdf`

```python
def html2pdf(html_str: str, pdf_file: str | Path) -> bool | None:
    """Converts HTML content to a PDF file using WeasyPrint."""
```

**Описание**: Преобразует HTML-контент в PDF-файл, используя `WeasyPrint`.

**Как работает функция**:
Функция `html2pdf` принимает HTML-контент в виде строки и путь к PDF-файлу, в который нужно сохранить результат. Она использует библиотеку `WeasyPrint` для преобразования HTML в PDF.

**Параметры**:
- `html_str` (str): HTML-контент в виде строки.
- `pdf_file` (str | Path): Путь к сохраняемому PDF-файлу.

**Возвращает**:
- `bool | None`: `True`, если PDF успешно сохранен, иначе `None`.

**Вызывает исключения**:
- Отсутствуют явные исключения, но могут возникнуть исключения при работе с библиотекой `WeasyPrint`.

**Примеры**:

```python
from src.utils.pdf import PDFUtils

html_content = "<html><body><h1>Hello, PDF!</h1></body></html>"
pdf_file = "example_html2pdf.pdf"
result = PDFUtils.html2pdf(html_content, pdf_file)
print(f"PDF saved successfully: {result}")
```

### `pdf_to_html`

```python
def pdf_to_html(pdf_file: str | Path, html_file: str | Path) -> bool:
    """
    Конвертирует PDF-файл в HTML-файл.

    Args:
        pdf_file (str | Path): Путь к исходному PDF-файлу.
        html_file (str | Path): Путь к сохраняемому HTML-файлу.

    Returns:
        bool: `True`, если конвертация прошла успешно, иначе `False`.
    """
```

**Описание**: Конвертирует PDF-файл в HTML-файл.

**Как работает функция**:
Функция `pdf_to_html` принимает путь к PDF-файлу и путь к HTML-файлу, в который нужно сохранить результат. Она использует библиотеку `pdfminer.high_level` для извлечения текста из PDF и сохраняет его в HTML-файл.

**Параметры**:
- `pdf_file` (str | Path): Путь к исходному PDF-файлу.
- `html_file` (str | Path): Путь к сохраняемому HTML-файлу.

**Возвращает**:
- `bool`: `True`, если конвертация прошла успешно, иначе `False`.

**Вызывает исключения**:
- Любые исключения, которые могут возникнуть при работе с библиотекой `pdfminer.high_level`.

**Примеры**:

```python
from pathlib import Path
from src.utils.pdf import PDFUtils

pdf_file = "example.pdf"  # Укажите путь к существующему PDF-файлу
html_file = "example.html"
result = PDFUtils.pdf_to_html(pdf_file, html_file)
print(f"HTML saved successfully: {result}")
```

### `dict2pdf`

```python
def dict2pdf(data: Any, file_path: str | Path) -> None:
    """
    Save dictionary data to a PDF file.

    Args:
        data (dict | SimpleNamespace): The dictionary to convert to PDF.
        file_path (str | Path): Path to the output PDF file.
    """
```

**Описание**: Сохраняет данные словаря в PDF-файл.

**Как работает функция**:
Функция `dict2pdf` принимает словарь с данными и путь к PDF-файлу. Она использует библиотеку `reportlab.pdfgen` для создания PDF-документа и добавления данных из словаря в него. Функция перебирает элементы словаря и записывает их в PDF, создавая новые страницы при необходимости.

**Параметры**:
- `data` (dict | SimpleNamespace): Словарь с данными для сохранения в PDF.
- `file_path` (str | Path): Путь к сохраняемому PDF-файлу.

**Возвращает**:
- `None`: Функция ничего не возвращает.

**Вызывает исключения**:
- Отсутствуют явные исключения, но могут возникнуть исключения при работе с библиотекой `reportlab.pdfgen`.

**Примеры**:

```python
from src.utils.pdf import PDFUtils

data = {"name": "John Doe", "age": 30, "city": "New York"}
pdf_file = "example_dict2pdf.pdf"
PDFUtils.dict2pdf(data, pdf_file)
print(f"PDF saved successfully: {pdf_file}")
```