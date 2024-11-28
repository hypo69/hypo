Как использовать класс ProductFields
========================================================================================

Описание
-------------------------
Класс `ProductFields` предназначен для работы с полями товаров в формате API PrestaShop. Он предоставляет методы для получения, установки и работы с данными, связанными с товарами в базе данных PrestaShop, включая как основные поля, так и дополнительные поля для категорий, изображений, метаданных и т.д.  Класс позволяет загружать данные полей из файла `fields_list.txt`, а также загружать значения по умолчанию из `product_fields_default_values.json`.  Класс содержит свойства (properties) и методы для доступа к данным полей товара,  поддерживая алфавитный порядок.

Шаги выполнения
-------------------------
1. **Импортирование необходимых библиотек**:
   Импортируются необходимые модули, такие как `pydantic`, `SimpleNamespace`, `Path`, `j_loads`, `StringNormalizer`,  `StringFormatter`, `read_text_file` и `logger` для обработки данных, работы с файлами и ведения логов.


2. **Инициализация класса `ProductFields`**:
   Создается экземпляр класса `ProductFields`.  В конструкторе происходит загрузка списка полей из файла `fields_list.txt`. Также создается словарь `language` и служебный словарь `assist_fields_dict`.  Обратите внимание, что класс использует `SimpleNamespace` для хранения данных полей товара. Важная часть инициализации - вызов метода `_payload()`, который загружает значения по умолчанию из файла `product_fields_default_values.json`.


3. **Доступ к полям товара**:
   После инициализации можно получить доступ к полям товара с помощью свойств (properties) класса, например, `product_fields.id_product`, `product_fields.name`, и т.д. Свойства `id_product`, `id_supplier`, `id_manufacturer` и другие работают как getter-setter (с использованием декораторов `@property` и `@setter`). Это позволяет и получать значение поля и изменять его. Методы `@property` (getters) возвращают значения полей, а `@setter` (setters) устанавливают значения в соответствующее поле.

4. **Установка значений полей**:
   Для установки значений полей используются setters, например,  `product_fields.id_product = 123`.

5. **Работа с дополнительными полями**:
   Класс предоставляет методы для работы с дополнительными полями, такими как `additional_categories`, `images_urls`, и т.д.  Эти поля обрабатываются несколько сложнее, так как  они, возможно, представляют собой сложные структуры данных (списки словарей).

6. **Обработка ошибок**:
   Класс содержит обработку исключений `ProductFieldException` для перехватывания ошибок при работе с полями.

Пример использования
-------------------------
.. code-block:: python

    from hypotez.src.product.product_fields.product_fields import ProductFields

    # Создание экземпляра класса
    product_fields = ProductFields()

    # Установка значения поля id_product
    product_fields.id_product = 10

    # Получение значения поля id_product
    product_id = product_fields.id_product

    # Вывод значения id_product
    print(f"ID продукта: {product_id}")


    # пример для поля с дополнительными категориями
    product_fields.additional_categories = [1, 2, 3]
    additional_cats = product_fields.additional_categories
    print(f"Дополнительные категории: {additional_cats}")


    #Пример работы со значением `name`
    product_fields.name = "My Product Name" , 'ru'
    product_name = product_fields.name
    print(f"Имя продукта (ru): {product_name}")