Как использовать этот блок кода
=========================================================================================

Описание
-------------------------
Этот код определяет две класса: `Category` и `ChildCategory`.  Класс `Category` представляет собой базовую категорию и содержит атрибуты `category_id` (идентификатор категории) и `category_name` (название категории).  Класс `ChildCategory` наследуется от `Category` и добавляет атрибут `parent_category_id` (идентификатор родительской категории).

Шаги выполнения
-------------------------
1. Определяется базовый класс `Category` с атрибутами `category_id` и `category_name`. Это означает, что все экземпляры этого класса будут содержать эти поля.
2. Определяется класс `ChildCategory`, который наследуется от `Category`.  Это означает, что `ChildCategory` получает все атрибуты и методы класса `Category`, а также дополнительно имеет атрибут `parent_category_id`.
3.  Атрибуты `category_id`, `category_name` и `parent_category_id` объявляются как типы данных (int и str соответственно). Это позволяет статической проверке типов, таких как MyPy,  используя анотации типов.


Пример использования
-------------------------
.. code-block:: python

    from hypotez.src.suppliers.aliexpress.api.models.category import Category, ChildCategory

    # Создаем экземпляр класса Category
    electronics_category = Category(
        category_id=1,
        category_name="Electronics"
    )

    # Создаем экземпляр класса ChildCategory
    laptops_category = ChildCategory(
        category_id=2,
        category_name="Laptops",
        parent_category_id=1
    )

    # Выводим значения атрибутов
    print(f"Категория: {electronics_category.category_name}, ID: {electronics_category.category_id}")
    print(f"Категория: {laptops_category.category_name}, ID: {laptops_category.category_id}, Родитель: {laptops_category.parent_category_id}")