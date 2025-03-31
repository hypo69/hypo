# Модуль `pricelist.py`

## Обзор

Модуль `pricelist.py` предназначен для запроса и управления ценами товаров в PrestaShop. Он включает класс `PriceListRequester`, который обеспечивает функциональность для получения цен товаров, обновления источника данных и модификации цен товаров.

## Содержание

1. [Классы](#Классы)
    - [`PriceListRequester`](#PriceListRequester)
2. [Импорты](#Импорты)

## Классы

### `PriceListRequester`

**Описание**: Класс для запроса списка цен. Наследуется от класса `PrestaShop`.

**Методы**:

- `__init__`: Инициализирует объект класса `PriceListRequester`.
- `request_prices`: Запрашивает список цен для указанных товаров.
- `update_source`: Обновляет источник данных для запроса цен.
- `modify_product_price`: Модифицирует цену указанного товара.

#### `__init__`

```python
def __init__(self, api_credentials):
    """
    Args:
        api_credentials (dict): Словарь с учетными данными для API, включая 'api_domain' и 'api_key'.
    """
```

**Описание**: Инициализирует объект класса `PriceListRequester`.

**Параметры**:

- `api_credentials` (dict): Словарь с учетными данными для API, включая `api_domain` и `api_key`.

#### `request_prices`

```python
def request_prices(self, products):
    """
    Args:
        products (list): Список товаров, для которых требуется получить цены.

    Returns:
        dict: Словарь, где ключами являются товары, а значениями - их цены.
              Например: {'product1': 10.99, 'product2': 5.99}
    """
```

**Описание**: Запрашивает список цен для указанных товаров.

**Параметры**:

- `products` (list): Список товаров, для которых требуется получить цены.

**Возвращает**:

- `dict`: Словарь, где ключами являются товары, а значениями - их цены. Например: `{'product1': 10.99, 'product2': 5.99}`.

#### `update_source`

```python
def update_source(self, new_source):
    """
    Args:
        new_source: Новый источник данных.
    """
```

**Описание**: Обновляет источник данных для запроса цен.

**Параметры**:

- `new_source`: Новый источник данных.

#### `modify_product_price`

```python
def modify_product_price(self, product, new_price):
    """
    Args:
        product: Название товара.
        new_price: Новая цена товара.
    """
```

**Описание**: Модифицирует цену указанного товара.

**Параметры**:

- `product`: Название товара.
- `new_price`: Новая цена товара.

## Импорты

Модуль импортирует следующие модули:

- `sys`
- `os`
- `attr`, `attrs` из `attr`
- `Path` из `pathlib`
- `Union` из `typing`
- `header`
- `gs` из `src`
- `logger` из `src.logger.logger`
- `j_loads`, `j_loads_ns` из `src.utils.jjson`
- `PrestaShop` из `.api`
- `SimpleNamespace` из `types`