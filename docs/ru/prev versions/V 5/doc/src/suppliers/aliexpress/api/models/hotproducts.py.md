# Модуль `hotproducts`

## Обзор

Модуль содержит класс `HotProductsResponse`, который представляет собой структуру данных для хранения информации об ответе, содержащем список популярных товаров (hot products) с AliExpress. Он включает в себя информацию о текущей странице, количестве записей на текущей странице, общем количестве записей и список самих товаров.

## Подробней

Данный модуль предназначен для организации данных, возвращаемых API AliExpress при запросе списка популярных товаров. Класс `HotProductsResponse` служит контейнером для хранения этих данных, что облегчает их дальнейшую обработку и использование в других частях проекта `hypotez`. Информация о товарах представлена в виде списка объектов класса `Product`, импортированного из модуля `product`.

## Классы

### `HotProductsResponse`

**Описание**: Класс, представляющий ответ, содержащий список популярных товаров.

**Как работает класс**:
Класс `HotProductsResponse` предназначен для хранения данных, полученных в ответ на запрос популярных товаров с AliExpress. Он содержит атрибуты, описывающие текущую страницу, количество товаров на странице и общее количество товаров, а также список объектов `Product`, представляющих сами товары.

**Методы**:
- Отсутствуют

**Параметры**:
- `current_page_no` (int): Номер текущей страницы.
- `current_record_count` (int): Количество записей (товаров) на текущей странице.
- `total_record_count` (int): Общее количество записей (товаров) во всех страницах.
- `products` (List[Product]): Список объектов `Product`, представляющих товары на текущей странице.

**Примеры**:

```python
# Пример создания объекта HotProductsResponse
from typing import List
class Product:
    product_id: int
    product_title: str
    product_price: float
    product_url: str
class HotProductsResponse:
    current_page_no: int
    current_record_count: int
    total_record_count: int
    products: List[Product]

product1 = Product()
product1.product_id = 123
product1.product_title = 'Example Product 1'
product1.product_price = 10.0
product1.product_url = 'http://example.com/product1'

product2 = Product()
product2.product_id = 456
product2.product_title = 'Example Product 2'
product2.product_price = 20.0
product2.product_url = 'http://example.com/product2'

hot_products_response = HotProductsResponse()
hot_products_response.current_page_no = 1
hot_products_response.current_record_count = 2
hot_products_response.total_record_count = 20
hot_products_response.products = [product1, product2]
```