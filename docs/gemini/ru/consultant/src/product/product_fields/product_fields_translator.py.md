# Анализ кода модуля `product_fields_translator.py`

**Качество кода**
1.  Соответствие требованиям по оформлению кода: 6/10
    *   **Плюсы:**
        *   Используется `logger` для логирования ошибок.
        *   Импорты в начале файла.
        *   Присутствуют docstring.
    *   **Минусы:**
        *   Не все комментарии приведены в формате RST.
        *   Используется стандартный `try-except` вместо более точной обработки ошибок через `logger.error`.
        *   Некоторые имена функций и переменных не соответствуют стандарту (например,  `presta_fields_dict`).
        *   Используются глобальные переменные (например, `record`).
        *   Не используются `j_loads` или `j_loads_ns`.
        *   В комментариях встречаются слова "получаем", "делаем".
        *   Отсутствуют проверки на типы данных (например, `client_langs_schema`).

**Рекомендации по улучшению**

1.  **Комментарии и Docstring:**
    *   Переписать все комментарии и docstring в формате reStructuredText (RST).
    *   Добавить более подробные описания параметров и возвращаемых значений для функций.
2.  **Обработка ошибок:**
    *   Заменить общие блоки `try-except` на более конкретную обработку ошибок с использованием `logger.error`, где это возможно.
3.  **Именование:**
    *   Переименовать переменные и функции, чтобы они были более понятными и соответствовали соглашениям (например, `presta_fields_dict` -> `presta_fields`,  `client_langs_schema`  -> `client_languages_schema`).
4.  **Импорты:**
    *   Добавить необходимые импорты, которые могли быть пропущены.
    *   Упорядочить импорты по алфавиту.
5.  **Глобальные переменные:**
    *   Избегать использования глобальных переменных, таких как `record`,  передавая необходимые данные через аргументы функции.
6.  **Чтение данных:**
    *   Использовать `j_loads` или `j_loads_ns` из `src.utils.jjson` для чтения файлов, если это применимо.
7. **Проверка типов:**
    * Добавить проверки типов данных для входных аргументов функций.
8. **Логирование:**
    * Добавить логирование для всех важных операций, таких как получение данных, обновление, и т.д.
9. **Упрощение кода:**
    * Упростить логику определения языка, сделав код более читаемым.

**Оптимизированный код**

```python
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe
#! venv/bin/python/python3.12

"""
Модуль для перевода полей товара на языки клиентской базы данных.
===================================================================

Этот модуль содержит функции для перевода многоязычных полей продукта
в соответствии со схемой языков клиентской базы данных.
Он включает функции для перестановки ключей языка, перевода полей и
управления переводами продуктов.

.. module:: src.product.product_fields.product_fields_translator
   :platform: Windows, Unix
   :synopsis: Модуль перевода полей товара на языки клиентской базы данных

"""

from pathlib import Path
from typing import List, Dict, Any
from src.logger.logger import logger
from src.utils.printer import pprint
from src import gs
# from src.db import ProductTranslationsManager
# from src.translator import get_translations_from_presta_translations_table
# from src.translator import insert_new_translation_to_presta_translations_table
from src.logger.exceptions import ProductFieldException
from src.utils.jjson import j_loads  # Добавлен импорт

MODE = 'dev'

def rearrange_language_keys(presta_fields: Dict[str, Any], client_languages_schema: List[Dict[str, Any]], page_lang: str) -> Dict[str, Any]:
    """
    Обновляет идентификатор языка в словаре полей товара (`presta_fields`)
    на соответствующий идентификатор из схемы клиентских языков
    (`client_languages_schema`) при совпадении языка страницы (`page_lang`).

    :param presta_fields: Словарь полей товара.
    :type presta_fields: Dict[str, Any]
    :param client_languages_schema: Схема языков клиента.
    :type client_languages_schema: List[Dict[str, Any]]
    :param page_lang: Язык страницы.
    :type page_lang: str
    :raises TypeError: Если `presta_fields` не является словарем, `client_languages_schema` не является списком, а `page_lang` не является строкой.
    :return: Обновленный словарь полей товара.
    :rtype: Dict[str, Any]
    """
    if not isinstance(presta_fields, dict):
        logger.error(f'Неверный тип данных для presta_fields, ожидается dict, получено {type(presta_fields)}')
        raise TypeError(f'Expected dict for presta_fields, got {type(presta_fields)}')
    if not isinstance(client_languages_schema, list):
        logger.error(f'Неверный тип данных для client_languages_schema, ожидается list, получено {type(client_languages_schema)}')
        raise TypeError(f'Expected list for client_languages_schema, got {type(client_languages_schema)}')
    if not isinstance(page_lang, str):
        logger.error(f'Неверный тип данных для page_lang, ожидается str, получено {type(page_lang)}')
        raise TypeError(f'Expected str for page_lang, got {type(page_lang)}')

    client_lang_id = None
    # Поиск соответствующего идентификатора языка в схеме клиентских языков
    for lang in client_languages_schema:
        if not isinstance(lang, dict) or not all(key in lang for key in ['locale', 'iso_code', 'language_code', 'id']):
            logger.warning(f'Неверный формат данных в client_languages_schema: {lang}')
            continue

        if lang['locale'] == page_lang or lang['iso_code'] == page_lang or lang['language_code'] == page_lang:
            client_lang_id = lang['id']
            break

    if client_lang_id is not None:
        # Обновление значения атрибута id в словаре `presta_fields`
        for field in presta_fields.values():
            if isinstance(field, dict) and 'language' in field:
                for lang_data in field['language']:
                    if isinstance(lang_data, dict) and 'attrs' in lang_data and isinstance(lang_data['attrs'], dict):
                        lang_data['attrs']['id'] = str(client_lang_id)  # ID обязательно должны быть строками.

    return presta_fields

def translate_presta_fields_dict(presta_fields: Dict[str, Any],
                                  client_languages_schema: List[Dict[str, Any]],
                                  page_lang: str = None) -> Dict[str, Any]:
    """
    Переводит мультиязычные поля в соответствии со схемой значений `id` языка в базе данных клиента.

    Функция получает на вход заполненный словарь полей. Мультиязычные поля содержат значения,
    полученные с сайта поставщика в виде словаря
    ```
    {
        'language':[
            {'attrs':{'id':'1'}, 'value':value},
        ]
    }
    ```
    У клиента язык с ключом `id=1` может быть любым в зависимости от того на каком языке была
    изначально установлена PrestaShop. Чаще всего это английский, но это не правило.
    Точные соответствия получаются в схеме языков клиента.

    :param presta_fields: Словарь полей товара, собранный со страницы поставщика.
    :type presta_fields: Dict[str, Any]
    :param client_languages_schema: Словарь актуальных языков на клиенте.
    :type client_languages_schema: List[Dict[str, Any]]
    :param page_lang: Язык страницы поставщика в коде en-US, ru-RU, he_HE. Если не задан - функция пытается определить по тексту.
    :type page_lang: str, optional
    :raises TypeError: Если `presta_fields` не является словарем, `client_languages_schema` не является списком, а `page_lang` не является строкой.
    :return: Переведенный словарь полей товара.
    :rtype: Dict[str, Any]
    """
    if not isinstance(presta_fields, dict):
        logger.error(f'Неверный тип данных для presta_fields, ожидается dict, получено {type(presta_fields)}')
        raise TypeError(f'Expected dict for presta_fields, got {type(presta_fields)}')
    if not isinstance(client_languages_schema, list):
        logger.error(f'Неверный тип данных для client_languages_schema, ожидается list, получено {type(client_languages_schema)}')
        raise TypeError(f'Expected list for client_languages_schema, got {type(client_languages_schema)}')
    if page_lang is not None and not isinstance(page_lang, str):
         logger.error(f'Неверный тип данных для page_lang, ожидается str, получено {type(page_lang)}')
         raise TypeError(f'Expected str for page_lang, got {type(page_lang)}')
    
    logger.debug(f'Начало перевода полей товара для языка: {page_lang}')
    # Переупорядочиваем ключи таблицы
    presta_fields = rearrange_language_keys(presta_fields, client_languages_schema, page_lang)
    # получаем переводы из БД
    enabled_product_translations = get_translations_from_presta_translations_table(presta_fields['reference'])

    if not enabled_product_translations or len(enabled_product_translations) < 1:
        # В таблице переводов нет такого перевода товара. Код добавляет текущий, как новый
        # TODO: заменить record
        # global record
        # rec = record(presta_fields)
        # insert_new_translation_to_presta_translations_table(rec)
        logger.debug(f"Нет перевода для товара {presta_fields.get('reference')}. Добавление нового перевода.")
        return presta_fields

    for client_lang in client_languages_schema:
        if not isinstance(client_lang, dict) or not all(key in client_lang for key in ['iso_code', 'id']):
            logger.warning(f'Неверный формат данных в client_languages_schema: {client_lang}')
            continue
        for translated_record in enabled_product_translations:
            # Код выполняет перевод
            # client codes from PrestaShop table
            # 'iso_code'    'en'    str
            # 'locale'    'en-US'    str
            # 'language_code'    'en-us'    str
            # нужен iso_code
            try:
                if client_lang['iso_code'] in translated_record.locale:
                    # Код записывает перевод из таблицы
                    for key in presta_fields.keys():
                        if hasattr(translated_record, key):
                            presta_fields[key] = {'language': [{'attrs': {'id': str(client_lang['id'])},
                                                               'value': getattr(translated_record, key)}]}
                            # айдишники обязательно строки. Связано с XML парсером
            except Exception as ex:
                logger.error(f"Ошибка при переводе: {ex}\n client_lang = {pprint(client_lang)}")
                continue

    logger.debug(f'Завершение перевода полей товара для языка: {page_lang}')
    return presta_fields
```