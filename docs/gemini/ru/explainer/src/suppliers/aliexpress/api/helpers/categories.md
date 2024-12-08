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

**filter_parent_categories:**

1. Принимает список `categories` (объекты `Category` или `ChildCategory`).
2. Проверяет, является ли вход `categories` списком. Если нет, преобразует его в список.
3. Итерируется по каждому элементу в `categories`.
4. Проверяет, есть ли атрибут `parent_category_id` у текущего элемента.
5. Если атрибут `parent_category_id` отсутствует, добавляет текущий элемент в `filtered_categories`.
6. Возвращает `filtered_categories`.

**Пример:**

Вход: `[Category(id=1), ChildCategory(id=2, parent_category_id=3), Category(id=3, parent_category_id=None)]`

Выход: `[Category(id=1), Category(id=3)]`

**filter_child_categories:**

1. Принимает список `categories` (объекты `Category` или `ChildCategory`) и `parent_category_id`.
2. Проверяет, является ли вход `categories` списком. Если нет, преобразует его в список.
3. Итерируется по каждому элементу в `categories`.
4. Проверяет, есть ли атрибут `parent_category_id` у текущего элемента и равен ли он `parent_category_id`.
5. Если атрибут есть и значения равны, добавляет текущий элемент в `filtered_categories`.
6. Возвращает `filtered_categories`.

**Пример:**

Вход: `[Category(id=1, parent_category_id=3), ChildCategory(id=2, parent_category_id=3), ChildCategory(id=4, parent_category_id=5)]`, `parent_category_id = 3`

Выход: `[ChildCategory(id=2, parent_category_id=3)]`


# <mermaid>

```mermaid
graph LR
    A[categories] --> B{isinstance(categories, list)?};
    B -- yes --> C[for category in categories];
    B -- no --> D[categories = [categories]];
    C --> E{hasattr(category, 'parent_category_id')?};
    E -- yes --> F[category.parent_category_id == parent_category_id?];
    F -- yes --> G[filtered_categories.append(category)];
    F -- no --> H[Null];
    E -- no --> G;
    G --> I[return filtered_categories];
    D --> C;
```

# <explanation>

**Импорты:**

- `from typing import List, Union`: Импортирует типы данных `List` и `Union` для лучшей типизации.
- `from .. import models`: Импортирует модуль `models` из родительского каталога `suppliers/aliexpress/api`.  Это предполагает, что `models` содержит определения классов для `Category` и `ChildCategory`.  Связь с другими частями проекта:  `models` вероятно содержит структуры данных для работы с категориями товаров, а функции в текущем модуле (`categories.py`) используют эти данные для фильтрации.

**Классы:**

- `Category` и `ChildCategory`:  Не определены в данном коде, но предполагается, что они находятся в модуле `models`. Классы вероятно представляют собой структуры данных для категорий и подкатегорий товаров.  Атрибуты `id` и `parent_category_id` необходимы для работы фильтрации.

**Функции:**

- `filter_parent_categories(categories: List[models.Category | models.ChildCategory]) -> List[models.Category]`:
    - Принимает список категорий и подкатегорий.
    - Возвращает список категорий, у которых нет родительской категории.
    - Обрабатывает случай, когда `categories` не является списком, превращая его в список.
- `filter_child_categories(categories: List[models.Category | models.ChildCategory], parent_category_id: int) -> List[models.ChildCategory]`:
    - Принимает список категорий и подкатегорий и ID родительской категории.
    - Возвращает список подкатегорий, которые относятся к заданной родительской категории.
    - Обрабатывает случай, когда `categories` не является списком, превращая его в список.

**Переменные:**

- `filtered_categories`: Список, в который добавляются отфильтрованные категории.  Типизирован как `List[models.Category]` или `List[models.ChildCategory]`.


**Возможные ошибки или области для улучшений:**

- **Валидация входных данных:** Функции могли бы проверять, что входные данные `categories` являются списками, и содержат ожидаемые типы данных (объекты `Category` или `ChildCategory`).  Дополнительно можно было бы добавлять проверку, чтобы  `parent_category_id` был валидным значением, учитывая схему базы данных.
- **Использование `isinstance`:**  В коде используется проверка `isinstance(categories, (str, int, float))` для конвертации в список, но это может привести к ошибкам, если `categories` имеет другой тип. Вместо этого, было бы полезно иметь более точный способ проверки, соответствует ли входное значение ожидаемому типу данных, например, используя `isinstance` для проверки, что `categories` является объектом `List`.

**Цепочка взаимосвязей:**

Функции `filter_parent_categories` и `filter_child_categories` из модуля `categories.py` напрямую взаимодействуют с данными, которые им предоставляют другие части проекта.  Эти данные, вероятно, получаются из API запросов или других источников данных, и далее результаты фильтрации могут быть использованы в других частях проекта для обработки, отображения или дальнейшей работы с данными.