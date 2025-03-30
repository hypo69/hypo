# Документация модуля `pricelist.py`

## Обзор

Модуль `pricelist.py` предназначен для работы с ценами товаров в PrestaShop. Он содержит класс `PriceListRequester`, который позволяет запрашивать и обновлять цены товаров, используя API PrestaShop. Этот модуль является частью подсистемы для интеграции с PrestaShop и предоставляет функциональность для получения актуальной информации о ценах.

## Подробней

Модуль `pricelist.py` содержит класс `PriceListRequester`, который наследуется от класса `PrestaShop`. Он используется для запроса списка цен товаров из PrestaShop. Класс инициализируется с учетными данными API, которые используются для аутентификации при запросах к API PrestaShop. Основная функциональность модуля включает запрос цен для указанных товаров, обновление источника данных для цен и модификацию цен товаров.

## Классы

### `PriceListRequester`

**Описание**: Класс для запроса списка цен.

**Методы**: 
- `__init__`: Инициализирует объект класса `PriceListRequester`.
- `request_prices`: Запрашивает список цен для указанных товаров.
- `update_source`: Обновляет источник данных для запроса цен.
- `modify_product_price`: Модифицирует цену указанного товара.

**Параметры**:
- `api_credentials` (dict): Словарь с учетными данными для API, включая `'api_domain'` и `'api_key'`.
- `products` (list): Список товаров, для которых требуется получить цены.
- `new_source`: Новый источник данных.
- `product` (str): Название товара.
- `new_price`: Новая цена товара.

**Примеры**
```python
# Пример инициализации класса PriceListRequester
api_credentials = {'api_domain': 'your_api_domain', 'api_key': 'your_api_key'}
price_requester = PriceListRequester(api_credentials)

# Пример запроса цен для списка товаров
products = ['product1', 'product2']
prices = price_requester.request_prices(products)
print(prices)

# Пример обновления источника данных
new_source = 'new_data_source'
price_requester.update_source(new_source)

# Пример изменения цены товара
product = 'product1'
new_price = 12.99
price_requester.modify_product_price(product, new_price)
```

## Функции

### `__init__`

```python
def __init__(self, api_credentials):
    """
    Args:
        api_credentials: Словарь с учетными данными для API,
                            включая 'api_domain' и 'api_key'.
    """
```

**Описание**: Инициализирует объект класса `PriceListRequester`.

**Параметры**:
- `api_credentials` (dict): Словарь с учетными данными для API, включая `'api_domain'` и `'api_key'`.

**Примеры**:
```python
api_credentials = {'api_domain': 'your_api_domain', 'api_key': 'your_api_key'}
price_requester = PriceListRequester(api_credentials)
```

### `request_prices`

```python
def request_prices(self, products):
    """
    Args:
        products: Список товаров, для которых требуется получить цены.
    Returns:
        Словарь, где ключами являются товары, а значениями - их цены.
        Например: {'product1': 10.99, 'product2': 5.99}
    """
```

**Описание**: Запрашивает список цен для указанных товаров.

**Параметры**:
- `products` (list): Список товаров, для которых требуется получить цены.

**Возвращает**:
- `dict`: Словарь, где ключами являются товары, а значениями - их цены.

**Примеры**:
```python
products = ['product1', 'product2']
prices = price_requester.request_prices(products)
print(prices)
```

### `update_source`

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

**Примеры**:
```python
new_source = 'new_data_source'
price_requester.update_source(new_source)
```

### `modify_product_price`

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
- `product` (str): Название товара.
- `new_price`: Новая цена товара.

**Примеры**:
```python
product = 'product1'
new_price = 12.99
price_requester.modify_product_price(product, new_price)
```