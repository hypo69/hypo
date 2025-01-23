from __future__ import annotations
## \file /src/endpoints/kazarinov/scenarios/scenario_pricelist.py
# -*- coding: utf-8 -*-\
#! .pyenv/bin/python3

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

from bs4 import BeautifulSoup
import requests
import asyncio
import random
import shutil
from pathlib import Path
from typing import Optional, List, Any
from types import SimpleNamespace
from dataclasses import field

import header
from header import __root__
from src import gs
from src.endpoints.prestashop.product_fields import ProductFields

from src.webdriver.driver import Driver
from src.webdriver.firefox import Firefox
from src.webdriver.playwright import Playwrid


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
from src.utils.image import save_image_from_url, save_image
from src.utils.convertors.unicode import decode_unicode_escape
from src.utils.printer import pprint
from src.logger.logger import logger


class QuotationBuilder:
    """
    Обрабатывает извлечение, разбор и сохранение данных о продуктах поставщиков.
    
    Attributes:
        driver (Driver): Экземпляр Selenium WebDriver.
        export_path (Path): Путь для экспорта данных.
        products_list (List[dict]): Список обработанных данных о продуктах.
    """
    ENDPOINT = 'kazarinov'
    base_path:Path = __root__ / 'src' / 'endpoints' / ENDPOINT

    try:
        config: SimpleNamespace = j_loads_ns(base_path / f'{ENDPOINT}.json')
    except Exception as ex:
        logger.error(f"Error loading configuration",ex)
        
        

    #driver: Playwrid = Playwrid()
    driver = Driver(Firefox)
    export_path: Path
    mexiron_name: str
    price: float
    timestamp: str
    products_list: List = field(default_factory=list)
    model: GoogleGenerativeAI
    
    translations: 'SimpleNamespace' =  j_loads_ns(base_path / 'translations' / 'mexiron.json')


    # Не все поля товара надо заполнять. Вот кортеж необходимых полей:
    required_fields:tuple = ('id_product',
                                'name',
                                'description_short',
                                'description',
                                'specification',
                                'local_image_path')

    def __init__(self, mexiron_name: Optional[str] = None):
        """
        Initializes Mexiron class with required components.

        Args:
            driver (Driver): Selenium WebDriver instance.
            mexiron_name (Optional[str]): Custom name for the Mexiron process.
        """


        self.timestamp = gs.now
        self.mexiron_name = mexiron_name or self.timestamp

        try:
            storage = gs.path.external_storage if self.config.storage == 'external_storage' else gs.path.data if self.config.storage == 'data' else gs.path.goog
            self.export_path = storage / 'kazarinov' / 'mexironim' / self.mexiron_name
        except Exception as ex:
            logger.error(f"Error constructing export path:",ex)
            ...
            return


        try:
            system_instruction:str = (self.base_path / 'instructions' / 'system_instruction_mexiron.md').read_text(encoding='UTF-8')
            api_key:str = gs.credentials.gemini.kazarinov
            self.model = GoogleGenerativeAI(
                api_key=api_key,
                system_instruction=system_instruction,
                generation_config={'response_mime_type': 'application/json'}
            )
        except Exception as ex:
            logger.error(f"Error loading instructions or API key:", ex)
            return



    def convert_product_fields(self, f: ProductFields) -> dict:
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
        product_name = '' if not f.name else  f.name['language'][0]['value'].strip().replace("'", "\\'").replace('"', '\\"')
        description = '' if not f.description else f.description['language'][0]['value'].strip().replace("'", "\\'").replace('"', '\\"').replace(';','<br>')
        description_short = '' if not f.description_short else f.description_short['language'][0]['value'].strip().replace("'", "\\'").replace('"', '\\"').replace(';','<br>')
        specification = '' if not f.specification else f.specification['language'][0]['value'].strip().replace("'", "\\'").replace('"', '\\"').replace(';','<br>')
        
        return {
            'product_name':product_name,
            'product_id': f.id_product,
            'description_short':description_short,
            'description': description,
            'specification': specification,
            'local_image_path': str(f.local_image_path),
        }

    async def save_product_data(self, product_data: dict) -> bool:
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

        model_command = Path(self.base_path / 'instructions' / f'command_instruction_mexiron_{lang}.md').read_text(encoding='UTF-8')
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

        await generator.create_report(data, lang, html_file, pdf_file)
        # Проверка, существует ли файл и является ли он файлом
        if pdf_file.exists() and pdf_file.is_file():
            return pdf_file
        else:
            logger.error(f"PDF файл не найден или не является файлом: {pdf_file}")
            return

