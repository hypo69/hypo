# Модуль `hypotez/src/utils/pdf.py`

## Обзор

Этот модуль предоставляет инструменты для преобразования HTML-контента или файлов в PDF-формат с использованием библиотек `pdfkit` и `reportlab.pdfgen`. Он также включает альтернативный метод сохранения текста в PDF через `fpdf`.

## Установка зависимостей

Для корректной работы модуля необходимо установить следующие библиотеки:

- `pdfkit`
- `reportlab`
- `fpdf`

## Переменные

### `MODE`

Строковая переменная, хранящая текущий режим работы (например, 'dev', 'prod').

### `wkhtmltopdf_exe`

Путь к исполняемому файлу `wkhtmltopdf`.


## Функции

### `set_project_root`

**Описание**: Находит корневую директорию проекта, начиная с директории текущего файла.

**Параметры**:
- `marker_files` (tuple, опционально): Кортеж имен файлов или директорий, по которым определяется корень проекта. По умолчанию: `('pyproject.toml', 'requirements.txt', '.git')`.

**Возвращает**:
- `Path`: Путь к корневой директории проекта, если найдена, иначе путь к директории, где находится скрипт.

### `PDFUtils.save_pdf`

**Описание**: Сохраняет HTML-контент или файл в PDF.

**Параметры**:
- `data` (str | Path): HTML-контент или путь к HTML-файлу.
- `pdf_file` (str | Path): Путь к сохраняемому PDF-файлу.

**Возвращает**:
- `bool`: `True`, если PDF успешно сохранен, иначе `False`.

**Возможные исключения**:
- `pdfkit.PDFKitError`: Ошибка генерации PDF через `pdfkit`.
- `OSError`: Ошибка доступа к файлу.
- `Exception`: Другие неожиданные ошибки.

### `PDFUtils.save_pdf_v2`

**Описание**: Альтернативный метод сохранения текста в PDF с использованием библиотеки FPDF.

**Параметры**:
- `data` (str): Текст, который необходимо сохранить в PDF.
- `pdf_file` (str | Path): Путь к сохраняемому PDF-файлу.

**Возвращает**:
- `bool`: `True`, если PDF успешно сохранен, иначе `False`.

**Возможные исключения**:
- `Exception`: Любые ошибки, возникающие во время работы с FPDF.


## Классы

### `PDFUtils`

**Описание**: Класс для работы с PDF-файлами, предоставляющий методы для сохранения HTML-контента в PDF.


```