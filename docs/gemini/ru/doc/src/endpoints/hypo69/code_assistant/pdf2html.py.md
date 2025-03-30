# Модуль конвертации PDF в HTML

## Обзор

Модуль предназначен для конвертации PDF-файлов в HTML-формат. Он использует библиотеку `PDFUtils` для выполнения этой задачи.

## Подробней

Этот модуль предоставляет функцию `pdf2html`, которая принимает путь к PDF-файлу и путь к выходному HTML-файлу в качестве аргументов. Затем он использует метод `pdf_to_html` из класса `PDFUtils` для выполнения преобразования. Этот модуль полезен в проекте для преобразования PDF-документов в HTML для облегчения их отображения и анализа в веб-интерфейсе.

## Функции

### `pdf2html`

```python
def pdf2html(pdf_file, html_file):
    """ """
    PDFUtils.pdf_to_html(pdf_file, html_file)
```

**Описание**: Конвертирует PDF-файл в HTML-файл.

**Параметры**:
- `pdf_file` (str): Путь к PDF-файлу.
- `html_file` (str): Путь к выходному HTML-файлу.

**Возвращает**:
- `None`: Функция ничего не возвращает.

**Вызывает исключения**:
- `Exception`: Может вызывать исключения, если возникнут проблемы при конвертации PDF в HTML.

**Примеры**:
```python
pdf_file = gs.path.root / 'assets' / 'materials' / '101_BASIC_Computer_Games_Mar75.pdf'
html_file = gs.path.root / 'assets' / 'materials' / '101_BASIC_Computer_Games_Mar75.html'

pdf2html(pdf_file, html_file)