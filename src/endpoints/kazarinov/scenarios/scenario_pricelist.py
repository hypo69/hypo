from __future__ import annotations
## \file hypotez/src/endpoints/kazarinov/scenarios/scenario_pricelist.py
# -*- coding: utf-8 -*-\
#! venv/Scripts/python.exe
#! venv/bin/python/python3.12

"""
Модуль исполнения сценария создания мехирона для Сергея Казаринова
==================================================================

```rst
.. module:: src.endpoints.kazarinov.scenarios 
	:platform: Windows, Unix
	:synopsis: Provides functionality for extracting, parsing, and processing product data from 
various suppliers. The module handles data preparation, AI processing, 
and integration with Facebook for product posting.
```

"""
MODE = 'dev'

import asyncio
import random
import shutil
from pathlib import Path
from typing import Optional, List
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
    
    Attributes:
        driver (Driver): Экземпляр Selenium WebDriver.
        export_path (Path): Путь для экспорта данных.
        products_list (List[dict]): Список обработанных данных о продуктах.
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
        Initializes Mexiron class with required components.

        Args:
            driver (Driver): Selenium WebDriver instance.
            mexiron_name (Optional[str]): Custom name for the Mexiron process.
        """
        try:
            self.config = j_loads_ns(gs.path.endpoints / 'kazarinov' / 'kazarinov.json')
        except Exception as e:
            logger.error(f"Error loading configuration: {e}")
            return  # or raise an exception, depending on your error handling strategy

        self.timestamp = gs.now
        self.driver = driver
        self.mexiron_name = mexiron_name or self.timestamp

        try:
            storage = gs.path.external_storage if self.config.storage == 'external_storage' else gs.path.data if self.config.storage == 'data' else gs.path.goog
            self.export_path = storage / 'kazarinov' / 'mexironim' / self.mexiron_name
        except Exception as e:
            logger.error(f"Error constructing export path: {e}")
            return


        try:
            system_instruction = (gs.path.endpoints / 'kazarinov' / 'instructions' / 'system_instruction_mexiron.md').read_text(encoding='UTF-8')
            
            api_key = gs.credentials.gemini.kazarinov
            self.model = GoogleGenerativeAI(
                api_key=api_key,
                system_instruction=system_instruction,
                generation_config={'response_mime_type': 'application/json'}
            )
        except Exception as ex:
            logger.error(f"Error loading instructions or API key:", ex)
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
        Executes the scenario: parses products, processes them via AI, and stores data.

        Args:
            system_instruction (Optional[str]): System instructions for the AI model.
            price (Optional[str]): Price to process.
            mexiron_name (Optional[str]): Custom Mexiron name.
            urls (Optional[str | List[str]]): Product page URLs.

        Returns:
            bool: True if the scenario executes successfully, False otherwise.

        .. todo:
            сделать логер перед отрицательным выходом из функции. 
            Важно! модель ошибается. 

        ```mermaid
flowchart TD
    A[Start] --> B{URL is from OneTab?}
    B -->|Yes| C[Get data from OneTab]
    B -->|No| D[Reply - Try again]
    C --> E{Data valid?}
    E -->|No| F[Reply Incorrect data]
    E -->|Yes| G[Run Mexiron scenario]
    G --> H{Scenario successful?}
    H -->|Yes| I[Reply Done! I will send the link to WhatsApp]
    H -->|No| J[Reply Error running scenario]
    F --> K[Return]
    I --> K[Return]
    D --> K[Return]
    J --> K[Return]


```
        """
        self.update = update
        self.context = context

        # Не все поля товара надо заполнять. Вот кортеж необходимых полей:
        required_fields:tuple = ('id_product',
                                 'name',
                                 'description_short',
                                 'description',
                                 'specification',
                                 'local_saved_image')
        products_list = []

        for url in urls:

            graber = self.get_graber_by_supplier_url(url) 
            
            if not graber:
                logger.debug(f"Нет грабера для:\n{url}", None, False)
                ...
                continue

            try:
                await update.message.reply_text(f"""Strat parsing: 
                {url}""")
                f = await graber.grab_page(*required_fields)
                if gs.host_name == 'Vostro-3888':
                    self.driver.wait(5)   # <- ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Замедлитель
            except Exception as ex:
                logger.error(f"Ошибка получения полей товара",ex)
                ...
                continue

            if not f:
                logger.debug(f'Failed to parse product fields for URL: {url}')
                ...
                continue

            product_data = await self.convert_product_fields(f)

            if not product_data:
                logger.debug(f'Failed to convert product fields: {product_data}')
                ...
                continue

            if not await self.save_product_data(product_data):
                logger.error(f"Data not saved! {pprint(product_data)}")
                ...
            products_list.append(product_data)    

        # AI processing
        """ список компонентов сборки компьютера уходит в обработку моделью (`gemini`) -> 
        модель парсит данные, делает перевод на `ru`, `he` и возвращает кортеж словарей по языкам.
        Внимание! модель может ошибаться"""
        await update.message.reply_text(f"Start processing AI. lang = he")
        he = await self.process_ai(products_list,'he')

        await update.message.reply_text(f"Start processing AI. lang = he")
        ru = await self.process_ai(products_list,'ru')


        if not j_dumps(he, self.export_path / f'{self.mexiron_name}_he.json'):
            logger.error(f'Ошибка сохранения словаря `he`', None, False)
            ...
                
        if not j_dumps(ru, self.export_path / f'{self.mexiron_name}_ru.json'):
            logger.error(f'Ошибка сохранения словаря `ru`', None, False)
            ...

        if not await self.create_report(he, Path(self.export_path/f'{self.mexiron_name}_he.html'), Path(self.export_path/f'{self.mexiron_name}_he.pdf')):
            logger.error(f"Ошибка создания PDF: {self.mexiron_name}_he.pdf", None, False)
            ...

        if not await self.create_report(ru, Path(self.export_path/f'{self.mexiron_name}_ru.html'), Path(self.export_path/f'{self.mexiron_name}_ru.pdf')):
            logger.error(f"Ошибка создания PDF: {self.mexiron_name}_ru.pdf", None, False)
        ...
        return True 


    def get_graber_by_supplier_url(self, url: str):
        """
        Returns the appropriate graber for a given supplier URL.
        Для каждого поставщика реализован свой грабер, который вытаскивает значения полей с целевой html страницы 

        Args:
            url (str): Supplier page URL.

        Returns:
            Optional[object]: Graber instance if a match is found, None otherwise.
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
        logger.debug(f'No graber found for URL: {url}')
        ...
        return 

    async def convert_product_fields(self, f: ProductFields) -> dict:
        """
        Converts product fields into a dictionary. 
        Функция конвертирует поля из объекта `ProductFields` в простой словарь для модели ии.


        Args:
            f (ProductFields): Object containing parsed product data.

        Returns:
            dict: Formatted product data dictionary.

        .. note:: Правила построения полей определяются в `ProductFields`
        """



        return {
            'product_title': f.name['language'][0]['value'].strip().replace("'", "\\'").replace('"', '\\"'),
            'product_id': f.id_product,
            'description_short': f.description_short['language'][0]['value'].strip().replace("'", "\\'").replace('"', '\\"'),
            'description': f.description['language'][0]['value'].strip().replace("'", "\\'").replace('"', '\\"'),
            'specification': f.specification['language'][0]['value'].strip().replace("'", "\\'").replace('"', '\\"'),
            'local_saved_image': str(f.local_saved_image),
        }

    async def save_product_data(self, product_data: dict):
        """
        Saves individual product data to a file.

        Args:
            product_data (dict): Formatted product data.
        """
        file_path = self.export_path / 'products' / f"{product_data['product_id']}.json"
        if not j_dumps(product_data, file_path, ensure_ascii=False):
            logger.error(f'Ошибка сохранения словаря {pprint(product_data)}\n Путь: {file_path}')
            ...
            return
        return True

    async def process_ai(self, products_list: List[str], lang:str,  attempts: int = 3) -> tuple | bool:
        """
        Processes the product list through the AI model.

        Args:
            products_list (str): List of product data dictionaries as a string.
            attempts (int, optional): Number of attempts to retry in case of failure. Defaults to 3.

        Returns:
            tuple: Processed response in `ru` and `he` formats.
            bool: False if unable to get a valid response after retries.

        .. note::
            Модель может возвращать невелидный результат.
            В таком случае я переспрашиваю модель разумное количество раз.
        """
        if attempts < 1:
            ...
            return {}  # return early if no attempts are left
        model_command = Path(gs.path.endpoints / 'kazarinov' / 'instructions' / f'command_instruction_mexiron_{lang}.md').read_text(encoding='UTF-8')
        # Request response from the AI model
        response = await self.model.ask(model_command + '\n' + str(products_list))
        if not response:
            logger.error(f"Нет ответа от модели")
            ...
            return {}

        response_dict:dict = j_loads(response)

        if not response_dict:
            logger.error("Ошибка парсинга ответа модели", None, False)
            if attempts > 1:
                ...
                await self.process_ai(products_list, lang, attempts -1 )
            return {}
        return  response_dict

 
    async def post_facebook(self, mexiron:SimpleNamespace) -> bool:
        """Функция исполняет сценарий рекламного модуля `facvebook`."""
        ...
        self.driver.get_url(r'https://www.facebook.com/profile.php?id=61566067514123')
        currency = "ש''ח"
        title = f'{mexiron.title}\n{mexiron.description}\n{mexiron.price} {currency}'
        if not post_message_title(self.d, title):
            logger.warning(f'Не получилось отправить название мехирона')
            ...
            return

        if not upload_post_media(self.d, media = mexiron.products):
            logger.warning(f'Не получилось отправить media')
            ...
            return
        if not message_publish(self.d):
            logger.warning(f'Не получилось отправить media')
            ...
            return

        return True

    async def create_report(self, data:dict, html_file:Path, pdf_file:Path):
        """Функция отправляет задание на создание мехирона в форматax `html` и `pdf`"""

        generator = ReportGenerator( base_path = self.export_path, timestamp = self.timestamp )
        ...
        for lang in ['he','ru']:
            generator.create_report(lang)


