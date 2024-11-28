Как использовать модуль bangood
========================================================================================

Описание
-------------------------
Данный модуль (`hypotez/src/suppliers/bangood/__init__.py`) предоставляет функции для работы с сайтом Banggood. Он импортирует классы и функции из подмодулей `graber` и `scenario`, предназначенных для сбора данных о категориях и продуктах.  Константа `MODE` установлена в 'dev'.

Шаги выполнения
-------------------------
1. Модуль импортирует необходимые классы и функции из подмодулей `graber` и `scenario`: `Graber`, `get_list_categories_from_site`, `get_list_products_in_category`.
2. Устанавливает константу `MODE` со значением 'dev'.  Это, скорее всего, конфигурационная переменная, определяющая режим работы модуля (например, режим разработки).

Пример использования
-------------------------
.. code-block:: python

    from hypotez.src.suppliers.bangood import Graber, get_list_categories_from_site, get_list_products_in_category

    # Получение списка категорий с сайта Banggood
    categories = get_list_categories_from_site()
    print(categories)

    # Пример работы с классом Graber (предполагается, что у него есть метод для работы с конкретным продуктом)
    graber = Graber()  #  инициализируем объект Graber
    # Пример, как использовать  graber (предполагаем метод для получения данных о продуктах)
    product_data = graber.get_product_details(product_id=12345)  # Замените 12345 на реальный ID продукта
    print(product_data)

    # Получение списка продуктов в заданной категории
    selected_category = 'Electronics'  # Замените на реальное значение
    products = get_list_products_in_category(category_name=selected_category)
    print(products)