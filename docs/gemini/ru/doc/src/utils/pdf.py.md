# Модуль `src.utils.pdf`

## Обзор

Модуль предназначен для преобразования HTML-контента или файлов в PDF с использованием различных библиотек.
Он предоставляет классы и методы для работы с PDF-файлами, обеспечивая сохранение HTML-контента в PDF с использованием различных библиотек, таких как `pdfkit`, `FPDF`, `WeasyPrint` и `xhtml2pdf`.

## Подробнее

Модуль предоставляет статические методы класса `PDFUtils` для преобразования HTML в PDF с использованием различных библиотек. Каждая функция выполняет преобразование с использованием определенной библиотеки и обрабатывает исключения, которые могут возникнуть в процессе.

## Классы

### `PDFUtils`

**Описание**:
Класс `PDFUtils` предоставляет статические методы для сохранения HTML-контента в PDF с использованием различных библиотек.

**Как работает класс**:
Класс содержит статические методы, каждый из которых использует определенную библиотеку для преобразования HTML в PDF. Он предоставляет гибкий интерфейс для выбора наиболее подходящего инструмента для конкретной задачи.

**Методы**:
- `save_pdf_pdfkit(data: str | Path, pdf_file: str | Path) -> bool`
- `save_pdf_fpdf(data: str, pdf_file: str | Path) -> bool`
- `save_pdf_weasyprint(data: str | Path, pdf_file: str | Path) -> bool`
- `save_pdf_xhtml2pdf(data: str | Path, pdf_file: str | Path) -> bool`
- `html2pdf(html_str: str, pdf_file: str | Path) -> bool | None`
- `pdf_to_html(pdf_file: str | Path, html_file: str | Path) -> bool`
- `dict2pdf(data: Any, file_path: str | Path) -> None`

## Функции

### `save_pdf_pdfkit`

```python
@staticmethod
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
    ...
```

**Как работает функция**:
Функция `save_pdf_pdfkit` принимает HTML-контент или путь к HTML-файлу и сохраняет его в PDF-файл, используя библиотеку `pdfkit`. Она настраивает `pdfkit` с указанием пути к исполняемому файлу `wkhtmltopdf.exe`, который необходим для работы `pdfkit`. Если `data` является строкой, она интерпретируется как HTML-контент; в противном случае, она интерпретируется как путь к HTML-файлу.

**Параметры**:
- `data` (str | Path): HTML-контент или путь к HTML-файлу.
- `pdf_file` (str | Path): Путь к сохраняемому PDF-файлу.

**Возвращает**:
- `bool`: `True`, если PDF успешно сохранен, иначе `False`.

**Вызывает исключения**:
- `pdfkit.PDFKitError`: Возникает при ошибке генерации PDF через `pdfkit`.
- `OSError`: Возникает при ошибке доступа к файлу.

**Примеры**:

```python
from pathlib import Path
from src.utils.pdf import PDFUtils

html_content = "<html><body><h1>Hello, world!</h1></body></html>"
pdf_file = "example.pdf"
result = PDFUtils.save_pdf_pdfkit(html_content, pdf_file)
print(f"PDF saved successfully: {result}")

html_file = Path("example.html")
html_file.write_text(html_content)
pdf_file = "example_from_file.pdf"
result = PDFUtils.save_pdf_pdfkit(html_file, pdf_file)
print(f"PDF saved successfully from file: {result}")
```

### `save_pdf_fpdf`

```python
@staticmethod
def save_pdf_fpdf(data: str, pdf_file: str | Path) -> bool:
    """
    Сохранить текст в PDF с использованием библиотеки FPDF.

    Args:
        data (str): Текст, который необходимо сохранить в PDF.
        pdf_file (str | Path): Путь к сохраняемому PDF-файлу.

    Returns:
        bool: `True`, если PDF успешно сохранен, иначе `False`.
    """
    ...
```

**Как работает функция**:
Функция `save_pdf_fpdf` сохраняет текст в PDF-файл, используя библиотеку `FPDF`. Она создает экземпляр класса `FPDF`, добавляет страницу, устанавливает автоматический перенос текста и добавляет указанный текст в PDF. Функция также поддерживает добавление шрифтов из файла `fonts.json`.

**Параметры**:
- `data` (str): Текст, который необходимо сохранить в PDF.
- `pdf_file` (str | Path): Путь к сохраняемому PDF-файлу.

**Возвращает**:
- `bool`: `True`, если PDF успешно сохранен, иначе `False`.

**Вызывает исключения**:
- `FileNotFoundError`: Возникает, если файл шрифта не найден.

**Примеры**:

```python
from src.utils.pdf import PDFUtils

text_data = "Hello, world! This is a test PDF generated using FPDF."
pdf_file = "example_fpdf.pdf"
result = PDFUtils.save_pdf_fpdf(text_data, pdf_file)
print(f"PDF saved successfully using FPDF: {result}")
```

### `save_pdf_weasyprint`

```python
@staticmethod
def save_pdf_weasyprint(data: str | Path, pdf_file: str | Path) -> bool:
    """
    Сохранить HTML-контент или файл в PDF с использованием библиотеки `WeasyPrint`.

    Args:
        data (str | Path): HTML-контент или путь к HTML-файлу.
        pdf_file (str | Path): Путь к сохраняемому PDF-файлу.

    Returns:
        bool: `True` если PDF успешно сохранен, иначе `False`.
    """
    ...
```

**Как работает функция**:
Функция `save_pdf_weasyprint` сохраняет HTML-контент или файл в PDF-файл, используя библиотеку `WeasyPrint`. Если `data` является строкой, она интерпретируется как HTML-контент; в противном случае, она интерпретируется как путь к HTML-файлу.

**Параметры**:
- `data` (str | Path): HTML-контент или путь к HTML-файлу.
- `pdf_file` (str | Path): Путь к сохраняемому PDF-файлу.

**Возвращает**:
- `bool`: `True`, если PDF успешно сохранен, иначе `False`.

**Примеры**:

```python
from pathlib import Path
from src.utils.pdf import PDFUtils

html_content = "<html><body><h1>Hello, world!</h1></body></html>"
pdf_file = "example_weasyprint.pdf"
result = PDFUtils.save_pdf_weasyprint(html_content, pdf_file)
print(f"PDF saved successfully using WeasyPrint: {result}")

html_file = Path("example.html")
html_file.write_text(html_content)
pdf_file = "example_weasyprint_from_file.pdf"
result = PDFUtils.save_pdf_weasyprint(html_file, pdf_file)
print(f"PDF saved successfully from file using WeasyPrint: {result}")
```

### `save_pdf_xhtml2pdf`

```python
@staticmethod
def save_pdf_xhtml2pdf(data: str | Path, pdf_file: str | Path) -> bool:
    """
    Сохранить HTML-контент или файл в PDF с использованием библиотеки `xhtml2pdf`.

    Args:
        data (str | Path): HTML-контент или путь к HTML-файлу.
        pdf_file (str | Path): Путь к сохраняемому PDF-файлу.

    Returns:
        bool: `True` если PDF успешно сохранен, иначе `False`.
    """
    ...
```

**Как работает функция**:
Функция `save_pdf_xhtml2pdf` сохраняет HTML-контент или файл в PDF-файл, используя библиотеку `xhtml2pdf`. Если `data` является строкой, она интерпретируется как HTML-контент; в противном случае, она интерпретируется как путь к HTML-файлу. Функция обрабатывает HTML-контент в кодировке UTF-8.

**Параметры**:
- `data` (str | Path): HTML-контент или путь к HTML-файлу.
- `pdf_file` (str | Path): Путь к сохраняемому PDF-файлу.

**Возвращает**:
- `bool`: `True`, если PDF успешно сохранен, иначе `False`.

**Примеры**:

```python
from pathlib import Path
from src.utils.pdf import PDFUtils

html_content = "<html><body><h1>Hello, world!</h1></body></html>"
pdf_file = "example_xhtml2pdf.pdf"
result = PDFUtils.save_pdf_xhtml2pdf(html_content, pdf_file)
print(f"PDF saved successfully using xhtml2pdf: {result}")

html_file = Path("example.html")
html_file.write_text(html_content)
pdf_file = "example_xhtml2pdf_from_file.pdf"
result = PDFUtils.save_pdf_xhtml2pdf(html_file, pdf_file)
print(f"PDF saved successfully from file using xhtml2pdf: {result}")
```

### `html2pdf`

```python
@staticmethod
def html2pdf(html_str: str, pdf_file: str | Path) -> bool | None:
    """Converts HTML content to a PDF file using WeasyPrint."""
    ...
```

**Как работает функция**:
Функция `html2pdf` преобразует HTML-контент в PDF-файл, используя библиотеку `WeasyPrint`.

**Параметры**:
- `html_str` (str): HTML-контент для преобразования.
- `pdf_file` (str | Path): Путь к сохраняемому PDF-файлу.

**Возвращает**:
- `bool | None`: `True`, если PDF успешно сохранен, иначе `None`.

**Примеры**:

```python
from src.utils.pdf import PDFUtils

html_content = "<html><body><h1>Hello, world!</h1></body></html>"
pdf_file = "example_html2pdf.pdf"
result = PDFUtils.html2pdf(html_content, pdf_file)
print(f"PDF saved successfully using html2pdf: {result}")
```

### `pdf_to_html`

```python
@staticmethod
def pdf_to_html(pdf_file: str | Path, html_file: str | Path) -> bool:
    """
    Конвертирует PDF-файл в HTML-файл.

    Args:
        pdf_file (str | Path): Путь к исходному PDF-файлу.
        html_file (str | Path): Путь к сохраняемому HTML-файлу.

    Returns:
        bool: `True`, если конвертация прошла успешно, иначе `False`.
    """
    ...
```

**Как работает функция**:
Функция `pdf_to_html` конвертирует PDF-файл в HTML-файл. Она извлекает текст из PDF-файла с использованием библиотеки `pdfminer.high_level` и сохраняет его в HTML-файл.

**Параметры**:
- `pdf_file` (str | Path): Путь к исходному PDF-файлу.
- `html_file` (str | Path): Путь к сохраняемому HTML-файлу.

**Возвращает**:
- `bool`: `True`, если конвертация прошла успешно, иначе `False`.

**Примеры**:

```python
from pathlib import Path
from src.utils.pdf import PDFUtils

# Создаем тестовый PDF-файл
pdf_file = Path("example.pdf")
pdf_file.write_bytes(b"%PDF-1.5\n1 0 obj\n<< /Title (Test PDF) /Creator (PDFUtils) >>\nendobj\n2 0 obj\n<< /Type /Page /Parent 3 0 R /Contents 4 0 R >>\nendobj\n3 0 obj\n<< /Type /Pages /Count 1 /Kids [2 0 R] >>\nendobj\n4 0 obj\n<< /Length 44 >>\nstream\nBT /F1 12 Tf 50 750 Td (Hello, world!) Tj ET\nendstream\nendobj\n5 0 obj\n<< /Type /Font /Subtype /Type1 /Name /F1 /BaseFont /Helvetica /Encoding /MacRomanEncoding >>\nendobj\nxref\n0 6\n0000000000 65535 f \n0000000010 00000 n \n0000000059 00000 n \n0000000108 00000 n \n0000000157 00000 n \n0000000223 00000 n \ntrailer\n<< /Size 6 /Root 3 0 R >>\nstartxref\n328\n%%EOF")

html_file = "example.html"
result = PDFUtils.pdf_to_html(pdf_file, html_file)
print(f"HTML saved successfully: {result}")
```

### `dict2pdf`

```python
@staticmethod
def dict2pdf(data: Any, file_path: str | Path) -> None:
    """
    Save dictionary data to a PDF file.

    Args:
        data (dict | SimpleNamespace): The dictionary to convert to PDF.
        file_path (str | Path): Path to the output PDF file.
    """
    ...
```

**Как работает функция**:
Функция `dict2pdf` сохраняет данные словаря в PDF-файл. Она создает PDF-файл с использованием библиотеки `reportlab.pdfgen.canvas` и записывает в него данные словаря построчно.

**Параметры**:
- `data` (dict | SimpleNamespace): Словарь для преобразования в PDF.
- `file_path` (str | Path): Путь к выходному PDF-файлу.

**Примеры**:

```python
from src.utils.pdf import PDFUtils

data = {"name": "John Doe", "age": 30, "city": "New York"}
pdf_file = "example_dict2pdf.pdf"
PDFUtils.dict2pdf(data, pdf_file)
print(f"PDF saved successfully from dictionary: {pdf_file}")