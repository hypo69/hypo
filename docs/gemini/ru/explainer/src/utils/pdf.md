```MD
# <input code>

```python
## \file hypotez/src/utils/pdf.py
# -*- coding: utf-8 -*-\
#! venv/Scripts/python.exe
#! venv/bin/python/python3.12

"""
.. module: src.utils.pdf 
    :platform: Windows, Unix
    :synopsis: Модуль для преобразования HTML-контента или файлов в PDF

Модуль для преобразования HTML-контента или файлов в PDF с использованием различных библиотек.
Дополнительная информация:
- https://chatgpt.com/share/672266a3-0048-800d-a97b-c38f647d496b
- https://stackoverflow.com/questions/73599970/how-to-solve-wkhtmltopdf-reported-an-error-exit-with-code-1-due-to-network-err
- https://habr.com/ru/companies/bothub/articles/853490/
"""
MODE = 'dev'
import sys
import os
import json

from pathlib import Path
import pdfkit
from reportlab.pdfgen import canvas
from fpdf import FPDF
from weasyprint import HTML
from xhtml2pdf import pisa
from src.logger import logger
from src.utils.printer import pprint

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


class PDFUtils:
    """
    Класс для работы с PDF-файлами, предоставляющий методы для сохранения HTML-контента в PDF с использованием различных библиотек.
    """
    # ... (rest of the code)
```

# <algorithm>

**Алгоритм работы модуля `pdf.py`**

1. **`set_project_root`**:
   - Находит корневую директорию проекта, начиная с текущего файла.
   - Проверяет наличие указанных файлов (`pyproject.toml`, `requirements.txt`, `.git`) в родительских директориях.
   - Если корневой каталог найден, добавляет его в `sys.path`.
   - Возвращает корневой каталог.

   *Пример:* Если текущий файл находится в `hypotez/src/utils/pdf.py`, функция будет искать корень проекта, поднимаясь вверх по дереву директорий, пока не найдет директорию, содержащую `pyproject.toml`.

2. **Инициализация `wkhtmltopdf_exe`:**
   - Определяет путь к исполняемому файлу `wkhtmltopdf.exe`.
   - Проверяет существование файла. Если файла нет, выводит ошибку и завершает выполнение.

3. **Класс `PDFUtils`**:
   - `save_pdf_pdfkit`, `save_pdf_fpdf`, `save_pdf_weasyprint`, `save_pdf_xhtml2pdf`:  Реализуют методы для сохранения HTML-контента в PDF с использованием различных библиотек.

   *Пример:* `save_pdf_pdfkit` принимает HTML-строку или путь к HTML-файлу и путь к PDF-файлу в качестве аргументов.  Функция использует `pdfkit` для преобразования данных в PDF и сохраняет его по указанному пути.

4. **`html2pdf`:**  
    - Функция принимает HTML-строку и путь к файлу PDF.
    - Использует библиотеку `WeasyPrint` для преобразования HTML в PDF и сохранения его.

   *Пример:*  Функция вызывается с HTML-контентом и путем сохранения.

**Передача данных:**

- Функции и методы класса `PDFUtils` принимают данные (HTML-контент или путь к файлу) и путь к выходному PDF-файлу.
- Результатом выполнения функций/методов является булево значение, обозначающее успешность сохранения PDF.

# <mermaid>

```mermaid
graph LR
    A[set_project_root] --> B(Найти корень проекта);
    B --> C{Корень проекта найден?};
    C -- Да --> D[Добавить в sys.path];
    C -- Нет --> E[Вернуть текущий путь];
    D --> F[Инициализация wkhtmltopdf_exe];
    F --> G[wkhtmltopdf.exe существует?];
    G -- Да --> H[PDFUtils];
    G -- Нет --> I[Ошибка];
    H --> J[save_pdf_pdfkit];
    H --> K[save_pdf_fpdf];
    H --> L[save_pdf_weasyprint];
    H --> M[save_pdf_xhtml2pdf];
    J --> N[Преобразование HTML в PDF (pdfkit)];
    K --> O[Преобразование HTML в PDF (fpdf)];
    L --> P[Преобразование HTML в PDF (weasyprint)];
    M --> Q[Преобразование HTML в PDF (xhtml2pdf)];
    N --> R[Сохранение PDF];
    O --> R;
    P --> R;
    Q --> R;
    R --> S[Возврат True];
    I --> T[Возврат False/Исключение];
    
```

# <explanation>

**Импорты:**

- `sys`, `os`, `json`, `pathlib`: Стандартные библиотеки Python для работы с системой, файлами, JSON и путями.
- `pdfkit`: Библиотека для преобразования HTML в PDF с использованием wkhtmltopdf.
- `reportlab.pdfgen`: Библиотека для создания PDF.
- `fpdf`: Библиотека для создания PDF.
- `weasyprint`: Библиотека для преобразования HTML в PDF.
- `xhtml2pdf`: Библиотека для преобразования HTML в PDF.
- `src.logger`: Модуль для логирования, вероятно, собственной реализации.
- `src.utils.printer`: Модуль для вывода данных.

**Классы:**

- `PDFUtils`: Класс для работы с PDF-файлами. Он содержит статические методы для сохранения HTML-контента в PDF с использованием разных библиотек (`pdfkit`, `fpdf`, `weasyprint`, `xhtml2pdf`).  Это хороший пример организации кода, так как разные методы не зависят друг от друга, и могут использовать разные библиотеки для достижения одного результата.

**Функции:**

- `set_project_root(marker_files)`: Находит корневую директорию проекта. Это важная функция для работы, которая позволяет избежать абсолютных путей и делает код более переносимым.
- `save_pdf_pdfkit(data, pdf_file)`: Сохраняет HTML-контент или файл в PDF с использованием `pdfkit`. Обработка исключений в этом методе могла бы быть улучшена.
- `save_pdf_fpdf(data, pdf_file)`: Сохраняет текст в PDF с использованием `FPDF`. Важно, что в коде есть реализация загрузки и применения шрифтов для обеспечения возможности поддержки разных языков и символов.
- `save_pdf_weasyprint(data, pdf_file)`: Сохраняет HTML-контент или файл в PDF с использованием `WeasyPrint`.
- `save_pdf_xhtml2pdf(data, pdf_file)`: Сохраняет HTML-контент или файл в PDF с использованием `xhtml2pdf`. Обрабатывает разные типы входных данных (строка или путь к файлу). Улучшает кодировку входных данных.

**Переменные:**

- `__root__`: Путь к корневой директории проекта.
- `wkhtmltopdf_exe`: Путь к исполняемому файлу `wkhtmltopdf`.

**Возможные ошибки и улучшения:**

- **Обработка исключений**:  В методах `save_pdf_pdfkit`, `save_pdf_fpdf`, `save_pdf_weasyprint`, `save_pdf_xhtml2pdf` следует улучшить обработку исключений (`pdfkit.PDFKitError`, `OSError`, `FileNotFoundError` и т.д.).  Должны быть детализированы типы исключений.
- **Работа с кодировкой**: `save_pdf_xhtml2pdf` теперь корректно обрабатывает кодировку UTF-8, что устраняет потенциальную ошибку, когда входной HTML-файл имеет кодировку, отличную от UTF-8.
- **Загрузка шрифтов (FPDF)**: Функция `save_pdf_fpdf`  умело загружает шрифты из `fonts.json`, но стоит учесть возможность обработки ситуаций, когда этот файл не существует, что могло бы быть предсказуемым и исключить возможность сбоя.
- **Проверка путей**:  Добавление проверки существования указанных директорий и файлов в `set_project_root` и других методах значительно улучшит надёжность кода.

**Взаимосвязь с другими частями проекта:**

Код взаимодействует с `src.logger` для вывода сообщений об ошибках и успешном выполнении.  Также с `src.utils.printer`, но по коду не ясно, как.  Необходимые зависимости (wkhtmltopdf) должны быть установлены в виртуальном окружении.