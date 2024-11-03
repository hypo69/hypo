## \file ../src/suppliers/kazarinov/scenarios/scenario_pricelist.py
# -*- coding: utf-8 -*-
#! /usr/share/projects/hypotez/venv/scripts python
"""! Module for handling suppliers (morlevi, grandadvance, ivory, ksp) product data extraction and saving."""

import asyncio
import random
import time
from pathlib import Path
from typing import Optional, List
from types import SimpleNamespace
from dataclasses import field

from src import gs
from src.product.product_fields import ProductFields
from src.webdriver import Driver
from src.ai.gemini import GoogleGenerativeAI
from src.advertisement.facebook.scenarios import (
    post_message_title, 
    upload_post_media, 
    message_publish
)
from src.suppliers.morlevi.graber import Graber as MorleviGraber
from src.suppliers.ksp.graber import Graber as KspGraber
from src.suppliers.ivory.graber import Graber as IvoryGraber
from src.suppliers.grandadvance.graber import Graber as GrandadvanceGraber
from src.suppliers.kazarinov.react import ReportGenerator
from src.utils.jjson import j_loads_ns, j_dumps
from src.utils.file import read_text_file, save_text_file, recursively_get_filepath
from src.utils.image import save_png_from_url, save_png
from src.utils import pprint
from src.logger import logger

class Mexiron:
    """! Handles Morlevi product extraction, parsing, and saving processes."""
    
    d: Driver
    base_path: Path
    mexiron_title: str
    price: float
    timestamp: str
    products_list: List = field(default_factory=list)  # Инициализация пустого списка для продуктов
    products_list: List = field(default_factory=list)  # Инициализация пустого списка заголовков продуктов
    model: GoogleGenerativeAI


    def __init__(self, d: Driver):
        """Initializes the driver and base path."""
        self.timestamp = gs.now
        self.d = d
        self.base_path = gs.path.google_drive / 'kazarinov' / 'mexironim' / self.timestamp

        system_instruction_path = gs.path.google_drive / 'kazarinov' / 'prompts' /  'buid_mexiron.txt'
        system_instruction: str = read_text_file(system_instruction_path)

        api_key = gs.credentials.gemini.kazarinov
        self.model = GoogleGenerativeAI(api_key = api_key, system_instruction = system_instruction, generation_config = {"response_mime_type": "application/json"})


    async def run_scenario(self, system_instruction: Optional[str] = None, price:Optional[str] = None, mexiron_name:str = None, urls:Optional[str | list] = None  ) -> bool:
        """Prepares product data by parsing and saving product pages.

        Args:
            mexiron_name (str): Я могу задать имя мехирона. Оно приходит в onetab после цены. Например, 'компьтер для тёти Любы'
            price (str): Price to assign or process.
            urls (list | str): URL(s) to be processed.

        Returns:
            list[dict] | None: List of product data if successful, otherwise None.
        """
        ...
        base_path = self.base_path   # <- в onetab после цены можно указать название сборки. Если не указано - подставляю `timestamp`

        urls_list:list = [urls] if isinstance(urls, str) else urls
        if not urls_list:
            logger.debug("Нет ссылок на страницы с комплектующими")
            ...
            return

        product_fields_list: list = []
        products_list: list = []
        ru:SimpleNamespace = SimpleNamespace()
        he:SimpleNamespace = SimpleNamespace()
        supplier_prefix:str
        
        for url in urls_list:
            graber = None # <- принимает значение грабера поставщика

            if url.startswith(('https://morlevi.co.il', 'https://www.morlevi.co.il')):
                graber  = MorleviGraber()
            elif url.startswith(('https://ksp.co.il', 'https://www.ksp.co.il')):
                graber  = KspGraber()
            elif url.startswith(('https://grandadvance.co.il', 'https://www.grandadvance.co.il')):
                graber  = GrandadvanceGraber()
            elif url.startswith(('https://ivory.co.il', 'https://www.ivory.co.il')):
                graber  = IvoryGraber()

            if not graber:
                continue

            try:
                self.d.get_url(url)
                f: ProductFields = await graber.grab_page(self.d)
            except Exception as ex:
                logger.debug(f"Ошибка открытия страницы {url}",ex)
                ...
                continue

            if not f:
                logger.debug(f"Не получил поля товaра {supplier_prefix} \n {url}")
                ...
                continue
            
            f: ProductFields = self.convert_product_fields(f)
            f: SimpleNamespace = SimpleNamespace(**f)
            if not f:
                logger.debug(f"Ошибка конвертации {pprint(f)}")
                ...

            
            if not j_dumps(f, base_path /  'products' / f'{f.product_id}.json' , ensure_ascii=False):
                logger.debug(f"не сохранился файл {f.product_id}.json")
                ...
            if not save_text_file(f.product_title, base_path  / 'product_titles.txt', mode='a'):
               logger.debug(f"не сохранилось имя товара {f.product_title=} \nв файл {base_path}/product_titles.txt")
               ...

            # prepare products_list for ask gemini
            products_list.append({'product_id': f.product_id,
                                        'name': f.product_title,
                                        'description_short': f.description_short,
                                        'description': f.description,
                                        'specification': f.specification,
                                        'local_saved_image': f.local_saved_image,
                                        })

            if not j_dumps(products_list, base_path / 'products.json', ensure_ascii=False):
                logger.debug(f"не сохранился файл {f.product_id}.json")
                ...


        def ask_and_repair(products_list:str, attemts:int = 3):
            if attemts < 1:
                return
            response = self.model.ask(products_list)
            if not response:
                logger.error("no response from gemini")
                ...
                ask_and_repair(products_list,attemts - 1)


            data: SimpleNamespace = j_loads_ns(response) # <- вернет False в случае ошибки

            if not data:
                logger.error(f"Error in data from gemini:{data}")
                ...
                ask_and_repair(products_list,attemts - 1)

                if not j_dumps(data, base_path / 'ai' / f'{gs.now}.json', ensure_ascii=False): # <- певая проверка валидности полученных данных
                    ...
                    ask_and_repair(products_list, attemts - 1)

            try:
                if hasattr(data,'ru'):
                    ru:SimpleNamespace = data.ru
                    if not ru:
                        ...
                        ask_and_repair(products_list, attemts-1)
                else:
                    ...
                    ask_and_repair(products_list, attemts-1)

                if hasattr(data,'he'):
                    he:SimpleNamespace = data.he
                    if not he:
                        ...
                        ask_and_repair(products_list, attemts-1)
                else:
                    ...
                    ask_and_repair(products_list, attemts-1)
                return ru, he
            except Exception as ex:
                logger.debug(f"ошибка словаря")
                ...
                return

        ru, he = ask_and_repair(products_list)    
        
        service_images_path = recursively_get_filepath(gs.path.google_drive / 'kazarinov' / 'converted_images' / 'for_pricelist', ['*.jpeg','*.jpg','*.png'])
        #service_image = random.choice(service_images_path)
        ...
        setattr(ru, 'id', self.timestamp)
        setattr(ru, 'language', 'ru')
        setattr(ru, 'currency', 'ils')
        setattr(ru, 'price', price)
        service_description_ru = f"""{read_text_file(gs.path.google_drive / 'kazarinov' / 'service_as_product_ru.txt')}
            \n ----------------- \n
            Общая цена за все: {price} шек.
            Для защитников страны — солдат ЦАХАЛ — специальные цены на все услуги! Спасибо вам за то, что вы защищаете нашу страну.
            """
        ru.products.append(SimpleNamespace (**{
            "product_id":"service",
            "product_title":"Сервисное обслуживание:",
            "description":service_description_ru,
            "local_saved_image": random.choice(service_images_path),
            "language":"ru",
            }))
        j_dumps(ru, base_path / f'{self.timestamp}_ru.json', ensure_ascii=False)

        setattr(he, 'id', self.timestamp) 
        setattr(he, 'language', 'he')
        setattr(he, 'currency', 'ils')
        setattr(he, 'price', price)
        service_description_he = f"""{read_text_file(gs.path.google_drive / 'kazarinov' / 'prompts' / 'service_as_product_he.txt')}
            \n ----------------- \n
           מחיר כולל הכל {price} ש''ח
           . 

            """
        he.products.append(SimpleNamespace (**{
            "product_id":"service",
            "product_title":"שרות",
            "description":service_description_he,
            "local_saved_image": random.choice(service_images_path),
            "language":"he",
            }))
        j_dumps(he, base_path / f'{self.timestamp}_he.json', ensure_ascii=False)

        self.create_report(base_path)
        #self.post_facebook(ru)
        #self.post_facebook(he)
        
        return True


    def convert_product_fields(self, f: ProductFields) -> dict:
        """Prepares a product dictionary from product field data.

        Args:
            f (ProductFields): Object containing product field data.

        Returns:
            dict: Product information including title, description, ID, and image path.
        """
        image_path = self.base_path /  'images' / f'{f.id_product}.png'
        if isinstance(f.default_image_url,(Path, str)):
            if not asyncio.run( save_png_from_url(f.default_image_url, image_path)):
                logger.debug(f"Картинка {image_path}\nне сохранилась на диске :(" )
                ...
        elif not asyncio.run(save_png(f.default_image_url, image_path)):
            logger.debug(f"Картинка {image_path}\nне сохранилась на диске :(" )
            ...

        return {
            'product_title': str(f.name['language'][0]['value']).strip(),
            'product_id': f.id_product,
            'description_short': f.description_short['language'][0]['value'].strip(),
            'description': f.description['language'][0]['value'].strip(),
            'specification': f.specification['language'][0]['value'].strip(),
            'local_saved_image': fr'file:///{str(image_path)}',
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

    def create_report(self, base_path):
        """"""
        ...
        generator = ReportGenerator( base_path = base_path, timestamp = self.timestamp )
        for lang in ['he','ru']:
            generator.create_report(lang)


