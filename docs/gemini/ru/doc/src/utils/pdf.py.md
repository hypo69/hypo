# Модуль для работы с PDF-файлами
=================================

Модуль `src.utils.pdf` предназначен для преобразования HTML-контента или файлов в PDF с использованием различных библиотек.
Он предоставляет класс :class:`PDFUtils`, который содержит статические методы для сохранения HTML в PDF, текста в PDF, а также для конвертации PDF в HTML и словаря в PDF.

Примеры использования и дополнительная информация:
- https://chatgpt.com/share/672266a3-0048-800d-a97b-c38f647d496b
- https://stackoverflow.com/questions/73599970/how-to-solve-wkhtmltopdf-reported-an-error-exit-with-code-1-due-to-network-err
- https://habr.com/ru/companies/bothub/articles/853490/

## Обзор

Модуль предоставляет статические методы класса :class:`PDFUtils` для работы с PDF-файлами. Он позволяет сохранять HTML-контент и файлы в PDF, а также конвертировать PDF в HTML.
Поддерживаются различные библиотеки для работы с PDF, такие как `pdfkit`, `FPDF`, `WeasyPrint` и `xhtml2pdf`.

## Подробней

Модуль `src.utils.pdf` предоставляет инструменты для работы с PDF-файлами, позволяя сохранять данные в формате PDF из различных источников, таких как HTML-контент, HTML-файлы и текст.
Он использует несколько библиотек для достижения этой цели, каждая из которых имеет свои особенности и преимущества. Выбор библиотеки зависит от конкретной задачи и требований к форматированию PDF.

## Классы

### `PDFUtils`

**Описание**: Класс `PDFUtils` предоставляет статические методы для работы с PDF-файлами. Он содержит методы для сохранения HTML-контента в PDF с использованием различных библиотек, сохранения текста в PDF, а также для конвертации PDF в HTML.

**Принцип работы**:

Класс `PDFUtils` предоставляет набор статических методов, каждый из которых использует определенную библиотеку Python для работы с PDF-файлами.
Метод `save_pdf_pdfkit` использует библиотеку `pdfkit` для сохранения HTML-контента или файла в PDF.
Метод `save_pdf_fpdf` использует библиотеку `FPDF` для сохранения текста в PDF.
Метод `save_pdf_weasyprint` использует библиотеку `WeasyPrint` для сохранения HTML-контента или файла в PDF.
Метод `save_pdf_xhtml2pdf` использует библиотеку `xhtml2pdf` для сохранения HTML-контента или файла в PDF.
Метод `pdf_to_html` конвертирует PDF-файл в HTML-файл.
Метод `dict2pdf` сохраняет данные словаря в PDF-файл.

**Методы**:
- `save_pdf_pdfkit`: Сохраняет HTML-контент или файл в PDF с использованием библиотеки `pdfkit`.
- `save_pdf_fpdf`: Сохраняет текст в PDF с использованием библиотеки `FPDF`.
- `save_pdf_weasyprint`: Сохраняет HTML-контент или файл в PDF с использованием библиотеки `WeasyPrint`.
- `save_pdf_xhtml2pdf`: Сохраняет HTML-контент или файл в PDF с использованием библиотеки `xhtml2pdf`.
- `html2pdf`: Преобразует HTML-контент в PDF-файл, используя WeasyPrint.
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

**Назначение**: Функция `save_pdf_pdfkit` сохраняет HTML-контент или HTML-файл в PDF-файл, используя библиотеку `pdfkit`.

**Параметры**:
- `data` (str | Path): HTML-контент в виде строки или путь к HTML-файлу.
- `pdf_file` (str | Path): Путь к сохраняемому PDF-файлу.

**Возвращает**:
- `bool`: `True`, если PDF успешно сохранен, иначе `False`.

**Вызывает исключения**:
- `pdfkit.PDFKitError`: Если произошла ошибка при генерации PDF с использованием `pdfkit`.
- `OSError`: Если произошла ошибка при доступе к файлу.

**Как работает функция**:

1. Определяется путь к исполняемому файлу `wkhtmltopdf.exe`, который необходим для работы `pdfkit`.
2. Проверяется существование файла `wkhtmltopdf.exe` по указанному пути. Если файл не найден, функция логирует ошибку и вызывает исключение `FileNotFoundError`.
3. Настраивается конфигурация `pdfkit` с указанием пути к `wkhtmltopdf.exe`.
4. Устанавливаются опции, разрешающие доступ к локальным файлам.
5. В зависимости от типа данных (`str` или `Path`) вызывается метод `pdfkit.from_string` для сохранения HTML-контента или метод `pdfkit.from_file` для сохранения HTML-файла в PDF.
6. В случае успешного сохранения PDF, функция логирует информацию об успешном сохранении и возвращает `True`.
7. Если происходит исключение во время процесса сохранения, функция логирует ошибку и возвращает `False`.

**ASCII flowchart**:

```
A[Начало]
|
B[Проверка наличия wkhtmltopdf.exe]
|
C[Настройка конфигурации pdfkit]
|
D[Определение типа данных (HTML-контент или файл)]
|
E[Сохранение в PDF (pdfkit.from_string или pdfkit.from_file)]
|
F[Логирование и возврат результата]
|
G[Конец]
```

**Примеры**:

```python
from pathlib import Path
from src.utils.pdf import PDFUtils

# Пример 1: Сохранение HTML-контента в PDF
html_content = "<html><body><h1>Hello, PDF!</h1></body></html>"
pdf_file_path = "example.pdf"
result = PDFUtils.save_pdf_pdfkit(html_content, pdf_file_path)
print(f"PDF saved successfully: {result}")

# Пример 2: Сохранение HTML-файла в PDF
html_file_path = Path("example.html")
html_file_path.write_text(html_content) # Создаем файл example.html с содержимым html_content
pdf_file_path = "example_from_file.pdf"
result = PDFUtils.save_pdf_pdfkit(html_file_path, pdf_file_path)
print(f"PDF saved successfully: {result}")
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

**Назначение**: Функция `save_pdf_fpdf` сохраняет текст в PDF-файл, используя библиотеку `FPDF`.

**Параметры**:
- `data` (str): Текст, который необходимо сохранить в PDF.
- `pdf_file` (str | Path): Путь к сохраняемому PDF-файлу.

**Возвращает**:
- `bool`: `True`, если PDF успешно сохранен, иначе `False`.

**Как работает функция**:

1. Импортируется класс `FPDF` из библиотеки `fpdf`.
2. Создается экземпляр класса `FPDF`.
3. Добавляется новая страница в PDF-документ.
4. Устанавливается автоматический перенос страниц и отступ от края страницы.
5. Определяется путь к файлу `fonts.json`, который содержит информацию о шрифтах.
6. Проверяется существование файла `fonts.json` по указанному пути. Если файл не найден, функция логирует ошибку, предоставляет информацию о формате файла и вызывает исключение `FileNotFoundError`.
7. Открывается файл `fonts.json` и загружается информация о шрифтах.
8. Добавляются шрифты, указанные в файле `fonts.json`, в PDF-документ. Для каждого шрифта проверяется существование файла шрифта по указанному пути. Если файл не найден, функция логирует ошибку и вызывает исключение `FileNotFoundError`.
9. Устанавливается шрифт по умолчанию для текста в PDF-документе.
10. Добавляется текст в PDF-документ с использованием метода `multi_cell`.
11. Сохраняется PDF-документ в файл по указанному пути.
12. В случае успешного сохранения PDF, функция логирует информацию об успешном сохранении и возвращает `True`.
13. Если происходит исключение во время процесса сохранения, функция логирует ошибку и возвращает `False`.

**ASCII flowchart**:

```
A[Начало]
|
B[Импорт FPDF и создание экземпляра]
|
C[Настройка страницы PDF]
|
D[Проверка наличия fonts.json]
|
E[Загрузка информации о шрифтах]
|
F[Добавление шрифтов в PDF]
|
G[Установка шрифта по умолчанию]
|
H[Добавление текста в PDF]
|
I[Сохранение PDF]
|
J[Логирование и возврат результата]
|
K[Конец]
```

**Примеры**:

```python
from pathlib import Path
from src.utils.pdf import PDFUtils

# Пример: Сохранение текста в PDF
text_data = "Hello, PDF! This is a test."
pdf_file_path = "example_fpdf.pdf"
result = PDFUtils.save_pdf_fpdf(text_data, pdf_file_path)
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

**Назначение**: Функция `save_pdf_weasyprint` сохраняет HTML-контент или HTML-файл в PDF-файл, используя библиотеку `WeasyPrint`.

**Параметры**:
- `data` (str | Path): HTML-контент в виде строки или путь к HTML-файлу.
- `pdf_file` (str | Path): Путь к сохраняемому PDF-файлу.

**Возвращает**:
- `bool`: `True`, если PDF успешно сохранен, иначе `False`.

**Как работает функция**:

1. Импортируется класс `HTML` из библиотеки `weasyprint`.
2. В зависимости от типа данных (`str` или `Path`) вызывается метод `HTML(string=data).write_pdf(pdf_file)` для сохранения HTML-контента или метод `HTML(filename=str(data)).write_pdf(pdf_file)` для сохранения HTML-файла в PDF.
3. В случае успешного сохранения PDF, функция логирует информацию об успешном сохранении и возвращает `True`.
4. Если происходит исключение во время процесса сохранения, функция логирует ошибку и возвращает `False`.

**ASCII flowchart**:

```
A[Начало]
|
B[Импорт HTML из weasyprint]
|
C[Определение типа данных (HTML-контент или файл)]
|
D[Сохранение в PDF (HTML(string=data).write_pdf или HTML(filename=str(data)).write_pdf)]
|
E[Логирование и возврат результата]
|
F[Конец]
```

**Примеры**:

```python
from pathlib import Path
from src.utils.pdf import PDFUtils

# Пример 1: Сохранение HTML-контента в PDF
html_content = "<html><body><h1>Hello, PDF!</h1></body></html>"
pdf_file_path = "example_weasyprint.pdf"
result = PDFUtils.save_pdf_weasyprint(html_content, pdf_file_path)
print(f"PDF saved successfully: {result}")

# Пример 2: Сохранение HTML-файла в PDF
html_file_path = Path("example.html")
html_file_path.write_text(html_content) # Создаем файл example.html с содержимым html_content
pdf_file_path = "example_from_file_weasyprint.pdf"
result = PDFUtils.save_pdf_weasyprint(html_file_path, pdf_file_path)
print(f"PDF saved successfully: {result}")
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

**Назначение**: Функция `save_pdf_xhtml2pdf` сохраняет HTML-контент или HTML-файл в PDF-файл, используя библиотеку `xhtml2pdf`.

**Параметры**:
- `data` (str | Path): HTML-контент в виде строки или путь к HTML-файлу.
- `pdf_file` (str | Path): Путь к сохраняемому PDF-файлу.

**Возвращает**:
- `bool`: `True`, если PDF успешно сохранен, иначе `False`.

**Как работает функция**:

1. Импортируется модуль `pisa` из библиотеки `xhtml2pdf`.
2. Открывается файл для записи PDF по указанному пути.
3. В зависимости от типа данных (`str` или `Path`) происходит следующее:
    - Если данные - строка (HTML-контент), то строка кодируется в UTF-8. Затем вызывается функция `pisa.CreatePDF` для создания PDF из HTML-контента.
    - Если данные - путь к файлу (HTML-файл), то файл открывается для чтения в кодировке UTF-8, содержимое считывается, и вызывается функция `pisa.CreatePDF` для создания PDF из содержимого файла.
4. В случае успешного сохранения PDF, функция логирует информацию об успешном сохранении и возвращает `True`.
5. Если происходит исключение во время процесса сохранения, функция логирует ошибку и возвращает `False`.

**ASCII flowchart**:

```
A[Начало]
|
B[Импорт pisa из xhtml2pdf]
|
C[Открытие файла для записи PDF]
|
D[Определение типа данных (HTML-контент или файл)]
|
E[Сохранение в PDF (pisa.CreatePDF)]
|
F[Логирование и возврат результата]
|
G[Конец]
```

**Примеры**:

```python
from pathlib import Path
from src.utils.pdf import PDFUtils

# Пример 1: Сохранение HTML-контента в PDF
html_content = "<html><body><h1>Hello, PDF!</h1></body></html>"
pdf_file_path = "example_xhtml2pdf.pdf"
result = PDFUtils.save_pdf_xhtml2pdf(html_content, pdf_file_path)
print(f"PDF saved successfully: {result}")

# Пример 2: Сохранение HTML-файла в PDF
html_file_path = Path("example.html")
html_file_path.write_text(html_content) # Создаем файл example.html с содержимым html_content
pdf_file_path = "example_from_file_xhtml2pdf.pdf"
result = PDFUtils.save_pdf_xhtml2pdf(html_file_path, pdf_file_path)
print(f"PDF saved successfully: {result}")
```

### `html2pdf`

```python
def html2pdf(html_str: str, pdf_file: str | Path) -> bool | None:
    """Converts HTML content to a PDF file using WeasyPrint."""
```

**Назначение**: Функция `html2pdf` преобразует HTML-контент в PDF-файл, используя библиотеку `WeasyPrint`.

**Параметры**:
- `html_str` (str): HTML-контент в виде строки.
- `pdf_file` (str | Path): Путь к сохраняемому PDF-файлу.

**Возвращает**:
- `bool | None`: `True`, если PDF успешно сохранен, иначе `None`.

**Как работает функция**:

1. Импортируется класс `HTML` из библиотеки `weasyprint`.
2. Вызывается метод `HTML(string=html_str).write_pdf(pdf_file)` для сохранения HTML-контента в PDF.
3. В случае успешного сохранения PDF, функция возвращает `True`.
4. Если происходит исключение во время процесса сохранения, функция выводит сообщение об ошибке и возвращает `None`.

**ASCII flowchart**:

```
A[Начало]
|
B[Импорт HTML из weasyprint]
|
C[Сохранение в PDF (HTML(string=html_str).write_pdf)]
|
D[Возврат результата]
|
E[Конец]
```

**Примеры**:

```python
from pathlib import Path
from src.utils.pdf import PDFUtils

# Пример: Сохранение HTML-контента в PDF
html_content = "<html><body><h1>Hello, PDF!</h1></body></html>"
pdf_file_path = "example_html2pdf.pdf"
result = PDFUtils.html2pdf(html_content, pdf_file_path)
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

**Назначение**: Функция `pdf_to_html` конвертирует PDF-файл в HTML-файл, извлекая текст из PDF и сохраняя его в HTML-файл.

**Параметры**:
- `pdf_file` (str | Path): Путь к исходному PDF-файлу.
- `html_file` (str | Path): Путь к сохраняемому HTML-файлу.

**Возвращает**:
- `bool`: `True`, если конвертация прошла успешно, иначе `False`.

**Как работает функция**:

1. Импортируется функция `extract_text` из библиотеки `pdfminer.high_level`.
2. Извлекается текст из PDF-файла с помощью функции `extract_text`.
3. Открывается файл для записи HTML по указанному пути.
4. Записывается HTML-код, содержащий извлеченный текст, в файл.
5. В случае успешной конвертации, функция выводит сообщение об успешном сохранении и возвращает `True`.
6. Если происходит исключение во время процесса конвертации, функция выводит сообщение об ошибке и возвращает `False`.

**ASCII flowchart**:

```
A[Начало]
|
B[Импорт extract_text из pdfminer]
|
C[Извлечение текста из PDF]
|
D[Открытие файла для записи HTML]
|
E[Запись HTML-кода с извлеченным текстом]
|
F[Логирование и возврат результата]
|
G[Конец]
```

**Примеры**:

```python
from pathlib import Path
from src.utils.pdf import PDFUtils

# Пример: Конвертация PDF в HTML
pdf_file_path = "example.pdf"  # Укажите путь к существующему PDF-файлу
html_file_path = "example.html"
result = PDFUtils.pdf_to_html(pdf_file_path, html_file_path)
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

**Назначение**: Функция `dict2pdf` сохраняет данные словаря в PDF-файл.

**Параметры**:
- `data` (Any): Словарь, который нужно преобразовать в PDF.
- `file_path` (str | Path): Путь к выходному PDF-файлу.

**Как работает функция**:

1. Проверяется, является ли входной параметр экземпляром `SimpleNamespace`. Если да, то он преобразуется в словарь.
2. Создается объект `Canvas` из библиотеки `reportlab.pdfgen.canvas` для создания PDF-файла.
3. Определяются размеры страницы A4.
4. Устанавливается шрифт "Helvetica" размером 12.
5. Итерируется по элементам словаря. Для каждой пары ключ-значение создается строка, которая выводится на PDF-страницу.
6. Если текущая позиция по высоте становится меньше 50, создается новая страница.
7. Сохраняется PDF-файл.

**ASCII flowchart**:

```
A[Начало]
|
B[Проверка типа данных (SimpleNamespace -> dict)]
|
C[Создание Canvas]
|
D[Установка шрифта]
|
E[Итерация по словарю]
|
F[Вывод данных на страницу]
|
G[Проверка высоты страницы]
|
H[Создание новой страницы (если необходимо)]
|
I[Сохранение PDF]
|
J[Конец]
```

**Примеры**:

```python
from pathlib import Path
from types import SimpleNamespace
from src.utils.pdf import PDFUtils

# Пример 1: Сохранение словаря в PDF
data = {"name": "John Doe", "age": 30, "city": "New York"}
file_path = "example_dict.pdf"
PDFUtils.dict2pdf(data, file_path)

# Пример 2: Сохранение SimpleNamespace в PDF
data = SimpleNamespace(name="Jane Doe", age=25, city="Los Angeles")
file_path = "example_simplenamespace.pdf"
PDFUtils.dict2pdf(data, file_path)