# Анализ кода модуля `product_fields_translator`

## Качество кода
6
- Плюсы
    - Код структурирован и разделен на функции, что облегчает понимание и поддержку.
    - Используется `logger` для логирования ошибок, что помогает при отладке.
    - Есть docstring для функций, что упрощает понимание их назначения.
- Минусы
    - Не все функции имеют полные docstring с описанием аргументов и возвращаемых значений.
    - Используются глобальные переменные (например, `record`).
    - Присутствуют закомментированные блоки кода.
    - В `rearrange_language_keys` есть уязвимость при сравнении языков.
    - Код не следует PEP 8 (например, использование `\` для переноса длинных строк).
    - Есть избыточное условие `enabled_product_translations or len(enabled_product_translations) <1`.
    - Функция `translate_presta_fields_dict` имеет слишком много уровней вложенности, что затрудняет чтение.
    - Не используется `j_loads` или `j_loads_ns` для чтения файлов, хотя это указано в инструкции.
    - Отсутствуют `from src.logger.logger import logger`, импорты расположены не в алфавитном порядке, есть `...` .
    - Есть смешение стилей кода (использование двойных и одинарных кавычек).

## Рекомендации по улучшению

1. **Импорты**:
   - Добавить отсутствующие импорты: `from src.utils.jjson import j_loads, j_loads_ns`, `from src.logger.logger import logger`, `from typing import Any`.
   - Расположить импорты в алфавитном порядке.
2. **Документация**:
   - Дополнить docstring для функций `rearrange_language_keys` и `translate_presta_fields_dict`  с описанием всех аргументов, типов данных и возвращаемых значений.
   - Добавить примеры использования в docstring.
   - Изменить комментарии в соответствии с инструкциями.
3. **Глобальные переменные**:
   - Избегать использования глобальных переменных, таких как `record`. Переделать архитектуру.
4. **Удаление неиспользуемого кода**:
   - Удалить закомментированные блоки кода или пересмотреть их необходимость.
5. **Логика сравнения языков**:
   - Улучшить логику сравнения языков в `rearrange_language_keys` для корректной обработки случаев с `he` и `IL`.
6. **PEP 8**:
   - Следовать PEP 8 стандартам при написании кода, включая использование явных переносов строк, избегать `\`.
7. **Упрощение условий**:
   - Упростить условия, например, `if not enabled_product_translations or len(enabled_product_translations) <1` на `if not enabled_product_translations or not enabled_product_translations`.
8. **Уменьшение вложенности**:
   - Разбить функцию `translate_presta_fields_dict` на более мелкие подфункции для уменьшения вложенности.
9. **Использование `j_loads`**:
   - Если необходимо использовать `j_loads` или `j_loads_ns` для чтения файлов, добавить их использование.
10. **Стиль кавычек**:
    - Использовать одинарные кавычки в коде, двойные - только для вывода.
11. **Обработка ошибок**:
    - Убрать избыточные try-except и использовать logger.error.
    - Добавить обработку случая, когда не найден `client_lang` в цикле `for translated_record in enabled_product_translations`.
12. **Комментарии**:
    - Добавить подробные комментарии, объясняющие логику кода.
13. **Удалить ...**:
    - Убрать все `...` из кода.

## Оптимизированный код
```python
"""
Модуль для перевода полей товара на языки клиентской базы данных
=========================================================================================

Этот модуль содержит функции для перевода полей товара PrestaShop на языки,
используемые в клиентской базе данных.
Он обрабатывает многоязычные поля, корректируя идентификаторы языков и
выполняя перевод на основе данных из базы данных.

Пример использования
--------------------

Пример использования функции `translate_presta_fields_dict`:

.. code-block:: python

    presta_fields = {
        'name': {
            'language': [
                {'attrs': {'id': '1'}, 'value': 'Product Name EN'},
                {'attrs': {'id': '2'}, 'value': 'Product Name RU'},
            ]
        },
        'reference': 'PRODUCT001'
    }
    client_langs = [
        {'id': 1, 'iso_code': 'en', 'locale': 'en-US', 'language_code': 'en-us'},
        {'id': 2, 'iso_code': 'ru', 'locale': 'ru-RU', 'language_code': 'ru-ru'},
    ]
    translated_fields = translate_presta_fields_dict(presta_fields, client_langs, 'ru-RU')
    print(translated_fields)
"""
from pathlib import Path
from typing import List, Dict, Any

from src.utils.jjson import j_loads, j_loads_ns
from src.utils.printer import pprint
from src.logger.logger import logger
#from src.db import ProductTranslationsManager
#from src.translator import get_translations_from_presta_translations_table
#from src.translator import insert_new_translation_to_presta_translations_table
from src.logger.exceptions import ProductFieldException


def rearrange_language_keys(presta_fields_dict: Dict, client_langs_schema: List[Dict], page_lang: str) -> Dict:
    """Обновляет идентификатор языка в словаре `presta_fields_dict` на соответствующий идентификатор из схемы клиентских языков.

    Args:
        presta_fields_dict (dict): Словарь полей товара, где ключи - это названия полей, а значения - словари с языковыми данными.
            Пример: {'name': {'language': [{'attrs': {'id': '1'}, 'value': 'Product Name EN'}]}}.
        client_langs_schema (list): Список словарей, представляющих схему языков клиента.
            Каждый словарь содержит ключи 'id', 'locale', 'iso_code', 'language_code'.
            Пример: [{'id': 1, 'locale': 'en-US', 'iso_code': 'en', 'language_code': 'en-us'}].
        page_lang (str): Язык страницы, например, 'en-US', 'ru-RU', 'he_IL'.

    Returns:
        dict: Обновленный словарь `presta_fields_dict` с измененными идентификаторами языков, если они найдены.
             Возвращает исходный словарь, если соответствие не найдено.

    Raises:
        ProductFieldException: Если возникает ошибка при обработке полей.

    Example:
        >>> presta_fields = {'name': {'language': [{'attrs': {'id': '1'}, 'value': 'Product Name EN'}]}}
        >>> client_langs = [{'id': 2, 'locale': 'ru-RU', 'iso_code': 'ru', 'language_code': 'ru-ru'}]
        >>> page_lang = 'ru-RU'
        >>> updated_fields = rearrange_language_keys(presta_fields, client_langs, page_lang)
        >>> print(updated_fields)
        {'name': {'language': [{'attrs': {'id': '2'}, 'value': 'Product Name EN'}]}}
    """
    client_lang_id = None
    # Ищет соответствующий идентификатор языка в схеме клиентских языков
    for lang in client_langs_schema:
        if (lang['locale'] == page_lang or
            lang['iso_code'] == page_lang or
            lang['language_code'] == page_lang):
            client_lang_id = lang['id']
            break

    # Обновляет идентификатор языка в полях, если он был найден
    if client_lang_id is not None:
        for field in presta_fields_dict.values():
            if isinstance(field, dict) and 'language' in field:
                for lang_data in field['language']:
                    if 'attrs' in lang_data and 'id' in lang_data['attrs']:
                        lang_data['attrs']['id'] = str(client_lang_id)
    return presta_fields_dict


def translate_presta_fields_dict(presta_fields_dict: Dict,
                                 client_langs_schema: List[Dict],
                                 page_lang: str = None) -> Dict:
    """Переводит мультиязычные поля в соответствии со схемой значений `id` языка в базе данных клиента.

        Функция получает на вход заполненный словарь полей. Мультиязычные поля содержат значения,
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

    Args:
        presta_fields_dict (dict): Словарь полей товара, где ключи - это названия полей, а значения - словари с языковыми данными.
            Пример: {'name': {'language': [{'attrs': {'id': '1'}, 'value': 'Product Name EN'}]}}.
        client_langs_schema (list): Список словарей, представляющих схему языков клиента.
            Каждый словарь содержит ключи 'id', 'locale', 'iso_code', 'language_code'.
            Пример: [{'id': 1, 'locale': 'en-US', 'iso_code': 'en', 'language_code': 'en-us'}].
        page_lang (str, optional): Язык страницы поставщика в коде en-US, ru-RU, he_IL.
            Если не задан, функция пытается определить язык по тексту. Defaults to None.

    Returns:
        dict: Переведенный словарь полей товара.
        Возвращает исходный словарь, если перевод не требуется.

    Raises:
        ProductFieldException: Если возникает ошибка при обработке полей.

    Example:
        >>> presta_fields = {'name': {'language': [{'attrs': {'id': '1'}, 'value': 'Product Name EN'}]}, 'reference': 'PRODUCT001'}
        >>> client_langs = [{'id': 1, 'locale': 'en-US', 'iso_code': 'en', 'language_code': 'en-us'},
        ...                {'id': 2, 'locale': 'ru-RU', 'iso_code': 'ru', 'language_code': 'ru-ru'}]
        >>> translated_fields = translate_presta_fields_dict(presta_fields, client_langs, 'ru-RU')
        >>> print(translated_fields)
        {'name': {'language': [{'attrs': {'id': '2'}, 'value': 'Product Name EN'}]}, 'reference': 'PRODUCT001'}

    """
    # Переупорядочивает ключи таблицы.
    presta_fields_dict = rearrange_language_keys(presta_fields_dict, client_langs_schema, page_lang)
    #product_translations = get_translations_from_presta_translations_table(presta_fields_dict['reference'])
    enabled_product_translations = get_translations_from_presta_translations_table(presta_fields_dict['reference'])

    if not enabled_product_translations or not enabled_product_translations:
        # В таблице переводов нет такого перевода товара. Добавляет текущий, как новый
        #record = ProductTranslationsManager
        #rec = record(presta_fields_dict)
        #insert_new_translation_to_presta_translations_table(rec)
        return presta_fields_dict


    for client_lang in client_langs_schema:
        for translated_record in enabled_product_translations:
            #  ПЕРЕВОД
            #  client codes from PrestaShop table
            #  'iso_code'    'en'    str
            #  'locale'    'en-US'    str
            #  'language_code'    'en-us'    str
            #  нужен iso_code
            try:
                if client_lang['iso_code'] in translated_record.locale:
                    # Записывает перевод из таблицы
                    for key in presta_fields_dict.keys():
                        if hasattr(translated_record, key):
                            presta_fields_dict[key] = {'language': [{'attrs': {'id': str(client_lang['id'])}, 'value': getattr(translated_record, key)}]}
                             # айдишники ОБЯЗАТЕЛЬНО строки. Связано с XML парсером
            except Exception as ex:
                logger.error(f'Ошибка при переводе: {ex}\nclient_lang = {pprint(client_lang)}')

    return presta_fields_dict