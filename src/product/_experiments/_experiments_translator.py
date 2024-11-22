## \file hypotez/src/product/_experiments/_experiments_translator.py
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe
#! venv/bin/python/python3.12

"""
.. module: src.product._experiments 
	:platform: Windows, Unix
	:synopsis:

"""
MODE = 'development'

"""
	:platform: Windows, Unix
	:synopsis:

"""

"""
	:platform: Windows, Unix
	:synopsis:

"""

"""
  :platform: Windows, Unix

"""
"""
  :platform: Windows, Unix
  :platform: Windows, Unix
  :synopsis:
"""MODE = 'development'
  
""" module: src.product._experiments """


""" Переводы мультиязычных полей """
from pathlib import Path
from typing import Dict, List
import header
from src import gs, j_dumps, j_loads
from src.db import ProductTranslationsManager
from src.ai import translate
from src.endpoints.PrestaShop import PrestaShop
from src.webdriver import Driver
from header import ecat_api_credentials,emil_api_credentials
from src.db import ProductTranslationsManager
from src.translator import translate_product_fields as translator




""" ## Тестовый Клиент (emil-design.com,e-cat.co.il) """
#1. ecat_api_credentials
# presta_client_ecat = PrestaShop(ecat_api_credentials)
# presta_client_ecat_laguages_schema = presta_client_ecat.get_languages_schema()

#2. emil_api_credentials
presta_client_emil = PrestaShop(emil_api_credentials)
emil_laguages_schema = presta_client_emil.get_languages_schema() 


def rearrange_language_keys(presta_fields_dict: Dict, page_lang: str, client_langs_schema: list | dict) -> Dict:
    """Функция обновляет идентификатор языка в словаре presta_fields_dict на соответствующий идентификатор
    из схемы клиентских языков при совпадении языка страницы.

    Args:
        presta_fields_dict (Dict): Словарь полей товара.
        page_lang (str): Язык страницы.
        client_langs_schema (list | dict): Схема языков клиента.

    Returns:
        Dict: Обновленный словарь presta_fields_dict.
    """
    # Найти соответствующий идентификатор языка в схеме клиентских языков
    # Найти соответствующий идентификатор языка в схеме клиентских языков
    client_lang_id = None
    for lang in client_langs_schema:
        if lang['locale'] == page_lang:
            client_lang_id = lang['id']
            break

    # Если найден идентификатор языка в схеме клиентских языков
    if client_lang_id is not None:
        # Обновить значение атрибута id в словаре presta_fields_dict
        for field in presta_fields_dict.values():
            if isinstance(field, dict) and 'language' in field:
                for lang_data in field['language']:
                    lang_data['attrs']['id'] = str(client_lang_id)   # <- Эти айдишники ОБЯЗАТЕЛЬНО строки. Связано с XML парсером

    return presta_fields_dict



def translate_presta_fields_dict (presta_fields_dict: Dict, page_lang: str, client_langs_schema: list | dict) -> Dict:
    """ @Перевод мультиязычных полей в соответствии со схемой значений `id` языка в базе данных клиента
	    Функция получает на вход заполненный словарь полей. Мультиязычные поля содржат значения,
	    полученные с сайта поставщика в виде словаря 
	    ```
	    {
		    'language':[
					    {'attrs':{'id':'1'}, 'value':value},
					    ]
	    }
	    ```
	    У клиента язык с ключом `id=1` Может быть любым в зависимости от того на каком языке была 
	    изначально установлена PrestaShop. Чаще всего это английский, но это не правило.
	    Точные соответствия я получаю в схеме языков клиента 
	    locator_description
	    Самый быстрый способ узнать схему API языков - набрать в адресной строке браузера
	    https://API_KEY@mypresta.com/api/languages?display=full&io_format=JSON
	  
    @param client_langs_schema `dict` словарь актуальных языков на клиенте
    @param presta_fields_dict `dict` словарь полей товара собранный со страницы поставщика
    @param page_lang `str` язык страницы поставщика в коде en-US, ru-RU, he_HE
    @returns presta_fields_dict переведенный словарь полей товара
    """

    """ Переупорядывачиваю ключи таблицы. """
    presta_fields_dict = rearrange_language_keys (presta_fields_dict, page_lang, client_langs_schema)
    
    translations_manager = ProductTranslationsManager()
    search_filter = {'product_reference': presta_fields_dict['reference']}
    enabled_product_translations = translations_manager.select_record(**search_filter)

    if len(enabled_product_translations) <1:
        """ В таблице переводов нет такого перевода товара. Добавляю текущий, как новый """
        ...
        logger.warning("Нет переводов для товара ",presta_fields_dict['reference'])
        record = translator.build_record(presta_fields_dict, page_lang)
        translations_manager.insert(record)
        ...
        return presta_fields_dict

    for client_lang in client_langs_schema:
        for translated_record in enabled_product_translations:
            """ 
                        ПЕРЕВОД
            client codes from PrestaShop table
            'iso_code'    'en'    str
            'locale'    'en-US'    str
            'language_code'    'en-us'    str
            """
            try:
                if client_lang['iso_code'] in translated_record.locale: 
                    "Записываю перевод из таблицы"
                    for key in presta_fields_dict.keys():
                        if hasattr(translated_record, key):
                            presta_fields_dict[key] = {'language': [{'attrs': {'id': str(client_lang['id'])}, 'value': getattr(translated_record, key)}]}
                            # айдишники ОБЯЗАТЕЛЬНО строки. Связано с XML парсером
            except Exception as ex:
                logger.error(f"""Ошибка {ex}
                client_lang = {pprint(client_lang)}
                """)
                ...
						
    return presta_fields_dict


while True:
    """ Файлы создаются в директории tmp """
    presta_fields_dict = j_loads(Path(gs.path.src,'product','_test', '11267-1219_presta_fields_dict.json'))
    assist_fields_dict = j_loads(Path(gs.path.src,'product','_test', '11267-20100_assist_fields_dict.json'))
    presta_client = presta_client_emil
    presta_fields_dict = translate_presta_fields_dict(presta_fields_dict, emil_laguages_schema)
    ...
...