# Модуль `hypotez/src/suppliers/aliexpress/api/models/category.py`

## Обзор

Модуль содержит определения классов `Category` и `ChildCategory`, представляющих категории товаров на AliExpress.  Класс `ChildCategory` наследуется от `Category` и добавляет атрибут `parent_category_id`, который указывает на родительскую категорию.

## Классы

### `Category`

**Описание**: Базовый класс для представления категории. Содержит идентификатор категории (`category_id`) и название категории (`category_name`).

**Атрибуты**:

- `category_id` (int): Идентификатор категории.
- `category_name` (str): Название категории.


### `ChildCategory`

**Описание**: Класс, представляющий дочернюю категорию. Наследуется от `Category` и добавляет атрибут `parent_category_id`.

**Атрибуты**:

- `category_id` (int): Идентификатор категории (наследуется от `Category`).
- `category_name` (str): Название категории (наследуется от `Category`).
- `parent_category_id` (int): Идентификатор родительской категории.