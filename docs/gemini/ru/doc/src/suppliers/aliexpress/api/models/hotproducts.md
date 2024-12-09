# Модуль `hypotez/src/suppliers/aliexpress/api/models/hotproducts.py`

## Обзор

Данный модуль содержит определение класса `HotProductsResponse`, представляющего ответ API AliExpress для горячих товаров. Класс содержит информацию о текущей странице, количестве записей на текущей странице, общем количестве записей и списке продуктов.

## Оглавление

- [Модуль `HotProductsResponse`](#модуль-hotproductsresponse)


## Классы

### `HotProductsResponse`

**Описание**: Класс `HotProductsResponse` предназначен для хранения данных, возвращаемых API AliExpress при запросе горячих товаров.  Он содержит информацию о текущей странице, количестве продуктов на текущей странице, общем количестве продуктов и списке продуктов.

**Атрибуты**:

- `current_page_no` (int): Номер текущей страницы.
- `current_record_count` (int): Количество продуктов на текущей странице.
- `total_record_count` (int): Общее количество продуктов.
- `products` (List[Product]): Список объектов `Product`, представляющих горячие товары.

```python
class HotProductsResponse:
    current_page_no: int
    current_record_count: int
    total_record_count: int
    products: List[Product]
```