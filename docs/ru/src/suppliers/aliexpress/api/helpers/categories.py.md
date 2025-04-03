# Модуль `categories.py`

## Обзор

Модуль `categories.py` содержит функции для фильтрации категорий и подкатегорий, полученных из API Aliexpress. Он предоставляет инструменты для разделения категорий на родительские (не имеющие родительской категории) и дочерние (принадлежащие определенной родительской категории).

## Подробней

Этот модуль используется для обработки данных категорий, полученных из API Aliexpress. Он помогает организовать категории в древовидную структуру, что упрощает навигацию и фильтрацию товаров. Функции модуля позволяют выделить основные категории и их подкатегории, что важно для структурирования данных о товарах.

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

**Назначение**: Фильтрует и возвращает список категорий, у которых нет родительской категории.

**Параметры**:
- `categories` (List[models.Category | models.ChildCategory]): Список объектов категорий или дочерних категорий.

**Возвращает**:
- `List[models.Category]`: Список объектов категорий без родительской категории.

**Как работает функция**:

1.  **Инициализация**: Создается пустой список `filtered_categories` для хранения отфильтрованных категорий.
2.  **Обработка входных данных**: Если входной параметр `categories` является строкой, целым числом или числом с плавающей точкой, он преобразуется в список, чтобы обеспечить корректную обработку.
3.  **Фильтрация категорий**: Перебирает все элементы в списке `categories`. Для каждого элемента проверяется, есть ли у него атрибут `parent_category_id`. Если атрибута нет, категория считается родительской и добавляется в список `filtered_categories`.
4.  **Возврат результата**: Функция возвращает список `filtered_categories`, содержащий только родительские категории.

**ASCII flowchart**:

```
A: Инициализация filtered_categories = []
|
B: Проверка типа categories: categories - строка, число, float?
|
C: Если да, преобразование categories в список: categories = [categories]
|
D: Перебор category в categories
|
E: Проверка наличия атрибута parent_category_id у category
|
F: Если атрибута нет, добавление category в filtered_categories
|
G: Возврат filtered_categories
```

**Примеры**:

```python
from src.suppliers.aliexpress.api import models

# Пример 1: Список категорий и дочерних категорий
categories = [
    models.Category(id=1, name='Electronics'),
    models.ChildCategory(id=2, name='Smartphones', parent_category_id=1),
    models.Category(id=3, name='Fashion')
]
parent_categories = filter_parent_categories(categories)
# parent_categories будет содержать [Category(id=1, name='Electronics'), Category(id=3, name='Fashion')]

# Пример 2: Список только дочерних категорий
child_categories = [
    models.ChildCategory(id=2, name='Smartphones', parent_category_id=1),
    models.ChildCategory(id=4, name='T-Shirts', parent_category_id=3)
]
parent_categories = filter_parent_categories(child_categories)
# parent_categories будет содержать []

# Пример 3: Передана строка вместо списка
category_name = "Home Appliances"
parent_categories = filter_parent_categories(category_name)
# parent_categories будет содержать []
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

**Назначение**: Фильтрует и возвращает список дочерних категорий, принадлежащих указанной родительской категории.

**Параметры**:
- `categories` (List[models.Category | models.ChildCategory]): Список объектов категорий или дочерних категорий.
- `parent_category_id` (int): ID родительской категории, по которой нужно фильтровать дочерние категории.

**Возвращает**:
- `List[models.ChildCategory]`: Список объектов дочерних категорий с указанным ID родительской категории.

**Как работает функция**:

1.  **Инициализация**: Создается пустой список `filtered_categories` для хранения отфильтрованных дочерних категорий.
2.  **Обработка входных данных**: Если входной параметр `categories` является строкой, целым числом или числом с плавающей точкой, он преобразуется в список для обеспечения корректной обработки.
3.  **Фильтрация категорий**: Перебирает все элементы в списке `categories`. Для каждого элемента проверяется наличие атрибута `parent_category_id` и соответствие значения этого атрибута значению `parent_category_id`, переданному в функцию. Если оба условия выполняются, категория добавляется в список `filtered_categories`.
4.  **Возврат результата**: Функция возвращает список `filtered_categories`, содержащий только дочерние категории, принадлежащие указанной родительской категории.

**ASCII flowchart**:

```
A: Инициализация filtered_categories = []
|
B: Проверка типа categories: categories - строка, число, float?
|
C: Если да, преобразование categories в список: categories = [categories]
|
D: Перебор category в categories
|
E: Проверка наличия атрибута parent_category_id у category И category.parent_category_id == parent_category_id
|
F: Если условия выполнены, добавление category в filtered_categories
|
G: Возврат filtered_categories
```

**Примеры**:

```python
from src.suppliers.aliexpress.api import models

# Пример 1: Список категорий и дочерних категорий
categories = [
    models.Category(id=1, name='Electronics'),
    models.ChildCategory(id=2, name='Smartphones', parent_category_id=1),
    models.Category(id=3, name='Fashion'),
    models.ChildCategory(id=4, name='T-Shirts', parent_category_id=3)
]
child_categories = filter_child_categories(categories, 1)
# child_categories будет содержать [ChildCategory(id=2, name='Smartphones', parent_category_id=1)]

# Пример 2: Список только родительских категорий
parent_categories = [
    models.Category(id=1, name='Electronics'),
    models.Category(id=3, name='Fashion')
]
child_categories = filter_child_categories(parent_categories, 1)
# child_categories будет содержать []

# Пример 3: Передана строка вместо списка
category_name = "Smartphones"
child_categories = filter_child_categories(category_name, 1)
# child_categories будет содержать []