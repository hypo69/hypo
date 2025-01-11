# <input code>

```python
## \file hypotez/src/product/product_fields/product_fields_translator.py
# -*- coding: utf-8 -*-\

#! venv/bin/python/python3.12

"""
.. module: src.product.product_fields 
	:platform: Windows, Unix
	:synopsis: Модуль перевода полей товара на языки клиентской базы данных

"""


from pathlib import Path
from typing import List
...
from src import gs
from src.utils.printer import pprint
from src.logger import logger
#from src.db import ProductTranslationsManager
#from src.translator import get_translations_from_presta_translations_table
#from src.translator import insert_new_translation_to_presta_translations_table
from src.logger.exceptions import ProductFieldException
...

def rearrange_language_keys(presta_fields_dict: dict, client_langs_schema: dict | List[dict], page_lang: str) -> dict:
    """Функция обновляет идентификатор языка в словаре presta_fields_dict на соответствующий идентификатор
    из схемы клиентских языков при совпадении языка страницы.

    Args:
        presta_fields_dict (dict): Словарь полей товара.
        page_lang (str): Язык страницы.
        client_langs_schema (list | dict): Схема языков клиента.

    Returns:
        dict: Обновленный словарь presta_fields_dict.
    """
    client_lang_id = None
    for lang in client_langs_schema:
        if lang['locale'] == page_lang or \
        lang['iso_code'] == page_lang or  \
        lang['language_code'] == page_lang:   # <- оч плохо А если he или IL?
            client_lang_id = lang['id']
            break

    if client_lang_id is not None:
        for field in presta_fields_dict.values():
            if isinstance(field, dict) and 'language' in field:
                for lang_data in field['language']:
                    lang_data['attrs']['id'] = str(client_lang_id)   # <- Эти айдишники ОБЯЗАТЕЛЬНО строки. Связано с XML парсером

    return presta_fields_dict


def translate_presta_fields_dict (presta_fields_dict: dict, 
                                  client_langs_schema: list | dict, 
                                  page_lang: str = None) -> dict:
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
    @param page_lang `str` язык страницы поставщика в коде en-US, ru-RU, he_HE. 
    Если не задан - функция пытается определить п тексту
    @returns presta_fields_dict переведенный словарь полей товара
    """

    presta_fields_dict = rearrange_language_keys (presta_fields_dict, client_langs_schema, page_lang)
    #product_translations = get_translations_from_presta_translations_table(presta_fields_dict['reference'])
    enabled_product_translations = get_translations_from_presta_translations_table(presta_fields_dict['reference'])
    ...
    if not enabled_product_translations or enabled_product_translations or len(enabled_product_translations) <1:
        """ В таблице переводов нет такого перевода товара. Добавляю текущий, как новый """
        ...
        global record
        rec = record(presta_fields_dict)
        insert_new_translation_to_presta_translations_table(rec)
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
            мне нужен iso_code
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
```

# <algorithm>

**Шаг 1:** Функция `rearrange_language_keys` ищет идентификатор `client_lang_id` языка в схеме `client_langs_schema` по переданному `page_lang` (язык страницы).  Проверяет соответствие с `locale`, `iso_code` и `language_code`.
**Пример:** Если `page_lang` = 'ru-RU', функция ищет запись в `client_langs_schema` с `locale`='ru-RU', `iso_code`='ru', или `language_code`='ru'.
**Шаг 2:** Если `client_lang_id` найден, функция итерируется по всем полям `presta_fields_dict` и ищет вложенные словари с ключом 'language'.
**Пример:** Если `presta_fields_dict` содержит поле с ключом 'title' и значением `{'language': [{'attrs': {'id': '2'}, 'value': 'Заголовок'}]}`, функция обновит `id` в `attrs` на найденный `client_lang_id`.
**Шаг 3:** Функция `translate_presta_fields_dict` принимает словарь `presta_fields_dict`, схему языков `client_langs_schema` и язык страницы `page_lang`.
**Шаг 4:** Вызывает функцию `rearrange_language_keys` для начальной обработки.
**Шаг 5:** Вызывает функцию `get_translations_from_presta_translations_table` для получения переводов из базы данных.
**Шаг 6:** Проверяет, есть ли переводы в базе данных для данного товара.
**Шаг 7:** Если переводов нет, добавляет новый перевод в базу данных (вызывая `insert_new_translation_to_presta_translations_table`).
**Шаг 8:** Итерируется по схеме языков `client_langs_schema` и переводит поля `presta_fields_dict` на соответствующие языки, используя данные из `enabled_product_translations` и устанавливая `id`  в соответствие с `client_lang['id']`.
**Пример:** Если `client_lang['iso_code']` соответствует `translated_record.locale`, функция перезаписывает значения полей в `presta_fields_dict` с новым `id` (строковым).

# <mermaid>

```mermaid
graph LR
    A[presta_fields_dict] --> B(rearrange_language_keys);
    B --> C{get_translations_from_presta_translations_table};
    C --True --> D[enabled_product_translations];
    C --False --> E[insert_new_translation_to_presta_translations_table];
    E --> F[presta_fields_dict];
    D --> G[loop client_lang in client_langs_schema];
    G --> H[loop translated_record in enabled_product_translations];
    H --> I{client_lang['iso_code'] in translated_record.locale?};
    I --True --> J[update presta_fields_dict];
    I --False --> H;
    J --> F;
    F --> K[return presta_fields_dict];
```

# <explanation>

**Импорты**:

- `from pathlib import Path`: Импортирует класс `Path` для работы с путями к файлам.  Не используется в данном коде напрямую.
- `from typing import List`: Импортирует тип данных `List` для работы со списками. Используется для указания типов аргументов и возвращаемых значений функций.
- `from src import gs`:  Импортирует модуль `gs` из пакета `src`.  Неясно, что он представляет собой без контекста кода проекта.
- `from src.utils.printer import pprint`: Импортирует функцию `pprint` из модуля `printer` в пакете `src.utils`. Вероятно, для форматированного вывода данных.
- `from src.logger import logger`: Импортирует объект `logger` для ведения журналов событий. Используется для записи сообщений об ошибках.
- `from src.logger.exceptions import ProductFieldException`: Импортирует пользовательское исключение `ProductFieldException` из пакета `src.logger.exceptions`.
 - Остальные импорты, помеченные комментариями, вероятно, служат для доступа к функциональности работы с базой данных и переводом.

**Классы**:

- Нет явно объявленных классов в представленном коде.

**Функции**:

- `rearrange_language_keys(presta_fields_dict, client_langs_schema, page_lang)`: Обновляет идентификатор языка в словаре `presta_fields_dict` на основе соответствия `page_lang` в схеме языков `client_langs_schema`.
- `translate_presta_fields_dict(presta_fields_dict, client_langs_schema, page_lang)`: Главная функция для перевода полей товара. Получает данные о товаре, схему языков и язык страницы.  Ищет соответствующие переводы в базе данных, обновляет поля товара, обрабатывает возможные ошибки.

**Переменные**:

- `MODE`: Строковая константа, вероятно, для определения режима работы (например, 'dev', 'prod').
- `client_lang_id`: Переменная для хранения идентификатора языка клиента.
- `presta_fields_dict`: Словарь, содержащий данные о товаре. Ожидается, что содержит вложенные словари, представляющие мультиязычные поля.
- `client_langs_schema`:  Структура данных, содержащая схему языков клиента.


**Возможные ошибки и улучшения**:

- **Неустойчивость к невалидным данным:** Код не содержит проверок на корректность входных данных (например, типы данных, наличие необходимых ключей в словарях).  Возможны ошибки, если `presta_fields_dict` или `client_langs_schema` не соответствуют ожидаемому формату.
- **Обработка ошибок:** Обработка исключений (`try...except`) недостаточно полная.  Необходимо ловить и обрабатывать все типы возможных ошибок.
- **Непонятность зависимости `gs`:**  Нет информации о том, что представляет собой импортируемый модуль `gs`.
- **Плохое имя функции `rearrange_language_keys`**: Функция делает больше, чем просто переупорядочивает ключи. Поменяйте на более описательное имя.
- **Проверки на пустые списки:** Проверьте, что `enabled_product_translations` не пусто, прежде чем итерироваться по нему.
- **Переменная `page_lang` по умолчанию:** Лучше сделать параметр `page_lang` обязательным и не пытаться его определять по тексту.
- **Избегание `global`:** В коде используется `global record`, что не рекомендуется.  Найдите способ сделать переменную локальной.
- **Ошибки в `if` условиях:** Строки вида `enabled_product_translations or enabled_product_translations`. Возможен логический баг.

**Взаимосвязи с другими частями проекта**:

Функции `get_translations_from_presta_translations_table` и `insert_new_translation_to_presta_translations_table` указывают на существование модулей/классов для взаимодействия с базой данных переводов.  Возможно, существуют классы/функции для управления переводом, схемы языков, менеджер базы данных.