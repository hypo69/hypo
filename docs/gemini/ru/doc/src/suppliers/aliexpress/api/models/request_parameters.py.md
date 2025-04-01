# Модуль `request_parameters`

## Обзор

Модуль `request_parameters` содержит классы, определяющие константы для параметров запросов к API AliExpress. Эти константы используются для указания типа продукта, способа сортировки и типа ссылки.

## Подробнее

Этот модуль предоставляет набор констант, которые помогают стандартизировать и упростить формирование запросов к API AliExpress. Он определяет возможные значения для различных параметров, таких как тип продукта (`ProductType`), способ сортировки (`SortBy`) и тип ссылки (`LinkType`).

## Классы

### `ProductType`

**Описание**: Класс, определяющий константы для типов продуктов.

**Принцип работы**:
Класс `ProductType` содержит три константы: `ALL`, `PLAZA` и `TMALL`, представляющие различные типы продуктов, доступные на AliExpress.

**Методы**: Нет.

**Параметры**: Нет.

**Примеры**
```python
product_type_all = ProductType.ALL  # 'ALL'
product_type_plaza = ProductType.PLAZA  # 'PLAZA'
product_type_tmall = ProductType.TMALL  # 'TMALL'
```

### `SortBy`

**Описание**: Класс, определяющий константы для способов сортировки результатов поиска.

**Принцип работы**:
Класс `SortBy` содержит четыре константы: `SALE_PRICE_ASC`, `SALE_PRICE_DESC`, `LAST_VOLUME_ASC` и `LAST_VOLUME_DESC`, представляющие различные способы сортировки продуктов по цене и объему продаж.

**Методы**: Нет.

**Параметры**: Нет.

**Примеры**
```python
sort_by_price_asc = SortBy.SALE_PRICE_ASC  # 'SALE_PRICE_ASC'
sort_by_price_desc = SortBy.SALE_PRICE_DESC  # 'SALE_PRICE_DESC'
sort_by_volume_asc = SortBy.LAST_VOLUME_ASC  # 'LAST_VOLUME_ASC'
sort_by_volume_desc = SortBy.LAST_VOLUME_DESC  # 'LAST_VOLUME_DESC'
```

### `LinkType`

**Описание**: Класс, определяющий константы для типов ссылок.

**Принцип работы**:
Класс `LinkType` содержит две константы: `NORMAL` и `HOTLINK`, представляющие различные типы ссылок, используемые в API AliExpress.

**Методы**: Нет.

**Параметры**: Нет.

**Примеры**
```python
link_type_normal = LinkType.NORMAL  # 0
link_type_hotlink = LinkType.HOTLINK  # 2
```