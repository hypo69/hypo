# Модуль `hypotez/src/suppliers/aliexpress/api/models/hotproducts.py`

## Обзор

Модуль содержит определение класса `HotProductsResponse`, который представляет ответ API для получения горячих продуктов.  Класс содержит информацию о текущей странице, количестве записей на странице, общем количестве записей и списке продуктов.

## Оглавление

* [Классы](#классы)
    * [HotProductsResponse](#hotproductsresponse)

## Классы

### `HotProductsResponse`

**Описание**: Класс представляет ответ API для получения горячих продуктов.

**Атрибуты**:

- `current_page_no` (int): Номер текущей страницы.
- `current_record_count` (int): Количество записей на текущей странице.
- `total_record_count` (int): Общее количество записей.
- `products` (List[Product]): Список объектов `Product`.


```
```python
from .product import Product
from typing import List


class HotProductsResponse:
    current_page_no: int
    current_record_count: int
    total_record_count: int
    products: List[Product]