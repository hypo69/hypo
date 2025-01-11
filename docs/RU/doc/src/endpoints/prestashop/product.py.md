# Модуль `product.py`

## Обзор

Модуль `product.py` предоставляет класс `PrestaProduct` для работы с товарами в PrestaShop через API. Класс включает методы для проверки наличия товара, поиска, получения информации по ID и инициализации.

## Оглавление

1. [Классы](#классы)
    - [`PrestaProduct`](#prestaproduct)
        - [`__init__`](#__init__)
        - [`check`](#check)
        - [`search`](#search)
        - [`get`](#get)

## Классы

### `PrestaProduct`

**Описание**: Класс для работы с товарами в PrestaShop. Предоставляет методы для проверки, поиска и получения информации о товарах через API.

**Методы**:
- [`__init__`](#__init__): Инициализация экземпляра класса `PrestaProduct`.
- [`check`](#check): Проверка наличия товара в БД по product_reference (SKU, MKT).
- [`search`](#search): Расширенный поиск в БД по фильтрам.
- [`get`](#get): Возвращает информацию о товаре по ID.

#### `__init__`

**Описание**: Инициализация экземпляра класса `PrestaProduct`. Устанавливает параметры соединения с API PrestaShop.

**Параметры**:
- `credentials` (Optional[dict | SimpleNamespace], optional): Словарь или объект `SimpleNamespace` с параметрами `api_domain` и `api_key`. По умолчанию `None`.
- `api_domain` (Optional[str], optional): Домен API. По умолчанию `None`.
- `api_key` (Optional[str], optional): Ключ API. По умолчанию `None`.

**Вызывает исключения**:
- `ValueError`: Если не переданы параметры `api_domain` и `api_key`.

#### `check`

```python
def check(product_reference: str) -> dict | bool:
    """
    Args:
        product_reference (str): Артикул товара для проверки наличия.

    Returns:
        dict | bool: Возвращает словарь с данными о товаре, если товар найден, иначе False.
    """
    pass
```

**Описание**: Проверяет наличие товара в базе данных PrestaShop по артикулу (`product_reference`).

**Параметры**:
- `product_reference` (str): Артикул товара для проверки наличия.

**Возвращает**:
- `dict | bool`: Возвращает словарь с данными о товаре, если товар найден, иначе `False`.

#### `search`

```python
def search(filter: str, value: str) -> list:
    """
    Args:
        filter (str): Фильтр для поиска, например, `reference` или `name`.
        value (str): Значение для фильтра.

    Returns:
        list: Возвращает список товаров, соответствующих критериям поиска.
    """
    pass
```

**Описание**: Выполняет расширенный поиск товаров в базе данных PrestaShop по заданным фильтрам.

**Параметры**:
- `filter` (str): Фильтр для поиска, например, `reference` или `name`.
- `value` (str): Значение для фильтра.

**Возвращает**:
- `list`: Возвращает список товаров, соответствующих критериям поиска.

#### `get`

```python
def get(id_product: int) -> dict | None:
    """
    Args:
        id_product (int): ID товара.

    Returns:
        dict | None: Возвращает словарь с данными товара или None, если товар не найден.
    """
    pass
```

**Описание**: Возвращает информацию о товаре из базы данных PrestaShop по его ID.

**Параметры**:
- `id_product` (int): ID товара.

**Возвращает**:
- `dict | None`: Возвращает словарь с данными товара или `None`, если товар не найден.