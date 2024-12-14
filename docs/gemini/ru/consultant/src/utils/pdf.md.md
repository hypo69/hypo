# Анализ кода модуля `pdf`

**Качество кода: 7/10**

-   **Плюсы:**
    -   Модуль предоставляет широкий набор функций для работы с PDF, включая преобразование HTML в PDF и PDF в HTML с использованием различных библиотек.
    -   Есть подробное описание функциональности модуля, ключевых особенностей, структуры, примеров использования и зависимостей.
    -   Используется `pathlib` для работы с путями, что является хорошей практикой.
    -   Присутствует информация о необходимых зависимостях и их установке.
-   **Минусы:**
    -   Отсутствуют docstrings в коде Python, что затрудняет понимание функций и их использования.
    -   Не используется кастомный логгер `src.logger.logger`.
    -   Не используется `j_loads` или `j_loads_ns` для загрузки `fonts.json`.
    -   Не хватает обработки ошибок с помощью `logger.error`.
    -   Не все функции и переменные имеют подробные комментарии в стиле reStructuredText.

**Рекомендации по улучшению**

1.  Добавить docstrings в формате reStructuredText для всех функций и классов.
2.  Использовать `from src.logger.logger import logger` для логирования ошибок.
3.  Использовать `j_loads` или `j_loads_ns` для чтения файла `fonts.json`.
4.  Избегать стандартных `try-except` блоков, предпочитая обработку ошибок через `logger.error`.
5.  Добавить подробные комментарии в стиле RST ко всем функциям, методам и переменным, включая объяснение выполняемых действий.
6.  Привести в соответствие имена функций, переменных и импортов с ранее обработанными файлами.
7.  Убедиться, что все импорты присутствуют и необходимы.

**Оптимизированный код**

```python
"""
Модуль для работы с PDF файлами.
=========================================================================================

Этот модуль содержит статические методы класса :class:`PDFUtils` для работы с PDF файлами,
включая преобразование HTML в PDF и PDF в HTML с использованием различных библиотек.

Пример использования
--------------------

Пример использования класса `PDFUtils`:

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
import platform
from pathlib import Path
from typing import Any

import pdfkit
from fpdf import FPDF
from pdfminer.high_level import extract_text
from weasyprint import HTML
from xhtml2pdf import pisa

from src.logger.logger import logger  # Импорт логгера
from src.utils.jjson import j_loads  # Импорт j_loads для работы с json
from src.utils.printer import print_info, print_error

def set_project_root() -> Path:
    """
    Определяет корневую директорию проекта.

    Функция проверяет наличие маркеров проекта (pyproject.toml, requirements.txt, .git)
    в текущей директории и родительских, возвращая Path корневой директории.

    :return: Path: Корневая директория проекта.
    """
    current_dir = Path(os.getcwd())
    while True:
        if any((current_dir / marker).exists() for marker in ['pyproject.toml', 'requirements.txt', '.git']):
            return current_dir
        if current_dir == current_dir.parent:
            return Path(os.getcwd())
        current_dir = current_dir.parent


ROOT_DIR = set_project_root()
ASSETS_DIR = ROOT_DIR / 'assets'
FONTS_DIR = ASSETS_DIR / 'fonts'
FONTS_JSON = FONTS_DIR / 'fonts.json'

# Конфигурация путей для wkhtmltopdf
wkhtmltopdf_exe = None
if platform.system() == 'Windows':
    wkhtmltopdf_exe = 'C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe'
elif platform.system() == 'Linux':
    wkhtmltopdf_exe = '/usr/bin/wkhtmltopdf'
elif platform.system() == 'Darwin':
     wkhtmltopdf_exe = '/usr/local/bin/wkhtmltopdf' # для MacOS

class PDFUtils:
    """
    Класс статических методов для работы с PDF файлами.
    """
    @staticmethod
    def save_pdf_pdfkit(html_content: str, output_path: str) -> bool:
        """
        Конвертирует HTML контент в PDF файл используя pdfkit.

        :param html_content: HTML контент в виде строки.
        :param output_path: Путь к файлу PDF, в который будет сохранен результат.
        :return: bool: True, если конвертация прошла успешно, False в случае ошибки.
        """
        try:
            #  Конфигурация опций для pdfkit
            config = pdfkit.configuration(wkhtmltopdf=wkhtmltopdf_exe)
            #  Преобразует HTML в PDF
            pdfkit.from_string(html_content, output_path, configuration=config)
            print_info(f'PDF файл успешно сохранен: {output_path}')
            return True
        except Exception as ex:
            # Логирование ошибки
            logger.error(f'Ошибка при конвертации HTML в PDF (pdfkit): {ex}')
            print_error(f'Ошибка при конвертации HTML в PDF (pdfkit): {ex}')
            return False

    @staticmethod
    def save_pdf_fpdf(text: str, output_path: str, font_config_path: Path = FONTS_JSON) -> bool:
        """
        Создает PDF файл из текста с использованием FPDF.

        Поддерживает добавление пользовательских шрифтов через файл fonts.json.

        :param text: Текст, который будет добавлен в PDF файл.
        :param output_path: Путь к файлу PDF, в который будет сохранен результат.
        :param font_config_path: Путь к файлу конфигурации шрифтов (по умолчанию `FONTS_JSON`).
        :return: bool: True, если PDF файл создан успешно, False в случае ошибки.
        """
        try:
            # Загрузка конфигурации шрифтов из JSON
            fonts_config = j_loads(font_config_path)
            #  Инициализация PDF документа
            pdf = FPDF()
            pdf.add_page()
            #  Добавление пользовательских шрифтов
            if fonts_config:
                for font_name, font_info in fonts_config.items():
                    font_path = FONTS_DIR / font_info['file']
                    pdf.add_font(font_name, '', str(font_path), uni=True)
                pdf.set_font('DejaVu', size=12) # Установка шрифта
            else:
                pdf.set_font('Arial', size=12)  # Установка стандартного шрифта
            # Добавление текста
            pdf.multi_cell(0, 10, text)  # Добавление текста в ячейку
            # Сохранение PDF файла
            pdf.output(output_path)
            print_info(f'PDF файл успешно сохранен: {output_path}')
            return True
        except Exception as ex:
            # Логирование ошибки
            logger.error(f'Ошибка при создании PDF из текста (FPDF): {ex}')
            print_error(f'Ошибка при создании PDF из текста (FPDF): {ex}')
            return False

    @staticmethod
    def save_pdf_weasyprint(html_content: str, output_path: str) -> bool:
        """
        Конвертирует HTML контент в PDF файл используя WeasyPrint.

        :param html_content: HTML контент в виде строки.
        :param output_path: Путь к файлу PDF, в который будет сохранен результат.
        :return: bool: True, если конвертация прошла успешно, False в случае ошибки.
        """
        try:
            # Преобразует HTML в PDF
            HTML(string=html_content).write_pdf(output_path)
            print_info(f'PDF файл успешно сохранен: {output_path}')
            return True
        except Exception as ex:
            # Логирование ошибки
            logger.error(f'Ошибка при конвертации HTML в PDF (WeasyPrint): {ex}')
            print_error(f'Ошибка при конвертации HTML в PDF (WeasyPrint): {ex}')
            return False

    @staticmethod
    def save_pdf_xhtml2pdf(html_content: str, output_path: str) -> bool:
        """
        Конвертирует HTML контент в PDF файл используя xhtml2pdf.

        :param html_content: HTML контент в виде строки.
        :param output_path: Путь к файлу PDF, в который будет сохранен результат.
        :return: bool: True, если конвертация прошла успешно, False в случае ошибки.
        """
        try:
             #  Конвертация HTML в PDF
            with open(output_path, 'wb') as f:
                pisa.CreatePDF(html_content, dest=f)
            print_info(f'PDF файл успешно сохранен: {output_path}')
            return True
        except Exception as ex:
            # Логирование ошибки
            logger.error(f'Ошибка при конвертации HTML в PDF (xhtml2pdf): {ex}')
            print_error(f'Ошибка при конвертации HTML в PDF (xhtml2pdf): {ex}')
            return False

    @staticmethod
    def pdf_to_html(pdf_path: str, output_path: str) -> bool:
        """
        Конвертирует PDF файл в HTML файл, извлекая текст из PDF.

        :param pdf_path: Путь к файлу PDF.
        :param output_path: Путь к файлу HTML, в который будет сохранен результат.
        :return: bool: True, если конвертация прошла успешно, False в случае ошибки.
        """
        try:
            #  Извлечение текста из PDF файла
            text = extract_text(pdf_path)
            #  Формирование HTML структуры из текста
            html_content = f'<html><body><pre>{text}</pre></body></html>'
            # Сохранение HTML файла
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(html_content)
            print_info(f'HTML файл успешно сохранен: {output_path}')
            return True
        except Exception as ex:
            # Логирование ошибки
            logger.error(f'Ошибка при конвертации PDF в HTML: {ex}')
            print_error(f'Ошибка при конвертации PDF в HTML: {ex}')
            return False
```