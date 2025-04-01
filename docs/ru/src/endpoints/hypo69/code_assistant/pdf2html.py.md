# Модуль конвертации PDF в HTML

## Обзор

Модуль предназначен для конвертации PDF-файлов в HTML-формат. Он использует утилиты из модуля `src.utils.pdf` для выполнения преобразования.

## Подробней

Данный код обеспечивает функциональность преобразования PDF-документов в HTML, что может быть полезно для отображения содержимого PDF в веб-интерфейсах или для дальнейшей обработки текста.

## Функции

### `pdf2html`

```python
def pdf2html(pdf_file, html_file):
    """ """
    PDFUtils.pdf_to_html(pdf_file, html_file)
```

**Назначение**: Преобразует PDF-файл в HTML-файл.

**Параметры**:
- `pdf_file` (str): Путь к исходному PDF-файлу.
- `html_file` (str): Путь к выходному HTML-файлу.

**Возвращает**:
- `None`: Функция ничего не возвращает явно.

**Вызывает исключения**:
- Возможные исключения, возникающие при работе `PDFUtils.pdf_to_html`, не обрабатываются в данной функции, поэтому могут быть проброшены выше.

**Как работает функция**:

1. Функция `pdf2html` принимает пути к PDF-файлу (`pdf_file`) и HTML-файлу (`html_file`) в качестве аргументов.
2. Она вызывает метод `pdf_to_html` из класса `PDFUtils`, передавая ему пути к входному и выходному файлам.
3. Метод `pdf_to_html` выполняет фактическое преобразование PDF в HTML и сохраняет результат в указанный HTML-файл.

ASCII flowchart:

```
PDF file --> PDFUtils.pdf_to_html() --> HTML file
```

**Примеры**:

```python
from src.endpoints.hypo69.code_assistant.pdf2html import pdf2html
from src import gs

pdf_file = gs.path.root / 'assets' / 'materials' / 'example.pdf'
html_file = gs.path.root / 'assets' / 'materials' / 'example.html'

pdf2html(pdf_file, html_file)