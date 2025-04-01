# Модуль `category`

## Обзор

Модуль `category` содержит классы для представления категорий товаров, используемые при взаимодействии с API AliExpress. Определены базовый класс `Category` и класс `ChildCategory`, представляющий дочерние категории.

## Подробней

Модуль предоставляет структуры данных для хранения информации о категориях товаров, полученных от API AliExpress. Эти классы используются для организации и обработки данных о категориях, таких как идентификаторы и названия.

## Классы

### `Category`

**Описание**: Базовый класс для представления категории товара.

**Принцип работы**:
Класс `Category` служит основой для представления информации о категории товара. Он содержит поля `category_id` и `category_name`, которые хранят идентификатор и название категории соответственно.

**Атрибуты**:
- `category_id` (int): Идентификатор категории.
- `category_name` (str): Название категории.

### `ChildCategory`

**Описание**: Класс для представления дочерней категории товара, наследуется от класса `Category`.

**Принцип работы**:
Класс `ChildCategory` расширяет класс `Category`, добавляя информацию о родительской категории. Поле `parent_category_id` хранит идентификатор родительской категории.

**Наследует**:
- `Category`: класс `ChildCategory` наследует атрибуты `category_id` и `category_name` от класса `Category`.

**Атрибуты**:
- `parent_category_id` (int): Идентификатор родительской категории.

## Примеры

Пример создания экземпляра класса `Category`:

```python
category = Category()
category.category_id = 12345
category.category_name = "Электроника"
print(f"ID категории: {category.category_id}, Название: {category.category_name}")
```

Пример создания экземпляра класса `ChildCategory`:

```python
child_category = ChildCategory()
child_category.category_id = 67890
child_category.category_name = "Смартфоны"
child_category.parent_category_id = 12345
print(f"ID дочерней категории: {child_category.category_id}, Название: {child_category.category_name}, ID родительской категории: {child_category.parent_category_id}")