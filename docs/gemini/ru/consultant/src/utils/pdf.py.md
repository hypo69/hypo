# Анализ кода модуля `pdf.py`

**Качество кода**
7
-  Плюсы
    - Код содержит docstring для модуля, классов и методов.
    - Используется `logger` для логирования ошибок.
    - Код предоставляет несколько способов для преобразования HTML в PDF с использованием различных библиотек.
    - Наличие обработки основных исключений в блоках `try-except`.
-  Минусы
    - Используется стандартный `json.load` вместо `j_loads` или `j_loads_ns` из `src.utils.jjson`.
    -  Избыточное использование `try-except` блоков, которое можно заменить на обработку ошибок через `logger.error`.
    -  Не все функции имеют docstring.
    -  Некоторые сообщения об ошибках не информативны.
    -  Не все импорты используются.
    - Некоторые комментарии не соответствуют RST стилю
    - Есть `print` для ошибок, которые не должны попадать в продакшен
    - В коде есть `...` как точки остановки, которые нужно убрать.

**Рекомендации по улучшению**

1.  **Импорты:**
    -   Удалить неиспользуемые импорты.
2.  **Использование `j_loads`:**
    -   Заменить `json.load` на `j_loads` или `j_loads_ns` из `src.utils.jjson`.
3.  **Логирование ошибок:**
    -   Улучшить обработку ошибок, используя `logger.error` вместо `print` и избыточного `try-except`.
4.  **Комментарии:**
    -   Привести все комментарии в соответствие с форматом RST, включая docstring.
5.  **Docstring:**
    -   Добавить docstring для всех функций и методов.
6.  **Удалить точки остановки:**
     - Удалить `...` из кода.
7.  **Информативность ошибок:**
    - Улучшить сообщения об ошибках, сделав их более информативными.

**Оптимизированный код**

```python
"""
Модуль для преобразования HTML-контента или файлов в PDF
=========================================================================================

Этот модуль содержит класс :class:`PDFUtils`, который используется для преобразования HTML-контента или файлов в PDF
с использованием различных библиотек, таких как pdfkit, FPDF, WeasyPrint и xhtml2pdf.

.. note::
    Для работы модуля требуется установленная библиотека `wkhtmltopdf`.
    Путь к исполняемому файлу `wkhtmltopdf.exe` определяется автоматически.

Пример использования
--------------------

Пример использования класса `PDFUtils`:

.. code-block:: python

    from src.utils.pdf import PDFUtils
    from pathlib import Path

    html_content = "<h1>Hello, World!</h1>"
    pdf_path = Path("output.pdf")
    success = PDFUtils.save_pdf_pdfkit(html_content, pdf_path)
    if success:
        print(f"PDF файл успешно создан: {pdf_path}")
    else:
        print("Не удалось создать PDF файл")
"""

import sys
import os
from pathlib import Path
import pdfkit
from fpdf import FPDF
from weasyprint import HTML
from xhtml2pdf import pisa
from pdfminer.high_level import extract_text
from src.logger.logger import logger
from src.utils.jjson import j_loads
# from src.utils.printer import pprint # не используется


MODE = 'dev'

def set_project_root(marker_files: tuple = ('pyproject.toml', 'requirements.txt', '.git')) -> Path:
    """
    Определяет корневую директорию проекта на основе наличия файлов-маркеров.

    :param marker_files: Список файлов или директорий, которые используются для определения корня проекта.
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
"""__root__ (Path): Path to the root directory of the project"""

wkhtmltopdf_exe = __root__ / 'bin' / 'wkhtmltopdf' / 'files' / 'bin' /  'wkhtmltopdf.exe'

if not wkhtmltopdf_exe.exists():
    logger.error(f"Не найден wkhtmltopdf.exe по указанному пути: {wkhtmltopdf_exe}")
    raise FileNotFoundError(f"wkhtmltopdf.exe отсутствует по пути: {wkhtmltopdf_exe}")


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

        :raises pdfkit.PDFKitError: Если возникает ошибка при генерации PDF.
        :raises OSError: Если возникает ошибка доступа к файлу.
        """
        try:
            configuration = pdfkit.configuration(wkhtmltopdf=str(wkhtmltopdf_exe))
            options = {"enable-local-file-access": ""}

            if isinstance(data, str):
                #  Преобразование HTML-контента в PDF
                pdfkit.from_string(data, pdf_file, configuration=configuration, options=options)
            else:
                #  Преобразование HTML-файла в PDF
                pdfkit.from_file(str(data), pdf_file, configuration=configuration, options=options)
            logger.info(f"PDF успешно сохранен: {pdf_file}")
            return True
        except pdfkit.PDFKitError as ex:
             # Логирование ошибки генерации PDF через pdfkit
            logger.error(f"Ошибка генерации PDF через pdfkit: {ex}")
            return False
        except OSError as ex:
            # Логирование ошибки доступа к файлу
            logger.error(f"Ошибка доступа к файлу: {ex}")
            return False
        except Exception as ex:
            # Логирование неожиданной ошибки
            logger.error(f"Неожиданная ошибка при генерации PDF: {ex}")
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
            pdf.set_auto_page_break(auto = True, margin = 15)

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
                

            with open(fonts_file_path, 'r', encoding = 'utf-8') as json_file:
                #  Загрузка шрифтов из JSON файла с использованием j_loads
                fonts = j_loads(json_file)
            
            # Добавление шрифтов
            for font_name, font_info in fonts.items():
                font_path = __root__ / 'assets' / 'fonts' / font_info['path']
                if not font_path.exists():
                    logger.error(f'Файл шрифта не найден: {font_path}')
                    raise FileNotFoundError(f'Файл шрифта не найден: {font_path}')
                   

                pdf.add_font(font_info['family'], font_info['style'], str(font_path), uni = font_info['uni'])

            # Установка шрифта по умолчанию
            pdf.set_font('DejaVuSans', style = 'book', size = 12)
            pdf.multi_cell(0, 10, data)
            pdf.output(str(pdf_file))
            logger.info(f'PDF отчет успешно сохранен: {pdf_file}')
            return True
        except FileNotFoundError as ex:
            # Логирование ошибки, если файл шрифта не найден
            logger.error(f'Ошибка при сохранении PDF через FPDF: Файл не найден: {ex}')
            return False
        except Exception as ex:
             # Логирование общей ошибки при сохранении PDF через FPDF
            logger.error(f'Ошибка при сохранении PDF через FPDF: {ex}')
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
            # Логирование ошибки при сохранении PDF через WeasyPrint
            logger.error(f"Ошибка при сохранении PDF через WeasyPrint: {ex}")
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
                    #  Убедимся, что строка имеет кодировку UTF-8
                    data_utf8 = data.encode('utf-8').decode('utf-8')  #  Преобразуем строку обратно в UTF-8, если нужно
                    try:
                        pisa.CreatePDF(data, dest=result_file)
                    except Exception as ex:
                         # Логирование ошибки компиляции PDF
                        logger.error(f"Ошибка компиляции PDF: {ex}")
                        
                else:
                    with open(data, "r", encoding="utf-8") as source_file:
                        try:
                            #  Прочитаем файл в кодировке UTF-8
                            source_data = source_file.read()
                            pisa.CreatePDF(source_data, dest=result_file, encoding='UTF-8')
                        except Exception as ex:
                            # Логирование ошибки компиляции PDF
                            logger.error(f"Ошибка компиляции PDF: {ex}")
                            
            logger.info(f"PDF успешно сохранен: {pdf_file}")
            return True
        except Exception as ex:
            # Логирование ошибки при сохранении PDF через xhtml2pdf
            logger.error(f"Ошибка при сохранении PDF через xhtml2pdf: {ex}")
            return False

    @staticmethod
    def html2pdf(html_str: str, pdf_file: str | Path) -> bool | None:
         """
         Конвертирует HTML-контент в PDF-файл с использованием WeasyPrint.
         
         :param html_str: HTML контент в виде строки.
         :type html_str: str
         :param pdf_file: Путь к выходному PDF-файлу.
         :type pdf_file: str | Path
         :return: `True`, если PDF успешно сохранен, иначе `None`.
         :rtype: bool | None
         """
         try:
             HTML(string=html_str).write_pdf(pdf_file)
             return True
         except Exception as ex:
            # Логирование ошибки при генерации PDF
            logger.error(f"Ошибка при генерации PDF: {ex}")
            return None

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
            #  Извлечение текста из PDF
            text = extract_text(str(pdf_file))

            #  Создание HTML-файла
            with open(html_file, 'w', encoding='utf-8') as file:
                file.write(f"<html><body>{text}</body></html>")

            logger.info(f"HTML успешно сохранен: {html_file}")
            return True
        except Exception as ex:
             # Логирование ошибки при конвертации PDF в HTML
            logger.error(f"Ошибка при конвертации PDF в HTML: {ex}")
            return False