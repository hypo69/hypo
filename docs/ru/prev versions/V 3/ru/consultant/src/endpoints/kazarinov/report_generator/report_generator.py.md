## Анализ кода модуля `report_generator`

### Качество кода:

- **Соответствие стандартам**: 6/10
- **Плюсы**:
  - Код достаточно хорошо структурирован, с использованием классов и функций для разделения логики.
  - Присутствуют docstring для большинства функций и классов, что облегчает понимание их назначения.
  - Используются типы аннотаций, что улучшает читаемость и помогает в отладке.
- **Минусы**:
  - Не везде используется логирование ошибок с `exc_info=True` для полного traceback.
  - Некоторые комментарии неинформативны (например, "Определение, какие форматы данных требуется вернуть").
  - Есть дублирование кода, например, при создании PDF и DOCX отчетов.
  - Не все переменные аннотированы типами.
  - Используются устаревшие конструкции, такие как `from src.utils.pdf import PDFUtils` внутри функции.
  - В некоторых местах не соблюдены стандарты PEP8 (пробелы вокруг операторов).

### Рекомендации по улучшению:

1. **Документация и комментарии**:
   - Улучшить docstring для класса `ReportGenerator`, добавив описание каждого атрибута класса.
   - Перефразировать комментарий в `__init__` для большей ясности.
   - Добавить примеры использования в docstring для основных методов, таких как `create_html_report_async` и `create_pdf_report_async`.
   - Уточнить комментарии, чтобы они более точно описывали назначение кода.

2. **Обработка ошибок и логирование**:
   - Добавить `exc_info=True` при логировании ошибок для получения полного traceback, например:
     ```python
     except Exception as ex:
         logger.error(f"Не удалось сгенерирпвать HTML файл {html_path}", ex, exc_info=True)
     ```
   - Логировать все исключения, чтобы упростить отладку.

3. **Структура кода и рефакторинг**:
   - Избегать дублирования кода. Например, вызов `create_pdf_report_async` для создания DOCX файла выглядит ошибочным. Возможно, следует вызывать `create_docx_report_async`.
   - Вынести инициализацию `PDFUtils` из функции `create_pdf_report_async` на уровень класса или модуля.
   - Убедиться, что все переменные аннотированы типами.
   - Использовать `j_loads` для загрузки JSON данных в функции `main`.

4. **Форматирование и стиль кода**:
   - Соблюдать PEP8: добавить пробелы вокруг операторов присваивания и других операторов.
   - Использовать константы для строковых литералов, таких как `"product_id"`, `"product_name"` и т.д.

5. **Импорты**:
   - Всегда импортируйте `logger` только из `src.logger`:
     ```python
     from src.logger.logger import logger
     ```

### Оптимизированный код:

```python
## \file /src/endpoints/kazarinov/react/report_generator.py
# -*- coding: utf-8 -*-

#! .pyenv/bin/python3

"""
Модуль для генерации HTML и PDF отчетов для мехиронов Казаринова.
==================================================================

Модуль содержит класс :class:`ReportGenerator`, который используется для генерации отчетов в форматах HTML, PDF и DOCX
на основе данных из JSON.

Пример использования:
----------------------
>>> report_generator = ReportGenerator()
>>> asyncio.run(report_generator.create_reports_async(bot, chat_id, data, lang, mexiron_name))
"""

import asyncio
import telebot
from pathlib import Path
from typing import Optional
from jinja2 import Environment, FileSystemLoader

from src import gs
from src.utils.jjson import j_loads
from src.utils.file import read_text_file, save_text_file
from src.utils.convertors.html2pdf import html2pdf
from src.utils.convertors.html2docx import html_to_docx
from src.utils.image import random_image
from src.logger.logger import logger
from src.utils.pdf import PDFUtils

# Константы для имен файлов и путей
ENDPOINT: str = 'kazarinov'
TEMPLATE_TABLE_HE: str = 'template_table_he.html'
TEMPLATE_TABLE_RU: str = 'template_table_ru.html'
SERVICE_AS_PRODUCT_RU: str = 'service_as_product_ru.html'
SERVICE_AS_PRODUCT_HE: str = 'service_as_product_he.html'

class ReportGenerator:
    """
    Класс для генерации HTML- и PDF-отчётов на основе данных из JSON.

    Attributes:
        if_need_html (bool): Флаг, указывающий, нужно ли генерировать HTML-отчет.
        if_need_pdf (bool): Флаг, указывающий, нужно ли генерировать PDF-отчет.
        if_need_docx (bool): Флаг, указывающий, нужно ли генерировать DOCX-отчет.
        storage_path (Path): Путь к директории хранения отчетов.
        html_path (Path | str): Путь к HTML-файлу.
        pdf_path (Path | str): Путь к PDF-файлу.
        docs_path (Path | str): Путь к DOCX-файлу.
        html_content (str): HTML-контент отчета.
        data (dict): Данные для генерации отчета.
        lang (str): Язык отчета.
        mexiron_name (str): Название мехирона.
        env (Environment): Окружение Jinja2 для работы с шаблонами.
    """
    if_need_html: bool
    if_need_pdf: bool
    if_need_docx: bool
    storage_path: Path = Path(gs.path.external_storage, ENDPOINT)
    html_path: Path | str
    pdf_path: Path | str
    docs_path: Path | str
    html_content: str
    data: dict
    lang: str
    mexiron_name: str
    env: Environment = Environment(loader=FileSystemLoader('.'))
    pdf_utils: PDFUtils = PDFUtils()

    def __init__(self,
                 if_need_pdf: Optional[bool] = True,
                 if_need_docx: Optional[bool] = True,
                 ):
        """
        Инициализация ReportGenerator.

        Args:
            if_need_pdf (Optional[bool]): Флаг, указывающий, нужно ли генерировать PDF-отчет. Defaults to True.
            if_need_docx (Optional[bool]): Флаг, указывающий, нужно ли генерировать DOCX-отчет. Defaults to True.
        """
        # Указываем, какие форматы данных требуется вернуть
        self.if_need_pdf = if_need_pdf
        self.if_need_docx = if_need_docx

    async def create_reports_async(self,
                                 bot: telebot.TeleBot,
                                 chat_id: int,
                                 data: dict,
                                 lang: str,
                                 mexiron_name: str,
                                 ) -> tuple:
        """Create ALL types: HTML, PDF, DOCX"""
        ...
        self.mexiron_name = mexiron_name
        export_path: Path = self.storage_path / 'mexironim' / self.mexiron_name

        self.html_path: Path = export_path / f'{self.mexiron_name}_{lang}.html'
        self.pdf_path: Path = export_path / f'{self.mexiron_name}_{lang}.pdf'
        self.docx_path: Path = export_path / f'{self.mexiron_name}_{lang}.docx'
        self.bot: telebot.TeleBot = bot
        self.chat_id: int = chat_id

        self.html_content: str = await self.create_html_report_async(data, lang, self.html_path)

        if not self.html_content:
            return False

        if self.if_need_pdf:
            if not await self.create_pdf_report_async(self.html_content, lang, self.pdf_path):
                logger.error(f"Не удалось создать PDF-отчет для {self.pdf_path}", exc_info=True)
                return False

        if self.if_need_docx:
            if not await self.create_docx_report_async(self.html_path, self.docx_path):
                logger.error(f"Не удалось создать DOCX-отчет для {self.docx_path}", exc_info=True)
                return False

    def service_apendix(self, lang: str) -> dict:
        """
        Создает и возвращает словарь с информацией о сервисе.

        Args:
            lang (str): Язык, на котором должна быть информация о сервисе.

        Returns:
            dict: Словарь с информацией о сервисе.
        """
        return {
            'product_id': '00000',
            'product_name': 'Сервис' if lang == 'ru' else 'שירות',
            'specification': Path(gs.path.root / 'src' / 'endpoints' / ENDPOINT / 'report_generator' / 'templates' / f'service_as_product_{lang}.html').read_text(encoding='UTF-8').replace('/n', '<br>'),
            'image_local_saved_path': random_image(self.storage_path / 'converted_images')
        }
        ...

    async def create_html_report_async(self, data: dict, lang: str, html_path: Optional[str | Path]) -> str | None:
        """
        Генерирует HTML-контент на основе шаблона и данных.

        Args:
            data (dict): Данные для заполнения шаблона.
            lang (str): Язык отчёта.
            html_path (Optional[str | Path]): Путь для сохранения HTML-файла.

        Returns:
            str | None: HTML-контент, если успешно сгенерирован, иначе None.

        Example:
            >>> report_generator = ReportGenerator()
            >>> html_content = await report_generator.create_html_report_async(data, 'ru', 'report.html')
            >>> print(html_content[:100])
            <!DOCTYPE html>
            <html>
            <head>
                <meta charset="UTF-8">
                <title>Отчет</title>
            </head>
        """
        self.html_path: Path = Path(html_path) if html_path and isinstance(html_path, str) else Path(html_path) if html_path else self.html_path

        try:
            service_apendix: dict = self.service_apendix(lang)
            data['products'].append(service_apendix)
            template_name: str = TEMPLATE_TABLE_HE if lang == 'he' else TEMPLATE_TABLE_RU
            template_path: str = str(gs.path.endpoints / ENDPOINT / 'report_generator' / 'templates' / template_name)
            template_string: str = Path(template_path).read_text(encoding='UTF-8')
            template = self.env.from_string(template_string)
            self.html_content: str = template.render(**data)

            try:
                Path(self.html_path).write_text(data=self.html_content, encoding='UTF-8')
            except Exception as ex:
                logger.error(f"Не удалось сохранить HTML файл {self.html_path}", ex, exc_info=True)
                return self.html_content

            logger.info(f"HTML файл успешно сохранен в {self.html_path}")
            return self.html_content

        except Exception as ex:
            logger.error(f"Не удалось сгенерировать HTML файл {self.html_path}", ex, exc_info=True)
            return None

    async def create_pdf_report_async(self,
                                    data: str,
                                    lang: str,
                                    pdf_path: str | Path) -> bool:
        """
        Генерирует PDF-отчет на основе HTML-контента.

        Args:
            data (str): HTML-контент для генерации PDF.
            lang (str): Язык отчёта.
            pdf_path (str | Path): Путь для сохранения PDF-файла.

        Returns:
            bool: True, если PDF-отчет успешно сгенерирован и отправлен, иначе False.
        """
        pdf_path: Path = Path(pdf_path) if pdf_path and isinstance(pdf_path, (str, Path)) else self.pdf_path
        self.html_content: str = data if data else self.html_content

        if not self.pdf_utils.save_pdf_pdfkit(self.html_content, pdf_path):
            logger.error(f"Не удалось сохранить PDF файл {pdf_path}", exc_info=True)
            if self.bot:
                self.bot.send_message(self.chat_id, f"Не удалось сохранить файл {pdf_path}")
            ...
            return False

        if self.bot:
            try:
                with open(pdf_path, 'rb') as f:
                    self.bot.send_document(self.chat_id, f)
                    return True
            except Exception as ex:
                logger.error(f"Не удалось отправить файл {pdf_path} в чат {self.chat_id}", ex, exc_info=True)
                self.bot.send_message(self.chat_id, f"Не удалось отправить файл {pdf_path} по причине: {ex}")
                return False
        return True

    async def create_docx_report_async(self, html_path: str | Path, docx_path: str | Path) -> bool:
        """
        Создает DOCX файл из HTML.

        Args:
            html_path (str | Path): Путь к HTML файлу.
            docx_path (str | Path): Путь для сохранения DOCX файла.

        Returns:
            bool: True, если DOCX файл успешно создан, иначе False.
        """
        html_path: Path = Path(html_path) if isinstance(html_path, str) else html_path
        docx_path: Path = Path(docx_path) if isinstance(docx_path, str) else docx_path

        if not html_to_docx(html_path, docx_path):
            logger.error(f"Не удалось скомпилировать DOCX файл из {html_path} в {docx_path}", exc_info=True)
            return False
        logger.info(f"DOCX файл успешно создан из {html_path} в {docx_path}")
        return True

def main(maxiron_name: str, lang: str) -> bool:
    """
    Главная функция для генерации отчетов.

    Args:
        maxiron_name (str): Название мехирона.
        lang (str): Язык отчета.

    Returns:
        bool: True, если отчеты успешно сгенерированы, иначе False.
    """
    external_storage: Path = gs.path.external_storage / ENDPOINT / 'mexironim' / maxiron_name
    data: dict = j_loads(external_storage / f'{maxiron_name}_{lang}.json') #  Используем j_loads для загрузки JSON
    html_path: Path = external_storage / f'{maxiron_name}_{lang}.html'
    pdf_path: Path = external_storage / f'{maxiron_name}_{lang}.pdf'
    docx_path: Path = external_storage / f'{maxiron_name}_{lang}.docx'
    if_need_html: bool = True
    if_need_pdf: bool = True
    if_need_docx: bool = True
    r: ReportGenerator = ReportGenerator(if_need_html, if_need_pdf, if_need_docx)

    asyncio.run(r.create_reports_async(bot=None, #  Замените на реальный объект bot, если необходимо
                                        chat_id=None, # Замените на реальный chat_id, если необходимо
                                        data=data,
                                        lang=lang,
                                        mexiron_name=maxiron_name))
    return True

if __name__ == "__main__":
    maxiron_name: str = '250127221657987'  # <- debug
    lang: str = 'ru'

    main(maxiron_name, lang)