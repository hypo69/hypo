# Анализ кода модуля `product_fields_translator.py`

**Качество кода**
8
-  Плюсы
    - Код в целом структурирован и выполняет поставленную задачу.
    - Используется `logger` для логирования ошибок.
    - Присутствует docstring для функций.
-  Минусы
    -  Не все комментарии и docstring написаны в формате reStructuredText (RST).
    -  В коде присутствуют закомментированные строки, которые следует удалить.
    -  Используется глобальная переменная `record`, что не является хорошей практикой.
    -  Используются стандартные `try-except`, которые можно заменить на обработку ошибок с помощью `logger.error`.
    -  Не хватает проверок типов входных данных для функций.
    -  Необходимо добавить отсутствующие импорты.
    -  Необходимо убрать лишние комментарии, такие как ` # <- оч плохо А если he или IL?`
    -  Стоит пересмотреть использование `enabled_product_translations`, т.к. проверка на `if not enabled_product_translations or enabled_product_translations or len(enabled_product_translations) <1:` выглядит избыточной.

**Рекомендации по улучшению**

1.  **Документация**:
    -   Переписать docstring и комментарии в формате RST, включая описания параметров, возвращаемых значений и примеры использования.
    -   Добавить docstring для модуля.
2.  **Импорты**:
    -   Добавить отсутствующие импорты.
3.  **Обработка ошибок**:
    -   Использовать `logger.error` для обработки исключений вместо `try-except` блоков.
4.  **Глобальные переменные**:
    -   Избегать использования глобальных переменных, таких как `record`.
5.  **Проверки типов**:
    -   Добавить проверки типов для аргументов функций.
6.  **Удаление лишнего кода**:
    -   Удалить закомментированные строки.
    -   Пересмотреть логику с `enabled_product_translations`.
7.  **Форматирование**:
    -   Привести код в соответствие с PEP8.

**Оптимизированный код**

```python
# -*- coding: utf-8 -*-
"""
Модуль для перевода полей товара на языки клиентской базы данных.
===================================================================

Этот модуль содержит функции для перевода полей товара, полученных от поставщика,
на языки, соответствующие клиентской базе данных. Он обрабатывает мультиязычные поля,
где каждое значение связано с определенным языковым идентификатором.

Функции используют схему языков клиента для корректного сопоставления идентификаторов
и обеспечивают правильное отображение информации о товарах на разных языках.
"""

from pathlib import Path
from typing import List, Dict, Any
from src.utils.jjson import j_loads, j_loads_ns
from src import gs
from src.utils.printer import pprint
from src.logger.logger import logger
from src.db import ProductTranslationsManager # <- Добавлен импорт
from src.translator import get_translations_from_presta_translations_table, insert_new_translation_to_presta_translations_table # <- Добавлен импорт
from src.logger.exceptions import ProductFieldException
from collections import namedtuple  # <- Добавлен импорт

record = namedtuple('record', ['reference', 'description', 'description_short', 'name']) #  <- Исправлена глобальная переменная


def rearrange_language_keys(presta_fields_dict: Dict, client_langs_schema: List[Dict], page_lang: str) -> Dict:
    """
    Обновляет идентификаторы языка в словаре `presta_fields_dict` на соответствующие идентификаторы
    из схемы клиентских языков при совпадении языка страницы.

    :param presta_fields_dict: Словарь полей товара.
    :type presta_fields_dict: dict
    :param client_langs_schema: Схема языков клиента.
    :type client_langs_schema: list[dict]
    :param page_lang: Язык страницы.
    :type page_lang: str
    :raises TypeError: Если `presta_fields_dict` не является словарем, или `client_langs_schema` не список, или `page_lang` не строка.
    :return: Обновленный словарь `presta_fields_dict`.
    :rtype: dict
    """
    if not isinstance(presta_fields_dict, dict):
        logger.error(f'Неверный тип данных для presta_fields_dict: {type(presta_fields_dict)}')
        raise TypeError(f'Expected dict, got {type(presta_fields_dict)}')
    if not isinstance(client_langs_schema, list):
         logger.error(f'Неверный тип данных для client_langs_schema: {type(client_langs_schema)}')
         raise TypeError(f'Expected list, got {type(client_langs_schema)}')
    if not isinstance(page_lang, str):
        logger.error(f'Неверный тип данных для page_lang: {type(page_lang)}')
        raise TypeError(f'Expected str, got {type(page_lang)}')

    client_lang_id = None
    for lang in client_langs_schema:
        if not isinstance(lang, dict):
            logger.error(f'Неверный тип данных в client_langs_schema: {type(lang)}')
            continue
        if (lang.get('locale') == page_lang or
            lang.get('iso_code') == page_lang or
            lang.get('language_code') == page_lang):
            client_lang_id = lang.get('id')
            break

    if client_lang_id is not None:
        for field in presta_fields_dict.values():
             if isinstance(field, dict) and 'language' in field:
                for lang_data in field['language']:
                    if isinstance(lang_data, dict) and 'attrs' in lang_data:
                        lang_data['attrs']['id'] = str(client_lang_id)
    return presta_fields_dict


def translate_presta_fields_dict(presta_fields_dict: Dict,
                                  client_langs_schema: List[Dict],
                                  page_lang: str = None) -> Dict:
    """
    Переводит мультиязычные поля в соответствии со схемой значений `id` языка в базе данных клиента.

    Функция получает на вход словарь полей товара. Мультиязычные поля содержат значения,
    полученные с сайта поставщика в виде словаря:

    .. code-block:: python

        {
            'language':[
                {'attrs':{'id':'1'}, 'value':value},
                ]
        }

    У клиента язык с ключом `id=1` может быть любым, в зависимости от того, на каком языке
    была изначально установлена PrestaShop. Чаще всего это английский, но это не правило.
    Точные соответствия получаются в схеме языков клиента.

    Самый быстрый способ узнать схему API языков - набрать в адресной строке браузера:
    https://API_KEY@mypresta.com/api/languages?display=full&io_format=JSON

    :param client_langs_schema: Словарь актуальных языков на клиенте.
    :type client_langs_schema: list[dict]
    :param presta_fields_dict: Словарь полей товара, собранный со страницы поставщика.
    :type presta_fields_dict: dict
    :param page_lang: Язык страницы поставщика в коде en-US, ru-RU, he_HE.
    Если не задан, функция пытается определить по тексту.
    :type page_lang: str, optional
    :raises TypeError: Если `presta_fields_dict` не является словарем, или `client_langs_schema` не список.
    :return: Переведенный словарь полей товара.
    :rtype: dict
    """

    if not isinstance(presta_fields_dict, dict):
        logger.error(f'Неверный тип данных для presta_fields_dict: {type(presta_fields_dict)}')
        raise TypeError(f'Expected dict, got {type(presta_fields_dict)}')
    if not isinstance(client_langs_schema, list):
         logger.error(f'Неверный тип данных для client_langs_schema: {type(client_langs_schema)}')
         raise TypeError(f'Expected list, got {type(client_langs_schema)}')

    presta_fields_dict = rearrange_language_keys(presta_fields_dict, client_langs_schema, page_lang)
    enabled_product_translations = get_translations_from_presta_translations_table(presta_fields_dict.get('reference'))

    if not enabled_product_translations:
        rec = record(presta_fields_dict.get('reference'),
                     presta_fields_dict.get('description'),
                     presta_fields_dict.get('description_short'),
                     presta_fields_dict.get('name'))

        insert_new_translation_to_presta_translations_table(rec)
        return presta_fields_dict

    for client_lang in client_langs_schema:
         if not isinstance(client_lang, dict):
              logger.error(f'Неверный тип данных в client_langs_schema: {type(client_lang)}')
              continue
         for translated_record in enabled_product_translations:
            try:
                if not hasattr(translated_record, 'locale'):
                     logger.error(f'Объект {translated_record} не имеет атрибута "locale"')
                     continue
                if client_lang.get('iso_code') in translated_record.locale:
                   for key in presta_fields_dict.keys():
                        if hasattr(translated_record, key):
                            presta_fields_dict[key] = {'language': [{'attrs': {'id': str(client_lang.get('id'))},
                                                                    'value': getattr(translated_record, key)}]}
            except Exception as ex:
                logger.error(f"""Ошибка {ex}\n
                client_lang = {pprint(client_lang)}\n
                """)
                ...
    return presta_fields_dict
```