```MD
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

**Алгоритм работы функций:**

**`filter_parent_categories`:**

1. Принимает список категорий (`categories`).
2. Проверяет, является ли вход `categories` списком. Если нет, преобразует в список.
3. Итерируется по каждой категории в списке.
4. Проверяет, содержит ли текущая категория атрибут `parent_category_id`.
5. Если атрибут `parent_category_id` отсутствует, добавляет текущую категорию в список `filtered_categories`.
6. Возвращает список `filtered_categories`.

**Пример:**

Вход: `[category1, category2, child_category1]` где `category1` и `category2` - объекты `models.Category`, а `child_category1` - `models.ChildCategory`.

Предположим, `category1` и `child_category1` имеют атрибут `parent_category_id`, а `category2` - нет.

Результат: `[category2]`

**`filter_child_categories`:**

1. Принимает список категорий (`categories`) и `parent_category_id`.
2. Проверяет, является ли вход `categories` списком. Если нет, преобразует в список.
3. Итерируется по каждой категории в списке.
4. Проверяет, содержит ли текущая категория атрибут `parent_category_id`.
5. Если атрибут `parent_category_id` существует и равен `parent_category_id`, добавляет текущую категорию в список `filtered_categories`.
6. Возвращает список `filtered_categories`.


**Пример:**

Вход: `[child_category1, child_category2, category1]`, `parent_category_id = 10`.


Предположим, `child_category1` имеет `parent_category_id = 10`, а `child_category2` - `parent_category_id = 20`.

Результат: `[child_category1]`

# <mermaid>

```mermaid
graph LR
    A[categories] --> B{isinstance(categories, list)};
    B -- yes --> C[for category in categories];
    B -- no --> D[categories = [categories]];
    C --> E{hasattr(category, 'parent_category_id')};
    E -- yes --> F[category.parent_category_id == parent_category_id?];
    F -- yes --> G[filtered_categories.append(category)];
    F -- no --> H;
    E -- no --> I[filtered_categories.append(category)];
    G --> J[return filtered_categories];
    H --> J;
    I --> J;
    
    subgraph "filter_parent_categories"
        E -- no --> I;
    end
```

**Объяснение диаграммы:**

* `categories` - входной список категорий.
* Проверка на список (`B`).
* Цикл (`C`) для обработки каждой категории.
* Проверка на наличие атрибута `parent_category_id` (`E`).
* Для `filter_parent_categories` - непосредственное добавление в `filtered_categories` если атрибут отсутствует (`I`).
* Для `filter_child_categories` проверка на соответствие `parent_category_id` (`F`).
* Возврат `filtered_categories` (`J`).

**Зависимости:**

Функции зависят от `models.Category` и `models.ChildCategory` из модуля `models` в `..`.


# <explanation>

**Импорты:**

* `from typing import List, Union`: Импортирует типы данных `List` и `Union` из модуля `typing`.  Эти типы используются для явного определения типов входных параметров функций, что улучшает читаемость и позволяет статическому анализатору обнаружить потенциальные ошибки.
* `from .. import models`: Импортирует модуль `models` из родительской директории (`..`). Это, скорее всего, модуль, содержащий определения классов `Category` и `ChildCategory`, используемые в функции.

**Классы:**

* Определённых классов в этом файле нет. Классы `Category` и `ChildCategory` предполагаются определёнными в модуле `models` (см. импорт).

**Функции:**

* `filter_parent_categories(categories: List[models.Category | models.ChildCategory]) -> List[models.Category]`: Фильтрует входной список категорий, возвращая список только тех категорий, у которых нет родительской категории.  
* `filter_child_categories(categories: List[models.Category | models.ChildCategory], parent_category_id: int) -> List[models.ChildCategory]`: Фильтрует список категорий, возвращая подкатегории, которые относятся к указанной родительской категории.

**Переменные:**

* `filtered_categories`: Список, в который добавляются отфильтрованные категории.

**Возможные ошибки и улучшения:**

* **Обработка исключений:** Функции не обрабатывают ситуации, когда `category` может быть `None` или иметь другой неподходящий тип. Добавление проверки `isinstance(category, models.Category | models.ChildCategory)` улучшит надёжность.
* **Читаемость:** Вместо `hasattr(category, 'parent_category_id')` возможно использование `getattr(category, 'parent_category_id', None)` для более явного определения возможного `None`.
* **Docstrings:**  Docstrings могли бы быть более подробными, включая примеры использования с различными типами входных данных, а также пояснение возможных ошибок.


**Взаимосвязи с другими частями проекта:**

Функции `filter_parent_categories` и `filter_child_categories` из модуля `categories.py` взаимодействуют с классом `models.Category` и `models.ChildCategory` из модуля `models.py` (судя по импорту `from .. import models`) для доступа к атрибуту `parent_category_id`.  Возможно, эти функции используются в других частях приложения для фильтрации категорий и подкатегорий, например, в API обработчиках, для формирования списков категорий для отображения пользователю.