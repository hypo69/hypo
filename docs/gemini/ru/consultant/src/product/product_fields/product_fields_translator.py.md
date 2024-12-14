# Анализ кода модуля `product_fields_translator.py`

**Качество кода**
8
- Плюсы
    - Код имеет docstring для модуля и функций, что облегчает понимание его назначения и использования.
    - Используется `logger` для логирования ошибок, что помогает в отладке и мониторинге приложения.
    - Код структурирован и разбит на функции, каждая из которых выполняет определенную задачу.
- Минусы
    - Присутствуют неиспользуемые импорты, что может загромождать код.
    - Некоторые комментарии не соответствуют reStructuredText.
    - В логировании ошибок не везде используется f-строки для форматирования.
    - В функции `translate_presta_fields_dict` есть повторение кода и неявная обработка ошибок.
    - Некоторые комментарии внутри функций не несут полезной информации.

**Рекомендации по улучшению**

1.  **Импорты**: Удалить неиспользуемые импорты.
2.  **Документация**:
    - Переписать docstring модуля и функций в формате reStructuredText (RST).
    - Добавить описания параметров и возвращаемых значений для каждой функции.
3.  **Логирование**: Использовать f-строки для форматирования сообщений об ошибках в `logger.error`.
4.  **Обработка ошибок**: Убрать лишние блоки `try-except` и обрабатывать ошибки более гранулярно.
5.  **Код**:
    -   Упростить логику в `translate_presta_fields_dict` для повышения читаемости.
    -   Избегать повторения кода в циклах.
6.  **Комментарии**: Сделать комментарии более информативными и убрать бесполезные комментарии.

**Оптимизированный код**
```python
# -*- coding: utf-8 -*-
"""
Модуль для перевода полей товара на языки клиентской базы данных.
==================================================================

Этот модуль содержит функции для обработки и перевода полей товара,
полученных от поставщика, в соответствии с языковыми настройками
клиентской базы данных.

Функции модуля:
    - :func:`rearrange_language_keys`: Обновляет идентификаторы языков в данных о товаре.
    - :func:`translate_presta_fields_dict`: Переводит многоязычные поля товара.
"""
MODE = 'dev'

from pathlib import Path
from typing import List, Dict, Any
from src import gs
from src.utils.printer import pprint
from src.logger.logger import logger
from src.logger.exceptions import ProductFieldException
from src.utils.jjson import j_loads_ns
from src.db import get_translations_from_presta_translations_table, insert_new_translation_to_presta_translations_table


def rearrange_language_keys(presta_fields_dict: Dict, client_langs_schema: List[Dict], page_lang: str) -> Dict:
    """
    Обновляет идентификаторы языков в словаре `presta_fields_dict` на соответствующие
    идентификаторы из схемы клиентских языков при совпадении языка страницы.

    :param presta_fields_dict: Словарь полей товара.
    :type presta_fields_dict: dict
    :param client_langs_schema: Схема языков клиента.
    :type client_langs_schema: list or dict
    :param page_lang: Язык страницы.
    :type page_lang: str
    :return: Обновленный словарь `presta_fields_dict`.
    :rtype: dict
    """
    client_lang_id = None
    for lang in client_langs_schema:
        if lang['locale'] == page_lang or lang['iso_code'] == page_lang or lang['language_code'] == page_lang:
            client_lang_id = lang['id']
            break

    if client_lang_id is not None:
        for field in presta_fields_dict.values():
            if isinstance(field, dict) and 'language' in field:
                for lang_data in field['language']:
                    lang_data['attrs']['id'] = str(client_lang_id)  # Айдишники ОБЯЗАТЕЛЬНО строки. Связано с XML парсером

    return presta_fields_dict


def translate_presta_fields_dict(presta_fields_dict: Dict,
                                  client_langs_schema: List[Dict],
                                  page_lang: str = None) -> Dict:
    """
    Переводит многоязычные поля в соответствии со схемой значений `id` языка
    в базе данных клиента.

    Многоязычные поля содержат значения, полученные с сайта поставщика
    в виде словаря:

    .. code-block:: python

        {
            'language': [
                {'attrs': {'id': '1'}, 'value': value},
            ]
        }

    У клиента язык с ключом `id=1` может быть любым, в зависимости от
    того, на каком языке была изначально установлена PrestaShop.

    :param client_langs_schema: Словарь актуальных языков на клиенте.
    :type client_langs_schema: list or dict
    :param presta_fields_dict: Словарь полей товара, собранный со страницы поставщика.
    :type presta_fields_dict: dict
    :param page_lang: Язык страницы поставщика в коде en-US, ru-RU, he_HE. Если не задан,
                      функция пытается определить по тексту.
    :type page_lang: str, optional
    :return: Переведенный словарь полей товара.
    :rtype: dict
    """
    # Код переупорядочивает ключи таблицы
    presta_fields_dict = rearrange_language_keys(presta_fields_dict, client_langs_schema, page_lang)
    # Код получает переводы из таблицы переводов
    enabled_product_translations = get_translations_from_presta_translations_table(presta_fields_dict['reference'])
    
    if not enabled_product_translations or len(enabled_product_translations) < 1:
        # Если в таблице переводов нет такого перевода товара. Код добавляет текущий, как новый
        rec = record(presta_fields_dict)
        insert_new_translation_to_presta_translations_table(rec)
        return presta_fields_dict

    for client_lang in client_langs_schema:
        for translated_record in enabled_product_translations:
            # Код производит проверку соответствия языка перевода
            try:
                if client_lang['iso_code'] in translated_record.locale:
                    # Код записывает перевод из таблицы
                    for key in presta_fields_dict.keys():
                        if hasattr(translated_record, key):
                            presta_fields_dict[key] = {
                                'language': [{'attrs': {'id': str(client_lang['id'])},
                                              'value': getattr(translated_record, key)}]
                            }  # Айдишники ОБЯЗАТЕЛЬНО строки. Связано с XML парсером
            except Exception as ex:
                logger.error(f"Ошибка при переводе: {ex}\n client_lang = {pprint(client_lang)}")
                ...
    return presta_fields_dict


def record(data: Dict) -> Any:
        """
        TODO: Add docstring
        """
        class Record:
            def __init__(self, data: Dict):
                self.data = data
                for key, value in data.items():
                    setattr(self, key, value)
        return Record(data)
```