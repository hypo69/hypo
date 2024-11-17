```markdown
# hypotez/src/product/product_fields/utils/product_fields_normalizer.py

Файл: `C:\Users\user\Documents\repos\hypotez\src\product\product_fields\utils\product_fields_normalizer.py`
Роль: `doc_creator`

Этот модуль предоставляет функции для нормализации данных полей продукта.  Он обрабатывает различные типы данных, такие как строки и булевы значения, возвращая их в стандартизированном формате.


## Функции:

**`normalize_product_name(value: str) -> str`**

Нормализует имя продукта.

**Аргументы:**

* `value` (str): Имя продукта, которое требуется нормализовать.

**Возвращаемое значение:**

* str: Нормализованное имя продукта.


**`normalize_bool(value: Union[str, bool]) -> int`**

Преобразует булевы значения (строковые или прямое булевое значение) в 1 или 0.

**Аргументы:**

* `value` (Union[str, bool]): Значение, которое требуется преобразовать.

**Возвращаемое значение:**

* int: 1, если `value` истинно, 0, если `value` ложно.


## Пример использования:

```python
from hypotez.src.product.product_fields.utils.product_fields_normalizer import normalize_product_name, normalize_bool

product_name = "  Product Name  "
normalized_name = normalize_product_name(product_name)
print(f"Нормализованное имя продукта: {normalized_name}")

is_active = "true"
active_int = normalize_bool(is_active)
print(f"Активность (1/0): {active_int}")

is_not_active = "false"
not_active_int = normalize_bool(is_not_active)
print(f"Активность (1/0): {not_active_int}")


is_active_bool = True
active_int = normalize_bool(is_active_bool)
print(f"Активность (1/0): {active_int}")
```


## Замечания:

* Данный модуль использует вспомогательные функции из модулей `StringNormalizer` и `StringFormatter`.  Эти вспомогательные функции должны быть определены в модулях `src.utils.string`.
*  Константа `MODE` с значением `'debug'` указывает на режим работы модуля (в данном случае, это режим отладки).  Для production окружения, эта константа может быть изменена.


```