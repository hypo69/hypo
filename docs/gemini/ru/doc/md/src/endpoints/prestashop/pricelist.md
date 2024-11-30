# Модуль `hypotez/src/endpoints/prestashop/pricelist.py`

## Обзор

Данный модуль предоставляет инструменты для работы со списком цен в системе PrestaShop.  Он реализует класс `PriceListRequester`, который наследуется от `PrestaShop` и предоставляет методы для запроса, обновления и изменения цен товаров.

## Классы

### `PriceListRequester`

**Описание**: Класс для запроса списка цен товаров из системы PrestaShop. Наследуется от класса `PrestaShop`.

**Методы**:

#### `__init__`

**Описание**: Инициализирует объект класса `PriceListRequester`.

**Параметры**:
- `api_credentials` (dict): Словарь с учетными данными для API, включая `api_domain` и `api_key`.

#### `request_prices`

**Описание**: Запрашивает список цен для указанных товаров.

**Параметры**:
- `products` (list): Список товаров, для которых требуется получить цены.

**Возвращает**:
- dict | None: Словарь, где ключами являются товары, а значениями — их цены. Возвращает `None` в случае ошибки.  Пример: `{\'product1\': 10.99, \'product2\': 5.99}`.

#### `update_source`

**Описание**: Обновляет источник данных для запроса цен.

**Параметры**:
- `new_source`: Новый источник данных.

#### `modify_product_price`

**Описание**: Модифицирует цену указанного товара.

**Параметры**:
- `product` (str): Название товара.
- `new_price` (float): Новая цена товара.


## Функции

(В данном модуле нет функций, только классы.)


## Модули

- `header`
- `gs`
- `src.logger`
- `src.utils.jjson`
- `.api`
- `types`

## Использование

```python
# Пример использования
from hypotez.src.endpoints.prestashop.pricelist import PriceListRequester

# Укажите ваши учетные данные
api_credentials = {
    'api_domain': 'ваш_домен',
    'api_key': 'ваш_ключ'
}

# Создайте экземпляр класса
price_list_requester = PriceListRequester(api_credentials)

# Список товаров
products_to_get_prices = ['product1', 'product2']

# Запрос цен
prices = price_list_requester.request_prices(products_to_get_prices)

# Обработка результата
if prices:
    for product, price in prices.items():
        print(f"Цена для {product}: {price}")
else:
    print("Ошибка при запросе цен.")


```

**Примечание:**  В примере кода заглушены (не реализованы) необходимые действия по отправке запросов на сервер PrestaShop.  Для корректной работы необходимо реализовать эти запросы в методе `request_prices`.