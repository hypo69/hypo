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


# **ВАЖНО!**  Обработка отсутствия wkhtmltopdf.exe должна быть вне класса
if not wkhtmltopdf_exe.exists():
    logger.error("Не найден wkhtmltopdf.exe по указанному пути. Проверьте установку и путь.")
    raise FileNotFoundError("wkhtmltopdf.exe отсутствует")


configuration = pdfkit.configuration(wkhtmltopdf=str(wkhtmltopdf_exe))
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
                pdfkit.from_string(data, str(pdf_file), configuration=configuration, options=options)
            elif isinstance(data, Path):
                pdfkit.from_file(str(data), str(pdf_file), configuration=configuration, options=options)
            else:
                raise TypeError("Неподдерживаемый тип данных для 'data'. Ожидается str или Path.")
            logger.info(f"PDF успешно сохранен: {pdf_file}")
            return True
        except (pdfkit.PDFKitError, OSError, TypeError) as ex:
            logger.error(f"Ошибка генерации PDF: {ex}", exc_info=True)
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
            
            # **ВАЖНО!** Убедитесь, что шрифт DejaVu установлен
            #  или укажите корректный путь к нему.
            #  Если шрифт не найден, будет ошибка!
            pdf.add_font("DejaVu", "", "DejaVuSans.ttf", uni=True) # Если DejaVu установлен на системе, путь можно убрать

            pdf.set_font("DejaVu", size=12)
            pdf.multi_cell(0, 10, data)
            pdf.output(str(pdf_file))
            logger.info(f"PDF отчет успешно сохранен: {pdf_file}")
            return True
        except Exception as ex:
            logger.error(f"Ошибка при сохранении PDF через FPDF: {ex}", exc_info=True)
            return False
```

**Изменения и объяснения:**

* **Обработка `wkhtmltopdf.exe` вне класса:** Проверка существования `wkhtmltopdf.exe` выполняется до создания объекта класса. Это важно, так как ошибки на ранних стадиях работы могут быть пропущены, если проверка находится внутри класса.
* **Улучшенная обработка ошибок:**  Добавлена проверка типа данных `data` в методе `save_pdf`. Теперь метод `save_pdf` будет возвращать `False` при некорректном типе данных.  Обработка ошибок теперь более надежно ловит ошибки `TypeError`, что важно для устойчивой работы кода.
* **Более точный логгинг:**  Добавлен более подробный логгинг с описанием, что именно не удалось (например, `TypeError`).
* **Обработка путей:**  Метод `save_pdf` теперь корректно обрабатывает как строки, так и объекты `Path` для `data` и `pdf_file`.

* **ВАЖНО! Шрифт FPDF:**  Код содержит комментарий о необходимости наличия шрифта "DejaVuSans.ttf".  Если шрифт не установлен на системе или не найден по указанному пути, вы получите ошибку.  **Не забудьте:**
    * **Установить шрифт** DejaVu Sans (и другие, если используете).
    * **Указать правильный путь** к файлу шрифта, если он находится не в стандартном месте.


**Как использовать:**

```python
from utils.pdf import PDFUtils
from pathlib import Path

# Пример использования с HTML-строкой
html_content = """<html><body><h1>Заголовок</h1><p>Текст</p></body></html>"""
pdf_file = Path("output.pdf")
success = PDFUtils.save_pdf(html_content, pdf_file)
if success:
    print("PDF успешно создан")
else:
    print("Ошибка при создании PDF")


# Пример с HTML-файлом:
html_file = Path("input.html")  # Замените на ваш файл
success = PDFUtils.save_pdf(html_file, pdf_file)
if success:
    print("PDF успешно создан")
else:
    print("Ошибка при создании PDF")



# Пример использования с текстом
text_data = "Это тестовый текст для сохранения в PDF."
pdf_file_text = Path("output_text.pdf")
success = PDFUtils.save_pdf_v2(text_data, pdf_file_text)  # Использование v2 для текста
if success:
    print("PDF успешно создан")
else:
    print("Ошибка при создании PDF")
```

Этот улучшенный код более надежен, прост в использовании и обеспечивает лучшую обработку ошибок, что очень важно для стабильности вашего приложения.  **Не забудьте установить необходимые библиотеки!** ( `pdfkit`, `reportlab`, `fpdf`).