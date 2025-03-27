# Модуль `hotproducts`

## Обзор

Модуль `hotproducts` определяет модель данных для представления ответа, содержащего список популярных продуктов с AliExpress. Он включает класс `HotProductsResponse`, который содержит информацию о текущей странице, количестве записей на странице, общем количестве записей и списке продуктов.

## Подробнее

Этот модуль используется для структурированного представления данных, полученных из API AliExpress, касающихся популярных продуктов. Класс `HotProductsResponse` позволяет удобно хранить и передавать информацию о пагинации и списке продуктов.

## Классы

### `HotProductsResponse`

**Описание**: Класс, представляющий ответ, содержащий список популярных продуктов.

**Методы**:
- Нет явных методов, класс используется как структура данных.

**Параметры**:
- `current_page_no` (int): Номер текущей страницы.
- `current_record_count` (int): Количество записей на текущей странице.
- `total_record_count` (int): Общее количество записей.
- `products` (List[Product]): Список объектов `Product`, представляющих популярные продукты.

**Примеры**:

```python
from src.suppliers.aliexpress.api.models.hotproducts import HotProductsResponse
from src.suppliers.aliexpress.api.models.product import Product

# Пример создания экземпляра класса HotProductsResponse
hot_products_response = HotProductsResponse()
hot_products_response.current_page_no = 1
hot_products_response.current_record_count = 10
hot_products_response.total_record_count = 100
hot_products_response.products = [Product(), Product()]  # Пример списка продуктов