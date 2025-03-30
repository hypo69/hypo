# Модуль `src.utils.pdf`

## Обзор

Модуль `src.utils.pdf` предназначен для преобразования HTML-контента или файлов в PDF с использованием различных библиотек. Он предоставляет статические методы класса `PDFUtils` для выполнения этих преобразований, поддерживая `pdfkit`, `FPDF`, `WeasyPrint` и `xhtml2pdf`.

## Подробней

Этот модуль предоставляет набор инструментов для работы с PDF-файлами, позволяя сохранять HTML-контент, текст и даже данные из словарей в формате PDF. Он включает поддержку различных библиотек для генерации PDF, что обеспечивает гибкость и возможность выбора наиболее подходящего инструмента в зависимости от требований проекта. Модуль также содержит функции для конвертации PDF в HTML.

## Классы

### `PDFUtils`

**Описание**: Класс для работы с PDF-файлами, предоставляющий методы для сохранения HTML-контента в PDF с использованием различных библиотек.

**Методы**:
- `save_pdf_pdfkit`: Сохраняет HTML-контент или файл в PDF с использованием библиотеки `pdfkit`.
- `save_pdf_fpdf`: Сохраняет текст в PDF с использованием библиотеки `FPDF`.
- `save_pdf_weasyprint`: Сохраняет HTML-контент или файл в PDF с использованием библиотеки `WeasyPrint`.
- `save_pdf_xhtml2pdf`: Сохраняет HTML-контент или файл в PDF с использованием библиотеки `xhtml2pdf`.
- `html2pdf`: Конвертирует HTML-контент в PDF-файл с использованием `WeasyPrint`.
- `pdf_to_html`: Конвертирует PDF-файл в HTML-файл.
- `dict2pdf`: Сохраняет данные из словаря в PDF-файл.

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

**Описание**: Сохраняет HTML-контент или файл в PDF с использованием библиотеки `pdfkit`.

**Параметры**:
- `data` (str | Path): HTML-контент или путь к HTML-файлу.
- `pdf_file` (str | Path): Путь к сохраняемому PDF-файлу.

**Возвращает**:
- `bool`: `True`, если PDF успешно сохранен, иначе `False`.

**Вызывает исключения**:
- `pdfkit.PDFKitError`: Ошибка генерации PDF через `pdfkit`.
- `OSError`: Ошибка доступа к файлу.

**Примеры**:

```python
from pathlib import Path
from src.utils.pdf import PDFUtils

# Пример сохранения HTML-контента в PDF
html_content = "<html><body><h1>Hello, PDF!</h1></body></html>"
pdf_file = "example.pdf"
result = PDFUtils.save_pdf_pdfkit(html_content, pdf_file)
print(f"PDF сохранен: {result}")

# Пример сохранения HTML-файла в PDF
html_file = Path("example.html")  # Убедитесь, что файл существует
pdf_file = "example_from_file.pdf"
result = PDFUtils.save_pdf_pdfkit(html_file, pdf_file)
print(f"PDF сохранен из файла: {result}")
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

**Описание**: Сохраняет текст в PDF с использованием библиотеки `FPDF`.

**Параметры**:
- `data` (str): Текст, который необходимо сохранить в PDF.
- `pdf_file` (str | Path): Путь к сохраняемому PDF-файлу.

**Возвращает**:
- `bool`: `True`, если PDF успешно сохранен, иначе `False`.

**Примеры**:

```python
from src.utils.pdf import PDFUtils

# Пример сохранения текста в PDF
text_data = "Hello, PDF generated with FPDF!"
pdf_file = "example_fpdf.pdf"
result = PDFUtils.save_pdf_fpdf(text_data, pdf_file)
print(f"PDF сохранен с помощью FPDF: {result}")
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

**Описание**: Сохраняет HTML-контент или файл в PDF с использованием библиотеки `WeasyPrint`.

**Параметры**:
- `data` (str | Path): HTML-контент или путь к HTML-файлу.
- `pdf_file` (str | Path): Путь к сохраняемому PDF-файлу.

**Возвращает**:
- `bool`: `True`, если PDF успешно сохранен, иначе `False`.

**Примеры**:

```python
from pathlib import Path
from src.utils.pdf import PDFUtils

# Пример сохранения HTML-контента в PDF
html_content = "<html><body><h1>Hello, PDF with WeasyPrint!</h1></body></html>"
pdf_file = "example_weasyprint.pdf"
result = PDFUtils.save_pdf_weasyprint(html_content, pdf_file)
print(f"PDF сохранен с помощью WeasyPrint: {result}")

# Пример сохранения HTML-файла в PDF
html_file = Path("example.html")  # Убедитесь, что файл существует
pdf_file = "example_from_file_weasyprint.pdf"
result = PDFUtils.save_pdf_weasyprint(html_file, pdf_file)
print(f"PDF сохранен из файла с помощью WeasyPrint: {result}")
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

**Описание**: Сохраняет HTML-контент или файл в PDF с использованием библиотеки `xhtml2pdf`.

**Параметры**:
- `data` (str | Path): HTML-контент или путь к HTML-файлу.
- `pdf_file` (str | Path): Путь к сохраняемому PDF-файлу.

**Возвращает**:
- `bool`: `True`, если PDF успешно сохранен, иначе `False`.

**Примеры**:

```python
from pathlib import Path
from src.utils.pdf import PDFUtils

# Пример сохранения HTML-контента в PDF
html_content = "<p>Hello, PDF with xhtml2pdf!</p>"
pdf_file = "example_xhtml2pdf.pdf"
result = PDFUtils.save_pdf_xhtml2pdf(html_content, pdf_file)
print(f"PDF сохранен с помощью xhtml2pdf: {result}")

# Пример сохранения HTML-файла в PDF
html_file = Path("example.html")  # Убедитесь, что файл существует
pdf_file = "example_from_file_xhtml2pdf.pdf"
result = PDFUtils.save_pdf_xhtml2pdf(html_file, pdf_file)
print(f"PDF сохранен из файла с помощью xhtml2pdf: {result}")
```

### `html2pdf`

```python
def html2pdf(html_str: str, pdf_file: str | Path) -> bool | None:
    """Converts HTML content to a PDF file using WeasyPrint."""
```

**Описание**: Конвертирует HTML-контент в PDF-файл с использованием библиотеки `WeasyPrint`.

**Параметры**:
- `html_str` (str): HTML-контент для конвертации.
- `pdf_file` (str | Path): Путь к сохраняемому PDF-файлу.

**Возвращает**:
- `bool | None`: `True`, если конвертация прошла успешно, иначе `None`.

**Примеры**:

```python
from src.utils.pdf import PDFUtils

# Пример конвертации HTML-контента в PDF
html_content = "<html><body><h1>Hello, PDF with WeasyPrint!</h1></body></html>"
pdf_file = "example_html2pdf.pdf"
result = PDFUtils.html2pdf(html_content, pdf_file)
print(f"PDF сохранен с помощью WeasyPrint: {result}")
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

**Параметры**:
- `pdf_file` (str | Path): Путь к исходному PDF-файлу.
- `html_file` (str | Path): Путь к сохраняемому HTML-файлу.

**Возвращает**:
- `bool`: `True`, если конвертация прошла успешно, иначе `False`.

**Примеры**:

```python
from pathlib import Path
from src.utils.pdf import PDFUtils

# Пример конвертации PDF-файла в HTML-файл
pdf_file = Path("example.pdf")  # Убедитесь, что файл существует
html_file = "example_pdf2html.html"
result = PDFUtils.pdf_to_html(pdf_file, html_file)
print(f"HTML сохранен: {result}")
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

**Описание**: Сохраняет данные из словаря в PDF-файл.

**Параметры**:
- `data` (Any): Словарь для конвертации в PDF.
- `file_path` (str | Path): Путь к сохраняемому PDF-файлу.

**Примеры**:

```python
from pathlib import Path
from types import SimpleNamespace
from src.utils.pdf import PDFUtils

# Пример сохранения словаря в PDF
data = {"name": "John", "age": 30, "city": "New York"}
pdf_file = "example_dict.pdf"
PDFUtils.dict2pdf(data, pdf_file)
print(f"Словарь сохранен в PDF: {pdf_file}")

# Пример сохранения SimpleNamespace в PDF
data = SimpleNamespace(name="Alice", age=25, city="Los Angeles")
pdf_file = "example_simplenamespace.pdf"
PDFUtils.dict2pdf(data, pdf_file)
print(f"SimpleNamespace сохранен в PDF: {pdf_file}")