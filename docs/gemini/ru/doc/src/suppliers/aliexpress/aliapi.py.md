# Модуль `aliapi.py`

## Обзор

Модуль `aliapi.py` представляет собой кастомный класс `AliApi` для работы с API AliExpress. Он расширяет базовый класс `AliexpressApi` и предоставляет дополнительные методы для получения данных о продуктах, создания партнерских ссылок и управления категориями и кампаниями.

## Содержание

- [Обзор](#обзор)
- [Классы](#классы)
  - [`AliApi`](#aliapi)
- [Функции](#функции)
    - [`retrieve_product_details_as_dict`](#retrieve_product_details_as_dict)
    - [`get_affiliate_links`](#get_affiliate_links)

## Классы

### `AliApi`

**Описание**:
Класс `AliApi` представляет собой расширение `AliexpressApi` для более удобной работы с AliExpress API.

**Родительский класс**:
`AliexpressApi`

**Атрибуты класса**:
- `manager_categories` (CategoryManager): Менеджер для работы с категориями товаров.
- `manager_campaigns` (ProductCampaignsManager): Менеджер для работы с кампаниями товаров.

**Методы**:

- `__init__`: Инициализирует экземпляр класса `AliApi`.

    **Описание**: Инициализирует экземпляр класса `AliApi` с заданными языком и валютой.

    **Параметры**:
      - `language` (str): Язык для API-запросов. По умолчанию `'en'`.
      - `currency` (str): Валюта для API-запросов. По умолчанию `'usd'`.
    
    **Возвращает**:
       - `None`

## Функции

### `retrieve_product_details_as_dict`

**Описание**:
Отправляет список ID продуктов в AliExpress и получает список объектов `SimpleNamespace` с описанием продуктов, затем преобразует их в список словарей.

**Параметры**:
- `product_ids` (list): Список ID продуктов.

**Возвращает**:
- `dict | None`: Список данных о продуктах в виде словарей, или `None` в случае ошибки.

**Пример преобразования SimpleNamespace в dict:**
```python
namespace_list = [
    SimpleNamespace(a=1, b=2, c=3),
    SimpleNamespace(d=4, e=5, f=6),
    SimpleNamespace(g=7, h=8, i=9)
]

dict_list = [vars(ns) for ns in namespace_list]
# или
dict_list = [ns.__dict__ for ns in namespace_list]
```
### `get_affiliate_links`

**Описание**:
Получает партнерские ссылки для указанных продуктов.

**Параметры**:
- `links` (str | list): Ссылки на продукты для которых нужно сгенерировать партнерские ссылки.
- `link_type` (int, optional): Тип партнерской ссылки. По умолчанию `0`.
- `**kwargs`: Дополнительные параметры.
**Возвращает**:
- `List[SimpleNamespace]`: Список объектов `SimpleNamespace`, содержащих партнерские ссылки.