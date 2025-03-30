# Модуль `src.utils.pdf`

## Обзор

Модуль `src.utils.pdf` предоставляет инструменты для преобразования HTML-контента или файлов в PDF с использованием различных библиотек. Он включает в себя функции для сохранения HTML в PDF с использованием `pdfkit`, `FPDF`, `WeasyPrint` и `xhtml2pdf`, а также функцию для конвертации PDF-файлов в HTML-файлы.

## Подробнее

Этот модуль предоставляет статические методы класса `PDFUtils` для работы с PDF-файлами. Он позволяет сохранять HTML-контент в PDF, используя различные библиотеки, что обеспечивает гибкость и возможность выбора наиболее подходящего инструмента в зависимости от требований проекта.

## Классы

### `PDFUtils`

**Описание**: Класс для работы с PDF-файлами, предоставляющий методы для сохранения HTML-контента в PDF с использованием различных библиотек.

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
    Args:
        data (str | Path): HTML-контент или путь к HTML-файлу.
        pdf_file (str | Path): Путь к сохраняемому PDF-файлу.

    Returns:
        bool: `True` если PDF успешно сохранен, иначе `False`.

    Raises:
        pdfkit.PDFKitError: Ошибка генерации PDF через `pdfkit`.
        OSError: Ошибка доступа к файлу.

     **Как работает функция**:
     Функция `save_pdf_pdfkit` использует библиотеку `pdfkit` для преобразования HTML-контента или файла в PDF. Она принимает HTML-контент или путь к HTML-файлу, а также путь к сохраняемому PDF-файлу. Функция проверяет наличие исполняемого файла `wkhtmltopdf.exe`, необходимого для работы `pdfkit`, и вызывает соответствующий метод `pdfkit` (либо `from_string`, либо `from_file`) для генерации PDF. В случае успеха возвращается `True`, иначе - `False`.
    """
    - Не выводи тело функции. только документацию и примеры вызова функции;
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

html_content = "<html><body><h1>Hello, world!</h1></body></html>"
pdf_file = "example.pdf"
result = PDFUtils.save_pdf_pdfkit(html_content, pdf_file)
print(f"PDF сохранен: {result}")

html_file_path = Path("example.html")
html_file_path.write_text(html_content)
result = PDFUtils.save_pdf_pdfkit(html_file_path, pdf_file)
print(f"PDF сохранен: {result}")
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

     **Как работает функция**:
     Функция `save_pdf_fpdf` использует библиотеку `FPDF` для сохранения текста в PDF-файл. Она принимает текст, который необходимо сохранить, и путь к сохраняемому PDF-файлу. Функция инициализирует объект `FPDF`, добавляет страницу, устанавливает автоматический перенос строк и добавляет указанный шрифт. Затем устанавливается шрифт и добавляется текст в PDF. В случае успеха возвращается `True`, иначе - `False`.
    """
    - Не выводи тело функции. только документацию и примеры вызова функции;
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

text_data = "Hello, world! This is a test PDF generated with FPDF."
pdf_file = "example_fpdf.pdf"
result = PDFUtils.save_pdf_fpdf(text_data, pdf_file)
print(f"PDF сохранен: {result}")
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

     **Как работает функция**:
     Функция `save_pdf_weasyprint` использует библиотеку `WeasyPrint` для преобразования HTML-контента или файла в PDF. Она принимает HTML-контент или путь к HTML-файлу, а также путь к сохраняемому PDF-файлу. Функция вызывает соответствующий метод `HTML` (либо `string`, либо `filename`) для генерации PDF. В случае успеха возвращается `True`, иначе - `False`.
    """
    - Не выводи тело функции. только документацию и примеры вызова функции;
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

html_content = "<html><body><h1>Hello, world!</h1></body></html>"
pdf_file = "example_weasyprint.pdf"
result = PDFUtils.save_pdf_weasyprint(html_content, pdf_file)
print(f"PDF сохранен: {result}")

html_file_path = Path("example.html")
html_file_path.write_text(html_content)
result = PDFUtils.save_pdf_weasyprint(html_file_path, pdf_file)
print(f"PDF сохранен: {result}")
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

     **Как работает функция**:
     Функция `save_pdf_xhtml2pdf` использует библиотеку `xhtml2pdf` для преобразования HTML-контента или файла в PDF. Она принимает HTML-контент или путь к HTML-файлу, а также путь к сохраняемому PDF-файлу. Функция вызывает метод `pisa.CreatePDF` для генерации PDF. В случае успеха возвращается `True`, иначе - `False`.
    """
    - Не выводи тело функции. только документацию и примеры вызова функции;
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

html_content = "<html><body><h1>Hello, world!</h1></body></html>"
pdf_file = "example_xhtml2pdf.pdf"
result = PDFUtils.save_pdf_xhtml2pdf(html_content, pdf_file)
print(f"PDF сохранен: {result}")

html_file_path = Path("example.html")
html_file_path.write_text(html_content)
result = PDFUtils.save_pdf_xhtml2pdf(html_file_path, pdf_file)
print(f"PDF сохранен: {result}")
```

### `html2pdf`

```python
def html2pdf(html_str: str, pdf_file: str | Path) -> bool | None:
    """
    Args:
        html_str (str): HTML контент для конвертации.
        pdf_file (str | Path): Путь к сохраняемому PDF-файлу.

    Returns:
        bool | None: `True` если PDF успешно сохранен, иначе `None`.

     **Как работает функция**:
     Функция `html2pdf` использует библиотеку `WeasyPrint` для преобразования HTML-контента в PDF-файл. Она принимает HTML-контент и путь к сохраняемому PDF-файлу. Функция вызывает метод `HTML(string=html_str).write_pdf(pdf_file)` для генерации PDF. В случае успеха возвращается `True`, иначе - `None`.
    """
    - Не выводи тело функции. только документацию и примеры вызова функции;
```

**Описание**: Конвертирует HTML-контент в PDF-файл, используя WeasyPrint.

**Параметры**:

- `html_str` (str): HTML контент для конвертации.
- `pdf_file` (str | Path): Путь к сохраняемому PDF-файлу.

**Возвращает**:

- `bool | None`: `True`, если PDF успешно сохранен, иначе `None`.

**Примеры**:

```python
from src.utils.pdf import PDFUtils

html_content = "<html><body><h1>Hello, world!</h1></body></html>"
pdf_file = "example_html2pdf.pdf"
result = PDFUtils.html2pdf(html_content, pdf_file)
print(f"PDF сохранен: {result}")
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

     **Как работает функция**:
     Функция `pdf_to_html` конвертирует PDF-файл в HTML-файл. Она принимает путь к исходному PDF-файлу и путь к сохраняемому HTML-файлу. Функция использует библиотеку `pdfminer.high_level` для извлечения текста из PDF-файла, а затем создает HTML-файл и записывает извлеченный текст в него. В случае успеха возвращается `True`, иначе - `False`.
    """
    - Не выводи тело функции. только документацию и примеры вызова функции;
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

pdf_file = "example.pdf"
html_file = "example.html"
# Создайте пустой PDF файл для примера
Path(pdf_file).write_bytes(b'')
result = PDFUtils.pdf_to_html(pdf_file, html_file)
print(f"HTML сохранен: {result}")
```

### `dict2pdf`

```python
def dict2pdf(data: Any, file_path: str | Path) -> None:
    """
    Args:
        data (dict | SimpleNamespace): The dictionary to convert to PDF.
        file_path (str | Path): Path to the output PDF file.

     **Как работает функция**:
     Функция `dict2pdf` сохраняет данные словаря в PDF-файл. Она принимает словарь или `SimpleNamespace` и путь к сохраняемому PDF-файлу. Функция использует библиотеку `reportlab.pdfgen.canvas` для создания PDF-файла и записывает данные словаря в него. Функция проходит по каждой паре ключ-значение в словаре и записывает их в PDF-файл. Если места на странице недостаточно, создается новая страница.
    """
    - Не выводи тело функции. только документацию и примеры вызова функции;
```

**Описание**: Сохраняет данные словаря в PDF-файл.

**Параметры**:

- `data` (dict | SimpleNamespace): Данные словаря для преобразования в PDF.
- `file_path` (str | Path): Путь к сохраняемому PDF-файлу.

**Примеры**:

```python
from src.utils.pdf import PDFUtils

data = {"name": "John Doe", "age": 30, "city": "New York"}
pdf_file = "example_dict2pdf.pdf"
PDFUtils.dict2pdf(data, pdf_file)
print(f"PDF сохранен: {pdf_file}")