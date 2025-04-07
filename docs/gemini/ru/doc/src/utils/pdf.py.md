# Модуль для работы с PDF файлами
=================================================

Модуль содержит класс :class:`PDFUtils`, который предоставляет методы для преобразования HTML-контента или файлов в PDF, а также для конвертации PDF в HTML.

## Обзор

Модуль `src.utils.pdf` предназначен для работы с PDF-файлами. Он предоставляет функциональность для сохранения HTML-контента в PDF, используя различные библиотеки, такие как `pdfkit`, `FPDF`, `WeasyPrint` и `xhtml2pdf`. Также модуль позволяет конвертировать PDF-файлы в HTML.

## Подробней

Этот модуль предоставляет статические методы класса `PDFUtils` для работы с PDF-файлами. Он использует различные библиотеки для генерации PDF из HTML, такие как `pdfkit`, `FPDF`, `WeasyPrint` и `xhtml2pdf`. Кроме того, модуль включает функцию для конвертации PDF-файлов в HTML с использованием библиотеки `pdfminer`.

## Классы

### `PDFUtils`

**Описание**:
Класс предоставляет статические методы для работы с PDF-файлами, включая сохранение HTML-контента в PDF с использованием различных библиотек и конвертацию PDF в HTML.

**Методы**:
- `save_pdf_pdfkit(data: str | Path, pdf_file: str | Path) -> bool`: Сохраняет HTML-контент или файл в PDF с использованием библиотеки `pdfkit`.
- `save_pdf_fpdf(data: str, pdf_file: str | Path) -> bool`: Сохраняет текст в PDF с использованием библиотеки `FPDF`.
- `save_pdf_weasyprint(data: str | Path, pdf_file: str | Path) -> bool`: Сохраняет HTML-контент или файл в PDF с использованием библиотеки `WeasyPrint`.
- `save_pdf_xhtml2pdf(data: str | Path, pdf_file: str | Path) -> bool`: Сохраняет HTML-контент или файл в PDF с использованием библиотеки `xhtml2pdf`.
- `html2pdf(html_str: str, pdf_file: str | Path) -> bool | None`: Преобразует HTML-контент в PDF-файл с использованием WeasyPrint.
- `pdf_to_html(pdf_file: str | Path, html_file: str | Path) -> bool`: Конвертирует PDF-файл в HTML-файл.
- `dict2pdf(data: Any, file_path: str | Path) -> None`: Сохраняет данные словаря в PDF-файл.

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
```

**Назначение**: Сохраняет HTML-контент или HTML-файл в PDF-файл с использованием библиотеки `pdfkit`.

**Параметры**:
- `data` (str | Path): HTML-контент (строка) или путь к HTML-файлу (Path).
- `pdf_file` (str | Path): Путь к сохраняемому PDF-файлу.

**Возвращает**:
- `bool`: `True`, если PDF успешно сохранен, иначе `False`.

**Вызывает исключения**:
- `pdfkit.PDFKitError`: Если происходит ошибка во время генерации PDF с использованием `pdfkit`.
- `OSError`: Если возникает ошибка доступа к файлу.
- `FileNotFoundError`: Если не найден исполняемый файл `wkhtmltopdf.exe`.

**Как работает функция**:
1. Определяется путь к исполняемому файлу `wkhtmltopdf.exe`.
2. Проверяется наличие файла `wkhtmltopdf.exe` по указанному пути. Если файл не найден, вызывается исключение `FileNotFoundError`.
3. Настраивается конфигурация `pdfkit` с указанием пути к `wkhtmltopdf.exe`.
4. Устанавливаются опции, разрешающие доступ к локальным файлам.
5. В зависимости от типа данных (`str` или `Path`), вызывается `pdfkit.from_string` (для HTML-контента) или `pdfkit.from_file` (для HTML-файла) для преобразования в PDF.
6. В случае успеха возвращается `True`, иначе логируется ошибка и возвращается `False`.

```
A[Определение пути к wkhtmltopdf.exe и проверка наличия]
|
B[Настройка конфигурации pdfkit]
|
C[Определение типа данных (HTML-контент или файл)]
|
D[Преобразование HTML в PDF (pdfkit.from_string или pdfkit.from_file)]
|
E[Обработка исключений (pdfkit.PDFKitError, OSError, Exception)]
|
F[Возврат True при успехе или False при ошибке]
```

**Примеры**:

```python
from pathlib import Path
from src.utils.pdf import PDFUtils

# Пример сохранения HTML-контента в PDF
html_content = "<html><body><h1>Hello, world!</h1></body></html>"
pdf_file = "example.pdf"
result = PDFUtils.save_pdf_pdfkit(html_content, pdf_file)
print(f"Сохранение HTML-контента в PDF: {result}")  # Вывод: Сохранение HTML-контента в PDF: True

# Пример сохранения HTML-файла в PDF
html_file = Path("example.html")
html_file.write_text("<html><body><h1>Hello, world!</h1></body></html>")
pdf_file = "example_file.pdf"
result = PDFUtils.save_pdf_pdfkit(html_file, pdf_file)
print(f"Сохранение HTML-файла в PDF из файла: {result}")  # Вывод: Сохранение HTML-файла в PDF из файла: True
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
```

**Назначение**: Сохраняет текст в PDF-файл с использованием библиотеки `FPDF`.

**Параметры**:
- `data` (str): Текст, который необходимо сохранить в PDF.
- `pdf_file` (str | Path): Путь к сохраняемому PDF-файлу.

**Возвращает**:
- `bool`: `True`, если PDF успешно сохранен, иначе `False`.

**Вызывает исключения**:
- `FileNotFoundError`: Если JSON-файл с информацией о шрифтах не найден.

**Как работает функция**:
1. Инициализируется объект `FPDF`.
2. Добавляется новая страница в PDF-документ и устанавливаются отступы.
3. Определяется путь к файлу `fonts.json`, содержащему информацию о шрифтах.
4. Загружается информация о шрифтах из `fonts.json`.
5. Добавляются шрифты, указанные в `fonts.json`, в PDF-документ.
6. Устанавливается шрифт по умолчанию и добавляется текст в PDF.
7. Сохраняется PDF-файл.
8. В случае успеха возвращается `True`, иначе логируется ошибка и возвращается `False`.

```
A[Инициализация объекта FPDF]
|
B[Настройка страницы PDF (добавление страницы, отступы)]
|
C[Определение пути к файлу fonts.json и загрузка информации о шрифтах]
|
D[Добавление шрифтов в PDF документ]
|
E[Установка шрифта по умолчанию и добавление текста]
|
F[Сохранение PDF-файла]
|
G[Обработка исключений и логирование ошибок]
|
H[Возврат True при успехе или False при ошибке]
```

**Примеры**:

```python
from pathlib import Path
from src.utils.pdf import PDFUtils

# Пример сохранения текста в PDF
text_data = "Пример текста для сохранения в PDF."
pdf_file = "example_fpdf.pdf"
result = PDFUtils.save_pdf_fpdf(text_data, pdf_file)
print(f"Сохранение текста в PDF с использованием FPDF: {result}")  # Вывод: Сохранение текста в PDF с использованием FPDF: True
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
```

**Назначение**: Сохраняет HTML-контент или HTML-файл в PDF-файл с использованием библиотеки `WeasyPrint`.

**Параметры**:
- `data` (str | Path): HTML-контент (строка) или путь к HTML-файлу (Path).
- `pdf_file` (str | Path): Путь к сохраняемому PDF-файлу.

**Возвращает**:
- `bool`: `True`, если PDF успешно сохранен, иначе `False`.

**Как работает функция**:
1. Проверяется, является ли `data` строкой или путем к файлу.
2. В зависимости от типа данных, вызывается `HTML(string=data).write_pdf(pdf_file)` для HTML-контента или `HTML(filename=str(data)).write_pdf(pdf_file)` для HTML-файла.
3. В случае успеха возвращается `True`, иначе логируется ошибка и возвращается `False`.

```
A[Определение типа данных (HTML-контент или файл)]
|
B[Преобразование HTML в PDF (HTML(string=data).write_pdf или HTML(filename=str(data)).write_pdf)]
|
C[Обработка исключений и логирование ошибок]
|
D[Возврат True при успехе или False при ошибке]
```

**Примеры**:

```python
from pathlib import Path
from src.utils.pdf import PDFUtils

# Пример сохранения HTML-контента в PDF
html_content = "<html><body><h1>Hello, world!</h1></body></html>"
pdf_file = "example_weasyprint.pdf"
result = PDFUtils.save_pdf_weasyprint(html_content, pdf_file)
print(f"Сохранение HTML-контента в PDF с использованием WeasyPrint: {result}")  # Вывод: Сохранение HTML-контента в PDF с использованием WeasyPrint: True

# Пример сохранения HTML-файла в PDF
html_file = Path("example.html")
html_file.write_text("<html><body><h1>Hello, world!</h1></body></html>")
pdf_file = "example_file_weasyprint.pdf"
result = PDFUtils.save_pdf_weasyprint(html_file, pdf_file)
print(f"Сохранение HTML-файла в PDF с использованием WeasyPrint: {result}")  # Вывод: Сохранение HTML-файла в PDF с использованием WeasyPrint: True
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
```

**Назначение**: Сохраняет HTML-контент или HTML-файл в PDF-файл с использованием библиотеки `xhtml2pdf`.

**Параметры**:
- `data` (str | Path): HTML-контент (строка) или путь к HTML-файлу (Path).
- `pdf_file` (str | Path): Путь к сохраняемому PDF-файлу.

**Возвращает**:
- `bool`: `True`, если PDF успешно сохранен, иначе `False`.

**Как работает функция**:
1. Открывается PDF-файл для записи в бинарном режиме.
2. Проверяется, является ли `data` строкой или путем к файлу.
3. Если `data` - строка, она кодируется в UTF-8 и передается в `pisa.CreatePDF`.
4. Если `data` - путь к файлу, файл открывается, читается его содержимое в кодировке UTF-8 и передается в `pisa.CreatePDF`.
5. В случае успеха возвращается `True`, иначе логируется ошибка и возвращается `False`.

```
A[Открытие PDF-файла для записи]
|
B[Определение типа данных (HTML-контент или файл)]
|
C[Обработка HTML (кодирование в UTF-8, чтение из файла)]
|
D[Преобразование HTML в PDF (pisa.CreatePDF)]
|
E[Обработка исключений и логирование ошибок]
|
F[Возврат True при успехе или False при ошибке]
```

**Примеры**:

```python
from pathlib import Path
from src.utils.pdf import PDFUtils

# Пример сохранения HTML-контента в PDF
html_content = "<html><body><h1>Hello, world!</h1></body></html>"
pdf_file = "example_xhtml2pdf.pdf"
result = PDFUtils.save_pdf_xhtml2pdf(html_content, pdf_file)
print(f"Сохранение HTML-контента в PDF с использованием xhtml2pdf: {result}")  # Вывод: Сохранение HTML-контента в PDF с использованием xhtml2pdf: True

# Пример сохранения HTML-файла в PDF
html_file = Path("example.html")
html_file.write_text("<html><body><h1>Hello, world!</h1></body></html>")
pdf_file = "example_file_xhtml2pdf.pdf"
result = PDFUtils.save_pdf_xhtml2pdf(html_file, pdf_file)
print(f"Сохранение HTML-файла в PDF с использованием xhtml2pdf: {result}")  # Вывод: Сохранение HTML-файла в PDF с использованием xhtml2pdf: True
```

### `html2pdf`

```python
@staticmethod
def html2pdf(html_str: str, pdf_file: str | Path) -> bool | None:
    """Converts HTML content to a PDF file using WeasyPrint."""
```

**Назначение**: Преобразует HTML-контент в PDF-файл с использованием WeasyPrint.

**Параметры**:
- `html_str` (str): HTML-контент для преобразования.
- `pdf_file` (str | Path): Путь к сохраняемому PDF-файлу.

**Возвращает**:
- `bool | None`: `True`, если преобразование прошло успешно, иначе `None`.

**Как работает функция**:
1. Использует библиотеку WeasyPrint для преобразования HTML-строки в PDF-файл.
2. В случае успеха возвращает `True`, иначе выводит сообщение об ошибке и возвращает `None`.

```
A[Преобразование HTML в PDF (WeasyPrint)]
|
B[Обработка исключений и вывод сообщения об ошибке]
|
C[Возврат True при успехе или None при ошибке]
```

**Примеры**:

```python
from pathlib import Path
from src.utils.pdf import PDFUtils

# Пример сохранения HTML-контента в PDF
html_content = "<html><body><h1>Hello, world!</h1></body></html>"
pdf_file = "example_html2pdf.pdf"
result = PDFUtils.html2pdf(html_content, pdf_file)
print(f"Сохранение HTML-контента в PDF с использованием html2pdf: {result}")  # Вывод: Сохранение HTML-контента в PDF с использованием html2pdf: True или None
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
```

**Назначение**: Конвертирует PDF-файл в HTML-файл.

**Параметры**:
- `pdf_file` (str | Path): Путь к исходному PDF-файлу.
- `html_file` (str | Path): Путь к сохраняемому HTML-файлу.

**Возвращает**:
- `bool`: `True`, если конвертация прошла успешно, иначе `False`.

**Как работает функция**:
1. Извлекает текст из PDF-файла с использованием библиотеки `pdfminer`.
2. Создает HTML-файл и записывает извлеченный текст в формате HTML.
3. В случае успеха возвращает `True`, иначе выводит сообщение об ошибке и возвращает `False`.

```
A[Извлечение текста из PDF (pdfminer)]
|
B[Создание HTML-файла и запись текста]
|
C[Обработка исключений и вывод сообщения об ошибке]
|
D[Возврат True при успехе или False при ошибке]
```

**Примеры**:

```python
from pathlib import Path
from src.utils.pdf import PDFUtils

# Пример конвертации PDF в HTML
pdf_file = "example.pdf"  # Укажите путь к существующему PDF-файлу
html_file = "example_pdf_to_html.html"
result = PDFUtils.pdf_to_html(pdf_file, html_file)
print(f"Конвертация PDF в HTML: {result}")  # Вывод: Конвертация PDF в HTML: True или False
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
```

**Назначение**: Сохраняет данные словаря в PDF-файл.

**Параметры**:
- `data` (Any): Данные словаря для сохранения в PDF.
- `file_path` (str | Path): Путь к сохраняемому PDF-файлу.

**Как работает функция**:
1. Проверяет, является ли `data` экземпляром `SimpleNamespace`, и если да, преобразует его в словарь.
2. Создает объект `canvas.Canvas` для создания PDF-файла.
3. Устанавливает шрифт и размер шрифта.
4. Итерируется по элементам словаря и записывает каждую пару "ключ: значение" в PDF-файл.
5. Если достигнут конец страницы, создает новую страницу.
6. Сохраняет PDF-файл.

```
A[Проверка типа данных (SimpleNamespace -> dict)]
|
B[Создание объекта canvas.Canvas]
|
C[Установка шрифта]
|
D[Итерация по элементам словаря]
|
E[Запись данных в PDF]
|
F[Проверка на конец страницы и создание новой страницы при необходимости]
|
G[Сохранение PDF-файла]
```

**Примеры**:

```python
from pathlib import Path
from src.utils.pdf import PDFUtils

# Пример сохранения словаря в PDF
data = {"name": "John Doe", "age": 30, "city": "New York"}
pdf_file = "example_dict2pdf.pdf"
PDFUtils.dict2pdf(data, pdf_file)
print(f"Сохранение словаря в PDF: {pdf_file}")  # Вывод: Сохранение словаря в PDF: example_dict2pdf.pdf