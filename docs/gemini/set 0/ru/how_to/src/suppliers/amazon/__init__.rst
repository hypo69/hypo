Как использовать этот блок кода
=========================================================================================

Описание
-------------------------
Этот файл `hypotez/src/suppliers/amazon/__init__.py` является инициализатором модуля, отвечающего за работу с поставщиком Amazon. Он импортирует классы и функции, необходимые для взаимодействия с API Amazon, такие как `Graber` для сбора данных и `get_list_products_in_category` для получения списка продуктов по категории.  Файл также определяет константу `MODE`, которая, вероятно, указывает на режим работы (например, `dev`, `prod`).

Шаги выполнения
-------------------------
1. Импортируются необходимые классы и функции: `Graber` и `get_list_products_in_category` из соответствующих файлов в подпапке `amazon`.
2. Определяется константа `MODE` со значением 'dev'. Это указывает на режим работы. Вероятно, в других сценариях это значение может быть иным (например, 'prod').

Пример использования
-------------------------
.. code-block:: python

    from hypotez.src.suppliers.amazon import Graber, get_list_products_in_category

    # Пример использования функции get_list_products_in_category
    products = get_list_products_in_category("Electronics", "Laptops")
    if products:
        for product in products:
            print(product)

    # Пример использования класса Graber
    graber = Graber()
    data = graber.fetch_data()
    if data:
        print(data)