## \file /src/endpoints/kazarinov/react/report_generator.py
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



from argparse import OPTIONAL
import asyncio
from dataclasses import dataclass, field
import telebot
from itertools import filterfalse
from types import SimpleNamespace
from typing import Optional
import json
from pathlib import Path
from jinja2 import Environment, FileSystemLoader
import pdfkit

import header
from src import gs
from src.utils.jjson import j_loads
from src.utils.file import read_text_file, save_text_file    
from src.utils.convertors.html2pdf import html2pdf
from src.utils.convertors.html2docx  import html_to_docx
from src.utils.image import random_image
from src.utils.printer import pprint
from src.logger.logger import logger

# config = pdfkit.configuration(wkhtmltopdf= str( gs.path.bin / 'wkhtmltopdf' / 'files' / 'bin' / 'wkhtmltopdf.exe' ) )

##################################################################

ENDPOINT = 'kazarinov'

##################################################################

class ReportGenerator:
    """
    Класс для генерации HTML- и PDF-отчётов на основе данных из JSON.
    """
    if_need_html: bool
    if_need_pdf: bool
    if_need_docx: bool
    base_path:Path =  gs.path.external_storage / ENDPOINT
    html_path: Path|str = base_path / f'{gs.now}.html'
    pdf_path: Path|str = base_path / f'{gs.now}.pdf'
    docs_path: Path|str = base_path / f'{gs.now}.docx'
    html_content:str
    data:dict
    env: Environment = Environment(loader=FileSystemLoader('.'))

    def __init__(self, 
                 if_need_pdf:Optional[bool] = True, 
                 if_need_docx:Optional[bool] = True, 
            ):
        """Определение, какие форматы данных требуется вернуть"""
        self.if_need_pdf = if_need_pdf
        self.if_need_docx = if_need_docx
        

    async def create_reports(self,
                             bot: telebot.TeleBot,
                             chat_id: int,
                             data:dict,
                             maxiron_name:str,
                             lang:str, 
                             html_path:str|Path, 
                             pdf_path:str|Path, 
                             docx_path:str|Path) -> tuple:
        """Create ALL types: HTML, PDF, DOCX"""
        ...
        self.html_path = html_path
        self.pdf_path = pdf_path
        self.docx_path = docx_path
        self.bot = bot
        self.chat_id = chat_id

        self.html_content = await self.create_html_report(data, lang, self.html_path)

        if not self.html_content:
            return False


        if self.if_need_pdf:
            await self.create_pdf_report(self.html_content, lang, self.pdf_path)

        if self.if_need_docx:
            await self.create_docx_report(self.html_path, self.docx_path)

      
         
    def service_apendix(self, lang:str) -> dict:
        return  {
                "product_id":"00000",
                "product_name":"Сервис" if lang == 'ru' else "שירות",
                "specification":Path(gs.path.src / 'endpoints' / ENDPOINT / 'report_generator' / 'templates' / f'service_as_product_{lang}.html').read_text(encoding='UTF-8').replace('/n','<br>'),
                "image_local_saved_path":random_image(gs.path.external_storage / ENDPOINT / 'converted_images' )
                }

        ...

    async def create_html_report(self, data:dict, lang:str, html_path:Optional[ str|Path] ) -> str | None:
        """
        Генерирует HTML-контент на основе шаблона и данных.

        Args:
            lang (str): Язык отчёта.

        Returns:
            str: HTML-контент.
        """
        self.html_path = html_path if html_path and isinstance(html_path, str)  else Path(html_path) or self.html_path

        try:
            service_apendix = self.service_apendix(lang)
            data['products'].append(service_apendix)
            template:str = 'template_table_he.html' if lang == 'he' else  'template_table_ru.html'
            template_path: str  =  str(gs.path.endpoints / ENDPOINT / 'report_generator' / 'templates' / template)
            #template = self.env.get_template(self.template_path)
            template_string = Path(template_path).read_text(encoding = 'UTF-8')
            template = self.env.from_string(template_string)
            self.html_content:str = template.render(**data)

            try:
                Path(self.html_path).write_text(data = self.html_content, encoding='UTF-8')
            except Exception as ex:
                logger.error(f"Не удалось сохранить файл")
                return self.html_content
                

            logger.info(f"Файл HTML удачно сохранен в {html_path}")
            return self.html_content

        except Exception as ex:
            logger.error(f"Не удалось сгенерирпвать HTML файл {html_path}", ex)
            return 

    async def create_pdf_report(self, 
                                data: dict, 
                                lang:str, 
                                pdf_path:str |Path) -> bool:
        """
        Полный цикл генерации отчёта.

        Args:
            lang (str): Язык отчёта.
        """
        pdf_path = pdf_path if pdf_path and isinstance(pdf_path, (str,Path)) else self.pdf_path

        self.html_content = data if data else self.html_content

        from src.utils.pdf import PDFUtils
        pdf = PDFUtils()

        if not pdf.save_pdf_pdfkit(self.html_content, pdf_path):
            logger.error(f"Не скопмилировался PDF. Попробую docx")
            ...
            return False
        
        with open(pdf_path, 'rb') as f:
            self.bot.send_document(self.chat_id, f)
            


    async def create_docx_report(self, html_path:str|Path, docx_path:str|Path) -> bool :
        """Создаю мсйкрософт docx файл """

        if not html_to_docx(self.html_path, docx_path):
            logger.error(f"Не скопмилировался DOCX.")
            return False
        return True


def main(maxiron_name:str, lang:str) ->bool:
    
    external_storage: Path =  gs.path.external_storage / ENDPOINT / 'mexironim' /  maxiron_name
    data: dict = j_loads(external_storage / f'{maxiron_name}_{lang}.json')
    html_path: Path =  external_storage / f'{maxiron_name}_{lang}.html' 
    pdf_path: Path = external_storage / f'{maxiron_name}_{lang}.pdf'
    docx_path: Path = external_storage / f'{maxiron_name}_{lang}.docx'
    if_need_html: bool = True
    if_need_pdf: bool = True
    if_need_docx: bool = True 
    r = ReportGenerator(if_need_html, if_need_pdf, if_need_docx, html_path, pdf_path, docx_path)

    asyncio.run( r.create_reports( data,
                                    maxiron_name,
                                    lang, 
                                    html_path, 
                                    pdf_path, 
                                    docx_path, )   
                )

if __name__ == "__main__":
    maxiron_name = '250127221657987' # <- debug
    lang:str = 'ru'
    
    main(maxiron_name, lang)

