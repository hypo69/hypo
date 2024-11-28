Как использовать модуль product
========================================================================================

Описание
-------------------------
Модуль `product` содержит функциональность для работы с продуктами. Он включает в себя определение локаторов для веб-элементов, управление данными продуктов, управление полями продуктов, а также управление версиями модуля. Модуль предоставляет примеры использования и документацию.

Шаги выполнения
-------------------------
1. **Импортировать необходимые модули**: Импортируйте классы `Product` и `ProductFields` из соответствующих файлов модуля:
   ```python
   from product.product import Product
   from product.product_fields import ProductFields
   ```
2. **Инициализировать объекты**: Создайте экземпляры классов `Product` и `ProductFields`:
   ```python
   product = Product()
   product_fields = ProductFields()
   ```
3. **Получить данные продукта**: Используйте метод `get_product_data` класса `Product`, передав идентификатор продукта в качестве аргумента:
   ```python
   product_data = product.get_product_data(product_id="12345")
   ```
4. **Обновить поле продукта**: Используйте метод `update_field` класса `ProductFields`, передав имя поля и новое значение:
   ```python
   product_fields.update_field("price", 19.99)
   ```
5. **Вывести данные**: Выведите полученные данные продукта на экран:
   ```python
   print(product_data)
   ```

Пример использования
-------------------------
.. code-block:: python

    from product.product import Product
    from product.product_fields import ProductFields

    # Инициализировать объекты
    product = Product()
    product_fields = ProductFields()

    # Получить данные продукта с ID 12345
    product_data = product.get_product_data(product_id="12345")

    # Обновить поле "price" на 19.99
    product_fields.update_field("price", 19.99)

    # Вывести данные продукта
    print(product_data)
```