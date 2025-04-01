# Модуль конвертации PDF в HTML

## Обзор

Модуль предназначен для конвертации PDF-файлов в HTML-формат. В частности, он использует утилиту `PDFUtils` для выполнения преобразования.

## Подробней

Этот модуль предоставляет функцию `pdf2html`, которая принимает путь к PDF-файлу и путь для сохранения HTML-файла. Он использует библиотеку `PDFUtils` для конвертации PDF в HTML. Код предназначен для автоматизации процесса конвертации PDF-документов в HTML-формат. 

## Функции

### `pdf2html`

```python
def pdf2html(pdf_file, html_file):
    """ """
```

**Назначение**: Конвертирует PDF-файл в HTML-файл.

**Параметры**:
- `pdf_file` (str | Path): Путь к PDF-файлу, который нужно конвертировать.
- `html_file` (str | Path): Путь для сохранения сгенерированного HTML-файла.

**Возвращает**:
- `None`: Функция ничего не возвращает.

**Как работает функция**:
1. Функция `pdf2html` использует метод `pdf_to_html` из класса `PDFUtils` для преобразования PDF-файла в HTML.
2. Внутри `PDFUtils.pdf_to_html` происходит процесс извлечения текста и форматирования из PDF-файла и записи его в HTML-файл.

**Примеры**:

```python
pdf_file = gs.path.root / 'assets' / 'materials' / '101_BASIC_Computer_Games_Mar75.pdf'
html_file = gs.path.root / 'assets' / 'materials' / '101_BASIC_Computer_Games_Mar75.html'

pdf2html(pdf_file, html_file)
```
В данном примере, PDF файл `'101_BASIC_Computer_Games_Mar75.pdf'`, расположенный в директории `'assets/materials'`, конвертируется в HTML файл `'101_BASIC_Computer_Games_Mar75.html'`, расположенный в той же директории.