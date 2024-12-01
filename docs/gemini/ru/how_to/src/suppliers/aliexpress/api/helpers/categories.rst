Как использовать этот блок кода
=========================================================================================

Описание
-------------------------
Этот код содержит две функции для работы с категориями и подкатегориями API AliExpress. Функция `filter_parent_categories` возвращает список категорий, у которых нет родительской категории. Функция `filter_child_categories` возвращает список подкатегорий, относящихся к указанной родительской категории. Код также обрабатывает случай, когда на вход подаётся не список, а отдельное значение.

Шаги выполнения
-------------------------
1. **Импорт необходимых модулей:** Модули `List`, `Union` и `models` импортируются из соответствующего пространства имён.

2. **Определение функции `filter_parent_categories`:**
    * Функция принимает список объектов `Category` или `ChildCategory` в качестве аргумента `categories`.
    * Инициализирует пустой список `filtered_categories`.
    * Обрабатывает случай, когда вход `categories` - не список, преобразуя его в список из одного элемента.
    * Проходит по каждому элементу `category` в списке `categories`.
    * Проверяет, есть ли у объекта `category` атрибут `parent_category_id`. Если его нет, добавляет `category` в список `filtered_categories`.
    * Возвращает список `filtered_categories`.

3. **Определение функции `filter_child_categories`:**
    * Функция принимает список объектов `Category` или `ChildCategory` в качестве аргумента `categories` и идентификатор родительской категории `parent_category_id`.
    * Инициализирует пустой список `filtered_categories`.
    * Обрабатывает случай, когда вход `categories` - не список, преобразуя его в список из одного элемента.
    * Проходит по каждому элементу `category` в списке `categories`.
    * Проверяет, есть ли у объекта `category` атрибут `parent_category_id` и соответствует ли он значению `parent_category_id`. Если да, добавляет `category` в список `filtered_categories`.
    * Возвращает список `filtered_categories`.

Пример использования
-------------------------
.. code-block:: python

    from hypotez.src.suppliers.aliexpress.api.helpers import categories
    from hypotez.src.suppliers.aliexpress.api import models

    # Пример данных
    parent_category = models.Category(id=1, name='Электроника')
    child_category1 = models.ChildCategory(id=2, name='Телефоны', parent_category_id=1)
    child_category2 = models.ChildCategory(id=3, name='Ноутбуки', parent_category_id=1)
    child_category3 = models.ChildCategory(id=4, name='Наушники', parent_category_id=5)  # Отсутствует в списке родительских категорий

    categories_list = [parent_category, child_category1, child_category2, child_category3]

    # Получение категорий без родителей
    parent_categories = categories.filter_parent_categories(categories_list)
    print(parent_categories)  # Выведет [<__main__.Category object at ...>,]

    # Получение подкатегорий с родительской категорией ID 1
    child_categories_filtered = categories.filter_child_categories(categories_list, 1)
    print(child_categories_filtered)  # Выведет [<__main__.ChildCategory object at ...>, <__main__.ChildCategory object at ...>]

    # Пример с не-списком как аргументом
    single_category = child_category1
    filtered_categories = categories.filter_child_categories(single_category, 1)
    print(filtered_categories)