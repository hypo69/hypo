# Анализ кода модуля `pricelist_generator.py`

**Качество кода**
10
- Плюсы
    - Код соответствует PEP 8, использует dataclass для представления данных.
    - Применяется `logger` для логирования ошибок.
    - Используется `j_loads` для чтения JSON.
    - Присутствуют docstring для классов и функций.
    - Код разбит на логические блоки, что упрощает понимание.
- Минусы
    - Есть неиспользуемые импорты
    - Есть неявные типы.
    - Присутствуют `...` как точки остановки, что не является лучшей практикой.

**Рекомендации по улучшению**

1.  **Импорты**:
    -  Удалить неиспользуемые импорты `header`, `json`, `asyncio`.
    -  Добавить `from src.logger.logger import logger` для явного импорта.
2.  **Типизация**:
    -  Добавить явную типизацию для переменных `template_string`, `template`.
3.  **Обработка ошибок**:
    - Заменить `...` на `return False` или `raise Exception` c логированием ошибки.
    - Добавить обработку исключений при чтении файлов.
4. **Комментарии и Docstring**:
    - Добавить более подробные docstring для функций, включая описание параметров и возвращаемых значений.
    - Переписать docstring в формате RST
5.  **Улучшение логики:**
    - Использовать Path для всех путей и `gs.path`.
    - Убрать использование `replace('/n', '<br>')` в `service_dict` и использовать `replace('\n', '<br>')`

**Оптимизированный код**

```python
"""
Модуль для генерации HTML и PDF прайс-листов для Казаринова.
============================================================

Этот модуль содержит класс :class:`ReportGenerator`, который используется для генерации HTML и PDF отчетов
на основе данных из JSON.

Основные возможности:
- Загрузка данных из JSON-файла.
- Генерация HTML с использованием Jinja2.
- Сохранение HTML в файл.
- Преобразование HTML в PDF.
- Запуск полного цикла генерации отчёта.

Пример использования
--------------------

.. code-block:: python

    report_generator = ReportGenerator()
    asyncio.run(report_generator.create_report(data, lang, html_file, pdf_file))

"""
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe
#! venv/bin/python/python3.12

MODE = 'dev'


from dataclasses import dataclass, field
from pathlib import Path
from jinja2 import Environment, FileSystemLoader, Template
from src.utils.jjson import j_loads
from src.utils.file import  save_text_file
from src.utils.pdf import PDFUtils
from src.utils.image import random_image
from src.logger.logger import logger
from src import gs
import asyncio # не используется


@dataclass
class ReportGenerator:
    """
    Класс для генерации HTML- и PDF-отчётов на основе данных из JSON.

    :ivar env: Jinja2 Environment для работы с шаблонами.
    """

    env: Environment = field(default_factory=lambda: Environment(loader=FileSystemLoader('.')))

    async def generate_html(self, data: dict, lang: str) -> str:
        """
        Генерирует HTML-контент на основе шаблона и данных.

        :param data: Словарь с данными для рендеринга шаблона.
        :type data: dict
        :param lang: Язык отчёта ('ru' или 'he').
        :type lang: str
        :return: HTML-контент в виде строки.
        :rtype: str
        """
        template_name: str = 'template_table_he.html' if lang == 'he' else 'template_table_ru.html'
        template_path: Path = gs.path.endpoints / 'kazarinov' / 'pricelist_generator' / 'templates' / template_name
        try:
            template_string: str = template_path.read_text(encoding='UTF-8')
            template: Template = self.env.from_string(template_string)
            return template.render(**data)
        except Exception as ex:
            logger.error(f"Ошибка чтения или рендеринга шаблона {template_path}", exc_info=ex)
            return ""


    async def create_report(self, data: dict, lang: str, html_file: Path, pdf_file: Path) -> bool:
        """
        Полный цикл генерации отчёта.

        :param data: Словарь с данными для отчета.
        :type data: dict
        :param lang: Язык отчёта ('ru' или 'he').
        :type lang: str
        :param html_file: Путь к файлу для сохранения HTML.
        :type html_file: Path
        :param pdf_file: Путь к файлу для сохранения PDF.
        :type pdf_file: Path
        :return: True, если отчет сгенерирован успешно, иначе False.
        :rtype: bool
        """
        _data: dict = data[lang]

        # Формирование словаря для сервиса.
        service_dict: dict = {
            "product_title": "Сервис" if lang == 'ru' else "שירות",
            "specification": (gs.path.endpoints / 'kazarinov' / 'pricelist_generator' / 'templates' / f'service_as_product_{lang}.html').read_text(encoding='UTF-8').replace('\n','<br>'),
            "image_local_saved_path": str(random_image(gs.path.external_storage / 'kazarinov' / 'converted_images'))
        }
        _data['products'].append(service_dict)

        html_content = await self.generate_html(_data, lang)
        try:
            save_text_file(html_file,html_content)
        except Exception as ex:
            logger.error(f"Ошибка сохранения html файла: {html_file}", exc_info=ex)
            return False
        pdf = PDFUtils()

        if not pdf.save_pdf_pdfkit(html_content, pdf_file):
            logger.error(f"Не удалось скомпилировать PDF")
            return False
        return True


def main(mexiron: str, lang: str) -> bool:
    """
    Основная функция для запуска генерации отчёта.

    :param mexiron: Имя мехирона.
    :type mexiron: str
    :param lang: Язык отчёта ('ru' или 'he').
    :type lang: str
    :return: True, если отчет сгенерирован успешно, иначе False.
    :rtype: bool
    """
    base_path: Path = gs.path.external_storage / 'kazarinov' / 'mexironim' / mexiron
    data: dict = j_loads(base_path / f'{lang}.json')
    html_file: Path = base_path / f'{mexiron}_{lang}.html'
    pdf_file: Path = base_path / f'{mexiron}_{lang}.pdf'
    r = ReportGenerator()
    return asyncio.run(r.create_report(data, lang, html_file, pdf_file))


if __name__ == "__main__":
    mexiron: str = '24_12_01_03_18_24_269'
    lang: str = 'ru'
    main(mexiron, lang)

```