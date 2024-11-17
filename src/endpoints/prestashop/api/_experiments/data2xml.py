

""" Проверка валидности словаря престасшоп """
from pathlib import Path
import header
from src import gs, j_loads, j_dumps, save_text_file
from header import logger
from src.endpoints.PrestaShop.presta_apis.presta_python_api_v3 import dict2xml,xml2dict


"""Перед проверками загрузи свежий слловарь """
while True:
    try:
        data = j_loads(Path(gs.path.src,'PrestaShop','presta_apis','_test', 'presta_fields_dict.json'))
        xml = dict2xml.dict2xml(data)
        ...
    except Exception as ex:
        logger.error("XML", ex, True)
        ...