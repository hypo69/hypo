## \file /src/endpoints/kazarinov/scenarios/_experiments/ask_model.py
# -*- coding: utf-8 -*-\

#! .pyenv/bin/python3

"""
Модуль для проверки валидности ответов от модели
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
import re
import header
from src import gs, logger
from src.ai.gemini.gemini import GoogleGenerativeAI
from src.utils.jjson import j_dumps, j_loads_ns,j_loads
from src.logger.logger import logger

test_directory:Path = gs.path.external_storage / 'kazarinov' / 'mexironim' / '24_12_07_19_06_40_508' 
products_in_test_dir:Path = test_directory /  'products'
products_list:list[dict] = j_loads(products_in_test_dir)

system_instruction = Path(gs.path.endpoints / 'kazarinov' / 'instructions' / 'system_instruction_mexiron.md').read_text(encoding='UTF-8')
command_instruction_ru = Path(gs.path.endpoints / 'kazarinov' / 'instructions' / 'command_instruction_mexiron_ru.md').read_text(encoding='UTF-8')
command_instruction_he = Path(gs.path.endpoints / 'kazarinov' / 'instructions' / 'command_instruction_mexiron_he.md').read_text(encoding='UTF-8')
api_key = gs.credentials.gemini.kazarinov
model = GoogleGenerativeAI(
                api_key=api_key,
                system_instruction=system_instruction,
                generation_config={'response_mime_type': 'application/json'}
            )
q_ru = command_instruction_ru + str(products_list)
q_he = command_instruction_he + str(products_list)

def model_ask(lang:str, attempts = 3) -> dict:
    """"""
    global model, q_ru, q_he

    response = model.ask(q_ru if lang == 'ru' else q_he)
    if not response:
        logger.error(f"Нет ответа от модели")
        ...
        return {}

    response_dict:dict = j_loads(response)
    if not response_dict:
        logger.error("Ошибка парсинга ")
        if attempts >1:
            model_ask(lang, attempts -1 )
        return {}

    return response_dict

response_ru_dict = model_ask('ru')
j_dumps(response_ru_dict,gs.path.external_storage / 'kazarinov' / 'mexironim' / '24_12_07_19_06_40_508' / f'ru_{gs.now}.json')
response_he_dict = model_ask('he')
j_dumps(response_he_dict, gs.path.external_storage / 'kazarinov' / 'mexironim' / '24_12_07_19_06_40_508' / f'he_{gs.now}.json')

