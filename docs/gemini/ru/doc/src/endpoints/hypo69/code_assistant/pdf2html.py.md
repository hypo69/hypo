# Документация для модуля pdf2html

## Обзор

Модуль `pdf2html` предназначен для конвертации PDF-файлов в HTML-формат. Он использует библиотеку `PDFUtils` для выполнения преобразования.

## Подробней

Этот модуль является частью проекта `hypotez` и служит для преобразования PDF-документов в HTML, что может быть полезно для отображения содержимого PDF-файлов в веб-интерфейсе или для дальнейшей обработки текста.

## Функции

### `pdf2html`

```python
def pdf2html(pdf_file, html_file):
    """Функция конвертирует PDF файл в HTML файл.

    Args:
        pdf_file: Путь к PDF файлу.
        html_file: Путь к HTML файлу, в который будет записан результат конвертации.

    Returns:
        None

    Raises:
        None
    """
```

**Как работает функция**:
1. Функция принимает на вход путь к PDF-файлу (`pdf_file`) и путь к HTML-файлу (`html_file`).
2. Вызывает метод `pdf_to_html` из класса `PDFUtils`, передавая ему пути к PDF и HTML файлам. Этот метод выполняет фактическое преобразование PDF в HTML.

**Параметры**:
- `pdf_file`: Путь к исходному PDF-файлу.
- `html_file`: Путь к файлу, в который будет сохранен HTML-код.

**Возвращает**:
- `None`: Функция ничего не возвращает явно.

**Пример**:

```python
pdf_file = gs.path.root / 'assets' / 'materials' / '101_BASIC_Computer_Games_Mar75.pdf'
html_file = gs.path.root / 'assets' / 'materials' / '101_BASIC_Computer_Games_Mar75.html'

pdf2html(pdf_file, html_file)