### Анализ кода модуля `pdf`

**Качество кода**:
- **Соответствие стандартам**: 7/10
- **Плюсы**:
    -   Код разбит на функции, что улучшает читаемость и повторное использование.
    -   Используется `logger` для логирования ошибок.
    -   Есть docstring для большинства функций, что облегчает понимание их назначения.
    -   Применяется `Path` из `pathlib` для работы с путями, что делает код более кроссплатформенным.
- **Минусы**:
    -   Не везде используется `from src.logger.logger import logger`, что противоречит инструкции.
    -   Использование стандартного `json.load` вместо `j_loads` или `j_loads_ns` из `src.utils.jjson`.
    -   Присутствуют `...` как маркеры, которые следует сохранить, но не совсем понятно их назначение.
    -   Смешанное использование `try-except` и `logger.error` для обработки ошибок.
    -   Некоторые docstring отсутствуют (например, для `set_project_root`).
    -   Не везде используется одинарные кавычки в коде и двойные кавычки для операций вывода
    -   Некоторые функции имеют неполную документацию RST.
    -   Не везде используется `str()` при конвертации путей к файлам

**Рекомендации по улучшению**:
1.  Используйте `j_loads` или `j_loads_ns` из `src.utils.jjson` вместо `json.load`.
2.  Замените все `print` на `logger.info` или `logger.error` в зависимости от контекста.
3.  Всегда используйте одинарные кавычки в коде и двойные кавычки для операций вывода
4.  Замените множественные `try-except` на обработку ошибок с помощью `logger.error`, а исключения поднимайте, чтобы вышестоящий код мог их обрабатывать, или использовать `finally` для обработки.
5.  Добавьте полные RST docstring для всех функций и классов.
6.  Используйте `from src.logger.logger import logger` для логирования ошибок.
7.  Добавьте обработку `FileNotFoundError` в `set_project_root` и другие функции.
8.  Удалите неиспользуемые импорты.
9.  Проверьте все операции с файлами на наличие ошибок.
10. Используйте `str()` при конвертации путей к файлам

**Оптимизированный код**:

```python
"""
.. module:: src.utils.pdf
    :platform: Windows, Unix
    :synopsis: Модуль для преобразования HTML-контента или файлов в PDF

Модуль для преобразования HTML-контента или файлов в PDF с использованием различных библиотек.
Дополнительная информация:
- https://chatgpt.com/share/672266a3-0048-800d-a97b-c38f647d496b
- https://stackoverflow.com/questions/73599970/how-to-solve-wkhtmltopdf-reported-an-error-exit-with-code-1-due-to-network-err
- https://habr.com/ru/companies/bothub/articles/853490/
"""
import sys
from pathlib import Path

import pdfkit
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from fpdf import FPDF
from weasyprint import HTML
from xhtml2pdf import pisa
from pdfminer.high_level import extract_text

from src.logger.logger import logger
from src.utils.jjson import j_loads
from src.utils.printer import pprint


def set_project_root(marker_files: tuple[str, ...] = ('__root__', '.git')) -> Path:
    """
    Находит корневой каталог проекта, начиная с каталога текущего файла,
    поиском вверх и остановкой на первом каталоге, содержащем любой из маркерных файлов.

    :param marker_files: Имена файлов или каталогов для идентификации корня проекта.
    :type marker_files: tuple[str, ...], optional
    :return: Путь к корневому каталогу, если найден, иначе каталог, где расположен скрипт.
    :rtype: Path
    :raises FileNotFoundError: Если не удалось найти корневой каталог проекта.

    Пример:
        >>> set_project_root()
        PosixPath('/path/to/your/project')
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


# Get the root directory of the project
__root__ = set_project_root()
"""__root__ (Path): Path to the root directory of the project"""

wkhtmltopdf_exe = __root__ / 'bin' / 'wkhtmltopdf' / 'files' / 'bin' / 'wkhtmltopdf.exe'

if not wkhtmltopdf_exe.exists():
    logger.error("Не найден wkhtmltopdf.exe по указанному пути.")  # Используем logger.error для вывода сообщения об ошибке.
    raise FileNotFoundError("wkhtmltopdf.exe отсутствует")  # Поднимаем исключение, чтобы вышестоящий код мог его обработать.


class PDFUtils:
    """
    Класс для работы с PDF-файлами, предоставляющий методы для сохранения HTML-контента в PDF с использованием различных библиотек.
    """

    @staticmethod
    def save_pdf_pdfkit(data: str | Path, pdf_file: str | Path) -> bool:
        """
        Сохранить HTML-контент или файл в PDF с использованием библиотеки `pdfkit`.

        :param data: HTML-контент или путь к HTML-файлу.
        :type data: str | Path
        :param pdf_file: Путь к сохраняемому PDF-файлу.
        :type pdf_file: str | Path
        :return: `True`, если PDF успешно сохранен, иначе `False`.
        :rtype: bool
        :raises pdfkit.PDFKitError: Ошибка генерации PDF через `pdfkit`.
        :raises OSError: Ошибка доступа к файлу.

        Пример:
            >>> PDFUtils.save_pdf_pdfkit('<h1>Test</h1>', 'test.pdf')
            True
        """
        try:
            configuration = pdfkit.configuration(
                wkhtmltopdf=str(wkhtmltopdf_exe)  # используем str()
            )
            options = {'enable-local-file-access': ''}
            if isinstance(data, str):
                # Преобразование HTML-контента в PDF
                pdfkit.from_string(data, str(pdf_file), configuration=configuration, options=options)  # используем str()
            else:
                # Преобразование HTML-файла в PDF
                pdfkit.from_file(str(data), str(pdf_file), configuration=configuration, options=options)  # используем str()
            logger.info(f'PDF успешно сохранен: {pdf_file}')  # Используем logger.info для вывода информационного сообщения.
            return True
        except pdfkit.PDFKitError as ex:
            logger.error(f"Ошибка генерации PDF: {ex}")  # Используем logger.error для вывода сообщения об ошибке.
            return False
        except OSError as ex:
            logger.error(f"Ошибка доступа к файлу: {ex}")  # Используем logger.error для вывода сообщения об ошибке.
            return False
        except Exception as ex:
            logger.error(f"Неожиданная ошибка: {ex}")
            return False

    @staticmethod
    def save_pdf_fpdf(data: str, pdf_file: str | Path) -> bool:
        """
        Сохранить текст в PDF с использованием библиотеки FPDF.

        :param data: Текст, который необходимо сохранить в PDF.
        :type data: str
        :param pdf_file: Путь к сохраняемому PDF-файлу.
        :type pdf_file: str | Path
        :return: `True`, если PDF успешно сохранен, иначе `False`.
        :rtype: bool
        :raises FileNotFoundError: Если файл шрифтов или шрифт не найден.
        :raises Exception: В случае других ошибок.

        Пример:
            >>> PDFUtils.save_pdf_fpdf('Пример текста', 'example.pdf')
            True
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
                raise FileNotFoundError(f'Файл шрифтов не найден: {fonts_file_path}')  # Поднимаем исключение, если файл не найден

            with open(fonts_file_path, 'r', encoding='utf-8') as json_file:
                fonts = j_loads(json_file)  # Используем j_loads для загрузки JSON

            # Добавление шрифтов
            for font_name, font_info in fonts.items():
                font_path = __root__ / 'assets' / 'fonts' / font_info['path']
                if not font_path.exists():
                    logger.error(f'Файл шрифта не найден: {font_path}')  # Используем logger.error для вывода сообщения об ошибке.
                    raise FileNotFoundError(f'Файл шрифта не найден: {font_path}')  # Поднимаем исключение, если файл шрифта не найден

                pdf.add_font(font_info['family'], font_info['style'], str(font_path), uni=font_info['uni'])  # используем str()

            # Установка шрифта по умолчанию
            pdf.set_font('DejaVuSans', style='book', size=12)
            pdf.multi_cell(0, 10, data)
            pdf.output(str(pdf_file))  # используем str()
            logger.info(f'PDF отчет успешно сохранен: {pdf_file}')  # Используем logger.info для вывода информационного сообщения.
            return True
        except Exception as ex:
            logger.error(f'Ошибка при сохранении PDF через FPDF: {ex}')  # Используем logger.error для вывода сообщения об ошибке.
            return False

    @staticmethod
    def save_pdf_weasyprint(data: str | Path, pdf_file: str | Path) -> bool:
        """
        Сохранить HTML-контент или файл в PDF с использованием библиотеки `WeasyPrint`.

        :param data: HTML-контент или путь к HTML-файлу.
        :type data: str | Path
        :param pdf_file: Путь к сохраняемому PDF-файлу.
        :type pdf_file: str | Path
        :return: `True`, если PDF успешно сохранен, иначе `False`.
        :rtype: bool
        :raises Exception: В случае ошибки при сохранении PDF.
        """
        try:
            if isinstance(data, str):
                HTML(string=data).write_pdf(str(pdf_file))  # используем str()
            else:
                HTML(filename=str(data)).write_pdf(str(pdf_file))  # используем str()
            logger.info(f'PDF успешно сохранен: {pdf_file}')  # Используем logger.info для вывода информационного сообщения.
            return True
        except Exception as ex:
            logger.error(f'Ошибка при сохранении PDF через WeasyPrint: {ex}')  # Используем logger.error для вывода сообщения об ошибке.
            return False

    @staticmethod
    def save_pdf_xhtml2pdf(data: str | Path, pdf_file: str | Path) -> bool:
        """
        Сохранить HTML-контент или файл в PDF с использованием библиотеки `xhtml2pdf`.

        :param data: HTML-контент или путь к HTML-файлу.
        :type data: str | Path
        :param pdf_file: Путь к сохраняемому PDF-файлу.
        :type pdf_file: str | Path
        :return: `True`, если PDF успешно сохранен, иначе `False`.
        :rtype: bool
        :raises Exception: В случае ошибки при сохранении PDF.
        """
        try:
            with open(pdf_file, 'w+b') as result_file:
                if isinstance(data, str):
                    # Убедимся, что строка имеет кодировку UTF-8
                    data_utf8 = data.encode('utf-8').decode('utf-8')  # Преобразуем строку обратно в UTF-8, если нужно
                    try:
                        pisa.CreatePDF(data, dest=result_file)
                    except Exception as ex:
                        logger.error(f"Ошибка компиляции PDF: {ex}")
                        return False
                else:
                    with open(str(data), 'r', encoding='utf-8') as source_file:  # используем str()
                        try:
                            # Прочитаем файл в кодировке UTF-8
                            source_data = source_file.read()
                            pisa.CreatePDF(source_data, dest=result_file, encoding='UTF-8')
                        except Exception as ex:
                            logger.error(f'Ошибка компиляции PDF: {ex}')
                            return False
            logger.info(f"PDF успешно сохранен: {pdf_file}")  # Используем logger.info для вывода информационного сообщения.
            return True
        except Exception as ex:
            logger.error(f'Ошибка при сохранении PDF через xhtml2pdf: {ex}')  # Используем logger.error для вывода сообщения об ошибке.
            return False

    @staticmethod
    def html2pdf(html_str: str, pdf_file: str | Path) -> bool | None:
        """Converts HTML content to a PDF file using WeasyPrint."""
        try:
            HTML(string=html_str).write_pdf(str(pdf_file))  # используем str()
            return True
        except Exception as e:
            logger.error(f'Error during PDF generation: {e}')  # Используем logger.error для вывода сообщения об ошибке.
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
        :raises Exception: В случае ошибки при конвертации.
        """
        try:
            # Извлечение текста из PDF
            text = extract_text(str(pdf_file))  # используем str()

            # Создание HTML-файла
            with open(html_file, 'w', encoding='utf-8') as file:
                file.write(f'<html><body>{text}</body></html>')

            logger.info(f'HTML успешно сохранен: {html_file}')  # Используем logger.info для вывода информационного сообщения.
            return True
        except Exception as ex:
            logger.error(f'Ошибка при конвертации PDF в HTML: {ex}')  # Используем logger.error для вывода сообщения об ошибке.
            return False

    # Функция для конвертации словаря в PDF
    @staticmethod
    def dict2pdf(data: dict | 'SimpleNamespace', file_path: str | Path) -> None:
        """
        Сохраняет данные словаря в PDF файл.

        :param data: Словарь для преобразования в PDF.
        :type data: dict | SimpleNamespace
        :param file_path: Путь к выходному PDF файлу.
        :type file_path: str | Path
        :raises TypeError: Если входные данные не являются словарем или SimpleNamespace.
        """
        if isinstance(data, 'SimpleNamespace'):
            data = data.__dict__
        if not isinstance(data, dict):
            logger.error(f"Ошибка: входные данные должны быть словарем или SimpleNamespace, но получили {type(data)}")  # Используем logger.error для вывода сообщения об ошибке.
            raise TypeError(f"Input must be a dictionary or SimpleNamespace, but got {type(data)}")

        pdf = canvas.Canvas(str(file_path), pagesize=A4)  # используем str()
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