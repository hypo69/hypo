# Документация для `amazon_categories_laptops_lenovo.json`

## Оглавление

1.  [Обзор](#обзор)
2.  [Структура JSON](#структура-json)
    *   [store](#store)
    *   [scenarios](#scenarios)
        *   [LAPTOP LENOVO AMD ATHLON 13](#laptop-lenovo-amd-athlon-13)
        *   [LAPTOP LENOVO AMD RYZEN 3](#laptop-lenovo-amd-ryzen-3)
        *   [LAPTOP LENOVO AMD RYZEN 5](#laptop-lenovo-amd-ryzen-5)
        *   [LAPTOP LENOVO AMD RYZEN 7](#laptop-lenovo-amd-ryzen-7)
        *   [LAPTOP LENOVO INTEL CELERON](#laptop-lenovo-intel-celeron)
        *   [LAPTOP LENOVO INTEL I3](#laptop-lenovo-intel-i3)
        *   [LAPTOP LENOVO INTEL I5](#laptop-lenovo-intel-i5)
        *   [LAPTOP LENOVO INTEL I7](#laptop-lenovo-intel-i7)

## Обзор

Файл `amazon_categories_laptops_lenovo.json` содержит конфигурацию для сбора данных о ноутбуках Lenovo с сайта Amazon. Он включает в себя общую информацию о магазине и настройки для различных сценариев поиска ноутбуков, разделенных по процессорам и размерам.

## Структура JSON

JSON-файл состоит из двух основных секций: `store` и `scenarios`.

### `store`

Секция `store` содержит общую информацию о магазине Amazon, включая идентификаторы, описание, бренд и URL для поиска товаров.

*   `store_id` (str): Идентификатор магазина. В текущей версии пустая строка.
*   `supplier_id` (str): Идентификатор поставщика. В текущей версии пустая строка.
*   `get store banners` (bool): Флаг, указывающий на необходимость сбора баннеров магазина. В текущей версии установлено значение `true`.
*   `description` (str): Описание магазина, в данном случае "Lenovo laptops".
*   `about` (str): Краткое описание магазина, в данном случае "Lenovo laptops".
*   `brand` (str): Бренд товара, в данном случае "LENOVO".
*   `url` (str): URL-адрес для поиска ноутбуков Lenovo на Amazon.
*   `shop categories page` (str): URL-адрес страницы категорий магазина. В текущей версии пустая строка.
*   `shop categories json file` (str): Путь к JSON-файлу с категориями магазина. В текущей версии пустая строка.

### `scenarios`

Секция `scenarios` содержит наборы конфигураций для различных сценариев поиска ноутбуков Lenovo, классифицированных по типам процессоров и размерам. Каждый сценарий включает в себя:

*   `brand` (str): Бренд товара, в данном случае "LENOVO".
*   `url` (str): URL-адрес для поиска товаров по конкретному сценарию.
*   `active` (bool): Флаг, указывающий, активен ли данный сценарий для сбора данных.
*   `condition` (str): Состояние товара, в данном случае "new".
*    `presta_categories` (dict): Словарь, содержащий информацию о категориях для PrestaShop.
*   `checkbox` (bool): Флаг, в текущей версии всегда `false`.
*   `price_rule` (int): Правило ценообразования, в текущей версии всегда `1`.

#### `LAPTOP LENOVO AMD ATHLON 13`

**Описание**: Конфигурация для поиска ноутбуков Lenovo с процессором AMD Athlon и размером экрана 13 дюймов.

**Параметры**:
*   `brand` (str): "LENOVO".
*   `url` (str): URL-адрес для поиска ноутбуков Lenovo с процессором AMD Athlon и экраном 13 дюймов на Amazon.
*   `active` (bool): `true`.
*   `condition` (str): "new".
*    `presta_categories` (dict): 
    ```json
    {
        "template": {
            "lenovo": [
            "LAPTOPS AMD ATHLON",
             "13"
            ]
        }
    }
    ```
*   `checkbox` (bool): `false`.
*   `price_rule` (int): `1`.

#### `LAPTOP LENOVO AMD RYZEN 3`

**Описание**: Конфигурация для поиска ноутбуков Lenovo с процессором AMD Ryzen 3.

**Параметры**:
*   `brand` (str): "LENOVO".
*   `url` (str): URL-адрес для поиска ноутбуков Lenovo с процессором AMD Ryzen 3 на Amazon.
*   `active` (bool): `true`.
*   `condition` (str): "new".
*    `presta_categories` (dict): 
    ```json
    {
        "template": {
            "lenovo": "LAPTOPS AMD RYZEN 3"
        }
    }
    ```
*   `checkbox` (bool): `false`.
*   `price_rule` (int): `1`.

#### `LAPTOP LENOVO AMD RYZEN 5`

**Описание**: Конфигурация для поиска ноутбуков Lenovo с процессором AMD Ryzen 5.

**Параметры**:
*   `brand` (str): "LENOVO".
*   `url` (str): URL-адрес для поиска ноутбуков Lenovo с процессором AMD Ryzen 5 на Amazon.
*   `active` (bool): `true`.
*   `condition` (str): "new".
*    `presta_categories` (dict): 
    ```json
    {
        "template": {
            "lenovo": "LAPTOPS AMD RYZEN 5"
        }
    }
    ```
*   `checkbox` (bool): `false`.
*   `price_rule` (int): `1`.

#### `LAPTOP LENOVO AMD RYZEN 7`

**Описание**: Конфигурация для поиска ноутбуков Lenovo с процессором AMD Ryzen 7.

**Параметры**:
*   `brand` (str): "LENOVO".
*   `url` (str): URL-адрес для поиска ноутбуков Lenovo с процессором AMD Ryzen 7 на Amazon.
*   `active` (bool): `true`.
*   `condition` (str): "new".
*    `presta_categories` (dict): 
    ```json
    {
        "template": {
            "lenovo": "LAPTOPS AMD RYZEN 7"
        }
    }
    ```
*   `checkbox` (bool): `false`.
*   `price_rule` (int): `1`.

#### `LAPTOP LENOVO INTEL CELERON`

**Описание**: Конфигурация для поиска ноутбуков Lenovo с процессором Intel Celeron.

**Параметры**:
*   `brand` (str): "LENOVO".
*   `url` (str): URL-адрес для поиска ноутбуков Lenovo с процессором Intel Celeron на Amazon.
*   `active` (bool): `true`.
*   `condition` (str): "new".
*    `presta_categories` (dict): 
    ```json
    {
        "template": {
            "lenovo": "LAPTOPS INTEL CELERON"
        }
    }
    ```
*   `checkbox` (bool): `false`.
*   `price_rule` (int): `1`.

#### `LAPTOP LENOVO INTEL I3`

**Описание**: Конфигурация для поиска ноутбуков Lenovo с процессором Intel i3.

**Параметры**:
*   `brand` (str): "LENOVO".
*   `url` (str): URL-адрес для поиска ноутбуков Lenovo с процессором Intel i3 на Amazon.
*   `active` (bool): `true`.
*   `condition` (str): "new".
*    `presta_categories` (dict): 
    ```json
    {
        "template": {
            "lenovo": "LAPTOPS INTEL I3"
        }
    }
    ```
*   `checkbox` (bool): `false`.
*   `price_rule` (int): `1`.

#### `LAPTOP LENOVO INTEL I5`

**Описание**: Конфигурация для поиска ноутбуков Lenovo с процессором Intel i5.

**Параметры**:
*   `brand` (str): "LENOVO".
*   `url` (str): URL-адрес для поиска ноутбуков Lenovo с процессором Intel i5 на Amazon.
*   `active` (bool): `true`.
*   `condition` (str): "new".
*    `presta_categories` (dict): 
    ```json
    {
        "template": {
            "lenovo": "LAPTOPS INTEL I5"
        }
    }
    ```
*   `checkbox` (bool): `false`.
*   `price_rule` (int): `1`.

#### `LAPTOP LENOVO INTEL I7`

**Описание**: Конфигурация для поиска ноутбуков Lenovo с процессором Intel i7.

**Параметры**:
*   `brand` (str): "LENOVO".
*   `url` (str): URL-адрес для поиска ноутбуков Lenovo с процессором Intel i7 на Amazon.
*   `active` (bool): `true`.
*   `condition` (str): "new".
*    `presta_categories` (dict): 
    ```json
    {
        "template": {
            "lenovo": "LAPTOPS INTEL I7"
        }
    }
    ```
*   `checkbox` (bool): `false`.
*   `price_rule` (int): `1`.