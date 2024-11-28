Как использовать модуль product_fields
========================================================================================

Описание
-------------------------
Модуль `product_fields` содержит классы и функции для работы с полями товаров. Он предоставляет интерфейс для взаимодействия с полями товара, а также содержит функцию для перевода словарей полей из PrestaShop в внутренний формат.  В частности, он определяет константу `MODE` и импортирует класс `ProductFields` и функцию `translate_presta_fields_dict` из соответствующих модулей.


Шаги выполнения
-------------------------
1. Импортировать необходимый класс и/или функцию из модуля. Например, для работы с полями товара, импортируется класс `ProductFields`:

   .. code-block:: python

       from hypotez.src.product.product_fields import ProductFields

2.  (Если требуется) использовать функцию `translate_presta_fields_dict` для перевода словаря полей из PrestaShop в внутренний формат.

   .. code-block:: python

       from hypotez.src.product.product_fields import translate_presta_fields_dict

       presta_fields = {'field1': 'value1', 'field2': 'value2'}
       translated_fields = translate_presta_fields_dict(presta_fields)


3. (Если используется класс `ProductFields`) создать экземпляр класса `ProductFields`.

   .. code-block:: python

       product_fields_instance = ProductFields()

4.  (Если используется класс `ProductFields`) Выполнить необходимые действия с полями товара, используя методы класса. (Например, получение, изменение или проверку полей).  Пример методов, которые *могут* быть доступны в классе `ProductFields` (зависит от реализации) - неизвестен без доступа к полному коду класса.

   .. code-block:: python
       #Пример использования методов класса (предполагается, что они существуют)
       field_value = product_fields_instance.get_field_value('name')
       product_fields_instance.set_field_value('name', 'New Name')
       is_valid = product_fields_instance.validate_field('price', 10.00)
       


Пример использования
-------------------------
.. code-block:: python

    from hypotez.src.product.product_fields import ProductFields, translate_presta_fields_dict

    # Пример словаря полей PrestaShop
    presta_fields = {'name': 'Название', 'price': 'Цена'}

    # Перевод словаря
    translated_fields = translate_presta_fields_dict(presta_fields)
    print(translated_fields)

    # Создание экземпляра класса ProductFields
    product_fields_instance = ProductFields()


    # Пример использования методов класса (предполагается, что такие методы существуют)
    # (Замените 'field_name' и 'new_value' на актуальные названия полей и новые значения)
    field_name = "name"
    new_value = "New Product Name"
    try:
        product_fields_instance.set_field_value(field_name, new_value)
        print(f"Значение поля '{field_name}' успешно обновлено до '{new_value}'.")
    except Exception as e:
        print(f"Ошибка при обновлении поля '{field_name}': {e}")