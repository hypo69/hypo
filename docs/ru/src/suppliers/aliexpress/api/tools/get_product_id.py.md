# Модуль: src.suppliers.aliexpress.api.tools

## Обзор

Модуль содержит инструменты для извлечения идентификатора продукта из различных форматов входных данных. Основная функция `get_product_id` использует функцию `extract_prod_ids` для поиска и возврата идентификатора продукта.

## Подробнее

Этот модуль предназначен для работы с идентификаторами продуктов AliExpress. Он пытается извлечь идентификатор из строки, используя регулярные выражения и другие методы. В случае неудачи, выбрасывается исключение `ProductIdNotFoundException`.

## Функции

### `get_product_id`

```python
def get_product_id(raw_product_id: str) -> str:
    """Returns the product ID from a given text. Raises ProductIdNotFoundException on fail."""
```

**Назначение**:
Извлекает и возвращает идентификатор продукта из предоставленной строки. Если идентификатор не найден, выбрасывает исключение `ProductIdNotFoundException`.

**Параметры**:
- `raw_product_id` (str): Строка, содержащая идентификатор продукта или URL.

**Возвращает**:
- `str`: Идентификатор продукта.

**Вызывает исключения**:
- `ProductIdNotFoundException`: Если идентификатор продукта не найден в предоставленной строке.

**Как работает функция**:

1. Функция `get_product_id` принимает строку `raw_product_id` в качестве аргумента.
2. Вызывает функцию `extract_prod_ids` с переданной строкой.
3. `extract_prod_ids` возвращает найденный идентификатор продукта.
4. Функция возвращает извлеченный идентификатор продукта.

**Примеры**:

```python
from src.suppliers.aliexpress.api.tools.get_product_id import get_product_id

# Пример 1: Извлечение идентификатора продукта из строки
product_id = get_product_id("1234567890")
print(product_id)  # Вывод: 1234567890

# Пример 2: Извлечение идентификатора продукта из URL
product_id = get_product_id("https://www.aliexpress.com/item/1234567890.html")
print(product_id)  # Вывод: 1234567890

# Пример 3: Обработка исключения, если идентификатор продукта не найден
try:
    product_id = get_product_id("Some random text")
except ProductIdNotFoundException as ex:
    print(f"Ошибка: {ex}")
```