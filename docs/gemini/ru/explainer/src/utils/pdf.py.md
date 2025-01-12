## АНАЛИЗ КОДА: `src/utils/pdf.py`

### 1. <алгоритм>
#### Блок-схема

```mermaid
graph LR
    A[Start] --> B{set_project_root()};
    B --> C{Найти корень проекта};
    C -- Найдено --> D[Сохранить путь к корню];
    C -- Не найдено --> E[Использовать текущий путь];
    D --> F{Проверка wkhtmltopdf.exe};
    E --> F;
    F -- wkhtmltopdf.exe найден --> G[Определить функции класса PDFUtils];
    F -- wkhtmltopdf.exe не найден --> H[Выбросить FileNotFoundError];
     G --> I{save_pdf_pdfkit()};
     I --> J{Инициализация pdfkit.configuration};
      J --> K{Преобразование HTML в PDF};
     K -- Успешно --> L[Вернуть True];
     K -- Ошибка --> M[Вернуть False];
     G --> N{save_pdf_fpdf()};
    N --> O{Создание PDF документа};
    O --> P{Загрузка шрифтов из JSON};
      P --> Q{Добавление шрифтов};
      Q --> R{Сохранение PDF};
        R -- Успешно --> S[Вернуть True];
     R -- Ошибка --> T[Вернуть False];
      G --> U{save_pdf_weasyprint()};
       U --> V{Преобразование HTML в PDF (WeasyPrint)};
       V -- Успешно --> W[Вернуть True];
       V -- Ошибка --> X[Вернуть False];
    G --> Y{save_pdf_xhtml2pdf()};
    Y --> Z{Преобразование HTML в PDF (xhtml2pdf)};
         Z -- Успешно --> AA[Вернуть True];
        Z -- Ошибка --> AB[Вернуть False];
      G --> AC{html2pdf()};
      AC --> AD{Преобразование HTML в PDF (WeasyPrint)};
          AD -- Успешно --> AE[Вернуть True];
         AD -- Ошибка --> AF[Вернуть None];
      G --> AG{pdf_to_html()};
      AG --> AH{Извлечение текста из PDF};
      AH --> AI{Сохранить HTML};
          AI -- Успешно --> AJ[Вернуть True];
        AI -- Ошибка --> AK[Вернуть False];
    G --> AL{dict2pdf()};
        AL --> AM{Преобразование словаря в PDF};
            AM --> AN[Сохранение PDF];
  H --> End
  L --> End
    M --> End
    S --> End
      T --> End
       W --> End
     X --> End
     AA --> End
     AB --> End
    AE --> End
      AF --> End
     AJ --> End
    AK --> End
    AN --> End

```
#### Пример для каждого логического блока:

1.  **`set_project_root()`**: 
    *   **Пример**:  Если скрипт находится в `/project/src/utils/pdf.py`, а маркерный файл `.git` есть в `/project`, то функция вернет `/project`.
    *   **Поток данных**: Путь к файлу `__file__` -> Поиск родительских директорий -> Возврат найденного пути.
2.  **Проверка `wkhtmltopdf.exe`**:
    *   **Пример**: Проверяется существование файла `/project/bin/wkhtmltopdf/files/bin/wkhtmltopdf.exe`.
    *   **Поток данных**: Путь к исполняемому файлу -> Проверка существования -> Вывод ошибки или продолжение работы.
3.  **`PDFUtils.save_pdf_pdfkit()`**:
    *   **Пример**: `PDFUtils.save_pdf_pdfkit("<h1>Hello</h1>", "/tmp/output.pdf")` создаст PDF из HTML.
    *   **Поток данных**: HTML/путь к HTML файлу, путь к PDF -> Конфигурация `pdfkit` -> Сохранение PDF.
4.  **`PDFUtils.save_pdf_fpdf()`**:
    *   **Пример**: `PDFUtils.save_pdf_fpdf("Hello World!", "/tmp/output.pdf")` создаст PDF с текстом.
    *   **Поток данных**: Текст, путь к PDF -> Создание PDF документа `fpdf`-> Сохранение PDF.
5.  **`PDFUtils.save_pdf_weasyprint()`**:
    *   **Пример**: `PDFUtils.save_pdf_weasyprint("<h1>Hello</h1>", "/tmp/output.pdf")` или `PDFUtils.save_pdf_weasyprint("/tmp/input.html", "/tmp/output.pdf")`.
    *   **Поток данных**: HTML/путь к HTML файлу, путь к PDF -> Создание PDF документа `WeasyPrint`-> Сохранение PDF.
6.  **`PDFUtils.save_pdf_xhtml2pdf()`**:
    *   **Пример**: `PDFUtils.save_pdf_xhtml2pdf("<h1>Hello</h1>", "/tmp/output.pdf")` или `PDFUtils.save_pdf_xhtml2pdf("/tmp/input.html", "/tmp/output.pdf")`.
    *   **Поток данных**: HTML/путь к HTML файлу, путь к PDF -> Создание PDF документа `xhtml2pdf`-> Сохранение PDF.
7.   **`PDFUtils.html2pdf()`**:
    *   **Пример**:  `PDFUtils.html2pdf("<h1>Hello</h1>", "/tmp/output.pdf")`.
    *   **Поток данных**: HTML строка, путь к PDF -> Преобразование с помощью `weasyprint` -> Сохранение PDF.
8. **`PDFUtils.pdf_to_html()`**:
    *   **Пример**:  `PDFUtils.pdf_to_html("/tmp/input.pdf", "/tmp/output.html")`.
    *   **Поток данных**: путь к PDF файлу, путь к HTML файлу -> извлечение текста из PDF -> сохранение HTML.
9. **`PDFUtils.dict2pdf()`**:
    *  **Пример**: `PDFUtils.dict2pdf({"name": "John", "age": 30}, "/tmp/output.pdf")`
    *   **Поток данных**: Словарь данных, путь к PDF -> Сохранение содержимого словаря в PDF.

### 2. <mermaid>

```mermaid
flowchart TD
    A[Start] --> B(set_project_root)
    B --> C{Find Project Root}
    C -- Found --> D[Set Project Root Path]
    C -- Not Found --> E[Use Current Path]
    D --> F{Check wkhtmltopdf.exe}
    E --> F
    F -- Exists --> G[Define PDFUtils Class Methods]
     F -- Not Exists --> H[Raise FileNotFoundError]
    G --> I(save_pdf_pdfkit)
    I --> J{Configure pdfkit}
    J --> K{Convert HTML to PDF}
     K -- Success --> L[Return True]
     K -- Error --> M[Return False]
    G --> N(save_pdf_fpdf)
    N --> O{Create PDF document}
     O --> P{Load fonts from JSON}
    P --> Q{Add Fonts}
     Q --> R{Save PDF}
    R -- Success --> S[Return True]
    R -- Error --> T[Return False]
    G --> U(save_pdf_weasyprint)
    U --> V{Convert HTML to PDF (WeasyPrint)}
    V -- Success --> W[Return True]
    V -- Error --> X[Return False]
    G --> Y(save_pdf_xhtml2pdf)
    Y --> Z{Convert HTML to PDF (xhtml2pdf)}
     Z -- Success --> AA[Return True]
     Z -- Error --> AB[Return False]
     G --> AC(html2pdf)
      AC --> AD{Convert HTML to PDF (WeasyPrint)}
        AD -- Success --> AE[Return True]
         AD -- Error --> AF[Return None]
    G --> AG(pdf_to_html)
     AG --> AH{Extract Text from PDF}
        AH --> AI{Save HTML}
         AI -- Success --> AJ[Return True]
         AI -- Error --> AK[Return False]
    G --> AL(dict2pdf)
     AL --> AM{Convert Dictionary to PDF}
        AM --> AN[Save PDF]

    H --> End
   L --> End
   M --> End
    S --> End
      T --> End
      W --> End
     X --> End
     AA --> End
      AB --> End
     AE --> End
        AF --> End
       AJ --> End
       AK --> End
    AN --> End
```

###  Зависимости `mermaid`:

1.  **`Start`**: Начальная точка выполнения.
2.  **`set_project_root`**: Функция для определения корневой директории проекта.
3.  **`Find Project Root`**: Логический блок, определяющий, был ли найден корень проекта.
4.  **`Set Project Root Path`**: Сохраняет путь к корню проекта, если он был найден.
5.  **`Use Current Path`**: Использует путь к текущему файлу, если корень проекта не был найден.
6.  **`Check wkhtmltopdf.exe`**: Проверяет существование исполняемого файла `wkhtmltopdf.exe`.
7.  **`Define PDFUtils Class Methods`**: Определяет статические методы класса `PDFUtils`.
8.  **`Raise FileNotFoundError`**: Выбрасывает исключение, если `wkhtmltopdf.exe` не найден.
9.  **`save_pdf_pdfkit`**: Метод для сохранения PDF с использованием библиотеки `pdfkit`.
10. **`Configure pdfkit`**: Настройка параметров `pdfkit`, включая путь к исполняемому файлу `wkhtmltopdf.exe`.
11. **`Convert HTML to PDF`**: Логический блок для преобразования HTML в PDF.
12. **`Return True`**: Возвращает `True`, если PDF успешно создан.
13. **`Return False`**: Возвращает `False`, если во время создания PDF произошла ошибка.
14. **`save_pdf_fpdf`**: Метод для сохранения PDF с использованием библиотеки `FPDF`.
15. **`Create PDF document`**: Создает экземпляр PDF документа `FPDF`.
16. **`Load fonts from JSON`**: Загружает информацию о шрифтах из JSON файла.
17. **`Add Fonts`**: Добавляет шрифты в документ `FPDF`.
18. **`Save PDF`**: Сохраняет PDF документ.
19. **`save_pdf_weasyprint`**: Метод для сохранения PDF с использованием библиотеки `WeasyPrint`.
20. **`Convert HTML to PDF (WeasyPrint)`**: Логический блок для преобразования HTML в PDF с помощью `WeasyPrint`.
21. **`save_pdf_xhtml2pdf`**: Метод для сохранения PDF с использованием библиотеки `xhtml2pdf`.
22. **`Convert HTML to PDF (xhtml2pdf)`**: Логический блок для преобразования HTML в PDF с помощью `xhtml2pdf`.
23. **`html2pdf`**: Метод для сохранения PDF с использованием библиотеки `WeasyPrint`.
24. **`Convert HTML to PDF (WeasyPrint)`**: Логический блок для преобразования HTML в PDF с помощью `WeasyPrint`.
25. **`pdf_to_html`**: Метод для конвертации PDF в HTML.
26.  **`Extract Text from PDF`**: Извлекает текст из PDF файла с помощью библиотеки `pdfminer`.
27. **`Save HTML`**: Сохраняет извлеченный текст в HTML файл.
28.  **`dict2pdf`**: Метод для сохранения данных словаря в PDF.
29. **`Convert Dictionary to PDF`**:  Логический блок для преобразования словаря в PDF.
30. **`End`**: Конечная точка выполнения.
31.  **`Save PDF`**: Сохраняет PDF документ.

### 3. <объяснение>
#### Импорты:
*   `sys`: Используется для добавления пути к корневой директории проекта в `sys.path`, чтобы импорты модулей проекта работали корректно.
*   `os`: Используется для работы с файловой системой.
*   `json`: Используется для загрузки настроек шрифтов из JSON-файла.
*   `pathlib.Path`:  Используется для работы с путями к файлам и директориям.
*   `pdfkit`: Библиотека для преобразования HTML в PDF, использующая wkhtmltopdf.
*   `reportlab.pdfgen.canvas`:  Используется для создания PDF-документов, в частности для  `dict2pdf`.
*   `fpdf.FPDF`:  Библиотека для создания PDF-файлов, в частности для `save_pdf_fpdf`.
*   `weasyprint.HTML`:  Библиотека для преобразования HTML в PDF, используется в `save_pdf_weasyprint` и `html2pdf`.
*   `xhtml2pdf.pisa`:  Библиотека для преобразования HTML в PDF.
*   `pdfminer.high_level.extract_text`: Библиотека для извлечения текста из PDF-файлов, используется в `pdf_to_html`.
*   `src.logger.logger`:  Модуль для логирования, используется для записи ошибок и информации.
*   `src.utils.printer`:  Модуль для вывода информации в консоль.

**Взаимосвязи с другими пакетами `src`:**
- `src.logger.logger` используется для логирования событий и ошибок в рамках проекта.
- `src.utils.printer` используется для вывода информации в консоль.

#### Классы:

*   **`PDFUtils`**:
    *   **Роль**: Предоставляет набор статических методов для преобразования HTML в PDF с использованием различных библиотек (`pdfkit`, `FPDF`, `weasyprint`, `xhtml2pdf`), а также для конвертации PDF в HTML и словаря в PDF.
    *   **Атрибуты**: Нет атрибутов экземпляра, используются только статические методы.
    *   **Методы**:
        *   **`save_pdf_pdfkit(data: str | Path, pdf_file: str | Path) -> bool`**: Сохраняет HTML-контент или файл в PDF с использованием `pdfkit`.
        *   **`save_pdf_fpdf(data: str, pdf_file: str | Path) -> bool`**: Сохраняет текст в PDF с использованием `FPDF`, поддерживает добавление шрифтов из JSON файла.
        *   **`save_pdf_weasyprint(data: str | Path, pdf_file: str | Path) -> bool`**: Сохраняет HTML-контент или файл в PDF с использованием `WeasyPrint`.
        *   **`save_pdf_xhtml2pdf(data: str | Path, pdf_file: str | Path) -> bool`**: Сохраняет HTML-контент или файл в PDF с использованием `xhtml2pdf`.
        *   **`html2pdf(html_str: str, pdf_file: str | Path) -> bool | None`**: Сохраняет HTML-контент или файл в PDF с использованием `WeasyPrint`.
        *   **`pdf_to_html(pdf_file: str | Path, html_file: str | Path) -> bool`**: Конвертирует PDF-файл в HTML-файл.
        *   **`dict2pdf(data: dict | SimpleNamespace, file_path: str | Path) -> None`**: Сохраняет данные словаря в PDF-файл.
    *   **Взаимодействие**: Этот класс используется для предоставления унифицированного интерфейса для работы с PDF-файлами и различными методами преобразования.

#### Функции:

*   **`set_project_root(marker_files: tuple = ('__root__', '.git')) -> Path`**:
    *   **Аргументы**: `marker_files` - кортеж с именами файлов или директорий для определения корня проекта.
    *   **Возвращаемое значение**: `Path` - путь к корню проекта или к текущей директории, если корень не найден.
    *   **Назначение**:  Находит корень проекта на основе наличия маркерных файлов или директорий.
    *   **Пример**:  Если маркерный файл `.git` находится в директории `/project`, то `set_project_root()` вернет `Path("/project")`.

#### Переменные:

*   **`__root__`** (`Path`): Глобальная переменная, содержащая путь к корневой директории проекта, полученный вызовом `set_project_root()`.
*   **`wkhtmltopdf_exe`** (`Path`): Глобальная переменная, содержащая путь к исполняемому файлу `wkhtmltopdf.exe`, используется `pdfkit`.

#### Потенциальные ошибки и области для улучшения:

1.  **Обработка ошибок**:
    *   В некоторых функциях (`save_pdf_fpdf`, `save_pdf_xhtml2pdf`) используются блоки `try...except Exception as ex` с общим перехватом ошибок, что может затруднить отладку и идентификацию конкретных проблем. Рекомендуется перехватывать более специфические исключения.
    *   В функциях `save_pdf_pdfkit`, `save_pdf_weasyprint`, `save_pdf_xhtml2pdf`, `html2pdf`, `pdf_to_html` не всегда обеспечивается полная обработка ошибок, таких как, например, ошибки при работе с файлами (отсутствие прав доступа или неверный формат файла).
2.  **Зависимости**:
    *   `wkhtmltopdf.exe` является внешней зависимостью, и его отсутствие вызывает `FileNotFoundError`. Необходимо предусмотреть более удобный механизм для установки и настройки этой зависимости.
    *   В `save_pdf_fpdf` шрифты ищутся в JSON файле, который является внешней зависимостью.
3.  **Кодировка**:
    *   В функции `save_pdf_xhtml2pdf` есть некоторая избыточность кодирования, когда данные сначала кодируются в UTF-8, а затем декодируются обратно.
4.  **Производительность**:
    *   Для больших PDF-файлов извлечение всего текста может быть неэффективным в `pdf_to_html`, возможно, стоит рассмотреть потоковую обработку или другие оптимизации.
5.  **Разделение ответственности**:
    *   Класс `PDFUtils` выполняет множество различных задач по созданию и преобразованию PDF. Возможно, стоит разбить его на несколько классов с более узкой специализацией.

#### Цепочка взаимосвязей с другими частями проекта:

1.  **`src.logger.logger`**: Используется для записи сообщений об ошибках и успехе операций, обеспечивая логирование работы модуля.
2. **`src.utils.printer`**: Используется для вывода сообщений в консоль.
3. **`src.utils.pdf`**: Использует модуль `src.logger.logger` для логирования, таким образом, `src.utils.pdf` зависит от `src.logger.logger`.

Этот анализ предоставляет подробное понимание функциональности кода, его зависимостей и потенциальных проблем, а также предлагает пути для его улучшения.