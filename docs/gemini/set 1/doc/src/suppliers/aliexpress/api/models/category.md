# Модуль `hypotez/src/suppliers/aliexpress/api/models/category.py`

## Обзор

Модуль `category.py` содержит определения классов `Category` и `ChildCategory`, используемых для представления категорий товаров на AliExpress. Класс `Category` описывает базовые характеристики категории, а `ChildCategory` расширяет его, добавляя информацию о родительской категории.

## Оглавление

- [Модуль `category.py`](#модуль-categorypy)
- [Класс `Category`](#класс-category)
- [Класс `ChildCategory`](#класс-childcategory)


## Классы

### `Category`

**Описание**: Базовый класс для представления категорий. Хранит идентификатор категории (`category_id`) и ее название (`category_name`).

**Атрибуты**:

- `category_id` (int): Идентификатор категории.
- `category_name` (str): Название категории.


### `ChildCategory`

**Описание**: Класс, расширяющий `Category`, добавляя информацию о родительской категории.

**Атрибуты**:

- `parent_category_id` (int): Идентификатор родительской категории.
- `category_id` (int): Идентификатор категории.
- `category_name` (str): Название категории. (наследуется от `Category`)