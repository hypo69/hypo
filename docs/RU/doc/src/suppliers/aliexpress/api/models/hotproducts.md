# Модуль hypotez/src/suppliers/aliexpress/api/models/hotproducts.py

## Обзор

Этот модуль содержит определение класса `HotProductsResponse`, который представляет собой ответ API AliExpress для горячих продуктов.  Класс содержит информацию о текущей странице, количестве записей на текущей странице, общем количестве записей и списке продуктов.

## Оглавление

* [Модуль `HotProductsResponse`](#модуль-hotproductsresponse)


## Модуль `HotProductsResponse`

### Класс `HotProductsResponse`

**Описание**: Класс `HotProductsResponse` предназначен для хранения данных, возвращаемых API AliExpress о горячих продуктах.  Он содержит информацию о текущей странице, количестве записей на ней, общем количестве записей и списке продуктов.

**Атрибуты**:

* `current_page_no` (int): Номер текущей страницы в результатах поиска.
* `current_record_count` (int): Количество продуктов на текущей странице.
* `total_record_count` (int): Общее количество продуктов, соответствующих запросу.
* `products` (List[Product]): Список объектов `Product`, представляющих горячие продукты.

```python
class HotProductsResponse:
    current_page_no: int
    current_record_count: int
    total_record_count: int
    products: List[Product]
```
```
```
```
```