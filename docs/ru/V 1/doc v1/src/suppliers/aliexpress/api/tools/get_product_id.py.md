# Модуль `get_product_id`

## Обзор

Модуль `get_product_id` предоставляет функцию для извлечения идентификатора продукта из заданного текста. Он использует функцию `extract_prod_ids` для поиска и возврата идентификатора продукта.

## Подробней

Этот модуль предназначен для получения идентификатора продукта из различных форматов входных данных, таких как URL или просто строка с идентификатором. Он используется в проекте `hypotez` для стандартизации и извлечения идентификаторов продуктов AliExpress.

## Функции

### `get_product_id`

```python
def get_product_id(raw_product_id: str) -> str:
    """Returns the product ID from a given text. Raises ProductIdNotFoundException on fail."""
    return extract_prod_ids(raw_product_id)
```

**Описание**: Извлекает идентификатор продукта из заданного текста.

**Параметры**:
- `raw_product_id` (str): Текст, из которого требуется извлечь идентификатор продукта.

**Возвращает**:
- `str`: Идентификатор продукта.

**Вызывает исключения**:
- `ProductIdNotFoundException`: Если идентификатор продукта не найден в заданном тексте.

**Примеры**:

```python
from src.suppliers.aliexpress.api.tools.get_product_id import get_product_id

product_id = get_product_id("1234567890")
print(product_id)  # Вывод: 1234567890

try:
    product_id = get_product_id("https://example.com/item/1234567890.html")
    print(product_id)  # Вывод: 1234567890
except ProductIdNotFoundException as ex:
    print(f"Error: {ex}")