Как использовать модуль bangood
========================================================================================

Описание
-------------------------
Модуль `bangood` предоставляет функции для работы с сайтом Banggood. Он содержит классы и функции для получения списка категорий и продуктов в заданной категории.  Этот модуль настроен на работу с сайтом Banggood в режиме "dev".

Шаги выполнения
-------------------------
1. Импортируйте необходимые функции из модуля `bangood`:
   ```python
   from hypotez.src.suppliers.bangood import Graber, get_list_categories_from_site, get_list_products_in_category
   ```

2. Для получения списка категорий используйте функцию `get_list_categories_from_site()`:
   ```python
   categories = get_list_categories_from_site()
   ```
   Эта функция возвращает список категорий, представленных как объекты, содержащие информацию о категориях.

3. Для получения списка продуктов в заданной категории используйте функцию `get_list_products_in_category()`:
   ```python
   category_id = 123 # Замените на id нужной категории
   products = get_list_products_in_category(category_id)
   ```
   Функция `get_list_products_in_category()` принимает идентификатор категории и возвращает список продуктов в этой категории, также представленные как объекты, содержащие подробную информацию о продуктах.

4. Для получения более глубокой информации о продукте или других действиях с сайтом, возможно, потребуется использовать класс `Graber`.


Пример использования
-------------------------
.. code-block:: python

    from hypotez.src.suppliers.bangood import get_list_categories_from_site, get_list_products_in_category

    # Получение списка категорий
    categories = get_list_categories_from_site()
    for category in categories:
        print(f"Категория: {category.name}, ID: {category.id}")


    # Получение списка продуктов в определенной категории (замените 123 на фактический ID категории)
    category_id = 123
    products = get_list_products_in_category(category_id)
    for product in products:
        print(f"Название продукта: {product.name}, Цена: {product.price}")