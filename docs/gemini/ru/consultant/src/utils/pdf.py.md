# Анализ кода модуля src.utils.pdf

**Качество кода**
7
-  Плюсы
    - Код имеет четкую структуру, разбит на функции и класс `PDFUtils`, что облегчает понимание и поддержку.
    - Используется библиотека `logger` для логирования ошибок и информации.
    - Присутствуют docstring для функций и класса, что способствует лучшей читаемости кода.
    - Код использует `Path` для работы с путями, что делает его более кроссплатформенным.
    - Код корректно обрабатывает различные типы входных данных (строки и пути).
-  Минусы
    - Используется `json.load` вместо `j_loads` или `j_loads_ns` из `src.utils.jjson`.
    - В некоторых местах используется избыточный `try-except`, который можно заменить на `logger.error` и `return False`.
    - Присутствуют `...` в коде, которые не должны быть в финальном варианте.
    - В docstring не все описания аргументов и возвращаемых значений следуют стандарту reStructuredText.
    -  Не везде в комментариях используется reStructuredText.
    - Есть `print` вместо `logger.info`.
    - Захардкоженный MODE = 'dev'
    - Не все импорты соответствуют ранее обработанным файлам.

**Рекомендации по улучшению**

1.  Заменить `json.load` на `j_loads` из `src.utils.jjson` для чтения файлов.
2.  Удалить избыточные блоки `try-except` и использовать `logger.error` для обработки ошибок.
3.  Удалить `...` из кода, заменяя на `return` или `pass`.
4.  Переписать docstring в соответствии со стандартом reStructuredText, добавив описание параметров и возвращаемых значений.
5.  Все комментарии переписать в формате reStructuredText.
6.  Использовать `logger.info` вместо `print`.
7.  Удалить захардкоженный `MODE`, сделать его переменной окружения.
8. Добавить отсутствующие импорты: `from src.utils.jjson import j_loads`
9. Исправить docstring `Args` -> `:param`  и `Returns` -> `:return:`

**Оптимизированный код**

```python
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe
#! venv/bin/python/python3.12

"""
Модуль для преобразования HTML-контента или файлов в PDF
=========================================================================================

Этот модуль предоставляет инструменты для преобразования HTML-контента или файлов в PDF
с использованием различных библиотек, таких как pdfkit, FPDF, WeasyPrint и xhtml2pdf.

Дополнительная информация:
- https://chatgpt.com/share/672266a3-0048-800d-a97b-c38f647d496b
- https://stackoverflow.com/questions/73599970/how-to-solve-wkhtmltopdf-reported-an-error-exit-with-code-1-due-to-network-err
- https://habr.com/ru/companies/bothub/articles/853490/
"""
import os
import sys
from pathlib import Path

import pdfkit
from fpdf import FPDF
from pdfminer.high_level import extract_text
from reportlab.pdfgen import canvas
from weasyprint import HTML
from xhtml2pdf import pisa

from src.logger.logger import logger
from src.utils.jjson import j_loads
from src.utils.printer import pprint


MODE = os.getenv('MODE', 'dev')


def set_project_root(marker_files: tuple = ('pyproject.toml', 'requirements.txt', '.git')) -> Path:
    """
    Определяет корневую директорию проекта, начиная с директории текущего файла,
    поиском вверх до первой директории, содержащей любой из маркерных файлов.

    :param marker_files: Список файлов или директорий, которые идентифицируют корень проекта.
    :type marker_files: tuple
    :return: Путь к корневой директории проекта, или директория, где находится скрипт.
    :rtype: Path
    """
    __root__: Path
    current_path: Path = Path(__file__).resolve().parent
    __root__ = current_path
    for parent in [current_path] + list(current_path.parents):
        if any((parent / marker).exists() for marker in marker_files):
            __root__ = parent
            break
    if __root__ not in sys.path:
        sys.path.insert(0, str(__root__))
    return __root__


# Получение корневой директории проекта
__root__ = set_project_root()
"""__root__ (Path): Путь к корневой директории проекта"""

wkhtmltopdf_exe = __root__ / 'bin' / 'wkhtmltopdf' / 'files' / 'bin' / 'wkhtmltopdf.exe'

if not wkhtmltopdf_exe.exists():
    logger.error("Не найден wkhtmltopdf.exe по указанному пути.")
    raise FileNotFoundError("wkhtmltopdf.exe отсутствует")


class PDFUtils:
    """
    Класс для работы с PDF-файлами, предоставляющий методы для сохранения HTML-контента в PDF с использованием различных библиотек.
    """

    @staticmethod
    def save_pdf_pdfkit(data: str | Path, pdf_file: str | Path) -> bool:
        """
        Сохраняет HTML-контент или файл в PDF с использованием библиотеки `pdfkit`.

        :param data: HTML-контент или путь к HTML-файлу.
        :type data: str | Path
        :param pdf_file: Путь к сохраняемому PDF-файлу.
        :type pdf_file: str | Path
        :return: `True`, если PDF успешно сохранен, иначе `False`.
        :rtype: bool
        :raises pdfkit.PDFKitError: Ошибка генерации PDF через `pdfkit`.
        :raises OSError: Ошибка доступа к файлу.
        """
        try:
            configuration = pdfkit.configuration(
                wkhtmltopdf=str(wkhtmltopdf_exe)
            )
            options = {"enable-local-file-access": ""}
            if isinstance(data, str):
                # Преобразование HTML-контента в PDF
                pdfkit.from_string(data, pdf_file, configuration=configuration, options=options)
            else:
                # Преобразование HTML-файла в PDF
                pdfkit.from_file(str(data), pdf_file, configuration=configuration, options=options)
            logger.info(f"PDF успешно сохранен: {pdf_file}")
            return True
        except Exception as ex:
            logger.error("Ошибка генерации PDF: ", ex)
            return False

    @staticmethod
    def save_pdf_fpdf(data: str, pdf_file: str | Path) -> bool:
        """
        Сохраняет текст в PDF с использованием библиотеки FPDF.

        :param data: Текст, который необходимо сохранить в PDF.
        :type data: str
        :param pdf_file: Путь к сохраняемому PDF-файлу.
        :type pdf_file: str | Path
        :return: `True`, если PDF успешно сохранен, иначе `False`.
        :rtype: bool
        """
        try:
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

            # Загрузка шрифтов из JSON файла
            fonts = j_loads(fonts_file_path)

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
            logger.error('Ошибка при сохранении PDF через FPDF: ', ex)
            return False

    @staticmethod
    def save_pdf_weasyprint(data: str | Path, pdf_file: str | Path) -> bool:
        """
        Сохраняет HTML-контент или файл в PDF с использованием библиотеки `WeasyPrint`.

        :param data: HTML-контент или путь к HTML-файлу.
        :type data: str | Path
        :param pdf_file: Путь к сохраняемому PDF-файлу.
        :type pdf_file: str | Path
        :return: `True`, если PDF успешно сохранен, иначе `False`.
        :rtype: bool
        """
        try:
            if isinstance(data, str):
                HTML(string=data).write_pdf(pdf_file)
            else:
                HTML(filename=str(data)).write_pdf(pdf_file)
            logger.info(f"PDF успешно сохранен: {pdf_file}")
            return True
        except Exception as ex:
            logger.error("Ошибка при сохранении PDF через WeasyPrint: ", ex)
            return False

    @staticmethod
    def save_pdf_xhtml2pdf(data: str | Path, pdf_file: str | Path) -> bool:
        """
        Сохраняет HTML-контент или файл в PDF с использованием библиотеки `xhtml2pdf`.

        :param data: HTML-контент или путь к HTML-файлу.
        :type data: str | Path
        :param pdf_file: Путь к сохраняемому PDF-файлу.
        :type pdf_file: str | Path
        :return: `True`, если PDF успешно сохранен, иначе `False`.
        :rtype: bool
        """
        try:
            with open(pdf_file, "w+b") as result_file:
                if isinstance(data, str):
                    # Убедимся, что строка имеет кодировку UTF-8
                    data_utf8 = data.encode('utf-8').decode('utf-8')  # Преобразуем строку обратно в UTF-8, если нужно
                    try:
                        pisa.CreatePDF(data, dest=result_file)
                    except Exception as ex:
                        logger.error("Ошибка компиляции PDF: ", ex)
                        return False
                else:
                    with open(data, "r", encoding="utf-8") as source_file:
                        try:
                            # Прочитаем файл в кодировке UTF-8
                            source_data = source_file.read()
                            pisa.CreatePDF(source_data, dest=result_file, encoding='UTF-8')
                        except Exception as ex:
                            logger.error("Ошибка компиляции PDF: ", ex)
                            return False
            logger.info(f"PDF успешно сохранен: {pdf_file}")
            return True
        except Exception as ex:
            logger.error("Ошибка при сохранении PDF через xhtml2pdf: ", ex)
            return False

    @staticmethod
    def html2pdf(html_str: str, pdf_file: str | Path) -> bool | None:
        """Конвертирует HTML контент в PDF файл используя WeasyPrint."""
        try:
            HTML(string=html_str).write_pdf(pdf_file)
            return True
        except Exception as e:
            logger.error(f"Ошибка во время генерации PDF: {e}")
            return

    @staticmethod
    def pdf_to_html(pdf_file: str | Path, html_file: str | Path) -> bool:
        """
        Конвертирует PDF-файл в HTML-файл.

        :param pdf_file: Путь к исходному PDF-файлу.
        :type pdf_file: str | Path
        :param html_file: Путь к сохраняемому HTML-файлу.
        :type html_file: str | Path
        :return: `True`, если конвертация прошла успешно, иначе `False`.
        :rtype: bool
        """
        try:
            # Извлечение текста из PDF
            text = extract_text(str(pdf_file))

            # Создание HTML-файла
            with open(html_file, 'w', encoding='utf-8') as file:
                file.write(f"<html><body>{text}</body></html>")

            logger.info(f"HTML успешно сохранен: {html_file}")
            return True
        except Exception as ex:
            logger.error(f"Ошибка при конвертации PDF в HTML: {ex}")
            return False