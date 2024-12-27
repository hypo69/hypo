# Анализ кода модуля `pricelist_generator.py`

**Качество кода**
**Соответствие требованиям по оформлению кода: 7/10**
-  Плюсы
    - Код в целом структурирован и выполняет поставленную задачу.
    - Используется `dataclass` для `ReportGenerator`, что упрощает создание и управление атрибутами класса.
    - Применяются асинхронные методы, что хорошо для I/O-зависимых операций.
    - Используется `j_loads` для загрузки данных из JSON.
    - Применено логирование ошибок с помощью `logger.error`.
-  Минусы
    -  Не вся документация приведена в reStructuredText (RST) формате.
    -  Некоторые переменные не имеют docstring.
    -  Не везде использованы f-строки.
    -  Избыточное использование `...` как точки остановки в коде.
    -  Не все импорты упорядочены.

**Рекомендации по улучшению**

1.  **Документация:**
    -   Добавить docstring в формате reStructuredText (RST) для класса `ReportGenerator`, функций `generate_html`, `create_report`, `main` и всех переменных.
    -   Улучшить комментарии, переведя их в формат RST.
2.  **Импорты:**
    -   Упорядочить и сгруппировать импорты.
3.  **Обработка ошибок:**
    -   Убрать избыточное использование `...` в блоке `except`.
    -   Улучшить логику обработки ошибок.
4.  **Код:**
    -   Заменить конкатенацию строк на f-строки, где это применимо.
    -   Удалить ненужные комментарии и `#!`.
    -   Унифицировать наименование переменных.
    -   Убрать `service_dict` за пределы функции `create_report`.
    -   Добавить docstring к переменным `MODE`.
5. **Прочее:**
    -   Переименовать все переменные в соответствии с snake_case.

**Оптимизированный код**

```python
# -*- coding: utf-8 -*-
"""
Модуль для генерации HTML и PDF отчётов на основе данных из JSON.
================================================================

Этот модуль предоставляет класс :class:`ReportGenerator` для создания отчётов.
Он использует шаблоны Jinja2 для HTML и PDFKit для конвертации в PDF.

Основные возможности:
- Загрузка данных из JSON файлов.
- Генерация HTML с использованием шаблонов.
- Конвертация HTML в PDF.

Пример использования:
--------------------

.. code-block:: python

    from pathlib import Path
    from src.endpoints.kazarinov.pricelist_generator.pricelist_generator import ReportGenerator
    import asyncio
    
    async def main():
        mexiron = '24_12_01_03_18_24_269'
        lang = 'ru'
        base_path = Path('path/to/your/mexironim') / mexiron
        data = {'products': [{'product_title': 'Продукт 1', 'specification': 'Описание 1', 'image_local_saved_path': 'image1.png'}]}
        html_file = base_path / f'{mexiron}_{lang}.html'
        pdf_file = base_path / f'{mexiron}_{lang}.pdf'
        r = ReportGenerator()
        await r.create_report(data, lang, html_file, pdf_file)
    
    if __name__ == "__main__":
        asyncio.run(main())
"""
import asyncio
from dataclasses import dataclass, field
from pathlib import Path

from jinja2 import Environment, FileSystemLoader
from src import gs
from src.logger.logger import logger
from src.utils.jjson import j_loads
from src.utils.pdf import PDFUtils
from src.utils.image import random_image

#: Режим работы приложения
MODE: str = 'dev'

@dataclass
class ReportGenerator:
    """
    Класс для генерации HTML- и PDF-отчётов на основе данных из JSON.

    :ivar env: Экземпляр окружения Jinja2.
    :vartype env: jinja2.Environment
    """
    env: Environment = field(default_factory=lambda: Environment(loader=FileSystemLoader('.')))

    async def generate_html(self, data: dict, lang: str) -> str:
        """
        Генерирует HTML-контент на основе шаблона и данных.

        :param data: Словарь с данными для шаблона.
        :type data: dict
        :param lang: Язык отчёта ('ru' или 'he').
        :type lang: str
        :return: HTML-контент.
        :rtype: str
        """
        template_name: str = 'template_table_he.html' if lang == 'he' else 'template_table_ru.html'
        template_path: str = str(gs.path.endpoints / 'kazarinov' / 'pricelist_generator' / 'templates' / template_name)
        # Чтение шаблона из файла
        template_string = Path(template_path).read_text(encoding='UTF-8')
        template = self.env.from_string(template_string)
        return template.render(**data)

    async def create_report(self, data: dict, lang: str, html_file: Path, pdf_file: Path) -> bool:
        """
        Полный цикл генерации отчёта.

        :param data: Словарь с данными для отчёта.
        :type data: dict
        :param lang: Язык отчёта ('ru' или 'he').
        :type lang: str
        :param html_file: Путь для сохранения HTML-файла.
        :type html_file: Path
        :param pdf_file: Путь для сохранения PDF-файла.
        :type pdf_file: Path
        :return: True если отчёт успешно создан, False в противном случае.
        :rtype: bool
        """
        # Словарь для сервиса
        service_dict: dict = {
                            "product_title":"Сервис" if lang == 'ru' else "שירות",
                            "specification":Path(gs.path.endpoints / 'kazarinov' / 'pricelist_generator' / 'templates' / f'service_as_product_{lang}.html').read_text(encoding='UTF-8').replace('/n','<br>'),
                            "image_local_saved_path":random_image(gs.path.external_storage / 'kazarinov' / 'converted_images' )
                            }
        
        data['products'].append(service_dict)

        html_content = await self.generate_html(data, lang)
        try:
            # Сохранение HTML контента
            Path(html_file).write_text(data=html_content, encoding='UTF-8')
        except Exception as e:
           logger.error(f"Ошибка при записи HTML файла: {e}")
           return False

        pdf_utils = PDFUtils()
        if not pdf_utils.save_pdf_pdfkit(html_content, pdf_file):
            logger.error("Не удалось скомпилировать PDF")
            return False
        return True

def main(mexiron: str, lang: str) -> bool:
    """
    Основная функция для запуска генерации отчёта.

    :param mexiron: Название директории мехирона.
    :type mexiron: str
    :param lang: Язык отчёта ('ru' или 'he').
    :type lang: str
    :return: True если отчёт успешно создан, False в противном случае.
    :rtype: bool
    """
    base_path: Path = gs.path.external_storage / 'kazarinov' / 'mexironim' / mexiron
    data: dict = j_loads(base_path / f'{lang}.json')
    html_file: Path = base_path / f'{mexiron}_{lang}.html'
    pdf_file: Path = base_path / f'{mexiron}_{lang}.pdf'
    report_generator = ReportGenerator()
    return asyncio.run(report_generator.create_report(data, lang, html_file, pdf_file))


if __name__ == "__main__":
    mexiron: str = '24_12_01_03_18_24_269'
    lang: str = 'ru'
    main(mexiron, lang)

```