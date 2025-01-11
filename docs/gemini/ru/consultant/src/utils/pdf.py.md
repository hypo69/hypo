# Анализ кода модуля `pdf`

**Качество кода**
7
- Плюсы
    - Код разбит на функции, что улучшает читаемость и поддерживаемость.
    - Используется `logger` для логирования ошибок.
    - Есть docstring для функций и классов.
    - Код работает с разными библиотеками для генерации PDF.
- Минусы
    - Используется `json.load` вместо `j_loads` или `j_loads_ns`.
    - Не все блоки `try-except` обрабатываются через `logger.error`, некоторые используют `print`.
    - В коде встречаются лишние `...`  точки останова.
    - Не везде соблюдается единый стиль кавычек (использованы как одинарные так и двойные)
    - Не во всех методах и функциях есть подробное описание в формате rst.
    - В блоках кода, которые необходимо изменить отсутствуют комментарии с `#`
    -  Некоторые комментарии несут слишком общий характер, и не объясняют предназначения блока кода

**Рекомендации по улучшению**

1.  **Импорты:** Добавьте недостающие импорты, такие как `Any` и `SimpleNamespace` из `types`.
2.  **`json.load`:** Замените `json.load` на `j_loads` из `src.utils.jjson`.
3.  **Обработка ошибок:** Используйте `logger.error` вместо `print` для логирования ошибок.
4.  **Формат кавычек**: Приведите в соответствие одинарные кавычки в коде.
5.  **`try-except`:** Сократите использование `try-except`, где это возможно, заменив на `logger.error`.
6.  **Документация:** Добавьте более подробные docstring в формате RST для всех функций, классов и переменных.
7.  **Удалить** `...`  точки останова.
8.  **Комментарии:** Добавьте подробные комментарии перед блоками кода.
9.  **Форматирование кода**: Используйте `black` для автоматического форматирования кода.

**Оптимизированный код**

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
from __future__ import annotations

import os
import sys
from pathlib import Path
from typing import Any
from types import SimpleNamespace

import pdfkit
from fpdf import FPDF
from pdfminer.high_level import extract_text
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from weasyprint import HTML
from xhtml2pdf import pisa

from src.logger.logger import logger
# from src.utils.printer import pprint
from src.utils.jjson import j_loads


def set_project_root(marker_files: tuple[str, ...] = ('__root__', '.git')) -> Path:
    """
    Находит корневой каталог проекта, начиная с каталога текущего файла,
    поиска вверх и остановки на первом каталоге, содержащем любой из файлов-маркеров.

    Args:
        marker_files (tuple): Имена файлов или каталогов для идентификации корня проекта.

    Returns:
        Path: Путь к корневому каталогу, если найден, иначе каталог, где находится скрипт.
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
"""__root__ (Path): Путь к корневому каталогу проекта"""

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

        Args:
            data (str | Path): HTML-контент или путь к HTML-файлу.
            pdf_file (str | Path): Путь к сохраняемому PDF-файлу.

        Returns:
            bool: `True`, если PDF успешно сохранен, иначе `False`.

        Raises:
            pdfkit.PDFKitError: Ошибка генерации PDF через `pdfkit`.
            OSError: Ошибка доступа к файлу.
        """
        try:
            # Настройка pdfkit с указанием пути к wkhtmltopdf
            configuration = pdfkit.configuration(wkhtmltopdf=str(wkhtmltopdf_exe))
            # Включение локального доступа к файлам
            options = {'enable-local-file-access': ''}
            # Проверка, является ли data строкой или путем к файлу
            if isinstance(data, str):
                # Преобразование HTML-контента в PDF
                pdfkit.from_string(data, pdf_file, configuration=configuration, options=options)
            else:
                # Преобразование HTML-файла в PDF
                pdfkit.from_file(str(data), pdf_file, configuration=configuration, options=options)
            logger.info(f'PDF успешно сохранен: {pdf_file}')
            return True
        except Exception as ex:
            # Логирование ошибки и возврат False в случае неудачи
            logger.error('Неожиданная ошибка при генерации PDF через pdfkit:', ex)
            return False

    @staticmethod
    def save_pdf_fpdf(data: str, pdf_file: str | Path) -> bool:
        """
        Сохраняет текст в PDF с использованием библиотеки FPDF.

        Args:
            data (str): Текст, который необходимо сохранить в PDF.
            pdf_file (str | Path): Путь к сохраняемому PDF-файлу.

        Returns:
            bool: `True`, если PDF успешно сохранен, иначе `False`.
        """
        try:
            # Создание объекта PDF
            pdf = FPDF()
            pdf.add_page()
            pdf.set_auto_page_break(auto=True, margin=15)

            # Путь к файлу шрифтов
            fonts_file_path = __root__ / 'assets' / 'fonts' / 'fonts.json'
            # Проверка наличия файла шрифтов
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

            # Загрузка шрифтов из json файла
            with open(fonts_file_path, 'r', encoding='utf-8') as json_file:
                fonts = j_loads(json_file)
            # Добавление шрифтов
            for font_name, font_info in fonts.items():
                font_path = __root__ / 'assets' / 'fonts' / font_info['path']
                if not font_path.exists():
                    logger.error(f'Файл шрифта не найден: {font_path}')
                    raise FileNotFoundError(f'Файл шрифта не найден: {font_path}')

                pdf.add_font(font_info['family'], font_info['style'], str(font_path), uni=font_info['uni'])
            # Установка шрифта
            pdf.set_font('DejaVuSans', style='book', size=12)
            # Запись текста в PDF
            pdf.multi_cell(0, 10, data)
            # Сохранение PDF файла
            pdf.output(str(pdf_file))
            logger.info(f'PDF отчет успешно сохранен: {pdf_file}')
            return True
        except Exception as ex:
            # Логирование ошибки и возврат False в случае неудачи
            logger.error('Ошибка при сохранении PDF через FPDF: ', ex)
            return False

    @staticmethod
    def save_pdf_weasyprint(data: str | Path, pdf_file: str | Path) -> bool:
        """
        Сохраняет HTML-контент или файл в PDF с использованием библиотеки `WeasyPrint`.

        Args:
            data (str | Path): HTML-контент или путь к HTML-файлу.
            pdf_file (str | Path): Путь к сохраняемому PDF-файлу.

        Returns:
            bool: `True`, если PDF успешно сохранен, иначе `False`.
        """
        try:
            # Проверка, является ли data строкой или путем к файлу
            if isinstance(data, str):
                # Преобразование HTML-контента в PDF
                HTML(string=data).write_pdf(pdf_file)
            else:
                # Преобразование HTML-файла в PDF
                HTML(filename=str(data)).write_pdf(pdf_file)
            logger.info(f'PDF успешно сохранен: {pdf_file}')
            return True
        except Exception as ex:
            # Логирование ошибки и возврат False в случае неудачи
            logger.error('Ошибка при сохранении PDF через WeasyPrint: ', ex)
            return False

    @staticmethod
    def save_pdf_xhtml2pdf(data: str | Path, pdf_file: str | Path) -> bool:
        """
        Сохраняет HTML-контент или файл в PDF с использованием библиотеки `xhtml2pdf`.

        Args:
            data (str | Path): HTML-контент или путь к HTML-файлу.
            pdf_file (str | Path): Путь к сохраняемому PDF-файлу.

        Returns:
            bool: `True`, если PDF успешно сохранен, иначе `False`.
        """
        try:
            # Открытие PDF-файла для записи
            with open(pdf_file, 'w+b') as result_file:
                # Проверка, является ли data строкой или путем к файлу
                if isinstance(data, str):
                    # Преобразование строки в UTF-8
                    data_utf8 = data.encode('utf-8').decode('utf-8')
                    try:
                        # Создание PDF из HTML-строки
                        pisa.CreatePDF(data_utf8, dest=result_file)
                    except Exception as ex:
                        # Логирование ошибки
                        logger.error('Ошибка компиляции PDF: ', ex)
                else:
                    # Открытие HTML-файла для чтения
                    with open(data, 'r', encoding='utf-8') as source_file:
                        try:
                            # Чтение HTML-контента из файла
                            source_data = source_file.read()
                            # Создание PDF из HTML-файла
                            pisa.CreatePDF(source_data, dest=result_file, encoding='UTF-8')
                        except Exception as ex:
                            # Логирование ошибки
                            logger.error('Ошибка компиляции PDF: ', ex)
            logger.info(f'PDF успешно сохранен: {pdf_file}')
            return True
        except Exception as ex:
            # Логирование ошибки и возврат False в случае неудачи
            logger.error('Ошибка при сохранении PDF через xhtml2pdf: ', ex)
            return False

    @staticmethod
    def html2pdf(html_str: str, pdf_file: str | Path) -> bool | None:
        """Конвертирует HTML-контент в PDF-файл, используя WeasyPrint."""
        try:
            # Преобразование HTML в PDF с помощью WeasyPrint
            HTML(string=html_str).write_pdf(pdf_file)
            return True
        except Exception as e:
            # Логирование ошибки и возврат None в случае неудачи
            logger.error(f"Ошибка при генерации PDF: {e}")
            return

    @staticmethod
    def pdf_to_html(pdf_file: str | Path, html_file: str | Path) -> bool:
        """
        Конвертирует PDF-файл в HTML-файл.

        Args:
            pdf_file (str | Path): Путь к исходному PDF-файлу.
            html_file (str | Path): Путь к сохраняемому HTML-файлу.

        Returns:
            bool: `True`, если конвертация прошла успешно, иначе `False`.
        """
        try:
            # Извлечение текста из PDF-файла
            text = extract_text(str(pdf_file))
            # Создание HTML-файла
            with open(html_file, 'w', encoding='utf-8') as file:
                # Запись HTML-контента в файл
                file.write(f'<html><body>{text}</body></html>')

            logger.info(f'HTML успешно сохранен: {html_file}')
            return True
        except Exception as ex:
            # Логирование ошибки и возврат False в случае неудачи
            logger.error(f'Ошибка при конвертации PDF в HTML: {ex}')
            return False

    @staticmethod
    def dict2pdf(data: dict | SimpleNamespace, file_path: str | Path) -> None:
        """
        Сохраняет данные словаря в PDF-файл.

        Args:
            data (dict | SimpleNamespace): Словарь для преобразования в PDF.
            file_path (str | Path): Путь к выходному PDF-файлу.
        """
        # Преобразование SimpleNamespace в словарь, если необходимо
        if isinstance(data, SimpleNamespace):
            data = data.__dict__

        # Создание PDF-документа
        pdf = canvas.Canvas(str(file_path), pagesize=A4)
        width, height = A4
        x, y = 50, height - 50

        # Установка шрифта
        pdf.setFont('Helvetica', 12)

        # Запись данных словаря в PDF
        for key, value in data.items():
            line = f'{key}: {value}'
            pdf.drawString(x, y, line)
            y -= 20

            # Создание новой страницы при достижении низа текущей
            if y < 50:
                pdf.showPage()
                pdf.setFont('Helvetica', 12)
                y = height - 50

        # Сохранение PDF-файла
        pdf.save()
```