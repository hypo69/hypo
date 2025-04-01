# Модуль для извлечения ID продукта из текста

## Обзор

Модуль `get_product_id.py` предназначен для извлечения идентификатора продукта (product ID) из различных форматов входных данных, таких как URL-адреса или текстовые строки. Он использует функцию `extract_prod_ids` для поиска и возврата идентификатора продукта. Если идентификатор не найден, вызывается исключение `ProductIdNotFoundException`.

## Подробней

Этот модуль является частью системы обработки данных о товарах с AliExpress. Он используется для стандартизации и унификации идентификаторов продуктов, что необходимо для дальнейшей обработки и хранения информации о товарах. Модуль гарантирует, что извлекаемый ID продукта соответствует ожидаемому формату, и сообщает об ошибке, если ID не может быть извлечен.

## Функции

### `get_product_id`

```python
def get_product_id(raw_product_id: str) -> str:
    """Returns the product ID from a given text. Raises ProductIdNotFoundException on fail."""
    return extract_prod_ids(raw_product_id)
```

**Назначение**: Извлекает и возвращает идентификатор продукта из предоставленной строки.

**Параметры**:

-   `raw_product_id` (str): Строка, содержащая потенциальный идентификатор продукта, который может быть частью URL-адреса или просто числовым значением.

**Возвращает**:

-   `str`: Идентификатор продукта, если он найден.

**Вызывает исключения**:

-   `ProductIdNotFoundException`: Если идентификатор продукта не найден во входной строке.

**Как работает функция**:

1.  Функция принимает строку `raw_product_id` в качестве аргумента.
2.  Вызывает функцию `extract_prod_ids` с переданной строкой.
3.  Возвращает результат, полученный от функции `extract_prod_ids`.

**ASCII flowchart**:

```
A[Прием raw_product_id]
|
B[Вызов extract_prod_ids(raw_product_id)]
|
C[Возврат результата]
```

**Примеры**:

```python
from src.suppliers.aliexpress.api.tools.get_product_id import get_product_id
from src.suppliers.aliexpress.api.errors import ProductIdNotFoundException

# Пример 1: Успешное извлечение ID продукта
product_id = get_product_id("1234567890")
print(product_id)  # Вывод: 1234567890

# Пример 2: Попытка извлечения ID продукта из строки без ID
try:
    product_id = get_product_id("No product ID here")
except ProductIdNotFoundException as ex:
    print(f"Ошибка: {ex}")  # Вывод: Ошибка: Product id not found: No product ID here