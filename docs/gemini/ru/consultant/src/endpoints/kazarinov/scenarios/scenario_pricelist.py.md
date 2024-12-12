# Анализ кода модуля scenario_pricelist

**Качество кода**
9
-  Плюсы
    - Код хорошо структурирован, с разделением на классы и функции.
    - Используется `asyncio` для асинхронных операций, что улучшает производительность.
    - Применяется логирование для отслеживания ошибок и важной информации.
    - Код разбит на логические блоки, что облегчает понимание.
    - Используется `j_loads_ns`, `j_loads`, `j_dumps` для работы с `json`.
    - Документация в формате reStructuredText (RST).
-  Минусы
    - Есть места с `...`, которые должны быть заменены конкретной обработкой или логированием.
    - Некоторые блоки `try-except` могут быть заменены на `logger.error`.
    - Дублирование логики отправки PDF-файлов в функциях `run_scenario` и `create_report`.
    - Не всегда понятно, почему используется `...` в коде.

**Рекомендации по улучшению**

1.  **Удалить `...`:** Заменить все `...` на конкретные действия, такие как логирование или обработка ошибок.
2.  **Унификация логирования:** Вместо использования `try-except` с пустым `except` использовать `logger.error` с указанием исключения.
3.  **Рефакторинг отправки PDF:** Вынести логику отправки PDF в отдельную функцию для избежания дублирования кода.
4.  **Уточнение комментариев:** Добавить более точные комментарии к функциям, методам и переменным, где это необходимо.
5.  **Обработка ошибок в `__init__`:**  Если не удалось загрузить конфиг или создать путь экспорта, то лучше поднять исключение, чем просто выйти из `__init__`. Это поможет избежать последующих ошибок при использовании этого класса.
6.  **Упрощение `convert_product_fields`:** Упростить формирование словаря в методе `convert_product_fields` , для избежания дублирования кода и упрощения читаемости.
7.  **Обработка ошибок в `process_ai`:**  В методе `process_ai` убрать рекурсивный вызов функции в случае ошибки. Использовать цикл `for`.

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
from typing import Optional, List, Any
from types import SimpleNamespace
from dataclasses import field

import header
from src import gs
from src.product.product_fields import ProductFields
from src.webdriver.driver import Driver
from src.ai.gemini import GoogleGenerativeAI
from src.endpoints.advertisement.facebook.scenarios import (
    post_message_title, upload_post_media, message_publish
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
from src.utils.printer import pprint
from src.logger.logger import logger


class MexironBuilder:
    """
    Обрабатывает извлечение, разбор и сохранение данных о продуктах поставщиков.

    :ivar driver: Экземпляр Selenium WebDriver.
    :vartype driver: Driver
    :ivar export_path: Путь для экспорта данных.
    :vartype export_path: Path
    :ivar products_list: Список обработанных данных о продуктах.
    :vartype products_list: List[dict]
    :ivar mexiron_name: Имя мехирона
    :vartype mexiron_name: str
    :ivar price: Цена
    :vartype price: float
    :ivar timestamp: Временная метка
    :vartype timestamp: str
    :ivar model: Экземпляр модели GoogleGenerativeAI
    :vartype model: GoogleGenerativeAI
    :ivar config: Конфигурация
    :vartype config: SimpleNamespace
    :ivar update: Объект Update от Telegram
    :vartype update: Update
    :ivar context: Объект CallbackContext от Telegram
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
        :param mexiron_name: Имя мехирона.
        :type mexiron_name: Optional[str], optional
        :raises FileNotFoundError: Если не удается загрузить конфигурационный файл.
        :raises Exception: Если не удается создать путь экспорта.
        """
        try:
            self.config = j_loads_ns(gs.path.endpoints / 'kazarinov' / 'kazarinov.json')
        except Exception as e:
            logger.error(f"Error loading configuration: {e}", exc_info=True)
            raise FileNotFoundError(f"Configuration file not found or invalid: {e}")
        
        self.timestamp = gs.now
        self.driver = driver
        self.mexiron_name = mexiron_name or self.timestamp
        try:
            storage = gs.path.external_storage if self.config.storage == 'external_storage' else gs.path.data if self.config.storage == 'data' else gs.path.goog
            self.export_path = storage / 'kazarinov' / 'mexironim' / self.mexiron_name
        except Exception as e:
             logger.error(f"Error constructing export path: {e}", exc_info=True)
             raise Exception(f"Failed to construct export path: {e}")

        try:
            system_instruction = (gs.path.endpoints / 'kazarinov' / 'instructions' / 'system_instruction_mexiron.md').read_text(encoding='UTF-8')

            api_key = gs.credentials.gemini.kazarinov
            self.model = GoogleGenerativeAI(
                api_key=api_key,
                system_instruction=system_instruction,
                generation_config={'response_mime_type': 'application/json'}
            )
        except Exception as ex:
             logger.error(f"Error loading instructions or API key: {ex}", exc_info=True)
             raise Exception(f"Failed to load instructions or API key: {ex}")

    async def run_scenario(
        self,
        update: Update,
        context: CallbackContext,
        urls: list[str],
        price: Optional[str] = '',
        mexiron_name: Optional[str] = '',

    ) -> bool:
        """
        Исполняет сценарий: обрабатывает продукты, используя ИИ, и сохраняет данные.

        :param update: Объект Update от Telegram.
        :type update: Update
        :param context: Объект CallbackContext от Telegram.
        :type context: CallbackContext
        :param urls: Список URL страниц товаров.
        :type urls: list[str]
        :param price: Цена для обработки.
        :type price: Optional[str], optional
        :param mexiron_name: Имя мехирона.
        :type mexiron_name: Optional[str], optional
        :return: True, если сценарий выполнен успешно, иначе False.
        :rtype: bool
        """
        self.update = update
        self.context = context

        required_fields: tuple = (
            'id_product',
            'name',
            'description_short',
            'description',
            'specification',
            'local_saved_image'
        )
        products_list = []

        for url in urls:
            graber = self.get_graber_by_supplier_url(url)

            if not graber:
                logger.debug(f"Нет грабера для: {url}")
                continue

            try:
                await update.message.reply_text(f"Process: \n{url}")
                f = await graber.grab_page(*required_fields)
                if gs.host_name == 'Vostro-3888':
                    self.driver.wait(5) # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Замедлитель
            except Exception as ex:
                logger.error(f"Ошибка получения полей товара: {ex}", exc_info=True)
                continue

            if not f:
                logger.debug(f'Не удалось распарсить поля продукта для URL: {url}')
                continue

            product_data = await self.convert_product_fields(f)

            if not product_data:
                logger.debug(f'Не удалось преобразовать поля продукта: {product_data}')
                continue

            if not await self.save_product_data(product_data):
                logger.error(f"Данные не сохранены! {pprint(product_data)}")

            products_list.append(product_data)

        # AI processing
        """
        Список компонентов сборки компьютера уходит в обработку моделью (`gemini`) ->
        модель парсит данные, делает перевод на `ru`, `he` и возвращает кортеж словарей по языкам.
        Внимание! модель может ошибаться
        """
        await update.message.reply_text(f"AI processing lang = he")
        he = await self.process_ai(products_list, 'he')
        await update.message.reply_text("successfull")
        await update.message.reply_text(f"AI processing lang = ru")
        ru = await self.process_ai(products_list, 'ru')
        await update.message.reply_text("successfull")


        if not j_dumps(he, self.export_path / f'{self.mexiron_name}_he.json'):
            logger.error(f'Ошибка сохранения словаря `he`')

        if not j_dumps(ru, self.export_path / f'{self.mexiron_name}_ru.json'):
            logger.error(f'Ошибка сохранения словаря `ru`')


        generator = ReportGenerator()

        for lang in ['he', 'ru']:
            html_file = Path(self.export_path / f'{self.mexiron_name}_{lang}.html')
            pdf_file = Path(self.export_path / f'{self.mexiron_name}_{lang}.pdf')
            if not await generator.create_report(data=he if lang == 'he' else ru,
                                                 lang=lang,
                                                 html_file=html_file,
                                                 pdf_file=pdf_file):
                logger.error(f"Ошибка создания PDF: {self.mexiron_name}_{lang}.pdf")
                continue

            await self._send_pdf_to_bot(pdf_file)

        return True

    def get_graber_by_supplier_url(self, url: str):
        """
        Возвращает соответствующий грабер для URL поставщика.

        :param url: URL страницы поставщика.
        :type url: str
        :return: Экземпляр грабера, если найден, иначе None.
        :rtype: Optional[object]
        """
        self.driver.get_url(url)
        if url.startswith(('https://morlevi.co.il', 'https://www.morlevi.co.il')):
            return MorleviGraber(self.driver)
        if url.startswith(('https://ksp.co.il', 'https://www.ksp.co.il')):
            return KspGraber(self.driver)
        if url.startswith(('https://grandadvance.co.il', 'https://www.grandadvance.co.il')):
            return GrandadvanceGraber(self.driver)
        if url.startswith(('https://ivory.co.il', 'https://www.ivory.co.il')):
            return IvoryGraber(self.driver)
        logger.debug(f'Не найден грабер для URL: {url}')
        return None

    async def convert_product_fields(self, f: ProductFields) -> dict:
        """
        Преобразует поля продукта в словарь для обработки ИИ.

        :param f: Объект с распарсенными данными продукта.
        :type f: ProductFields
        :return: Словарь с данными продукта.
        :rtype: dict
        """
        def _sanitize_value(value: str) -> str:
             return value.strip().replace("'", "\\'").replace('"', '\\"').replace(';', '<br>')

        return {
             'product_title': _sanitize_value(f.name['language'][0]['value']),
             'product_id': f.id_product,
             'description_short': _sanitize_value(f.description_short['language'][0]['value']),
             'description': _sanitize_value(f.description['language'][0]['value']),
             'specification': _sanitize_value(f.specification['language'][0]['value']),
             'local_saved_image': str(f.local_saved_image),
        }

    async def save_product_data(self, product_data: dict):
        """
        Сохраняет данные продукта в файл.

        :param product_data: Словарь с данными продукта.
        :type product_data: dict
        :return: True, если данные сохранены, иначе False.
        :rtype: bool
        """
        file_path = self.export_path / 'products' / f"{product_data['product_id']}.json"
        if not j_dumps(product_data, file_path, ensure_ascii=False):
            logger.error(f'Ошибка сохранения словаря {pprint(product_data)}\\n Путь: {file_path}')
            return False
        return True

    async def process_ai(self, products_list: List[str], lang: str, attempts: int = 3) -> dict:
        """
        Обрабатывает список продуктов с помощью ИИ.

        :param products_list: Список словарей с данными продуктов.
        :type products_list: List[dict]
        :param lang: Язык для обработки.
        :type lang: str
        :param attempts: Количество попыток для повторной обработки в случае неудачи.
        :type attempts: int
        :return: Словарь с обработанными данными.
        :rtype: dict
        """
        if attempts < 1:
            logger.error(f"Не удалось получить корректный ответ от модели после {attempts} попыток")
            return {}
        model_command = (gs.path.endpoints / 'kazarinov' / 'instructions' / f'command_instruction_mexiron_{lang}.md').read_text(encoding='UTF-8')
        # Request response from the AI model
        response = await self.model.ask(model_command + '\n' + str(products_list))
        if not response:
            logger.error(f"Нет ответа от модели")
            return {}

        response_dict: dict = j_loads(response)

        if not response_dict:
            logger.error("Ошибка парсинга ответа модели")
            for _ in range(attempts - 1):
                 return await self.process_ai(products_list, lang, 0)
            return {}
        return response_dict


    async def post_facebook(self, mexiron: SimpleNamespace) -> bool:
        """
         Исполняет сценарий рекламного модуля `facvebook`.

         :param mexiron: Объект с данными мехирона.
         :type mexiron: SimpleNamespace
         :return: True, если сценарий выполнен успешно, иначе False.
         :rtype: bool
        """
        self.driver.get_url(r'https://www.facebook.com/profile.php?id=61566067514123')
        currency = "ש''ח"
        title = f'{mexiron.title}\n{mexiron.description}\n{mexiron.price} {currency}'
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

    async def create_report(self, data: dict, html_file: Path, pdf_file: Path):
         """
         Создает мехирон в формате `html` и `pdf`.

         :param data: Словарь с данными для отчета.
         :type data: dict
         :param html_file: Путь к html файлу.
         :type html_file: Path
         :param pdf_file: Путь к pdf файлу.
         :type pdf_file: Path
         """
         generator = ReportGenerator()
         for lang in ['he', 'ru']:
            if await generator.create_report(data, lang, html_file, pdf_file):
                await self._send_pdf_to_bot(pdf_file)
            else:
                logger.error(f"Ошибка создания PDF: {pdf_file}")

    async def _send_pdf_to_bot(self, pdf_file: Path):
        """
         Отправляет PDF файл боту.

         :param pdf_file: Путь к pdf файлу.
         :type pdf_file: Path
         """
        if pdf_file.exists() and pdf_file.is_file():
             await self.update.message.reply_document(document=pdf_file)
        else:
             logger.error(f"PDF файл не найден или не является файлом: {pdf_file}")