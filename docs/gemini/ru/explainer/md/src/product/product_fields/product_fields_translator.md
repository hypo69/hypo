# <input code>

```python
## \file hypotez/src/product/product_fields/product_fields_translator.py
# -*- coding: utf-8 -*-\
#! venv/Scripts/python.exe
#! venv/bin/python/python3.12

"""
.. module: src.product.product_fields 
	:platform: Windows, Unix
	:synopsis: Модуль перевода полей товара на языки клиентской базы данных

"""
MODE = 'dev'

from pathlib import Path
from typing import List
...
from src import gs
from src.utils import pprint
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
		    'language': [
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

**Описание алгоритма:**

Функция `translate_presta_fields_dict` отвечает за перевод полей товара на нужный язык.

**Шаг 1:** Переупорядочивает языковые ключи в словаре `presta_fields_dict` используя функцию `rearrange_language_keys`.
**Пример:** Если `page_lang` = 'ru-RU' и в `client_langs_schema` есть язык с `locale='ru-RU'`, то идентификатор языка будет изменен.

**Шаг 2:**  Получает переводы из базы данных (`enabled_product_translations`) по `reference` товара из входного словаря.
**Пример:** Если товар с `reference='XYZ123'` уже переведен на несколько языков, функция получит этот список переводов.


**Шаг 3:** Если переводов нет или они пустые, добавляет запись о переводе в базу данных.


**Шаг 4:** Проходит по схеме языков `client_langs_schema` и переведенным записям.
**Пример:** Если в `client_langs_schema` есть язык с `iso_code='ru'`, и в базе есть перевод для этого языка, то значения для поля переводит.

**Шаг 5:** В цикле по полям `presta_fields_dict` ищет соответствие в `translated_record`  и сохраняет перевод.
**Пример:** Если у `translated_record` есть поле `name`, то соответствующее поле в `presta_fields_dict` обновляется со значением перевода.

**Шаг 6:** Возвращает переведенный `presta_fields_dict`.


# <mermaid>

```mermaid
graph LR
    A[translate_presta_fields_dict] --> B{rearrange_language_keys};
    B --> C[presta_fields_dict];
    C --> D(get_translations_from_presta_translations_table);
    D --> E{enabled_product_translations};
    E -- нет переводов --> F[insert_new_translation_to_presta_translations_table];
    F --> C;
    E -- есть переводы --> G(Цикл по client_langs_schema);
    G --> H(Цикл по translated_record);
    H --> I[Проверка совпадения iso_code];
    I -- совпадение --> J[Обновление поля в presta_fields_dict];
    J --> C;
    I -- не совпадение --> H;
    C --> K[return presta_fields_dict];

subgraph src
  subgraph src.utils
    subgraph pprint
      D --> pprint;
    end
  end
    subgraph src.logger
      subgraph src.logger.exceptions
      end
    end
  
    subgraph src.db
    
    end
  subgraph src.translator
    
    end
end

```

# <explanation>

**Импорты:**

- `from pathlib import Path`:  Импортирует класс `Path` для работы с путями к файлам.  Не используется в данном файле.
- `from typing import List`:  Импортирует тип данных `List` для работы со списками. Используется для аннотации типов параметров.
- `from src import gs`: Импортирует модуль `gs` из пакета `src`.  Непонятно, что он делает, так как не используется в этом фрагменте.
- `from src.utils import pprint`:  Импортирует функцию `pprint` из модуля `utils` пакета `src`. Используется для вывода отладочной информации.
- `from src.logger import logger`: Импортирует логгер `logger` из пакета `src.logger`.  Используется для записи сообщений об ошибках.
- `from src.logger.exceptions import ProductFieldException`: Импортирует пользовательское исключение `ProductFieldException` из подпакета `exceptions` пакета `src.logger`.

**Классы:**

Нет классов в данном фрагменте.

**Функции:**

- `rearrange_language_keys`:  Обновляет атрибут `id` языковых полей в словаре `presta_fields_dict` на основе схемы `client_langs_schema` и языка страницы `page_lang`.
- `translate_presta_fields_dict`: Основная функция для перевода полей товара. Принимает словарь полей `presta_fields_dict`, схему языков `client_langs_schema` и язык страницы `page_lang`.  Из базы данных получает переводы (или добавляет их если не находит),  затем обновляет `presta_fields_dict` на основе этой информации.

**Переменные:**

- `MODE`:  Строковая переменная, хранит режим работы (вероятно, 'dev' или 'prod').
- `presta_fields_dict`:  Словарь, содержащий поля товара.
- `client_langs_schema`: Словарь или список словарей, описывающих языки клиента.
- `page_lang`: Язык страницы, используется для выбора нужного языка из `client_langs_schema`.
- `client_lang_id`:  Идентификатор языка клиента.
- `enabled_product_translations`: Результат запроса к базе данных о переводах для данного товара.

**Возможные ошибки и улучшения:**

- **Неявное определение `record`:**  В коде используется `global record`, но нет объявления переменной `record`. Это может привести к неожиданному поведению.  Необходимо явно определить `record` перед использованием.
- **Сложная логика проверки переводов:**  Логика поиска подходящего перевода (по `iso_code`) кажется сложной.  Можно рассмотреть более аккуратные механизмы определения.
- **Обработка исключений:**  Обработка исключений в `translate_presta_fields_dict` недостаточна. Можно добавить более подробную диагностику ошибок.
- **Неопределенный `page_lang`:** Если `page_lang` не задан, функция пытается определить его, но это не описано. Это может привести к ошибкам.
- **Обработка пустых или неправильных входных данных:** Нет проверок входных данных (`presta_fields_dict`, `client_langs_schema`, `page_lang`).  Если данные не корректны, функция может сломаться.
- **Уязвимость к SQL injection:** В запросе к базе данных, если `reference` не защищен, существует уязвимость к SQL injection.  Надо использовать параметризованные запросы.


**Взаимосвязи с другими частями проекта:**

Функции `get_translations_from_presta_translations_table` и `insert_new_translation_to_presta_translations_table` показывают зависимость от модулей, вероятно, из папки `src.db` и `src.translator`. Это подразумевает связь с системой базы данных.


```