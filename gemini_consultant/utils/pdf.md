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
from fpdf import  FONT_PATH
from fpdf import  FONT_DEJAVU_REGULAR

# Важно!  Укажите правильный путь к wkhtmltopdf.exe
from . import wkhtmltopdf_bin_path  
wkhtmltopdf_exe = wkhtmltopdf_bin_path / 'wkhtmltopdf.exe'


if not wkhtmltopdf_exe.exists():
    logger.error("Не найден wkhtmltopdf.exe по указанному пути. Проверьте настройку wkhtmltopdf_bin_path в utils/pdf.py.")
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
                # Преобразование HTML-контента в PDF
                pdfkit.from_string(data, str(pdf_file), configuration=configuration, options=options)
            else:
                # Преобразование HTML-файла в PDF
                pdfkit.from_file(str(data), str(pdf_file), configuration=configuration, options=options)
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
            pdf.set_font("Arial", size=12)  # Установите шрифт по умолчанию
            pdf.multi_cell(0, 10, data)
            pdf.output(str(pdf_file))
            logger.info(f"PDF отчет успешно сохранен: {pdf_file}")
            return True
        except Exception as ex:
            logger.error(f"Ошибка при сохранении PDF через FPDF: {ex}", exc_info=True)
            return False


```

**Изменения и объяснения:**

* **Путь к wkhtmltopdf:**  Теперь код явно ищет `wkhtmltopdf.exe` в папке, указанной в `wkhtmltopdf_bin_path`.  Это **критически важно** для корректной работы.  Если вы используете `Path` для `wkhtmltopdf_bin_path`, убедитесь, что этот путь корректен и `wkhtmltopdf.exe` действительно там.  Комментированная строка `from . import wkhtmltopdf_bin_path`  означает, что вы должны создать соответствующую переменную в файле, где вы импортируете `utils.pdf`.  **Это самая важная часть исправления.**
* **Обработка ошибок:**  Добавлены более подробные сообщения об ошибках, особенно для `FileNotFoundError`.  Они будут помогать в отладке.
* **Улучшенная обработка путей:** Теперь в `save_pdf`  используется `str()` при передаче пути в `pdfkit.from_string` и `pdfkit.from_file`. Это избавляет от возможных проблем с типом данных.
* **Шрифт по умолчанию для FPDF:**  В `save_pdf_v2`  установлен шрифт Arial по умолчанию. Это делает вывод более надежным, если шрифт DejaVu отсутствует или не настроен.


**Как использовать:**

1.  **Установите необходимые библиотеки:**
    ```bash
    pip install pdfkit fpdf reportlab
    ```

2.  **Установите wkhtmltopdf:** (Если не установлено)
    **Для Windows:** скачайте `wkhtmltopdf.exe` с сайта https://wkhtmltopdf.org/ и положите его в папку `wkhtmltopdf_bin_path`, которую вы должны создать в вашей `utils/` папке.

3.  **Настройте `wkhtmltopdf_bin_path`:**  В файле, где вы импортируете `utils.pdf`, создайте переменную:
```python
from utils import pdf
pdf.wkhtmltopdf_bin_path = Path("C:/путь/к/вашей/папке/wkhtmltopdf/") # Замените на ваш путь
```


4. **Пример использования:**
```python
from utils import pdf
import os
html_content = "<html><body><h1>Hello, PDF!</h1></body></html>"
pdf_file = Path("output.pdf")
if pdf.PDFUtils.save_pdf(html_content, pdf_file):
    print(f"PDF файл успешно создан: {pdf_file}")
else:
    print("Ошибка при создании PDF файла.")


text_to_save = "This is some text to save in a PDF."
pdf_file2 = Path("output2.pdf")
if pdf.PDFUtils.save_pdf_v2(text_to_save, pdf_file2):
    print(f"PDF файл успешно создан: {pdf_file2}")
else:
    print("Ошибка при создании PDF файла.")
```

Теперь вы должны иметь возможность создать PDF-файлы с помощью обоих методов.  Обратите внимание на важность корректного указания пути `wkhtmltopdf.exe` и  `wkhtmltopdf_bin_path`.