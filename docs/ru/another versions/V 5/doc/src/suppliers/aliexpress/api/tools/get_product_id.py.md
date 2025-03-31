# Модуль для извлечения идентификатора продукта из текста
## Обзор

Модуль `get_product_id.py` предназначен для извлечения идентификатора продукта из предоставленной строки. Он использует функцию `extract_prod_ids` из модуля `src.suppliers.aliexpress.utils.extract_product_id` для поиска и возврата идентификатора продукта. В случае, если идентификатор не найден, выбрасывается исключение `ProductIdNotFoundException`.

## Подробней

Этот модуль является частью системы для работы с AliExpress и используется для автоматического извлечения идентификаторов продуктов из различных источников, таких как URL-адреса или другие текстовые данные. Идентификатор продукта необходим для дальнейшей работы с API AliExpress, например, для получения информации о продукте или для выполнения других действий, связанных с конкретным продуктом.

## Функции

### `get_product_id`

```python
def get_product_id(raw_product_id: str) -> str:
    """Returns the product ID from a given text. Raises ProductIdNotFoundException on fail."""
```

**Описание**: Извлекает и возвращает идентификатор продукта из предоставленной строки.

**Как работает функция**:
1. Функция принимает строку `raw_product_id` в качестве аргумента.
2. Использует функцию `extract_prod_ids` для извлечения идентификатора продукта из предоставленной строки.
3. Возвращает извлеченный идентификатор продукта.
4. Если идентификатор продукта не найден, функция `extract_prod_ids` должна вызвать исключение `ProductIdNotFoundException`.

**Параметры**:
- `raw_product_id` (str): Строка, содержащая идентификатор продукта или URL, из которого можно извлечь идентификатор.

**Возвращает**:
- `str`: Идентификатор продукта.

**Вызывает исключения**:
- `ProductIdNotFoundException`: Вызывается, если не удается извлечь идентификатор продукта из предоставленной строки.

**Примеры**:

```python
from src.suppliers.aliexpress.api.tools.get_product_id import get_product_id
from src.suppliers.aliexpress.api.errors import ProductIdNotFoundException

# Пример 1: Извлечение идентификатора продукта из строки
product_id = get_product_id("1234567890")
print(product_id)  # Вывод: 1234567890

# Пример 2: Извлечение идентификатора продукта из URL
# (Предполагается, что extract_prod_ids умеет извлекать из URL)
product_id = get_product_id("https://aliexpress.com/item/1234567890.html")
print(product_id)  # Вывод: 1234567890

# Пример 3: Обработка исключения, если идентификатор не найден
try:
    product_id = get_product_id("Неверный формат строки")
    print(product_id)
except ProductIdNotFoundException as ex:
    print(f"Ошибка: {ex}")  # Вывод: Ошибка: Product id not found: Неверный формат строки
```