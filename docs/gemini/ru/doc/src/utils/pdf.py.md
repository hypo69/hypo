# Модуль для работы с PDF-файлами
=====================================

Модуль `src.utils.pdf` предназначен для преобразования HTML-контента или файлов в PDF с использованием различных библиотек.

Дополнительная информация:
- https://chatgpt.com/share/672266a3-0048-800d-a97b-c38f647d496b
- https://stackoverflow.com/questions/73599970/how-to-solve-wkhtmltopdf-reported-an-error-exit-with-code-1-due-to-network-err
- https://habr.com/ru/companies/bothub/articles/853490/

## Обзор

Модуль предоставляет класс `PDFUtils` с набором статических методов для сохранения HTML-контента или файлов в PDF, а также для конвертации PDF в HTML и сохранения словарей в PDF. Поддерживаются различные библиотеки для работы с PDF, такие как `pdfkit`, `FPDF`, `WeasyPrint` и `xhtml2pdf`.

## Подробней

Этот модуль предоставляет инструменты для работы с PDF-файлами, позволяя сохранять HTML-контент в PDF с использованием разных библиотек. Это полезно, когда требуется сгенерировать PDF-отчеты или документы из HTML-шаблонов. Модуль также включает функциональность для конвертации PDF-файлов в HTML и сохранения данных из словаря в PDF-формате.

## Классы

### `PDFUtils`

**Описание**: Класс `PDFUtils` предоставляет статические методы для работы с PDF-файлами, включая сохранение HTML-контента в PDF с использованием различных библиотек, конвертацию PDF в HTML и сохранение словарей в PDF.

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
```

**Назначение**: Сохраняет HTML-контент или файл в PDF с использованием библиотеки `pdfkit`.

**Параметры**:
- `data` (str | Path): HTML-контент в виде строки или путь к HTML-файлу.
- `pdf_file` (str | Path): Путь к сохраняемому PDF-файлу.

**Возвращает**:
- `bool`: `True`, если PDF успешно сохранен, иначе `False`.

**Вызывает исключения**:
- `pdfkit.PDFKitError`: Если происходит ошибка при генерации PDF с использованием `pdfkit`.
- `OSError`: Если происходит ошибка доступа к файлу.
- `FileNotFoundError`: Если `wkhtmltopdf.exe` не найден.

**Как работает функция**:
1. Определяет путь к исполняемому файлу `wkhtmltopdf.exe`.
2. Проверяет, существует ли исполняемый файл. Если файл не существует, функция логирует ошибку и вызывает исключение `FileNotFoundError`.
3. Конфигурирует `pdfkit` с использованием указанного пути к `wkhtmltopdf.exe`.
4. Устанавливает опцию `enable-local-file-access` для обеспечения доступа к локальным файлам.
5. Проверяет тип входных данных (`data`):
   - Если `data` является строкой, функция преобразует HTML-контент в PDF, используя `pdfkit.from_string()`.
   - Если `data` является путем к файлу, функция преобразует HTML-файл в PDF, используя `pdfkit.from_file()`.
6. Логирует информацию об успешном сохранении PDF-файла.
7. Возвращает `True` в случае успешного сохранения PDF.
8. Обрабатывает возможные исключения, такие как `pdfkit.PDFKitError` и `OSError`, логирует ошибку и возвращает `False`.

**ASCII flowchart**:
```
A[Проверка наличия wkhtmltopdf.exe]
|
B[Настройка pdfkit]
|
C[Проверка типа входных данных (data)]
|
D[data - строка: pdfkit.from_string()] --> F[Логирование и возврат True]
|
E[data - файл: pdfkit.from_file()]   --> F
|
G[Обработка исключений] --> H[Логирование и возврат False]
```

**Примеры**:
```python
from pathlib import Path
from src.utils.pdf import PDFUtils

# Пример 1: Сохранение HTML-контента в PDF
html_content = "<html><body><h1>Hello, PDF!</h1></body></html>"
pdf_file = "example1.pdf"
result = PDFUtils.save_pdf_pdfkit(html_content, pdf_file)
print(f"PDF сохранен: {result}")

# Пример 2: Сохранение HTML-файла в PDF
html_file = Path("example.html")
html_file.write_text("<html><body><h1>Hello, PDF!</h1></body></html>")
pdf_file = "example2.pdf"
result = PDFUtils.save_pdf_pdfkit(html_file, pdf_file)
print(f"PDF сохранен: {result}")
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

**Назначение**: Сохраняет текст в PDF с использованием библиотеки FPDF.

**Параметры**:
- `data` (str): Текст, который необходимо сохранить в PDF.
- `pdf_file` (str | Path): Путь к сохраняемому PDF-файлу.

**Возвращает**:
- `bool`: `True`, если PDF успешно сохранен, иначе `False`.

**Вызывает исключения**:
- `FileNotFoundError`: Если JSON файл установки шрифтов или файл шрифта не найден.
- Различные исключения, которые могут возникнуть при работе с FPDF.

**Как работает функция**:
1. Импортирует класс `FPDF` из библиотеки `fpdf`.
2. Создает экземпляр класса `FPDF`.
3. Добавляет новую страницу в PDF-документ.
4. Устанавливает автоматический перенос текста и отступ от края страницы.
5. Определяет путь к файлу `fonts.json`, содержащему информацию о шрифтах.
6. Проверяет, существует ли файл `fonts.json`. Если файл не существует, функция логирует ошибку и вызывает исключение `FileNotFoundError`.
7. Открывает файл `fonts.json`, загружает информацию о шрифтах.
8. Для каждого шрифта, указанного в `fonts.json`, проверяет наличие файла шрифта. Если файл шрифта не найден, функция логирует ошибку и вызывает исключение `FileNotFoundError`.
9. Добавляет шрифт в PDF-документ, используя информацию из `fonts.json`.
10. Устанавливает шрифт по умолчанию.
11. Добавляет текст в PDF-документ, используя метод `multi_cell`.
12. Сохраняет PDF-документ в указанный файл.
13. Логирует информацию об успешном сохранении PDF-файла.
14. Возвращает `True` в случае успешного сохранения PDF.
15. Обрабатывает возможные исключения, логирует ошибку и возвращает `False`.

**ASCII flowchart**:
```
A[Инициализация FPDF]
|
B[Поиск и загрузка fonts.json]
|
C[Проверка наличия файла шрифтов]
|
D[Добавление шрифтов]
|
E[Установка шрифта и добавление текста]
|
F[Сохранение PDF]
|
G[Обработка исключений]
```

**Примеры**:
```python
from src.utils.pdf import PDFUtils

# Пример: Сохранение текста в PDF с использованием FPDF
text_data = "Hello, PDF with FPDF!"
pdf_file = "example_fpdf.pdf"
result = PDFUtils.save_pdf_fpdf(text_data, pdf_file)
print(f"PDF сохранен: {result}")
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

**Назначение**: Сохраняет HTML-контент или файл в PDF с использованием библиотеки `WeasyPrint`.

**Параметры**:
- `data` (str | Path): HTML-контент в виде строки или путь к HTML-файлу.
- `pdf_file` (str | Path): Путь к сохраняемому PDF-файлу.

**Возвращает**:
- `bool`: `True`, если PDF успешно сохранен, иначе `False`.

**Как работает функция**:
1. Импортирует класс `HTML` из библиотеки `weasyprint`.
2. Проверяет тип входных данных (`data`):
   - Если `data` является строкой, функция преобразует HTML-контент в PDF, используя `HTML(string=data).write_pdf(pdf_file)`.
   - Если `data` является путем к файлу, функция преобразует HTML-файл в PDF, используя `HTML(filename=str(data)).write_pdf(pdf_file)`.
3. Логирует информацию об успешном сохранении PDF-файла.
4. Возвращает `True` в случае успешного сохранения PDF.
5. Обрабатывает возможные исключения, логирует ошибку и возвращает `False`.

**ASCII flowchart**:
```
A[Импорт HTML из weasyprint]
|
B[Проверка типа входных данных (data)]
|
C[data - строка: HTML(string=data).write_pdf()] --> E[Логирование и возврат True]
|
D[data - файл: HTML(filename=str(data)).write_pdf()]   --> E
|
F[Обработка исключений] --> G[Логирование и возврат False]
```

**Примеры**:
```python
from pathlib import Path
from src.utils.pdf import PDFUtils

# Пример 1: Сохранение HTML-контента в PDF
html_content = "<html><body><h1>Hello, PDF!</h1></body></html>"
pdf_file = "example_weasyprint1.pdf"
result = PDFUtils.save_pdf_weasyprint(html_content, pdf_file)
print(f"PDF сохранен: {result}")

# Пример 2: Сохранение HTML-файла в PDF
html_file = Path("example.html")
html_file.write_text("<html><body><h1>Hello, PDF!</h1></body></html>")
pdf_file = "example_weasyprint2.pdf"
result = PDFUtils.save_pdf_weasyprint(html_file, pdf_file)
print(f"PDF сохранен: {result}")
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

**Назначение**: Сохраняет HTML-контент или файл в PDF с использованием библиотеки `xhtml2pdf`.

**Параметры**:
- `data` (str | Path): HTML-контент в виде строки или путь к HTML-файлу.
- `pdf_file` (str | Path): Путь к сохраняемому PDF-файлу.

**Возвращает**:
- `bool`: `True`, если PDF успешно сохранен, иначе `False`.

**Как работает функция**:
1. Импортирует класс `pisa` из библиотеки `xhtml2pdf`.
2. Открывает файл для записи PDF в бинарном режиме (`"w+b"`).
3. Проверяет тип входных данных (`data`):
   - Если `data` является строкой, кодирует строку в UTF-8 и создает PDF из HTML-контента с использованием `pisa.CreatePDF(data, dest=result_file)`.
   - Если `data` является путем к файлу, открывает HTML-файл в кодировке UTF-8, читает содержимое и создает PDF из HTML-контента с использованием `pisa.CreatePDF(source_data, dest=result_file, encoding='UTF-8')`.
4. Логирует информацию об успешном сохранении PDF-файла.
5. Возвращает `True` в случае успешного сохранения PDF.
6. Обрабатывает возможные исключения, логирует ошибку и возвращает `False`.

**ASCII flowchart**:
```
A[Импорт pisa из xhtml2pdf]
|
B[Открытие PDF-файла для записи]
|
C[Проверка типа входных данных (data)]
|
D[data - строка: pisa.CreatePDF(data, dest=result_file)] --> F[Логирование и возврат True]
|
E[data - файл: pisa.CreatePDF(source_data, dest=result_file, encoding='UTF-8')]   --> F
|
G[Обработка исключений] --> H[Логирование и возврат False]
```

**Примеры**:
```python
from pathlib import Path
from src.utils.pdf import PDFUtils

# Пример 1: Сохранение HTML-контента в PDF
html_content = "<html><body><h1>Hello, PDF!</h1></body></html>"
pdf_file = "example_xhtml2pdf1.pdf"
result = PDFUtils.save_pdf_xhtml2pdf(html_content, pdf_file)
print(f"PDF сохранен: {result}")

# Пример 2: Сохранение HTML-файла в PDF
html_file = Path("example.html")
html_file.write_text("<html><body><h1>Hello, PDF!</h1></body></html>")
pdf_file = "example_xhtml2pdf2.pdf"
result = PDFUtils.save_pdf_xhtml2pdf(html_file, pdf_file)
print(f"PDF сохранен: {result}")
```

### `html2pdf`

```python
@staticmethod
def html2pdf(html_str: str, pdf_file: str | Path) -> bool | None:
    """Converts HTML content to a PDF file using WeasyPrint."""
```

**Назначение**: Конвертирует HTML-контент в PDF-файл с использованием библиотеки `WeasyPrint`.

**Параметры**:
- `html_str` (str): HTML-контент для конвертации.
- `pdf_file` (str | Path): Путь к сохраняемому PDF-файлу.

**Возвращает**:
- `bool | None`: `True`, если PDF успешно создан, иначе `None`.

**Как работает функция**:
1. Импортирует класс `HTML` из библиотеки `weasyprint`.
2. Использует `HTML(string=html_str).write_pdf(pdf_file)` для создания PDF-файла из HTML-контента.
3. Возвращает `True` в случае успеха.
4. В случае возникновения исключения выводит сообщение об ошибке и возвращает `None`.

**ASCII flowchart**:
```
A[Импорт HTML из weasyprint]
|
B[Создание PDF из HTML: HTML(string=html_str).write_pdf()]
|
C[Обработка исключений]
```

**Примеры**:
```python
from src.utils.pdf import PDFUtils

# Пример: Преобразование HTML-контента в PDF
html_content = "<html><body><h1>Hello, PDF!</h1></body></html>"
pdf_file = "example_html2pdf.pdf"
result = PDFUtils.html2pdf(html_content, pdf_file)
print(f"PDF создан: {result}")
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
1. Импортирует функцию `extract_text` из библиотеки `pdfminer.high_level`.
2. Извлекает текст из PDF-файла с использованием `extract_text(str(pdf_file))`.
3. Открывает HTML-файл для записи в кодировке UTF-8.
4. Записывает HTML-структуру с извлеченным текстом в файл.
5. Выводит сообщение об успешном сохранении HTML-файла.
6. Возвращает `True` в случае успеха.
7. В случае возникновения исключения выводит сообщение об ошибке и возвращает `False`.

**ASCII flowchart**:
```
A[Импорт extract_text из pdfminer]
|
B[Извлечение текста из PDF]
|
C[Открытие HTML-файла для записи]
|
D[Запись HTML-структуры с текстом в файл]
|
E[Обработка исключений]
```

**Примеры**:
```python
from pathlib import Path
from src.utils.pdf import PDFUtils

# Пример: Конвертация PDF-файла в HTML
pdf_file = Path("example.pdf")  # Укажите путь к существующему PDF-файлу
html_file = "example.html"
result = PDFUtils.pdf_to_html(pdf_file, html_file)
print(f"HTML сохранен: {result}")
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
- `data` (Any): Словарь или объект `SimpleNamespace` для конвертации в PDF.
- `file_path` (str | Path): Путь к выходному PDF-файлу.

**Как работает функция**:
1. Проверяет, является ли входной параметр `data` экземпляром `SimpleNamespace`, и если да, преобразует его в словарь.
2. Создает объект `Canvas` из библиотеки `reportlab.pdfgen` для создания PDF-файла.
3. Устанавливает шрифт "Helvetica" размером 12.
4. Перебирает элементы словаря и записывает каждую пару ключ-значение в PDF-файл, начиная с координат (50, height - 50), где height - высота страницы A4.
5. Уменьшает координату `y` на 20 после каждой записи.
6. Если координата `y` становится меньше 50, создает новую страницу и сбрасывает координату `y` к верхней части страницы.
7. Сохраняет PDF-файл.

**ASCII flowchart**:
```
A[Проверка типа данных (SimpleNamespace -> dict)]
|
B[Создание Canvas]
|
C[Установка шрифта]
|
D[Перебор элементов словаря]
|
E[Запись пары ключ-значение в PDF]
|
F[Проверка необходимости создания новой страницы]
|
G[Сохранение PDF]
```

**Примеры**:
```python
from pathlib import Path
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from src.utils.pdf import PDFUtils

# Пример: Сохранение словаря в PDF
data = {"name": "John Doe", "age": 30, "city": "New York"}
file_path = "example_dict2pdf.pdf"
PDFUtils.dict2pdf(data, file_path)