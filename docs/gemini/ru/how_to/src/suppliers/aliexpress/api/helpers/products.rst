Как использовать этот блок кода
=========================================================================================

Описание
-------------------------
Модуль `products.py` содержит две функции: `parse_product` и `parse_products`. Функция `parse_product` преобразует объект `product`, изменяя атрибут `product_small_image_urls` в строку. Функция `parse_products` применяет функцию `parse_product` ко всем элементам списка `products`, возвращая новый список `new_products` с измененными объектами.

Шаги выполнения
-------------------------
1. Функция `parse_product` принимает на вход объект `product`.
2. Она извлекает значение атрибута `product_small_image_urls` объекта `product`.
3. Она присваивает извлеченное значение (как строку) атрибуту `product_small_image_urls` объекта `product`.
4. Функция возвращает измененный объект `product`.
5. Функция `parse_products` принимает на вход список `products`.
6. Она итерируется по каждому элементу (объекту `product`) в списке `products`.
7. Для каждого объекта `product` она вызывает функцию `parse_product`, передавая этот объект в качестве аргумента.
8. Результатом вызова `parse_product` является измененный объект `product`.
9. Измененный объект добавляется в новый список `new_products`.
10. После обработки всех элементов списка `products` функция возвращает новый список `new_products` с измененными объектами.


Пример использования
-------------------------
.. code-block:: python

    from hypotez.src.suppliers.aliexpress.api.helpers.products import parse_product, parse_products

    # Пример данных (замените на ваши данные)
    example_products = [
        {'product_small_image_urls': ['url1', 'url2']},
        {'product_small_image_urls': ['url3']},
    ]

    # Применяем parse_products к списку продуктов
    processed_products = parse_products(example_products)
    
    # Выводим результат
    for product in processed_products:
        print(product)