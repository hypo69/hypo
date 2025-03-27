# Модуль `categories`

## Обзор

Модуль `categories` содержит функции для фильтрации категорий и подкатегорий, полученных из API Aliexpress. Он предназначен для обработки списков категорий и подкатегорий, разделяя их на основе наличия или отсутствия родительской категории, а также фильтруя подкатегории по идентификатору родительской категории.

## Подробней

Этот модуль предоставляет две основные функции: `filter_parent_categories` и `filter_child_categories`. Первая функция используется для извлечения категорий верхнего уровня, которые не имеют родительской категории. Вторая функция позволяет получить подкатегории, принадлежащие определенной родительской категории. Эти функции полезны для организации и структурирования данных, полученных из API Aliexpress, чтобы упростить дальнейшую обработку и отображение категорий товаров.

## Функции

### `filter_parent_categories`

```python
def filter_parent_categories(categories: List[models.Category | models.ChildCategory]) -> List[models.Category]:
    """
    Args:
        categories (List[models.Category | models.ChildCategory]): List of category or child category objects.

    Returns:
        List[models.Category]: List of category objects without a parent category.
    """
```

**Описание**: Фильтрует список категорий и возвращает список категорий, у которых нет родительской категории.

**Параметры**:
- `categories` (List[models.Category | models.ChildCategory]): Список объектов категорий или подкатегорий.

**Возвращает**:
- `List[models.Category]`: Список объектов категорий без родительской категории.

**Примеры**:
```python
from typing import List
from .. import models  # Предполагается, что models находится в родительском пакете

# Пример использования с фиктивными данными для models.Category
class MockCategory:
    def __init__(self, category_id: int, name: str, parent_category_id: int = None):
        self.category_id = category_id
        self.name = name
        self.parent_category_id = parent_category_id

# Создаем экземпляры MockCategory
category1 = MockCategory(category_id=1, name="Электроника")
category2 = MockCategory(category_id=2, name="Одежда", parent_category_id=10)
category3 = MockCategory(category_id=3, name="Телефоны")

categories_list = [category1, category2, category3]

# Фильтруем категории без родительской категории
filtered_categories = filter_parent_categories(categories_list)

# Выводим результаты
for category in filtered_categories:
    print(f"Category ID: {category.category_id}, Name: {category.name}")
```

### `filter_child_categories`

```python
def filter_child_categories(categories: List[models.Category | models.ChildCategory],
                            parent_category_id: int) -> List[models.ChildCategory]:
    """
    Args:
        categories (List[models.Category | models.ChildCategory]): List of category or child category objects.
        parent_category_id (int): The ID of the parent category to filter child categories by.

    Returns:
        List[models.ChildCategory]: List of child category objects with the specified parent category ID.
    """
```

**Описание**: Фильтрует список категорий и возвращает список подкатегорий, принадлежащих указанной родительской категории.

**Параметры**:
- `categories` (List[models.Category | models.ChildCategory]): Список объектов категорий или подкатегорий.
- `parent_category_id` (int): ID родительской категории, по которой нужно отфильтровать подкатегории.

**Возвращает**:
- `List[models.ChildCategory]`: Список объектов подкатегорий с указанным ID родительской категории.

**Примеры**:
```python
from typing import List
from .. import models  # Предполагается, что models находится в родительском пакете

# Пример использования с фиктивными данными для models.Category и models.ChildCategory
class MockCategory:
    def __init__(self, category_id: int, name: str, parent_category_id: int = None):
        self.category_id = category_id
        self.name = name
        self.parent_category_id = parent_category_id

class MockChildCategory(MockCategory):
    pass

# Создаем экземпляры MockCategory и MockChildCategory
category1 = MockCategory(category_id=10, name="Электроника")
category2 = MockChildCategory(category_id=21, name="Телефоны", parent_category_id=10)
category3 = MockChildCategory(category_id=22, name="Аксессуары", parent_category_id=10)
category4 = MockChildCategory(category_id=23, name="Ноутбуки", parent_category_id=11)  # Другая родительская категория

categories_list = [category1, category2, category3, category4]

# Фильтруем подкатегории для родительской категории с ID 10
parent_category_id = 10
filtered_categories = filter_child_categories(categories_list, parent_category_id)

# Выводим результаты
for category in filtered_categories:
    print(f"Category ID: {category.category_id}, Name: {category.name}, Parent Category ID: {category.parent_category_id}")