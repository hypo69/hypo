# Модуль `src.suppliers.aliexpress.api.helpers.categories`

## Обзор

Модуль содержит функции для фильтрации категорий и подкатегорий, полученных из API Aliexpress. Он предоставляет инструменты для разделения категорий на родительские и дочерние, основываясь на наличии идентификатора родительской категории.

## Подробней

Этот модуль предназначен для обработки данных о категориях, полученных из API Aliexpress. Он помогает отделить основные категории от подкатегорий, что упрощает дальнейшую обработку и представление данных. Функции модуля позволяют фильтровать категории по идентификатору родительской категории, что полезно для создания иерархической структуры категорий.

## Функции

### `filter_parent_categories`

```python
def filter_parent_categories(categories: List[models.Category | models.ChildCategory]) -> List[models.Category]:
    """
    Фильтрует и возвращает список категорий, у которых нет родительской категории.

    Args:
        categories (List[models.Category | models.ChildCategory]): Список объектов категорий или дочерних категорий.

    Returns:
        List[models.Category]: Список объектов категорий без родительской категории.
    """
```

**Назначение**:
Функция `filter_parent_categories` принимает список категорий (или дочерних категорий) и возвращает новый список, содержащий только те категории, у которых отсутствует родительская категория. Это позволяет выделить основные категории верхнего уровня из общего списка.

**Параметры**:
- `categories` (List[models.Category | models.ChildCategory]): Список категорий для фильтрации. Каждый элемент списка должен быть объектом типа `models.Category` или `models.ChildCategory`.

**Возвращает**:
- `List[models.Category]`: Список категорий, у которых нет родительской категории.

**Как работает функция**:

1. **Инициализация**: Создается пустой список `filtered_categories` для хранения отфильтрованных категорий.
2. **Проверка входных данных**: Проверяется, является ли входной параметр `categories` экземпляром `str`, `int` или `float`. Если да, то он преобразуется в список, чтобы обеспечить возможность итерации.
3. **Итерация по категориям**: Функция проходит по каждой категории в списке `categories`.
4. **Проверка наличия атрибута `parent_category_id`**: Для каждой категории проверяется наличие атрибута `parent_category_id`. Если атрибут отсутствует, это означает, что категория не является дочерней и, следовательно, является родительской.
5. **Добавление в отфильтрованный список**: Если у категории нет атрибута `parent_category_id`, она добавляется в список `filtered_categories`.
6. **Возврат результата**: После завершения итерации функция возвращает список `filtered_categories`, содержащий только родительские категории.

**Примеры**:

```python
from typing import List
from .. import models

# Пример использования с фиктивными данными
class MockCategory:
    def __init__(self, category_id: int, parent_category_id: int = None):
        self.category_id = category_id
        self.parent_category_id = parent_category_id

# Создаем список категорий, включая родительские и дочерние
categories: List[models.Category | models.ChildCategory] = [
    MockCategory(1),  # Родительская категория
    MockCategory(2, 1),  # Дочерняя категория
    MockCategory(3),  # Еще одна родительская категория
    MockCategory(4, 3)   # Дочерняя категория
]

# Фильтруем родительские категории
parent_categories = filter_parent_categories(categories)

# Выводим ID родительских категорий
parent_category_ids = [cat.category_id for cat in parent_categories]
print(parent_category_ids)  # Вывод: [1, 3]
```

### `filter_child_categories`

```python
def filter_child_categories(categories: List[models.Category | models.ChildCategory],
                            parent_category_id: int) -> List[models.ChildCategory]:
    """
    Фильтрует и возвращает список дочерних категорий, принадлежащих указанной родительской категории.

    Args:
        categories (List[models.Category | models.ChildCategory]): Список объектов категорий или дочерних категорий.
        parent_category_id (int): ID родительской категории, по которому нужно отфильтровать дочерние категории.

    Returns:
        List[models.ChildCategory]: Список объектов дочерних категорий с указанным ID родительской категории.
    """
```

**Назначение**:
Функция `filter_child_categories` принимает список категорий и идентификатор родительской категории, после чего возвращает список дочерних категорий, принадлежащих указанной родительской категории.

**Параметры**:
- `categories` (List[models.Category | models.ChildCategory]): Список категорий для фильтрации. Каждый элемент списка должен быть объектом типа `models.Category` или `models.ChildCategory`.
- `parent_category_id` (int): Идентификатор родительской категории, по которому производится фильтрация дочерних категорий.

**Возвращает**:
- `List[models.ChildCategory]`: Список дочерних категорий, принадлежащих указанной родительской категории.

**Как работает функция**:

1. **Инициализация**: Создается пустой список `filtered_categories` для хранения отфильтрованных категорий.
2. **Проверка входных данных**: Проверяется, является ли входной параметр `categories` экземпляром `str`, `int` или `float`. Если да, то он преобразуется в список, чтобы обеспечить возможность итерации.
3. **Итерация по категориям**: Функция проходит по каждой категории в списке `categories`.
4. **Проверка атрибута `parent_category_id` и соответствия ID**: Для каждой категории проверяется наличие атрибута `parent_category_id` и его соответствие значению `parent_category_id`, переданному в функцию.
5. **Добавление в отфильтрованный список**: Если категория имеет атрибут `parent_category_id`, и его значение совпадает с переданным `parent_category_id`, категория добавляется в список `filtered_categories`.
6. **Возврат результата**: После завершения итерации функция возвращает список `filtered_categories`, содержащий только дочерние категории, принадлежащие указанной родительской категории.

**Примеры**:

```python
from typing import List
from .. import models

# Пример использования с фиктивными данными
class MockCategory:
    def __init__(self, category_id: int, parent_category_id: int = None):
        self.category_id = category_id
        self.parent_category_id = parent_category_id

# Создаем список категорий, включая родительские и дочерние
categories: List[models.Category | models.ChildCategory] = [
    MockCategory(1),  # Родительская категория
    MockCategory(2, 1),  # Дочерняя категория для категории 1
    MockCategory(3),  # Еще одна родительская категория
    MockCategory(4, 3)   # Дочерняя категория для категории 3
]

# Фильтруем дочерние категории для parent_category_id = 1
child_categories = filter_child_categories(categories, 1)

# Выводим ID дочерних категорий
child_category_ids = [cat.category_id for cat in child_categories]
print(child_category_ids)  # Вывод: [2]