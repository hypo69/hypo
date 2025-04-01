# Модуль перевода полей товара на языки клиентской базы данных

## Обзор

Модуль `product_fields_translator.py` предназначен для перевода полей товара в соответствии со схемой языков, используемой в клиентской базе данных PrestaShop. Он позволяет адаптировать мультиязычные поля товаров, полученные от поставщика, к языковым настройкам конкретного клиента. Это необходимо, поскольку идентификаторы языков (`id`) в PrestaShop могут отличаться в зависимости от языка, выбранного при установке.

## Подробнее

Этот модуль решает задачу сопоставления и перевода полей товара между языковыми схемами поставщика и клиента. Он обрабатывает случаи, когда `id` языка в данных от поставщика не соответствует `id` языка в базе данных клиента. Для этого модуль использует схему языков клиента, полученную из API PrestaShop, чтобы правильно перевести и адаптировать поля товара.

Модуль содержит следующие функции:

- `rearrange_language_keys`: Обновляет идентификаторы языка в словаре полей товара в соответствии со схемой клиентских языков.
- `translate_presta_fields_dict`: Выполняет перевод мультиязычных полей товара на основе схемы языков клиента.

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

**Назначение**: Обновление идентификаторов языка в словаре полей товара (`presta_fields_dict`) на соответствующие идентификаторы из схемы клиентских языков (`client_langs_schema`) при совпадении языка страницы (`page_lang`).

**Параметры**:

- `presta_fields_dict` (dict): Словарь полей товара, содержащий мультиязычные значения.
- `client_langs_schema` (dict | List[dict]): Схема языков клиента, полученная из API PrestaShop. Содержит информацию о соответствии между языковыми кодами и идентификаторами языков в базе данных клиента.
- `page_lang` (str): Язык страницы товара, например `'en-US'`, `'ru-RU'` или `'he_HE'`.

**Возвращает**:

- `dict`: Обновленный словарь `presta_fields_dict` с новыми идентификаторами языков, соответствующими схеме клиента.

**Как работает функция**:

1. **Поиск идентификатора языка клиента**: Функция итерируется по схеме языков клиента (`client_langs_schema`) и сравнивает значения ключей `'locale'`, `'iso_code'` и `'language_code'` с языком страницы (`page_lang`).
2. **Обновление идентификатора языка в полях товара**: Если идентификатор языка найден, функция итерируется по словарю `presta_fields_dict` и обновляет атрибут `'id'` в мультиязычных полях (`'language'`) на значение `client_lang_id`. Важно отметить, что айдишники принудительно преобразуются в строки, поскольку XML парсер требует строковые значения.

**ASCII flowchart**:

```
Начало
  ↓
Найти client_lang_id в client_langs_schema
  ↓
Если client_lang_id найден:
  │
  → Обновить attrs['id'] в presta_fields_dict на client_lang_id (строка)
  │
Конец
```

**Примеры**:

```python
presta_fields_dict = {
    'name': {'language': [{'attrs': {'id': '1'}, 'value': 'Product Name'}]},
    'description': {'language': [{'attrs': {'id': '1'}, 'value': 'Product Description'}]}
}
client_langs_schema = [
    {'id': '2', 'locale': 'ru-RU', 'iso_code': 'ru', 'language_code': 'ru-ru'},
    {'id': '3', 'locale': 'en-US', 'iso_code': 'en', 'language_code': 'en-us'}
]
page_lang = 'en-US'

updated_dict = rearrange_language_keys(presta_fields_dict, client_langs_schema, page_lang)
print(updated_dict)
# {'name': {'language': [{'attrs': {'id': '3'}, 'value': 'Product Name'}]}, 'description': {'language': [{'attrs': {'id': '3'}, 'value': 'Product Description'}]}}
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
	        'language':[{'attrs':{'id':'1'}, 'value':value},]
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

**Назначение**: Функция для перевода мультиязычных полей товара в соответствии со схемой значений `id` языка в базе данных клиента.

**Параметры**:

- `presta_fields_dict` (dict): Словарь полей товара, собранный со страницы поставщика.
- `client_langs_schema` (list | dict): Словарь актуальных языков на клиенте.
- `page_lang` (str, optional): Язык страницы поставщика в коде (например, `'en-US'`, `'ru-RU'`, `'he_HE'`). Если не указан, функция попытается определить язык автоматически.

**Возвращает**:

- `dict`: Переведенный словарь полей товара `presta_fields_dict`.

**Как работает функция**:

1. **Переупорядочивание ключей таблицы**: Вызывает функцию `rearrange_language_keys` для обновления идентификаторов языка в `presta_fields_dict`.
2. **Получение переводов из таблицы**: Пытается получить существующие переводы товара из таблицы переводов PrestaShop (`get_translations_from_presta_translations_table`).
3. **Обработка отсутствующих переводов**: Если переводы отсутствуют, добавляет текущий товар как новый перевод в таблицу.
4. **Применение переводов из таблицы**: Если переводы найдены, итерируется по языкам клиента и записям переводов, чтобы обновить значения в `presta_fields_dict` соответствующими переводами из таблицы. Использует атрибут `iso_code` для сопоставления языков.
5. **Обработка ошибок**: В случае возникновения ошибки при применении переводов, логирует ошибку с использованием `logger.error`.

**Внутренние функции**:

- **`rearrange_language_keys`**: (Описание выше)

**ASCII flowchart**:

```
Начало
  ↓
Переупорядочивание ключей (rearrange_language_keys)
  ↓
Получение переводов из таблицы
  ↓
Если переводы отсутствуют:
  │
  → Добавить текущий товар как новый перевод
  │
Иначе:
  │
  → Для каждого языка клиента и записи перевода:
  │  │
  │  → Если iso_code языка клиента совпадает с locale записи перевода:
  │  │  │
  │  │  → Обновить значения в presta_fields_dict переводами из таблицы
  │  │
Конец
```

**Примеры**:

```python
presta_fields_dict = {
    'name': {'language': [{'attrs': {'id': '1'}, 'value': 'Product Name'}]},
    'description': {'language': [{'attrs': {'id': '1'}, 'value': 'Product Description'}]},
    'reference': '12345'
}
client_langs_schema = [
    {'id': '2', 'locale': 'ru-RU', 'iso_code': 'ru', 'language_code': 'ru-ru'},
    {'id': '3', 'locale': 'en-US', 'iso_code': 'en', 'language_code': 'en-us'}
]
page_lang = 'en-US'

translated_dict = translate_presta_fields_dict(presta_fields_dict, client_langs_schema, page_lang)
print(translated_dict)
# {'name': {'language': [{'attrs': {'id': '3'}, 'value': 'Product Name'}]}, 'description': {'language': [{'attrs': {'id': '3'}, 'value': 'Product Description'}]} ...}