# Модуль `product_fields_translator.py`

## Обзор

Модуль предназначен для перевода полей товара на языки клиентской базы данных. Он содержит функции для адаптации идентификаторов языка в данных о товарах, полученных от поставщика, к схеме, используемой в базе данных клиента PrestaShop. Это необходимо, поскольку соответствие идентификаторов языков может различаться между поставщиком и клиентом.

## Подробнее

Этот модуль играет важную роль в процессе синхронизации данных о товарах между поставщиком и клиентской платформой PrestaShop. Он гарантирует, что мультиязычные поля товара правильно отображаются на клиентском сайте, используя соответствующую схему идентификаторов языков. Модуль также включает функциональность для работы с переводами товаров, полученными из базы данных клиента.

## Функции

### `rearrange_language_keys`

```python
def rearrange_language_keys(presta_fields_dict: dict, client_langs_schema: dict | List[dict], page_lang: str) -> dict:
    """
    Args:
        presta_fields_dict (dict): Словарь полей товара.
        page_lang (str): Язык страницы.
        client_langs_schema (list | dict): Схема языков клиента.

    Returns:
        dict: Обновленный словарь `presta_fields_dict`.
    """
```

**Описание**: Обновляет идентификатор языка в словаре `presta_fields_dict` на соответствующий идентификатор из схемы клиентских языков при совпадении языка страницы.

**Параметры**:
- `presta_fields_dict` (dict): Словарь полей товара.
- `client_langs_schema` (dict | List[dict]): Схема языков клиента.
- `page_lang` (str): Язык страницы.

**Возвращает**:
- `dict`: Обновленный словарь `presta_fields_dict`.

**Пример**:
```python
client_langs_schema = [{'locale': 'en-US', 'id': '2'}, {'locale': 'ru-RU', 'id': '3'}]
presta_fields_dict = {'name': {'language': [{'attrs': {'id': '1'}, 'value': 'Product Name'}]}}
page_lang = 'en-US'
result = rearrange_language_keys(presta_fields_dict, client_langs_schema, page_lang)
print(result)
# {'name': {'language': [{'attrs': {'id': '2'}, 'value': 'Product Name'}]}}
```

### `translate_presta_fields_dict`

```python
def translate_presta_fields_dict (presta_fields_dict: dict, 
                                  client_langs_schema: list | dict, 
                                  page_lang: str = None) -> dict:
    """
    Args:
        presta_fields_dict (dict): словарь полей товара собранный со страницы поставщика
        client_langs_schema (dict): словарь актуальных языков на клиенте
        page_lang (str): язык страницы поставщика в коде en-US, ru-RU, he_HE. Если не задан - функция пытается определить п тексту

    Returns:
        dict: переведенный словарь полей товара
    """
```

**Описание**: Переводит мультиязычные поля в соответствии со схемой значений `id` языка в базе данных клиента.

**Параметры**:
- `presta_fields_dict` (dict): Словарь полей товара, собранный со страницы поставщика.
- `client_langs_schema` (list | dict): Словарь актуальных языков на клиенте.
- `page_lang` (str, optional): Язык страницы поставщика в коде `en-US`, `ru-RU`, `he_HE`. Если не задан, функция пытается определить его по тексту. По умолчанию `None`.

**Возвращает**:
- `dict`: Переведенный словарь полей товара.

**Вызывает исключения**:
- `Exception`: Возникает в случае ошибки при обработке перевода.

**Примеры**:
```python
client_langs_schema = [{'iso_code': 'en', 'id': '2'}, {'iso_code': 'ru', 'id': '3'}]
presta_fields_dict = {'name': {'language': [{'attrs': {'id': '1'}, 'value': 'Product Name'}], 'reference': '123'}}
page_lang = 'en-US'
# Mocking functions to avoid actual database calls
def get_translations_from_presta_translations_table(reference: str):
    #Return empty list to simulate missing translations
    return []

def insert_new_translation_to_presta_translations_table(record: dict):
    print('Record to insert:', record)
    return {}

enabled_product_translations = get_translations_from_presta_translations_table(presta_fields_dict['reference'])   
result = translate_presta_fields_dict(presta_fields_dict, client_langs_schema, page_lang)
print(result)
# {'name': {'language': [{'attrs': {'id': '2'}, 'value': 'Product Name'}], 'reference': '123'}}