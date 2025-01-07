# <input code>

```python
## \file hypotez/src/suppliers/aliexpress/api/helpers/categories.py
# -*- coding: utf-8 -*-\
 # <- venv win
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

**Алгоритм `filter_parent_categories`:**

1. Принимает список категорий.
2. Проверяет, является ли входной параметр `categories` списком, или одиночным значением (строкой, числом).  Если это не список, то преобразует его в список.
3. Итерируется по каждой категории в списке.
4. Проверяет, содержит ли текущая категория атрибут `parent_category_id`.
5. Если атрибут `parent_category_id` отсутствует, добавляет категорию в результирующий список `filtered_categories`.
6. Возвращает список `filtered_categories`.

**Пример:**

Вход: `[Category(id=1), ChildCategory(id=2, parent_category_id=3), Category(id=3, parent_category_id=None)]`
Выход: `[Category(id=1), Category(id=3, parent_category_id=None)]`

**Алгоритм `filter_child_categories`:**

1. Принимает список категорий и ID родительской категории.
2. Проверяет, является ли входной параметр `categories` списком, или одиночным значением (строкой, числом).  Если это не список, то преобразует его в список.
3. Итерируется по каждой категории в списке.
4. Проверяет, содержит ли текущая категория атрибут `parent_category_id` и равен ли он переданному `parent_category_id`.
5. Если оба условия верны, добавляет категорию в результирующий список `filtered_categories`.
6. Возвращает список `filtered_categories`.

**Пример:**

Вход: `[ChildCategory(id=2, parent_category_id=3), ChildCategory(id=4, parent_category_id=5), Category(id=1)]`, `parent_category_id = 3`
Выход: `[ChildCategory(id=2, parent_category_id=3)]`


# <mermaid>

```mermaid
graph TD
    A[Входной список категорий] --> B{Проверка на список};
    B -- Список -- > C[Итерация по категориям];
    B -- Не список -- > D[Преобразование в список];
    D --> C;
    C --> E{Проверка на parent_category_id (filter_parent_categories)};
    E -- Отсутствует -- > F[Добавление в filtered_categories];
    E -- Есть -- > G[Пропускается];
    F --> H[Возврат filtered_categories];
    G --> C;
    C -- (filter_child_categories) -- > I{Проверка на parent_category_id и совпадение};
    I -- Совпадает -- > J[Добавление в filtered_categories];
    I -- Не совпадает -- > K[Пропускается];
    J --> H;
    K --> C;

    subgraph Объекты
        Category
        ChildCategory
    end

    style F fill:#ccf,stroke:#333,stroke-width:2px,stroke-dasharray:5 5;
    style J fill:#ccf,stroke:#333,stroke-width:2px,stroke-dasharray:5 5;
    
```

# <explanation>

**Импорты:**

- `from typing import List, Union`: Импортирует типы данных из модуля `typing` для более ясной типизации. `List` используется для работы со списками, `Union` используется для указания, что параметр может быть одного из нескольких типов.
- `from .. import models`: Импортирует модуль `models` из пакета `..` (две точки обозначают "два уровня вверх" в файловой системе). Этот импорт предполагает, что в директории `hypotez/src/suppliers/aliexpress/api/models.py` определены классы `models.Category` и `models.ChildCategory`, содержащие данные о категориях и подкатегориях.  Неявная зависимость от моделей.

**Классы:**

В коде не объявлены классы.  Они предполагаются в модуле `models`, на который ссылается импорт. Классы `Category` и `ChildCategory` (или их аналоги) должны иметь атрибут `parent_category_id` для работы функций.

**Функции:**

- `filter_parent_categories(categories: List[models.Category | models.ChildCategory]) -> List[models.Category]`:  Фильтрует список категорий, возвращая только родительские категории (без родительской категории).
    - Принимает список категорий (`categories`).  Обработка не-списков (строки, числа).
    - Возвращает список `models.Category`, где `parent_category_id` отсутствует.
- `filter_child_categories(categories: List[models.Category | models.ChildCategory], parent_category_id: int) -> List[models.ChildCategory]`: Фильтрует список категорий, возвращая только подкатегории, относящиеся к указанному родительскому элементу.
    - Принимает список категорий (`categories`) и ID родительской категории (`parent_category_id`). Обработка не-списков (строки, числа).
    - Возвращает список `models.ChildCategory`, где `parent_category_id` соответствует переданному значению.

**Переменные:**

- `filtered_categories`: Список, который используется для хранения отфильтрованных категорий.  Тип `List`.

**Возможные ошибки и улучшения:**

- **Проверка типов:** В текущем коде есть обработка, если введен не список, но более подходящим вариантом может быть поднятие исключения `TypeError`.  Например:  
  ```python
  if not isinstance(categories, list):
      raise TypeError("Input 'categories' must be a list.")
  ```
- **Обработка ошибок:** Функции не проверяют, что переданные категории являются экземплярами `models.Category` или `models.ChildCategory`.  Возможные проблемы с несоответствием типов могут привести к ошибке.  Добавление проверки поможет предотвратить ошибки во время выполнения.  
```python
  if not all(isinstance(cat, (models.Category, models.ChildCategory)) for cat in categories):
      raise TypeError("All elements in 'categories' must be instances of Category or ChildCategory")
```
- **Документация:**  Добавить более полную документацию к функциям, включающую  примеры использования.


**Взаимосвязи с другими частями проекта:**

Функции из этого модуля используются для фильтрации данных, получаемых из API Aliexpress.  Они зависят от моделей данных (`models.Category` и `models.ChildCategory`),  определенных в другом модуле (`models.py`).  Также, вероятно, эти функции используются в других частях приложения, например, для отображения или дальнейшей обработки полученных категорий.
```
+-----------------+        +---------------------+
| api/helpers/     |        | api/models/         |
| categories.py    | ----> | models.py           |
+-----------------+        +---------------------+
          |
          V
+---------------------+
| Другие части проекта |
+---------------------+