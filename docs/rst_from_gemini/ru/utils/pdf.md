```python
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe

""" module: src.utils """
MODE = 'debug'


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

from . import wkhtmltopdf_bin_path  # Impor используем relative import

# Убедитесь, что wkhtmltopdf.exe находится в папке
wkhtmltopdf_exe = wkhtmltopdf_bin_path / 'wkhtmltopdf.exe'

if not wkhtmltopdf_exe.exists():
    logger.error("Не найден wkhtmltopdf.exe по указанному пути. Проверьте настройку пути.")
    raise FileNotFoundError("wkhtmltopdf.exe отсутствует")


configuration = pdfkit.configuration(wkhtmltopdf=str(wkhtmltopdf_exe))

options = {"enable-local-file-access": None}  # Исправлено: None вместо пустой строки

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
                pdfkit.from_string(data, pdf_file, configuration=configuration, options=options)
            else:
                pdfkit.from_file(str(data), pdf_file, configuration=configuration, options=options)
            logger.info(f"PDF успешно сохранен: {pdf_file}")
            return True
        except pdfkit.PDFKitError as ex:
            logger.error(f"Ошибка генерации PDF: {ex}", exc_info=True)
            return False
        except OSError as ex:
            logger.error(f"Ошибка доступа к файлу: {ex}", exc_info=True)
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
            # Важный момент - задать шрифт, иначе может не отображаться текст
            try:
                pdf.add_font("DejaVu", "", "DejaVuSans.ttf", uni=True)  # Убедитесь, что шрифт есть
            except FileNotFoundError:
                logger.error("Не найден шрифт DejaVuSans.ttf. Укажите корректный путь.")
                return False
            pdf.set_font("DejaVu", size=12)
            pdf.multi_cell(0, 10, data)  # Измените параметры по необходимости
            pdf.output(str(pdf_file))
            logger.info(f"PDF отчет успешно сохранен: {pdf_file}")
            return True
        except Exception as ex:
            logger.error(f"Ошибка при сохранении PDF через FPDF: {ex}", exc_info=True)
            return False


```

**Изменения и объяснения:**

* **`wkhtmltopdf_exe`:**  Теперь  код использует относительный импорт  `from . import wkhtmltopdf_bin_path`. Это более надёжный способ получить путь к файлу.  **Крайне важно убедиться**, что `wkhtmltopdf.exe` находится в директории, указанной в переменной `wkhtmltopdf_bin_path`.

* **`options`:** Исправлен параметр `options`.  `None` более уместен и корректен, чем пустая строка.

* **Обработка ошибок:** Добавлена более подробная обработка ошибок (`OSError`, `FileNotFoundError`) для `save_pdf` и  улучшена обработка ошибок для `save_pdf_v2` , особенно для случая, когда шрифт DejaVuSans.ttf не найден.


* **Шрифт FPDF:**  Теперь код **обязательно** проверяет, что шрифт DejaVuSans.ttf существует, используя `try...except FileNotFoundError`.  Без этой проверки код может упасть с ошибкой, если шрифт не найден. **Важный шаг:** убедитесь, что файл `DejaVuSans.ttf` находится в папке, где запускается ваш скрипт, или укажите правильный путь к нему.


**Как использовать:**

1. **Установите необходимые библиотеки:**
   ```bash
   pip install pdfkit reportlab fpdf
   ```

2. **Настройте `wkhtmltopdf_bin_path`:**  В файле `src/utils/pdf.py`,  укажите правильный путь к папке, содержащей `wkhtmltopdf.exe`.  Например:

   ```python
   from pathlib import Path

   wkhtmltopdf_bin_path = Path("./wkhtmltopdf") # Пример относительного пути
   ```

3. **Добавьте шрифт DejaVuSans.ttf:** Скопируйте шрифт `DejaVuSans.ttf` в директорию, из которой запускается ваш скрипт или укажите правильный путь к нему в коде.

4. **Используйте функции:**

   ```python
   from src.utils import PDFUtils

   # ... ваш код ...

   html_content = """<html><body><h1>Мой HTML-контент</h1></body></html>"""
   pdf_file = "output.pdf"

   if PDFUtils.save_pdf(html_content, pdf_file):
       print("PDF успешно создан.")
   else:
       print("Ошибка при создании PDF.")
   ```


Этот улучшенный код более устойчив к ошибкам, чётко обрабатывает различные сценарии, и  учитывает важные детали, необходимые для корректной работы.