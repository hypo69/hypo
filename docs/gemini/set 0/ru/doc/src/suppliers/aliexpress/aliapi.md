# Модуль `hypotez/src/suppliers/aliexpress/aliapi.py`

## Обзор

Модуль `aliapi.py` предоставляет класс `AliApi`, расширяющий функциональность базового класса `AliexpressApi`. Он предназначен для взаимодействия с API AliExpress, выполнения запросов, получения данных о продуктах и генерации аффилированных ссылок.  Модуль использует менеджеры баз данных для работы с категориями и кампаниями.

## Классы

### `AliApi`

**Описание**: Расширенный класс для работы с API AliExpress. Наследует от `AliexpressApi`.  Предоставляет дополнительные методы и атрибуты для работы с данными, полученными из API.

**Атрибуты**:

* `manager_categories`: Менеджер для работы с категориями AliExpress.  Тип: `CategoryManager`.
* `manager_campaigns`: Менеджер для работы с рекламными кампаниями продуктов. Тип: `ProductCampaignsManager`.


**Методы**:

#### `__init__`

**Описание**: Инициализирует экземпляр класса `AliApi`.

**Параметры**:

* `language` (str, по умолчанию 'en'): Язык для запросов к API.
* `currency` (str, по умолчанию 'usd'): Валюта для запросов к API.

**Возвращает**:
    None.

#### `retrieve_product_details_as_dict`

**Описание**: Отправляет список идентификаторов продуктов в API AliExpress и возвращает список словарей с деталями продуктов.

**Параметры**:

* `product_ids` (list): Список идентификаторов продуктов.

**Возвращает**:
* `dict | dict | None`:  Список словарей с деталями продуктов. Возвращает `None`, если произошла ошибка.

**Пример кода**:

```python
# Пример использования
product_ids = [123, 456, 789]
api_instance = AliApi()
product_details = api_instance.retrieve_product_details_as_dict(product_ids)
print(product_details)
```

#### `get_affiliate_links`

**Описание**: Возвращает аффилированные ссылки для указанных ссылок на продукты.

**Параметры**:

* `links` (str | list): Список или строка ссылок на продукты.
* `link_type` (int, по умолчанию 0): Тип аффилированной ссылки.
* `**kwargs`: Дополнительные параметры для метода `get_affiliate_links` базового класса.

**Возвращает**:
* `List[SimpleNamespace]`: Список объектов `SimpleNamespace` содержащих аффилированные ссылки.


## Функции

(Нет функций в данном модуле)


## Модули

* `src`
* `gs`
* `src.utils`
* `src.utils.convertors`
* `src.logger`
* `.api`
* `src.db.manager_categories`
* `src.db.manager_coupons_and_sales`


##  Примечание

В коде присутствуют комментарии с примерами использования.  Некоторые методы, такие как `collect_deals_from_url`, помечаны как плановые.