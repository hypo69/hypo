# Модуль `categories.py`

## Обзор

Модуль `categories.py` содержит функции для фильтрации категорий и подкатегорий, полученных из API Aliexpress. Он предоставляет инструменты для выделения родительских и дочерних категорий на основе их структуры.

## Оглавление

- [Обзор](#обзор)
- [Функции](#функции)
    - [`filter_parent_categories`](#filter_parent_categories)
    - [`filter_child_categories`](#filter_child_categories)

## Функции

### `filter_parent_categories`

**Описание**: Фильтрует и возвращает список категорий, у которых нет родительской категории.

**Параметры**:
- `categories` (List[models.Category | models.ChildCategory]): Список объектов категорий или дочерних категорий.

**Возвращает**:
- `List[models.Category]`: Список объектов категорий без родительской категории.

### `filter_child_categories`

**Описание**: Фильтрует и возвращает список дочерних категорий, принадлежащих указанной родительской категории.

**Параметры**:
- `categories` (List[models.Category | models.ChildCategory]): Список объектов категорий или дочерних категорий.
- `parent_category_id` (int): ID родительской категории, по которой нужно отфильтровать дочерние категории.

**Возвращает**:
- `List[models.ChildCategory]`: Список объектов дочерних категорий с указанным ID родительской категории.