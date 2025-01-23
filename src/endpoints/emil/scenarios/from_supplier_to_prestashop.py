from __future__ import annotations

from src.suppliers import aliexpress
## \file /src/endpoints/emil/scenarios/from_supplier_to_prestashop.py
# -*- coding: utf-8 -*-\

#! .pyenv/bin/python3

"""
Модуль исполнения сценария создания мехирона для Сергея Казаринова
==================================================================

```rst
.. module:: src.endpoints.emil.scenarios.from_supplier_to_prestashop 
	:platform: Windows, Unix
	:synopsis: Provides functionality for extracting, parsing, and processing product data from 
various suppliers. The module handles data preparation, AI processing, 
and integration with Prestashop for product posting.
```

"""


import asyncio
import random
import shutil
from pathlib import Path
from typing import Optional, List
from types import SimpleNamespace
from dataclasses import field

from telegram import Update
from telegram.ext import CallbackContext

import header
from src import gs
from src.endpoints.prestashop.product_fields import ProductFields
from src.webdriver.driver import Driver
from src.ai.gemini import GoogleGenerativeAI
from src.endpoints.advertisement.facebook.scenarios import (
    post_message_title, upload_post_media, message_publish
)



from src.utils.jjson import j_loads, j_loads_ns, j_dumps
from src.utils.file import read_text_file, save_text_file, recursively_get_file_path
from src.utils.image import save_image_from_url, save_image
from src.utils.convertors.unicode import decode_unicode_escape
from src.utils.printer import pprint
from src.logger.logger import logger


class SupplierToPrestashopProvider:
    """
    Обрабатывает извлечение, разбор и сохранение данных о продуктах поставщиков.
    
    Attributes:
        driver (Driver): Экземпляр Selenium WebDriver.
        export_path (Path): Путь для экспорта данных.
        products_list (List[dict]): Список обработанных данных о продуктах.
    """

    driver: 'Driver'
    export_path: Path
    mexiron_name: str
    price: float
    timestamp: str
    products_list: List = field(default_factory=list)
    model: 'GoogleGenerativeAI'
    config: SimpleNamespace
    update: 'Update' 
    context: 'CallbackContext'

    def __init__(self, driver: Driver):
        """
        Initializes SupplierToPrestashopProvider class with required components.

        Args:
            driver (Driver): Selenium WebDriver instance.

        """
        try:
            self.config = j_loads_ns(gs.path.endpoints / 'emil' / 'emil.json')
        except Exception as ex:
            logger.error(f"Error loading configuration: {ex}")
            return  # or raise an exception, depending on your error handling strategy

        self.timestamp = gs.now
        self.driver = driver

        try:
            storage = gs.path.external_storage if self.config.storage == 'external_storage' else gs.path.data if self.config.storage == 'data' else gs.path.goog
            self.export_path = storage / 'emil' 
        except Exception as ex:
            logger.error(f"Error constructing export path: {ex}")
            return


        try:
            system_instruction = (gs.path.endpoints / 'emil' / 'instructions' / 'system_instruction_mexiron.md').read_text(encoding='UTF-8')
            
            api_key = gs.credentials.gemini.emil
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

        """
        self.update = update
        self.context = context

        # Не все поля товара надо заполнять. Вот кортеж необходимых полей:
        required_fields:tuple = ('id_product',
                                 'name',
                                 'description_short',
                                 'description',
                                 'specification',
                                 'local_image_path')
        products_list = []

        # 1. Сбор товаров
        for url in urls:

            graber = self.get_graber_by_supplier_url(url) 
            
            if not graber:
                logger.debug(f"Нет грабера для: {url}", None, False)
                ...
                continue

            try:
                await update.message.reply_text(f"""Process: 
                {url}""")
                f = await graber.grab_page(*required_fields)

                ...
                if gs.host_name == 'Vostro-3888':
                    ...
                    #self.driver.wait(5)   # <- ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Замедлитель
            except Exception as ex:
                logger.error(f"Ошибка получения полей товара",ex, False)
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
                continue
            products_list.append(product_data)    



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
        if not f.id_product:
            return {} # <- сбой при получении полей товара. Такое может произойти если вместо страницы товара попалась страница категории, при невнимательном составлении мехирона из комплектующих
        ...
        return {
            'product_title': f.name['language'][0]['value'].strip().replace("'", "\\'").replace('"', '\\"'),
            'product_id': f.id_product,
            'description_short': f.description_short['language'][0]['value'].strip().replace("'", "\\'").replace('"', '\\"').replace(';','<br>'),
            'description': f.description['language'][0]['value'].strip().replace("'", "\\'").replace('"', '\\"').replace(';','<br>'),
            'specification': f.specification['language'][0]['value'].strip().replace("'", "\\'").replace('"', '\\"').replace(';','<br>'),
            'local_image_path': str(f.local_image_path),
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
        model_command = Path(gs.path.endpoints / 'emil' / 'instructions' / f'command_instruction_mexiron_{lang}.md').read_text(encoding='UTF-8')
        # Request response from the AI model
        q = model_command + '\n' + str(products_list)
        response = await self.model.ask(q)
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

    async def create_report(self, data: dict, lang:str, html_file: Path, pdf_file: Path) -> bool:
        """Функция отправляет задание на создание мехирона в формате `html` и `pdf`.
        Если мехорон в pdf создался (`generator.create_report()` вернул True) - 
        отправить его боту
        """

        generator = ReportGenerator()

        if await generator.create_report(data, lang, html_file, pdf_file):
            # Проверка, существует ли файл и является ли он файлом
            if pdf_file.exists() and pdf_file.is_file():
                # Отправка боту PDF-файл через reply_document()
                await self.update.message.reply_document(document=pdf_file)
                return True
            else:
                logger.error(f"PDF файл не найден или не является файлом: {pdf_file}")
                return

