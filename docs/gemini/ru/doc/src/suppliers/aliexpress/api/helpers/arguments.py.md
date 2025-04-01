# Модуль `arguments.py`

## Обзор

Модуль `arguments.py` содержит вспомогательные функции для обработки и валидации аргументов, передаваемых в API запросах к AliExpress. Он предоставляет методы для преобразования входных данных в нужный формат, а также для проверки их корректности.

## Подробней

Этот модуль предназначен для стандартизации входных данных, используемых в API запросах. Он включает функции для работы со списками идентификаторов продуктов и другими параметрами, что позволяет избежать ошибок и повысить надежность взаимодействия с API.

## Функции

### `get_list_as_string`

```python
def get_list_as_string(value) -> str | None:
    """Преобразует переданное значение в строку, если это список или строка.

    Args:
        value (str | list | None): Значение для преобразования.

    Returns:
        str | None: Строковое представление списка, исходная строка или None, если значение None.

    Raises:
        InvalidArgumentException: Если значение не является строкой, списком или None.
    """
```

**Назначение**:
Функция `get_list_as_string` предназначена для преобразования входного значения в строку. Если входное значение является списком, элементы списка объединяются в строку, разделенную запятыми. Если входное значение уже является строкой, оно возвращается без изменений. Если входное значение равно `None`, функция также возвращает `None`.

**Как работает функция**:

1. Проверяет, является ли входное значение `None`. Если да, возвращает `None`.
2. Проверяет, является ли входное значение строкой. Если да, возвращает его без изменений.
3. Проверяет, является ли входное значение списком. Если да, объединяет элементы списка в строку, разделяя их запятыми, и возвращает полученную строку.
4. Если значение не является ни строкой, ни списком, вызывает исключение `InvalidArgumentException`.

**Примеры**:

```python
from src.suppliers.aliexpress.api.helpers.arguments import get_list_as_string
from src.suppliers.aliexpress.api.errors.exceptions import InvalidArgumentException

# Пример 1: Преобразование списка в строку
value = ['123', '456', '789']
result = get_list_as_string(value)
print(result)  # Вывод: 123,456,789

# Пример 2: Возвращение строки без изменений
value = 'abc,def,ghi'
result = get_list_as_string(value)
print(result)  # Вывод: abc,def,ghi

# Пример 3: Возвращение None
value = None
result = get_list_as_string(value)
print(result)  # Вывод: None

# Пример 4: Вызов исключения
try:
    value = 123
    result = get_list_as_string(value)
except InvalidArgumentException as ex:
    print(ex)  # Вывод: Argument should be a list or string: 123
```

### `get_product_ids`

```python
def get_product_ids(values) -> list:
    """Преобразует входные значения в список идентификаторов продуктов.

    Args:
        values (str | list): Строка с разделенными запятыми идентификаторами или список идентификаторов.

    Returns:
        list: Список идентификаторов продуктов.

    Raises:
        InvalidArgumentException: Если аргумент `product_ids` не является списком или строкой.
    """
```

**Назначение**:
Функция `get_product_ids` предназначена для преобразования входных значений в список идентификаторов продуктов. Если входное значение является строкой, она разделяется на список идентификаторов по запятой. Затем каждый идентификатор продукта в списке обрабатывается функцией `get_product_id` для получения корректного идентификатора.

**Как работает функция**:

1. Проверяет, является ли входное значение строкой. Если да, разделяет строку на список подстрок, используя запятую в качестве разделителя.
2. Проверяет, является ли входное значение списком. Если нет, вызывает исключение `InvalidArgumentException`.
3. Инициализирует пустой список `product_ids`.
4. Итерируется по значениям во входном списке. Для каждого значения вызывает функцию `get_product_id` и добавляет результат в список `product_ids`.
5. Возвращает список `product_ids`.

**Примеры**:

```python
from src.suppliers.aliexpress.api.helpers.arguments import get_product_ids
from src.suppliers.aliexpress.api.errors.exceptions import InvalidArgumentException

# Пример 1: Преобразование строки в список идентификаторов
values = '123,456,789'
result = get_product_ids(values)
print(result)  # Вывод: ['123', '456', '789']

# Пример 2: Преобразование списка в список идентификаторов
values = ['abc', 'def', 'ghi']
result = get_product_ids(values)
print(result)  # Вывод: ['abc', 'def', 'ghi']

# Пример 3: Вызов исключения
try:
    values = 123
    result = get_product_ids(values)
except InvalidArgumentException as ex:
    print(ex)  # Вывод: Argument product_ids should be a list or string