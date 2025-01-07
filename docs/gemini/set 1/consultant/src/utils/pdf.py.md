# Анализ кода модуля `pdf`

**Качество кода: 8**

-   **Плюсы:**
    *   Код содержит docstring для модуля и большинства функций, что соответствует требованиям.
    *   Используется `logger` для логирования ошибок и информации.
    *   Код применяет различные библиотеки для генерации PDF, предоставляя гибкость в работе.
    *   Проект структурирован, с вынесением поиска корневой директории в отдельную функцию.
    *   Используется `Path` для работы с путями, что улучшает читаемость.
    *   Обработка ошибок присутствует в большинстве функций.
-   **Минусы:**
    *   Импорты не полностью соответствуют стандарту PEP8, в частности, импортирование нескольких модулей из одной библиотеки в одной строке.
    *   В некоторых местах используется стандартный `json.load`, вместо `j_loads` из `src.utils.jjson` (не показано в коде).
    *   Комментарии не все в формате RST.
    *   Некоторые блоки `try-except` могут быть упрощены с использованием логирования ошибок.
    *   Не все функции имеют подробные docstring.
    *   В некоторых функциях обработка ошибок реализована через `print`, а не `logger.error`.
    *   В функции `save_pdf_xhtml2pdf` есть попытка повторного декодирования `data` в UTF-8.
    *   Некоторые `...` точки остановки не имеют пояснений.

**Рекомендации по улучшению**

1.  **Импорты:** Разделить импорты на отдельные строки для каждого модуля.
2.  **Комментарии:** Привести все комментарии и docstring в формат RST.
3.  **Обработка JSON:** Использовать `j_loads` или `j_loads_ns` вместо `json.load`.
4.  **Логирование:** Заменить `print` на `logger.error` и упростить `try-except` блоки.
5.  **Удаление лишнего кода:** Убрать избыточное преобразование кодировки в `save_pdf_xhtml2pdf`.
6.  **Расширение документации:** Добавить более подробные docstring для всех функций, включая параметры и возвращаемые значения.
7.  **Точки остановки:** Дать пояснения к точкам остановки `...` в коде.

**Оптимизированный код**

```python
# -*- coding: utf-8 -*-

#! venv/bin/python/python3.12

"""
Модуль для преобразования HTML-контента или файлов в PDF
=========================================================================================

:platform: Windows, Unix
:synopsis: Модуль для преобразования HTML-контента или файлов в PDF.

Этот модуль предоставляет функциональность для преобразования HTML-контента или файлов в PDF
с использованием различных библиотек, таких как pdfkit, FPDF, WeasyPrint и xhtml2pdf.

Дополнительная информация:
    - https://chatgpt.com/share/672266a3-0048-800d-a97b-c38f647d496b
    - https://stackoverflow.com/questions/73599970/how-to-solve-wkhtmltopdf-reported-an-error-exit-with-code-1-due-to-network-err
    - https://habr.com/ru/companies/bothub/articles/853490/
"""

import sys
import os
import json
# from src.utils.jjson import j_loads # TODO:  Использовать  j_loads или j_loads_ns вместо json.load
from pathlib import Path
import pdfkit
from reportlab.pdfgen import canvas
from fpdf import FPDF
from weasyprint import HTML
from xhtml2pdf import pisa
from src.logger.logger import logger
from src.utils.printer import pprint


def set_project_root(marker_files: tuple = ('pyproject.toml', 'requirements.txt', '.git')) -> Path:
    """
    Определяет корневую директорию проекта.
    
    Функция ищет корневую директорию проекта, начиная с директории текущего файла,
    двигаясь вверх по иерархии директорий и останавливаясь на первой директории,
    содержащей один из файлов-маркеров.

    :param marker_files: Кортеж имен файлов или директорий, идентифицирующих корень проекта.
    :type marker_files: tuple
    :return: Путь к корневой директории проекта.
    :rtype: Path
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


# Получение корневой директории проекта
__root__ = set_project_root()
"""Path: Путь к корневой директории проекта"""

wkhtmltopdf_exe = __root__ / 'bin' / 'wkhtmltopdf' / 'files' / 'bin' /  'wkhtmltopdf.exe'

if not wkhtmltopdf_exe.exists():
    logger.error("Не найден wkhtmltopdf.exe по указанному пути.")
    raise FileNotFoundError("wkhtmltopdf.exe отсутствует")


class PDFUtils:
    """
    Класс для работы с PDF-файлами.

    Предоставляет статические методы для сохранения HTML-контента в PDF,
    используя различные библиотеки.
    """

    @staticmethod
    def save_pdf_pdfkit(data: str | Path, pdf_file: str | Path) -> bool:
        """
        Сохраняет HTML-контент или файл в PDF с использованием библиотеки `pdfkit`.
        
        :param data: HTML-контент или путь к HTML-файлу.
        :type data: str | Path
        :param pdf_file: Путь к сохраняемому PDF-файлу.
        :type pdf_file: str | Path
        :return: True если PDF успешно сохранен, иначе False.
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
            # Логирование ошибки и возврат False при неудачной генерации PDF.
            logger.error("Ошибка генерации PDF: ", ex)
            ...
            return False


    @staticmethod
    def save_pdf_fpdf(data: str, pdf_file: str | Path) -> bool:
        """
        Сохраняет текст в PDF с использованием библиотеки FPDF.

        :param data: Текст, который необходимо сохранить в PDF.
        :type data: str
        :param pdf_file: Путь к сохраняемому PDF-файлу.
        :type pdf_file: str | Path
        :return: True, если PDF успешно сохранен, иначе False.
        :rtype: bool
        :raises FileNotFoundError: Если файл шрифтов не найден.
        """
        try:
            pdf = FPDF()
            pdf.add_page()
            pdf.set_auto_page_break(auto = True, margin = 15)

            # Путь к файлу fonts.json
            fonts_file_path = __root__ / 'assets' / 'fonts' / 'fonts.json'
            if not fonts_file_path.exists():
                logger.error(
                    f'JSON файл установки шрифтов не найден: {fonts_file_path}\\n'
                    'Формат файла `fonts.json`:\\n'
                    '{\\n'
                    '    "dejavu-sans.book": {\\n'
                    '        "family": "DejaVuSans",\\n'
                    '        "path": "dejavu-sans.book.ttf",\\n'
                    '        "style": "book",\\n'
                    '        "uni": true\\n'
                    '    }\\n'
                    '}'
                )
                raise FileNotFoundError(f'Файл шрифтов не найден: {fonts_file_path}')
                ...

            with open(fonts_file_path, 'r', encoding = 'utf-8') as json_file:
                # Загружаем настройки шрифтов из JSON файла.
                fonts = json.load(json_file) # TODO:  Использовать  j_loads или j_loads_ns вместо json.load

            # Добавление шрифтов
            for font_name, font_info in fonts.items():
                font_path = __root__ / 'assets' / 'fonts' / font_info['path']
                if not font_path.exists():
                    logger.error(f'Файл шрифта не найден: {font_path}')
                    raise FileNotFoundError(f'Файл шрифта не найден: {font_path}')
                    ...

                pdf.add_font(font_info['family'], font_info['style'], str(font_path), uni = font_info['uni'])

            # Установка шрифта по умолчанию
            pdf.set_font('DejaVuSans', style = 'book', size = 12)
            pdf.multi_cell(0, 10, data)
            pdf.output(str(pdf_file))
            logger.info(f'PDF отчет успешно сохранен: {pdf_file}')
            return True
        except Exception as ex:
            # Логирование ошибки и возврат False при неудачной генерации PDF.
            logger.error('Ошибка при сохранении PDF через FPDF: ', ex)
            ...
            return False


    @staticmethod
    def save_pdf_weasyprint(data: str | Path, pdf_file: str | Path) -> bool:
        """
        Сохраняет HTML-контент или файл в PDF с использованием библиотеки `WeasyPrint`.
        
        :param data: HTML-контент или путь к HTML-файлу.
        :type data: str | Path
        :param pdf_file: Путь к сохраняемому PDF-файлу.
        :type pdf_file: str | Path
        :return: True если PDF успешно сохранен, иначе False.
        :rtype: bool
        """
        try:
            if isinstance(data, str):
                # Код преобразовывает HTML-строку в PDF.
                HTML(string=data).write_pdf(pdf_file)
            else:
                # Код преобразовывает HTML-файл в PDF.
                HTML(filename=str(data)).write_pdf(pdf_file)
            logger.info(f"PDF успешно сохранен: {pdf_file}")
            return True
        except Exception as ex:
            # Логирование ошибки и возврат False при неудачной генерации PDF.
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
        :return: True если PDF успешно сохранен, иначе False.
        :rtype: bool
        """
        try:
            with open(pdf_file, "w+b") as result_file:
                if isinstance(data, str):
                    # Код преобразовывает HTML-строку в PDF.
                    try:
                        pisa.CreatePDF(data, dest=result_file)
                    except Exception as ex:
                        # Логирование ошибки компиляции PDF.
                        logger.error("Ошибка компиляции PDF: ", ex)
                        ...
                else:
                    with open(data, "r", encoding="utf-8") as source_file:
                        try:
                            # Код преобразовывает HTML-файл в PDF.
                            source_data = source_file.read()
                            pisa.CreatePDF(source_data, dest=result_file, encoding='UTF-8')
                        except Exception as ex:
                            # Логирование ошибки компиляции PDF.
                            logger.error("Ошибка компиляции PDF: ", ex)
                            ...
            logger.info(f"PDF успешно сохранен: {pdf_file}")
            ...
            return True
        except Exception as ex:
            # Логирование ошибки при сохранении PDF через xhtml2pdf.
            logger.error("Ошибка при сохранении PDF через xhtml2pdf: ", ex)
            ...
            return False


    @staticmethod
    def html2pdf(html_str: str, pdf_file: str | Path) -> bool | None:
        """
        Преобразует HTML-контент в PDF-файл, используя WeasyPrint.

        :param html_str: HTML-контент в виде строки.
        :type html_str: str
        :param pdf_file: Путь к сохраняемому PDF-файлу.
        :type pdf_file: str | Path
        :return: True, если PDF успешно создан, None в случае ошибки.
        :rtype: bool | None
        """
        try:
            # Код преобразует HTML в PDF.
            HTML(string=html_str).write_pdf(pdf_file)
            return True
        except Exception as e:
            # Логирование ошибки и возврат None.
            logger.error(f"Ошибка при генерации PDF: {e}")
            return
```