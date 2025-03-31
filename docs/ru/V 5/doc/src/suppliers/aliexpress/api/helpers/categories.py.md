# Модуль `categories.py`

## Обзор

Модуль содержит функции для фильтрации категорий и подкатегорий, полученных через API Aliexpress. Он предоставляет инструменты для разделения категорий на родительские и дочерние, основываясь на наличии идентификатора родительской категории.

## Подробней

Этот модуль предназначен для обработки данных, полученных из API Aliexpress, и фильтрации категорий товаров. Он используется для разделения категорий на верхний уровень (родительские категории) и подкатегории (дочерние категории), что необходимо для организации иерархической структуры каталога товаров.

## Функции

### `filter_parent_categories`

```python
def filter_parent_categories(categories: List[models.Category | models.ChildCategory]) -> List[models.Category]:
    """
    Filters and returns a list of categories that do not have a parent category.

    @param categories: List of category or child category objects.
    @return: List of category objects without a parent category.
    """
```

**Как работает функция**:
Функция `filter_parent_categories` принимает список категорий (объектов `Category` или `ChildCategory`) и возвращает новый список, содержащий только те категории, у которых отсутствует идентификатор родительской категории (`parent_category_id`). Это позволяет выделить категории верхнего уровня, не являющиеся подкатегориями.

1.  Создается пустой список `filtered_categories` для хранения отфильтрованных категорий.
2.  Проверяется, является ли входной параметр `categories` экземпляром одного из типов `str`, `int` или `float`. Если это так, то он преобразуется в список, содержащий только этот элемент. Это необходимо для обработки случая, когда в функцию передается единичное значение вместо списка категорий.
3.  Проходится по каждой категории в списке `categories`.
4.  Для каждой категории проверяется, отсутствует ли атрибут `parent_category_id` с помощью `hasattr`. Если атрибут отсутствует, это означает, что категория является родительской.
5.  Если категория является родительской, она добавляется в список `filtered_categories`.
6.  После обработки всех категорий функция возвращает список `filtered_categories`, содержащий только родительские категории.

**Параметры**:

*   `categories` (List[models.Category | models.ChildCategory]): Список категорий или дочерних категорий для фильтрации.

**Возвращает**:

*   `List[models.Category]`: Список категорий, у которых нет родительской категории.

**Примеры**:

```python
from src.suppliers.aliexpress.api import models
# Пример использования функции filter_parent_categories
parent_categories = filter_parent_categories([
    models.Category(id=1, name='Category 1'),
    models.ChildCategory(id=2, name='Child Category 1', parent_category_id=1),
    models.Category(id=3, name='Category 2')
])
# В результате parent_categories будет содержать список из Category 1 и Category 2
```

### `filter_child_categories`

```python
def filter_child_categories(categories: List[models.Category | models.ChildCategory],
                            parent_category_id: int) -> List[models.ChildCategory]:
    """
    Filters and returns a list of child categories that belong to the specified parent category.

    @param categories: List of category or child category objects.
    @param parent_category_id: The ID of the parent category to filter child categories by.
    @return: List of child category objects with the specified parent category ID.
    """
```

**Как работает функция**:
Функция `filter_child_categories` принимает список категорий и идентификатор родительской категории (`parent_category_id`). Она возвращает список дочерних категорий, принадлежащих указанной родительской категории.

1.  Создается пустой список `filtered_categories` для хранения отфильтрованных дочерних категорий.
2.  Проверяется, является ли входной параметр `categories` экземпляром одного из типов `str`, `int` или `float`. Если это так, то он преобразуется в список, содержащий только этот элемент. Это необходимо для обработки случая, когда в функцию передается единичное значение вместо списка категорий.
3.  Проходится по каждой категории в списке `categories`.
4.  Для каждой категории проверяется наличие атрибута `parent_category_id` и соответствие его значения заданному `parent_category_id`.
5.  Если категория является дочерней и принадлежит указанной родительской категории, она добавляется в список `filtered_categories`.
6.  После обработки всех категорий функция возвращает список `filtered_categories`, содержащий только дочерние категории, принадлежащие указанной родительской категории.

**Параметры**:

*   `categories` (List[models.Category | models.ChildCategory]): Список категорий или дочерних категорий для фильтрации.
*   `parent_category_id` (int): Идентификатор родительской категории, по которому необходимо отфильтровать дочерние категории.

**Возвращает**:

*   `List[models.ChildCategory]`: Список дочерних категорий с указанным идентификатором родительской категории.

**Примеры**:

```python
from src.suppliers.aliexpress.api import models
# Пример использования функции filter_child_categories
child_categories = filter_child_categories([
    models.Category(id=1, name='Category 1'),
    models.ChildCategory(id=2, name='Child Category 1', parent_category_id=1),
    models.ChildCategory(id=3, name='Child Category 2', parent_category_id=2)
], parent_category_id=1)
# В результате child_categories будет содержать список только из Child Category 1