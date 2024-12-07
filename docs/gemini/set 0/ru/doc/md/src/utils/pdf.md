# Модуль hypotez/src/utils/pdf.py

## Обзор

Модуль `pdf.py` предназначен для преобразования HTML-контента или файлов в PDF-формат. Он использует библиотеки `pdfkit` и `fpdf` для этой цели. Модуль также включает функцию для определения корневой директории проекта.

## Функции

### `set_project_root`

**Описание**: Находит корневую директорию проекта, начиная с текущей директории, и проходя вверх по дереву директорий.

**Параметры**:

- `marker_files` (tuple): Кортеж имен файлов или директорий, по которым определяется корневая директория проекта. По умолчанию содержит `('pyproject.toml', 'requirements.txt', '.git')`.

**Возвращает**:

- `Path`: Путь к корневой директории проекта, если она найдена. В противном случае возвращает директорию, где находится текущий файл.

### `PDFUtils.save_pdf`

**Описание**: Сохраняет HTML-контент или HTML-файл в PDF-файл.

**Параметры**:

- `data` (str | Path): HTML-контент или путь к HTML-файлу.
- `pdf_file` (str | Path): Путь к сохраняемому PDF-файлу.

**Возвращает**:

- bool: `True`, если PDF успешно сохранен, иначе `False`.

**Вызывает исключения**:

- `pdfkit.PDFKitError`: Ошибка при генерации PDF через `pdfkit`.
- `OSError`: Ошибка доступа к файлу.
- `Exception`: Любые другие ошибки.


### `PDFUtils.save_pdf_v2`

**Описание**: Альтернативный метод сохранения текста в PDF с использованием библиотеки `FPDF`.

**Параметры**:

- `data` (str): Текст, который необходимо сохранить в PDF.
- `pdf_file` (str | Path): Путь к сохраняемому PDF-файлу.


**Возвращает**:

- bool: `True`, если PDF успешно сохранен, иначе `False`.
- `Exception`: Любые другие ошибки.

## Переменные

### `MODE`

**Описание**: Строковая переменная, которая задает режим работы модуля. В данном случае это 'dev'.


### `wkhtmltopdf_exe`

**Описание**: Путь к исполняемому файлу `wkhtmltopdf`.


### `__root__`

**Описание**: Переменная, хранящая путь к корневой директории проекта. Получается с помощью функции `set_project_root`.


### `configuration`

**Описание**: Настройка конфигурации для библиотеки `pdfkit`.


### `options`

**Описание**: Словарь с настройками для преобразования HTML в PDF.


## Классы

### `PDFUtils`

**Описание**: Класс для работы с PDF-файлами.


```