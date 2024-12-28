## АНАЛИЗ КОДА: `hypotez/src/suppliers/aliexpress/api/helpers/categories.py`

### <алгоритм>

**1. `filter_parent_categories(categories)`**

   - **Начало**: Функция принимает список `categories`, который может содержать объекты `models.Category` или `models.ChildCategory`.
   - **Проверка типа `categories`**: Проверяется, является ли `categories` экземпляром `str`, `int` или `float`. Если да, то `categories` преобразуется в список, содержащий этот единственный элемент.
     - *Пример*: `categories = "test"` преобразуется в `categories = ["test"]`
   - **Итерация**: Перебирается каждый `category` в списке `categories`.
   - **Проверка на наличие атрибута `parent_category_id`**: Для каждого `category` проверяется, есть ли у него атрибут `parent_category_id`.
     - *Пример*: Если `category` – объект `models.Category`, то атрибута `parent_category_id` нет. Если `category` – объект `models.ChildCategory`, то атрибут `parent_category_id` есть.
   - **Добавление в `filtered_categories`**: Если атрибута `parent_category_id` нет, значит, это родительская категория, и она добавляется в список `filtered_categories`.
   - **Конец**: Функция возвращает список `filtered_categories`, содержащий только родительские категории.

**2. `filter_child_categories(categories, parent_category_id)`**

   - **Начало**: Функция принимает список `categories` и `parent_category_id` (целое число).
   - **Проверка типа `categories`**: Проверяется, является ли `categories` экземпляром `str`, `int` или `float`. Если да, то `categories` преобразуется в список, содержащий этот единственный элемент.
      - *Пример*: `categories = 123` преобразуется в `categories = [123]`
   - **Итерация**: Перебирается каждый `category` в списке `categories`.
   - **Проверка на наличие атрибута `parent_category_id` и совпадение ID**: Для каждого `category` проверяется, есть ли у него атрибут `parent_category_id` и равен ли он заданному `parent_category_id`.
      - *Пример*: Если `category` – объект `models.ChildCategory` с `parent_category_id = 123` и `parent_category_id` переданный в функцию равен `123`, то условие истинно.
   - **Добавление в `filtered_categories`**: Если оба условия истинны, значит, это дочерняя категория, принадлежащая указанной родительской, и она добавляется в список `filtered_categories`.
   - **Конец**: Функция возвращает список `filtered_categories`, содержащий только дочерние категории, принадлежащие указанной родительской категории.

### <mermaid>

```mermaid
flowchart TD
    Start_filter_parent_categories[Начало: filter_parent_categories]
    Input_categories_parent(Вход: categories: List[Category | ChildCategory])
    Start_filter_parent_categories --> Input_categories_parent
    
    Check_categories_type_parent{Проверка типа: categories is str, int, float?}
    Input_categories_parent --> Check_categories_type_parent
    
     Convert_to_list_parent{Преобразовать в список: categories = [categories]}
    Check_categories_type_parent -- Yes --> Convert_to_list_parent
    
     Convert_to_list_parent --> Loop_categories_parent
    Check_categories_type_parent -- No --> Loop_categories_parent
    

    Loop_categories_parent[Цикл: for category in categories]
    
    Check_parent_id_attribute{Проверка: hasattr(category, 'parent_category_id')?}
    Loop_categories_parent --> Check_parent_id_attribute
    
    
    Add_to_filtered_parent[Добавить в filtered_categories]
    Check_parent_id_attribute -- No --> Add_to_filtered_parent
    
    Check_parent_id_attribute -- Yes --> Loop_categories_parent
    Add_to_filtered_parent --> Loop_categories_parent
    
    
    End_filter_parent_categories[Конец: return filtered_categories]
   Loop_categories_parent -- end_loop --> End_filter_parent_categories
    
    
    Start_filter_child_categories[Начало: filter_child_categories]
    Input_categories_child(Вход: categories: List[Category | ChildCategory], parent_category_id: int)
   Start_filter_child_categories --> Input_categories_child
   
   Check_categories_type_child{Проверка типа: categories is str, int, float?}
    Input_categories_child --> Check_categories_type_child
    
    Convert_to_list_child{Преобразовать в список: categories = [categories]}
     Check_categories_type_child -- Yes --> Convert_to_list_child
     Convert_to_list_child --> Loop_categories_child
     Check_categories_type_child -- No --> Loop_categories_child
    
    Loop_categories_child[Цикл: for category in categories]
  
    Check_child_id_attribute{Проверка: hasattr(category, 'parent_category_id') AND category.parent_category_id == parent_category_id?}
   Loop_categories_child --> Check_child_id_attribute
    
    
   Add_to_filtered_child[Добавить в filtered_categories]
    Check_child_id_attribute -- Yes --> Add_to_filtered_child
     Add_to_filtered_child --> Loop_categories_child
      Check_child_id_attribute -- No --> Loop_categories_child
    
    End_filter_child_categories[Конец: return filtered_categories]
  Loop_categories_child -- end_loop --> End_filter_child_categories
    
```

**Зависимости `mermaid`:**

- Диаграмма не использует внешние зависимости. Она описывает логику работы функций `filter_parent_categories` и `filter_child_categories` и их взаимодействие.
- В `mermaid` используются условные операторы и циклы, которые наглядно демонстрируют алгоритм работы функций.

### <объяснение>

**Импорты:**

-   `from typing import List, Union`: Импортирует `List` и `Union` из модуля `typing`.
    -   `List` используется для аннотации типов, указывая, что переменная является списком элементов определенного типа.
    -   `Union` используется для аннотации типов, указывая, что переменная может иметь один из нескольких указанных типов.
-   `from .. import models`: Импортирует модуль `models` из родительского пакета. Предполагается, что в `models.py` определены классы `Category` и `ChildCategory`.

**Функции:**

1.  **`filter_parent_categories(categories: List[models.Category | models.ChildCategory]) -> List[models.Category]`**
    -   **Аргументы**:
        -   `categories`: Список, содержащий объекты типов `models.Category` или `models.ChildCategory`.
    -   **Возвращаемое значение**: Список объектов типа `models.Category`.
    -   **Назначение**: Фильтрует входной список `categories` и возвращает только те элементы, которые являются родительскими категориями (т.е., не имеют атрибута `parent_category_id`).
        -   Проверяет каждый элемент списка на наличие атрибута `parent_category_id`.
        -   Если атрибут отсутствует, то элемент считается родительской категорией и добавляется в результирующий список.
        -   Если в функцию передан не список, а строка, число или число с плавающей точкой, то эти значения преобразуются в список, чтобы корректно отработать итерацию по списку.
    -   **Пример**:
        ```python
        from src.suppliers.aliexpress.api import models
        
        parent_cat_1 = models.Category(id=1, name="Category 1")
        child_cat_1 = models.ChildCategory(id=101, name="Child 1", parent_category_id=1)
        parent_cat_2 = models.Category(id=2, name="Category 2")
        
        categories = [parent_cat_1, child_cat_1, parent_cat_2]
        
        filtered_categories = filter_parent_categories(categories)
        print(filtered_categories)  # Output: [<models.Category object at ...>, <models.Category object at ...>]
        # filtered_categories будет содержать parent_cat_1 и parent_cat_2
        ```

2.  **`filter_child_categories(categories: List[models.Category | models.ChildCategory], parent_category_id: int) -> List[models.ChildCategory]`**
    -   **Аргументы**:
        -   `categories`: Список, содержащий объекты типов `models.Category` или `models.ChildCategory`.
        -   `parent_category_id`: Целое число, представляющее ID родительской категории.
    -   **Возвращаемое значение**: Список объектов типа `models.ChildCategory`.
    -   **Назначение**: Фильтрует входной список `categories` и возвращает только те элементы, которые являются дочерними категориями и имеют атрибут `parent_category_id`, равный заданному `parent_category_id`.
        -   Проверяет каждый элемент списка на наличие атрибута `parent_category_id` и его соответствие переданному значению `parent_category_id`.
        -   Если оба условия соблюдены, то элемент считается дочерней категорией, принадлежащей указанной родительской, и добавляется в результирующий список.
        -   Если в функцию передан не список, а строка, число или число с плавающей точкой, то эти значения преобразуются в список, чтобы корректно отработать итерацию по списку.
    -   **Пример**:
        ```python
        from src.suppliers.aliexpress.api import models
        
        parent_cat_1 = models.Category(id=1, name="Category 1")
        child_cat_1 = models.ChildCategory(id=101, name="Child 1", parent_category_id=1)
        child_cat_2 = models.ChildCategory(id=102, name="Child 2", parent_category_id=2)
        
        categories = [parent_cat_1, child_cat_1, child_cat_2]
        
        filtered_categories = filter_child_categories(categories, 1)
        print(filtered_categories) # Output: [<models.ChildCategory object at ...>]
        # filtered_categories будет содержать child_cat_1
        ```

**Переменные:**

-   `categories`: Список объектов, которые могут быть как родительскими, так и дочерними категориями. Может быть списком или единственным значением (строка, число или число с плавающей точкой), в этом случае будет преобразован в список.
-   `filtered_categories`: Список, в который добавляются отфильтрованные категории (родительские или дочерние в зависимости от функции).
-   `parent_category_id`: Идентификатор родительской категории, используемый для фильтрации дочерних категорий.
- `category` временная переменная, используемая в цикле `for`, в которой хранится объект, который обрабатывается в данный момент.

**Потенциальные ошибки и области для улучшения:**

-   **Обработка ошибок:** В коде не предусмотрена явная обработка ошибок. Например, если в `categories` попадёт объект, не имеющий нужных атрибутов, это может вызвать ошибку `AttributeError`.
-   **Проверка типов**: В функциях не выполняется проверка того, что в список `categories` попадают только экземпляры классов `models.Category` и `models.ChildCategory`.
-   **Улучшение читаемости**: Можно было бы использовать более явное определение родительской и дочерней категории, например, путем проверки типа объекта, вместо проверки наличия атрибута `parent_category_id`.
-   **Унификация**: В обеих функциях есть повторяющийся код обработки `categories` если он не является списком. Это можно вынести в отдельную функцию.

**Взаимосвязи с другими частями проекта:**

-   Этот модуль взаимодействует с `src.suppliers.aliexpress.api.models`, где определены классы `Category` и `ChildCategory`, которые он использует для фильтрации.
-   Модуль `categories.py` является частью API Aliexpress и используется для обработки данных, полученных из этого API.
-   Он может быть использован в других частях проекта для выбора категорий товаров, например, для запросов к API.

**Дополнительные замечания:**

-   В коде используется динамическая проверка наличия атрибута через `hasattr`.
-   В коде выполняется проверка на `str, int, float`, чтобы иметь возможность обработать случай, когда в функцию передан не список, а одно значение.
-   Код хорошо структурирован и выполняет поставленные задачи.