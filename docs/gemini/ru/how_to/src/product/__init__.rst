Как использовать модуль hypotez/src/product
========================================================================================

Описание
-------------------------
Модуль `hypotez/src/product` предоставляет классы и функции для работы с продуктами.  Он содержит классы `Product` и `ProductFields`, а также функцию `translate_presta_fields_dict` для работы с данными продуктов. Также определен словарь `record` для хранения данных продуктов в плоском формате.  Модуль определяет константу `MODE`,  вероятно используемую для управления режимами работы.

Шаги выполнения
-------------------------
1. Импортируйте необходимые классы и функции из соответствующих файлов:
    ```python
    from .product import Product
    from .product_fields.product_fields import ProductFields
    from .product_fields.product_fields_translator import translate_presta_fields_dict
    ```

2. Используйте класс `Product` для работы с объектами продуктов.  Подробности о методах и атрибутах этого класса описаны в файле `product.py`.

3. Используйте класс `ProductFields` для работы с полями продуктов. Подробности о методах и атрибутах этого класса описаны в файле `product_fields.py`.

4. Используйте функцию `translate_presta_fields_dict`, чтобы перевести многоязычные поля `ProductFields`.  Функция ожидает словарь в качестве аргумента, вероятно, содержащий исходные данные полей.  Подробности о возвращаемом значении и параметрах функции находятся в файле `product_fields_translator.py`.

5. Используйте словарь `record` для доступа к данным продуктов в плоском формате.

6.  Используйте константу `MODE` для управления режимом работы (например, `dev`, `prod`).


Пример использования
-------------------------
.. code-block:: python

    # Пример использования класса Product
    my_product = Product(product_id=123, name="My Product")
    print(my_product.name)

    # Пример использования ProductFields
    fields = ProductFields(my_product.product_id)  # Предполагается, что product_id существует
    translated_fields = translate_presta_fields_dict(fields.presta_fields)
    # ... дальнейшие действия с переведёнными полями ...

    # Пример использования record (если доступно)
    if 'record' in locals():
        product_data = record.get(123)
        if product_data:
            print(product_data.get('name'))

    # Пример использования константы MODE
    if MODE == 'dev':
        print("Запущен в режиме разработки")