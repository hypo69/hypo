Как использовать этот блок кода
=========================================================================================

Описание
-------------------------
Этот код определяет класс `HotProductsResponse`, который представляет ответ API для получения списка популярных продуктов (hot products) с AliExpress.  Класс содержит атрибуты для номера текущей страницы, количества записей на текущей странице, общего количества записей и списка продуктов (`products`).  Класс наследуется от класса `Product`.

Шаги выполнения
-------------------------
1. Импортируются необходимые модули: `Product` и `List` из модуля `typing`.
2. Определяется класс `HotProductsResponse`.
3. Класс `HotProductsResponse` имеет атрибуты:
    - `current_page_no`: Целое число, представляющее номер текущей страницы результатов.
    - `current_record_count`: Целое число, представляющее количество продуктов на текущей странице.
    - `total_record_count`: Целое число, представляющее общее количество продуктов.
    - `products`: Список объектов `Product`, содержащий полученные данные о продуктах.


Пример использования
-------------------------
.. code-block:: python

    from hypotez.src.suppliers.aliexpress.api.models.hotproducts import HotProductsResponse
    from hypotez.src.suppliers.aliexpress.api.models.product import Product

    # Пример данных (замените на реальные данные)
    product_data1 = {'id': 123, 'name': 'Product 1', 'price': 10.99}
    product_data2 = {'id': 456, 'name': 'Product 2', 'price': 20.50}

    product_list = [
        Product(**product_data1),
        Product(**product_data2)
    ]

    response = HotProductsResponse(
        current_page_no=1,
        current_record_count=2,
        total_record_count=10,
        products=product_list
    )

    # Обработка данных ответа
    print(f"Текущая страница: {response.current_page_no}")
    print(f"Количество продуктов на странице: {response.current_record_count}")
    print(f"Общее количество продуктов: {response.total_record_count}")

    for product in response.products:
        print(f"ID: {product.id}, Название: {product.name}, Цена: {product.price}")