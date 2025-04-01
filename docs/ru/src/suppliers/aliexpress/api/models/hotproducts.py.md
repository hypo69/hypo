# Модуль `hotproducts`

## Обзор

Модуль `hotproducts` содержит классы для представления ответа с горячими продуктами от AliExpress API. Основной класс `HotProductsResponse` используется для хранения информации о текущей странице, количестве записей на странице, общем количестве записей и списке продуктов.

## Подробней

Этот модуль определяет структуру данных, которая соответствует формату ответа API AliExpress для запросов горячих продуктов. Он включает класс `HotProductsResponse`, который содержит информацию о пагинации и список объектов `Product`. Класс `Product` импортируется из модуля `product`.

## Классы

### `HotProductsResponse`

**Описание**: Класс `HotProductsResponse` представляет собой структуру данных для хранения ответа, содержащего информацию о горячих продуктах.

**Принцип работы**:
Класс содержит атрибуты, соответствующие полям ответа API AliExpress:
- `current_page_no`: номер текущей страницы.
- `current_record_count`: количество записей на текущей странице.
- `total_record_count`: общее количество записей.
- `products`: список объектов `Product`, представляющих горячие продукты на текущей странице.

```python
class HotProductsResponse:
    current_page_no: int
    current_record_count: int
    total_record_count: int
    products: List[Product]
```

**Параметры**:
- `current_page_no` (int): Номер текущей страницы.
- `current_record_count` (int): Количество записей на текущей странице.
- `total_record_count` (int): Общее количество записей.
- `products` (List[Product]): Список объектов `Product`.

**Примеры**:

```python
from typing import List
from .product import Product

# Пример создания экземпляра класса HotProductsResponse
products: List[Product] = []  # Предположим, что у вас есть список объектов Product
hot_products_response = HotProductsResponse()
hot_products_response.current_page_no = 1
hot_products_response.current_record_count = 10
hot_products_response.total_record_count = 100
hot_products_response.products = products

print(f"Current Page No: {hot_products_response.current_page_no}")
print(f"Current Record Count: {hot_products_response.current_record_count}")
print(f"Total Record Count: {hot_products_response.total_record_count}")
print(f"Products: {hot_products_response.products}")