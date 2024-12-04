Как использовать функции parse_product и parse_products
========================================================================================

Описание
-------------------------
Функция `parse_product` обрабатывает объект `product`, извлекая и форматируя значение атрибута `product_small_image_urls`.  Функция `parse_products` обрабатывает список объектов `products`, применяя `parse_product` к каждому элементу списка и возвращает новый список обработанных объектов.

Шаги выполнения
-------------------------
1. Функция `parse_product` принимает на вход объект `product`.
2. Она извлекает строковое представление значения атрибута `product_small_image_urls` объекта `product` и присваивает его атрибуту `product_small_image_urls` объекта `product`.
3. Функция возвращает изменённый объект `product`.
4. Функция `parse_products` принимает на вход список объектов `products`.
5. Она итерируется по каждому объекту `product` в списке.
6. Для каждого объекта она вызывает функцию `parse_product`, передавая объект в качестве аргумента.
7. Результат вызова `parse_product` (изменённый объект `product`) добавляется в новый список `new_products`.
8. Функция возвращает новый список `new_products` с обработанными объектами.

Пример использования
-------------------------
.. code-block:: python

    from typing import List
    from dataclasses import dataclass
    
    @dataclass
    class Product:
        product_small_image_urls: str = None


    products_list = [
        Product(product_small_image_urls='<html><body>some_url</body></html>'),
        Product(product_small_image_urls='<html><body>another_url</body></html>'),
    ]

    from hypotez.src.suppliers.aliexpress.api.helpers.products import parse_product, parse_products

    parsed_products = parse_products(products_list)

    for product in parsed_products:
        print(product.product_small_image_urls)