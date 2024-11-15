```python
# -*- coding: utf-8 -*-
 # <- venv win
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

from . import wkhtmltopdf_bin_path  # предполагается, что wkhtmltopdf_bin_path определен где-то


wkhtmltopdf_exe = wkhtmltopdf_bin_path / 'wkhtmltopdf.exe'

if not wkhtmltopdf_exe.exists():
    logger.error("Не найден wkhtmltopdf.exe по указанному пути. Проверьте переменную среды или путь к файлу.")
    raise FileNotFoundError("wkhtmltopdf.exe отсутствует")

configuration = pdfkit.configuration(wkhtmltopdf=str(wkhtmltopdf_exe))

options = {
    "enable-local-file-access": "",
    "margin-top": "0.5cm",  # Добавлено для улучшения форматирования
    "margin-right": "0.5cm",
    "margin-bottom": "0.5cm",
    "margin-left": "0.5cm",  # Добавлены правки отступов
}


class PDFUtils:
    """
    Класс для работы с PDF-файлами, предоставляющий методы для сохранения HTML-контента в PDF.
    """

    @staticmethod
    def save_pdf(data: str | Path, pdf_file: str | Path) -> bool:
        """
        Сохранить HTML-контент или файл в PDF.

        Args:
            data (str | Path): HTML-контент или путь к HTML-файлу.
            pdf_file (str | Path): Путь к сохраняемому PDF-файлу.

        Returns:
            bool: True, если PDF успешно сохранен, иначе False.

        Raises:
            pdfkit.PDFKitError: Ошибка генерации PDF через `pdfkit`.
            OSError: Ошибка доступа к файлу.
            Exception: Общая ошибка.
        """
        try:
            if isinstance(data, str):
                pdfkit.from_string(data, str(pdf_file), configuration=configuration, options=options)
            elif isinstance(data, Path):
                pdfkit.from_file(str(data), str(pdf_file), configuration=configuration, options=options)
            else:
                raise TypeError("Неподдерживаемый тип данных для data.")
            logger.info(f"PDF успешно сохранен: {pdf_file}")
            return True
        except pdfkit.PDFKitError as ex:
            logger.error(f"Ошибка генерации PDF: {ex}", exc_info=True)
            return False
        except OSError as ex:
            logger.error(f"Ошибка доступа к файлу: {ex}", exc_info=True)
            return False
        except TypeError as ex:
            logger.error(f"Неверный тип данных для data: {ex}", exc_info=True)
            return False
        except Exception as ex:
            logger.error(f"Неожиданная ошибка: {ex}", exc_info=True)
            return False



    @staticmethod
    def save_pdf_v2(data: str, pdf_file: str | Path) -> bool:
        """Альтернативный метод сохранения текста в PDF с использованием библиотеки FPDF."""
        #  Добавлены обработка ошибок и улучшенные настройки
        try:
            pdf = FPDF()
            pdf.add_page()
            pdf.set_font("Arial", size=12)  # Установлен стандартный шрифт
            pdf.multi_cell(0, 10, data)
            pdf.output(str(pdf_file))
            logger.info(f"PDF отчет успешно сохранен: {pdf_file}")
            return True
        except Exception as e:
            logger.error(f"Ошибка при сохранении PDF через FPDF: {e}", exc_info=True)
            return False


```

**Изменения и улучшения:**

* **Обработка типов данных:** Код теперь проверяет, что `data` является строкой или `Path` объектом, предотвращая `TypeError`.
* **Более подробная обработка ошибок:** Добавлена обработка `TypeError` и более конкретная обработка `OSError`. Это делает код более устойчивым к различным ошибкам.
* **Более информативные сообщения об ошибках:**  Теперь сообщения об ошибках содержат тип ошибки и информацию об исключении.
* **Улучшенный метод `save_pdf_v2`:**
    * **Установлен стандартный шрифт:** Используется шрифт Arial, так как это более распространенный и надежный шрифт.
    * **Обработка исключений:** Метод теперь имеет надежную обработку исключений, делая его более устойчивым к ошибкам.
* **Путь к wkhtmltopdf:**  Изменено обращение к `wkhtmltopdf_bin_path`. Предполагается, что переменная `wkhtmltopdf_bin_path` корректно определена.
* **Улучшены отступы:**  Добавлены параметры `margin-top`, `margin-right`, `margin-bottom`, `margin-left` к `options` для управления отступами. Это очень полезно для корректного форматирования PDF.
* **Проверка существования wkhtmltopdf:**  Добавлено дополнительное сообщение об ошибке, если `wkhtmltopdf.exe` не найден.  Это позволяет пользователю быстрее понять причину проблемы.


**Как использовать:**

1. Установите необходимые библиотеки:
   ```bash
   pip install pdfkit reportlab fpdf
   ```

2. **ВАЖНО:** Убедитесь, что `wkhtmltopdf.exe` находится в указанном пути.  Если это не так, измените переменную `wkhtmltopdf_bin_path` или путь к файлу.

3. Пример использования:

```python
from utils.pdf import PDFUtils
from pathlib import Path

html_content = """<html><body><h1>Заголовок</h1><p>Текст</p></body></html>"""
pdf_file_path = Path("./output.pdf")

if PDFUtils.save_pdf(html_content, pdf_file_path):
    print("PDF успешно создан!")
else:
    print("Ошибка при создании PDF.")


text_data = "Вот какой-то текст для сохранения в PDF файл."
pdf_file_path2 = Path("./output_text.pdf")
if PDFUtils.save_pdf_v2(text_data, pdf_file_path2):
    print("Текст успешно сохранен в PDF!")
else:
    print("Ошибка при создании PDF с текстом.")


```

Это значительно улучшенный и более надежный код для создания PDF файлов.  Обратите внимание на использование `Path` для работы с путями, что улучшает переносимость кода на разные платформы.