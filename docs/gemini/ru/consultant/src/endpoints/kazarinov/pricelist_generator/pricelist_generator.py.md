# Анализ кода модуля `pricelist_generator.py`

**Качество кода:**

8/10

*   **Плюсы:**
    *   Код имеет четкую структуру с использованием классов и функций, что облегчает понимание и поддержку.
    *   Используются `dataclass`, `Path`, `asyncio`, `jinja2`, `pdfkit` и другие полезные библиотеки.
    *   Применяется `j_loads` для чтения JSON.
    *   Имеется базовая документация в виде docstring для класса `ReportGenerator`.
    *   Есть логирование ошибок, хотя и не везде.

*   **Минусы:**
    *   Неполная документация функций и переменных.
    *   Много `...` в коде, что указывает на необходимость их доработки.
    *   Отсутствует явная обработка ошибок при чтении и записи файлов.
    *   Не все импорты соответствуют стандарту, например `import header`.
    *   Не всегда используется `logger.error` для обработки исключений.
    *   Некоторые переменные имеют не совсем ясные имена.
    *   Дублирование кода, например при загрузке шаблона.
    *   Не используются константы для путей и имен файлов.

**Рекомендации по улучшению:**

1.  **Документация:**
    *   Добавить подробные docstring для всех функций и методов, включая описание аргументов, возвращаемых значений и возможных исключений.
    *   Добавить описание переменных, используемых в коде.

2.  **Импорты:**
    *   Исправить импорт `import header`.
    *   Явно импортировать `logger` из `src.logger.logger`.
    *   Удалить неиспользуемые импорты.
3.  **Обработка ошибок:**
    *   Использовать `logger.error` для логирования ошибок вместо `...` и `try-except` там, где это возможно.
    *   Добавить проверку существования файлов перед их чтением.
4.  **Рефакторинг:**
    *   Убрать дублирование кода при загрузке HTML-шаблона в методе `generate_html`.
    *   Использовать константы для путей и имен файлов.
    *   Перенести чтение текста файла шаблона в отдельную функцию.
    *   Улучшить именование переменных.
    *   Переработать метод `create_report`, вынеся отдельные блоки в функции.

5. **Улучшения**
    * Использовать `Path.read_text` вместо `Path().read_text`.
    * Добавить проверки на корректность данных, которые читаются из JSON.
    * Добавить асинхронности в места, где это возможно (чтение и запись файлов).
    * Использовать более консистентные наименования переменных.

**Оптимизированный код:**

```python
# -*- coding: utf-8 -*-

"""
Модуль для генерации HTML и PDF отчётов на основе данных из JSON.
==================================================================

Этот модуль содержит класс :class:`ReportGenerator`, который используется для генерации отчётов в формате HTML и PDF,
основанных на данных, загруженных из JSON файлов.

Основной функционал включает:

- Загрузку данных из JSON-файла.
- Генерацию HTML-контента с использованием Jinja2.
- Сохранение HTML-файла.
- Преобразование HTML в PDF.
- Запуск полного цикла генерации отчёта.

Пример использования
--------------------

Пример использования класса `ReportGenerator`:

.. code-block:: python

    report_generator = ReportGenerator()
    data = {'products': [{'product_title': 'Product 1', 'specification': 'Spec 1', 'image_local_saved_path': 'path/to/image.jpg'}]}
    lang = 'ru'
    html_file = 'report.html'
    pdf_file = 'report.pdf'
    asyncio.run(report_generator.create_report(data, lang, html_file, pdf_file))

"""

import asyncio
from dataclasses import dataclass, field
from pathlib import Path
from jinja2 import Environment, FileSystemLoader
from src.utils.jjson import j_loads
from src.utils.file import save_text_file
from src.utils.pdf import PDFUtils
from src.utils.image import random_image
from src.logger.logger import logger
from src.config import gs


# Константы для путей к шаблонам
TEMPLATE_DIR = gs.path.endpoints / 'kazarinov' / 'pricelist_generator' / 'templates'
SERVICE_TEMPLATE_DIR = gs.path.endpoints / 'kazarinov' / 'pricelist_generator' / 'templates'
CONVERTED_IMAGES_DIR = gs.path.external_storage / 'kazarinov' / 'converted_images'


@dataclass
class ReportGenerator:
    """
    Класс для генерации HTML- и PDF-отчётов на основе данных из JSON.
    """
    env: Environment = field(default_factory=lambda: Environment(loader=FileSystemLoader('.')))

    async def _load_template(self, template_name: str) -> str:
        """
        Загружает шаблон из файла.

        Args:
            template_name (str): Имя файла шаблона.

        Returns:
            str: Содержимое шаблона.

        Raises:
            FileNotFoundError: Если файл шаблона не найден.
            Exception: При других ошибках чтения файла.
        """
        template_path = TEMPLATE_DIR / template_name
        try:
             # Чтение шаблона из файла
            return (template_path).read_text(encoding='UTF-8')
        except FileNotFoundError as e:
            logger.error(f'Файл шаблона не найден: {template_path}', exc_info=True)
            raise
        except Exception as e:
             # Логирование ошибки чтения файла
            logger.error(f'Ошибка чтения файла шаблона: {template_path}', exc_info=True)
            raise

    async def generate_html(self, data: dict, lang: str) -> str:
        """
        Генерирует HTML-контент на основе шаблона и данных.

        Args:
            data (dict): Данные для заполнения шаблона.
            lang (str): Язык отчёта ('ru' или 'he').

        Returns:
            str: HTML-контент.
        """
        template_name = 'template_table_he.html' if lang == 'he' else 'template_table_ru.html'
        try:
            # Загрузка шаблона
            template_string = await self._load_template(template_name)
            template = self.env.from_string(template_string)
            # Рендеринг шаблона с данными
            return template.render(**data)
        except Exception as e:
            # Логирование ошибки генерации HTML
             logger.error(f'Ошибка при генерации HTML: {e}', exc_info=True)
             return ''



    async def _create_service_data(self, lang: str) -> dict:
            """
            Создает словарь с данными для сервиса.

            Args:
                lang (str): Язык отчёта ('ru' или 'he').

            Returns:
                dict: Словарь с данными о сервисе.
            """
            service_template_name = f'service_as_product_{lang}.html'
            try:
                # Загрузка шаблона сервиса
                service_specification = await self._load_template(service_template_name)
                # Формирование словаря с данными
                return {
                "product_title": "Сервис" if lang == 'ru' else "שירות",
                "specification": service_specification.replace('\n', '<br>'),
                "image_local_saved_path": random_image(CONVERTED_IMAGES_DIR),
            }
            except Exception as e:
                logger.error(f'Ошибка при создании данных сервиса: {e}', exc_info=True)
                return {}



    async def create_report(self, data: dict, lang: str, html_file: str | Path, pdf_file: str | Path) -> bool:
        """
        Полный цикл генерации отчёта: добавляет данные о сервисе, генерирует HTML и PDF.

        Args:
            data (dict): Данные для отчёта.
            lang (str): Язык отчёта ('ru' или 'he').
            html_file (str | Path): Путь для сохранения HTML-файла.
            pdf_file (str | Path): Путь для сохранения PDF-файла.

        Returns:
            bool: True, если отчёт успешно создан, False в противном случае.
        """
        try:
            # Создание данных о сервисе
            service_data = await self._create_service_data(lang)
            # Добавление данных о сервисе к основным данным
            data['products'].append(service_data)
            # Генерация HTML
            html_content = await self.generate_html(data, lang)
            # Сохранение HTML файла
            await save_text_file(html_file, html_content)

            # Инициализация PDF утилиты
            pdf = PDFUtils()

            # Сохранение PDF файла
            if not pdf.save_pdf_pdfkit(html_content, pdf_file):
                # Логирование ошибки создания PDF
                logger.error(f"Не удалось скомпилировать PDF файл: {pdf_file}")
                return False
            return True
        except Exception as e:
            # Логирование общей ошибки при создании отчёта
             logger.error(f'Ошибка при создании отчёта: {e}', exc_info=True)
             return False


def main(mexiron: str, lang: str) -> bool:
    """
    Основная функция для запуска процесса генерации отчёта.

    Args:
        mexiron (str): Имя мехирона.
        lang (str): Язык отчёта ('ru' или 'he').

    Returns:
        bool: True если отчет был создан, иначе False
    """
    base_path: Path = gs.path.external_storage / 'kazarinov' / 'mexironim' / mexiron
    # Проверка существования файла
    json_file = base_path / f'{lang}.json'
    if not json_file.exists():
        logger.error(f'Файл JSON не найден: {json_file}')
        return False
    try:
        # Загрузка данных из JSON
        data: dict = j_loads(json_file)
    except Exception as e:
         logger.error(f'Ошибка при загрузке JSON: {json_file}', exc_info=True)
         return False

    html_file: Path = base_path / f'{mexiron}_{lang}.html'
    pdf_file: Path = base_path / f'{mexiron}_{lang}.pdf'

    report_generator = ReportGenerator()
    return asyncio.run(report_generator.create_report(data, lang, html_file, pdf_file))

if __name__ == "__main__":
    mexiron: str = '24_12_01_03_18_24_269'
    lang: str = 'ru'
    main(mexiron, lang)
```