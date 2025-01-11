# Модуль `pricelist.py`

## Обзор

Модуль `pricelist.py` предназначен для запроса и управления ценами товаров в системе PrestaShop. Он включает в себя класс `PriceListRequester`, который наследуется от класса `PrestaShop` и предоставляет функциональность для получения, обновления и изменения цен товаров.

## Оглавление

1.  [Классы](#классы)
    *   [`PriceListRequester`](#pricelistrequester)
2.  [Функции](#функции)
    *   [`__init__`](#__init__)
    *   [`request_prices`](#request_prices)
    *   [`update_source`](#update_source)
    *   [`modify_product_price`](#modify_product_price)

## Классы

### `PriceListRequester`

**Описание**: Класс для запроса списка цен.

**Наследует**: `PrestaShop`

**Методы**:

*   [`__init__`](#__init__)
*   [`request_prices`](#request_prices)
*   [`update_source`](#update_source)
*   [`modify_product_price`](#modify_product_price)

## Функции

### `__init__`

**Описание**: Инициализирует объект класса `PriceListRequester`.

**Параметры**:

*   `api_credentials` (dict): Словарь с учетными данными для API, включая `'api_domain'` и `'api_key'`.

### `request_prices`

**Описание**: Запрашивает список цен для указанных товаров.

**Параметры**:

*   `products` (list): Список товаров, для которых требуется получить цены.

**Возвращает**:

*   `dict`: Словарь, где ключами являются товары, а значениями - их цены. Например: `{'product1': 10.99, 'product2': 5.99}`.

### `update_source`

**Описание**: Обновляет источник данных для запроса цен.

**Параметры**:

*   `new_source` (any): Новый источник данных.

### `modify_product_price`

**Описание**: Модифицирует цену указанного товара.

**Параметры**:

*   `product` (any): Название товара.
*   `new_price` (any): Новая цена товара.