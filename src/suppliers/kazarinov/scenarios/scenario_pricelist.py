## \file ../src/suppliers/kazarinov/scenarios/scenario_pricelist.py
# -*- coding: utf-8 -*-
#! /usr/share/projects/hypotez/venv/scripts python
"""! Module for handling Morlevi product data extraction and saving.

This module interacts with a web driver to scrape product details from given URLs, 
processes the data, and saves relevant product information, including images, locally.
"""

from ast import Return
import random
import asyncio
import time
from pathlib import Path
from types import SimpleNamespace
from typing import Optional
import requests
from bs4 import BeautifulSoup
from lxml import etree

import header
from src import gs
from src.product.product_fields import ProductFields
from src.webdriver import Driver
from src.ai.gemini import GoogleGenerativeAI
from src.advertisement.facebook.scenarios import post_message_title, upload_post_media, message_publish
from src.suppliers.morlevi.graber import async_grab_page as grab_morlevi_page
from src.suppliers.ksp.graber import async_grab_page as grab_ksp_page 
from src.suppliers.grandadvance.graber import async_grab_page as grab_grandadvance_page
from src.utils.jjson import j_loads, j_loads_ns, j_dumps
from src.utils.image import save_png, save_png_from_url
from src.utils.file import read_text_file, save_text_file, recursively_get_filepath
from src.utils import pprint
from src.logger import logger

locators = j_loads_ns(gs.path.src / 'suppliers' / 'morlevi' / 'locators' / 'product.json')


class Mexiron:
    """! Handles Morlevi product extraction, parsing, and saving processes."""
    
    d:Driver
    base_path:Path
    mexiron_title:str
    price:float
    timestamp:str = gs.now
    products_list:list = []
    product_titles_list:list = []
    gemini:GoogleGenerativeAI
    system_instruction:str = None


    def __init__(self, d: Driver):
        """Initializes the driver and base path."""
        self.d = d
        self.base_path = gs.path.google_drive / 'kazarinov' / 'mexironim' 

        system_instruction_path = gs.path.google_drive / 'kazarinov' / 'prompts' /  'buid_mexiron.txt'
        self.system_instruction: str = read_text_file(system_instruction_path)

        api_key = gs.credentials.gemini.kazarinov
        self.model = GoogleGenerativeAI(api_key = api_key, system_instruction = self.system_instruction, generation_config = {"response_mime_type": "application/json"})


    async def run_scenario(self, system_instruction: Optional[str] = None, price:Optional[str] = None, mexiron_name:str = None, urls:Optional[str | list] = None  ) -> bool:
        """Prepares product data by parsing and saving product pages.

        Args:
            price (str): Price to assign or process.
            urls (list | str): URL(s) to be processed.

        Returns:
            list[dict] | None: List of product data if successful, otherwise None.
        """
        ...
        self.base_path = self.base_path / mexiron_name  if mexiron_name else self.base_path / gs.now # <- в onetab после цены можно указать название сборки. Если не указано - подставляю `timestamp`

        self.system_instruction = system_instruction if system_instruction else self.system_instruction

        urls_list:list = [urls] if isinstance(urls, str) else urls
        if not urls_list:
            logger.debug("Нет ссылок на страницы с комплектующими")
            ...
            return
        
        
        product_fields_list: list = []
        product_titles_list: list = []
        supplier_prefix:str
        for url in urls_list:
            if url.startswith(('https://morlevi.co.il', 'https://www.morlevi.co.il')):
                supplier_prefix = 'morlevi'
            elif url.startswith(('https://ksp.co.il', 'https://www.ksp.co.il')):
                supplier_prefix = 'ksp'
            elif url.startswith(('https://grandadvance.co.il', 'https://www.grandadvance.co.il')):
                supplier_prefix = 'grandadvance'
            else:
                continue

            try:
                self.d.get_url(url)
            except Exception as ex:
                logger.debug(f"Ошибка открытия страницы {url}",ex)
                ...
                continue
            try:
                if supplier_prefix == 'morlevi':
                    f: ProductFields = await grab_morlevi_page(self.d)
                if supplier_prefix == 'ksp':
                    f: ProductFields = await grab_ksp_page(self.d)
                if supplier_prefix == 'grandadvance':
                    f: ProductFields = await grab_grandadvance_page(self.d)


            except Exception as ex:
                logger.debug(f"Ошибка получения полей товара", ex)
                ...
                continue

            if not f:
                logger.debug(f"Ошибка при обработке товара морлеви")
                ...
                continue
            
            f: ProductFields = await self.convert_product_fields(f)
            if not f:
                logger.debug(f"Ошибка конвертации {pprint(f)}")
                ...

            f: SimpleNamespace = SimpleNamespace(**f)
            if not j_dumps(f, self.base_path / 'products' / f'{f.product_id}.json' , ensure_ascii=False):
                logger.debug(f"не сохранился файл {f.product_id}.json")
                ...
            save_text_file(f.product_title, self.base_path / 'product_titles.txt', mode='a')
            product_titles_list.append({'product_id':f.product_id,
                                        'product_title':f.product_title,
                                        'product_description':f.product_description,
                                        'image_local_saved_path':f.image_local_saved_path})
            if not j_dumps(product_titles_list, self.base_path / 'products' / 'product_titles.json', ensure_ascii=False):
                logger.debug(f"не сохранился файл {f.product_id}.json")
                ...


        def ask_gemini(q, system_instruction, attempts=3):
            """Attempts to get translations from Gemini AI."""
            ...
            for attempt in range(attempts):
                response = self.ask_gemini(q, system_instruction=system_instruction or self.system_instruction)

                data: SimpleNamespace = j_loads_ns(response) # <- вернет False в случае ошибки

                if data:
                    if j_dumps(data, self.base_path / 'ai' / f'{gs.now}.json', ensure_ascii=False): # <- певая проверка валидности полученных данных
                        return data
                    else:
                        if attempts <0:
                            return
                        logger.warning(f"Invalid JSON received: {pprint(response)}")
                        ask_gemini(q, system_instruction, attempts - 1)
                else:
                    if attempts <0:
                        return
                    logger.warning(f"Invalid JSON received: {pprint(translations)}")
                    ask_gemini(q, system_instruction, attempts-1)


            logger.error("Failed to get valid response from Gemini AI after multiple attempts")
            return 
        ...

        response = ask_gemini(product_titles_list, self.system_instruction)
        if not response:
            logger.error('нет словаря')
            ...
            return
        
        try:
            ru:SimpleNamespace = response.ru
            he:SimpleNamespace = response.he
        except Exception as ex:
            try:
                response = ask_gemini(product_titles_list, self.system_instruction)
                ru:SimpleNamespace = response.ru
                he:SimpleNamespace = response.he
            except Exception as ex:
                logger.debug("Нет словаря")
                ...
                return
            
        service_images_path = recursively_get_filepath(gs.path.google_drive / 'kazarinov' / 'converted_images' / 'pastel' / 'bright', ['*.jpeg','*.jpg','*.png'])
        #service_image = random.choice(service_images_path)
        ...
        setattr(ru, 'language', 'ru')
        setattr(ru, 'currency', 'ils')
        setattr(ru, 'price', price)
        service_product_description_ru = f"""{read_text_file(gs.path.google_drive / 'kazarinov' / 'service_as_product_ru.txt')}
            \n ----------------- \n
            Общая цена за все: {price} шек.
            Для защитников страны — солдат ЦАХАЛ — специальные цены на все услуги! Спасибо вам за то, что вы защищаете нашу страну.
            """
        ru.products.append(SimpleNamespace (**{
            "product_id":"service",
            "product_title":"Сервисное обслуживание:",
            "product_description":service_product_description_ru,
            "image_local_saved_path": random.choice(service_images_path),
            "language":"ru",
            }))
        j_dumps(ru, self.base_path / f'{self.timestamp}_ru.json', ensure_ascii=False)

        
        setattr(he, 'language', 'he')
        setattr(he, 'currency', 'ils')
        setattr(he, 'price', price)
        service_product_description_he = f"""{read_text_file(gs.path.google_drive / 'kazarinov' / 'service_as_product_he.txt')}
            \n ----------------- \n
           מחיר כולל הכל {price} ש''ח
           . 

            """
        he.products.append(SimpleNamespace (**{
            "product_id":"service",
            "product_title":"שרות",
            "product_description":service_product_description_he,
            "image_local_saved_path": random.choice(service_images_path),
            "language":"he",
            }))
        j_dumps(he, self.base_path / f'{self.timestamp}_he.json', ensure_ascii=False)

        self.post_facebook(ru)
        self.post_facebook(he)
        
        return True



    def ask_gemini(self, q: str |list | dict, system_instruction: Optional[str] = None) -> dict:
        """Переводчик полей товара"""
        return self.model.ask(q, system_instruction)
        ...

    async def convert_product_fields(self, f: ProductFields) -> dict:
        """Prepares a product dictionary from product field data.

        Args:
            f (ProductFields): Object containing product field data.

        Returns:
            dict: Product information including title, description, ID, and image path.
        """
        image_path = self.base_path / 'images' / f'{f.id_product}.png'
        if isinstance(f.default_image_url,(Path, str)):
            if not await save_png_from_url(f.default_image_url, image_path):
                logger.debug(f"Картинка {image_path}\nне сохранилась на диске :(" )
                ...
        elif not await save_png(f.default_image_url, image_path):
            logger.debug(f"Картинка {image_path}\nне сохранилась на диске :(" )
            ...

        return {
            'product_title': str(f.name['language'][0]['value']).strip(),
            'product_id': f.id_product,
            'product_description': f.description['language'][0]['value'].strip(),
            'image_local_saved_path': str(image_path),
        }


    def post_facebook(self, mexiron:SimpleNamespace) -> bool:
        """"""
        ...
        self.d.get_url(r'https://www.facebook.com/profile.php?id=61566067514123')
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


