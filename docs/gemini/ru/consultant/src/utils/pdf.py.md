## Улучшенный код
```python
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe
#! venv/bin/python/python3.12
"""
Модуль для преобразования HTML-контента или файлов в PDF
=======================================================

:platform: Windows, Unix
:synopsis: Модуль для преобразования HTML-контента или файлов в PDF.

Модуль для преобразования HTML-контента или файлов в PDF с использованием различных библиотек.

Дополнительная информация:
- https://chatgpt.com/share/672266a3-0048-800d-a97b-c38f647d496b
- https://stackoverflow.com/questions/73599970/how-to-solve-wkhtmltopdf-reported-an-error-exit-with-code-1-due-to-network-err
- https://habr.com/ru/companies/bothub/articles/853490/
"""
MODE = 'dev'
import sys
import os
# import json #  Удален неиспользуемый импорт
from pathlib import Path
import pdfkit
# from reportlab.pdfgen import canvas # Удален неиспользуемый импорт
from fpdf import FPDF
from weasyprint import HTML
from xhtml2pdf import pisa
from src.logger.logger import logger
# from src.utils.printer import pprint # Удален неиспользуемый импорт
from src.utils.jjson import j_loads # Импортируем j_loads для работы с json


def set_project_root(marker_files: tuple = ('pyproject.toml', 'requirements.txt', '.git')) -> Path:
    """
    Определяет корневой каталог проекта.

    Начиная с каталога текущего файла, поиск идет вверх по дереву каталогов,
    останавливаясь на первом каталоге, содержащем любой из файлов-маркеров.

    :param marker_files: Кортеж имен файлов или каталогов, используемых для определения корня проекта.
    :type marker_files: tuple
    :return: Путь к корневому каталогу, если найден, иначе путь к каталогу, где расположен скрипт.
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


# Получение корневого каталога проекта
__root__ = set_project_root()
"""Path: Путь к корневому каталогу проекта."""

wkhtmltopdf_exe = __root__ / 'bin' / 'wkhtmltopdf' / 'files' / 'bin' / 'wkhtmltopdf.exe'

if not wkhtmltopdf_exe.exists():
    logger.error("Не найден wkhtmltopdf.exe по указанному пути.")
    raise FileNotFoundError("wkhtmltopdf.exe отсутствует")


class PDFUtils:
    """
    Класс для работы с PDF-файлами.

    Предоставляет методы для сохранения HTML-контента в PDF с использованием различных библиотек.
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
                # Код преобразовывает HTML-контент в PDF
                pdfkit.from_string(data, pdf_file, configuration=configuration, options=options)
            else:
                # Код преобразовывает HTML-файл в PDF
                pdfkit.from_file(str(data), pdf_file, configuration=configuration, options=options)
            logger.info(f"PDF успешно сохранен: {pdf_file}")
            return True
        except Exception as ex:
            logger.error("Неожиданная ошибка при генерации PDF через pdfkit: ", ex)
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
                    '}\'
                )
                raise FileNotFoundError(f'Файл шрифтов не найден: {fonts_file_path}')

            with open(fonts_file_path, 'r', encoding='utf-8') as json_file:
                # Код загружает данные шрифтов из JSON файла
                fonts = j_loads(json_file)

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
                    # Код обеспечивает кодировку строки в UTF-8
                    data_utf8 = data.encode('utf-8').decode('utf-8')
                    try:
                        pisa.CreatePDF(data_utf8, dest=result_file)
                    except Exception as ex:
                        logger.error("Ошибка компиляции PDF: ", ex)
                        return False
                else:
                    with open(data, "r", encoding="utf-8") as source_file:
                        try:
                            # Код читает файл в кодировке UTF-8
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
        """
        Преобразует HTML-контент в PDF-файл с использованием WeasyPrint.

        :param html_str: HTML-контент для преобразования.
        :type html_str: str
        :param pdf_file: Путь к сохраняемому PDF-файлу.
        :type pdf_file: str | Path
        :return: `True` при успешном преобразовании, `None` при ошибке.
        :rtype: bool | None
        """
        try:
            HTML(string=html_str).write_pdf(pdf_file)
            return True
        except Exception as e:
            logger.error(f"Ошибка при генерации PDF: {e}")
            return
```
## Внесённые изменения
-  Добавлены docstring к модулю, классам и методам в формате reStructuredText (RST).
-  Удалены неиспользуемые импорты `json`, `reportlab.pdfgen`, `src.utils.printer`.
-  Импортирован `j_loads` из `src.utils.jjson` для обработки JSON файлов.
-  Заменено `json.load` на `j_loads` при загрузке данных из файла `fonts.json`.
-  Убраны лишние `...` в блоках `except`.
-  Изменены комментарии внутри функций, добавлена конкретика.
-  Заменено использование `print` на `logger.error` в `html2pdf`.
-  Добавлены явные типы для параметров и возвращаемых значений в docstring.
-  Улучшено форматирование и читаемость кода.
## Оптимизированный код
```python
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe
#! venv/bin/python/python3.12
"""
Модуль для преобразования HTML-контента или файлов в PDF
=======================================================

:platform: Windows, Unix
:synopsis: Модуль для преобразования HTML-контента или файлов в PDF.

Модуль для преобразования HTML-контента или файлов в PDF с использованием различных библиотек.

Дополнительная информация:
- https://chatgpt.com/share/672266a3-0048-800d-a97b-c38f647d496b
- https://stackoverflow.com/questions/73599970/how-to-solve-wkhtmltopdf-reported-an-error-exit-with-code-1-due-to-network-err
- https://habr.com/ru/companies/bothub/articles/853490/
"""
MODE = 'dev'
import sys
import os
# import json #  Удален неиспользуемый импорт
from pathlib import Path
import pdfkit
# from reportlab.pdfgen import canvas # Удален неиспользуемый импорт
from fpdf import FPDF
from weasyprint import HTML
from xhtml2pdf import pisa
from src.logger.logger import logger
# from src.utils.printer import pprint # Удален неиспользуемый импорт
from src.utils.jjson import j_loads # Импортируем j_loads для работы с json


def set_project_root(marker_files: tuple = ('pyproject.toml', 'requirements.txt', '.git')) -> Path:
    """
    Определяет корневой каталог проекта.

    Начиная с каталога текущего файла, поиск идет вверх по дереву каталогов,
    останавливаясь на первом каталоге, содержащем любой из файлов-маркеров.

    :param marker_files: Кортеж имен файлов или каталогов, используемых для определения корня проекта.
    :type marker_files: tuple
    :return: Путь к корневому каталогу, если найден, иначе путь к каталогу, где расположен скрипт.
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


# Получение корневого каталога проекта
__root__ = set_project_root()
"""Path: Путь к корневому каталогу проекта."""

wkhtmltopdf_exe = __root__ / 'bin' / 'wkhtmltopdf' / 'files' / 'bin' / 'wkhtmltopdf.exe'

if not wkhtmltopdf_exe.exists():
    logger.error("Не найден wkhtmltopdf.exe по указанному пути.")
    raise FileNotFoundError("wkhtmltopdf.exe отсутствует")


class PDFUtils:
    """
    Класс для работы с PDF-файлами.

    Предоставляет методы для сохранения HTML-контента в PDF с использованием различных библиотек.
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
                # Код преобразовывает HTML-контент в PDF
                pdfkit.from_string(data, pdf_file, configuration=configuration, options=options)
            else:
                # Код преобразовывает HTML-файл в PDF
                pdfkit.from_file(str(data), pdf_file, configuration=configuration, options=options)
            logger.info(f"PDF успешно сохранен: {pdf_file}")
            return True
        except Exception as ex:
            logger.error("Неожиданная ошибка при генерации PDF через pdfkit: ", ex)
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
                    '}\'
                )
                raise FileNotFoundError(f'Файл шрифтов не найден: {fonts_file_path}')

            with open(fonts_file_path, 'r', encoding='utf-8') as json_file:
                # Код загружает данные шрифтов из JSON файла
                fonts = j_loads(json_file)

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
                    # Код обеспечивает кодировку строки в UTF-8
                    data_utf8 = data.encode('utf-8').decode('utf-8')
                    try:
                        pisa.CreatePDF(data_utf8, dest=result_file)
                    except Exception as ex:
                        logger.error("Ошибка компиляции PDF: ", ex)
                        return False
                else:
                    with open(data, "r", encoding="utf-8") as source_file:
                        try:
                            # Код читает файл в кодировке UTF-8
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
        """
        Преобразует HTML-контент в PDF-файл с использованием WeasyPrint.

        :param html_str: HTML-контент для преобразования.
        :type html_str: str
        :param pdf_file: Путь к сохраняемому PDF-файлу.
        :type pdf_file: str | Path
        :return: `True` при успешном преобразовании, `None` при ошибке.
        :rtype: bool | None
        """
        try:
            HTML(string=html_str).write_pdf(pdf_file)
            return True
        except Exception as e:
            logger.error(f"Ошибка при генерации PDF: {e}")
            return