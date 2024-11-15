```markdown
# categories.py

Расположение файла: `C:\Users\user\Documents\repos\hypotez\src\suppliers\aliexpress\api\helpers\categories.py`

**Роль:** `doc_creator` - создание документации для функций, фильтрующих категории и подкатегории API Aliexpress.

**Описание:**

Файл `categories.py` содержит функции для фильтрации категорий и подкатегорий, возвращаемых API AliExpress.  Функции позволяют выделить родительские категории и подкатегории, относящиеся к определённому родительскому элементу.

**Функции:**

* **`filter_parent_categories(categories: List[models.Category | models.ChildCategory]) -> List[models.Category]`**:

    Фильтрует список категорий и подкатегорий, возвращая только родительские категории (без родительских элементов).

    * **Параметры:**
        * `categories`: Список объектов `Category` или `ChildCategory` (модели).  Может быть ошибочно передан как строка, число или другое значение, не являющееся списком категорий.
    * **Возвращаемое значение:**
        * Список объектов `Category` без родительских элементов. Если входной параметр `categories` не является списком, то возвращается список, содержащий единственный элемент - входной параметр.

* **`filter_child_categories(categories: List[models.Category | models.ChildCategory], parent_category_id: int) -> List[models.ChildCategory]`**:

    Фильтрует список категорий и подкатегорий, возвращая только подкатегории, относящиеся к определённому родительскому элементу.

    * **Параметры:**
        * `categories`: Список объектов `Category` или `ChildCategory`.  Может быть ошибочно передан как строка, число или другое значение, не являющееся списком категорий.
        * `parent_category_id`: Идентификатор родительской категории для фильтрации.
    * **Возвращаемое значение:**
        * Список объектов `ChildCategory`, относящихся к указанной родительской категории. Если входной параметр `categories` не является списком, то возвращается список, содержащий единственный элемент - входной параметр.


**Важно:**

* Функции предполагают, что входящие списки (`categories`) содержат объекты моделей `Category` и `ChildCategory`, определённые в модуле `models`.  В коде использовано `from .. import models`, поэтому необходимо убедиться, что модуль `models` находится в соответствующей директории, иначе произойдёт ошибка импорта.
* Добавлены проверки на случай, если в качестве входного параметра передаётся не список, а одиночное значение (строка, число и т.п.), предотвращая ошибки. Это важный шаг для повышения надёжности кода.
* Документация соответствует PEP 257.


**Пример использования (предполагая наличие соответствующих моделей):**

```python
from src.suppliers.aliexpress.api.helpers import categories
from src.suppliers.aliexpress.api import models #  Допустим, правильное импортирование

# Пример данных (замените на реальные данные)
categories_data = [models.Category(id=1, name='Electronics'),
                   models.ChildCategory(id=2, name='Phones', parent_category_id=1),
                   models.ChildCategory(id=3, name='Laptops', parent_category_id=1),
                   models.Category(id=4, name='Clothing')]


parent_categories = categories.filter_parent_categories(categories_data)
phones_categories = categories.filter_child_categories(categories_data, parent_category_id=1)


print(parent_categories)  # Выведет [Category(id=1, name='Electronics'), Category(id=4, name='Clothing')]
print(phones_categories)  # Выведет [ChildCategory(id=2, name='Phones', parent_category_id=1)]
```
