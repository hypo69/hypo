# Анализ кода модуля `pdf.ru.md`

**Качество кода**
9
-  Плюсы
    - Документация модуля подробная и охватывает все основные аспекты.
    - Описаны основные функции и классы, а также их назначение.
    - Приведены примеры использования основных функций модуля.
    - Есть информация о зависимостях и инструкция по их установке.
    - Документация содержит ссылки на внешние ресурсы, что облегчает понимание и использование модуля.
    - Документация хорошо структурирована и легко читается.
-  Минусы
    - Не все функции и методы модуля описаны в формате reStructuredText (RST), что затрудняет автоматическое генерирование документации.
    - Отсутствуют docstring в коде, что усложняет понимание назначения функций.
    - Не используются `j_loads` или `j_loads_ns` для загрузки `fonts.json`, а применяется стандартный `json.load`.
    -  В коде не используется `from src.logger.logger import logger` для логирования ошибок, а также не обрабатываются исключения.
    - Не указано, где находится файл `fonts.json` при использовании `FPDF`.
    - Не хватает описания возможных ошибок и их обработки.
    - Отсутствует описание функции `set_project_root`.
    - Отсутствует файл `pdf.py`.

**Рекомендации по улучшению**

1.  **Добавить docstring в формате reStructuredText (RST) для всех функций и методов:** Это необходимо для автоматического генерирования документации с помощью Sphinx и других инструментов.
2.  **Использовать `j_loads` или `j_loads_ns` для загрузки файла `fonts.json`:** Это обеспечит консистентность работы с файлами в проекте.
3.  **Применить `from src.logger.logger import logger` для логирования ошибок:** Это позволит централизованно обрабатывать и отслеживать ошибки в модуле.
4.  **Обработать возможные исключения с помощью `logger.error`:** Это повысит устойчивость и надежность кода.
5.  **Добавить описание функции `set_project_root`:** Это важно для понимания работы модуля.
6.  **Добавить файл `pdf.py`:** Этот файл должен содержать код, описанный в документации.
7.  **Указать явно путь к файлу `fonts.json`:** Это позволит избежать проблем при работе с модулем.
8.  **Добавить в документацию информацию о возможных ошибках и их обработке:** Это поможет пользователям правильно использовать модуль и избегать ошибок.

**Оптимизированный код**
```python
"""
Модуль для работы с PDF-файлами
=========================================================================================

Этот модуль предоставляет функции для преобразования HTML-контента или файлов в PDF,
а также для конвертации PDF-файлов в HTML.
Модуль использует несколько библиотек для выполнения этих задач,
включая `pdfkit`, `FPDF`, `WeasyPrint`, `xhtml2pdf` и `pdfminer.six`.

Пример использования
--------------------

Пример использования класса `PDFUtils`:

.. code-block:: python

    from src.utils.pdf import PDFUtils

    html_content = "<h1>Пример HTML</h1><p>Это текст.</p>"
    pdf_file = "output.pdf"

    success = PDFUtils.save_pdf_pdfkit(html_content, pdf_file)
    if success:
        print("PDF успешно создан.")
    else:
        print("Ошибка при создании PDF.")
"""

import json
import os
import subprocess
from pathlib import Path
from typing import Optional

import pdfkit
from fpdf import FPDF
from pdfminer.high_level import extract_text_to_fp
from pdfminer.layout import LAParams
from weasyprint import HTML
from xhtml2pdf import pisa

from src.logger.logger import logger
from src.utils.jjson import j_loads, j_loads_ns
from src.utils.printer import print_error, print_info


def set_project_root() -> Path:
    """
    Определяет корневую директорию проекта.

    Функция ищет маркерные файлы, такие как `pyproject.toml`, `requirements.txt` или `.git`,
    чтобы определить корневую директорию проекта. Это позволяет модулю работать независимо от
    текущего расположения файла.

    :return: Абсолютный путь к корневой директории проекта.
    :rtype: pathlib.Path
    """
    current_dir = Path(__file__).resolve().parent
    while True:
        if any(
            (current_dir / marker).exists()
            for marker in ["pyproject.toml", "requirements.txt", ".git"]
        ):
            return current_dir
        if current_dir == current_dir.parent:
            raise FileNotFoundError("Root project not found")
        current_dir = current_dir.parent


class PDFUtils:
    """
    Класс, предоставляющий статические методы для работы с PDF-файлами.
    """
    project_root = set_project_root()
    assets_dir = project_root / "assets"
    fonts_file = assets_dir / "fonts.json"
    wkhtmltopdf_exe = r"C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe"

    @staticmethod
    def save_pdf_pdfkit(html_content: str, pdf_file: str) -> bool:
        """
        Преобразует HTML-контент или файл в PDF с использованием библиотеки `pdfkit`.

        :param html_content: HTML-контент в виде строки или путь к HTML-файлу.
        :type html_content: str
        :param pdf_file: Путь к выходному PDF-файлу.
        :type pdf_file: str
        :return: `True`, если PDF успешно создан, `False` в противном случае.
        :rtype: bool
        """
        try:
            # код исполняет преобразование HTML в PDF с использованием pdfkit
            config = pdfkit.configuration(wkhtmltopdf=PDFUtils.wkhtmltopdf_exe)
            pdfkit.from_string(html_content, pdf_file, configuration=config)
            print_info(f"PDF file created successfully: {pdf_file}")
            return True
        except Exception as e:
            #  код отправляет сообщение об ошибке в лог
            logger.error(f"Error creating PDF file using pdfkit: {e}")
            print_error(f"Error creating PDF file: {pdf_file}")
            return False

    @staticmethod
    def save_pdf_fpdf(text: str, pdf_file: str, font_config: Optional[str] = None) -> bool:
        """
        Создает PDF-файл из текста с использованием библиотеки `FPDF`.
        Поддерживает добавление пользовательских шрифтов через файл `fonts.json`.

        :param text: Текст для добавления в PDF-файл.
        :type text: str
        :param pdf_file: Путь к выходному PDF-файлу.
        :type pdf_file: str
        :param font_config: Путь к файлу конфигурации шрифтов (по умолчанию `assets/fonts.json`).
        :type font_config: str, optional
        :return: `True`, если PDF успешно создан, `False` в противном случае.
        :rtype: bool
        """
        try:
            # код инициализирует объект FPDF
            pdf = FPDF()
            pdf.add_page()

            font_config = font_config or str(PDFUtils.fonts_file)
            # код загружает конфигурацию шрифтов из файла
            if Path(font_config).exists():
               fonts = j_loads(font_config)
            else:
               fonts = {}
               logger.error(f"Font configuration file not found: {font_config}")
               print_error(f"Font configuration file not found: {font_config}")
            #  код добавляет шрифты, если они есть в конфигурации
            for font_name, font_path in fonts.items():
                if not Path(font_path).is_absolute():
                    font_path = str(PDFUtils.assets_dir / font_path)
                pdf.add_font(font_name, "", font_path, uni=True)
                print_info(f"Font added {font_name=}")

            # код устанавливает шрифт и добавляет текст в PDF
            pdf.set_font("Arial", size=12)
            pdf.multi_cell(0, 10, text)
            # код сохраняет PDF файл
            pdf.output(pdf_file)
            print_info(f"PDF file created successfully: {pdf_file}")
            return True
        except Exception as e:
           #  код отправляет сообщение об ошибке в лог
            logger.error(f"Error creating PDF file using FPDF: {e}")
            print_error(f"Error creating PDF file: {pdf_file}")
            return False

    @staticmethod
    def save_pdf_weasyprint(html_content: str, pdf_file: str) -> bool:
        """
        Преобразует HTML-контент или файл в PDF с использованием библиотеки `WeasyPrint`.

        :param html_content: HTML-контент в виде строки или путь к HTML-файлу.
        :type html_content: str
        :param pdf_file: Путь к выходному PDF-файлу.
        :type pdf_file: str
        :return: `True`, если PDF успешно создан, `False` в противном случае.
        :rtype: bool
        """
        try:
            # код исполняет преобразование HTML в PDF с использованием WeasyPrint
            HTML(string=html_content).write_pdf(pdf_file)
            print_info(f"PDF file created successfully: {pdf_file}")
            return True
        except Exception as e:
            #  код отправляет сообщение об ошибке в лог
            logger.error(f"Error creating PDF file using WeasyPrint: {e}")
            print_error(f"Error creating PDF file: {pdf_file}")
            return False

    @staticmethod
    def save_pdf_xhtml2pdf(html_content: str, pdf_file: str) -> bool:
        """
        Преобразует HTML-контент или файл в PDF с использованием библиотеки `xhtml2pdf`.

        :param html_content: HTML-контент в виде строки или путь к HTML-файлу.
        :type html_content: str
        :param pdf_file: Путь к выходному PDF-файлу.
        :type pdf_file: str
        :return: `True`, если PDF успешно создан, `False` в противном случае.
        :rtype: bool
        """
        try:
             # код исполняет преобразование HTML в PDF с использованием xhtml2pdf
            with open(pdf_file, "wb") as f:
                pisa_status = pisa.CreatePDF(html_content, dest=f)
            if pisa_status.err:
                # код обрабатывает ошибки при создании PDF
                logger.error(f"Error creating PDF file using xhtml2pdf: {pisa_status.err}")
                print_error(f"Error creating PDF file: {pdf_file}")
                return False
            print_info(f"PDF file created successfully: {pdf_file}")
            return True
        except Exception as e:
             #  код отправляет сообщение об ошибке в лог
            logger.error(f"Error creating PDF file using xhtml2pdf: {e}")
            print_error(f"Error creating PDF file: {pdf_file}")
            return False

    @staticmethod
    def pdf_to_html(pdf_file: str, html_file: str) -> bool:
        """
        Конвертирует PDF-файл в HTML-файл, извлекая текст с использованием библиотеки `pdfminer.six`.

        :param pdf_file: Путь к входному PDF-файлу.
        :type pdf_file: str
        :param html_file: Путь к выходному HTML-файлу.
        :type html_file: str
        :return: `True`, если HTML успешно создан, `False` в противном случае.
        :rtype: bool
        """
        try:
            # код извлекает текст из PDF и записывает его в HTML-файл
            with open(html_file, "w", encoding="utf-8") as f:
                with open(pdf_file, "rb") as pdf_input:
                    extract_text_to_fp(pdf_input, f, laparams=LAParams())
            print_info(f"HTML file created successfully: {html_file}")
            return True
        except Exception as e:
             #  код отправляет сообщение об ошибке в лог
            logger.error(f"Error converting PDF to HTML: {e}")
            print_error(f"Error converting PDF to HTML: {html_file}")
            return False
```