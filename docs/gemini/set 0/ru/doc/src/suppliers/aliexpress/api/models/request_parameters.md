# Модуль `hypotez/src/suppliers/aliexpress/api/models/request_parameters.py`

## Обзор

Этот модуль определяет перечисления (enum) для параметров запросов API AliExpress, используемых для получения данных о продуктах.

## Оглавление

* [ProductType](#producttype)
* [SortBy](#sortby)
* [LinkType](#linktype)


## Перечисления

### `ProductType`

**Описание**: Перечисление типов продуктов, которые могут быть запрошены.

**Значения**:

- `ALL`: Все типы продуктов.
- `PLAZA`: Продукты с платформы PLAZA.
- `TMALL`: Продукты с платформы TMALL.


### `SortBy`

**Описание**: Перечисление способов сортировки результатов запроса.

**Значения**:

- `SALE_PRICE_ASC`: Сортировка по цене продажи по возрастанию.
- `SALE_PRICE_DESC`: Сортировка по цене продажи по убыванию.
- `LAST_VOLUME_ASC`: Сортировка по последнему объёму продаж по возрастанию.
- `LAST_VOLUME_DESC`: Сортировка по последнему объёму продаж по убыванию.


### `LinkType`

**Описание**: Перечисление типов ссылок на продукты.

**Значения**:

- `NORMAL`: Обычная ссылка.
- `HOTLINK`: Горячая ссылка.