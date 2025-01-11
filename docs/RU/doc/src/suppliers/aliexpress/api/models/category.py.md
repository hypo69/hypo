# Модуль `category.py`

## Обзор

Модуль `category.py` определяет модели данных для представления категорий товаров AliExpress. Включает базовый класс `Category` и класс `ChildCategory`, наследующий от `Category` и представляющий подкатегорию.

## Оглавление

- [Классы](#классы)
    - [`Category`](#class-category)
    - [`ChildCategory`](#class-childcategory)

## Классы

### `Category`

**Описание**: Базовый класс для представления категории товаров AliExpress.

**Атрибуты**:
- `category_id` (int): Идентификатор категории.
- `category_name` (str): Название категории.

### `ChildCategory`

**Описание**: Класс для представления подкатегории товаров AliExpress, наследуется от `Category`.

**Атрибуты**:
- `parent_category_id` (int): Идентификатор родительской категории.
- `category_id` (int): Идентификатор категории (унаследован от `Category`).
- `category_name` (str): Название категории (унаследован от `Category`).