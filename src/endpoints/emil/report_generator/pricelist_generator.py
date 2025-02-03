## \file /src/endpoints/kazarinov/react/pricelist_generator.py
# -*- coding: utf-8 -*-

#! .pyenv/bin/python3

"""
.. module:: src.endpoints.kazarinov.react 
	:platform: Windows, Unix
	:synopsis: Генератор HTML и PDF для мехиронов Казаринова

Описание работы:
- Конструктор `__init__`: Принимает шаблон, базовый путь, метку времени и язык.
- Метод `load_data`: Загружает данные из JSON-файла.
- Метод `generate_html`: Генерирует HTML с использованием Jinja2.
- Метод `save_html`: Сохраняет HTML в файл.
- Метод `generate_pdf`: Преобразует HTML в PDF.
- Метод `create_report`: Запускает полный цикл генерации отчёта.

"""


#https://dev.to/kboskin/building-web-applications-with-react-and-python-2d8c


import header
import asyncio
from dataclasses import dataclass, field
from src import gs
import json
from pathlib import Path
from jinja2 import Environment, FileSystemLoader
import pdfkit
from src.utils.jjson import j_loads
from src.utils.file import read_text_file, save_text_file    
from src.utils.pdf import PDFUtils
from src.utils.convertors.html import html2pdf
from src.utils.image import random_image
from src.utils.printer import pprint
from src.logger.logger import logger

# config = pdfkit.configuration(wkhtmltopdf= str( gs.path.bin / 'wkhtmltopdf' / 'files' / 'bin' / 'wkhtmltopdf.exe' ) )


@dataclass
class ReportGenerator:
    """
    Класс для генерации HTML- и PDF-отчётов на основе данных из JSON.
    """

    env: Environment = field(default_factory=lambda: Environment(loader=FileSystemLoader('.')))

    async def generate_html(self, data:dict, lang:str ) -> str:
        """
        Генерирует HTML-контент на основе шаблона и данных.

        Args:
            lang (str): Язык отчёта.

        Returns:
            str: HTML-контент.
        """
        template:str = 'template_table_he.html' if lang == 'he' else  'template_table_ru.html'
        template_path: str  =  str(gs.path.endpoints / 'kazarinov' / 'pricelist_generator' / 'templates' / template)
        #template = self.env.get_template(self.template_path)
        template_string = Path(template_path).read_text(encoding = 'UTF-8')
        template = self.env.from_string(template_string)
        return template.render(**data)


    async def create_report(self, data: dict, lang:str, html_file:str| Path, pdf_file:str |Path) -> bool:
        """
        Полный цикл генерации отчёта.

        Args:
            lang (str): Язык отчёта.
        """

        # Обслуживание:
        service_dict:dict = {
                            "product_title":"Сервис" if lang == 'ru' else "שירות",
                            "specification":Path(gs.path.endpoints / 'kazarinov' / 'pricelist_generator' / 'templates' / f'service_as_product_{lang}.html').read_text(encoding='UTF-8').replace('/n','<br>'),
                            "image_local_saved_path":random_image(gs.path.external_storage / 'kazarinov' / 'converted_images' )
                            }
        data['products'].append(service_dict)

        html_content = await self.generate_html(data,lang)
        Path(html_file).write_text(data = html_content, encoding='UTF-8')
        pdf = PDFUtils()

        if not pdf.save_pdf_pdfkit(html_content,pdf_file):
            logger.error(f"Не скопмилировался PDF")
            ...
            return False
        return True

def main(mexiron:str,lang:str) ->bool:
    base_path:Path =  gs.path.external_storage / 'kazarinov' / 'mexironim' / mexiron
    data:dict = j_loads(base_path / f'{lang}.json')
    html_file:Path =  base_path / f'{mexiron}_{lang}.html' 
    pdf_file:Path = base_path / f'{mexiron}_{lang}.pdf'
    r = ReportGenerator()
    asyncio.run( r.create_report(data, lang, html_file, pdf_file)   )

if __name__ == "__main__":
    mexiron:str = '24_12_01_03_18_24_269'
    lang:str = 'ru'
    main(mexiron,lang)

