# Модуль `request_parameters`

## Обзор

Модуль `request_parameters` определяет классы для представления параметров запросов к API AliExpress.

## Содержание

1.  [Классы](#Классы)
    *   [ProductType](#ProductType)
    *   [SortBy](#SortBy)
    *   [LinkType](#LinkType)

## Классы

### `ProductType`

**Описание**: Класс `ProductType` представляет типы продуктов, которые могут быть запрошены в API AliExpress.

**Атрибуты**:
- `ALL`: Представляет все типы продуктов.
- `PLAZA`: Представляет продукты, доступные на AliExpress Plaza.
- `TMALL`: Представляет продукты, доступные на AliExpress Tmall.

### `SortBy`

**Описание**: Класс `SortBy` представляет способы сортировки продуктов, полученных из API AliExpress.

**Атрибуты**:
- `SALE_PRICE_ASC`: Сортировка по цене продажи по возрастанию.
- `SALE_PRICE_DESC`: Сортировка по цене продажи по убыванию.
- `LAST_VOLUME_ASC`: Сортировка по последним продажам по возрастанию.
- `LAST_VOLUME_DESC`: Сортировка по последним продажам по убыванию.

### `LinkType`

**Описание**: Класс `LinkType` представляет типы ссылок, используемых в API AliExpress.

**Атрибуты**:
- `NORMAL`: Представляет обычную ссылку.
- `HOTLINK`: Представляет горячую ссылку.