# Модуль `hotproducts`

## Обзор

Модуль `hotproducts` определяет структуру данных для представления ответа, содержащего список популярных товаров (Hot Products) с платформы AliExpress. Он включает класс `HotProductsResponse`, который содержит информацию о текущей странице, количестве записей на странице, общем количестве записей и списке товаров, представленных классом `Product`.

## Подробней

Этот модуль предназначен для обработки данных, возвращаемых API AliExpress при запросе списка популярных товаров. Он обеспечивает структурированное представление данных, что упрощает их дальнейшую обработку и использование в других частях проекта `hypotez`. В частности, он определяет типы данных для различных полей ответа, что помогает обеспечить надежность и предсказуемость работы с API. Расположение файла `/src/suppliers/aliexpress/api/models/hotproducts.py` указывает, что этот модуль является частью подсистемы, отвечающей за взаимодействие с API AliExpress, в частности, для получения информации о популярных товарах.

## Классы

### `HotProductsResponse`

**Описание**: Класс `HotProductsResponse` представляет ответ, содержащий список популярных товаров с AliExpress.

**Методы**:
- Отсутствуют

**Параметры**:
- `current_page_no` (int): Номер текущей страницы в ответе.
- `current_record_count` (int): Количество записей на текущей странице.
- `total_record_count` (int): Общее количество записей (товаров).
- `products` (List[Product]): Список объектов `Product`, представляющих товары на текущей странице.

**Примеры**:
```python
# Пример создания экземпляра класса HotProductsResponse
from typing import List
from src.suppliers.aliexpress.api.models.product import Product

class HotProductsResponse:
    def __init__(self, current_page_no: int, current_record_count: int, total_record_count: int, products: List[Product]):
        self.current_page_no = current_page_no
        self.current_record_count = current_record_count
        self.total_record_count = total_record_count
        self.products = products

# Пример использования:
products_list = [Product(product_id='12345', product_title='Example Product')]  # Предполагается, что класс Product определен в другом месте
hot_products_response = HotProductsResponse(current_page_no=1, current_record_count=1, total_record_count=10, products=products_list)

print(hot_products_response.current_page_no)
# 1
print(hot_products_response.products[0].product_title)
# Example Product
```