# Анализ кода модуля `src.utils.pdf`

**Качество кода**
    9
 -  Плюсы
        - Код хорошо структурирован и разделен на логические блоки.
        - Присутствует подробное описание модуля и его функций.
        - Использованы библиотеки для работы с PDF, что соответствует заявленной цели модуля.
 -  Минусы
    - Недостаточное количество комментариев в коде (docstring)
    - Отсутствуют импорты используемых библиотек в коде.
    - Не используются кастомные `j_loads` и `j_loads_ns` для работы с JSON.
    - Не используется логгер для отслеживания ошибок.
    - Отсутствует обработка ошибок в функциях.
    - Переменная `wkhtmltopdf_exe` не определена в коде

**Рекомендации по улучшению**

1.  **Добавить docstring к модулю**: Добавьте полное описание модуля в формате reStructuredText (RST).
2.  **Добавить импорты**: Включите все необходимые импорты в начале файла.
3.  **Использовать `j_loads` и `j_loads_ns`**: Замените стандартный `json.load` на `j_loads` или `j_loads_ns` из `src.utils.jjson`.
4.  **Добавить логирование**: Используйте `logger.error` для обработки ошибок вместо `try-except`.
5.  **Добавить docstring к функциям**:  Добавьте описания ко всем функциям в формате RST.
6.  **Обработка ошибок**: Добавьте обработку ошибок с помощью `logger.error` и возвращайте `False` в случае ошибки.
7. **Определение `wkhtmltopdf_exe`**: Добавьте определение переменной `wkhtmltopdf_exe` или вынесите ее в настройки.
8. **Добавить комментарии**: Добавьте комментарии к коду с описанием выполняемых действий.

**Оптимизированный код**

```python
"""
Модуль для работы с PDF файлами.
=========================================================================================

Этот модуль предоставляет функции для конвертации HTML в PDF и наоборот,
а также для создания PDF из текста. Используются библиотеки pdfkit, FPDF,
WeasyPrint, xhtml2pdf и pdfminer.six.

Пример использования
--------------------

Пример конвертации HTML в PDF:

.. code-block:: python

    from src.utils.pdf import PDFUtils

    html_content = "<h1>Example HTML</h1><p>This is text.</p>"
    pdf_file = "output.pdf"

    success = PDFUtils.save_pdf_pdfkit(html_content, pdf_file)
    if success:
        print("PDF successfully created.")
    else:
        print("Error creating PDF.")
"""
import json
import os
import subprocess
from pathlib import Path
from typing import Any, List, Optional

import pdfkit
from fpdf import FPDF
from pdfminer.high_level import extract_text
from weasyprint import HTML
from xhtml2pdf import pisa

from src.logger.logger import logger
from src.utils.jjson import j_loads
from src.utils.printer import print_info, print_warning


def set_project_root() -> Path:
    """
    Определяет корень проекта на основе наличия маркерных файлов.

    :return: Путь к корневой директории проекта.
    """
    current_dir = Path(__file__).resolve().parent
    while current_dir != current_dir.parent:
        if any(
            (current_dir / marker).exists()
            for marker in ["pyproject.toml", "requirements.txt", ".git"]
        ):
            return current_dir
        current_dir = current_dir.parent
    return current_dir


PROJECT_ROOT = set_project_root()
ASSETS_DIR = PROJECT_ROOT / "assets"
FONTS_DIR = ASSETS_DIR / "fonts"
WKHTMLTOPDF_EXE = "/usr/local/bin/wkhtmltopdf" # TODO: Вынести в настройки

class PDFUtils:
    """
     Класс `PDFUtils` содержит статические методы для работы с PDF файлами.
    """

    @staticmethod
    def save_pdf_pdfkit(html_content: str, pdf_file: str) -> bool:
        """
        Конвертирует HTML контент в PDF файл, используя библиотеку pdfkit.

        :param html_content: HTML контент для конвертации.
        :param pdf_file: Путь к выходному PDF файлу.
        :return: True в случае успешной конвертации, False в случае ошибки.
        """
        try:
             # Код исполняет конфигурацию для pdfkit
            config = pdfkit.configuration(wkhtmltopdf=WKHTMLTOPDF_EXE)
            # Код исполняет конвертацию html в pdf файл
            pdfkit.from_string(
                html_content, pdf_file, configuration=config
            )  # type: ignore
            return True
        except Exception as ex:
             # Код логирует ошибку, если не удалось сконвертировать файл
            logger.error(f"Ошибка при конвертации HTML в PDF (pdfkit): {ex}")
            return False

    @staticmethod
    def save_pdf_fpdf(text: str, pdf_file: str) -> bool:
        """
        Создает PDF файл из текста, используя библиотеку FPDF.

        :param text: Текст для добавления в PDF.
        :param pdf_file: Путь к выходному PDF файлу.
        :return: True в случае успешного создания, False в случае ошибки.
        """
        try:
            # Код инициализирует объект FPDF
            pdf = FPDF()
            # Код добавляет страницу в pdf
            pdf.add_page()
            # Код устанавливает шрифт
            font_path = FONTS_DIR / "FreeSans.ttf"
            if os.path.exists(font_path):
                pdf.add_font("FreeSans", "", font_path, uni=True)
                pdf.set_font("FreeSans", size=12)
            else:
                 # Код устанавливает стандартный шрифт, если не найден кастомный
                pdf.set_font("Arial", size=12)
                logger.warning(
                    f"Шрифт по пути {font_path} не найден, будет использован стандартный шрифт"
                )

            # Код добавляет текст в pdf
            pdf.multi_cell(0, 10, text)
            # Код сохраняет pdf файл
            pdf.output(pdf_file)
            return True
        except Exception as ex:
             # Код логирует ошибку, если не удалось создать pdf файл
            logger.error(f"Ошибка при создании PDF из текста (fpdf): {ex}")
            return False

    @staticmethod
    def save_pdf_weasyprint(html_content: str, pdf_file: str) -> bool:
        """
        Конвертирует HTML контент в PDF файл, используя библиотеку WeasyPrint.

        :param html_content: HTML контент для конвертации.
        :param pdf_file: Путь к выходному PDF файлу.
        :return: True в случае успешной конвертации, False в случае ошибки.
        """
        try:
            # Код исполняет конвертацию html в pdf файл
            HTML(string=html_content).write_pdf(pdf_file)
            return True
        except Exception as ex:
            # Код логирует ошибку, если не удалось сконвертировать файл
            logger.error(f"Ошибка при конвертации HTML в PDF (weasyprint): {ex}")
            return False

    @staticmethod
    def save_pdf_xhtml2pdf(html_content: str, pdf_file: str) -> bool:
        """
        Конвертирует HTML контент в PDF файл, используя библиотеку xhtml2pdf.

        :param html_content: HTML контент для конвертации.
        :param pdf_file: Путь к выходному PDF файлу.
        :return: True в случае успешной конвертации, False в случае ошибки.
        """
        try:
            # Код открывает файл для записи pdf
            with open(pdf_file, "wb") as f:
                # Код исполняет конвертацию html в pdf
                pisa.CreatePDF(html_content, dest=f)
            return True
        except Exception as ex:
            # Код логирует ошибку, если не удалось сконвертировать файл
            logger.error(f"Ошибка при конвертации HTML в PDF (xhtml2pdf): {ex}")
            return False

    @staticmethod
    def pdf_to_html(pdf_file: str, html_file: str) -> bool:
        """
        Конвертирует PDF файл в HTML файл, извлекая текст из PDF.

        :param pdf_file: Путь к входному PDF файлу.
        :param html_file: Путь к выходному HTML файлу.
        :return: True в случае успешной конвертации, False в случае ошибки.
        """
        try:
             # Код извлекает текст из pdf файла
            text = extract_text(pdf_file)
            # Код формирует html из текста
            html_content = f"<html><body><pre>{text}</pre></body></html>"
            # Код открывает файл для записи html
            with open(html_file, "w", encoding="utf-8") as f:
                # Код записывает html в файл
                f.write(html_content)
            return True
        except Exception as ex:
             # Код логирует ошибку, если не удалось сконвертировать файл
            logger.error(f"Ошибка при конвертации PDF в HTML: {ex}")
            return False