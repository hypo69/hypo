Как использовать этот блок кода
=========================================================================================

Описание
-------------------------
Этот код определяет класс `HotProductsResponse`, который представляет собой ответ от API AliExpress.  Он описывает структуру данных, содержащую информацию о популярных продуктах. Класс содержит поля для номера текущей страницы, количества записей на текущей странице, общего количества записей и списка продуктов.  Этот класс использует тип `List[Product]` для хранения списка объектов `Product`.

Шаги выполнения
-------------------------
1. Импортируются необходимые модули: `Product` и `List` из модуля `typing`.
2. Определяется класс `HotProductsResponse`, который содержит следующие атрибуты:
    - `current_page_no`: Целочисленное значение, обозначающее номер текущей страницы.
    - `current_record_count`: Целочисленное значение, обозначающее количество записей на текущей странице.
    - `total_record_count`: Целочисленное значение, обозначающее общее количество записей.
    - `products`: Список объектов `Product`, содержащий информацию о продуктах.

Пример использования
-------------------------
.. code-block:: python

    from .product import Product
    from typing import List
    from hypotez.src.suppliers.aliexpress.api.models.hotproducts import HotProductsResponse

    # Пример создания объекта Product
    product1 = Product(id=123, title='Example Product', price=10.99)
    product2 = Product(id=456, title='Another Product', price=20.50)

    # Создание списка продуктов
    products_list: List[Product] = [product1, product2]

    # Создание объекта HotProductsResponse
    response = HotProductsResponse(
        current_page_no=1,
        current_record_count=2,
        total_record_count=10,
        products=products_list
    )

    # Доступ к данным из ответа
    print(response.current_page_no)  # Выведет 1
    print(response.products[0].title) # Выведет 'Example Product'