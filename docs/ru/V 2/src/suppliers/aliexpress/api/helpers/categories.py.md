# Модуль `categories.py`

## Обзор

Модуль `categories.py` содержит функции для фильтрации категорий и подкатегорий, полученных через API AliExpress. Он предоставляет инструменты для разделения категорий на родительские и дочерние, что упрощает их дальнейшую обработку.

## Оглавление

- [Функции](#функции)
    - [`filter_parent_categories`](#filter_parent_categories)
    - [`filter_child_categories`](#filter_child_categories)

## Функции

### `filter_parent_categories`

**Описание**:
Фильтрует и возвращает список категорий, у которых нет родительской категории.

**Параметры**:
- `categories` (List[models.Category | models.ChildCategory]): Список объектов категорий или подкатегорий.

**Возвращает**:
- `List[models.Category]`: Список объектов категорий, не имеющих родительской категории.

**Пример использования:**

```python
categories = [
    models.Category(id=1, name="Category 1"),
    models.ChildCategory(id=2, name="Child 1", parent_category_id=1),
    models.Category(id=3, name="Category 2")
]
parent_categories = filter_parent_categories(categories)
print(parent_categories)
# Вывод: [models.Category(id=1, name="Category 1"), models.Category(id=3, name="Category 2")]
```

### `filter_child_categories`

**Описание**:
Фильтрует и возвращает список дочерних категорий, принадлежащих указанной родительской категории.

**Параметры**:
- `categories` (List[models.Category | models.ChildCategory]): Список объектов категорий или подкатегорий.
- `parent_category_id` (int): Идентификатор родительской категории для фильтрации дочерних категорий.

**Возвращает**:
- `List[models.ChildCategory]`: Список объектов дочерних категорий, соответствующих указанному идентификатору родительской категории.

**Пример использования:**

```python
categories = [
    models.Category(id=1, name="Category 1"),
    models.ChildCategory(id=2, name="Child 1", parent_category_id=1),
    models.ChildCategory(id=3, name="Child 2", parent_category_id=1),
    models.ChildCategory(id=4, name="Child 3", parent_category_id=2)
]
child_categories = filter_child_categories(categories, 1)
print(child_categories)
# Вывод: [models.ChildCategory(id=2, name="Child 1", parent_category_id=1), models.ChildCategory(id=3, name="Child 2", parent_category_id=1)]
```