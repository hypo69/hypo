## ИНСТРУКЦИЯ:

Анализируй предоставленный код подробно и объясни его функциональность. Ответ должен включать три раздела:

1. **<алгоритм>**: Опиши рабочий процесс в виде пошаговой блок-схемы, включая примеры для каждого логического блока, и проиллюстрируй поток данных между функциями, классами или методами.
2. **<mermaid>**: Напиши код для диаграммы в формате `mermaid`, проанализируй и объясни все зависимости,
    которые импортируются при создании диаграммы.
    **ВАЖНО!** Убедитесь, что все имена переменных, используемые в диаграмме `mermaid`,
    имеют осмысленные и описательные имена. Имена переменных вроде `A`, `B`, `C`, и т.д., не допускаются!

    **Дополнительно**: Если в коде есть импорт `import header`, добавьте блок `mermaid` flowchart, объясняющий `header.py`:
    ```mermaid
    flowchart TD
        Start --> Header[<code>header.py</code><br> Determine Project Root]

        Header --> import[Import Global Settings: <br><code>from src import gs</code>]
    ```

3. **<объяснение>**: Предоставьте подробные объяснения:
   - **Импорты**: Их назначение и взаимосвязь с другими пакетами `src.`.
   - **Классы**: Их роль, атрибуты, методы и взаимодействие с другими компонентами проекта.
   - **Функции**: Их аргументы, возвращаемые значения, назначение и примеры.
   - **Переменные**: Их типы и использование.
   - Выделите потенциальные ошибки или области для улучшения.

Дополнительно, постройте цепочку взаимосвязей с другими частями проекта (если применимо).

Это обеспечивает всесторонний и структурированный анализ кода.
## Формат ответа: `.md` (markdown)
**КОНЕЦ ИНСТРУКЦИИ**
```markdown
## <алгоритм>

1.  **`set_project_root(marker_files)`**:
    *   **Начало**: Функция принимает кортеж `marker_files` (по умолчанию `('__root__', '.git')`) в качестве аргумента.
    *   **Определение начального пути**: Определяет путь к каталогу, в котором находится текущий файл (`__file__`).
    *   **Поиск корневого каталога**:  Начиная с текущего каталога, проходит вверх по структуре каталогов, проверяя наличие файлов/каталогов, указанных в `marker_files` в каждом родительском каталоге.
    *   **Установка корневого каталога**: Как только один из `marker_files` найден, путь к родительскому каталогу устанавливается в переменную `__root__`, и цикл завершается. Если ни один из маркеров не найден, то `__root__`  остается текущим каталогом.
    *   **Добавление корневого каталога в sys.path**: Если корневой каталог (`__root__`) ещё не добавлен в `sys.path`, то он добавляется.
    *   **Возврат**: Функция возвращает `__root__` (объект `Path`).
    
    *Пример:*
    Если текущий файл находится в `project/src/utils/pdf.py`, а в `project` есть файл `.git`, то функция вернет `project`.

2.  **Инициализация `__root__` и `wkhtmltopdf_exe`**:
    *   `__root__` устанавливается с помощью вызова `set_project_root()`.
    *   `wkhtmltopdf_exe` - формируется путь к исполняемому файлу `wkhtmltopdf.exe`, находящемуся в `bin/wkhtmltopdf/files/bin` относительно корневого каталога.
    *   **Проверка существования `wkhtmltopdf_exe`**: Если файл `wkhtmltopdf.exe` не существует по сформированному пути,  то в лог записывается ошибка и возбуждается исключение `FileNotFoundError`.

3.  **Класс `PDFUtils`**:
    *   Содержит статические методы для генерации PDF.

4.  **`PDFUtils.save_pdf_pdfkit(data, pdf_file)`**:
    *   **Входные данные:**
        *   `data`: HTML контент (строка) или путь к HTML-файлу (`str | Path`).
        *   `pdf_file`: Путь, по которому нужно сохранить PDF-файл (`str | Path`).
    *   **Конфигурация `pdfkit`**: Создает конфигурацию для `pdfkit`, указывая путь к исполняемому файлу `wkhtmltopdf.exe`.
    *   **Определение типа входных данных `data`**:
        *   Если `data` - строка, то HTML-контент напрямую передается в `pdfkit.from_string()`.
        *   Если `data` - путь, то HTML-файл, расположенный по указанному пути передается в `pdfkit.from_file()`.
    *   **Сохранение PDF**: PDF-файл сохраняется по пути, указанному в `pdf_file`.
    *   **Обработка исключений**: Если во время генерации PDF возникает ошибка, то в лог записывается сообщение об ошибке, и функция возвращает `False`, иначе `True`.

    *Пример:*
    `PDFUtils.save_pdf_pdfkit("<h1>Hello</h1>", "output.pdf")` преобразует HTML строку в PDF.
    `PDFUtils.save_pdf_pdfkit("input.html", "output.pdf")` преобразует HTML файл в PDF.

5.  **`PDFUtils.save_pdf_fpdf(data, pdf_file)`**:
    *   **Входные данные:**
        *   `data`: Текст для записи в PDF (строка).
        *   `pdf_file`: Путь для сохранения PDF-файла (`str | Path`).
    *   **Инициализация `FPDF`**: Создает объект `FPDF` для создания PDF.
    *   **Загрузка настроек шрифтов**: Загружает настройки шрифтов из JSON-файла (`assets/fonts/fonts.json`). Если файл не найден или файл шрифта не найден, то в лог записывается ошибка и возбуждается исключение `FileNotFoundError`.
    *   **Добавление шрифтов в `FPDF`**:  Добавляет шрифты, описанные в JSON-файле, в PDF документ.
    *   **Установка шрифта**: Устанавливает шрифт по умолчанию для текста.
    *   **Запись текста**: Записывает входные данные `data` в PDF-файл.
    *   **Сохранение PDF**: Сохраняет PDF-файл по пути, указанному в `pdf_file`.
    *   **Обработка исключений**: Если во время генерации PDF возникает ошибка, то в лог записывается сообщение об ошибке, и функция возвращает `False`, иначе `True`.

    *Пример:*
    `PDFUtils.save_pdf_fpdf("Привет мир!", "output.pdf")` создаёт PDF с текстом "Привет мир!".

6.  **`PDFUtils.save_pdf_weasyprint(data, pdf_file)`**:
    *   **Входные данные:**
        *   `data`: HTML-контент (строка) или путь к HTML-файлу (`str | Path`).
        *   `pdf_file`: Путь к PDF-файлу (`str | Path`).
    *   **Определение типа входных данных `data`**:
        *   Если `data` - строка, то HTML-контент напрямую передается в `HTML(string=data).write_pdf()`.
        *   Если `data` - путь, то HTML-файл, расположенный по указанному пути передается в `HTML(filename=str(data)).write_pdf()`.
    *   **Сохранение PDF**: PDF-файл сохраняется по пути, указанному в `pdf_file`.
    *   **Обработка исключений**: Если во время генерации PDF возникает ошибка, то в лог записывается сообщение об ошибке, и функция возвращает `False`, иначе `True`.

    *Пример:*
    `PDFUtils.save_pdf_weasyprint("<h1>Hello</h1>", "output.pdf")` преобразует HTML строку в PDF.
    `PDFUtils.save_pdf_weasyprint("input.html", "output.pdf")` преобразует HTML файл в PDF.

7.  **`PDFUtils.save_pdf_xhtml2pdf(data, pdf_file)`**:
    *   **Входные данные:**
        *   `data`: HTML-контент (строка) или путь к HTML-файлу (`str | Path`).
        *   `pdf_file`: Путь для сохранения PDF-файла (`str | Path`).
    *   **Открытие файла на запись**: Открывает файл, предназначенный для записи PDF в бинарном режиме (`w+b`).
    *   **Определение типа входных данных `data`**:
        *   Если `data` - строка, то она перекодируется в UTF-8 (для обработки возможных ошибок кодировки) и передаётся в `pisa.CreatePDF()`.
        *   Если `data` - путь, то HTML-файл читается в кодировке UTF-8, и его содержимое передаётся в `pisa.CreatePDF()`.
    *   **Сохранение PDF**: PDF-файл сохраняется по пути, указанному в `pdf_file`.
    *   **Обработка исключений**: Если во время генерации PDF возникает ошибка, то в лог записывается сообщение об ошибке, и функция возвращает `False`, иначе `True`.

    *Пример:*
    `PDFUtils.save_pdf_xhtml2pdf("<h1>Hello</h1>", "output.pdf")` преобразует HTML строку в PDF.
    `PDFUtils.save_pdf_xhtml2pdf("input.html", "output.pdf")` преобразует HTML файл в PDF.

8.  **`PDFUtils.html2pdf(html_str, pdf_file)`**:
    *   **Входные данные:**
        * `html_str`: HTML-контент (строка).
        *   `pdf_file`: Путь для сохранения PDF-файла (`str | Path`).
    *   **Сохранение PDF**: Использует `weasyprint` для преобразования `html_str` в PDF-файл, сохраняемый по пути, указанному в `pdf_file`.
     *   **Обработка исключений**: Если во время генерации PDF возникает ошибка, то выводится сообщение об ошибке в консоль, и функция возвращает `None`, иначе `True`.

9.  **`PDFUtils.pdf_to_html(pdf_file, html_file)`**:
    *   **Входные данные:**
        *   `pdf_file`: Путь к исходному PDF-файлу (`str | Path`).
        *   `html_file`: Путь для сохранения HTML-файла (`str | Path`).
    *   **Извлечение текста**: Извлекает весь текст из PDF-файла с помощью `pdfminer.high_level.extract_text()`.
    *   **Создание HTML-файла**: Создает HTML-файл с извлеченным текстом, обернутым в теги `<html><body>...</body></html>`.
    *   **Сохранение HTML**: Сохраняет HTML-файл по пути, указанному в `html_file`.
    *   **Обработка исключений**: Если во время конвертации PDF в HTML возникает ошибка, то в консоль выводится сообщение об ошибке, и функция возвращает `False`, иначе `True`.

    *Пример:*
     `PDFUtils.pdf_to_html("input.pdf", "output.html")` преобразует текст из PDF-файла в HTML-файл.

10. **`PDFUtils.dict2pdf(data, file_path)`**:
     *   **Входные данные:**
        *   `data`: Словарь или объект `SimpleNamespace`, данные которого нужно сохранить в PDF.
        *   `file_path`: Путь для сохранения PDF-файла (`str | Path`).
     *   **Преобразование `SimpleNamespace` в словарь**: Если `data` это `SimpleNamespace`, преобразует его в обычный словарь.
     *   **Создание объекта canvas**: Инициализирует объект `canvas.Canvas` из библиотеки `reportlab` для создания PDF-файла.
     *   **Установка параметров**: Задает размер страницы (A4) и начальную позицию для рисования текста.
     *   **Запись данных**: Проходит по элементам словаря `data`, записывая каждую пару ключ-значение в PDF-файл.
     *   **Перенос на новую страницу**: Если текст выходит за границы страницы, то создается новая страница.
     *   **Сохранение PDF**: Сохраняет PDF-файл по пути, указанному в `file_path`.

    *Пример:*
     `PDFUtils.dict2pdf({"name": "John", "age": 30}, "output.pdf")` создаёт PDF-файл, содержащий строки "name: John" и "age: 30".

## <mermaid>

```mermaid
flowchart TD
    Start[Start] --> FindRoot[<code>set_project_root()</code><br> Find Project Root]
    FindRoot --> SetRootVar[Set <code>__root__</code> Variable]
    SetRootVar --> CheckWkhtmltopdf[Check if <code>wkhtmltopdf.exe</code> exists]
    CheckWkhtmltopdf -- "wkhtmltopdf.exe exists" --> PDFUtilsClass[<code>PDFUtils</code> Class]
    CheckWkhtmltopdf -- "wkhtmltopdf.exe does not exist" --> Error[Raise <code>FileNotFoundError</code>]
    
    PDFUtilsClass --> save_pdf_pdfkit[<code>save_pdf_pdfkit(data, pdf_file)</code>]
    PDFUtilsClass --> save_pdf_fpdf[<code>save_pdf_fpdf(data, pdf_file)</code>]
    PDFUtilsClass --> save_pdf_weasyprint[<code>save_pdf_weasyprint(data, pdf_file)</code>]
    PDFUtilsClass --> save_pdf_xhtml2pdf[<code>save_pdf_xhtml2pdf(data, pdf_file)</code>]
     PDFUtilsClass --> html2pdf[<code>html2pdf(html_str, pdf_file)</code>]
    PDFUtilsClass --> pdf_to_html[<code>pdf_to_html(pdf_file, html_file)</code>]
    PDFUtilsClass --> dict2pdf[<code>dict2pdf(data, file_path)</code>]

    save_pdf_pdfkit --> pdfkit_config[Configure <code>pdfkit</code> with <code>wkhtmltopdf</code> path]
    pdfkit_config --> pdfkit_from_str_or_file[<code>pdfkit.from_string()</code> or <code>pdfkit.from_file()</code>]
     pdfkit_from_str_or_file -- PDF created --> PDFSaved_pdfkit[Return True]
     pdfkit_from_str_or_file-- Error --> PDFSavedError_pdfkit[Return False]


    save_pdf_fpdf --> FPDF_init[Initialize <code>FPDF</code>]
    FPDF_init --> load_fonts[Load fonts from <code>fonts.json</code>]
     load_fonts -- Fonts loaded --> add_fonts[Add fonts to <code>FPDF</code>]
    load_fonts -- Fonts not loaded --> Error_fonts[Raise <code>FileNotFoundError</code>]
    add_fonts --> set_default_font[Set Default Font]
    set_default_font --> add_text[Add Text Data]
    add_text -- PDF created --> PDFSaved_fpdf[Return True]
    add_text -- Error --> PDFSavedError_fpdf[Return False]


    save_pdf_weasyprint --> weasyprint_html[<code>HTML(string=data)</code> or <code>HTML(filename=data)</code>]
    weasyprint_html --> weasyprint_write_pdf[<code>.write_pdf(pdf_file)</code>]
     weasyprint_write_pdf -- PDF created --> PDFSaved_weasyprint[Return True]
    weasyprint_write_pdf -- Error --> PDFSavedError_weasyprint[Return False]
    
    save_pdf_xhtml2pdf --> xhtml2pdf_open_file[Open PDF File for Writing]
    xhtml2pdf_open_file --> xhtml2pdf_create_pdf[<code>pisa.CreatePDF()</code>]
    xhtml2pdf_create_pdf -- PDF created --> PDFSaved_xhtml2pdf[Return True]
    xhtml2pdf_create_pdf -- Error --> PDFSavedError_xhtml2pdf[Return False]
    
    html2pdf --> weasyprint_html_str[<code>HTML(string=html_str)</code>]
    weasyprint_html_str --> weasyprint_html_str_write_pdf[<code>.write_pdf(pdf_file)</code>]
     weasyprint_html_str_write_pdf -- PDF created --> PDFSaved_html2pdf[Return True]
    weasyprint_html_str_write_pdf -- Error --> PDFSavedError_html2pdf[Return None]
    
    pdf_to_html --> extract_pdf_text[<code>extract_text(pdf_file)</code>]
    extract_pdf_text --> create_html_file[Create HTML File]
    create_html_file -- HTML created --> HTMLSaved[Return True]
    create_html_file -- Error --> HTMLSavedError[Return False]
    
    dict2pdf --> transform_dict[Transform <code>SimpleNamespace</code> to dict]
    transform_dict --> canvas_init[Initialize <code>canvas.Canvas()</code>]
    canvas_init --> set_font_size[Set font and size]
    set_font_size --> draw_data[Draw Data]
    draw_data --> save_pdf_dict[Save <code>pdf</code>]
```

## <объяснение>

**Импорты:**

*   `from __future__ import annotations`: Позволяет использовать аннотации типов, например, `str | Path`, для указания типов данных, включая возможность использования составных типов.
*   `import sys`: Предоставляет доступ к переменным и функциям, которые взаимодействуют с интерпретатором Python. Используется для добавления пути к корневому каталогу в `sys.path`.
*   `import os`: Предоставляет функции для взаимодействия с операционной системой. В данном коде не используется напрямую, но может быть задействован через другие импортированные библиотеки.
*   `import json`: Используется для работы с данными в формате JSON, в частности для загрузки настроек шрифтов из файла `fonts.json`.
*   `from pathlib import Path`:  Позволяет работать с путями к файлам и каталогам в объектно-ориентированном стиле.
*   `import pdfkit`: Используется для конвертации HTML-контента в PDF с использованием `wkhtmltopdf`.
*   `from reportlab.pdfgen import canvas`: Используется для создания PDF-файлов и рисования на них.
*   `from fpdf import FPDF`: Используется для создания PDF-файлов с текстом, в том числе с поддержкой различных шрифтов.
*   `from weasyprint import HTML`: Используется для конвертации HTML-контента в PDF.
*   `from xhtml2pdf import pisa`:  Используется для конвертации HTML/CSS в PDF с помощью библиотеки `xhtml2pdf`.
*   `from pdfminer.high_level import extract_text`:  Используется для извлечения текста из PDF-файлов.
*   `from src.logger.logger import logger`:  Импортирует кастомный логгер из модуля `src.logger.logger`, используется для записи сообщений (ошибок, предупреждений, информационных сообщений).
*   `from src.utils.printer import pprint`: Импортирует функцию `pprint` из модуля `src.utils.printer`, для форматированного вывода (в коде не используется, но может быть задействован).

**Классы:**

*   **`PDFUtils`**:
    *   **Роль:** Предоставляет набор статических методов для работы с PDF-файлами, включая создание, сохранение, преобразование из HTML и извлечение текста.
    *   **Атрибуты:** Не имеет атрибутов.
    *   **Методы:**
        *   `save_pdf_pdfkit(data, pdf_file)`: Сохраняет HTML-контент в PDF с использованием библиотеки `pdfkit`.
        *   `save_pdf_fpdf(data, pdf_file)`: Сохраняет текст в PDF с использованием библиотеки `FPDF`.
        *   `save_pdf_weasyprint(data, pdf_file)`: Сохраняет HTML-контент в PDF с использованием библиотеки `WeasyPrint`.
        *   `save_pdf_xhtml2pdf(data, pdf_file)`: Сохраняет HTML-контент в PDF с использованием библиотеки `xhtml2pdf`.
        *    `html2pdf(html_str, pdf_file)`: Преобразует HTML контент в PDF с помощью библиотеки WeasyPrint.
        *   `pdf_to_html(pdf_file, html_file)`: Конвертирует PDF-файл в HTML-файл, извлекая текст из PDF.
        *   `dict2pdf(data, file_path)`: Сохраняет словарь или `SimpleNamespace` данные в PDF-файл.
    *   **Взаимодействие:**
        *   Используется как утилитарный класс, не взаимодействует напрямую с другими классами проекта.
        *   Использует другие библиотеки (например, `pdfkit`, `fpdf`, `weasyprint`, `xhtml2pdf`, `reportlab` и `pdfminer`) для выполнения своей основной работы.
        *   Использует кастомный логгер `src.logger.logger`.

**Функции:**

*   **`set_project_root(marker_files)`**:
    *   **Аргументы:** `marker_files` - кортеж строк, представляющих маркерные файлы или каталоги, указывающие на корень проекта.
    *   **Возвращаемое значение:** `Path` - путь к корневому каталогу проекта.
    *   **Назначение:** Находит корневой каталог проекта, начиная с каталога, где находится текущий файл. Это позволяет динамически определять путь к файлам внутри проекта.
    *   **Пример:** `set_project_root(marker_files=('__root__', '.git'))` - ищет каталоги, содержащие файлы с именем `__root__` или `.git`, начиная с текущего каталога и поднимаясь вверх по иерархии. Если ни один из файлов не найден, то возвращается путь к каталогу, где находится текущий файл.

**Переменные:**

*   `__root__`: `Path` -  путь к корневому каталогу проекта, вычисляется один раз при инициализации модуля с помощью `set_project_root()`.
*   `wkhtmltopdf_exe`: `Path` - путь к исполняемому файлу `wkhtmltopdf.exe`, используется `pdfkit` для генерации PDF из HTML.

**Потенциальные ошибки и области для улучшения:**

*   **Обработка ошибок:**
    *   В методах `PDFUtils.save_pdf_pdfkit` , `PDFUtils.save_pdf_fpdf`, `PDFUtils.save_pdf_weasyprint` , `PDFUtils.save_pdf_xhtml2pdf`, `PDFUtils.html2pdf`, `PDFUtils.pdf_to_html` есть общие блоки `try...except`, но используются разные подходы к обработке исключений:  в каких-то случаях, они просто печатаются в консоль, а в каких-то используется кастомный логгер. Было бы хорошо унифицировать подход и использовать логгер во всех случаях для отслеживания ошибок.
     *    В методах `PDFUtils.save_pdf_pdfkit` , `PDFUtils.save_pdf_xhtml2pdf`, `PDFUtils.save_pdf_fpdf` используется блок `except Exception as ex: ...`, что не позволяет конкретно определять тип возникшей ошибки.  Рекомендуется обрабатывать более специфичные исключения, которые могут возникать в процессе выполнения кода (например, `pdfkit.PDFKitError`, `FileNotFoundError`).
    *   В методе `PDFUtils.save_pdf_fpdf` при ошибке загрузки шрифтов возникает `FileNotFoundError`. Хорошо бы добавить дополнительную обработку  и запись в лог других возможных ошибок (например,  `json.JSONDecodeError`, когда `json.load` не может прочитать файл).
*   **Улучшение читаемости кода:**
    *   В методе  `PDFUtils.save_pdf_fpdf` формирование сообщения об ошибке в случае, если `fonts.json` не найден,  слишком длинное и нечитаемое.  Хорошо бы вынести его в отдельную переменную или константу.
     *    В методе `PDFUtils.save_pdf_xhtml2pdf` код, связанный с обработкой `data` в виде строки или файла можно вынести в отдельные методы.
*   **Проблема с кодировкой**:
    *  Метод `PDFUtils.save_pdf_xhtml2pdf`  пытается исправить кодировку  при помощи `data.encode('utf-8').decode('utf-8')` при работе со строками.  Однако это преобразование может не всегда быть необходимым и может привести к лишним преобразованиям данных. Было бы лучше проверять кодировку и преобразовывать ее только в случае необходимости.
*   **Извлечение текста из PDF**:
    *   Метод `PDFUtils.pdf_to_html`  извлекает текст из PDF файла и просто оборачивает его в HTML теги. Это может не сохранить форматирование исходного PDF-файла.
*   **Динамическое определение путей**:
     * Путь к файлу шрифтов и `wkhtmltopdf_exe` формируются жестко.  Рекомендуется для лучшей переносимости вынести эти параметры в настройки, например, в `.env` файл.
*   **`dict2pdf`**:
     *   В функции `dict2pdf` используется жестко заданный шрифт "Helvetica" и размер 12. Можно добавить возможность задания этих параметров.
     *  У функции `dict2pdf` нет возвращаемого значения, а другие функции возвращают логическое значение.  Хорошо бы унифицировать этот подход.
* **Зависимости**:
   * Код зависит от наличия исполняемого файла `wkhtmltopdf.exe`, что создает дополнительную сложность при развертывании проекта. Можно предложить использовать Docker для решения этой проблемы.
**Взаимосвязи с другими частями проекта:**

*   **`src.logger.logger`:** Используется для логирования сообщений.
*   **`src.utils.printer`:** Импортируется, но не используется напрямую, однако предполагается использование для форматированного вывода (например, в будущих итерациях).
*   Функция `set_project_root` может использоваться в других модулях для определения корневой директории проекта.
```