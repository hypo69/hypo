# Модуль `categories.py`

## Обзор

Модуль `categories.py` содержит функции для фильтрации категорий и подкатегорий, полученных из API Aliexpress. Он предоставляет инструменты для разделения категорий на родительские и дочерние, облегчая работу с иерархической структурой категорий товаров.

## Подробней

Модуль предназначен для обработки данных, полученных из API Aliexpress, и содержит функции для фильтрации категорий на основе наличия `parent_category_id`. Это позволяет отделить категории верхнего уровня (родительские) от подкатегорий (дочерних), принадлежащих к определенным родительским категориям.

## Функции

### `filter_parent_categories`

```python
def filter_parent_categories(categories: List[models.Category | models.ChildCategory]) -> List[models.Category]:
    """
    Фильтрует и возвращает список категорий, у которых нет родительской категории.

    Args:
        categories (List[models.Category | models.ChildCategory]): Список объектов категорий или дочерних категорий.

    Returns:
        List[models.Category]: Список объектов категорий без родительской категории.
    """
```

**Назначение**: Функция `filter_parent_categories` принимает список категорий (или дочерних категорий) и возвращает список категорий, которые не имеют родительской категории (`parent_category_id`).

**Параметры**:
- `categories` (List[models.Category | models.ChildCategory]): Список объектов, представляющих категории или дочерние категории.

**Возвращает**:
- `List[models.Category]`: Список категорий, у которых отсутствует `parent_category_id`.

**Как работает функция**:

1. Инициализируется пустой список `filtered_categories`.
2. Проверяется, является ли входной параметр `categories` строкой, числом или числом с плавающей запятой. Если да, он преобразуется в список, чтобы обеспечить итерацию.
3. Перебирается каждый элемент `category` в списке `categories`.
4. Для каждого элемента проверяется, отсутствует ли атрибут `parent_category_id`.
5. Если атрибут `parent_category_id` отсутствует, элемент добавляется в список `filtered_categories`.
6. Возвращается список `filtered_categories`.

```
Начало
   │
   │ categories: List[Category | ChildCategory]
   │
   │ Проверка типа categories (str, int, float) -> Преобразование в list [categories]
   │
   │ Инициализация filtered_categories = []
   │
   │ for category in categories:
   │   │
   │   └── Проверка наличия атрибута 'parent_category_id'
   │       │
   │       └── Если атрибут отсутствует:
   │           │   Добавление category в filtered_categories
   │           │
   │       └── Конец проверки
   │
   │ Конец цикла for
   │
   │ Возврат filtered_categories
   │
Конец
```

**Примеры**:

```python
from src.suppliers.aliexpress.api import models
# Пример использования
category1 = models.Category(id=1, name='Category 1')
category2 = models.ChildCategory(id=2, name='Category 2', parent_category_id=1)

categories = [category1, category2]
parent_categories = filter_parent_categories(categories)
print(parent_categories)  # Вывод: [<src.suppliers.aliexpress.api.models.Category object at 0x...>]
```

### `filter_child_categories`

```python
def filter_child_categories(categories: List[models.Category | models.ChildCategory],
                            parent_category_id: int) -> List[models.ChildCategory]:
    """
    Фильтрует и возвращает список дочерних категорий, принадлежащих к указанной родительской категории.

    Args:
        categories (List[models.Category | models.ChildCategory]): Список объектов категорий или дочерних категорий.
        parent_category_id (int): ID родительской категории для фильтрации дочерних категорий.

    Returns:
        List[models.ChildCategory]: Список объектов дочерних категорий с указанным ID родительской категории.
    """
```

**Назначение**: Функция `filter_child_categories` принимает список категорий (или дочерних категорий) и `parent_category_id` и возвращает список дочерних категорий, принадлежащих к указанной родительской категории.

**Параметры**:
- `categories` (List[models.Category | models.ChildCategory]): Список объектов, представляющих категории или дочерние категории.
- `parent_category_id` (int): ID родительской категории, по которому выполняется фильтрация дочерних категорий.

**Возвращает**:
- `List[models.ChildCategory]`: Список дочерних категорий, у которых `parent_category_id` соответствует указанному значению.

**Как работает функция**:

1. Инициализируется пустой список `filtered_categories`.
2. Проверяется, является ли входной параметр `categories` строкой, числом или числом с плавающей запятой. Если да, он преобразуется в список, чтобы обеспечить итерацию.
3. Перебирается каждый элемент `category` в списке `categories`.
4. Для каждого элемента проверяется наличие атрибута `parent_category_id` и соответствие значения этого атрибута значению `parent_category_id`, переданному в функцию.
5. Если оба условия выполняются, элемент добавляется в список `filtered_categories`.
6. Возвращается список `filtered_categories`.

```
Начало
   │
   │ categories: List[Category | ChildCategory], parent_category_id: int
   │
   │ Проверка типа categories (str, int, float) -> Преобразование в list [categories]
   │
   │ Инициализация filtered_categories = []
   │
   │ for category in categories:
   │   │
   │   └── Проверка наличия атрибута 'parent_category_id' и соответствия category.parent_category_id == parent_category_id
   │       │
   │       └── Если оба условия истинны:
   │           │   Добавление category в filtered_categories
   │           │
   │       └── Конец проверки
   │
   │ Конец цикла for
   │
   │ Возврат filtered_categories
   │
Конец
```

**Примеры**:

```python
from src.suppliers.aliexpress.api import models

# Пример использования
category1 = models.Category(id=1, name='Category 1')
category2 = models.ChildCategory(id=2, name='Category 2', parent_category_id=1)

categories = [category1, category2]
child_categories = filter_child_categories(categories, parent_category_id=1)
print(child_categories)  # Вывод: [<src.suppliers.aliexpress.api.models.ChildCategory object at 0x...>]