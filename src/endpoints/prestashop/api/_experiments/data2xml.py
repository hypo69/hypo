## \file hypotez/src/endpoints/prestashop/api/_experiments/data2xml.py
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe # <- venv win
#! venv/bin/python # <- venv linux/macos
#! py # <- system win
#! /usr/bin/python # <- system linux/macos
## ~~~~~~~~~~~~~
""" module: src.endpoints.prestashop.api._experiments """
""" Проверка валидности словаря престасшоп """
from pathlib import Path
import header
from header import gs, j_loads, j_dumps, save_text_file
from header import logger
from src.endpoints.prestashop.presta_apis.presta_python_api_v3 import dict2xml,xml2dict


"""Перед проверками загрузи свежий слловарь """
while True:
    try:
        data = j_loads(Path(gs.path.src,'prestashop','presta_apis','_test', 'presta_fields_dict.json'))
        xml = dict2xml.dict2xml(data)
        ...
    except Exception as ex:
        logger.error("XML", ex, True)
        ...