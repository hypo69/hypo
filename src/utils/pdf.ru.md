```rst
.. module:: src.utils.pdf
```
<TABLE >
<TR>
<TD>
<A HREF = 'https://github.com/hypo69/hypo/blob/master/readme.ru.md'>[Root ↑]</A>
</TD>
<TD>
<A HREF = 'https://github.com/hypo69/hypo/blob/master/src/readme.ru.md'>src</A> / 
<A HREF = 'https://github.com/hypo69/hypo/blob/master/src/utils/readme.ru.md'>utils</A>
</TD>
<TD>
<A HREF = 'https://github.com/hypo69/hypo/blob/master/src/utils/pdf/pdf.md'>English</A>
</TD>
</TR>
</TABLE>

# Модуль для работы с PDF-файлами

## Описание

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Модуль для работы с PDF-файлами. Предоставляет функции для преобразования HTML-контента или файлов в PDF, а также для конвертации PDF-файлов в HTML. Модуль использует несколько библиотек для выполнения этих задач, включая `pdfkit`, `FPDF`, `WeasyPrint`, `xhtml2pdf` и `pdfminer.six`.

## Основные возможности

1. **Преобразование HTML в PDF**:
   - Используется библиотека `pdfkit` для преобразования HTML-контента или файлов в PDF.
   - Поддерживаются как строки с HTML-кодом, так и файлы.

2. **Создание PDF из текста**:
   - Используется библиотека `FPDF` для создания PDF-файлов из текста.
   - Поддерживается добавление пользовательских шрифтов через файл `fonts.json`.

3. **Преобразование HTML в PDF с использованием WeasyPrint**:
   - Используется библиотека `WeasyPrint` для создания PDF-файлов из HTML-контента или файлов.

4. **Преобразование HTML в PDF с использованием xhtml2pdf**:
   - Используется библиотека `xhtml2pdf` для создания PDF-файлов из HTML-контента или файлов.

5. **Конвертация PDF в HTML**:
   - Используется библиотека `pdfminer.six` для извлечения текста из PDF-файлов и создания HTML-файлов.

## Структура модуля

### Импорты

Модуль использует следующие библиотеки:

- `pdfkit`: Для преобразования HTML в PDF.
- `FPDF`: Для создания PDF-файлов из текста.
- `WeasyPrint`: Для преобразования HTML в PDF с сохранением стилей.
- `xhtml2pdf`: Альтернатива для преобразования HTML в PDF.
- `pdfminer.six`: Для извлечения текста из PDF-файлов.
- `pathlib`: Для работы с путями файлов.
- `json`: Для загрузки конфигурации шрифтов.
- `src.logger.logger`: Пользовательский логгер для записи сообщений.
- `src.utils.printer`: Пользовательский модуль для вывода информации.

### Функция `set_project_root`

Функция определяет корневую директорию проекта на основе наличия маркерных файлов, таких как `pyproject.toml`, `requirements.txt` или `.git`. Это позволяет модулю работать независимо от текущего расположения файла.

### Класс `PDFUtils`

Класс `PDFUtils` содержит статические методы для работы с PDF-файлами:

#### Методы для создания PDF:

- **`save_pdf_pdfkit`**: Преобразует HTML-контент или файл в PDF с использованием библиотеки `pdfkit`.
- **`save_pdf_fpdf`**: Создает PDF-файл из текста с использованием библиотеки `FPDF`. Поддерживает добавление пользовательских шрифтов.
- **`save_pdf_weasyprint`**: Преобразует HTML-контент или файл в PDF с использованием библиотеки `WeasyPrint`.
- **`save_pdf_xhtml2pdf`**: Преобразует HTML-контент или файл в PDF с использованием библиотеки `xhtml2pdf`.

#### Методы для конвертации PDF:

- **`pdf_to_html`**: Конвертирует PDF-файл в HTML-файл, извлекая текст с использованием библиотеки `pdfminer.six`.

## Пример использования

### Преобразование HTML в PDF

```python
from src.utils.pdf import PDFUtils

html_content = "<h1>Пример HTML</h1><p>Это текст.</p>"
pdf_file = "output.pdf"

success = PDFUtils.save_pdf_pdfkit(html_content, pdf_file)
if success:
    print("PDF успешно создан.")
else:
    print("Ошибка при создании PDF.")
```

### Конвертация PDF в HTML

```python
from src.utils.pdf import PDFUtils

pdf_file = "example.pdf"
html_file = "example.html"

success = PDFUtils.pdf_to_html(pdf_file, html_file)
if success:
    print("HTML успешно создан.")
else:
    print("Ошибка при конвертации PDF в HTML.")
```

## Зависимости

Для работы модуля необходимо установить следующие библиотеки:

- `pdfkit`
- `FPDF`
- `WeasyPrint`
- `xhtml2pdf`
- `pdfminer.six`

Установка через `pip`:

```bash
pip install pdfkit fpdf weasyprint xhtml2pdf pdfminer.six
```

## Примечания

- Для работы `pdfkit` требуется установленный инструмент `wkhtmltopdf`. Путь к исполняемому файлу указывается в переменной `wkhtmltopdf_exe`.
- При использовании `FPDF` необходимо наличие файла `fonts.json` в директории `assets/fonts`, содержащего информацию о шрифтах.

## Ссылки

- [Документация по pdfkit](https://pypi.org/project/pdfkit/)
- [Документация по FPDF](https://pyfpdf.github.io/fpdf2/)
- [Документация по WeasyPrint](https://weasyprint.org/)
- [Документация по xhtml2pdf](https://xhtml2pdf.readthedocs.io/)
- [Документация по pdfminer.six](https://pdfminersix.readthedocs.io/)

## Автор

Автор модуля: [Ваше имя]

## Лицензия

Этот модуль распространяется под лицензией [укажите лицензию, если есть].