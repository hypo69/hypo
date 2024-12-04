Как использовать функции для фильтрации категорий Aliexpress
=========================================================================================

Описание
-------------------------
Данный код содержит две функции для фильтрации категорий и подкатегорий API AliExpress.
Функция `filter_parent_categories` возвращает список родительских категорий, не имеющих родительской категории.
Функция `filter_child_categories` возвращает список подкатегорий, относящихся к заданной родительской категории.
Обе функции обрабатывают различные типы входных данных, включая списки категорий и отдельные значения (целые числа, строки, числа с плавающей точкой), преобразовывая их в списки для корректной обработки.

Шаги выполнения
-------------------------
1. **Импорт необходимых модулей:** Код импортирует необходимые типы данных `List`, `Union` и модели `Category` и `ChildCategory` из модуля `models`.
2. **Определение функции `filter_parent_categories`:** Функция принимает на вход список категорий (`categories`).
3. **Проверка типа входных данных:** Функция проверяет, является ли входной параметр `categories` списком. Если нет (строка, число), преобразует его в список.
4. **Фильтрация родительских категорий:** Функция итерируется по элементам списка `categories`. Для каждого элемента проверяет, содержит ли он атрибут `parent_category_id`. Если атрибут отсутствует, то элемент добавляется в `filtered_categories`.
5. **Возврат результата:** Функция возвращает список `filtered_categories` содержащий родительские категории без родителя.
6. **Определение функции `filter_child_categories`:** Функция принимает на вход список категорий (`categories`) и идентификатор родительской категории (`parent_category_id`).
7. **Проверка типа входных данных:** Функция проверяет, является ли входной параметр `categories` списком. Если нет (строка, число), преобразует его в список.
8. **Фильтрация дочерних категорий:** Функция итерируется по элементам списка `categories`. Для каждого элемента проверяет, содержит ли он атрибут `parent_category_id` и равен ли он переданному `parent_category_id`. Если оба условия истинны, элемент добавляется в `filtered_categories`.
9. **Возврат результата:** Функция возвращает список `filtered_categories` содержащий дочерние категории с заданным `parent_category_id`.

Пример использования
-------------------------
.. code-block:: python

    from hypotez.src.suppliers.aliexpress.api.helpers import categories
    from hypotez.src.suppliers.aliexpress.api import models

    # Пример данных (предполагается, что модели определены)
    parent_category = models.Category(id=1, name='Электроника')
    child_category1 = models.ChildCategory(id=2, name='Телефоны', parent_category_id=1)
    child_category2 = models.ChildCategory(id=3, name='Наушники', parent_category_id=1)
    child_category3 = models.ChildCategory(id=4, name='Ноутбуки', parent_category_id=5)  # Другая категория

    categories_list = [parent_category, child_category1, child_category2, child_category3]


    parent_categories = categories.filter_parent_categories(categories_list)
    print(f"Родительские категории: {parent_categories}")

    child_categories = categories.filter_child_categories(categories_list, parent_category_id=1)
    print(f"Подкатегории для категории {parent_category.name}: {child_categories}")

    # Пример с неверным типом данных
    result = categories.filter_parent_categories(123)
    print(result)