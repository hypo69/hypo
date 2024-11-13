```python
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

from . import wkhtmltopdf_bin_path        
wkhtmltopdf_exe = wkhtmltopdf_bin_path /  'wkhtmltopdf.exe'

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
              raise TypeError("data должен быть строкой или объектом Path")
            logger.info(f"PDF успешно сохранен: {pdf_file}")
            return True
        except (pdfkit.PDFKitError, OSError) as ex:
            logger.error(f"Ошибка генерации PDF: {ex}", exc_info=True)
            return False
        except TypeError as e:
            logger.error(f"Ошибка типа данных: {e}")
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

            # Важно: Используем кодировку UTF-8
            pdf.add_font("DejaVu", "", "DejaVuSans.ttf", uni=True)  # Убедитесь, что шрифт существует
            pdf.set_font("DejaVu", size=12)
            pdf.multi_cell(0, 10, data,  encoding='UTF-8')  # Добавляем кодировку
            pdf.output(str(pdf_file), 'F')  # output в F-режиме для сохранения
            logger.info(f"PDF отчет успешно сохранен: {pdf_file}")
            return True
        except Exception as ex:
            logger.error(f"Ошибка при сохранении PDF через FPDF: {ex}", exc_info=True)
            return False


```

**Изменения и объяснения:**

* **Обработка типов данных:** Добавлена проверка типа `data` в методе `save_pdf`. Теперь он корректно обрабатывает как строки, так и объекты `Path`.  Добавлена обработка `TypeError`, если `data` не является ожидаемого типа.
* **Обработка путей:** Изменены вызовы `pdfkit.from_string` и `pdfkit.from_file` на использование `str(pdf_file)` и `str(data)` внутри функций для корректной работы с объектами `Path`.
* **Кодировка UTF-8:** В методе `save_pdf_v2` добавлена кодировка UTF-8 при вызове `pdf.multi_cell`. Это критично для корректного отображения кириллицы и других символов.
* **Обработка шрифта:** Изменен путь к шрифту  `pdf.add_font("DejaVu", "", "DejaVuSans.ttf", uni=True)` чтобы использовать путь непосредственно к шрифту `DejaVuSans.ttf`.  **Важно:**  Убедитесь, что шрифт `DejaVuSans.ttf` находится в той же папке, что и ваш скрипт, или укажите его абсолютный путь.

**Важные моменты:**

* **Путь к шрифту:** Убедитесь, что путь к шрифту `DejaVuSans.ttf` правильный.  Если шрифт находится в другом месте, укажите корректный абсолютный путь.
* **Шрифт DejaVu:** Удостоверьтесь, что шрифт DejaVuSans.ttf есть на вашей системе. Если он отсутствует, код выдаст ошибку. Рассмотрите возможность скачивания шрифта и его размещения в доступной директории.
* **pdfkit.from_string:**  Этот метод создает временный файл, поэтому нет необходимости явно создавать его.

**Как использовать:**

```python
from utils.pdf import PDFUtils
from pathlib import Path

# Пример использования save_pdf (HTML):
html_content = "<html><body><h1>Заголовок</h1></body></html>"
pdf_output = Path("output.pdf")

if PDFUtils.save_pdf(html_content, pdf_output):
  print("PDF успешно создан.")
else:
  print("Ошибка при создании PDF.")

# Пример использования save_pdf (файл):
html_file = Path("input.html")

if PDFUtils.save_pdf(html_file, pdf_output):
    print("PDF успешно создан.")
else:
    print("Ошибка при создании PDF.")


# Пример использования save_pdf_v2 (текст):
text_data = "Привет, мир! Это текст для сохранения в PDF."
pdf_output = Path("output_text.pdf")

if PDFUtils.save_pdf_v2(text_data, pdf_output):
    print("PDF успешно создан.")
else:
    print("Ошибка при создании PDF.")
```

Этот улучшенный код должен работать надежнее и учитывать различные ситуации, возникающие при работе с файлами и путями.  Проверьте, что все необходимые библиотеки установлены (`pdfkit`, `fpdf`, `reportlab`). Не забудьте, что вам нужно установить wkhtmltopdf.