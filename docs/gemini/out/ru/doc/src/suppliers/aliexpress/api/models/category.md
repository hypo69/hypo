# Модуль `hypotez/src/suppliers/aliexpress/api/models/category.py`

## Обзор

Данный модуль определяет классы `Category` и `ChildCategory`, предназначенные для представления категорий товаров на AliExpress.  `ChildCategory` наследуется от `Category` и добавляет поле `parent_category_id`.

## Классы

### `Category`

**Описание**: Представляет категорию товара на AliExpress.

**Атрибуты**:
- `category_id` (int): Идентификатор категории.
- `category_name` (str): Название категории.


### `ChildCategory`

**Описание**:  Представляет дочернюю категорию товара на AliExpress, наследующуюся от родительской категории.

**Атрибуты**:
- `category_id` (int): Идентификатор дочерней категории (наследуется от родительского класса).
- `category_name` (str): Название дочерней категории (наследуется от родительского класса).
- `parent_category_id` (int): Идентификатор родительской категории.