#! /usr/bin/python
## \file /src/endpoints/kazarinov/_experiments/pricelist_generator.py
# -*- coding: utf-8 -*-
#! /usr/share/projects/hypotez/venv/scripts python
"""! HERE SHOULD BE A DESCRIPTION OF THE MODULE OPERATION ! 
https://chatgpt.com/share/672266a3-0048-800d-a97b-c38f647d496b
"""

from pathlib import Path
import header 
from src import gs

from src.endpoints.kazarinov.react import ReportGenerator
from src.utils.jjson import j_loads, j_loads_ns, j_dumps

base_path = gs.path.data / 'kazarinov' / 'mexironim' / '202410262326' 
data:dict = j_loads(base_path / '202410262326_he.json')
html_file:Path = base_path / '202410262326_he.html' 
pdf_file:Path = base_path / '202410262326_he.pdf' 
r = ReportGenerator()
r.create_report(data, html_file, pdf_file)
...