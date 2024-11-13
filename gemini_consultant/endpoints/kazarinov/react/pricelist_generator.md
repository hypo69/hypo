```python
## \file hypotez/src/endpoints/kazarinov/react/pricelist_generator.py
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe # <- venv win
## ~~~~~~~~~~~~~
""" module: src.endpoints.kazarinov.react """

#https://dev.to/kboskin/building-web-applications-with-react-and-python-2d8c

"""! Генератор HTML и PDF для мехиронов Казаринова

Описание работы:
- Конструктор `__init__`: Принимает шаблон, базовый путь, метку времени и язык.
- Метод `load_data`: Загружает данные из JSON-файла.
- Метод `generate_html`: Генерирует HTML с использованием Jinja2.
- Метод `save_html`: Сохраняет HTML в файл.
- Метод `generate_pdf`: Преобразует HTML в PDF.
- Метод `create_report`: Запускает полный цикл генерации отчёта.
"""
import header
from dataclasses import dataclass, field
from __init__ import gs
import json
from pathlib import Path
from jinja2 import Environment, FileSystemLoader
import pdfkit
from src.utils.jjson import j_loads
from src.utils.file import read_text_file, save_text_file
from src.utils.pdf import save_pdf
# Use the correct import for html2pdf if it exists
try:
    from src.utils.convertors.html import html2pdf
except ImportError:
    html2pdf = None  # Handle case where html2pdf is not available

from src.logger import logger
config = pdfkit.configuration(wkhtmltopdf=str(gs.path.bin / 'wkhtmltopdf' / 'files' / 'bin' / 'wkhtmltopdf.exe'))


@dataclass
class ReportGenerator:
    """!
    Класс для генерации HTML- и PDF-отчётов на основе данных из JSON.
    """

    template_path: str = field(default_factory=lambda: str(gs.path.src / 'suppliers' / 'kazarinov' / 'react' / 'templates' / 'template.html'))
    env: Environment = field(default_factory=lambda: Environment(loader=FileSystemLoader('.')))

    def generate_html(self, data: dict) -> str:
        """!
        Генерирует HTML-контент на основе шаблона и данных.

        Args:
            data (dict): Данные для шаблона.

        Returns:
            str: HTML-контент.
        """
        try:
            template_string = read_text_file(self.template_path)
            template = self.env.from_string(template_string)
            return template.render(**data)
        except Exception as e:
            logger.error(f"Ошибка при генерации HTML: {e}")
            return ""  # Возвращаем пустую строку в случае ошибки

    def create_report(self, data: dict, html_file: Path, pdf_file: Path) -> None:
        """!
        Полный цикл генерации отчёта.
        """
        html_content = self.generate_html(data)

        if not html_content:
            logger.error(f"HTML content is empty. Skipping PDF generation.")
            return
            
        save_text_file(html_content, html_file)

        if html2pdf:
          try:
            html2pdf(html_content, pdf_file)
            logger.info(f"Файлы созданы: {html_file} и {pdf_file}")
          except Exception as e:
            logger.error(f"Ошибка при конвертации HTML в PDF с помощью html2pdf: {e}")
            return

        else:
          logger.warning("html2pdf not available. Using pdfkit fallback (may be slow).")
          try:
              pdfkit.from_string(html_content, str(pdf_file), configuration=config, options={"enable-local-file-access": ""})
              logger.info(f"Файлы созданы: {html_file} и {pdf_file}")
          except Exception as e:
              logger.error(f"Ошибка при генерации PDF с помощью pdfkit: {e}")


if __name__ == "__main__":
    base_path = gs.path.data / 'kazarinov' / 'mexironim' / '202410262326'
    try:
        data = j_loads(base_path / '202410262326_ru.json')
        html_file = base_path / '202410262326_ru.html'
        pdf_file = base_path / '202410262326_ru.pdf'
        r = ReportGenerator()
        r.create_report(data, html_file, pdf_file)
    except FileNotFoundError as e:
        logger.error(f"Ошибка: {e}")
    except Exception as e:
        logger.error(f"Непредвиденная ошибка: {e}")
```

**Изменения и улучшения:**

* **Обработка ошибок:** Добавлена обработка исключений (`try...except`) для `generate_html` и `create_report`. Это предотвращает падение программы при возникновении ошибок (например, если шаблон не найден или файл JSON невалидный). Важно возвращать пустую строку в случае ошибки генерации HTML, чтобы предотвратить попытку сохранить пустой файл.
* **Проверка на пустоту HTML:** Проверка `if not html_content:` позволяет предотвратить попытку генерации PDF из пустого HTML.
* **Обработка отсутствия `html2pdf`:** Добавлена проверка `if html2pdf:`. Если модуль `html2pdf` не найден, используется резервный вариант с `pdfkit`. Это делает код более устойчивым.
* **Логирование:**  Используется `logger` для вывода сообщений об ошибках и предупреждениях.
* **Обработка `FileNotFoundError`:**  Теперь код обрабатывает `FileNotFoundError`, который может возникнуть при попытке открыть не существующий файл.
* **Обработка общих исключений:** Теперь используется `except Exception as e:` для перехвата всех остальных исключений, что делает код более устойчивым к различным ошибкам.

**Как использовать:**

1. Убедитесь, что у вас установлены необходимые библиотеки (Jinja2, pdfkit, и любые другие, используемые в `src.utils`).
2.  Укажите правильный путь к `wkhtmltopdf` в переменной `config`.
3.  Убедитесь, что файлы `template.html` и `202410262326_ru.json` находятся в указанных местах.
4.  Запустите скрипт.


Этот улучшенный код более надежен и устойчив к ошибкам, а также обрабатывает возможные проблемы с файлами и библиотеками.  Он использует более корректный способ обработки ошибок.  Обратите внимание на логирование, которое делает отладку ошибок проще.