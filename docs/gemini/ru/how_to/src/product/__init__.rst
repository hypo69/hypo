Как использовать модуль product
========================================================================================

Описание
-------------------------
Модуль `hypotez/src/product/__init__.py` импортирует классы и функции, относящиеся к продуктам. Он предоставляет доступ к классу `Product`, `ProductFields`, функции перевода многоязычных полей `translate_presta_fields_dict`, а также  `record` – словарь полей продукта в плоском формате.

Шаги выполнения
-------------------------
1. Импортирует классы `Product` и `ProductFields` из соответствующих модулей (`product.py` и `product_fields.py`).
2. Импортирует функцию `translate_presta_fields_dict` для перевода многоязычных полей `ProductFields`.
3. Определяет константу `MODE`,  предположительно, для выбора режима работы (например, разработки, производства).
4. Предоставляет доступ к функциям и классам для работы с продуктами.

Пример использования
-------------------------
.. code-block:: python

    from hypotez.src.product import Product, ProductFields, translate_presta_fields_dict

    # Пример создания объекта Product (предполагается, что в product.py есть конструктор)
    my_product = Product(product_id=123, name="My Product")

    # Пример использования ProductFields (предполагается, что в product_fields.py есть необходимые методы)
    product_fields = ProductFields(product_id=123)
    translated_fields = translate_presta_fields_dict(product_fields, "en")

    # Пример работы с record (предполагается, что record - это словарь, заполненный данными)
    product_record = {'name': 'My Product', 'price': 10}
    print(product_record['name'])

    # Пример использования константы MODE
    if MODE == 'dev':
        print("Текущий режим - разработка")