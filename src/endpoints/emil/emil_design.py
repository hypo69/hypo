## \file /src/endpoints/emil/emil_design.py
# -*- coding: utf-8 -*-
#! .pyenv/bin/python3

"""
.. module:: src.endpoints.emil 
	:platform: Windows, Unix
	:synopsis: Module for managing and processing images and promoting to Facebook and PrestaShop.

"""
from __future__ import annotations

from dataclasses import dataclass, field
import os
import asyncio
import time
from pathlib import Path
from types import SimpleNamespace
from typing import Optional
from dotenv import load_dotenv
load_dotenv()
import header
from header import __root__

# Сторонние библиотеки
from src import gs

# Веб-драйверы
from src.webdriver.driver import Driver
from src.webdriver.chrome import Chrome
from src.webdriver.firefox import Firefox
# TODO: Add drivers e.g. Edge, crawlee_python, playwright

# AI модели
from src.ai.gemini import GoogleGenerativeAI
from src.ai.openai.model import OpenAIModel

# Обработка товаров
from src.endpoints.prestashop.product import PrestaProduct
from src.endpoints.prestashop.language import PrestaLanguage
from src.endpoints.prestashop.product_fields import ProductFields

# Работа с соцсетями
from src.endpoints.advertisement.facebook.scenarios.post_message import (
    post_message,
    post_title,
    upload_media,
)

# Утилиты
from src.utils.file_async import read_text_file, save_text_file, get_filenames_from_directory
from src.utils.jjson import j_loads, j_loads_ns, j_dumps
from src.utils.image import get_image_bytes, get_raw_image_data
from src.utils.convertors.ns import ns2dict

# Логирование
from src.logger.logger import logger

# ---------------------------------
ENDPOINT: str = 'emil'
USE_ENV: bool = True # <- Определает откуда брать ключи. Если False - то из базы данных с паролями, иначе из .env

# ---------------------------------
@dataclass
class EmilDesign:
    """ Class for designing and promoting images through various platforms. """
    gemini: GoogleGenerativeAI = None
    openai: OpenAIModel = None
    base_path: Path = field(default_factory=lambda: gs.path.endpoints / ENDPOINT)
    config: SimpleNamespace = field(default_factory=lambda: j_loads_ns(gs.path.endpoints / ENDPOINT / f'{ENDPOINT}.json'))
    data_path: Path = field(init=False)
    gemini_api: str = os.getenv('GEMINI_API') if USE_ENV else gs.credentials.gemini.emil
    presta_api: str = os.getenv('PRESTA_API') if USE_ENV else gs.credentials.prestashop.emil_design.api_key
    presta_url: str = os.getenv('PRESTA_URL') if USE_ENV else gs.credentials.prestashop.emil_design.url

    def __post_init__(self):
        self.data_path = getattr(gs.path, self.config.storage, 'external_storage') / ENDPOINT

    async def describe_images(self, lang: str, gemini_model_name: str = 'gemini-1.5-flash'):
        """ Describe images based on the provided instruction and examples.
        Args:
            lang (str): Language code for processing the description.
            gemini_model_name (str, optional): Model name for Gemini. Defaults to 'gemini-1.5-flash'.
        """
        system_instruction: str = Path(self.base_path / 'instructions' / f'system_instruction.{lang}.md').read_text(encoding='UTF-8')
        prompt: str = Path(self.base_path / 'instructions' / f'hand_made_furniture.{lang}.md').read_text(encoding='UTF-8')
        furniture_categories: str = Path(self.base_path / 'categories' / 'main_categories_furniture.json').read_text(encoding='UTF-8').replace(r'\n', '').replace(r'\t', '')
        system_instruction = system_instruction + furniture_categories + prompt
        output_json: Path = Path(self.data_path / f'out_{gs.now}_{lang}.json')
        described_images_path: Path = self.data_path / 'described_images.txt'
        described_images: list = read_text_file(described_images_path, as_list=True) or []
        images_dir = self.data_path / 'images' / 'furniture_images'
        images_files_list: list = get_filenames_from_directory(images_dir)
        images_to_process = [img for img in images_files_list if str(images_dir / img) not in described_images]
        data: list = []

        use_openai: bool = False
        if use_openai:
            self.openai = OpenAIModel(system_instruction=system_instruction, assistant_id='asst_uDr5aVY3qRByRwt5qFiMDk43')

        use_gemini: bool = True
        if use_gemini:
            self.gemini = GoogleGenerativeAI(
                api_key=self.gemini_api,
                model_name=gemini_model_name,
                system_instruction=system_instruction,
                generation_config={'response_mime_type': 'application/json'}
            )

        for img in images_to_process:
            print(f"starting process file {img}\nsleep for 20 sec")
            time.sleep(20)
            raw_img_data = get_raw_image_data(images_dir / img)
            response = await self.gemini.describe_image(image=raw_img_data, mime_type='image/jpeg')
            if not response:
                logger.debug(f"Не удалось получить описание к {img=}")
                continue
            res_ns: SimpleNamespace = j_loads_ns(response)
            res_ns = res_ns[0] if isinstance(res_ns, list) else res_ns
            setattr(res_ns, 'local_image_path', str(Path(images_dir / img)))
            data.append(res_ns)
            j_dumps(data, output_json)
            described_images.append(str(images_dir / img))
            await save_text_file(described_images_path, described_images)


def main():
    emil = EmilDesign()
    asyncio.run(emil.upload_described_products_to_prestashop(lang='he'))
    asyncio.run(emil.describe_images(lang='he', gemini_model_name='gemini-1.5-flash'))

if __name__ == "__main__":
    main()

