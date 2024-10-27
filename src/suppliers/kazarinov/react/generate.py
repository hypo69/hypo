## \file ../src/suppliers/kazarinov/react/generate.py
# -*- coding: utf-8 -*-
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
from venv import logger
import header
from src import gs
import json
from pathlib import Path
from jinja2 import Environment, FileSystemLoader
import pdfkit
from src.utils.jjson import j_loads
from src.utils.file import save_text_file
from dataclasses import dataclass, field

@dataclass
class ReportGenerator:
    """!
    Класс для генерации HTML- и PDF-отчётов на основе данных из JSON.
    """
    
    #template_path: str | Path = field(default_factory=lambda: gs.path.src / 'suppliers' / 'kazarinov' / 'react' / 'templates' / 'template.html')                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    #
    template_path: str | Path = field(default_factory=lambda:  'templates/template.html')                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    #
    base_path: str | Path = field(default="")
    timestamp: str = field(default="")
    env: Environment = field(default_factory=lambda: Environment(loader=FileSystemLoader('.')))

    def generate_html(self, lang: str) -> str:
        """!
        Генерирует HTML-контент на основе шаблона и данных.

        Args:
            lang (str): Язык отчёта.

        Returns:
            str: HTML-контент.
        """
        data = j_loads(self.base_path / f'{self.timestamp}_{lang}.json')
        #template = self.env.get_template(self.template_path.name)
        template = self.env.get_template(self.template_path)
        return template.render(**data)

    def save_html(self, html_content: str, lang: str) -> bool:
        """!
        Сохраняет HTML-контент в файл.

        Args:
            html_content (str): HTML-контент.
            lang (str): Язык отчёта.
        """
        output_html = f"{self.base_path}/{self.timestamp}_{lang}.html"
        if not save_text_file(html_content, output_html):
            logger.debug(f"{output_html=} не сохранился на диске")
            return False
        return True

    def generate_pdf(self, lang: str) -> None:
        """!
        Генерирует PDF из HTML-файла.

        Args:
            lang (str): Язык отчёта.
        """
        output_html = f"{self.base_path}/{self.timestamp}/{self.timestamp}_{lang}.html"
        output_pdf = f"{self.base_path}/{self.timestamp}/{self.timestamp}_{lang}.pdf"
        pdfkit.from_file(output_html, output_pdf)

    def create_report(self, lang: str) -> None:
        """!
        Полный цикл генерации отчёта.

        Args:
            lang (str): Язык отчёта.
        """
        html_content = self.generate_html(lang)
        self.save_html(html_content, lang)
        self.generate_pdf(lang)
        print(f"Файлы созданы: {self.base_path}/{self.timestamp}/{self.timestamp}_{lang}.html и {self.base_path}/{self.timestamp}/{self.timestamp}_{lang}.pdf")

# Примеры
def generate_reports_for_languages(base_path: str, timestamp: str, languages: list[str]) -> None:
    """!
    Генерирует отчёты для нескольких языков.

    Args:
        base_path (str): Базовый путь для выходных файлов.
        timestamp (str): Метка времени.
        languages (list[str]): Список языков.
    """
    generator = ReportGenerator(base_path=base_path, timestamp=timestamp)
    for lang in languages:
        generator.create_report(lang)

if __name__ == "__main__":
    generate_reports_for_languages(
        base_path='/path/to/reports',
        timestamp='2024-10-24',
        languages=['ru', 'he']
    )
