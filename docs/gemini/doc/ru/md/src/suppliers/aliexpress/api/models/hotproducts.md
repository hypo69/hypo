# Модуль hypotez/src/suppliers/aliexpress/api/models/hotproducts.py

## Обзор

Данный модуль содержит класс `HotProductsResponse`, который представляет собой ответ API для получения горячих продуктов. Класс описывает структуру ответа, содержащую информацию о текущей странице, количестве записей на текущей странице и во всем списке, а также список продуктов.

## Оглавление

* [Модуль](#модуль-hypotezsrcsuppliersaliexpressapimodels-hotproducts-py)
* [Класс HotProductsResponse](#класс-hotproductsresponse)


## Класс HotProductsResponse

### `HotProductsResponse`

**Описание**: Класс `HotProductsResponse` представляет структуру ответа API для получения списка горячих продуктов. Он содержит информацию о текущей странице, количестве записей на текущей странице, общее количество записей и список продуктов.

**Атрибуты**:

- `current_page_no` (int): Номер текущей страницы.
- `current_record_count` (int): Количество записей на текущей странице.
- `total_record_count` (int): Общее количество записей.
- `products` (List[Product]): Список продуктов.


```python
class HotProductsResponse:
    current_page_no: int
    current_record_count: int
    total_record_count: int
    products: List[Product]
```
```
```
**Примечание**: В данном модуле предполагается, что класс `Product` определен в другом месте (возможно, в файле `product.py`).