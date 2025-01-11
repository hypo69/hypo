# Анализ кода модуля `pdf.ru.md`

**Качество кода**
9
- Плюсы
    - Хорошая и подробная документация модуля на русском языке, описывающая назначение, возможности, структуру и примеры использования.
    - Четко указаны зависимости и инструкции по установке необходимых библиотек.
    - Присутствуют ссылки на документации используемых библиотек.
    - Логическая структура описания: от общего к частному.
    - Присутсвует описание для каждой функции в классе.

- Минусы
    - Не хватает блока с самим кодом, который должен быть проанализирован и представлен.
    - Отсутствуют docstring в стиле reStructuredText (RST) для функций и методов.
    - Не используется `j_loads` или `j_loads_ns` для загрузки `fonts.json`.
    - Нет обработки ошибок с использованием `logger.error`.
    - Отсутсвует `from src.logger.logger import logger`

**Рекомендации по улучшению**

1.  **Добавить код модуля**: Необходимо добавить исходный код модуля `pdf.py`, чтобы можно было провести его анализ и рефакторинг.
2.  **Использовать RST docstring**: Необходимо добавить reStructuredText (RST) docstring к каждой функции и методу в коде.
3.  **Использовать `j_loads`**: Заменить `json.load` на `j_loads` или `j_loads_ns` для загрузки `fonts.json`.
4.  **Добавить логирование**: Использовать `logger.error` для обработки исключений и логирования ошибок.
5.  **Удалить избыточный try-except**: Избегать избыточного использования `try-except` блоков, предпочитая использование `logger.error`.
6. **Использовать `from src.logger.logger import logger`**: Добавить импорт логгера.
7.  **Соблюдать PEP 8**: Проверить код на соответствие PEP 8, особенно в части именования переменных и функций.
8.  **Унификация импортов**: Убедиться, что импорты соответствуют ранее обработанным файлам и используются абсолютные пути.

**Оптимизированный код**

```python
"""
Модуль для работы с PDF-файлами.
=========================================================================================

Этот модуль предоставляет функции для преобразования HTML-контента или файлов в PDF,
а также для конвертации PDF-файлов в HTML.

Модуль использует несколько библиотек для выполнения этих задач, включая `pdfkit`,
`FPDF`, `WeasyPrint`, `xhtml2pdf` и `pdfminer.six`.

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
from typing import Union

import pdfkit
from fpdf import FPDF
from pdfminer.high_level import extract_text_to_fp
from pdfminer.layout import LAParams
from weasyprint import HTML
from xhtml2pdf import pisa

from src.logger.logger import logger
from src.utils.jjson import j_loads
from src.utils.printer import print_success, print_error


def set_project_root():
    """
    Определяет корневую директорию проекта.

    Функция ищет маркерные файлы (pyproject.toml, requirements.txt, .git)
    для определения корневой директории проекта.
    """
    current_dir = Path(__file__).resolve().parent
    while True:
        if any((current_dir / marker).exists() for marker in ['pyproject.toml', 'requirements.txt', '.git']):
            return current_dir
        if current_dir == current_dir.parent:
            raise FileNotFoundError('Не удалось найти корневую директорию проекта')
        current_dir = current_dir.parent


PROJECT_ROOT = set_project_root()
ASSETS_DIR = PROJECT_ROOT / 'assets'
FONT_DIR = ASSETS_DIR / 'fonts'


class PDFUtils:
    """
    Класс, предоставляющий статические методы для работы с PDF-файлами.
    """
    wkhtmltopdf_exe = None # устанавливаем значение по умолчанию, что бы не вызывать ошибку

    @staticmethod
    def save_pdf_pdfkit(html_content: str, pdf_file: str) -> bool:
        """
        Преобразует HTML-контент в PDF-файл с использованием библиотеки `pdfkit`.

        :param html_content: Строка с HTML-контентом или путь к HTML-файлу.
        :param pdf_file: Путь к результирующему PDF-файлу.
        :return: True в случае успешного создания PDF, False - в случае ошибки.
        """
        try:
            config = pdfkit.configuration(wkhtmltopdf=PDFUtils.wkhtmltopdf_exe)
            pdfkit.from_string(html_content, pdf_file, configuration=config)
            print_success(f'PDF успешно создан: {pdf_file}')
            return True
        except Exception as e:
            logger.error(f'Ошибка при создании PDF из HTML: {e}')
            print_error(f'Ошибка при создании PDF: {e}')
            return False

    @staticmethod
    def save_pdf_fpdf(text: str, pdf_file: str, font_config: str = 'fonts.json') -> bool:
        """
        Создает PDF-файл из текста с использованием библиотеки `FPDF`.

        :param text: Текст для записи в PDF.
        :param pdf_file: Путь к результирующему PDF-файлу.
        :param font_config: Путь к файлу конфигурации шрифтов.
        :return: True в случае успешного создания PDF, False - в случае ошибки.
        """
        try:
            pdf = FPDF()
            pdf.add_page()
            fonts_path = FONT_DIR / font_config
            fonts = j_loads(fonts_path) if os.path.exists(fonts_path) else None # используем j_loads для загрузки json
            if fonts:
                for font_name, font_data in fonts.items():
                    font_file = FONT_DIR / font_data['file']
                    if os.path.exists(font_file):
                        pdf.add_font(font_name, '', font_file, uni=True)
                    else:
                        logger.error(f'Файл шрифта не найден: {font_file}')
                        print_error(f'Файл шрифта не найден: {font_file}')
                pdf.set_font(fonts['default']['name'], size=12)
            else:
                pdf.set_font('Arial', size=12)
            pdf.multi_cell(0, 10, txt=text)
            pdf.output(pdf_file)
            print_success(f'PDF успешно создан: {pdf_file}')
            return True
        except Exception as e:
            logger.error(f'Ошибка при создании PDF из текста: {e}')
            print_error(f'Ошибка при создании PDF: {e}')
            return False

    @staticmethod
    def save_pdf_weasyprint(html_content: str, pdf_file: str) -> bool:
        """
        Преобразует HTML-контент в PDF-файл с использованием библиотеки `WeasyPrint`.

        :param html_content: Строка с HTML-контентом или путь к HTML-файлу.
        :param pdf_file: Путь к результирующему PDF-файлу.
        :return: True в случае успешного создания PDF, False - в случае ошибки.
        """
        try:
            HTML(string=html_content).write_pdf(pdf_file)
            print_success(f'PDF успешно создан: {pdf_file}')
            return True
        except Exception as e:
            logger.error(f'Ошибка при создании PDF с помощью WeasyPrint: {e}')
            print_error(f'Ошибка при создании PDF: {e}')
            return False

    @staticmethod
    def save_pdf_xhtml2pdf(html_content: str, pdf_file: str) -> bool:
        """
        Преобразует HTML-контент в PDF-файл с использованием библиотеки `xhtml2pdf`.

        :param html_content: Строка с HTML-контентом или путь к HTML-файлу.
        :param pdf_file: Путь к результирующему PDF-файлу.
        :return: True в случае успешного создания PDF, False - в случае ошибки.
        """
        try:
            with open(pdf_file, 'wb') as output_pdf:
                pisa_status = pisa.CreatePDF(html_content, dest=output_pdf)
                if pisa_status.err:
                    logger.error(f'Ошибка при создании PDF с помощью xhtml2pdf: {pisa_status.err}')
                    print_error(f'Ошибка при создании PDF: {pisa_status.err}')
                    return False
            print_success(f'PDF успешно создан: {pdf_file}')
            return True
        except Exception as e:
            logger.error(f'Ошибка при создании PDF с помощью xhtml2pdf: {e}')
            print_error(f'Ошибка при создании PDF: {e}')
            return False

    @staticmethod
    def pdf_to_html(pdf_file: str, html_file: str) -> bool:
        """
        Конвертирует PDF-файл в HTML-файл, извлекая текст с использованием библиотеки `pdfminer.six`.

        :param pdf_file: Путь к исходному PDF-файлу.
        :param html_file: Путь к результирующему HTML-файлу.
        :return: True в случае успешной конвертации, False - в случае ошибки.
        """
        try:
            with open(pdf_file, 'rb') as pdf_input, open(html_file, 'w', encoding='utf-8') as html_output:
                extract_text_to_fp(pdf_input, html_output, laparams=LAParams())
            print_success(f'HTML успешно создан: {html_file}')
            return True
        except Exception as e:
            logger.error(f'Ошибка при конвертации PDF в HTML: {e}')
            print_error(f'Ошибка при конвертации PDF в HTML: {e}')
            return False

    @staticmethod
    def set_wkhtmltopdf_path(path: str) -> None:
        """
        Устанавливает путь к исполняемому файлу wkhtmltopdf.

         :param path: Путь к исполняемому файлу wkhtmltopdf.
         """
        PDFUtils.wkhtmltopdf_exe = path
```