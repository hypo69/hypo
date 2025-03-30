# Модуль `src.utils.pdf`

## Обзор

Модуль `src.utils.pdf` предназначен для преобразования HTML-контента или файлов в PDF с использованием различных библиотек, таких как `pdfkit`, `FPDF`, `WeasyPrint` и `xhtml2pdf`.

## Подробней

Этот модуль предоставляет статические методы класса `PDFUtils` для сохранения HTML-контента или файлов в PDF с использованием различных библиотек. Он также включает методы для конвертации PDF-файлов в HTML и сохранения данных из словаря в PDF. Модуль использует библиотеку `reportlab` для создания PDF-файлов из словарей.

## Классы

### `PDFUtils`

**Описание**: Класс для работы с PDF-файлами, предоставляющий методы для сохранения HTML-контента в PDF с использованием различных библиотек.

**Методы**:
- `save_pdf_pdfkit`: Сохраняет HTML-контент или файл в PDF с использованием библиотеки `pdfkit`.
- `save_pdf_fpdf`: Сохраняет текст в PDF с использованием библиотеки `FPDF`.
- `save_pdf_weasyprint`: Сохраняет HTML-контент или файл в PDF с использованием библиотеки `WeasyPrint`.
- `save_pdf_xhtml2pdf`: Сохраняет HTML-контент или файл в PDF с использованием библиотеки `xhtml2pdf`.
- `html2pdf`: Преобразует HTML-контент в PDF-файл с использованием `WeasyPrint`.
- `pdf_to_html`: Конвертирует PDF-файл в HTML-файл.
- `dict2pdf`: Сохраняет данные словаря в PDF-файл.

## Функции

### `save_pdf_pdfkit`

```python
def save_pdf_pdfkit(data: str | Path, pdf_file: str | Path) -> bool:
    """
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
- `pdfkit.PDFKitError`: Возникает при ошибке генерации PDF через `pdfkit`.
- `OSError`: Возникает при ошибке доступа к файлу.

**Примеры**:
```python
from pathlib import Path
from src.utils.pdf import PDFUtils

html_content = "<html><body><h1>Hello, World!</h1></body></html>"
pdf_file = "output.pdf"
result = PDFUtils.save_pdf_pdfkit(html_content, pdf_file)
print(f"PDF saved successfully: {result}")

html_file_path = Path("input.html")
html_file_path.write_text(html_content)
result = PDFUtils.save_pdf_pdfkit(html_file_path, pdf_file)
print(f"PDF saved successfully from file: {result}")
```

### `save_pdf_fpdf`

```python
def save_pdf_fpdf(data: str, pdf_file: str | Path) -> bool:
    """
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

text_data = "Hello, World! This is a PDF generated using FPDF."
pdf_file = "output_fpdf.pdf"
result = PDFUtils.save_pdf_fpdf(text_data, pdf_file)
print(f"PDF saved successfully using FPDF: {result}")
```

### `save_pdf_weasyprint`

```python
def save_pdf_weasyprint(data: str | Path, pdf_file: str | Path) -> bool:
    """
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

html_content = "<html><body><h1>Hello, World!</h1></body></html>"
pdf_file = "output_weasyprint.pdf"
result = PDFUtils.save_pdf_weasyprint(html_content, pdf_file)
print(f"PDF saved successfully using WeasyPrint: {result}")

html_file_path = Path("input.html")
html_file_path.write_text(html_content)
result = PDFUtils.save_pdf_weasyprint(html_file_path, pdf_file)
print(f"PDF saved successfully from file using WeasyPrint: {result}")
```

### `save_pdf_xhtml2pdf`

```python
def save_pdf_xhtml2pdf(data: str | Path, pdf_file: str | Path) -> bool:
    """
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

html_content = "<html><body><h1>Hello, World!</h1></body></html>"
pdf_file = "output_xhtml2pdf.pdf"
result = PDFUtils.save_pdf_xhtml2pdf(html_content, pdf_file)
print(f"PDF saved successfully using xhtml2pdf: {result}")

html_file_path = Path("input.html")
html_file_path.write_text(html_content)
result = PDFUtils.save_pdf_xhtml2pdf(html_file_path, pdf_file)
print(f"PDF saved successfully from file using xhtml2pdf: {result}")
```

### `html2pdf`

```python
def html2pdf(html_str: str, pdf_file: str | Path) -> bool | None:
    """Args:
        html_str (str): HTML content to convert.
        pdf_file (str | Path): PDF file path to save to.

    Returns:
        bool | None: True if PDF was saved, None if error
    """
```

**Описание**: Преобразует HTML-контент в PDF-файл с использованием `WeasyPrint`.

**Параметры**:
- `html_str` (str): HTML-контент для преобразования.
- `pdf_file` (str | Path): Путь к сохраняемому PDF-файлу.

**Возвращает**:
- `bool | None`: `True`, если PDF сохранен успешно, `None` в случае ошибки.

**Примеры**:
```python
from src.utils.pdf import PDFUtils

html_content = "<html><body><h1>Hello, World!</h1></body></html>"
pdf_file = "output_html2pdf.pdf"
result = PDFUtils.html2pdf(html_content, pdf_file)
print(f"PDF saved successfully using html2pdf: {result}")
```

### `pdf_to_html`

```python
def pdf_to_html(pdf_file: str | Path, html_file: str | Path) -> bool:
    """
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

# Создайте фиктивный PDF-файл для примера
pdf_file = "example.pdf"
with open(pdf_file, "wb") as f:
    f.write(b"%PDF-1.0\n1 0 obj\n<< /Title (Dummy PDF) /Creator (PDFLib) >>\nendobj\n2 0 obj\n<< /Type /Page /Parent 3 0 R /Contents 4 0 R >>\nendobj\n3 0 obj\n<< /Type /Pages /Kids [2 0 R] /Count 1 >>\nendobj\n4 0 obj\n<< /Length 44 >>\nstream\nBT /F1 12 Tf 50 750 Td (Hello, World!) Tj ET\nendstream\nendobj\n5 0 obj\n<< /Type /Font /Subtype /Type1 /Name /F1 /BaseFont /Helvetica /Encoding /MacRomanEncoding >>\nendobj\nxref\n0 6\n0000000000 65535 f \n0000000010 00000 n \n0000000059 00000 n \n0000000127 00000 n \n0000000178 00000 n \n0000000272 00000 n \ntrailer\n<< /Size 6 /Root 1 0 R >>\nstartxref\n378\n%%EOF")

html_file = "output.html"
result = PDFUtils.pdf_to_html(pdf_file, html_file)
print(f"HTML saved successfully: {result}")
```

### `dict2pdf`

```python
def dict2pdf(data: Any, file_path: str | Path) -> None:
    """
    Args:
        data (dict | SimpleNamespace): The dictionary to convert to PDF.
        file_path (str | Path): Path to the output PDF file.
    """
```

**Описание**: Сохраняет данные словаря в PDF-файл.

**Параметры**:
- `data` (dict | SimpleNamespace): Словарь для преобразования в PDF.
- `file_path` (str | Path): Путь к выходному PDF-файлу.

**Примеры**:
```python
from pathlib import Path
from src.utils.pdf import PDFUtils
from types import SimpleNamespace

data = {"name": "John Doe", "age": 30, "city": "New York"}
pdf_file = "output_dict2pdf.pdf"
PDFUtils.dict2pdf(data, pdf_file)
print(f"PDF saved successfully from dictionary: {pdf_file}")

# Пример использования SimpleNamespace
data_ns = SimpleNamespace(name="Jane Doe", age=25, city="Los Angeles")
pdf_file_ns = "output_simplenamespace2pdf.pdf"
PDFUtils.dict2pdf(data_ns, pdf_file_ns)
print(f"PDF saved successfully from SimpleNamespace: {pdf_file_ns}")