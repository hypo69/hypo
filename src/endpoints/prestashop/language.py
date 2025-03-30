## \file /src/endpoints/prestashop/language.py
# -*- coding: utf-8 -*-
#! .pyenv/bin/python3

"""
```rst
    ..:modlue: src.endpoints.prestashop.language
```
Модуль для работы с языками в PrestaShop.
===========================================
Модуль представляет интерфейс взаимодейлствия с сущностью `language` в cms `Prestashop` через `API Prestashop`
"""
import asyncio
from types import SimpleNamespace

import header

from src import gs
from src.endpoints.prestashop.api import PrestaShop
from src.logger.exceptions import PrestaShopException
from src.utils.printer import pprint as print
from src.logger.logger import logger

from typing import Optional


class PrestaLanguage(PrestaShop):
    """
    Класс, отвечающий за настройки языков магазина PrestaShop.

    Example:
        >>> prestalanguage = PrestaLanguage(API_DOMAIN=API_DOMAIN, API_KEY=API_KEY)
        >>> prestalanguage.add_language_PrestaShop('English', 'en')
        >>> prestalanguage.delete_language_PrestaShop(3)
        >>> prestalanguage.update_language_PrestaShop(4, 'Updated Language Name')
        >>> print(prestalanguage.get_language_details_PrestaShop(5))
    """
    
    def __init__(self, *args, **kwards):
        """
        Args:
            *args: Произвольные аргументы.
            **kwards: Произвольные именованные аргументы.

        Note:
            Важно помнить, что у каждого магазина своя нумерация языков.
            Я определяю языки в своих базах в таком порядке:
            `en` - 1;
            `he` - 2;
            `ru` - 3.
        """
        ...

    def get_lang_name_by_index(self, lang_index: int | str) -> str:
        """
        Функция извлекает ISO код азыка из магазина `Prestashop`

        Args:
            lang_index: Индекс языка в таблице PrestaShop.

        Returns:
            Имя языка ISO по его индексу в таблице PrestaShop.
        """
        try:
            return super().get('languagaes', resource_id=str(lang_index), display='full', io_format='JSON')
        except Exception as ex:
            logger.error(f'Ошибка получения языка по индексу {lang_index=}', ex)
            return ''

    def get_languages_schema(self) -> Optional[dict]:
        """Функция извлекает словарь актуальных языков дла данного магазина.

        Returns:
            Language schema or `None` on failure.

        Examples:
            # Возвращаемый словарь:
            {
                "languages": {
                        "language": [
                                        {
                                        "attrs": {
                                            "id": "1"
                                        },
                                        "value": ""
                                        },
                                        {
                                        "attrs": {
                                            "id": "2"
                                        },
                                        "value": ""
                                        },
                                        {
                                        "attrs": {
                                            "id": "3"
                                        },
                                        "value": ""
                                        }
                                    ]
                }
            }
        """
        try:
            response = self._exec('languages', display='full', io_format='JSON')
            return response
        except Exception as ex:
            logger.error(f'Error:', ex)
            return


async def main():
    """
    Example:
        >>> asyncio.run(main())
    """
    ...
    lang_class = PrestaLanguage()
    languagas_schema = await lang_class.get_languages_schema()
    print(languagas_schema)


if __name__ == '__main__':
    asyncio.run(main())
