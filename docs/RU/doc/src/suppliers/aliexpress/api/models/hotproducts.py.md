# Модуль `hypotez/src/suppliers/aliexpress/api/models/hotproducts.py`

## Обзор

Модуль `hotproducts.py` содержит модели данных, используемые для представления ответа, содержащего список горячих товаров (продуктов) от AliExpress.

## Оглавление

1.  [Классы](#классы)
    *   [HotProductsResponse](#hotproductsresponse)

## Классы

### `HotProductsResponse`

**Описание**: Класс для представления ответа, содержащего список горячих товаров.

**Атрибуты**:

*   `current_page_no` (int): Номер текущей страницы.
*   `current_record_count` (int): Количество записей на текущей странице.
*   `total_record_count` (int): Общее количество записей.
*   `products` (List[Product]): Список объектов `Product`, представляющих горячие товары.