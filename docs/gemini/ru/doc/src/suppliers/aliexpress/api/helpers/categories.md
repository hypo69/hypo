# Модуль `hypotez/src/suppliers/aliexpress/api/helpers/categories.py`

## Обзор

Модуль `categories.py` содержит функции для фильтрации категорий и подкатегорий API AliExpress. Он предоставляет инструменты для работы с объектами категорий, позволяя отбирать категории без родительских категорий и подкатегории по заданному идентификатору родительской категории.

## Функции

### `filter_parent_categories`

**Описание**: Фильтрует список категорий и подкатегорий, возвращая только те, у которых нет родительской категории.

**Параметры**:

- `categories` (List[models.Category | models.ChildCategory]): Список объектов категорий или подкатегорий.


**Возвращает**:

- List[models.Category]: Список объектов категорий, не имеющих родительскую категорию.

**Обработка исключений**:

Нет.


### `filter_child_categories`

**Описание**: Фильтрует список категорий и подкатегорий, возвращая только подкатегории, относящиеся к заданной родительской категории.

**Параметры**:

- `categories` (List[models.Category | models.ChildCategory]): Список объектов категорий или подкатегорий.
- `parent_category_id` (int): Идентификатор родительской категории.


**Возвращает**:

- List[models.ChildCategory]: Список объектов подкатегорий, относящихся к указанной родительской категории.

**Обработка исключений**:

Нет.

**Примечания**:

Функции обрабатывают различные типы входных данных, включая некорректные типы.  Если на вход подаётся значение, отличное от списка, оно конвертируется в список.