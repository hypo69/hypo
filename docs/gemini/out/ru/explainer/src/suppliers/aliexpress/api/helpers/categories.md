# <input code>

```python
## \file hypotez/src/suppliers/aliexpress/api/helpers/categories.py
# -*- coding: utf-8 -*-\
#! venv/Scripts/python.exe # <- venv win
## ~~~~~~~~~~~~~\
""" module: src.suppliers.aliexpress.api.helpers """

"""  функции для фильтрации категорий и подкатегорий API Aliexpress"""
from typing import List, Union
from .. import models
#from src.suppliers.aliexpress.api.api import models

def filter_parent_categories(categories: List[models.Category | models.ChildCategory]) -> List[models.Category]:
    """
    Filters and returns a list of categories that do not have a parent category.

    @param categories: List of category or child category objects.
    @return: List of category objects without a parent category.
    """
    filtered_categories = []
    
    if isinstance(categories, (str, int, float)):
        categories = [categories]  # Convert to list if a single non-category value is passed.

    for category in categories:
        if not hasattr(category, 'parent_category_id'):
            filtered_categories.append(category)

    return filtered_categories

def filter_child_categories(categories: List[models.Category | models.ChildCategory],
                            parent_category_id: int) -> List[models.ChildCategory]:
    """
    Filters and returns a list of child categories that belong to the specified parent category.

    @param categories: List of category or child category objects.
    @param parent_category_id: The ID of the parent category to filter child categories by.
    @return: List of child category objects with the specified parent category ID.
    """
    filtered_categories = []
    
    if isinstance(categories, (str, int, float)):
        categories = [categories]  # Convert to list if a single non-category value is passed.

    for category in categories:
        if hasattr(category, 'parent_category_id') and category.parent_category_id == parent_category_id:
            filtered_categories.append(category)

    return filtered_categories
```

# <algorithm>

**Функция `filter_parent_categories`:**

1. Принимает список категорий (`categories`).
2. Если входной параметр `categories` не является списком, преобразует его в список.
3. Итерируется по каждой категории в списке.
4. Проверяет, есть ли у категории атрибут `parent_category_id`.
5. Если атрибута нет, добавляет категорию в `filtered_categories`.
6. Возвращает список `filtered_categories`.

**Функция `filter_child_categories`:**

1. Принимает список категорий (`categories`) и идентификатор родительской категории (`parent_category_id`).
2. Если входной параметр `categories` не является списком, преобразует его в список.
3. Итерируется по каждой категории в списке.
4. Проверяет, есть ли у категории атрибут `parent_category_id` и совпадает ли он с переданным `parent_category_id`.
5. Если оба условия верны, добавляет категорию в `filtered_categories`.
6. Возвращает список `filtered_categories`.

**Пример:**

```
categories = [category1, category2, childCategory1, childCategory2]

category1.parent_category_id = None
category2.parent_category_id = 10
childCategory1.parent_category_id = 10
childCategory2.parent_category_id = 20

parent_categories = filter_parent_categories(categories)  # parent_categories = [category1]
child_categories = filter_child_categories(categories, 10) # child_categories = [childCategory1]
```

# <mermaid>

```mermaid
graph LR
    A[categories] --> B{isinstance(categories, (str, int, float))}
    B -- True --> C[categories = [categories]]
    B -- False --> D[loop over categories]
    D --> E{hasattr(category, 'parent_category_id')}
    E -- True --> F[filter_child_categories]
    E -- False --> G[filtered_categories.append(category)]
    F --> H{category.parent_category_id == parent_category_id}
    H -- True --> G
    H -- False --> I[Continue]
    G --> J[return filtered_categories]
    C --> D
```

# <explanation>

**Импорты:**

- `from typing import List, Union`: Импортирует типы данных `List` и `Union` для явного определения типов аргументов и возвращаемых значений функций. Это повышает читабельность и позволяет использовать статическую типизацию.
- `from .. import models`: Импортирует модуль `models` из родительского каталога (`suppliers/aliexpress/api`).  Эта конструкция предполагает, что файл `models.py` содержит определения классов `Category` и `ChildCategory`, которые используются в текущем модуле.


**Классы:**

Этот код не определяет классы, а использует классы из `models`,  предполагая, что эти классы содержат атрибуты, такие как `parent_category_id`.


**Функции:**

- `filter_parent_categories(categories: List[models.Category | models.ChildCategory]) -> List[models.Category]`:
    - Принимает список категорий (или подкатегорий) и фильтрует его, возвращая список категорий без родительской категории.
    - Принимает список категорий,  обрабатывает также случаи, когда вход не является списком,  используя `isinstance`, что делает функцию более гибкой.

- `filter_child_categories(categories: List[models.Category | models.ChildCategory], parent_category_id: int) -> List[models.ChildCategory]`:
    - Принимает список категорий и идентификатор родительской категории.
    - Фильтрует список, возвращая только подкатегории, относящиеся к указанной родительской категории.

**Переменные:**

- `filtered_categories`: Список, в который помещаются отфильтрованные категории.

**Возможные ошибки или улучшения:**

- Необходимо убедиться, что `models.Category` и `models.ChildCategory` действительно содержат атрибут `parent_category_id`. В противном случае возникнут ошибки во время выполнения.
- Возможно, полезно добавить проверку на `None` для `parent_category_id` в `filter_child_categories` для повышения устойчивости к неожиданным данным.
- Для повышения эффективности, особенно при работе с большими наборами данных, можно рассмотреть использование `filter()` вместо циклов `for`.

**Взаимосвязи с другими частями проекта:**

Этот модуль (`categories.py`) тесно связан с модулем `models.py` (где определены классы `Category` и `ChildCategory`), который, скорее всего, импортируется из пакета `aliexpress.api`.  Файлы из папки `aliexpress.api` взаимодействуют с API Aliexpress, чтобы получать данные о категориях и подкатегориях.