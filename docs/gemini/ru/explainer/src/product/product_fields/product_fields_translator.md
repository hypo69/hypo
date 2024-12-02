```MD
# <input code>

```python
## \file hypotez/src/product/product_fields/product_fields_translator.py
# -*- coding: utf-8 -*-
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
    ...
    """
    presta_fields_dict = rearrange_language_keys (presta_fields_dict, client_langs_schema, page_lang)
    enabled_product_translations = get_translations_from_presta_translations_table(presta_fields_dict['reference'])
    ...
    if not enabled_product_translations or enabled_product_translations or len(enabled_product_translations) <1:
        # Добавление перевода в базу, если его нет
        ...
        return presta_fields_dict

    for client_lang in client_langs_schema:
        for translated_record in enabled_product_translations:
            try:
                if client_lang['iso_code'] in translated_record.locale: 
                    # Запись перевода в словарь
                    for key in presta_fields_dict.keys():
                        if hasattr(translated_record, key):
                            presta_fields_dict[key] = {'language': [{'attrs': {'id': str(client_lang['id'])}, 'value': getattr(translated_record, key)}]}
            except Exception as ex:
                logger.error(f"""Ошибка {ex}
                client_lang = {pprint(client_lang)}
                """)
                ...

    return presta_fields_dict
```

# <algorithm>

**Шаг 1:** Функция `rearrange_language_keys` принимает словарь `presta_fields_dict`, схему языков `client_langs_schema` и язык страницы `page_lang`.
* **Пример:** `presta_fields_dict = {'name': {'language': [{'attrs': {'id': '2'}, 'value': 'Product Name'}]}, 'description': {'language': [{'attrs': {'id': '1'}, 'value': 'Description'}]}}`, `client_langs_schema = [{'id': 1, 'locale': 'en-US', 'iso_code': 'en'}, {'id': 2, 'locale': 'ru-RU', 'iso_code': 'ru'} ]`, `page_lang = 'ru'`.

**Шаг 2:** Функция ищет ID языка из `client_langs_schema` по соответствию `page_lang`.
* **Пример:** Ищет в `client_langs_schema` элемент с `locale = 'ru'`, `iso_code = 'ru'`, или `language_code = 'ru'`. Находит `{'id': 2}`.

**Шаг 3:** Если ID языка найден, функция обновит значения `id` в `presta_fields_dict` для всех полей, соответсвующих языку страницы.
* **Пример:** Заменяет `id: '2'` на `id: '2'` во всех `language` элементах словаря `presta_fields_dict`.

**Шаг 4:** Функция `translate_presta_fields_dict` использует `rearrange_language_keys` для обновления словаря.


**Шаг 5:** Функция `translate_presta_fields_dict` использует `get_translations_from_presta_translations_table` для получения переводов.


**Шаг 6:** Если нет переводов, функция добавляет новый перевод в базу данных.


**Шаг 7:** Цикл перебирает языковые записи из `client_langs_schema`.


**Шаг 8:** Вложенный цикл перебирает переведенные записи.


**Шаг 9:** Проверяет, совпадает ли `iso_code` языка из схемы с языком переведенной записи.


**Шаг 10:** Если совпадение, то обновляет значение поля в `presta_fields_dict` соответствующим переведенным значением.
* **Пример:** Если `client_lang` = `en`, `translated_record` = `en`, обновляет значение поля `name` в `presta_fields_dict` из `translated_record`

**Шаг 11:** Обрабатывает исключения во время доступа к атрибутам переведенных записей.


**Шаг 12:** Возвращает обновленный словарь `presta_fields_dict`.


# <mermaid>

```mermaid
graph LR
    A[Вход: presta_fields_dict, client_langs_schema, page_lang] --> B{rearrange_language_keys};
    B --> C[client_lang_id = find_lang_id(client_langs_schema, page_lang)];
    C -- found --> D[Update presta_fields_dict];
    C -- not found --> E;
    D --> F[translate_presta_fields_dict];
    F --> G{get_translations(presta_fields_dict['reference'])};
    G -- translations --> H[Translate Fields];
    G -- no translations --> I[Insert New Translation];
    H --> J[Update presta_fields_dict];
    I --> J;
    J --> K[Выход: presta_fields_dict];
```

# <explanation>

**Импорты:**

- `from pathlib import Path`: Импортирует класс `Path` для работы с путями к файлам.
- `from typing import List`: Импортирует тип данных `List` для работы со списками.
- `from src import gs`: Импортирует модуль `gs` из пакета `src`.  Без контекста, трудно определить точную функциональность, но вероятно это вспомогательные функции или классы.
- `from src.utils import pprint`: Импортирует функцию `pprint` из модуля `utils` в пакете `src`. Вероятно, это функция для красивой печати данных.
- `from src.logger import logger`: Импортирует объект `logger` из модуля `logger` в пакете `src`. Это объект для ведения логов.
- `from src.logger.exceptions import ProductFieldException`: Импортирует пользовательское исключение `ProductFieldException` из модуля `exceptions` в пакете `src.logger`.
- Несколько строк импорта закомментированы. Эти импорты, вероятно, относятся к функциям или классам для работы с базой данных и переводами.

**Классы:**

Код не содержит объявления классов.

**Функции:**

- `rearrange_language_keys`: Эта функция принимает словарь `presta_fields_dict`, схему языков `client_langs_schema` и язык страницы `page_lang`.  Она ищет ID языка в `client_langs_schema` по соответствию `page_lang` и обновляет атрибут `id` в словаре `presta_fields_dict` для полей, соответствующих найденному языку.
- `translate_presta_fields_dict`:  Эта функция получает словарь `presta_fields_dict`, схему языков `client_langs_schema` и язык страницы.  Функция переводит мультиязычные поля товара, используя переводы из базы данных. Если перевод отсутствует, то добавляет новый в базу.

**Переменные:**

- `MODE`: Строковая константа, вероятно, используемая для управления режимом работы приложения (например, 'dev', 'prod').
- `client_lang_id`: Переменная, хранящая ID языка, найденный в схеме языков.
- `presta_fields_dict`: Словарь, содержащий поля товара, полученный с внешнего источника.
- `client_langs_schema`: Словарь, содержащий схему языков, необходимую для сопоставления.
- `page_lang`: Язык страницы, который используется для определения целевого языка перевода.


**Возможные ошибки и улучшения:**

- Неустойчивый поиск языка.  Функция ищет соответствие по `locale`, `iso_code` и `language_code`, что может привести к некорректному совпадению если формат не соответствует. Нужно выбрать один формат и использовать его для поиска (например, `iso_code`).
- Обработка исключений в `translate_presta_fields_dict`.  Обработка исключений может быть более детализирована для более точной диагностики ошибок.
- Проверка входных данных.  Функции не проверяют, что входные данные являются допустимыми, что может привести к ошибкам. Нужно добавить проверки типов и валидации данных.
- Сложность логики.  Логика, связанная с получением и использованием переводов, может быть переписана для лучшей читаемости и понимания.  Разделение на более мелкие, специализированные функции увеличит читаемость и позволит снизить сложность.
- Отсутствие явных проверок на корректность input `presta_fields_dict` (пустой или не содержащий нужных полей `language`).

**Взаимосвязи с другими частями проекта:**

Код взаимодействует с модулями `gs`, `pprint`, `logger`, `get_translations_from_presta_translations_table`, `insert_new_translation_to_presta_translations_table`, предполагая наличие соответствующих классов и функций в других модулях проекта (`src.utils`, `src.logger`, `src.translator`, `src.db`).  Отсутствие кода этих модулей затрудняет полное понимание функциональности.