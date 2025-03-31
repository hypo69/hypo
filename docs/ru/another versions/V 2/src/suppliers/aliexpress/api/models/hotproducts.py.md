# Модуль `hotproducts`

## Обзор

Модуль `hotproducts` содержит модель данных для ответа, содержащего список горячих товаров с AliExpress.

## Содержание

- [Классы](#классы)
    - [`HotProductsResponse`](#hotproductsresponse)

## Классы

### `HotProductsResponse`

**Описание**: Класс, представляющий ответ с горячими товарами.

**Атрибуты**:
- `current_page_no` (int): Номер текущей страницы.
- `current_record_count` (int): Количество записей на текущей странице.
- `total_record_count` (int): Общее количество записей.
- `products` (List[Product]): Список товаров типа `Product`.