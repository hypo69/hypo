## \file /src/endpoints/prestashop/language.py
# -*- coding: utf-8 -*-

#! .pyenv/bin/python3

"""
.. module:: src.endpoints.prestashop 
	:platform: Windows, Unix
	:synopsis:

"""
import asyncio
from types import SimpleNamespace

import header

from src import gs
from src.endpoints.prestashop.api import PrestaShop
from src.logger.exceptions import PrestaShopException
from src.utils.printer import  pprint as print
from src.logger.logger import logger

from typing import Optional

class PrestaLanguage(PrestaShop):
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

    def get_lang_name_by_index(self, lang_index:int|str ) -> str:
        """Возвращает имя языка ISO по его индексу в таблице Prestashop"""
        try:
            return super().get('languagaes', resource_id=str(lang_index), display='full', io_format='JSON')
        except Exception as ex:
            logger.error(f"Ошибка получения языка по индексу {lang_index=}", ex)
            return ''

        """Возвращает номер языка из таблицы Prestashop по его имени ISO """
        ...
        
    def get_languages_schema(self) -> Optional[dict]:
        """Get the schema for languages.

        :return: Language schema or `None` on failure.
        :rtype: dict
        """
        try:
            response = self._exec('languages', display='full', io_format='JSON')
            return response
        except Exception as ex:
            logger.error(f'Error:', ex)
            return


async def main():
    """"""
    ...
    lang_class = PrestaLanguageAync()
    languagas_schema = await  lang_class.get_languages_schema()
    print(languagas_schema)

if __name__ == '__main__':
    asyncio.run(main())

    
            

