# Модуль `category`

## Обзор

Модуль определяет модели данных для категорий товаров, используемых в API AliExpress. Он содержит классы `Category` и `ChildCategory`, представляющие базовую категорию и дочернюю категорию соответственно.

## Подробней

Этот модуль предоставляет структуру для хранения информации о категориях товаров, получаемых из API AliExpress. Класс `Category` содержит идентификатор и наименование категории, а класс `ChildCategory` наследует эти атрибуты и добавляет идентификатор родительской категории. Эти классы используются для организации и представления данных о категориях товаров в приложении.

## Классы

### `Category`

**Описание**:
Базовый класс для представления категории товара.

**Параметры**:
- `category_id` (int): Идентификатор категории.
- `category_name` (str): Наименование категории.

**Примеры**
```python
category = Category()
category.category_id = 123
category.category_name = "Электроника"
```

### `ChildCategory`

**Описание**:
Класс для представления дочерней категории товара, наследующий атрибуты от класса `Category` и добавляющий идентификатор родительской категории.

**Параметры**:
- `category_id` (int): Идентификатор категории.
- `category_name` (str): Наименование категории.
- `parent_category_id` (int): Идентификатор родительской категории.

**Примеры**
```python
child_category = ChildCategory()
child_category.category_id = 456
child_category.category_name = "Смартфоны"
child_category.parent_category_id = 123