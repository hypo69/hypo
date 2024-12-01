Как использовать модуль `aliexpress.api.tools`
========================================================================================

Описание
-------------------------
Модуль `aliexpress.api.tools` содержит вспомогательную функцию `get_product_id` для получения идентификатора продукта с сайта AliExpress.

Шаги выполнения
-------------------------
1. Импортировать функцию `get_product_id` из модуля `aliexpress.api.tools`.
2. Вызвать функцию `get_product_id` с необходимыми аргументами (например, с информацией о продукте).
3. Функция вернет идентификатор продукта.

Пример использования
-------------------------
.. code-block:: python

    from hypotez.src.suppliers.aliexpress.api.tools import get_product_id

    # Пример данных для поиска идентификатора продукта
    product_data = {
        'product_name': 'Xiaomi Redmi Note 11',
        'seller_id': '12345',
        # Добавьте другие необходимые данные
    }

    try:
        product_id = get_product_id(product_data)
        if product_id:
            print(f"Идентификатор продукта: {product_id}")
        else:
            print("Идентификатор продукта не найден.")
    except Exception as e:
        print(f"Ошибка при получении идентификатора: {e}")