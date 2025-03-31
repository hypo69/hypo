# Модуль `pricelist`

## Обзор

Модуль `pricelist` предоставляет класс `PriceListRequester`, который используется для запроса и обновления цен товаров в PrestaShop. Он наследует функциональность базового класса `PrestaShop` из модуля `api`.

## Подробней

Этот модуль предназначен для работы с API PrestaShop с целью получения и обновления информации о ценах товаров. Он позволяет запрашивать цены для списка товаров, обновлять источник данных для цен и модифицировать цены отдельных товаров. Модуль использует библиотеку `requests` для выполнения HTTP-запросов к API PrestaShop и модуль `logger` для логирования событий.

## Классы

### `PriceListRequester`

**Описание**: Класс для запроса списка цен.

**Как работает класс**:
Класс `PriceListRequester` наследуется от класса `PrestaShop` и предназначен для работы с ценами товаров в PrestaShop. Он инициализируется с учетными данными API, необходимыми для аутентификации и выполнения запросов.

**Методы**:
- `__init__`: Инициализирует объект класса `PriceListRequester`.
- `request_prices`: Запрашивает список цен для указанных товаров.
- `update_source`: Обновляет источник данных для запроса цен.
- `modify_product_price`: Модифицирует цену указанного товара.

#### `__init__`

```python
def __init__(self, api_credentials):
    """
    Инициализирует объект класса PriceListRequester.

    @param api_credentials: Словарь с учетными данными для API,
                            включая 'api_domain' и 'api_key'.
    """
    super().__init__(api_credentials['api_domain'], api_credentials['api_key'])
```

**Описание**: Инициализирует объект класса `PriceListRequester`.

**Как работает функция**:
Конструктор класса принимает словарь `api_credentials`, содержащий учетные данные для доступа к API PrestaShop. Он вызывает конструктор родительского класса `PrestaShop`, передавая ему домен API и ключ API из `api_credentials`.

**Параметры**:
- `api_credentials` (словарь): Словарь с учетными данными для API, включая `'api_domain'` и `'api_key'`.

**Примеры**:
```python
api_credentials = {'api_domain': 'your_api_domain', 'api_key': 'your_api_key'}
pricelist_requester = PriceListRequester(api_credentials)
```

#### `request_prices`

```python
def request_prices(self, products):
    """
    Запрашивает список цен для указанных товаров.

    @param products: Список товаров, для которых требуется получить цены.
    @return: Словарь, где ключами являются товары, а значениями - их цены.
             Например: {'product1': 10.99, 'product2': 5.99}
    """
    # Здесь код для отправки запроса на получение цен из источника данных
    pass
```

**Описание**: Запрашивает список цен для указанных товаров.

**Как работает функция**:
Метод `request_prices` принимает список товаров (`products`) и должен возвращать словарь, где ключами являются названия товаров, а значениями - их цены. В текущей реализации метод не реализован и содержит только `pass`.

**Параметры**:
- `products` (список): Список товаров, для которых требуется получить цены.

**Возвращает**:
- Словарь: Словарь, где ключами являются товары, а значениями - их цены. Например: `{'product1': 10.99, 'product2': 5.99}`

**Примеры**:
```python
products = ['product1', 'product2', 'product3']
prices = pricelist_requester.request_prices(products)
print(prices)  # Ожидаемый результат: {'product1': 10.99, 'product2': 5.99, 'product3': 12.50}
```

#### `update_source`

```python
def update_source(self, new_source):
    """
    Обновляет источник данных для запроса цен.

    @param new_source: Новый источник данных.
    """
    self.source = new_source
```

**Описание**: Обновляет источник данных для запроса цен.

**Как работает функция**:
Метод `update_source` принимает новый источник данных (`new_source`) и присваивает его атрибуту `source` объекта `PriceListRequester`.

**Параметры**:
- `new_source`: Новый источник данных.

**Примеры**:
```python
new_source = 'new_data_source'
pricelist_requester.update_source(new_source)
print(pricelist_requester.source)  # Ожидаемый результат: new_data_source
```

#### `modify_product_price`

```python
def modify_product_price(self, product, new_price):
    """
    Модифицирует цену указанного товара.

    @param product: Название товара.
    @param new_price: Новая цена товара.
    """
    # Здесь код для изменения цены товара в источнике данных
    pass
```

**Описание**: Модифицирует цену указанного товара.

**Как работает функция**:
Метод `modify_product_price` принимает название товара (`product`) и новую цену (`new_price`) и должен изменять цену товара в источнике данных. В текущей реализации метод не реализован и содержит только `pass`.

**Параметры**:
- `product` (строка): Название товара.
- `new_price`: Новая цена товара.

**Примеры**:
```python
product = 'product1'
new_price = 12.99
pricelist_requester.modify_product_price(product, new_price)
```