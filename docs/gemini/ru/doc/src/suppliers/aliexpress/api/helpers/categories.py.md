# Модуль `categories`

## Обзор

Модуль `categories` содержит функции для фильтрации категорий и подкатегорий, полученных из API Aliexpress. Он предоставляет инструменты для разделения категорий на родительские и дочерние, что упрощает обработку и организацию данных о товарах.

## Подробней

Этот модуль предназначен для работы с данными, полученными из API Aliexpress, в частности с категориями товаров. Он включает функции для фильтрации категорий на основе их parent_category_id, что позволяет отделить родительские категории от дочерних. Это может быть полезно для навигации по категориям товаров, создания структуры категорий на сайте и т.д.

## Функции

### `filter_parent_categories`

```python
def filter_parent_categories(categories: List[models.Category | models.ChildCategory]) -> List[models.Category]:
    """
    Args:
        categories (List[models.Category | models.ChildCategory]): List of category or child category objects.

    Returns:
        List[models.Category]: List of category objects without a parent category.
    """
```

**Описание**: Фильтрует список категорий и возвращает только те, у которых отсутствует родительская категория.

**Параметры**:
- `categories` (List[models.Category | models.ChildCategory]): Список объектов категорий или дочерних категорий.

**Возвращает**:
- `List[models.Category]`: Список объектов категорий без родительской категории.

**Примеры**:

```python
# from src.suppliers.aliexpress.api import models 
# categories = [models.Category(id=1, name='Category1'), models.ChildCategory(id=2, name='ChildCategory1', parent_category_id=1)]
# parent_categories = filter_parent_categories(categories)
# print(parent_categories)
# Вывод: [models.Category(id=1, name='Category1')]
```

### `filter_child_categories`

```python
def filter_child_categories(categories: List[models.Category | models.ChildCategory],
                            parent_category_id: int) -> List[models.ChildCategory]:
    """
    Args:
        categories (List[models.Category | models.ChildCategory]): List of category or child category objects.
        parent_category_id (int): The ID of the parent category to filter child categories by.

    Returns:
        List[models.ChildCategory]: List of child category objects with the specified parent category ID.
    """
```

**Описание**: Фильтрует список категорий и возвращает только дочерние категории, принадлежащие указанной родительской категории.

**Параметры**:
- `categories` (List[models.Category | models.ChildCategory]): Список объектов категорий или дочерних категорий.
- `parent_category_id` (int): ID родительской категории, по которому нужно фильтровать дочерние категории.

**Возвращает**:
- `List[models.ChildCategory]`: Список объектов дочерних категорий, принадлежащих указанной родительской категории.

**Примеры**:

```python
# from src.suppliers.aliexpress.api import models
# categories = [models.Category(id=1, name='Category1'), models.ChildCategory(id=2, name='ChildCategory1', parent_category_id=1)]
# child_categories = filter_child_categories(categories, 1)
# print(child_categories)
# Вывод: [models.ChildCategory(id=2, name='ChildCategory1', parent_category_id=1)]