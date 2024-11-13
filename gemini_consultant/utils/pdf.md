```python
## \file hypotez/src/utils/pdf.py
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe # <- venv win
## ~~~~~~~~~~~~~
""" module: src.utils """


"""
Модуль для преобразования HTML-контента или файлов в PDF с использованием библиотеки `pdfkit`.
Дополнительная информация:
- https://chatgpt.com/share/672266a3-0048-800d-a97b-c38f647d496b
- https://stackoverflow.com/questions/73599970/how-to-solve-wkhtmltopdf-reported-an-error-exit-with-code-1-due-to-network-err
- https://habr.com/ru/companies/bothub/articles/853490/
"""

import pdfkit
from pathlib import Path
import os
from reportlab.pdfgen import canvas
from src.logger import logger
from fpdf import FPDF

from . import wkhtmltopdf_bin_path  # Import the function from the correct place

# Make sure wkhtmltopdf_bin_path is a Path object
wkhtmltopdf_exe = Path(wkhtmltopdf_bin_path) / 'wkhtmltopdf.exe'


if not wkhtmltopdf_exe.exists():
    logger.error("Не найден wkhtmltopdf.exe по указанному пути.")
    raise FileNotFoundError("wkhtmltopdf.exe отсутствует")

configuration = pdfkit.configuration(
    wkhtmltopdf=str(wkhtmltopdf_exe)
)

options = {"enable-local-file-access": ""}


class PDFUtils:
    """!
    Класс для работы с PDF-файлами, предоставляющий методы для сохранения HTML-контента в PDF.
    """

    @staticmethod
    def save_pdf(data: str | Path, pdf_file: str | Path) -> bool:
        """!
        Сохранить HTML-контент или файл в PDF.

        Args:
            data (str | Path): HTML-контент или путь к HTML-файлу.
            pdf_file (str | Path): Путь к сохраняемому PDF-файлу.

        Returns:
            bool: `True` если PDF успешно сохранен, иначе `False`.

        Raises:
            pdfkit.PDFKitError: Ошибка генерации PDF через `pdfkit`.
            OSError: Ошибка доступа к файлу.
        """
        try:
            if isinstance(data, str):
                # Преобразование HTML-контента в PDF
                pdfkit.from_string(data, str(pdf_file), configuration=configuration, options=options)
            elif isinstance(data, Path):
                # Преобразование HTML-файла в PDF
                pdfkit.from_file(str(data), str(pdf_file), configuration=configuration, options=options)
            else:
                logger.error("Неверный тип данных для data. Ожидается str или Path.")
                return False

            logger.info(f"PDF успешно сохранен: {pdf_file}")
            return True
        except (pdfkit.PDFKitError, OSError) as ex:
            logger.error(f"Ошибка генерации PDF: {ex}", exc_info=True)
            return False
        except Exception as ex:
            logger.error(f"Неожиданная ошибка: {ex}", exc_info=True)
            return False

    @staticmethod
    def save_pdf_v2(data: str, pdf_file: str | Path) -> bool:
        """!
        Альтернативный метод сохранения текста в PDF с использованием библиотеки FPDF.

        Args:
            data (str): Текст, который необходимо сохранить в PDF.
            pdf_file (str | Path): Путь к сохраняемому PDF-файлу.

        Returns:
            bool: `True` если PDF успешно сохранен, иначе `False`.
        """
        try:
            pdf = FPDF()
            pdf.add_page()
            pdf.set_auto_page_break(auto=True, margin=15)
            # Важно: Установите шрифт, если он не встроен
            try:
                pdf.add_font('DejaVu', '', 'DejaVuSans.ttf', uni=True) # Укажите корректный путь
            except Exception as ex:
                logger.error(f"Ошибка добавления шрифта: {ex}")
                return False

            pdf.set_font('DejaVu', size=12)
            pdf.multi_cell(0, 10, data)
            pdf.output(str(pdf_file))
            logger.info(f"PDF отчет успешно сохранен: {pdf_file}")
            return True
        except Exception as ex:
            logger.error(f"Ошибка при сохранении PDF через FPDF: {ex}", exc_info=True)
            return False
```

**Изменения и улучшения:**

* **Тип данных `data`:** Теперь `save_pdf` корректно обрабатывает как строки, так и объекты `Path` для `data`.  Добавлена проверка типа, чтобы избежать ошибок.
* **Обработка путей:** Метод `save_pdf` теперь преобразует пути к файлам в строки для корректной работы `pdfkit.from_file`.
* **Добавление шрифта:** В `save_pdf_v2` добавлен обработчик ошибок при добавлении шрифта.  Важно:  **Убедитесь, что файл шрифта `DejaVuSans.ttf` находится в той же папке, что и ваш скрипт или укажите корректный путь.**  Не используйте `путь/к/DejaVuSans.ttf`.
* **Использование `Path`:** `wkhtmltopdf_exe` теперь корректно создается как объект `Path`, что делает код более устойчивым к различным вариантам ввода путей.
* **Улучшенная логика ошибок:** Добавлены более информативные сообщения об ошибках и обработка исключений `Exception` для лучшей диагностики проблем.


**Как использовать:**

```python
from utils import pdf  # Assuming your utils module is in the correct location

html_content = "<html><body><h1>Мой HTML-контент</h1></body></html>"

# Сохранение из контента
success = pdf.PDFUtils.save_pdf(html_content, "output.pdf")
if success:
    print("PDF успешно сохранен")

# Сохранение из файла
file_path = Path("input.html")  # Create input.html file with html content
success = pdf.PDFUtils.save_pdf(file_path, "output2.pdf")
if success:
    print("PDF успешно сохранен")


text_to_save = "Это текст, который нужно сохранить в PDF"
success = pdf.PDFUtils.save_pdf_v2(text_to_save, "output_text.pdf")
if success:
    print("Текст успешно сохранен в PDF")
```

**Важно:**

- Установите необходимые библиотеки: `pdfkit`, `reportlab`, `fpdf`.
- Убедитесь, что `wkhtmltopdf.exe` находится в указанной папке.
- Предоставьте корректный путь к шрифту (`DejaVuSans.ttf`) в `save_pdf_v2`.

Этот улучшенный код более надежен и устойчив к различным ошибкам, связанным с путями к файлам и обработкой данных.