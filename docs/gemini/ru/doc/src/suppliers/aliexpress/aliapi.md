# Модуль `aliapi.py`

## Обзор

Модуль `aliapi.py` предоставляет класс `AliApi`, расширяющий базовый класс `AliexpressApi`, для работы с API AliExpress.  Он предназначен для получения подробной информации о продуктах, аффилированных ссылок и других данных, необходимых для работы с AliExpress. Модуль использует менеджеры баз данных для работы с категориями и рекламными кампаниями.

## Классы

### `AliApi`

**Описание**: Класс `AliApi` расширяет функциональность `AliexpressApi`, предоставляя дополнительные методы для взаимодействия с API AliExpress. Он также включает в себя менеджеры баз данных для работы с категориями и рекламными кампаниями.

**Методы**:

- `__init__`: Инициализирует экземпляр класса `AliApi`.
- `retrieve_product_details_as_dict`: Преобразует список идентификаторов продуктов в список словарей с деталями продуктов.
- `get_affiliate_links`: Получает аффилированные ссылки для заданных ссылок на продукты.

**Параметры**:

- `__init__(language: str = 'en', currency: str = 'usd', *args, **kwargs)`:
    - `language (str)`: Язык для запросов API. По умолчанию 'en'.
    - `currency (str)`: Валюта для запросов API. По умолчанию 'usd'.

**Возвращает**:

- `retrieve_product_details_as_dict(product_ids: list) -> dict | dict | None`:  Список словарей с деталями продуктов. Возвращает None в случае ошибки.
- `get_affiliate_links(links: str | list, link_type: int = 0, **kwargs) -> List[SimpleNamespace]`: Список объектов `SimpleNamespace` с аффилированными ссылками.


## Функции

(Нет функций в данном модуле)

## Примеры использования

```python
# Пример использования retrieve_product_details_as_dict
product_ids = [123, 456, 789]
aliapi_instance = AliApi()
product_details = aliapi_instance.retrieve_product_details_as_dict(product_ids)
print(product_details)
```

```python
# Пример использования get_affiliate_links
links = ["link1", "link2"]
aliapi_instance = AliApi()
affiliate_links = aliapi_instance.get_affiliate_links(links)
print(affiliate_links)
```

**Примечания**:

- Пример использования `retrieve_product_details_as_dict` демонстрирует преобразование данных из `SimpleNamespace` в список словарей.
- Пример `get_affiliate_links` предполагает использование `super().get_affiliate_links()`, так как метод  в `AliApi` не переопределен.


```
```