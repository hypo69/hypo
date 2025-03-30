# Модуль `product_fields_translator.py`

## Обзор

Модуль предназначен для перевода полей товара на языки клиентской базы данных PrestaShop. Он обеспечивает соответствие идентификаторов языков в данных о товаре, полученных от поставщика, с идентификаторами, используемыми в базе данных клиента.

## Подробней

Этот модуль решает задачу сопоставления мультиязычных данных о товарах между системой поставщика и клиентской базой данных PrestaShop. Проблема заключается в том, что идентификаторы языков (`id`) в данных поставщика не всегда соответствуют идентификаторам, используемым в клиентской базе данных. Это может привести к неправильному отображению информации о товаре на разных языках на стороне клиента.

Модуль содержит функции для переупорядочивания идентификаторов языков в соответствии со схемой клиента, а также для получения и вставки переводов из/в таблицу переводов PrestaShop. Он использует схему языков клиента для точного сопоставления и обеспечивает правильное отображение мультиязычных полей товара.

## Функции

### `rearrange_language_keys`

```python
def rearrange_language_keys(presta_fields_dict: dict, client_langs_schema: dict | List[dict], page_lang: str) -> dict:
    """
    Функция обновляет идентификатор языка в словаре presta_fields_dict на соответствующий идентификатор
    из схемы клиентских языков при совпадении языка страницы.

    Args:
        presta_fields_dict (dict): Словарь полей товара.
        page_lang (str): Язык страницы.
        client_langs_schema (list | dict): Схема языков клиента.

    Returns:
        dict: Обновленный словарь presta_fields_dict.
    """
```

**Описание**: Обновляет идентификаторы языков в словаре `presta_fields_dict` на основе схемы языков клиента.

**Параметры**:
- `presta_fields_dict` (dict): Словарь полей товара.
- `client_langs_schema` (dict | List[dict]): Схема языков клиента.
- `page_lang` (str): Язык страницы.

**Возвращает**:
- `dict`: Обновленный словарь `presta_fields_dict`.

**Пример**:

```python
presta_fields_dict = {'name': {'language': [{'attrs': {'id': '1'}, 'value': 'Product Name'}]}}
client_langs_schema = [{'id': 2, 'locale': 'ru-RU'}]
page_lang = 'ru-RU'
result = rearrange_language_keys(presta_fields_dict, client_langs_schema, page_lang)
print(result)
# {'name': {'language': [{'attrs': {'id': '2'}, 'value': 'Product Name'}]}}
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
```

**Описание**: Переводит мультиязычные поля в словаре `presta_fields_dict` в соответствии со схемой языков клиента.

**Параметры**:
- `presta_fields_dict` (dict): Словарь полей товара.
- `client_langs_schema` (list | dict): Схема языков клиента.
- `page_lang` (str, optional): Язык страницы поставщика. По умолчанию `None`.

**Возвращает**:
- `dict`: Переведенный словарь `presta_fields_dict`.

**Пример**:

```python
presta_fields_dict = {'name': {'language': [{'attrs': {'id': '1'}, 'value': 'Product Name'}], 'reference': '123'}}
client_langs_schema = [{'id': 2, 'iso_code': 'ru'}]
page_lang = 'ru-RU'
result = translate_presta_fields_dict(presta_fields_dict, client_langs_schema, page_lang)
print(result)
# {'name': {'language': [{'attrs': {'id': '2'}, 'value': 'Product Name'}], 'reference': '123'}}