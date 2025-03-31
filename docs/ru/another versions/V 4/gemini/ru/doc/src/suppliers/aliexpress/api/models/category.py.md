# Модуль `category`

## Обзор

Модуль `category` определяет структуры данных для представления категорий товаров, используемые при взаимодействии с API AliExpress. Он содержит классы `Category` и `ChildCategory`, которые описывают основные атрибуты категорий и подкатегорий соответственно.

## Подробнее

Этот модуль предоставляет удобные классы для работы с данными категорий, полученными из API AliExpress. Он позволяет унифицировать и структурировать информацию о категориях товаров, что упрощает дальнейшую обработку и использование этих данных в проекте `hypotez`.

## Классы

### `Category`

**Описание**:
Базовый класс для представления категории товара.

**Атрибуты**:
- `category_id` (int): Идентификатор категории.
- `category_name` (str): Название категории.

**Примеры**
```python
category = Category()
category.category_id = 123
category.category_name = 'Электроника'
print(f'ID категории: {category.category_id}, Название: {category.category_name}')
```

### `ChildCategory`

**Описание**:
Класс для представления подкатегории товара, наследуется от класса `Category`.

**Атрибуты**:
- `parent_category_id` (int): Идентификатор родительской категории.

**Примеры**
```python
child_category = ChildCategory()
child_category.category_id = 456
child_category.category_name = 'Смартфоны'
child_category.parent_category_id = 123
print(f'ID подкатегории: {child_category.category_id}, Название: {child_category.category_name}, ID родительской категории: {child_category.parent_category_id}')