# Модуль `hypotez/src/suppliers/aliexpress/api/models/request_parameters.py`

## Обзор

Данный модуль содержит определения констант для параметров запросов API AliExpress.  Он предоставляет перечисления для типов продуктов, сортировки и типов ссылок.

## Оглавление

* [ProductType](#producttype)
* [SortBy](#sortby)
* [LinkType](#linktype)


## `ProductType`

**Описание**: Перечисление типов продуктов для поиска на AliExpress.

**Константы**:

- `ALL`: Все типы продуктов.
- `PLAZA`: Продукты из PLAZA.
- `TMALL`: Продукты из TMALL.


## `SortBy`

**Описание**: Перечисление типов сортировки результатов поиска на AliExpress.

**Константы**:

- `SALE_PRICE_ASC`: Сортировка по цене (возрастание).
- `SALE_PRICE_DESC`: Сортировка по цене (убывание).
- `LAST_VOLUME_ASC`: Сортировка по последнему объёму (возрастание).
- `LAST_VOLUME_DESC`: Сортировка по последнему объёму (убывание).


## `LinkType`

**Описание**: Перечисление типов ссылок на AliExpress.

**Константы**:

- `NORMAL`: Обычный тип ссылки.
- `HOTLINK`: Горячая ссылка.