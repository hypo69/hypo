# Анализ кода модуля `scenario_pricelist`

**Качество кода**
8
-   Плюсы
    -   Код разбит на логические блоки, что способствует читаемости.
    -   Используются `logger` для логирования ошибок.
    -   Применяется асинхронность для неблокирующих операций.
    -   Код использует dataclasses и typing для улучшения структуры данных.
    -   Используется `j_loads_ns` и `j_dumps` для работы с json.
-   Минусы
    -   Отсутствует полная документация в формате reStructuredText.
    -   Имеются неполные docstring.
    -   Многократное использование `...` как заглушек.
    -   Использование try/except с `return` без явной обработки ошибок.
    -   Некоторые функции требуют более подробных комментариев.
    -   Используется `pprint` напрямую, что может быть не оптимально для логирования.

**Рекомендации по улучшению**

1.  **Документация**:
    -   Добавить reStructuredText (RST) docstring для всех классов, методов и функций.
    -   Улучшить комментарии для функций, переменных, и методов, согласно стандарту RST.
2.  **Обработка ошибок**:
    -   Заменить `try-except` с `return` на `logger.error` и проброс исключений или корректную обработку.
    -   Улучшить логирование, добавляя контекст и уровень детализации.
3.  **Рефакторинг**:
    -   Использовать более описательные имена переменных и функций.
    -   Удалить или заменить `...` на конкретный код или комментарий.
    -   Разбить сложные функции на более мелкие и специализированные.
    -   Избегать дублирования кода, например, в блоках обработки языков.
4.  **Улучшение производительности**:
    -   Рассмотреть асинхронную обработку внутри цикла, если это возможно.
5.  **Структура кода**:
    -   Организовать импорты в соответствии с PEP 8.
    -   Привести в соответствие имена функций, переменных и импортов с ранее обработанными файлами.

**Оптимизированный код**
```python
"""
Модуль исполнения сценария создания мехирона для Сергея Казаринова
==================================================================

:platform: Windows, Unix
:synopsis: Provides functionality for extracting, parsing, and processing product data from 
           various suppliers. The module handles data preparation, AI processing, 
           and integration with Facebook for product posting.
"""
from __future__ import annotations

import asyncio
import random
import shutil
from pathlib import Path
from typing import Optional, List, Any, Tuple
from types import SimpleNamespace
from dataclasses import field

import header # TODO: уточнить назначение модуля и добавить описание в rst
from src import gs
from src.product.product_fields import ProductFields
from src.webdriver.driver import Driver
from src.ai.gemini import GoogleGenerativeAI
from src.endpoints.advertisement.facebook.scenarios import (
    post_message_title,
    upload_post_media,
    message_publish,
)
from src.suppliers.morlevi.graber import Graber as MorleviGraber
from src.suppliers.ksp.graber import Graber as KspGraber
from src.suppliers.ivory.graber import Graber as IvoryGraber
from src.suppliers.grandadvance.graber import Graber as GrandadvanceGraber
from src.endpoints.kazarinov.pricelist_generator import ReportGenerator
from telegram import Update
from telegram.ext import CallbackContext

from src.utils.jjson import j_loads, j_loads_ns, j_dumps
from src.utils.file import read_text_file, save_text_file, recursively_get_file_path
from src.utils.image import save_png_from_url, save_png
from src.utils.convertors.unicode import decode_unicode_escape
from src.logger.logger import logger # Исправлено: импорт logger
from src.utils.printer import pprint


MODE = 'dev'


class MexironBuilder:
    """
    Класс для обработки извлечения, разбора и сохранения данных о продуктах поставщиков.

    :param driver: Экземпляр Selenium WebDriver.
    :type driver: Driver
    :param mexiron_name: Имя мехирона (опционально).
    :type mexiron_name: Optional[str]
    :ivar driver: Экземпляр Selenium WebDriver.
    :vartype driver: Driver
    :ivar export_path: Путь для экспорта данных.
    :vartype export_path: Path
    :ivar mexiron_name: Имя мехирона.
    :vartype mexiron_name: str
    :ivar price: Цена мехирона.
    :vartype price: float
    :ivar timestamp: Временная метка создания мехирона.
    :vartype timestamp: str
    :ivar products_list: Список обработанных данных о продуктах.
    :vartype products_list: List[dict]
    :ivar model: Экземпляр модели Google Generative AI.
    :vartype model: GoogleGenerativeAI
    :ivar config: Конфигурация приложения.
    :vartype config: SimpleNamespace
    :ivar update: Telegram update object.
    :vartype update: Update
    :ivar context: Telegram callback context.
    :vartype context: CallbackContext

    """

    driver: Driver
    export_path: Path
    mexiron_name: str
    price: float
    timestamp: str
    products_list: List = field(default_factory=list)
    model: GoogleGenerativeAI
    config: SimpleNamespace

    # telegram
    update: Update
    context: CallbackContext

    def __init__(self, driver: Driver, mexiron_name: Optional[str] = None):
        """
        Инициализирует класс MexironBuilder.

        :param driver: Экземпляр Selenium WebDriver.
        :type driver: Driver
        :param mexiron_name: Пользовательское имя для процесса Mexiron (опционально).
        :type mexiron_name: Optional[str]
        """
        try:
            # код исполняет загрузку конфигурации из файла kazarinov.json
            self.config = j_loads_ns(gs.path.endpoints / 'kazarinov' / 'kazarinov.json')
        except Exception as e:
            logger.error(f"Ошибка загрузки конфигурации: {e}")
            return  # или вызвать исключение, в зависимости от стратегии обработки ошибок

        self.timestamp = gs.now
        self.driver = driver
        self.mexiron_name = mexiron_name or self.timestamp

        try:
            # код определяет путь к хранилищу в зависимости от конфигурации
            storage = gs.path.external_storage if self.config.storage == 'external_storage' else gs.path.data if self.config.storage == 'data' else gs.path.goog
            self.export_path = storage / 'kazarinov' / 'mexironim' / self.mexiron_name
        except Exception as e:
            logger.error(f"Ошибка при создании пути экспорта: {e}")
            return

        try:
            # код загружает системную инструкцию из файла system_instruction_mexiron.md
            system_instruction = (gs.path.endpoints / 'kazarinov' / 'instructions' / 'system_instruction_mexiron.md').read_text(encoding='UTF-8')
            api_key = gs.credentials.gemini.kazarinov
            # код инициализирует модель GoogleGenerativeAI
            self.model = GoogleGenerativeAI(
                api_key=api_key,
                system_instruction=system_instruction,
                generation_config={'response_mime_type': 'application/json'}
            )
        except Exception as ex:
            logger.error(f"Ошибка загрузки инструкций или API ключа: {ex}")
            return

    async def run_scenario(
        self,
        update: Update,
        context: CallbackContext,
        urls: list[str],
        price: Optional[str] = '',
        mexiron_name: Optional[str] = '',
    ) -> bool:
        """
        Выполняет сценарий: парсит продукты, обрабатывает их через ИИ и сохраняет данные.

        :param update: Telegram update object.
        :type update: Update
        :param context: Telegram callback context.
        :type context: CallbackContext
        :param urls: Список URL-адресов страниц продуктов.
        :type urls: List[str]
        :param price: Цена для обработки.
        :type price: Optional[str]
        :param mexiron_name: Пользовательское имя мехирона.
        :type mexiron_name: Optional[str]
        :return: True если сценарий выполнен успешно, False в противном случае.
        :rtype: bool

        .. todo::
            сделать логер перед отрицательным выходом из функции.
            Важно! модель ошибается.

        """
        self.update = update
        self.context = context
        required_fields: tuple = (
            'id_product',
            'name',
            'description_short',
            'description',
            'specification',
            'local_saved_image',
        )
        products_list = []
        # code cycles through the list of urls
        for url in urls:
            # код выбирает граббер на основе URL
            graber = self.get_graber_by_supplier_url(url)

            if not graber:
                logger.debug(f"Нет грабера для: {url}")
                continue

            try:
                # code informs the user that the page is being processed
                await update.message.reply_text(f"Process: \n{url}")
                # code calls the grabber method to get the product fields
                f = await graber.grab_page(*required_fields)
                if gs.host_name == 'Vostro-3888':
                   pass
            except Exception as ex:
                logger.error(f"Ошибка получения полей товара: {ex}")
                continue

            if not f:
                logger.debug(f'Не удалось распарсить поля товара для URL: {url}')
                continue

            # code converts product data from ProductFields to dict
            product_data = await self.convert_product_fields(f)
            if not product_data:
                logger.debug(f'Не удалось конвертировать поля товара: {product_data}')
                continue
            # code saves product data
            if not await self.save_product_data(product_data):
                logger.error(f"Данные не сохранены! {pprint(product_data)}")
                continue
            products_list.append(product_data)

        # AI processing
        """ список компонентов сборки компьютера уходит в обработку моделью (`gemini`) ->
        модель парсит данные, делает перевод на `ru`, `he` и возвращает кортеж словарей по языкам.
        Внимание! модель может ошибаться"""
        await update.message.reply_text(f"AI processing lang = he")
        he = await self.process_ai(products_list, 'he')
        if he and 'he' in he: # Проверка наличия ключа 'he'
             he['he']['price'] = price
             he['he']['currency'] = "ש''ח"
        else:
           logger.error(f'Неверный формат ответа модели для языка he. Проверьте структуру ответа. {he=}')
           return False

        await update.message.reply_text("successfull")
        await update.message.reply_text(f"AI processing lang = ru")
        ru = await self.process_ai(products_list, 'ru')
        if ru and 'ru' in ru: # Проверка наличия ключа 'ru'
           ru['ru']['price'] = price
           ru['ru']['currency'] = "шекелей"
        else:
           logger.error(f'Неверный формат ответа модели для языка ru. Проверьте структуру ответа. {ru=}')
           return False
        # code saving json files
        if not j_dumps(he, self.export_path / f'{self.mexiron_name}_he.json'):
            logger.error(f'Ошибка сохранения словаря `he`')
            return False


        if not j_dumps(ru, self.export_path / f'{self.mexiron_name}_ru.json'):
            logger.error(f'Ошибка сохранения словаря `ru`')
            return False


        generator = ReportGenerator()
        # code cycles through language list `he` and `ru`
        for lang in ['he', 'ru']:
            html_file = Path(self.export_path / f'{self.mexiron_name}_{lang}.html')
            pdf_file = Path(self.export_path / f'{self.mexiron_name}_{lang}.pdf')
            # code creates html and pdf reports
            if not await generator.create_report(
                data=he if lang == 'he' else ru,
                lang=lang,
                html_file=html_file,
                pdf_file=pdf_file,
            ):
                logger.error(f"Ошибка создания PDF: {self.mexiron_name}_{lang}.pdf")
                continue
            # code checking if the report exist
            if pdf_file.exists() and pdf_file.is_file():
                # code sends the pdf report to the bot
                await self.update.message.reply_document(document=pdf_file)
            else:
                logger.error(f"PDF файл не найден или не является файлом: {pdf_file}")
                continue

        return True

    def get_graber_by_supplier_url(self, url: str):
        """
        Возвращает соответствующий граббер для заданного URL-адреса поставщика.
        Для каждого поставщика реализован свой грабер, который извлекает значения полей с целевой HTML-страницы.

        :param url: URL-адрес страницы поставщика.
        :type url: str
        :return: Экземпляр граббера, если соответствие найдено, иначе None.
        :rtype: Optional[object]
        """
        # code opens a url in the browser
        self.driver.get_url(url)
        if url.startswith(('https://morlevi.co.il', 'https://www.morlevi.co.il')):
            return MorleviGraber(self.driver)
        if url.startswith(('https://ksp.co.il', 'https://www.ksp.co.il')):
            return KspGraber(self.driver)
        if url.startswith(('https://grandadvance.co.il', 'https://www.grandadvance.co.il')):
            return GrandadvanceGraber(self.driver)
        if url.startswith(('https://ivory.co.il', 'https://www.ivory.co.il')):
            return IvoryGraber(self.driver)
        logger.debug(f'Не найден граббер для URL: {url}')
        return None

    async def convert_product_fields(self, f: ProductFields) -> dict:
        """
        Преобразует поля продукта в словарь.
        Функция конвертирует поля из объекта `ProductFields` в простой словарь для модели ИИ.

        :param f: Объект, содержащий распарсенные данные о продукте.
        :type f: ProductFields
        :return: Словарь с отформатированными данными о продукте.
        :rtype: dict

        .. note:: Правила построения полей определяются в `ProductFields`
        """
        if not f.id_product:
            return {}  # сбой при получении полей товара. Такое может произойти если вместо страницы товара попалась страница категории, при невнимательном составлении мехирона из комплектующих
        return {
            'product_title': f.name['language'][0]['value'].strip().replace("'", "\\'").replace('"', '\\"'),
            'product_id': f.id_product,
            'description_short': f.description_short['language'][0]['value'].strip().replace("'", "\\'").replace('"', '\\"').replace(';', '<br>'),
            'description': f.description['language'][0]['value'].strip().replace("'", "\\'").replace('"', '\\"').replace(';', '<br>'),
            'specification': f.specification['language'][0]['value'].strip().replace("'", "\\'").replace('"', '\\"').replace(';', '<br>'),
            'local_saved_image': str(f.local_saved_image),
        }

    async def save_product_data(self, product_data: dict) -> bool:
        """
        Сохраняет данные об отдельном продукте в файл.

        :param product_data: Словарь с отформатированными данными о продукте.
        :type product_data: dict
        :return: True в случае успешного сохранения, False в противном случае
        :rtype: bool
        """
        file_path = self.export_path / 'products' / f"{product_data['product_id']}.json"
        if not j_dumps(product_data, file_path, ensure_ascii=False):
            logger.error(f'Ошибка сохранения словаря {pprint(product_data)}\\n Путь: {file_path}')
            return False
        return True

    async def process_ai(self, products_list: List[dict], lang: str, attempts: int = 3) -> dict | bool:
        """
        Обрабатывает список продуктов через модель ИИ.

        :param products_list: Список словарей с данными о продуктах.
        :type products_list: List[dict]
        :param lang: Язык для обработки.
        :type lang: str
        :param attempts: Количество попыток повтора в случае неудачи (по умолчанию 3).
        :type attempts: int
        :return: Обработанный ответ в формате словаря.
        :rtype: dict | bool

        .. note::
            Модель может возвращать невалидный результат.
            В таком случае я переспрашиваю модель разумное количество раз.
        """
        if attempts < 1:
            logger.error("Нет попыток для обработки запроса в ИИ")
            return {}  # return early if no attempts are left

        try:
             # code reads ai command from file
            model_command = Path(gs.path.endpoints / 'kazarinov' / 'instructions' / f'command_instruction_mexiron_{lang}.md').read_text(encoding='UTF-8')
            # code request response from the AI model
            response = await self.model.ask(model_command + '\n' + str(products_list))
            if not response:
                logger.error("Нет ответа от модели")
                return {}
            # code converts response from the AI model to dictionary
            response_dict: dict = j_loads(response)
            if not response_dict:
                logger.error("Ошибка парсинга ответа модели")
                if attempts > 1:
                    return await self.process_ai(products_list, lang, attempts - 1)
                return {}
            return response_dict
        except Exception as e:
            logger.error(f'Непредвиденная ошибка при обработке запроса в ИИ: {e}')
            return {}

    async def post_facebook(self, mexiron: SimpleNamespace) -> bool:
        """Исполняет сценарий рекламного модуля `facebook`."""
        self.driver.get_url(r'https://www.facebook.com/profile.php?id=61566067514123')
        currency = "ש''ח"
        title = f'{mexiron.title}\\n{mexiron.description}\\n{mexiron.price} {currency}'
        if not post_message_title(self.driver, title):
            logger.warning(f'Не получилось отправить название мехирона')
            return False

        if not upload_post_media(self.driver, media=mexiron.products):
            logger.warning(f'Не получилось отправить media')
            return False
        if not message_publish(self.driver):
            logger.warning(f'Не получилось отправить media')
            return False

        return True

    async def create_report(self, data: dict, html_file: Path, pdf_file: Path) -> bool:
        """
        Отправляет задание на создание мехирона в формате `html` и `pdf`.
        Если мехирон в PDF создался (`generator.create_report()` вернул True),
        отправить его боту.

        :param data: Данные для отчета.
        :type data: dict
        :param html_file: Путь к файлу HTML.
        :type html_file: Path
        :param pdf_file: Путь к файлу PDF.
        :type pdf_file: Path
        :return: True если отчет создан и отправлен, False в противном случае
        :rtype: bool
        """
        generator = ReportGenerator()
        # code cycles through language list `he` and `ru`
        for lang in ['he', 'ru']:
             # code creates html and pdf reports
             if await generator.create_report(data, lang, html_file, pdf_file):
                # code checking if the report exist
                if pdf_file.exists() and pdf_file.is_file():
                    # code sends the pdf report to the bot
                    await self.update.message.reply_document(document=pdf_file)
                else:
                    logger.error(f"PDF файл не найден или не является файлом: {pdf_file}")
                    return False
        return True
```