# Модуль pricelist.py

## Обзор

Этот модуль предоставляет класс `PriceListRequester` для запроса и обновления цен продуктов из системы Престашоп. Класс наследуется от `PrestaShop` и содержит методы для запроса цен, обновления источника данных и изменения цен отдельных продуктов.

## Оглавление

- [Модуль pricelist.py](#модуль-pricelistpy)
- [Класс `PriceListRequester`](#класс-pricelistrequester)
    - [Метод `__init__`](#метод-init)
    - [Метод `request_prices`](#метод-request_prices)
    - [Метод `update_source`](#метод-update_source)
    - [Метод `modify_product_price`](#метод-modify_product_price)


## Класс `PriceListRequester`

### Описание

Класс `PriceListRequester` отвечает за взаимодействие с API Престашоп для получения, обновления и модификации цен продуктов.

### Метод `__init__`

```python
def __init__(self, api_credentials):
    """
    Инициализирует объект класса PriceListRequester.

    Args:
        api_credentials (dict): Словарь с учетными данными для API,
                                включая 'api_domain' и 'api_key'.
    """
    super().__init__(api_credentials['api_domain'], api_credentials['api_key'])
```

### Метод `request_prices`

```python
def request_prices(self, products):
    """
    Запрашивает список цен для указанных товаров.

    Args:
        products (list): Список товаров, для которых требуется получить цены.

    Returns:
        dict | None: Словарь, где ключами являются товары, а значениями - их цены.
                     Например: {'product1': 10.99, 'product2': 5.99}.
                     Возвращает None в случае ошибки.
    """
    # Здесь код для отправки запроса на получение цен из источника данных
    pass
```

### Метод `update_source`

```python
def update_source(self, new_source):
    """
    Обновляет источник данных для запроса цен.

    Args:
        new_source: Новый источник данных.
    """
    self.source = new_source
```

### Метод `modify_product_price`

```python
def modify_product_price(self, product, new_price):
    """
    Модифицирует цену указанного товара.

    Args:
        product (str): Название товара.
        new_price (float): Новая цена товара.
    """
    # Здесь код для изменения цены товара в источнике данных
    pass
```