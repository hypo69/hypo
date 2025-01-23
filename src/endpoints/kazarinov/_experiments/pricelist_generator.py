## \file /src/endpoints/kazarinov/_experiments/pricelist_generator.py
# -*- coding: utf-8 -*-

#! .pyenv/bin/python3

"""
.. module:: src.endpoints.kazarinov._experiments 
	:platform: Windows, Unix
	:synopsis: Эксперименты с созданием pdf отчета

"""




"""  
https://chatgpt.com/share/672266a3-0048-800d-a97b-c38f647d496b
"""

from pathlib import Path
import header 
from src import gs

from src.endpoints.kazarinov.react import ReportGenerator
from src.utils.jjson import j_loads, j_loads_ns, j_dumps

base_path = gs.path.external_data / 'kazarinov' / 'mexironim' / '24_11_24_05_29_40_543' 
data:dict = j_loads(base_path / '202410262326_he.json')
html_file:Path = base_path / '202410262326_he.html' 
pdf_file:Path = base_path / '202410262326_he.pdf' 
r = ReportGenerator()
r.create_report(data, html_file, pdf_file)
...