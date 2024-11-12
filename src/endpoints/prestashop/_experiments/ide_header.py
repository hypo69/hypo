## \file hypotez/src/endpoints/prestashop/_experiments/ide_header.py
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe # <- venv win
#! venv/bin/python # <- venv linux/macos
#! py # <- system win
#! /usr/bin/python # <- system linux/macos
## ~~~~~~~~~~~~~
""" module: src.endpoints.prestashop._experiments """
""" Файл заголовок, подключаемый к ide тестовым модулям """



import json
from pathlib import Path
import sys
import os
from attr import attr, attrs
from typing import Union

dir_root: Path = Path(os.getcwd()[:os.getcwd().rfind('hypotez') + 7])
sys.path.append(str(dir_root))  # Adding the root folder to sys.path
dir_src = Path(dir_root, 'src')
sys.path.append(str(dir_root))

# ---------------------------------
from src import gs
from src.utils import  pprint


# -----------------------------------


