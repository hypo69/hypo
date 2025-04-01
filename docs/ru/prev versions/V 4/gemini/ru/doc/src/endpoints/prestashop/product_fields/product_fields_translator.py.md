# Модуль `product_fields_translator.py`

## Обзор

Модуль предназначен для перевода полей товара в соответствии со схемой значений `id` языка в базе данных клиента PrestaShop. Он включает функции для обновления идентификаторов языка в словаре полей товара и получения переводов из таблицы переводов PrestaShop.

## Подробнее

Основная задача модуля заключается в согласовании идентификаторов языков, используемых в данных о товарах, полученных от поставщика, с идентификаторами, используемыми в базе данных PrestaShop клиента. Это необходимо, поскольку идентификаторы языков могут отличаться в зависимости от настроек PrestaShop.

Модуль содержит функции:
- `rearrange_language_keys`: Обновляет идентификатор языка в словаре `presta_fields_dict` на соответствующий идентификатор из схемы клиентских языков.
- `translate_presta_fields_dict`: Переводит мультиязычные поля в соответствии со схемой значений `id` языка в базе данных клиента.

## Функции

### `rearrange_language_keys`

```python
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
```

**Описание**: Обновляет идентификатор языка в словаре `presta_fields_dict` на соответствующий идентификатор из схемы клиентских языков при совпадении языка страницы.

**Параметры**:
- `presta_fields_dict` (dict): Словарь полей товара, где ключи соответствуют полям, а значения содержат информацию о языке.
- `client_langs_schema` (dict | List[dict]): Схема языков клиента, содержащая информацию о соответствии между локалями, ISO-кодами и идентификаторами языков.
- `page_lang` (str): Язык страницы, для которого необходимо обновить идентификаторы.

**Возвращает**:
- `dict`: Обновленный словарь `presta_fields_dict` с новыми идентификаторами языков, соответствующими схеме клиента.

**Примеры**:

Предположим, у нас есть следующий словарь полей товара, схема языков клиента и язык страницы:

```python
presta_fields_dict = {
    'name': {
        'language': [
            {'attrs': {'id': '1'}, 'value': 'Product Name'}
        ]
    }
}
client_langs_schema = [
    {'id': 5, 'locale': 'en-US', 'iso_code': 'en', 'language_code': 'en-us'}
]
page_lang = 'en-US'

result = rearrange_language_keys(presta_fields_dict, client_langs_schema, page_lang)
print(result)
# Вывод:
# {
#     'name': {
#         'language': [
#             {'attrs': {'id': '5'}, 'value': 'Product Name'}
#         ]
#     }
# }
```

### `translate_presta_fields_dict`

```python
def translate_presta_fields_dict (presta_fields_dict: dict, 
                                  client_langs_schema: list | dict, 
                                  page_lang: str = None) -> dict:
    """ @Перевод мультиязычных полей в соответствии со схемой значений `id` языка в базе данных клиента
	    Функция получает на вход заполненный словарь полей. Мультиязычные поля содржат значения,
	    полученные с сайта поставщика в виде словаря 
	    ```
	    {
	\t    \'language\':[\
	\t\t\t\t\t    {\'attrs\':{\'id\':\'1\'}, \'value\':value},\
	\t\t\t\t\t    ]\
	    }\
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
```

**Описание**: Переводит мультиязычные поля в соответствии со схемой значений `id` языка в базе данных клиента.

**Параметры**:
- `presta_fields_dict` (dict): Словарь полей товара, где ключи соответствуют полям, а значения содержат информацию о языке.
- `client_langs_schema` (list | dict): Схема языков клиента, содержащая информацию о соответствии между локалями, ISO-кодами и идентификаторами языков.
- `page_lang` (str, optional): Язык страницы поставщика. Если не задан, функция пытается определить его автоматически. По умолчанию `None`.

**Возвращает**:
- `dict`: Переведенный словарь полей товара.

**Вызывает исключения**:
- `ProductFieldException`: Если возникает ошибка при переводе полей.

**Примеры**:

```python
presta_fields_dict = {
    'name': {
        'language': [
            {'attrs': {'id': '1'}, 'value': 'Product Name'}
        ]
    },
    'reference': '12345'
}
client_langs_schema = [
    {'id': 5, 'locale': 'en-US', 'iso_code': 'en', 'language_code': 'en-us'}
]
page_lang = 'en-US'

result = translate_presta_fields_dict(presta_fields_dict, client_langs_schema, page_lang)
print(result)
# Вывод может варьироваться в зависимости от данных в таблице переводов