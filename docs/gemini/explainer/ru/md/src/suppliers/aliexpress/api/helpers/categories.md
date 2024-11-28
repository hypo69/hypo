# Модуль `hypotez/src/suppliers/aliexpress/api/helpers/categories.py`

```markdown
## Файл `hypotez/src/suppliers/aliexpress/api/helpers/categories.py`

**Описание:** Модуль содержит функции для фильтрации категорий и подкатегорий API AliExpress.

**Функции:**

**`filter_parent_categories(categories: List[models.Category | models.ChildCategory]) -> List[models.Category]`**

* **Описание:** Фильтрует список категорий и возвращает список родительских категорий, у которых нет родительской категории.
* **Параметры:**
    * `categories`: Список объектов `Category` или `ChildCategory`.  Может принимать и единственное значение (не список) -- в этом случае оно преобразуется в список.
* **Возвращаемое значение:** Список объектов `Category`, не имеющих родительской категории.
* **Обработка ошибок:** Не содержит явного механизма обработки ошибок, но предполагается, что входные данные `categories` содержат корректные объекты. Функция корректно обрабатывает случай, когда в качестве входного параметра передано значение, которое не является списком объектов категорий (строка, число, float), преобразовывая его в список из одного элемента.
* **Пример использования:**

```python
# Предполагая, что models.Category и models.ChildCategory определены где-то в проекте
# ... (код для создания объектов)
parent_category = models.Category(id=1, name='Parent')
child_category1 = models.ChildCategory(id=2, name='Child 1', parent_category_id=1)
child_category2 = models.ChildCategory(id=3, name='Child 2', parent_category_id=1)
categories = [parent_category, child_category1, child_category2]

parent_categories = filter_parent_categories(categories)
# parent_categories будет содержать [parent_category]
```


**`filter_child_categories(categories: List[models.Category | models.ChildCategory], parent_category_id: int) -> List[models.ChildCategory]`**

* **Описание:** Фильтрует список категорий и возвращает список дочерних категорий, принадлежащих указанной родительской категории.
* **Параметры:**
    * `categories`: Список объектов `Category` или `ChildCategory`. Может принимать и единственное значение (не список) -- в этом случае оно преобразуется в список.
    * `parent_category_id`: Идентификатор родительской категории для фильтрации.
* **Возвращаемое значение:** Список объектов `ChildCategory`, имеющих указанный `parent_category_id`.
* **Обработка ошибок:** Аналогично `filter_parent_categories`, предполагает корректные входные данные. Обрабатывает случай, когда в качестве входного параметра передано значение, которое не является списком объектов категорий (строка, число, float).
* **Пример использования:**

```python
# ... (код для создания объектов, см. пример выше)

child_categories = filter_child_categories(categories, parent_category_id=1)
# child_categories будет содержать [child_category1, child_category2]
```


**Примечание:**  Код предполагает наличие классов `models.Category` и `models.ChildCategory` в модуле `..`. Также предполагается, что у класса `ChildCategory` есть атрибут `parent_category_id`.
```