## \file /src/endpoints/kazarinov/scenarios/_experiments/create_report.py
# -*- coding: utf-8 -*-\

#! .pyenv/bin/python3

"""
Модуль для проверки генерации прайслиста
==================================================================

```rst
.. module:: src.endpoints.kazarinov.scenarios._experiments 
	:platform: Windows, Unix
	:synopsis: Provides functionality for extracting, parsing, and processing product data from 
various suppliers. The module handles data preparation, AI processing, 
and integration with Facebook for product posting.
```

"""

from pathlib import Path

import header
from src import gs
from src.endpoints.kazarinov.pricelist_generator import ReportGenerator
from src.endpoints.kazarinov.scenarios._experiments.ask_model import *

report_generator = ReportGenerator()
html_file_he:Path = test_directory	/ 'he.html'
pdf_file_he:Path = test_directory	/ 'he.pdf'
html_file_ru:Path = test_directory	/ 'ru.html'
pdf_file_ru:Path = test_directory	/ 'ru.pdf'

report_generator.create_report(response_he_dict['he'], 'he', html_file_he, pdf_file_he)
report_generator.create_report(response_ru_dict['ru'], 'ru', html_file_ru, pdf_file_ru)
...