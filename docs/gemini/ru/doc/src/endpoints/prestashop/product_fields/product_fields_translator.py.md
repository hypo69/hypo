# Модуль `product_fields_translator.py`

## Обзор

Модуль предназначен для перевода полей товара на языки, используемые в клиентской базе данных PrestaShop. Он обеспечивает соответствие идентификаторов языков между данными, полученными от поставщика, и языковой схемой, настроенной у клиента.

## Подробнее

Этот модуль играет важную роль в процессе локализации данных о товарах. PrestaShop позволяет устанавливать разные языки для интерфейса и контента. ID языков в базе данных клиента могут отличаться от ID языков, используемых поставщиком. Модуль `product_fields_translator.py` приводит эти ID в соответствие, чтобы обеспечить корректное отображение информации о товаре на разных языках.

Основная задача модуля - адаптировать мультиязычные поля товара, полученные от поставщика, под актуальную схему языков, используемую на стороне клиента. Это включает в себя обновление идентификаторов языков в словаре полей товара (`presta_fields_dict`) в соответствии со схемой языков клиента (`client_langs_schema`).

Модуль также интегрируется с базой данных переводов PrestaShop для поиска и вставки новых переводов товаров, если они отсутствуют.

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

**Описание**: Обновляет идентификаторы языка в словаре `presta_fields_dict` на соответствующие идентификаторы из схемы клиентских языков при совпадении языка страницы.

**Параметры**:
- `presta_fields_dict` (dict): Словарь полей товара, содержащий мультиязычные значения.
- `client_langs_schema` (dict | List[dict]): Схема языков клиента, содержащая информацию о соответствии языков и их идентификаторов.
- `page_lang` (str): Язык текущей страницы товара.

**Возвращает**:
- `dict`: Обновленный словарь `presta_fields_dict` с новыми идентификаторами языков.

**Примеры**:
```python
client_langs_schema = [{'locale': 'en-US', 'id': '2'}, {'locale': 'ru-RU', 'id': '3'}]
presta_fields_dict = {'name': {'language': [{'attrs': {'id': '1'}, 'value': 'Product Name'}]}}
page_lang = 'en-US'
updated_dict = rearrange_language_keys(presta_fields_dict, client_langs_schema, page_lang)
print(updated_dict)
# Expected output: {'name': {'language': [{'attrs': {'id': '2'}, 'value': 'Product Name'}]}}
```

### `translate_presta_fields_dict`

```python
def translate_presta_fields_dict (presta_fields_dict: dict, 
                                  client_langs_schema: list | dict, 
                                  page_lang: str = None) -> dict:
    """
    Args:
        presta_fields_dict (dict): 
        client_langs_schema (list | dict): 
        page_lang (str, optional):  Defaults to None.

    Returns:
        dict: 
    """
```

**Описание**: Переводит мультиязычные поля в соответствии со схемой значений `id` языка в базе данных клиента.

**Параметры**:
- `presta_fields_dict` (dict): Словарь полей товара, собранный со страницы поставщика.
- `client_langs_schema` (list | dict): Словарь актуальных языков на клиенте.
- `page_lang` (str, optional): Язык страницы поставщика в коде en-US, ru-RU, he_HE. Если не задан - функция пытается определить по тексту. По умолчанию `None`.

**Возвращает**:
- `dict`: Переведенный словарь полей товара.

**Вызывает исключения**:
- `ProductFieldException`: Если возникает ошибка при обработке перевода полей товара.

**Примеры**:
```python
client_langs_schema = [{'iso_code': 'en', 'id': '2'}, {'iso_code': 'ru', 'id': '3'}]
presta_fields_dict = {'reference': '123', 'name': {'language': [{'attrs': {'id': '1'}, 'value': 'Product Name'}]}}
page_lang = 'en-US'
translated_dict = translate_presta_fields_dict(presta_fields_dict, client_langs_schema, page_lang)
print(translated_dict)
# {'reference': '123', 'name': {'language': [{'attrs': {'id': '2'}, 'value': 'Product Name'}]}}