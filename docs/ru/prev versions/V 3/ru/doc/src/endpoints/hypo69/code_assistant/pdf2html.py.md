# Модуль pdf2html

## Обзор

Модуль `pdf2html.py` предназначен для конвертации PDF-файлов в HTML-формат. Он использует утилиты из `src.utils.pdf` для выполнения преобразования.

## Подробней

Этот модуль является частью проекта `hypotez` и выполняет важную задачу преобразования PDF-документов в HTML, что может быть полезно для отображения содержимого PDF в веб-интерфейсе или для дальнейшей обработки текста. Расположение файла в структуре проекта указывает, что он является частью API endpoint `hypo69` и используется code_assistant.

## Функции

### `pdf2html`

```python
def pdf2html(pdf_file, html_file):
    """ """
```

**Описание**: Конвертирует PDF-файл в HTML-файл.

**Параметры**:
- `pdf_file` (str): Путь к PDF-файлу.
- `html_file` (str): Путь для сохранения HTML-файла.

**Возвращает**:
- `None`: Функция ничего не возвращает.

**Вызывает исключения**:
- Отсутствуют явные исключения, но могут быть исключения, вызванные функциями `PDFUtils.pdf_to_html`.

**Примеры**:

```python
pdf_file = gs.path.root / 'assets' / 'materials' / '101_BASIC_Computer_Games_Mar75.pdf'
html_file = gs.path.root / 'assets' / 'materials' / '101_BASIC_Computer_Games_Mar75.html'

pdf2html(pdf_file, html_file)
```