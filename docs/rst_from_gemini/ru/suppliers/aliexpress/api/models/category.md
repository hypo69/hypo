```markdown
# hypotez/src/suppliers/aliexpress/api/models/category.py

Расположение файла: `C:\Users\user\Documents\repos\hypotez\src\suppliers\aliexpress\api\models\category.py`
Роль: `doc_creator`

**Описание:**

Файл `category.py` содержит определения моделей категорий для API AliExpress. Он определяет базовые классы `Category` и `ChildCategory`.


**Классы:**

* **`Category`**:
    * `category_id: int`: Идентификатор категории.
    * `category_name: str`: Название категории.

* **`ChildCategory`**:
    * Наследуется от `Category`.
    * `parent_category_id: int`: Идентификатор родительской категории.


**Комментарии:**

* Переменная `MODE` определена дважды и не используется.  Следует удалить дублирование или объяснить её назначение.


**Рекомендации:**

* **Документирование атрибутов:**  Добавьте к атрибутам `category_id`, `category_name` и `parent_category_id` более подробные описания, например, о типе данных, ограничениях и возможных значениях.


**Пример использования (если есть):**

```python
# Пример использования (если есть)
from .category import Category, ChildCategory

# Создание объекта Category
category = Category(category_id=1, category_name="Electronics")

# Создание объекта ChildCategory
child_category = ChildCategory(
    category_id=2,
    category_name="Smartphones",
    parent_category_id=1
)

```

**Примечания:**

*  Дополните документацию примерами использования, если они существуют.
*  Если есть правила валидации или другие особенности работы с этими классами, добавьте соответствующие комментарии.


```
