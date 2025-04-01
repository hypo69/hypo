# Модуль src.endpoints.prestashop.pricelist

## Обзор

Модуль `pricelist.py` предназначен для работы с ценами товаров в PrestaShop. Он включает в себя класс `PriceListRequester`, который позволяет запрашивать и обновлять цены товаров через API PrestaShop.

## Подробней

Этот модуль предоставляет функциональность для интеграции с PrestaShop API, позволяя автоматизировать процесс получения и обновления цен товаров. Класс `PriceListRequester` наследуется от класса `PrestaShop` и использует его методы для взаимодействия с API.

## Классы

### `PriceListRequester`

**Описание**:
Класс для запроса списка цен.

**Методы**:
- `__init__`: Инициализирует объект класса `PriceListRequester`.
- `request_prices`: Запрашивает список цен для указанных товаров.
- `update_source`: Обновляет источник данных для запроса цен.
- `modify_product_price`: Модифицирует цену указанного товара.

**Параметры**:
- `api_credentials` (словарь): Словарь с учетными данными для API, включая `'api_domain'` и `'api_key'`.
- `products` (список): Список товаров, для которых требуется получить цены.
- `new_source`: Новый источник данных.
- `product` (str): Название товара.
- `new_price`: Новая цена товара.

**Примеры**

```python
# Пример использования класса PriceListRequester
api_credentials = {'api_domain': 'your_api_domain', 'api_key': 'your_api_key'}
price_requester = PriceListRequester(api_credentials)
products = ['product1', 'product2']
prices = price_requester.request_prices(products)
print(prices)
```

## Функции

### `__init__`

```python
def __init__(self, api_credentials):
    """
    Инициализирует объект класса PriceListRequester.

    Args:
        api_credentials: Словарь с учетными данными для API,
                         включая 'api_domain' и 'api_key'.
    """
    ...
```

**Описание**:
Инициализирует объект класса `PriceListRequester`, вызывая конструктор родительского класса `PrestaShop`.

**Параметры**:
- `api_credentials` (словарь): Словарь с учетными данными для API, включая `'api_domain'` и `'api_key'`.

**Примеры**:

```python
api_credentials = {'api_domain': 'your_api_domain', 'api_key': 'your_api_key'}
price_requester = PriceListRequester(api_credentials)
```

### `request_prices`

```python
def request_prices(self, products):
    """
    Запрашивает список цен для указанных товаров.

    Args:
        products: Список товаров, для которых требуется получить цены.
    Returns:
        Словарь, где ключами являются товары, а значениями - их цены.
             Например: {'product1': 10.99, 'product2': 5.99}
    """
    ...
```

**Описание**:
Запрашивает список цен для указанных товаров. В текущей реализации отсутствует код для отправки запроса на получение цен из источника данных.

**Параметры**:
- `products` (список): Список товаров, для которых требуется получить цены.

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
    Обновляет источник данных для запроса цен.

    Args:
        new_source: Новый источник данных.
    """
    ...
```

**Описание**:
Обновляет источник данных для запроса цен.

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
    Модифицирует цену указанного товара.

    Args:
        product: Название товара.
        new_price: Новая цена товара.
    """
    ...
```

**Описание**:
Модифицирует цену указанного товара в источнике данных. В текущей реализации отсутствует код для изменения цены товара.

**Параметры**:
- `product` (str): Название товара.
- `new_price`: Новая цена товара.

**Примеры**:

```python
product = 'product1'
new_price = 12.99
price_requester.modify_product_price(product, new_price)