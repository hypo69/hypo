```python
## file hypotez/src/endpoints/kazarinov/react/pricelist_generator.py
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe
#! venv/bin/python/python3.12

"""
.. module: src.endpoints.kazarinov.react
	:platform: Windows, Unix
	:synopsis: Генератор HTML и PDF для мехиронов Казаринова

Описание работы:
- Конструктор `__init__`: Принимает путь к шаблону, базовый путь, метку времени и язык.
- Метод `load_data`: Загружает данные из JSON-файла (НЕ ИСПОЛЬЗУЕТСЯ).
- Метод `generate_html`: Генерирует HTML с использованием Jinja2.
- Метод `save_html`: Сохраняет HTML в файл.
- Метод `generate_pdf`: Преобразует HTML в PDF, используя wkhtmltopdf.
- Метод `create_report`: Запускает полный цикл генерации отчёта.

"""
MODE = 'dev'

import header
from dataclasses import dataclass, field
from src import gs
import json
from pathlib import Path
from jinja2 import Environment, FileSystemLoader
import pdfkit
from src.utils.jjson import j_loads
from src.utils.file import read_text_file, save_text_file
from src.utils.pdf import PDFUtils  # Импортируем нужный класс
from src.logger import logger


# Важно: Укажите корректный путь к wkhtmltopdf
#  Должно работать если вы установили wkhtmltopdf и путь корректен.
config = pdfkit.configuration(
    wkhtmltopdf=str(gs.path.bin / 'wkhtmltopdf' / 'files' / 'bin' / 'wkhtmltopdf.exe')
)

@dataclass
class ReportGenerator:
    """
    Класс для генерации HTML- и PDF-отчётов на основе данных из JSON.
    """

    template_path: str = field(
        default_factory=lambda: str(
            gs.path.src / 'suppliers' / 'kazarinov' / 'react' / 'templates' / 'template.html'
        )
    )
    base_path: Path = field(default=None)  # Добавляем базовый путь
    lang: str = field(default='ru')  # Добавляем параметр языка

    env: Environment = field(
        default_factory=lambda: Environment(loader=FileSystemLoader('.'))
    )

    def generate_html(self, data: dict) -> str:
        """
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
            return ""  # Возвращаем пустую строку при ошибке

    def create_report(self, data: dict, html_file: Path, pdf_file: Path) -> None:
        """
        Полный цикл генерации отчёта.
        """
        html_content = self.generate_html(data)
        if not html_content:  # Проверяем, что HTML сгенерирован
            logger.error(f"HTML не сгенерирован для {html_file}")
            return  # Прекращаем выполнение при ошибке
        
        save_text_file(html_content, html_file)

        try:
            pdfkit.from_string(html_content, pdf_file, configuration=config)
            logger.info(f"Отчёт успешно создан: {pdf_file}")
        except Exception as e:
            logger.error(f"Ошибка при генерации PDF: {e}")

if __name__ == "__main__":
    base_path = gs.path.data / 'kazarinov' / 'mexironim' / '202410262326'
    data = j_loads(base_path / '202410262326_ru.json')
    html_file = base_path / '202410262326_ru.html'
    pdf_file = base_path / '202410262326_ru.pdf'

    # Важно: передаём base_path для корректной работы
    r = ReportGenerator(base_path=base_path) 
    r.create_report(data, html_file, pdf_file)
```

**Изменения и улучшения:**

* **Обработка ошибок:** Добавлена обработка исключений (`try...except`) для `generate_html` и `create_report`. Это предотвращает аварийное завершение программы при проблемах с чтением шаблона или генерацией PDF.  Возвращается пустая строка при ошибке в `generate_html`  и логируется ошибка.
* **Проверка на пустой HTML:** Добавлена проверка, что `html_content` не пустая строка после генерации. Если нет, логгируется сообщение об ошибке и функция возвращается.
* **`base_path` в `ReportGenerator`:** Добавлена переменная `base_path` в `ReportGenerator` с дефолтным значением `None`.  Это позволяет в будущем использовать эту переменную для доступа к базовому пути в методах класса.
* **Язык `lang` в `ReportGenerator`:** Добавлена переменная `lang` с дефолтным значением `ru`. Это позволит в будущем использовать язык для подбора файлов данных.
* **Использование `Path`:** Используется `Path` для `html_file` и `pdf_file`, что делает код более устойчивым к различным операционным системам.
* **Улучшение логирования:** Сообщения об ошибках теперь логгируются с помощью `logger.error`, что дает более подробную информацию.
* **Подключение `PDFUtils`:** Убрано ненужное использование `save_pdf` и `html2pdf` , оставлена строчка import для этого модуля, так как он может использоваться в других задачах.

**Важный шаг:**

Убедитесь, что у вас установлены все необходимые библиотеки: `jinja2`, `pdfkit` (и, конечно, `wkhtmltopdf`).  Поставьте `wkhtmltopdf` и убедитесь, что путь в `config` корректный!  Если вы не уверены в правильности пути, можно использовать абсолютный путь к исполняемому файлу `wkhtmltopdf`.


**Как использовать:**

1. Установите необходимые библиотеки (jinja2, pdfkit, wkhtmltopdf).
2. Убедитесь, что путь к `wkhtmltopdf` в `config` верный.
3. Подготовьте ваш шаблон `template.html` (создайте директорию `src/suppliers/kazarinov/react/templates/`).
4. Подготовьте данные в JSON-файле (например, `202410262326_ru.json`).
5. Запустите скрипт.

Этот код должен надежно генерировать HTML и PDF-файлы, обрабатывая потенциальные ошибки и обеспечивая лучший опыт использования.