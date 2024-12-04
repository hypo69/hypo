Как использовать класс Category и ChildCategory
========================================================================================

Описание
-------------------------
Этот код определяет два класса: `Category` и `ChildCategory`.  Класс `Category` представляет собой базовую категорию, а `ChildCategory` наследуется от него и добавляет дополнительное поле `parent_category_id`. Оба класса предназначены для хранения информации о категориях, вероятно, товаров на AliExpress.  Поля `category_id` и `category_name` являются обязательными для всех категорий.


Шаги выполнения
-------------------------
1. **Импортирование классов:** Для использования классов, необходимо импортировать их в свой скрипт.  Пример:
   ```python
   from hypotez.src.suppliers.aliexpress.api.models.category import Category, ChildCategory
   ```

2. **Создание экземпляров классов:**  Можно создать экземпляры как класса `Category`, так и `ChildCategory`.
   ```python
   # Создаем экземпляр класса Category
   my_category = Category(category_id=123, category_name="Электроника")

   # Создаем экземпляр класса ChildCategory
   child_category = ChildCategory(category_id=456, category_name="Телефоны", parent_category_id=123)
   ```

3. **Обращение к атрибутам:** Для получения значений свойств (полей) используйте точку доступа к атрибутам.
   ```python
   print(my_category.category_id)  # Выведет 123
   print(child_category.parent_category_id) # Выведет 123
   ```

4. **Работа с данными:**  Классы предназначены для хранения данных. В дальнейшем эти данные можно использовать в других частях приложения для работы с категориями.


Пример использования
-------------------------
.. code-block:: python

    from hypotez.src.suppliers.aliexpress.api.models.category import Category, ChildCategory

    # Пример создания и работы с категориями
    main_category = Category(category_id=1, category_name="Одежда")
    sub_category = ChildCategory(category_id=2, category_name="Мужская одежда", parent_category_id=1)

    print(f"Основная категория: {main_category.category_name}, ID: {main_category.category_id}")
    print(f"Подкатегория: {sub_category.category_name}, ID: {sub_category.category_id}, Родительская категория: {sub_category.parent_category_id}")