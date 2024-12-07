# Модуль hypotez/src/suppliers/aliexpress/api/helpers/categories.py

## Обзор

Модуль содержит функции для фильтрации категорий и подкатегорий API Aliexpress.  Он предоставляет инструменты для выделения родительских категорий и подкатегорий, относящихся к определенному родителю.


## Функции

### `filter_parent_categories`

**Описание**: Фильтрует список категорий и подкатегорий, возвращая только те категории, у которых нет родительской категории.

**Параметры**:

- `categories` (List[models.Category | models.ChildCategory]): Список объектов категорий или подкатегорий.

**Возвращает**:

- List[models.Category]: Список объектов категорий без родительской категории.

**Обрабатывает исключения**:

- Нет.


### `filter_child_categories`

**Описание**: Фильтрует список категорий и подкатегорий, возвращая только подкатегории, относящиеся к указанному родительскому идентификатору.

**Параметры**:

- `categories` (List[models.Category | models.ChildCategory]): Список объектов категорий или подкатегорий.
- `parent_category_id` (int): Идентификатор родительской категории.

**Возвращает**:

- List[models.ChildCategory]: Список объектов подкатегорий с указанным родительским идентификатором.

**Обрабатывает исключения**:

- Нет.


## Классы

Нет.