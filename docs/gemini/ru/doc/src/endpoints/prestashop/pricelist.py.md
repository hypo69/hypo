# Модуль `pricelist`

## Обзор

Модуль `pricelist` предназначен для работы с запросами списка цен PrestaShop. Он включает в себя класс `PriceListRequester`, который позволяет запрашивать и обновлять цены товаров через API PrestaShop.

## Подробнее

Этот модуль предоставляет функциональность для интеграции с PrestaShop API, позволяя автоматизировать процесс получения и обновления цен товаров. Он использует класс `PrestaShop` из модуля `src.endpoints.prestashop.api` для взаимодействия с API PrestaShop. Модуль предназначен для работы как в Windows, так и в Unix-подобных операционных системах.

## Классы

### `PriceListRequester`

**Описание**: Класс `PriceListRequester` используется для запроса списка цен товаров из PrestaShop.

**Наследует**:
- `PrestaShop`: Наследует базовый класс для работы с API PrestaShop.

**Методы**:
- `__init__(self, api_credentials: Dict[str, str]) -> None`: Инициализирует объект класса `PriceListRequester`.
- `request_prices(self, products: List[str]) -> Dict[str, float]`: Запрашивает список цен для указанных товаров.
- `update_source(self, new_source: str) -> None`: Обновляет источник данных для запроса цен.
- `modify_product_price(self, product: str, new_price: float) -> None`: Модифицирует цену указанного товара.

#### `__init__`

```python
def __init__(self, api_credentials: Dict[str, str]) -> None:
    """
    Инициализирует объект класса PriceListRequester.

    Args:
        api_credentials (Dict[str, str]): Словарь с учетными данными для API,
            включая 'api_domain' и 'api_key'.

    Returns:
        None
    """
    ...
```

**Назначение**: Инициализирует объект класса `PriceListRequester`, принимая учетные данные API.

**Параметры**:
- `api_credentials` (Dict[str, str]): Словарь, содержащий учетные данные для API PrestaShop, включая `api_domain` и `api_key`.

**Как работает функция**:
1. Функция `__init__` принимает словарь `api_credentials`, содержащий домен API и ключ API.
2. Вызывает конструктор родительского класса `PrestaShop`, передавая ему `api_domain` и `api_key` для инициализации соединения с API PrestaShop.

#### `request_prices`

```python
def request_prices(self, products: List[str]) -> Dict[str, float]:
    """
    Запрашивает список цен для указанных товаров.

    Args:
        products (List[str]): Список товаров, для которых требуется получить цены.

    Returns:
        Dict[str, float]: Словарь, где ключами являются товары, а значениями - их цены.
            Например: {'product1': 10.99, 'product2': 5.99}
    """
    ...
```

**Назначение**: Запрашивает цены для списка товаров.

**Параметры**:
- `products` (List[str]): Список товаров, для которых необходимо получить цены.

**Возвращает**:
- `Dict[str, float]`: Словарь, где ключи - это названия товаров, а значения - их соответствующие цены.

**Как работает функция**:
1. Функция `request_prices` принимает список названий товаров `products`.
2. Отправляет запрос в источник данных для получения цен на указанные товары.
3. Формирует словарь, где ключами являются названия товаров, а значениями - их цены.
4. Возвращает полученный словарь.

#### `update_source`

```python
def update_source(self, new_source: str) -> None:
    """
    Обновляет источник данных для запроса цен.

    Args:
        new_source (str): Новый источник данных.

    Returns:
        None
    """
    ...
```

**Назначение**: Обновляет источник данных для запроса цен.

**Параметры**:
- `new_source` (str): Новый источник данных.

**Как работает функция**:
1. Функция `update_source` принимает новый источник данных `new_source`.
2. Обновляет атрибут `source` объекта класса `PriceListRequester` новым значением.

#### `modify_product_price`

```python
def modify_product_price(self, product: str, new_price: float) -> None:
    """
    Модифицирует цену указанного товара.

    Args:
        product (str): Название товара.
        new_price (float): Новая цена товара.

    Returns:
        None
    """
    ...
```

**Назначение**: Изменяет цену указанного товара в источнике данных.

**Параметры**:
- `product` (str): Название товара, цену которого необходимо изменить.
- `new_price` (float): Новая цена товара.

**Как работает функция**:
1. Функция `modify_product_price` принимает название товара `product` и новую цену `new_price`.
2. Выполняет операцию изменения цены товара в источнике данных (код не показан, обозначен как `...`).

## Функции

В данном модуле нет отдельных функций, не относящихся к классам.