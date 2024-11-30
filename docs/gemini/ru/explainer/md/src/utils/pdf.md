# <input code>

```python
## \file hypotez/src/utils/pdf.py
# -*- coding: utf-8 -*-\
#! venv/Scripts/python.exe
#! venv/bin/python/python3.12

"""
.. module: src.utils 
	:platform: Windows, Unix
	:synopsis: Модуль для преобразования HTML-контента или файлов в PDF

Модуль для преобразования HTML-контента или файлов в PDF с использованием библиотеки `pdfkit`.
Дополнительная информация:
- https://chatgpt.com/share/672266a3-0048-800d-a97b-c38f647d496b
- https://stackoverflow.com/questions/73599970/how-to-solve-wkhtmltopdf-reported-an-error-exit-with-code-1-due-to-network-err
- https://habr.com/ru/companies/bothub/articles/853490/
"""
MODE = 'dev'
import sys
import os

from pathlib import Path
import pdfkit
from reportlab.pdfgen import canvas
from fpdf import FPDF

from src.logger import logger

def set_project_root(marker_files=('pyproject.toml', 'requirements.txt', '.git')) -> Path:
    """
    Finds the root directory of the project starting from the current file's directory,
    searching upwards and stopping at the first directory containing any of the marker files.

    Args:
        marker_files (tuple): Filenames or directory names to identify the project root.
    
    Returns:
        Path: Path to the root directory if found, otherwise the directory where the script is located.
    """
    __root__:Path
    current_path:Path = Path(__file__).resolve().parent
    __root__ = current_path
    for parent in [current_path] + list(current_path.parents):
        if any((parent / marker).exists() for marker in marker_files):
            __root__ = parent
            break
    if __root__ not in sys.path:
        sys.path.insert(0, str(__root__))
    return __root__


# Get the root directory of the project
__root__ = set_project_root()
"""__root__ (Path): Path to the root directory of the project"""


wkhtmltopdf_exe = __root__ / 'bin' / 'wkhtmltopdf' / 'files' / 'bin' / 'wkhtmltopdf.exe'

if not wkhtmltopdf_exe.exists():
    logger.error("Не найден wkhtmltopdf.exe по указанному пути.")
    raise FileNotFoundError("wkhtmltopdf.exe отсутствует")

configuration = pdfkit.configuration(
    wkhtmltopdf=str(wkhtmltopdf_exe)
)

options = {"enable-local-file-access": ""}


class PDFUtils:
    """
    Класс для работы с PDF-файлами, предоставляющий методы для сохранения HTML-контента в PDF.
    """

    @staticmethod
    def save_pdf(data: str | Path, pdf_file: str | Path) -> bool:
        """
        Сохранить HTML-контент или файл в PDF.

        Args:
            data (str | Path): HTML-контент или путь к HTML-файлу.
            pdf_file (str | Path): Путь к сохраняемому PDF-файлу.

        Returns:
            bool: `True` если PDF успешно сохранен, иначе `False`.

        Raises:
            pdfkit.PDFKitError: Ошибка генерации PDF через `pdfkit`.
            OSError: Ошибка доступа к файлу.
        """
        try:
            if isinstance(data, str):
                # Преобразование HTML-контента в PDF
                pdfkit.from_string(data, pdf_file, configuration=configuration, options=options)
            else:
                # Преобразование HTML-файла в PDF
                pdfkit.from_file(str(data), pdf_file, configuration=configuration, options=options)
            logger.info(f"PDF успешно сохранен: {pdf_file}")
            return True
        except (pdfkit.PDFKitError, OSError) as ex:
            logger.error(f"Ошибка генерации PDF: {ex}", exc_info=True)
            return False
        except Exception as ex:
            logger.error(f"Неожиданная ошибка: {ex}", exc_info=True)
            return False


    @staticmethod
    def save_pdf_v2(data: str, pdf_file: str | Path) -> bool:
        """
        Альтернативный метод сохранения текста в PDF с использованием библиотеки FPDF.

        Args:
            data (str): Текст, который необходимо сохранить в PDF.
            pdf_file (str | Path): Путь к сохраняемому PDF-файлу.

        Returns:
            bool: `True` если PDF успешно сохранен, иначе `False`.
        """
        try:
            pdf = FPDF()
            pdf.add_page()
            pdf.set_auto_page_break(auto=True, margin=15)
            pdf.add_font("DejaVu", "", "путь/к/DejaVuSans.ttf", uni=True)
            pdf.set_font("DejaVu", size=12)
            pdf.multi_cell(0, 10, data)
            pdf.output(str(pdf_file))
            logger.info(f"PDF отчет успешно сохранен: {pdf_file}")
            return True
        except Exception as ex:
            logger.error(f"Ошибка при сохранении PDF через FPDF: {ex}", exc_info=True)
            return False
```

```mermaid
graph TD
    A[__root__ = set_project_root()] --> B{wkhtmltopdf_exe exists?};
    B -- Yes --> C[configuration = pdfkit.configuration()];
    B -- No --> D[logger.error & raise FileNotFoundError];
    C --> E[PDFUtils.save_pdf()];
    E -- data is str --> F[pdfkit.from_string()];
    E -- data is Path --> G[pdfkit.from_file()];
    F --> H[PDF успешно сохранен];
    G --> H;
    E -- Exception --> I[logger.error & return False];
    H --> J[return True];
    I --> J;
    E --> K[PDFUtils.save_pdf_v2()];
    K --> L[pdf = FPDF()];
    L --> M[pdf.add_page()];
    M --> N[pdf.set_auto_page_break()];
    N --> O[pdf.add_font()];
    O --> P[pdf.set_font()];
    P --> Q[pdf.multi_cell()];
    Q --> R[pdf.output()];
    R --> S[PDF отчет успешно сохранен];
    S --> J;
    K -- Exception --> I;

    subgraph "src dependencies"
        style T fill:#ccf
        T[logger] --> E;
        T --> K;
        T --> I;

    end
```

```markdown
# <algorithm>

**Алгоритм работы кода:**

1. **Получение корневой директории проекта (set_project_root):**
   - Начинается с текущей директории файла.
   - Итеративно поднимается вверх по дереву директорий.
   - Проверяет наличие маркеров (pyproject.toml, requirements.txt, .git) в каждой директории.
   - Если маркер найден, то текущая директория принимается за корневую.
   - Добавляет корневую директорию в sys.path, если она там еще не присутствует.
   - Возвращает корневую директорию.

2. **Проверка существования wkhtmltopdf.exe:**
   - Ищет файл wkhtmltopdf.exe в заданной директории.
   - Если файл не найден, выводит ошибку и завершает работу.

3. **Настройка конфигурации pdfkit:**
   - Создается объект конфигурации для pdfkit, указывается путь к wkhtmltopdf.exe.

4. **Сохранение HTML-контента в PDF (save_pdf):**
   - Принимает HTML-контент (строка) или путь к HTML-файлу в качестве аргумента.
   - Если HTML-контент - строка, использует `pdfkit.from_string` для преобразования.
   - Если HTML-контент - путь к файлу, использует `pdfkit.from_file` для преобразования.
   - Сохраняет результат в указанный PDF-файл.
   - Возвращает True, если успешно, иначе False.

5. **Альтернативное сохранение текста в PDF (save_pdf_v2):**
   - Принимает текст и путь к PDF-файлу.
   - Использует библиотеку FPDF для создания PDF-документа.
   - Добавляет текст в документ.
   - Сохраняет PDF-файл.
   - Возвращает True, если успешно, иначе False.


# <explanation>

**Импорты:**

- `sys`: Предоставляет доступ к системным переменным и функциям.
- `os`: Модуль для работы с операционной системой.
- `pathlib`: Модуль для работы с путями к файлам и директориям.
- `pdfkit`: Библиотека для преобразования HTML в PDF.
- `reportlab.pdfgen`: Не используется.
- `fpdf`: Библиотека для работы с PDF.
- `src.logger`:  Логирование, вероятно, реализовано в другом модуле проекта, связанном с `src`.

**Классы:**

- `PDFUtils`: Класс для работы с PDF-файлами.  Содержит статические методы `save_pdf` и `save_pdf_v2`.

**Функции:**

- `set_project_root()`: Находит корневую директорию проекта, начиная с текущего файла, и возвращает путь к ней.  Важно для корректной работы импорта.
- `save_pdf()`:  Преобразует HTML-контент в PDF, используя `pdfkit`.
- `save_pdf_v2()`: Преобразует текст в PDF с использованием `fpdf`.

**Переменные:**

- `__root__`: Путь к корневой директории проекта.
- `wkhtmltopdf_exe`: Путь к исполняемому файлу `wkhtmltopdf`.
- `configuration`: Конфигурация для `pdfkit`.
- `options`: Опции для `pdfkit`, в данном случае для доступа к локальным файлам.

**Возможные ошибки и улучшения:**

- **Путь к шрифту:**  В методе `save_pdf_v2` путь к шрифту `"путь/к/DejaVuSans.ttf"` явно некорректен. Нужно заменить его на корректный путь или использовать другой шрифт, доступный по умолчанию.
- **Обработка ошибок:** Хотя в коде есть обработка исключений, она могла бы быть более детализированной. Например, можно выделить отдельные блоки для ошибок в `pdfkit` и в `fpdf`, что улучшит отладку.
- **Динамический поиск wkhtmltopdf:**  Можно добавить проверку, если `wkhtmltopdf.exe` не найден, то можно попытаться найти его в других стандартных местах установки (например, в папках Program Files, Program Files (x86)).
- **Типы данных:**  Использование `str` вместо `Path` при вызове `pdfkit.from_string` и `pdfkit.from_file` потенциально может привести к ошибкам, особенно на разных операционных системах. Лучше использовать `Path` для всех путей.

**Взаимосвязи с другими частями проекта:**

Метод `logger.info`, `logger.error` и `logger.error(f"Ошибка генерации PDF: {ex}", exc_info=True)` указывают на зависимость от модуля `logger`, который, вероятно, находится в директории `src`. Код, использующий функцию `PDFUtils.save_pdf`,  будет зависимым от этого файла.

```