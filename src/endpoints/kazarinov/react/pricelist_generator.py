## \file ./src/endpoints/kazarinov/react/pricelist_generator.py
# -*- coding: utf-8 -*-
#! /venv/Scripts/python.exe
#! /usr/bin/python
#! /usr/share/projects/hypotez/venv/scripts python

#https://dev.to/kboskin/building-web-applications-with-react-and-python-2d8c

"""! Генератор HTML и PDF для мехиронов Казаринова

Описание работы:
- Конструктор `__init__`: Принимает шаблон, базовый путь, метку времени и язык.
- Метод `load_data`: Загружает данные из JSON-файла.
- Метод `generate_html`: Генерирует HTML с использованием Jinja2.
- Метод `save_html`: Сохраняет HTML в файл.
- Метод `generate_pdf`: Преобразует HTML в PDF.
- Метод `create_report`: Запускает полный цикл генерации отчёта.
"""
import header
from dataclasses import dataclass, field
from src import gs
import json
from pathlib import Path
from jinja2 import Environment, FileSystemLoader
import pdfkit
from src.utils.jjson import j_loads
from src.utils.file import read_text_file, save_text_file    
from src.utils.pdf import save_pdf
from src.utils.convertors.html import html2pdf
from src.utils.printer import pprint
from src.logger import logger
config = pdfkit.configuration(wkhtmltopdf= str( gs.path.bin / 'wkhtmltopdf' / 'files' / 'bin' / 'wkhtmltopdf.exe' ) )


@dataclass
class ReportGenerator:
    """!
    Класс для генерации HTML- и PDF-отчётов на основе данных из JSON.
    """

    template_path: str  = field(default_factory=lambda: str(gs.path.src / 'suppliers' / 'kazarinov' / 'react' / 'templates' / 'template.html'))

    env: Environment = field(default_factory=lambda: Environment(loader=FileSystemLoader('.')))

    def generate_html(self, data:dict ) -> str:
        """!
        Генерирует HTML-контент на основе шаблона и данных.

        Args:
            lang (str): Язык отчёта.

        Returns:
            str: HTML-контент.
        """
        #template = self.env.get_template(self.template_path)
        template_string = read_text_file(self.template_path)
        template = self.env.from_string(template_string)
        return template.render(**data)


    def create_report(self, data: dict, html_file:str| Path, pdf_file:str |Path) -> None:
        """!
        Полный цикл генерации отчёта.

        Args:
            lang (str): Язык отчёта.
        """
        html_content = self.generate_html(data)
        save_text_file(html_content, html_file)
        html2pdf(html_content,pdf_file)
        #save_pdf(html_content,pdf_file)
        # pdfkit.from_string(html_content, pdf_file, configuration=config, options={"enable-local-file-access": ""})
        # pdfkit.from_file(html_file, pdf_file, configuration=config, options={"enable-local-file-access": ""})
        # logger.info(f"Файлы созданы: {html_file} и {pdf_file}")



if __name__ == "__main__":
    base_path = gs.path.data / 'kazarinov' / 'mexironim' / '202410262326' 
    data:dict = j_loads(base_path / '202410262326_ru.json')
    html_file:Path = base_path / '202410262326_ru.html' 
    pdf_file:Path = base_path / '202410262326_ru.pdf' 
    r = ReportGenerator()
    r.create_report(data, html_file, pdf_file)
