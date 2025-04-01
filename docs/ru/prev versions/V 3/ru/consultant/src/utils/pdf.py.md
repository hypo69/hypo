## Анализ кода модуля `pdf`

**Качество кода:**

- **Соответствие стандартам**: 6/10
- **Плюсы**:
  - Модуль предоставляет функциональность для преобразования HTML в PDF с использованием различных библиотек.
  - Присутствует обработка исключений.
  - Используется логирование через модуль `src.logger.logger`.
- **Минусы**:
  - Не все функции и классы документированы в соответствии с рекомендациями.
  - В коде встречаются устаревшие конструкции и неоднородный стиль.
  - Используется прямой вызов `print` вместо логирования через `logger`.
  - Не везде соблюдается PEP8.

**Рекомендации по улучшению:**

1.  **Документирование кода**:
    - Добавить документацию в формате, указанном в инструкции, для всех классов, методов и функций.
    - Описать назначение каждого аргумента и возвращаемого значения.
    - Добавить примеры использования.

2.  **Улучшение обработки исключений**:
    - Во всех блоках `except` добавить логирование ошибок с использованием `logger.error`, включая трассировку стека (`exc_info=True`).
    - Убрать `...` в блоках `except` и добавить конкретную обработку или логирование.

3.  **Использование `j_loads`**:
    - Заменить использование `open` и `json.load` на `j_loads` для чтения `fonts.json`.

4.  **Приведение к стандартам PEP8**:
    - Проверить и исправить код на соответствие PEP8, включая пробелы вокруг операторов, именование переменных и т.д.

5.  **Удаление неиспользуемых импортов**:
    - Удалить неиспользуемые импорты, такие как `import sys`.

6.  **Логирование вместо `print`**:
    - Заменить все вызовы `print` на `logger.info` или `logger.error` в зависимости от ситуации.

7.  **Улучшение читаемости**:
    - Использовать более конкретные имена для переменных, чтобы улучшить читаемость кода.
    - Добавить больше комментариев для объяснения сложных участков кода.

**Оптимизированный код:**

```python
## \file /src/utils/pdf.py
# -*- coding: utf-8 -*-
#! .pyenv/bin/python3

"""
Модуль для преобразования HTML-контента или файлов в PDF
=========================================================

Модуль предоставляет класс :class:`PDFUtils`, который используется для преобразования HTML-контента или файлов в PDF с использованием различных библиотек.

Пример использования
----------------------

>>> pdf_utils = PDFUtils()
>>> html_content = "<html><body><h1>Hello, world!</h1></body></html>"
>>> pdf_file = "example.pdf"
>>> result = pdf_utils.save_pdf_weasyprint(html_content, pdf_file)
>>> print(result)
True
"""

import os
from pathlib import Path
from typing import Any, Optional

import pdfkit
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4

from src.logger.logger import logger  # Import logger from src.logger
from src.utils.jjson import j_loads

from header import __root__


class PDFUtils:
    """
    Класс для работы с PDF-файлами, предоставляющий методы для сохранения HTML-контента в PDF с использованием различных библиотек.
    """

    @staticmethod
    def save_pdf_pdfkit(data: str | Path, pdf_file: str | Path) -> bool:
        """
        Сохранить HTML-контент или файл в PDF с использованием библиотеки `pdfkit`.

        Args:
            data (str | Path): HTML-контент или путь к HTML-файлу.
            pdf_file (str | Path): Путь к сохраняемому PDF-файлу.

        Returns:
            bool: `True`, если PDF успешно сохранен, иначе `False`.

        Raises:
            FileNotFoundError: Если не найден исполняемый файл wkhtmltopdf.
            pdfkit.PDFKitError: Ошибка генерации PDF через `pdfkit`.
            OSError: Ошибка доступа к файлу.
        """
        wkhtmltopdf_exe = __root__ / 'bin' / 'wkhtmltopdf' / 'files' / 'bin' / 'wkhtmltopdf.exe'

        if not wkhtmltopdf_exe.exists():
            logger.error("Не найден wkhtmltopdf.exe по указанному пути.")
            raise FileNotFoundError("wkhtmltopdf.exe отсутствует")

        try:
            configuration = pdfkit.configuration(wkhtmltopdf=str(wkhtmltopdf_exe))
            options = {'enable-local-file-access': ''}

            if isinstance(data, str):
                pdfkit.from_string(data, pdf_file, configuration=configuration, options=options)  # Преобразование HTML-контента в PDF
            else:
                pdfkit.from_file(str(data), pdf_file, configuration=configuration, options=options)  # Преобразование HTML-файла в PDF

            logger.info(f'PDF успешно сохранен: {pdf_file}')
            return True

        except pdfkit.PDFKitError as ex:  # Обработка ошибок, специфичных для pdfkit
            logger.error(f'Ошибка генерации PDF: {ex}', exc_info=True)  # Логирование ошибки с трассировкой
            return False
        except OSError as ex:  # Обработка ошибок, связанных с файловой системой
            logger.error(f'Ошибка доступа к файлу: {ex}', exc_info=True)  # Логирование ошибки с трассировкой
            return False
        except Exception as ex:  # Обработка всех остальных исключений
            logger.error(f'Неожиданная ошибка: {ex}', exc_info=True)  # Логирование ошибки с трассировкой
            return False

    @staticmethod
    def save_pdf_fpdf(data: str, pdf_file: str | Path) -> bool:
        """
        Сохранить текст в PDF с использованием библиотеки FPDF.

        Args:
            data (str): Текст, который необходимо сохранить в PDF.
            pdf_file (str | Path): Путь к сохраняемому PDF-файлу.

        Returns:
            bool: `True`, если PDF успешно сохранен, иначе `False`.

        Raises:
            FileNotFoundError: Если не найден файл шрифтов.
            Exception: Общая ошибка при работе с FPDF.
        """
        try:
            from fpdf import FPDF

            pdf = FPDF()
            pdf.add_page()
            pdf.set_auto_page_break(auto=True, margin=15)

            # Путь к файлу fonts.json
            fonts_file_path = __root__ / 'assets' / 'fonts' / 'fonts.json'
            if not fonts_file_path.exists():
                logger.error(
                    f'JSON файл установки шрифтов не найден: {fonts_file_path}\n'
                    'Формат файла `fonts.json`:\n'
                    '{\n'
                    '    "dejavu-sans.book": {\n'
                    '        "family": "DejaVuSans",\n'
                    '        "path": "dejavu-sans.book.ttf",\n'
                    '        "style": "book",\n'
                    '        "uni": true\n'
                    '    }\n'
                    '}'
                )
                raise FileNotFoundError(f'Файл шрифтов не найден: {fonts_file_path}')

            fonts = j_loads(fonts_file_path)  # Use j_loads instead of open and json.load

            # Добавление шрифтов
            for font_name, font_info in fonts.items():
                font_path = __root__ / 'assets' / 'fonts' / font_info['path']
                if not font_path.exists():
                    logger.error(f'Файл шрифта не найден: {font_path}')
                    raise FileNotFoundError(f'Файл шрифта не найден: {font_path}')

                pdf.add_font(font_info['family'], font_info['style'], str(font_path), uni=font_info['uni'])

            # Установка шрифта по умолчанию
            pdf.set_font('DejaVuSans', style='book', size=12)
            pdf.multi_cell(0, 10, data)
            pdf.output(str(pdf_file))
            logger.info(f'PDF отчет успешно сохранен: {pdf_file}')
            return True

        except Exception as ex:
            logger.error(f'Ошибка при сохранении PDF через FPDF: {ex}', exc_info=True)  # Логирование с трассировкой
            return False

    @staticmethod
    def save_pdf_weasyprint(data: str | Path, pdf_file: str | Path) -> bool:
        """
        Сохранить HTML-контент или файл в PDF с использованием библиотеки `WeasyPrint`.

        Args:
            data (str | Path): HTML-контент или путь к HTML-файлу.
            pdf_file (str | Path): Путь к сохраняемому PDF-файлу.

        Returns:
            bool: `True`, если PDF успешно сохранен, иначе `False`.

        Raises:
            Exception: Общая ошибка при работе с WeasyPrint.
        """
        try:
            from weasyprint import HTML

            if isinstance(data, str):
                HTML(string=data).write_pdf(pdf_file)
            else:
                HTML(filename=str(data)).write_pdf(pdf_file)

            logger.info(f'PDF успешно сохранен: {pdf_file}')
            return True

        except Exception as ex:
            logger.error(f'Ошибка при сохранении PDF через WeasyPrint: {ex}', exc_info=True)  # Логирование с трассировкой
            return False

    @staticmethod
    def save_pdf_xhtml2pdf(data: str | Path, pdf_file: str | Path) -> bool:
        """
        Сохранить HTML-контент или файл в PDF с использованием библиотеки `xhtml2pdf`.

        Args:
            data (str | Path): HTML-контент или путь к HTML-файлу.
            pdf_file (str | Path): Путь к сохраняемому PDF-файлу.

        Returns:
            bool: `True`, если PDF успешно сохранен, иначе `False`.

        Raises:
            Exception: Общая ошибка при работе с xhtml2pdf.
        """
        try:
            from xhtml2pdf import pisa

            with open(pdf_file, 'w+b') as result_file:
                if isinstance(data, str):
                    data_utf8 = data.encode('utf-8').decode('utf-8')  # Убедимся, что строка имеет кодировку UTF-8
                    try:
                        pisa.CreatePDF(data_utf8, dest=result_file)
                    except Exception as ex:
                        logger.error(f'Ошибка компиляции PDF: {ex}', exc_info=True)  # Логирование с трассировкой
                        return False
                else:
                    with open(data, 'r', encoding='utf-8') as source_file:
                        try:
                            source_data = source_file.read()  # Прочитаем файл в кодировке UTF-8
                            pisa.CreatePDF(source_data, dest=result_file, encoding='UTF-8')
                        except Exception as ex:
                            logger.error(f'Ошибка компиляции PDF: {ex}', exc_info=True)  # Логирование с трассировкой
                            return False

            logger.info(f'PDF успешно сохранен: {pdf_file}')
            return True

        except Exception as ex:
            logger.error(f'Ошибка при сохранении PDF через xhtml2pdf: {ex}', exc_info=True)  # Логирование с трассировкой
            return False

    @staticmethod
    def html2pdf(html_str: str, pdf_file: str | Path) -> bool | None:
        """Converts HTML content to a PDF file using WeasyPrint."""
        try:
            from weasyprint import HTML

            HTML(string=html_str).write_pdf(pdf_file)
            logger.info(f'PDF успешно сгенерирован: {pdf_file}')  # Use logger instead of print
            return True
        except Exception as e:
            logger.error(f'Ошибка во время генерации PDF: {e}', exc_info=True)  # Use logger instead of print
            return None

    @staticmethod
    def pdf_to_html(pdf_file: str | Path, html_file: str | Path) -> bool:
        """
        Конвертирует PDF-файл в HTML-файл.

        Args:
            pdf_file (str | Path): Путь к исходному PDF-файлу.
            html_file (str | Path): Путь к сохраняемому HTML-файлу.

        Returns:
            bool: `True`, если конвертация прошла успешно, иначе `False`.

        Raises:
            Exception: Общая ошибка при конвертации PDF в HTML.
        """
        try:
            from pdfminer.high_level import extract_text

            text = extract_text(str(pdf_file))

            with open(html_file, 'w', encoding='utf-8') as file:
                file.write(f'<html><body>{text}</body></html>')

            logger.info(f'HTML успешно сохранен: {html_file}')  # Use logger instead of print
            return True
        except Exception as ex:
            logger.error(f'Ошибка при конвертации PDF в HTML: {ex}', exc_info=True)  # Use logger instead of print
            return False

    @staticmethod
    def dict2pdf(data: Any, file_path: str | Path) -> None:
        """
        Сохраняет данные словаря в PDF-файл.

        Args:
            data (dict): Словарь для конвертации в PDF.
            file_path (str | Path): Путь к выходному PDF-файлу.

        Raises:
            TypeError: Если `data` не является словарем.
        """
        if isinstance(data, str):
            logger.error(f'Ожидался словарь, получена строка: {data}')
            raise TypeError(f'Ожидался словарь, получена строка: {data}')

        if not isinstance(data, dict):
            data = data.__dict__

        pdf = canvas.Canvas(str(file_path), pagesize=A4)
        width, height = A4
        x, y = 50, height - 50

        pdf.setFont('Helvetica', 12)

        for key, value in data.items():
            line = f'{key}: {value}'
            pdf.drawString(x, y, line)
            y -= 20

            if y < 50:  # Создать новую страницу, если места недостаточно
                pdf.showPage()
                pdf.setFont('Helvetica', 12)
                y = height - 50

        pdf.save()
        logger.info(f'Словарь успешно преобразован в PDF: {file_path}')