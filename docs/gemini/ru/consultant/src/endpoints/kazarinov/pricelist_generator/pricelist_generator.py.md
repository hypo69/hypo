# Анализ кода модуля `pricelist_generator.py`

**Качество кода: 7/10**

-   **Плюсы:**
    *   Код структурирован в класс `ReportGenerator`, что способствует  организации.
    *   Используются `dataclass` для создания класса `ReportGenerator`.
    *   Применяются асинхронные операции для генерации отчетов, что может улучшить производительность.
    *   Используется `j_loads` для чтения JSON-файлов.
    *   Присутствует логирование ошибок.
    *   Используется `Pathlib` для работы с файлами.
    *   Используется `jinja2` для рендеринга HTML.

-   **Минусы:**
    *   Отсутствует docstring для модуля.
    *   Не все функции имеют docstring, либо они недостаточно подробные.
    *   Не все импорты используются.
    *   Использование `asyncio.run` в `main` функции, не лучшее решение.
    *   Избыточное использование `...` как точки останова.
    *   Использование print для вывода, лучше использовать logger
    *   Комментарии не соответствуют reStructuredText (RST) стандарту.
    *   Не производится обработка исключений во всех необходимых местах.
    *   Не хватает проверок входных данных.

**Рекомендации по улучшению:**

1.  **Добавить docstring для модуля**:
    *   Описать назначение модуля, основные классы и функции.

2.  **Улучшить docstring для функций и методов**:
    *   Использовать формат reStructuredText (RST).
    *   Добавить описание параметров и возвращаемых значений.

3.  **Удалить неиспользуемые импорты**:
    *   Удалить `header` из импортов.

4.  **Переработать функцию `main`**:
    *   Убрать `asyncio.run`.
    *   Вынести вызов `create_report` из `asyncio.run`.
    *   Сделать функцию `main` синхронной.
    *   Обработать исключения при вызове `create_report` через `try-except` и логирование.

5.  **Удалить избыточное использование `...`**:
    *   Использовать `logger.error` для логирования ошибок.

6.  **Добавить проверок входных данных**:
    *   Проверять наличие файлов, корректность JSON.

7.  **Заменить print на logger**:
    *   Использовать `logger` для логирования вместо `print`.

8.  **Улучшить обработку исключений**:
    *   Использовать `try-except` для обработки исключений в нужных местах, а не только в `save_pdf_pdfkit`.
    *   Логировать исключения с помощью `logger.error`.

9.  **Форматирование кода**:
    *   Привести код в соответствие pep8

10. **Использование более конкретных ошибок**:
    *   Поднимать более конкретные ошибки, например `FileNotFoundError`

**Оптимизированный код:**

```python
"""
Модуль для генерации HTML и PDF отчетов для мехиронов Казаринова.
=================================================================

Этот модуль предоставляет класс `ReportGenerator`, который используется
для генерации HTML и PDF отчетов на основе данных из JSON файлов.

Основные возможности:

- Загрузка данных из JSON.
- Генерация HTML с использованием Jinja2.
- Преобразование HTML в PDF с помощью pdfkit.
- Создание полного отчета.

Пример использования
--------------------

.. code-block:: python

    from pathlib import Path
    from src.endpoints.kazarinov.pricelist_generator.pricelist_generator import ReportGenerator
    from src import gs
    import asyncio
    
    async def main():
        mexiron = '24_12_01_03_18_24_269'
        lang = 'ru'
        base_path = gs.path.external_storage / 'kazarinov' / 'mexironim' / mexiron
        data_file = base_path / f'{lang}.json'
        html_file = base_path / f'{mexiron}_{lang}.html'
        pdf_file = base_path / f'{mexiron}_{lang}.pdf'
    
        report_generator = ReportGenerator()
    
        if not await report_generator.create_report(data_file, lang, html_file, pdf_file):
            print('Report creation failed')
    
    if __name__ == '__main__':
        asyncio.run(main())
"""
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe
#! venv/bin/python/python3.12

MODE = 'dev'


import asyncio
from dataclasses import dataclass, field
from pathlib import Path
from jinja2 import Environment, FileSystemLoader
from src.utils.jjson import j_loads
from src.utils.pdf import PDFUtils
from src.utils.image import random_image
from src.logger.logger import logger


@dataclass
class ReportGenerator:
    """
    Класс для генерации HTML и PDF отчетов на основе данных из JSON.

    :param env: Jinja2 environment.
    """
    env: Environment = field(default_factory=lambda: Environment(loader=FileSystemLoader('.')))

    async def generate_html(self, data: dict, lang: str) -> str:
        """
        Генерирует HTML контент на основе шаблона и данных.

        :param data: Словарь с данными для рендеринга.
        :param lang: Язык отчета ('ru' или 'he').
        :return: HTML контент в виде строки.
        """
        template_name: str = 'template_table_he.html' if lang == 'he' else 'template_table_ru.html'
        template_path: Path = Path(
            Path(__file__).parent / 'templates' / template_name
        )

        try:
            template_string = template_path.read_text(encoding='UTF-8')
            template = self.env.from_string(template_string)
            return template.render(**data)
        except FileNotFoundError as e:
            logger.error(f'Файл шаблона не найден: {template_path}', exc_info=True)
            raise
        except Exception as e:
            logger.error(f'Ошибка при генерации HTML: {e}', exc_info=True)
            raise

    async def create_report(self, data_file: Path, lang: str, html_file: Path, pdf_file: Path) -> bool:
        """
        Создает полный отчет: генерирует HTML, сохраняет его и преобразует в PDF.

        :param data_file: Путь к JSON файлу с данными.
        :param lang: Язык отчета ('ru' или 'he').
        :param html_file: Путь для сохранения HTML файла.
        :param pdf_file: Путь для сохранения PDF файла.
        :return: True, если отчет успешно создан, False - в обратном случае.
        """
        try:
            data: dict = j_loads(data_file)
            _data: dict = data[lang]

            service_template_path = Path(
                Path(__file__).parent / 'templates' / f'service_as_product_{lang}.html'
            )
            service_dict: dict = {
                'product_title': 'Сервис' if lang == 'ru' else 'שירות',
                'specification': service_template_path.read_text(encoding='UTF-8').replace('\n', '<br>'),
                'image_local_saved_path': str(random_image(Path(
                    Path(__file__).parent / '..' / '..' / '..' / 'external_storage' / 'kazarinov' / 'converted_images'))),
            }
            _data['products'].append(service_dict)

            html_content: str = await self.generate_html(_data, lang)
            html_file.write_text(data=html_content, encoding='UTF-8')

            pdf = PDFUtils()
            if not pdf.save_pdf_pdfkit(html_content, pdf_file):
                logger.error(f'Не удалось скомпилировать PDF')
                return False
            return True

        except FileNotFoundError as e:
            logger.error(f'Файл не найден: {data_file}', exc_info=True)
            return False
        except Exception as e:
            logger.error(f'Произошла ошибка при создании отчета: {e}', exc_info=True)
            return False


async def main():
    """
    Основная функция для запуска генерации отчета.
    """
    mexiron: str = '24_12_01_03_18_24_269'
    lang: str = 'ru'
    base_path: Path = Path(__file__).parent / '..' / '..' / '..' / 'external_storage' / 'kazarinov' / 'mexironim' / mexiron
    data_file: Path = base_path / f'{lang}.json'
    html_file: Path = base_path / f'{mexiron}_{lang}.html'
    pdf_file: Path = base_path / f'{mexiron}_{lang}.pdf'
    
    r = ReportGenerator()
    if not await r.create_report(data_file, lang, html_file, pdf_file):
         logger.error("Не удалось сгенерировать отчет")


if __name__ == "__main__":
     asyncio.run(main())
```