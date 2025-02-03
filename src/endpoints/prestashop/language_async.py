## \file /src/endpoints/prestashop/language.py
# -*- coding: utf-8 -*-

#! .pyenv/bin/python3

"""
.. module:: src.endpoints.prestashop 
	:platform: Windows, Unix
	:synopsis:

"""


...
import asyncio
from types import SimpleNamespace


from src.endpoints.api.pre import PrestaShop
from src import gs
from src.utils.printer import  pprint
from .api import PrestaShop
import header
from src.logger.logger import logger
from src.logger.exceptions import PrestaShopException

from typing import Optional

class PrestaLanguageAync(PrestaShop):
    """ 
    Класс, отвечающий за настройки языков магазина PrestaShop.

    Пример использования класса:

    .. code-block:: python

        prestalanguage = PrestaLanguage(API_DOMAIN=API_DOMAIN, API_KEY=API_KEY)
        prestalanguage.add_language_PrestaShop('English', 'en')
        prestalanguage.delete_language_PrestaShop(3)
        prestalanguage.update_language_PrestaShop(4, 'Updated Language Name')
        print(prestalanguage.get_language_details_PrestaShop(5))
    """
    
    def __init__(self, *args, **kwards):
        """Класс интерфейс взаимодействия языками в Prestashop
        Важно помнить, что у каждого магазина своя нумерация языков
        :lang_string: ISO названия языка. Например: en, ru, he
        """
        ...

    async def get_lang_name_by_index(self, lang_index:int|str ) -> str:
        """Возвращает имя языка ISO по его индексу в таблице Prestashop"""
        try:
            return super().get('categories', resource_id=str(lang_index), display='full', io_format='JSON')
        except Exception as ex:
            logger.error(f"Ошибка получения языка по индексу {lang_index=}", ex)
            return ''

        """Возвращает номер языка из таблицы Prestashop по его имени ISO """
        ...
        try:
            lang_list = await self.get_lang_names()
            return lang_list
        except Exception as ex:
            logger.error(f"Ошибка получения языков")
            return []  
        
    async def get_languages_schema(self) -> dict:
        lang_dict = super().get_languages_schema()
        print(lang_dict) 


async def main():
    """"""
    ...
    lang_class = PrestaLanguageAync()
    languagas_schema = await  lang_class.get_languages_schema()
    print(languagas_schema)

if __name__ == '__main__':
    asyncio.run(main())

    
            

