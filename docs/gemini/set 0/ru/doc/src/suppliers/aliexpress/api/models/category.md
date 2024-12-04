# Модуль `hypotez/src/suppliers/aliexpress/api/models/category.py`

## Обзор

Модуль `category.py` содержит определения классов `Category` и `ChildCategory`, представляющих категории товаров на AliExpress. Класс `Category` описывает базовую категорию, а `ChildCategory` — дочернюю категорию, которая наследуется от `Category` и дополнительно содержит `parent_category_id`.

## Оглавление

* [Классы](#классы)
    * [Category](#category)
    * [ChildCategory](#childcategory)


## Классы

### `Category`

**Описание**: Базовый класс для представления категории товаров. Содержит идентификатор категории (`category_id`) и её название (`category_name`).

**Атрибуты**:

- `category_id` (int): Идентификатор категории.
- `category_name` (str): Название категории.


### `ChildCategory`

**Описание**: Класс, представляющий дочернюю категорию товаров. Наследуется от `Category` и добавляет атрибут `parent_category_id`.

**Атрибуты**:

- `category_id` (int): Идентификатор дочерней категории.
- `category_name` (str): Название дочерней категории.
- `parent_category_id` (int): Идентификатор родительской категории.