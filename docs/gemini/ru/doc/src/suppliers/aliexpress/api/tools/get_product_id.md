# Модуль get_product_id

## Обзор

Этот модуль содержит функцию `get_product_id`, которая извлекает идентификатор продукта из заданного текста.  Модуль использует вспомогательную функцию `extract_prod_ids` из модуля `src.suppliers.aliexpress.utils.extract_product_id` для извлечения идентификатора.

## Оглавление

* [Функции](#функции)


## Функции

### `get_product_id`

**Описание**: Возвращает идентификатор продукта из заданного текста.  Возвращает `None` если идентификатор не найден. Поднимает исключение `ProductIdNotFoundException`, если идентификатор не может быть извлечён.

**Параметры**:

* `raw_product_id` (str):  Входной текст, содержащий идентификатор продукта.

**Возвращает**:

* `str`: Идентификатор продукта, если он найден; `None` в противном случае.

**Вызывает исключения**:

* `ProductIdNotFoundException`: Если идентификатор продукта не найден в предоставленном тексте.


```
```python
from ..errors import ProductIdNotFoundException
from src.suppliers.aliexpress.utils.extract_product_id import extract_prod_ids
import re
def get_product_id(raw_product_id: str) -> str:
    """Returns the product ID from a given text. Raises ProductIdNotFoundException on fail."""
    return extract_prod_ids(raw_product_id)
```
**Примечания**:
Функция `get_product_id`  сейчас использует функцию `extract_prod_ids` для извлечения данных.  Предыдущие реализации, основанные на регулярных выражениях, были удалены, поскольку они имели низкую эффективность и были неэффективны в обработке широкого спектра входных данных.  Следует использовать более специализированный механизм для извлечения данных.