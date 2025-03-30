# Модуль `get_product_id`

## Обзор

Модуль `get_product_id` предназначен для извлечения идентификатора продукта из входной строки, представляющей собой "сырой" ID продукта. Он использует функцию `extract_prod_ids` для поиска и возврата ID. В случае, если ID не найден, вызывается исключение `ProductIdNotFoundException`.

## Подробней

Этот модуль является частью подсистемы для работы с AliExpress API, в частности, для обработки и стандартизации идентификаторов продуктов. Он помогает унифицировать процесс получения ID, независимо от формата входных данных (например, ID может быть частью URL или просто строкой с номером).

## Функции

### `get_product_id`

```python
def get_product_id(raw_product_id: str) -> str:
    """Returns the product ID from a given text. Raises ProductIdNotFoundException on fail."""
```

**Описание**: Извлекает и возвращает ID продукта из предоставленной строки.

**Параметры**:
- `raw_product_id` (str): Строка, содержащая "сырой" ID продукта.

**Возвращает**:
- `str`: Идентификатор продукта.

**Вызывает исключения**:
- `ProductIdNotFoundException`: Если ID продукта не найден в предоставленной строке.

**Примеры**:

```python
from src.suppliers.aliexpress.api.tools.get_product_id import get_product_id

# Пример успешного извлечения ID
product_id = get_product_id("1234567890")
print(product_id)  # Вывод: 1234567890

# Пример генерации исключения, если ID не найден (предполагается, что extract_prod_ids возвращает None)
try:
    product_id = get_product_id("invalid_id")
    print(product_id)
except ProductIdNotFoundException as ex:
    print(f"Error: {ex}")  # Вывод: Error: Product id not found: invalid_id